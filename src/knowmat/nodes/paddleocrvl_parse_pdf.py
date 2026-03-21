"""
PDF parsing node using PaddleOCR-VL (with PaddleOCR fallback).
"""

from __future__ import annotations

import json
import logging
import os
import shutil
import tempfile
from concurrent.futures import Future, ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, List, Tuple

from knowmat.pdf.blocks import block_to_item, text_to_paragraph_items
from knowmat.pdf.block_filter import filter_figure_internal_fragments
from knowmat.pdf.doi_extractor import extract_doi_from_pdf_metadata, extract_first_doi
from knowmat.pdf.html_cleaner import convert_html_to_markdown
from knowmat.pdf.table_structure import (
    reocr_chem_formula_blocks,
    release_ppstructurev3_pipeline,
    route_and_reocr,
)
from knowmat.pdf.ocr_engine import (
    collect_text,
    create_ocr_engine,
    default_model_dir,
    normalize_lines,
    run_ocr_batch,
    run_ocr_parallel,
    supports_batch_predict,
    try_release_paddle_gpu_memory,
)
from knowmat.pdf.section_normalizer import (
    normalize_alloy_strings,
    strip_references_section,
    structure_sections,
)
from knowmat.app_config import settings
from knowmat.states import KnowMatState

logger = logging.getLogger(__name__)

_MAX_RENDER_WORKERS = 4
_OCR_MAX_WORKERS_DEFAULT = 1

# Block labels that represent layout noise (headers, footers, sidebars).
# These are excluded from the main text flow but still stored in ocr_items
# with their block_label so downstream code can inspect them if needed.
_LAYOUT_NOISE_LABELS = frozenset(
    {
        "header",
        "footer",
        "header_image",
        "footer_image",
        "aside_text",
        "number",
        "footnote",
    }
)

# Fraction of page width/height used as sidebar heuristic when block_label
# is not available (x_start < _SIDEBAR_X_FRAC * page_width).
_SIDEBAR_X_FRAC = 0.15
# Fraction of page height for header/footer bbox heuristic.
_HEADER_Y_FRAC = 0.08
_FOOTER_Y_FRAC = 0.92


def _env_truthy(name: str) -> bool:
    v = os.getenv(name, "").strip().lower()
    return v in ("1", "true", "yes", "on")


def _render_page(args: Tuple[str, int, int, str]) -> Path:
    import fitz  # type: ignore

    pdf_path_str, page_idx, dpi, image_dir_str = args
    image_dir = Path(image_dir_str)
    pdf_stem = Path(pdf_path_str).stem
    image_path = image_dir / f"{pdf_stem}-page-{page_idx:04d}.png"

    doc = fitz.open(pdf_path_str)
    try:
        page = doc[page_idx - 1]
        page.get_pixmap(dpi=dpi, alpha=False).save(str(image_path))
    finally:
        doc.close()
    return image_path


def _save_ocr_json(raw: Any, dest: Path) -> None:
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(raw, f, ensure_ascii=False, indent=2, default=str)


def _export_tables_to_csv(ocr_items: List[Dict[str, Any]], tables_dir: Path) -> None:
    """Export structured table items to CSV files for traceability.

    Each table item with successfully parsed rows is written to
    ``tables_dir/page{page}-table{n}.csv``.  Items where structure parsing
    failed still carry ``data.raw_html`` in the JSON output for later
    reprocessing.
    """
    import csv

    table_items = [it for it in ocr_items if it.get("typer") == "table"]
    if not table_items:
        return

    tables_dir.mkdir(parents=True, exist_ok=True)
    counters: Dict[int, int] = {}
    for item in table_items:
        page = item.get("page", 0)
        counters[page] = counters.get(page, 0) + 1
        n = counters[page]
        data = item.get("data", {})
        structured = data if isinstance(data, dict) and "rows" in data else None
        if structured is None:
            continue
        rows = structured.get("rows", [])
        columns = [c["name"] for c in structured.get("columns", [])]
        if not rows or not columns:
            continue
        csv_path = tables_dir / f"page{page:04d}-table{n:02d}.csv"
        try:
            with open(csv_path, "w", newline="", encoding="utf-8") as fh:
                writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
                writer.writeheader()
                writer.writerows(rows)
        except OSError as exc:
            logger.warning("Failed to write table CSV %s: %s", csv_path, exc)


def _extract_pdf_with_paddleocrvl(
    pdf_path: str, output_dir: str, model_dir: Path, save_intermediate: bool = True
) -> Tuple[str, Dict[str, Any], List[Dict[str, Any]]]:
    try:
        import fitz  # type: ignore
    except ImportError as exc:
        raise ImportError("PyMuPDF is required for PaddleOCR parsing. Install with: pip install pymupdf") from exc

    pdf = Path(pdf_path)
    out_dir = Path(output_dir)
    temp_pdf_ctx = None
    work_pdf = pdf
    if not all(ord(c) < 128 for c in pdf_path):
        temp_pdf_ctx = tempfile.TemporaryDirectory()
        work_pdf = Path(temp_pdf_ctx.name) / "source.pdf"
        shutil.copy2(pdf_path, work_pdf)

    temp_dir = None
    if save_intermediate:
        image_dir = out_dir / "page_images"
        raw_dir = out_dir / "ocr_raw"
        image_dir.mkdir(parents=True, exist_ok=True)
        raw_dir.mkdir(parents=True, exist_ok=True)
    else:
        temp_dir = tempfile.TemporaryDirectory()
        image_dir = Path(temp_dir.name)
        raw_dir = None

    engine: Any = None
    backend = ""
    try:
        engine, backend = create_ocr_engine(model_dir=model_dir)
        header_lines = 5
        footer_lines = 3

        doc = fitz.open(str(work_pdf))
        total_pages = len(doc)
        first_page_pymupdf_text = doc[0].get_text("text") if total_pages > 0 else ""
        doc.close()

        render_dpi = int(os.getenv("OCR_RENDER_DPI", "300"))
        if render_dpi < 72 or render_dpi > 600:
            logger.warning("OCR_RENDER_DPI=%s out of range [72,600]; using 300.", render_dpi)
            render_dpi = 300
        render_args = [(str(work_pdf), idx, render_dpi, str(image_dir)) for idx in range(1, total_pages + 1)]
        num_workers = min(_MAX_RENDER_WORKERS, max(1, os.cpu_count() or 1), total_pages)
        with ThreadPoolExecutor(max_workers=num_workers) as render_pool:
            image_paths: List[Path] = list(render_pool.map(_render_page, render_args))

        page_blocks: List[str] = []
        page_level_meta: List[Dict[str, Any]] = []
        ocr_items: List[Dict[str, Any]] = []
        first_page_full_text = first_page_pymupdf_text
        bg_futures: List[Future] = []
        vl_results: List[Any] = []

        if supports_batch_predict(engine):
            batch_size = int(os.getenv("OCR_BATCH_SIZE", "2"))
            if batch_size < 1:
                batch_size = 1
            logger.info("Using batch OCR inference (batch_size=%d) for %d pages...", batch_size, len(image_paths))
            raw_results = run_ocr_batch(engine, image_paths, batch_size)
            logger.info("✓ OCR batch inference completed.")
        else:
            max_ocr_workers = int(os.getenv("OCR_MAX_WORKERS", str(_OCR_MAX_WORKERS_DEFAULT)))
            logger.info("Using parallel OCR inference (workers=%d) for %d pages...", max_ocr_workers, len(image_paths))
            raw_results = run_ocr_parallel(engine, image_paths, max_ocr_workers)
            logger.info("✓ OCR parallel inference completed.")

        with ThreadPoolExecutor(max_workers=2) as bg_io_pool:
            try:
                for page_idx, raw in enumerate(raw_results, start=1):
                    if raw is not None and raw_dir is not None:
                        dest = raw_dir / f"page-{page_idx:04d}.json"
                        bg_futures.append(bg_io_pool.submit(_save_ocr_json, raw, dest))

                    if backend == "paddleocrvl":
                        if raw is not None:
                            if isinstance(raw, list):
                                vl_results.extend(raw)
                            else:
                                vl_results.append(raw)
                    else:
                        lines: List[str] = []
                        collect_text(raw, lines)
                        lines = normalize_lines(lines)
                        if not lines:
                            doc = fitz.open(str(work_pdf))
                            try:
                                fallback = doc[page_idx - 1].get_text("text")
                            finally:
                                doc.close()
                            lines = [x.strip() for x in fallback.splitlines() if x.strip()]

                        page_text = convert_html_to_markdown("\n".join(lines).strip())
                        page_blocks.append(f"## Page {page_idx}\n\n{page_text}")
                        page_level_meta.append(
                            {
                                "page": page_idx,
                                "header_text": "\n".join(lines[:header_lines]),
                                "footer_text": "\n".join(lines[-footer_lines:]) if len(lines) >= footer_lines else "",
                                "line_count": len(lines),
                            }
                        )
                    if page_idx == 1:
                        first_page_full_text = first_page_pymupdf_text if backend == "paddleocrvl" else page_text + "\n" + first_page_pymupdf_text
            finally:
                for fut in bg_futures:
                    fut.result()

            if backend == "paddleocrvl" and vl_results:
                logger.info("Starting restructure_pages for layout analysis...")
                try:
                    # markdown_ignore_labels aligned with StarRiver model_settings.
                    _ignore_labels = list(_LAYOUT_NOISE_LABELS)
                    restructure_kwargs: Dict[str, Any] = {
                        "merge_tables": True,
                        "relevel_titles": True,
                        "concatenate_pages": True,
                    }
                    try:
                        restructured = engine.restructure_pages(
                            vl_results, markdown_ignore_labels=_ignore_labels, **restructure_kwargs
                        )
                    except TypeError:
                        restructured = engine.restructure_pages(vl_results, **restructure_kwargs)
                    restructured = list(restructured)
                    logger.info("✓ restructure_pages completed: %d pages", len(restructured))
                except (RuntimeError, ValueError, TypeError) as exc:
                    logger.warning("restructure_pages failed for %s: %s", pdf, exc, exc_info=True)
                    restructured = []

                for idx, res in enumerate(restructured, start=1):
                    try:
                        md_info = res._to_markdown(pretty=True, show_formula_number=False)
                        page_text = md_info.get("markdown_texts", "")
                    except (AttributeError, TypeError, KeyError) as exc:
                        logger.warning("_to_markdown failed for page %d of %s: %s", idx, pdf, exc)
                        page_text = ""
                    page_text = convert_html_to_markdown(page_text)
                    if page_text:
                        page_blocks.append(page_text)

                    lines = [ln for ln in page_text.splitlines() if ln.strip()]
                    page_level_meta.append(
                        {
                            "page": idx,
                            "header_text": "\n".join(lines[:header_lines]),
                            "footer_text": "\n".join(lines[-footer_lines:]) if len(lines) >= footer_lines else "",
                            "line_count": len(lines),
                        }
                    )

                    try:
                        blocks = res["parsing_res_list"]
                    except (KeyError, TypeError, IndexError):
                        blocks = getattr(res, "parsing_res_list", [])
                    for block in blocks or []:
                        blabel = (
                            block.get("block_label")
                            if isinstance(block, dict)
                            else getattr(block, "block_label", None)
                        )
                        bbox = (
                            block.get("block_bbox")
                            if isinstance(block, dict)
                            else getattr(block, "block_bbox", None)
                        )
                        is_noise = blabel in _LAYOUT_NOISE_LABELS
                        item = block_to_item(block)
                        if item:
                            item["page"] = idx
                            if bbox is not None:
                                item["bbox"] = bbox
                            if blabel is not None:
                                item["block_label"] = blabel
                            if is_noise:
                                item["is_layout_noise"] = True
                            ocr_items.append(item)

        merged = "\n\n".join(page_blocks).strip()
        if not ocr_items and merged:
            ocr_items = text_to_paragraph_items(merged)

        # Filter paragraph fragments that lie inside figure/image bounding boxes.
        if ocr_items:
            try:
                ocr_items, n_removed = filter_figure_internal_fragments(ocr_items)
                if n_removed:
                    logger.info("Removed %d figure-internal fragment(s) from %s", n_removed, pdf)
            except Exception as exc:
                logger.warning("filter_figure_internal_fragments failed: %s", exc, exc_info=True)

        # PP-Structure layout routing and region-level re-OCR.
        if backend == "paddleocrvl" and ocr_items and not _env_truthy("KNOWMAT_SKIP_PPSTRUCTURE_REFINE"):
            logger.info("Starting PP-StructureV3 refinement for tables and formulas...")
            page_images_map: Dict[int, Path] = {
                i + 1: p for i, p in enumerate(image_paths)
            }
            reocr_work_dir = out_dir if save_intermediate else Path(image_dir)
            try:
                ocr_items = route_and_reocr(
                    ocr_items,
                    str(work_pdf),
                    page_images_map,
                    engine,
                    reocr_work_dir,
                )
                logger.info("✓ PP-StructureV3 table/formula refinement completed.")
            except Exception as exc:
                logger.warning("route_and_reocr failed: %s", exc, exc_info=True)
            if not _env_truthy("KNOWMAT_SKIP_CHEM_REOCR"):
                try:
                    ocr_items = reocr_chem_formula_blocks(
                        ocr_items,
                        str(work_pdf),
                        page_images_map,
                        engine,
                        reocr_work_dir,
                    )
                    logger.info("✓ Chemical formula re-OCR completed.")
                except Exception as exc:
                    logger.warning("reocr_chem_formula_blocks failed: %s", exc, exc_info=True)
            else:
                logger.info("KNOWMAT_SKIP_CHEM_REOCR set: skipping chemical formula crop re-OCR.")
        elif backend == "paddleocrvl" and ocr_items and _env_truthy("KNOWMAT_SKIP_PPSTRUCTURE_REFINE"):
            logger.info(
                "KNOWMAT_SKIP_PPSTRUCTURE_REFINE set: skipping PP-StructureV3 refinement and chem re-OCR."
            )

        doi = extract_doi_from_pdf_metadata(str(work_pdf)) or extract_first_doi(first_page_full_text)

        # Export structured tables to CSV for traceability.
        if save_intermediate and raw_dir is not None:
            tables_dir = out_dir / "tables"
            _export_tables_to_csv(ocr_items, tables_dir)

        metadata = {
            "backend": backend,
            "model_dir": str(model_dir),
            "pages": len(page_blocks),
            "image_dir": str(image_dir),
            "ocr_raw_dir": str(raw_dir) if raw_dir is not None else None,
            "doi": doi,
            "page_level_metadata": page_level_meta,
            "ocr_items": len(ocr_items),
        }
        return merged, metadata, ocr_items
    finally:
        if engine is not None:
            del engine
        release_ppstructurev3_pipeline()
        try_release_paddle_gpu_memory()
        if temp_dir is not None:
            temp_dir.cleanup()
        if temp_pdf_ctx is not None:
            temp_pdf_ctx.cleanup()


def _read_txt_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def parse_pdf_with_paddleocrvl(state: KnowMatState) -> dict:
    input_path = state.get("pdf_path")
    if not input_path:
        raise ValueError("No input file path provided in state for parse_pdf_with_paddleocrvl node.")
    save_intermediate = bool(state.get("save_intermediate", True))
    output_dir = state.get("output_dir", ".")
    source_path = Path(input_path)
    suffix = source_path.suffix.lower()

    if suffix in (".txt", ".md"):
        parse_output_dir = Path(output_dir) / "txt_parse" if save_intermediate else Path(output_dir)
        if save_intermediate:
            parse_output_dir.mkdir(parents=True, exist_ok=True)

        raw_text = _read_txt_file(source_path)
        md_text = structure_sections(convert_html_to_markdown(raw_text))
        md_text = normalize_alloy_strings(md_text)
        cleaned_text = (
            strip_references_section(md_text) if settings.trim_references_section else md_text
        )
        stem = source_path.stem

        doi = extract_first_doi(cleaned_text[:5000])
        if doi and doi not in cleaned_text:
            cleaned_text = f"DOI: {doi}\n\n{cleaned_text}"

        if save_intermediate:
            final_md_path = parse_output_dir / f"{stem}_final_output.md"
            with open(final_md_path, "w", encoding="utf-8") as f:
                f.write(cleaned_text)
            print(f"Saved txt parsed output to: {final_md_path}")

        doc_meta: Dict[str, Any] = {"backend": "txt-direct", "source_file": str(source_path), "doi": doi}
        if save_intermediate:
            meta_path = parse_output_dir / f"{stem}_parse_metadata.json"
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(doc_meta, f, ensure_ascii=False, indent=2)
            print(f"Saved parser metadata to: {meta_path}")
        return {"paper_text": cleaned_text, "document_metadata": doc_meta, "ocr_items": text_to_paragraph_items(cleaned_text)}

    if suffix != ".pdf":
        raise ValueError(f"Unsupported file type: {source_path.suffix}. Only .pdf, .txt, and .md are supported.")
    parse_output_dir = Path(output_dir) / "paddleocrvl_parse" if save_intermediate else Path(output_dir)
    if save_intermediate:
        parse_output_dir.mkdir(parents=True, exist_ok=True)
    model_dir = default_model_dir()

    try:
        extracted_text, metadata, _ocr_items = _extract_pdf_with_paddleocrvl(
            str(source_path), str(parse_output_dir), model_dir, save_intermediate=save_intermediate
        )
        structured_text = structure_sections(extracted_text)
        structured_text = normalize_alloy_strings(structured_text)
        cleaned_text = (
            strip_references_section(structured_text)
            if settings.trim_references_section
            else structured_text
        )
        doi_from_ocr = metadata.get("doi")
        if doi_from_ocr and doi_from_ocr not in cleaned_text:
            cleaned_text = f"DOI: {doi_from_ocr}\n\n{cleaned_text}"

        pdf_name = source_path.stem
        if save_intermediate:
            final_md_path = parse_output_dir / f"{pdf_name}_final_output.md"
            with open(final_md_path, "w", encoding="utf-8") as f:
                f.write(cleaned_text)
            print(f"Saved final markdown output to: {final_md_path}")

        doc_meta = {
            "backend": metadata.get("backend", "paddleocrvl"),
            "model_dir": metadata.get("model_dir"),
            "pages": metadata.get("pages"),
            "doi": doi_from_ocr,
            "page_level_metadata": metadata.get("page_level_metadata"),
        }
        if save_intermediate:
            meta_path = parse_output_dir / f"{pdf_name}_parse_metadata.json"
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)
            print(f"Saved parser metadata to: {meta_path}")
        return {"paper_text": cleaned_text, "document_metadata": doc_meta, "ocr_items": _ocr_items or text_to_paragraph_items(cleaned_text)}
    except Exception as exc:
        raise RuntimeError(f"Failed to parse PDF with PaddleOCR-VL: {str(exc)}") from exc






