from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def norm_text(text: Any) -> str:
    s = str(text or "").strip().lower()
    s = (
        s.replace("–", "-")
        .replace("—", "-")
        .replace("γ", "gamma")
        .replace("η", "eta")
        .replace(" ", " ")
        .replace("μ", "u")
        .replace("×", "x")
        .replace("_", " ")
    )
    s = re.sub(r"\s+", " ", s)
    return s


def slug(text: Any) -> str:
    s = norm_text(text)
    return re.sub(r"[^a-z0-9\-\+\.\(\) ]", "", s)


def similarity(a: Any, b: Any) -> float:
    return SequenceMatcher(None, slug(a), slug(b)).ratio()


def paper_title(doc: dict[str, Any]) -> str:
    meta = doc.get("Paper_Metadata") or doc.get("paper_metadata") or {}
    return meta.get("Paper_Title") or meta.get("paper_title") or ""


def item_sample_id(item: dict[str, Any]) -> str:
    return item.get("Sample_ID") or item.get("sample_id") or ""


def item_role(item: dict[str, Any]) -> str:
    comp = item.get("Composition_Info") or {}
    return norm_text(comp.get("Role"))


def item_alloy_name(item: dict[str, Any]) -> str:
    comp = item.get("Composition_Info") or {}
    return comp.get("Alloy_Name_Raw") or ""


def item_gradient(item: dict[str, Any]) -> Any:
    return item.get("Gradient_Material")


def item_process_category(item: dict[str, Any]) -> str:
    proc = item.get("Process_Info") or {}
    return proc.get("Process_Category") or ""


def item_key_params(item: dict[str, Any]) -> dict[str, Any]:
    proc = item.get("Process_Info") or {}
    return proc.get("Key_Params") or {}


def item_micro(item: dict[str, Any]) -> dict[str, Any]:
    return item.get("Microstructure_Info") or {}


def item_aqf(item: dict[str, Any]) -> dict[str, Any]:
    return item_micro(item).get("Advanced_Quantitative_Features") or {}


def item_main_phase(item: dict[str, Any]) -> Any:
    return item_micro(item).get("Main_Phase")


def item_property_names(item: dict[str, Any]) -> set[str]:
    names: set[str] = set()
    for prop in item.get("Properties_Info") or []:
        if isinstance(prop, dict):
            name = prop.get("Property_Name") or prop.get("property_name")
            if name:
                names.add(str(name))
    return names


def composition_block(item: dict[str, Any]) -> dict[str, Any]:
    comp = item.get("Composition_Info") or {}
    measured = comp.get("Measured_Composition") or {}
    nominal = comp.get("Nominal_Composition") or {}
    if isinstance(measured, dict) and measured.get("Elements_Normalized"):
        return {
            "basis": "measured",
            "type": measured.get("Composition_Type"),
            "elements": measured.get("Elements_Normalized") or {},
        }
    return {
        "basis": "nominal" if nominal else None,
        "type": nominal.get("Composition_Type") if isinstance(nominal, dict) else None,
        "elements": nominal.get("Elements_Normalized") if isinstance(nominal, dict) else {},
    }


def normalize_sample_id(sample_id: Any) -> str:
    return slug(sample_id).replace(" ", "")


def normalize_process_category(text: Any) -> str:
    value = slug(text)
    replacements = {
        "laser powder bed fusion (lpbf)": "laser powder bed fusion",
        "laser powder bed fusion (pbf-lb)": "laser powder bed fusion",
        "selective laser melting (slm)": "laser powder bed fusion",
        "selective laser melting": "laser powder bed fusion",
        "lpbf": "laser powder bed fusion",
        "electron beam powder bed fusion (pbf-eb)": "electron beam powder bed fusion",
        "electron beam powder bed fusion": "electron beam powder bed fusion",
        "electron beam melting (ebm)": "electron beam melting",
        "electron beam melting": "electron beam melting",
        "additive manufacturing - electron beam melting": "electron beam melting",
        "laser-aided additive manufacturing (laam)": "directed energy deposition",
        "directed energy deposition (ded)": "directed energy deposition",
        "laam": "directed energy deposition",
        "ded": "directed energy deposition",
        "powder metallurgy": "powder metallurgy",
        "wrought": "wrought",
        "laser glazing": "laser glazing",
        "hot isostatic pressing": "hot isostatic pressing",
        "high-energy ball milling": "high-energy ball milling",
        "additive manufacturing": "additive manufacturing",
    }
    for src, dst in sorted(replacements.items(), key=lambda kv: -len(kv[0])):
        if value == src:
            value = dst
            break
    for suffix in (
        " + heat treatment",
        " + annealing",
        " + thermal stabilization",
        " + aging",
        " + solution treatment",
    ):
        if value.endswith(suffix):
            value = value[: -len(suffix)]
    return value.strip()


def normalize_param_key(key: Any) -> str:
    value = slug(key).replace(" ", "_")
    aliases = {
        "hatch_distance_mm": "hatch_spacing_mm",
        "hatch_distance_um": "hatch_spacing_um",
        "line_offset_mm": "hatch_spacing_mm",
        "pre_heating_temperature_c": "build_plate_temperature_k",
        "preheating_temperature_k": "powder_bed_preheating_temperature_k",
        "building_temperature_c": "building_temperature_k",
        "powder_recycling_cycles": "recycling_cycles",
        "beam_current_ma": "mean_beam_current_ma",
        "voltage_kv": "acceleration_voltage_kv",
        "beam_diameter_um": "spot_size_um",
        "gnd_density_m2": "dislocation_density_m2",
        "dislocation_density_m_minus_2": "dislocation_density_m2",
    }
    return aliases.get(value, value)


def to_number(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        text = (
            value.replace("−", "-")
            .replace("×10^", "e")
            .replace("×10", "e")
            .replace("x10^", "e")
            .replace("10⁻³", "1e-3")
        )
        match = re.search(r"-?\d+(?:\.\d+)?(?:e[+-]?\d+)?", text.lower())
        if match:
            try:
                return float(match.group(0))
            except ValueError:
                return None
    return None


def values_equivalent(key: Any, gt_value: Any, pred_value: Any) -> bool:
    gt_num = to_number(gt_value)
    pred_num = to_number(pred_value)
    if gt_num is None or pred_num is None:
        return slug(gt_value) == slug(pred_value)
    normalized_key = normalize_param_key(key)
    if normalized_key in {"layer_thickness_um", "hatch_spacing_um", "spot_size_um"}:
        return (
            abs(gt_num - pred_num) < 1e-6
            or abs(gt_num * 1000 - pred_num) < 1e-3
            or abs(gt_num - pred_num * 1000) < 1e-3
        )
    if normalized_key in {
        "build_plate_temperature_k",
        "aging_temperature_k",
        "building_temperature_k",
        "powder_bed_preheating_temperature_k",
    }:
        return (
            abs(gt_num - pred_num) <= 1.5
            or abs((gt_num + 273.15) - pred_num) <= 1.5
            or abs(gt_num - (pred_num + 273.15)) <= 1.5
        )
    tolerance = max(1e-6, 0.05 * max(abs(gt_num), abs(pred_num), 1.0))
    return abs(gt_num - pred_num) <= tolerance


def process_issue(gt_process: str, pred_process: str) -> str | None:
    if slug(gt_process) == slug(pred_process):
        return None
    gt_norm = normalize_process_category(gt_process)
    pred_norm = normalize_process_category(pred_process)
    if gt_norm == pred_norm and gt_norm:
        return "process_category_vocab_mismatch"
    if gt_norm and pred_norm and (gt_norm in pred_norm or pred_norm in gt_norm):
        return "process_category_missing_post_treatment"
    return "process_category_substantive_mismatch"


def item_match_score(gt_item: dict[str, Any], pred_item: dict[str, Any]) -> float:
    score = 0.0
    if item_role(gt_item) and item_role(gt_item) == item_role(pred_item):
        score += 4.0
    gt_id = item_sample_id(gt_item)
    pred_id = item_sample_id(pred_item)
    if gt_id and pred_id:
        score += 5.0 * similarity(gt_id, pred_id)
    gt_alloy = item_alloy_name(gt_item)
    pred_alloy = item_alloy_name(pred_item)
    if gt_alloy and pred_alloy:
        score += 3.0 * similarity(gt_alloy, pred_alloy)
    gt_elements = set(composition_block(gt_item)["elements"] or {})
    pred_elements = set(composition_block(pred_item)["elements"] or {})
    if gt_elements or pred_elements:
        score += 4.0 * len(gt_elements & pred_elements) / max(1, len(gt_elements | pred_elements))
    if slug(item_process_category(gt_item)) == slug(item_process_category(pred_item)):
        score += 2.0
    return score


@dataclass
class PaperSummary:
    paper: str
    title: str
    pair_score: float
    gt_items: int
    pred_items: int
    matched_items: int
    unmatched_gt: list[str]
    unmatched_pred: list[str]
    issues: Counter[str]
    missing_output: bool = False


@dataclass
class PredRecord:
    dir_path: Path
    extraction_path: Path | None
    doc: dict[str, Any] | None
    title: str
    doi: str | None

    @property
    def has_output(self) -> bool:
        return self.extraction_path is not None and self.doc is not None


class Analyzer:
    def __init__(self, gt_dir: Path, pred_dir: Path) -> None:
        self.gt_dir = gt_dir
        self.pred_dir = pred_dir
        self.issue_counts: Counter[str] = Counter()
        self.examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.key_pred_only: Counter[str] = Counter()
        self.key_gt_only: Counter[str] = Counter()
        self.key_value_diff: Counter[str] = Counter()
        self.aqf_pred_only: Counter[str] = Counter()
        self.aqf_gt_only: Counter[str] = Counter()
        self.prop_pred_only: Counter[str] = Counter()
        self.prop_gt_only: Counter[str] = Counter()
        self.paper_summaries: list[PaperSummary] = []

    def _discover_pred_records(self) -> list[PredRecord]:
        records: list[PredRecord] = []
        for dir_path in sorted(path for path in self.pred_dir.iterdir() if path.is_dir()):
            extraction_candidates = sorted(dir_path.glob("*_extraction.json"))
            if extraction_candidates:
                extraction_path = extraction_candidates[0]
                doc = load_json(extraction_path)
                records.append(
                    PredRecord(
                        dir_path=dir_path,
                        extraction_path=extraction_path,
                        doc=doc,
                        title=paper_title(doc) or dir_path.name,
                        doi=((doc.get("Paper_Metadata") or {}).get("DOI")),
                    )
                )
                continue

            parse_metadata = next(iter(sorted(dir_path.glob("txt_parse/*_parse_metadata.json"))), None)
            metadata = load_json(parse_metadata) if parse_metadata else {}
            source_file = metadata.get("source_file")
            source_title = Path(source_file).stem if source_file else dir_path.name
            records.append(
                PredRecord(
                    dir_path=dir_path,
                    extraction_path=None,
                    doc=None,
                    title=source_title,
                    doi=metadata.get("doi"),
                )
            )
        return records

    def pair_papers(self) -> list[tuple[Path, dict[str, Any], PredRecord, float]]:
        gt_papers = [(path, load_json(path)) for path in sorted(self.gt_dir.glob("*.json"))]
        pred_records = self._discover_pred_records()
        unused = set(range(len(pred_records)))
        pairs: list[tuple[Path, dict[str, Any], PredRecord, float]] = []
        for gt_path, gt_doc in gt_papers:
            best_idx = None
            best_score = -1.0
            gt_name = paper_title(gt_doc) or gt_path.stem
            for idx in list(unused):
                pred_name = pred_records[idx].title or pred_records[idx].dir_path.name
                score = similarity(gt_name, pred_name)
                if score > best_score:
                    best_idx = idx
                    best_score = score
            assert best_idx is not None
            unused.remove(best_idx)
            pairs.append((gt_path, gt_doc, pred_records[best_idx], best_score))
        return pairs

    def remember_example(self, issue: str, payload: dict[str, Any], limit: int = 8) -> None:
        if len(self.examples[issue]) < limit:
            self.examples[issue].append(payload)

    def analyze(self) -> list[tuple[Path, dict[str, Any], PredRecord, float]]:
        pairs = self.pair_papers()
        for gt_path, gt_doc, pred_record, pair_score in pairs:
            gt_items = gt_doc.get("items") or []
            if not pred_record.has_output:
                self.issue_counts["missing_output_file"] += 1
                self.paper_summaries.append(
                    PaperSummary(
                        paper=gt_path.stem,
                        title=paper_title(gt_doc) or gt_path.stem,
                        pair_score=pair_score,
                        gt_items=len(gt_items),
                        pred_items=0,
                        matched_items=0,
                        unmatched_gt=[
                            item_sample_id(item) or item_alloy_name(item) or f"gt_{idx}"
                            for idx, item in enumerate(gt_items)
                        ],
                        unmatched_pred=[],
                        issues=Counter({"missing_output_file": 1}),
                        missing_output=True,
                    )
                )
                self.remember_example(
                    "missing_output_file",
                    {
                        "paper": gt_path.stem,
                        "pred_dir": pred_record.dir_path.name,
                        "pair_score": round(pair_score, 3),
                    },
                    limit=12,
                )
                continue

            assert pred_record.doc is not None
            pred_path = pred_record.extraction_path or pred_record.dir_path
            pred_doc = pred_record.doc
            pred_items = pred_doc.get("items") or []
            remaining = set(range(len(pred_items)))
            matches: list[tuple[int, int | None]] = []
            for gt_idx, gt_item in enumerate(gt_items):
                candidates = sorted(
                    ((item_match_score(gt_item, pred_items[pred_idx]), pred_idx) for pred_idx in remaining),
                    reverse=True,
                )
                if candidates and candidates[0][0] >= 4.0:
                    _, pred_idx = candidates[0]
                    remaining.remove(pred_idx)
                    matches.append((gt_idx, pred_idx))
                else:
                    matches.append((gt_idx, None))
            paper_issues: Counter[str] = Counter()
            unmatched_gt: list[str] = []
            for gt_idx, pred_idx in matches:
                gt_item = gt_items[gt_idx]
                if pred_idx is None:
                    issue = "missing_reference_item" if item_role(gt_item) == "reference" else "missing_target_item"
                    self.issue_counts[issue] += 1
                    paper_issues[issue] += 1
                    unmatched_gt.append(item_sample_id(gt_item) or item_alloy_name(gt_item) or f"gt_{gt_idx}")
                    self.remember_example(
                        issue,
                        {
                            "paper": gt_path.stem,
                            "gt_id": item_sample_id(gt_item),
                            "role": item_role(gt_item),
                            "proc": item_process_category(gt_item),
                        },
                    )
                    continue
                pred_item = pred_items[pred_idx]
                gt_id = item_sample_id(gt_item)
                pred_id = item_sample_id(pred_item)
                if normalize_sample_id(gt_id) != normalize_sample_id(pred_id):
                    self.issue_counts["sample_id_mismatch"] += 1
                    paper_issues["sample_id_mismatch"] += 1
                    self.remember_example(
                        "sample_id_mismatch",
                        {"paper": gt_path.stem, "gt_id": gt_id, "pred_id": pred_id},
                        limit=12,
                    )
                if item_gradient(gt_item) != item_gradient(pred_item):
                    self.issue_counts["gradient_flag_mismatch"] += 1
                    paper_issues["gradient_flag_mismatch"] += 1
                    self.remember_example(
                        "gradient_flag_mismatch",
                        {
                            "paper": gt_path.stem,
                            "gt_id": gt_id,
                            "pred_id": pred_id,
                            "gt": item_gradient(gt_item),
                            "pred": item_gradient(pred_item),
                        },
                    )
                proc_issue = process_issue(item_process_category(gt_item), item_process_category(pred_item))
                if proc_issue:
                    self.issue_counts[proc_issue] += 1
                    paper_issues[proc_issue] += 1
                    self.remember_example(
                        proc_issue,
                        {
                            "paper": gt_path.stem,
                            "gt_id": gt_id,
                            "pred_id": pred_id,
                            "gt_proc": item_process_category(gt_item),
                            "pred_proc": item_process_category(pred_item),
                        },
                        limit=12,
                    )
                gt_comp = composition_block(gt_item)
                pred_comp = composition_block(pred_item)
                if gt_comp["basis"] != pred_comp["basis"]:
                    self.issue_counts["composition_basis_mismatch"] += 1
                    paper_issues["composition_basis_mismatch"] += 1
                    self.remember_example(
                        "composition_basis_mismatch",
                        {
                            "paper": gt_path.stem,
                            "gt_id": gt_id,
                            "pred_id": pred_id,
                            "gt_basis": gt_comp["basis"],
                            "pred_basis": pred_comp["basis"],
                        },
                    )
                if slug(gt_comp["type"]) != slug(pred_comp["type"]):
                    self.issue_counts["composition_type_mismatch"] += 1
                    paper_issues["composition_type_mismatch"] += 1
                    self.remember_example(
                        "composition_type_mismatch",
                        {
                            "paper": gt_path.stem,
                            "gt_id": gt_id,
                            "pred_id": pred_id,
                            "gt_type": gt_comp["type"],
                            "pred_type": pred_comp["type"],
                        },
                    )
                gt_elements = set(gt_comp["elements"] or {})
                pred_elements = set(pred_comp["elements"] or {})
                if gt_elements != pred_elements:
                    self.issue_counts["composition_element_set_mismatch"] += 1
                    paper_issues["composition_element_set_mismatch"] += 1
                    self.remember_example(
                        "composition_element_set_mismatch",
                        {
                            "paper": gt_path.stem,
                            "gt_id": gt_id,
                            "pred_id": pred_id,
                            "gt_only": sorted(gt_elements - pred_elements),
                            "pred_only": sorted(pred_elements - gt_elements),
                        },
                    )
                else:
                    for key in sorted(gt_elements):
                        if not values_equivalent(key, gt_comp["elements"].get(key), pred_comp["elements"].get(key)):
                            self.issue_counts["composition_value_mismatch"] += 1
                            paper_issues["composition_value_mismatch"] += 1
                            self.remember_example(
                                "composition_value_mismatch",
                                {
                                    "paper": gt_path.stem,
                                    "gt_id": gt_id,
                                    "pred_id": pred_id,
                                    "key": key,
                                    "gt": gt_comp["elements"].get(key),
                                    "pred": pred_comp["elements"].get(key),
                                },
                            )
                            break
                gt_params = {normalize_param_key(k): (k, v) for k, v in item_key_params(gt_item).items()}
                pred_params = {normalize_param_key(k): (k, v) for k, v in item_key_params(pred_item).items()}
                gt_only_params = sorted(set(gt_params) - set(pred_params))
                pred_only_params = sorted(set(pred_params) - set(gt_params))
                if gt_only_params or pred_only_params:
                    self.issue_counts["key_params_key_mismatch"] += 1
                    paper_issues["key_params_key_mismatch"] += 1
                    for key in gt_only_params:
                        self.key_gt_only[key] += 1
                    for key in pred_only_params:
                        self.key_pred_only[key] += 1
                    self.remember_example(
                        "key_params_key_mismatch",
                        {
                            "paper": gt_path.stem,
                            "gt_id": gt_id,
                            "pred_id": pred_id,
                            "gt_only": gt_only_params[:6],
                            "pred_only": pred_only_params[:6],
                        },
                        limit=12,
                    )
                for key in sorted(set(gt_params) & set(pred_params)):
                    _, gt_value = gt_params[key]
                    _, pred_value = pred_params[key]
                    if not values_equivalent(key, gt_value, pred_value):
                        self.issue_counts["key_params_value_mismatch"] += 1
                        paper_issues["key_params_value_mismatch"] += 1
                        self.key_value_diff[key] += 1
                        self.remember_example(
                            "key_params_value_mismatch",
                            {
                                "paper": gt_path.stem,
                                "gt_id": gt_id,
                                "pred_id": pred_id,
                                "key": key,
                                "gt": gt_value,
                                "pred": pred_value,
                            },
                            limit=12,
                        )
                        break
                gt_aqf = item_aqf(gt_item)
                pred_aqf = item_aqf(pred_item)
                gt_aqf_keys = set(gt_aqf)
                pred_aqf_keys = set(pred_aqf)
                if gt_aqf_keys != pred_aqf_keys:
                    self.issue_counts["aqf_key_mismatch"] += 1
                    paper_issues["aqf_key_mismatch"] += 1
                    for key in sorted(gt_aqf_keys - pred_aqf_keys):
                        self.aqf_gt_only[key] += 1
                    for key in sorted(pred_aqf_keys - gt_aqf_keys):
                        self.aqf_pred_only[key] += 1
                    self.remember_example(
                        "aqf_key_mismatch",
                        {
                            "paper": gt_path.stem,
                            "gt_id": gt_id,
                            "pred_id": pred_id,
                            "gt_only": sorted(gt_aqf_keys - pred_aqf_keys)[:6],
                            "pred_only": sorted(pred_aqf_keys - gt_aqf_keys)[:6],
                        },
                        limit=12,
                    )
                if slug(item_main_phase(gt_item)) != slug(item_main_phase(pred_item)):
                    self.issue_counts["main_phase_mismatch"] += 1
                    paper_issues["main_phase_mismatch"] += 1
                    self.remember_example(
                        "main_phase_mismatch",
                        {
                            "paper": gt_path.stem,
                            "gt_id": gt_id,
                            "pred_id": pred_id,
                            "gt_phase": item_main_phase(gt_item),
                            "pred_phase": item_main_phase(pred_item),
                        },
                        limit=12,
                    )
                gt_props = item_property_names(gt_item)
                pred_props = item_property_names(pred_item)
                if gt_props - pred_props:
                    self.issue_counts["property_under_extraction"] += 1
                    paper_issues["property_under_extraction"] += 1
                    for key in sorted(gt_props - pred_props):
                        self.prop_gt_only[key] += 1
                    self.remember_example(
                        "property_under_extraction",
                        {
                            "paper": gt_path.stem,
                            "gt_id": gt_id,
                            "pred_id": pred_id,
                            "missing": sorted(gt_props - pred_props)[:6],
                        },
                        limit=12,
                    )
                if pred_props - gt_props:
                    self.issue_counts["property_over_extraction"] += 1
                    paper_issues["property_over_extraction"] += 1
                    for key in sorted(pred_props - gt_props):
                        self.prop_pred_only[key] += 1
                    self.remember_example(
                        "property_over_extraction",
                        {
                            "paper": gt_path.stem,
                            "gt_id": gt_id,
                            "pred_id": pred_id,
                            "extra": sorted(pred_props - gt_props)[:6],
                        },
                        limit=12,
                    )
            unmatched_pred: list[str] = []
            for pred_idx in sorted(remaining):
                pred_item = pred_items[pred_idx]
                issue = "extra_reference_item" if item_role(pred_item) == "reference" else "extra_target_item"
                self.issue_counts[issue] += 1
                paper_issues[issue] += 1
                unmatched_pred.append(item_sample_id(pred_item) or item_alloy_name(pred_item) or f"pred_{pred_idx}")
                self.remember_example(
                    issue,
                    {
                        "paper": gt_path.stem,
                        "pred_id": item_sample_id(pred_item),
                        "role": item_role(pred_item),
                        "proc": item_process_category(pred_item),
                    },
                    limit=12,
                )
            self.paper_summaries.append(
                PaperSummary(
                    paper=gt_path.stem,
                    title=paper_title(gt_doc) or gt_path.stem,
                    pair_score=pair_score,
                    gt_items=len(gt_items),
                    pred_items=len(pred_items),
                    matched_items=len(gt_items) - len(unmatched_gt),
                    unmatched_gt=unmatched_gt,
                    unmatched_pred=unmatched_pred,
                    issues=paper_issues,
                    missing_output=False,
                )
            )
        self.paper_summaries.sort(
            key=lambda row: (len(row.unmatched_gt) + len(row.unmatched_pred), sum(row.issues.values())),
            reverse=True,
        )
        return pairs


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)


def format_examples(examples: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    for example in examples:
        parts = [f"`{key}`={value}" for key, value in example.items() if value not in (None, "", [], {})]
        if parts:
            lines.append("- " + ", ".join(parts))
    return lines


def build_markdown(analyzer: Analyzer, pairs: list[tuple[Path, dict[str, Any], PredRecord, float]]) -> str:
    pair_scores = [score for _, _, _, score in pairs]
    gt_total_items = sum(len(doc.get("items") or []) for _, doc, _, _ in pairs)
    pred_total_items = sum(
        len(pred.doc.get("items") or []) for _, _, pred, _ in pairs if pred.has_output and pred.doc is not None
    )
    matched_total = sum(summary.matched_items for summary in analyzer.paper_summaries)
    missing_total = sum(len(summary.unmatched_gt) for summary in analyzer.paper_summaries)
    extra_total = sum(len(summary.unmatched_pred) for summary in analyzer.paper_summaries)
    pair_min = min(pair_scores)
    pair_avg = sum(pair_scores) / len(pair_scores)
    missing_output_total = sum(1 for summary in analyzer.paper_summaries if summary.missing_output)
    pred_minus_gt = pred_total_items - gt_total_items
    missing_reference_total = analyzer.issue_counts.get("missing_reference_item", 0)
    sample_id_mismatch = analyzer.issue_counts.get("sample_id_mismatch", 0)
    extra_target_item = analyzer.issue_counts.get("extra_target_item", 0)
    extra_reference_item = analyzer.issue_counts.get("extra_reference_item", 0)
    process_vocab_mismatch = analyzer.issue_counts.get("process_category_vocab_mismatch", 0)
    process_substantive_mismatch = analyzer.issue_counts.get("process_category_substantive_mismatch", 0)
    composition_basis_mismatch = analyzer.issue_counts.get("composition_basis_mismatch", 0)
    composition_type_mismatch = analyzer.issue_counts.get("composition_type_mismatch", 0)
    composition_value_mismatch = analyzer.issue_counts.get("composition_value_mismatch", 0)
    key_params_key_mismatch = analyzer.issue_counts.get("key_params_key_mismatch", 0)
    key_params_value_mismatch = analyzer.issue_counts.get("key_params_value_mismatch", 0)
    aqf_key_mismatch = analyzer.issue_counts.get("aqf_key_mismatch", 0)
    main_phase_mismatch = analyzer.issue_counts.get("main_phase_mismatch", 0)
    property_over_extraction = analyzer.issue_counts.get("property_over_extraction", 0)
    property_under_extraction = analyzer.issue_counts.get("property_under_extraction", 0)

    overview_rows = [
        ["对比论文数", len(pairs)],
        ["GT 条目总数", gt_total_items],
        ["Pipeline 条目总数", pred_total_items],
        ["成功匹配条目", matched_total],
        ["GT 漏配条目", missing_total],
        ["Pipeline 多出条目", extra_total],
        ["缺失 extraction 输出论文数", missing_output_total],
        ["标题配对最低相似度", f"{min(pair_scores):.3f}"],
        ["标题配对平均相似度", f"{sum(pair_scores) / len(pair_scores):.3f}"],
    ]

    top_issue_rows = []
    for issue, count in analyzer.issue_counts.most_common(12):
        top_issue_rows.append([issue, count])

    worst_rows = []
    for summary in analyzer.paper_summaries[:10]:
        worst_rows.append(
            [
                summary.paper,
                summary.gt_items,
                summary.pred_items,
                len(summary.unmatched_gt),
                len(summary.unmatched_pred),
                "missing_output"
                if summary.missing_output
                else " / ".join(f"{k}:{v}" for k, v in summary.issues.most_common(4)),
            ]
        )

    key_rows = []
    for key, count in analyzer.key_pred_only.most_common(8):
        key_rows.append([f"Pred-only `{key}`", count])
    for key, count in analyzer.key_gt_only.most_common(8):
        key_rows.append([f"GT-only `{key}`", count])

    aqf_rows = []
    for key, count in analyzer.aqf_pred_only.most_common(6):
        aqf_rows.append([f"Pred-only `{key}`", count])
    for key, count in analyzer.aqf_gt_only.most_common(6):
        aqf_rows.append([f"GT-only `{key}`", count])

    prop_rows = []
    for key, count in analyzer.prop_pred_only.most_common(6):
        prop_rows.append([f"Pred-only `{key}`", count])
    for key, count in analyzer.prop_gt_only.most_common(6):
        prop_rows.append([f"GT-only `{key}`", count])

    sections = [
        "# Pipeline vs GT 问题分析报告（0417）",
        "",
        "> 评测对象：`data/processed/` 最新推理结果 vs `415反馈/人工修正/` GT 标注",
        "> 生成方式：基于论文标题配对 + 样品级 greedy 匹配 + 字段归一化后的启发式对比",
        "",
        "## 1. 总体结论",
        "",
        markdown_table(["指标", "数值"], overview_rows),
        "",
        "### 结论摘要",
        "",
        f"- 这批数据 **没有再出现上一版那种整篇论文错配源文档的 P0 问题**。20 篇论文标题配对平均相似度为 `{pair_avg:.3f}`，最低为 `{pair_min:.3f}`，说明 `data/processed` 与 GT 基本是一一对应的。",
        "- 当前主要瓶颈已经从“读错论文”转为“**同一论文内样品拆分与字段标准化不稳定**”。最突出的是 `Sample_ID`、`Key_Params`、`Advanced_Quantitative_Features`、`Main_Phase` 和 `Process_Category`。",
        f"- 条目数层面 Pipeline 与 GT 相差 `{pred_minus_gt}` 条（`{pred_total_items}` vs `{gt_total_items}`），但这不代表召回更好。偏差里的相当一部分来自 **过拆样品**、**漏掉 reference**，以及部分论文根本没有成功产出 extraction 文件。",
        f"- `Reference` 仍然是系统性短板：启发式匹配下统计到 `{missing_reference_total}` 个 GT reference 条目缺失，集中出现在 `文献(3)`、Paper 1、Paper 4 等论文。",
        f"- 本轮还有 `{missing_output_total}` 篇论文目录存在但没有生成 extraction 文件，这类样本需要单独看 pipeline 执行链路，不能误判为纯 prompt/schema 问题。",
        "",
        "## 2. 高频问题分布",
        "",
        markdown_table(["问题类型", "次数"], top_issue_rows),
        "",
        "### 如何解读这些高频问题",
        "",
        "- `sample_id_mismatch` 最高，并不全是严重错误；其中一部分只是命名风格不同，但它会显著放大后续匹配难度，也会掩盖真正的字段差异。",
        "- `missing_output_file` 代表目录存在但没有成功产出 extraction JSON，这说明除了抽取质量，当前还存在运行链路/落盘稳定性问题。",
        "- `key_params_key_mismatch` 和 `aqf_key_mismatch` 说明当前 schema 语义还没有完全收敛。很多是“同义不同名”，也有一部分是 Pipeline 过度展开了文中参数或高级表征特征。",
        "- `process_category_substantive_mismatch` 依旧偏高，说明除了词表问题外，还存在真实工艺路线判断错误，尤其在粉末回收、激光熔覆/激光表面处理、混合制造这几类论文里更明显。",
        "- `composition_basis_mismatch` 和 `composition_type_mismatch` 仍在出现，说明 `Nominal`/`Measured` 与 `wt%`/`at%` 的判定规则还不够稳。",
        "",
        "## 3. 最值得优先看的论文",
        "",
        markdown_table(["论文", "GT", "Pred", "漏配", "多出", "主要问题"], worst_rows),
        "",
        "### 重点观察",
        "",
        "- 凡是 `missing_output` 的论文，应优先检查 extraction 节点是否中断、写文件路径是否异常、或后处理是否提前失败；这类问题不应该继续用 prompt 调参去掩盖。",
        "- `文献3-人工修正结果`：Pipeline 输出 `10` 条，GT 只有 `2` 条，且多出的 `8` 条几乎都是 reference/中间态被独立拆出，属于明显过拆。",
        "- `文献2-人工修正结果`：同时存在额外 target、样品错配、参数键不统一和 AQF 过度展开，说明 prompt 对“哪些状态该独立成条目”仍缺硬约束。",
        "- `Powder recycling for electron beam powder bed_fixed`：条目数接近，但字段差异非常密集，说明这篇主要不是漏提，而是 **标准化失败**。",
        "- `4-Highly printable...`：少了两个 GT reference，又出现参数值和主相不一致，是“reference 召回不足 + 样品匹配偏移”的典型例子。",
        "",
        "## 4. 分层问题分析",
        "",
        "### 4.1 样品层：拆分与命名还不稳定",
        "",
        f"- 典型表现：`sample_id_mismatch = {sample_id_mismatch}`，`extra_target_item = {extra_target_item}`，`extra_reference_item = {extra_reference_item}`，`missing_reference_item = {missing_reference_total}`。",
        "- 这说明当前 prompt 已能识别更多状态，但还没有稳定学会“何时必须拆、何时不能拆、拆完后该如何命名”。",
        "- 中文论文里尤其明显，常见模式是把对照铸态、粉末态、文献 benchmark、热处理中间态都拆成新的 target。",
        "",
        "代表样例：",
        *format_examples(analyzer.examples["missing_reference_item"][:6]),
        *format_examples(analyzer.examples["extra_target_item"][:6]),
        "",
        "### 4.2 工艺层：词表问题和真实误判并存",
        "",
        f"- `process_category_vocab_mismatch = {process_vocab_mismatch}` 说明一部分只是 GT 与 Pipeline 表达方式不同，例如 `Laser Powder Bed Fusion` vs `Laser Powder Bed Fusion (LPBF)`。",
        f"- 更关键的是 `process_category_substantive_mismatch = {process_substantive_mismatch}`，这部分是真错，不是格式差异。",
        "- 误判高发场景：",
        "- 把 `Laser Glazing` 样品和 `LPBF + T6` 样品混到一起。",
        "- 把 `Casting` 或 `Wrought` 的参考样品误当成 AM 基准样品。",
        "- 在 hybrid / UAM / 后处理论文中，只抓住了 `LPBF`，没守住更完整的路线标签。",
        "",
        "代表样例：",
        *format_examples(analyzer.examples["process_category_substantive_mismatch"][:6]),
        *format_examples(analyzer.examples["process_category_vocab_mismatch"][:4]),
        "",
        "### 4.3 成分层：来源、单位制、余量填充仍有残留错误",
        "",
        f"- `composition_basis_mismatch = {composition_basis_mismatch}`：说明模型仍会把 GT 的 measured 结果回落成 nominal，或者在 GT 未单列成分时主动补 nominal。",
        f"- `composition_type_mismatch = {composition_type_mismatch}`：最典型的是 LAAM 论文里 GT 用 `at%`，Pipeline 输出成 `wt%`。",
        f"- `composition_value_mismatch = {composition_value_mismatch}`：不仅是数值抽错，也包括 `Bal.` 元素回填不正确带来的主元素偏大问题。",
        "",
        "代表样例：",
        *format_examples(analyzer.examples["composition_basis_mismatch"][:5]),
        *format_examples(analyzer.examples["composition_value_mismatch"][:5]),
        "",
        "### 4.4 参数层：schema 漂移比纯漏提更严重",
        "",
        f"- `key_params_key_mismatch = {key_params_key_mismatch}`，高于 `key_params_value_mismatch = {key_params_value_mismatch}`，说明参数层第一优先级不是继续“多抽点参数”，而是先把常见键名收敛。",
        "- Pred-only 高频键包括 `protective_atmosphere`、`layer_thickness_um`、`oxygen_content_ppm`、`acceleration_voltage_kv`，说明 Pipeline 会主动展开很多过程细节。",
        "- GT-only 高频键包括 `powder_bed_preheating_temperature_k`、`spot_size_um`、`aging_temperature_k`、`aging_time_h`，说明后处理参数和少数关键工艺参数仍会漏掉或被换名。",
        "",
        markdown_table(["键名趋势", "次数"], key_rows[:16]),
        "",
        "代表样例：",
        *format_examples(analyzer.examples["key_params_key_mismatch"][:6]),
        *format_examples(analyzer.examples["key_params_value_mismatch"][:5]),
        "",
        "### 4.5 微观组织层：AQF 和 Main_Phase 仍然容易过度解释",
        "",
        f"- `aqf_key_mismatch = {aqf_key_mismatch}` 与 `main_phase_mismatch = {main_phase_mismatch}` 说明当前 prompt 倾向于把论文里的组织解释写得更“丰富”，但未必符合 GT 的收敛粒度。",
        "- AQF 里 Pred-only 最高的是 `Dislocation_Density_m2`、`Lattice_Parameter_nm`、`Fresh_Powder_Percent`、`Yield_Strength_Increase_MPa`，体现出 Pipeline 在做“语义合理扩展”。",
        "- GT-only 最高的是更具体的分相/分区域字段，如 `Dislocation_Density_Deformed_m2`、`FCC_Lattice_Parameter_nm`、`Lamellar_Spacing_nm`。这说明现在的问题不是完全不会提，而是 **抽象层级不一致**。",
        "",
        markdown_table(["AQF 趋势", "次数"], aqf_rows[:12]),
        "",
        "代表样例：",
        *format_examples(analyzer.examples["aqf_key_mismatch"][:6]),
        *format_examples(analyzer.examples["main_phase_mismatch"][:5]),
        "",
        "### 4.6 性能层：同时存在过提和漏提",
        "",
        f"- `property_over_extraction = {property_over_extraction}`，`property_under_extraction = {property_under_extraction}`，说明性能字段已经不是简单的召回不足，而是 **边界不稳**。",
        "- Pred-only 高频属性里出现 `Aluminum_Content`、`Chromium_Content`、`Niobium_Content`，说明 Pipeline 仍会把局部成分或分析量误当成性能属性。",
        "- GT-only 里除了常规拉伸指标，还出现整组腐蚀指标，说明复杂表征论文的 property schema 仍不够稳。",
        "",
        markdown_table(["Property 趋势", "次数"], prop_rows[:12]),
        "",
        "## 5. 下一步优化建议",
        "",
        "### P0：先稳住样品边界和 reference 召回",
        "",
        "- 在 prompt 中单独加入“**只有当成分、工艺路线、后处理状态或论文明确比较对象发生变化时，才拆成独立 item**”的硬约束。",
        "- 对 `Reference` 增加更强规则：凡出现 `compared with`、`benchmark`、`reference alloy`、`conventional alloy`、`cast counterpart`、`wrought counterpart` 时，优先检查是否需要新增 `Role=Reference` 条目。",
        "- 为 `Sample_ID` 增加运行后标准化模板，优先拼接 `alloy + process + state`，减少自由命名。",
        "",
        "### P1：把 schema 归一化前移，而不是完全依赖 LLM 自觉输出",
        "",
        "- 在后处理中建立参数键名映射白名单，统一 `hatch distance -> hatch spacing`、`beam diameter -> spot size`、`pre-heating temperature C -> build plate temperature K` 之类的常见变体。",
        "- 对 `Composition_Type` 和 `Nominal/Measured` 增加冲突校验；若 measured 缺失但文字只给 nominal，禁止模型擅自补 measured。",
        "- 对 AQF 做字段粒度约束：优先保留定量字段，避免把解释性组织结论或派生强度提升量无限扩展成新键。",
        "",
        "### P1：给高风险论文类型加专门护栏",
        "",
        "- `Powder recycling / raw powder / fresh powder / reused powder` 论文：强制区分粉末状态样品与成形件样品，防止 reference 过拆。",
        "- `Hybrid AM / UAM / glazing / cladding` 论文：工艺分类必须抓完整短语，不能只保留最常见的 `LPBF` 或 `AM`。",
        "- 含大量 benchmark 对照的中文论文：先做样品表枚举，再补字段，降低“把一句背景综述拆成多个 item”的概率。",
        "",
        "## 6. 建议的代码优化顺序",
        "",
        "1. 先做 `Sample_ID/Role/Reference` 的 prompt 收紧和后处理归一化。",
        "2. 再做 `Key_Params` 键名映射与单位转换白名单。",
        "3. 然后收紧 `AQF/Main_Phase` 粒度，减少过解释。",
        "4. 最后再针对 `Powder recycling`、`Hybrid AM`、中文 benchmark 论文补 few-shot 或规则示例。",
        "",
        "## 7. 备注",
        "",
        "- 这份报告是启发式对比，不等同于严格评测分数；但它非常适合指导下一轮 prompt/schema 优化，因为它把问题拆到了“样品边界 / 工艺分类 / 参数标准化 / 组织粒度”四个可行动层面。",
        "- 若要进一步量化每条规则的收益，下一步建议直接挑 `文献2`、`文献3`、`Powder recycling`、`4-Highly printable` 这四篇做 targeted ablation，对比修改前后 item 数和字段差异数。",
        "",
    ]
    return "\n".join(sections).strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate heuristic problem analysis markdown.")
    parser.add_argument("--gt-dir", type=Path, required=True)
    parser.add_argument("--pred-dir", type=Path, required=True)
    parser.add_argument("--output-md", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    analyzer = Analyzer(args.gt_dir, args.pred_dir)
    pairs = analyzer.analyze()
    markdown = build_markdown(analyzer, pairs)
    args.output_md.write_text(markdown, encoding="utf-8")
    print(f"Wrote report to {args.output_md}")


if __name__ == "__main__":
    main()
