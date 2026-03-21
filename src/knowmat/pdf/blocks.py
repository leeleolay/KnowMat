"""Block adaptation helpers for PaddleOCR-VL outputs."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .html_cleaner import convert_html_to_markdown, html_table_to_structured


def _get_block_attr(block: Any, name: str, default: Any = None) -> Any:
    if hasattr(block, name):
        return getattr(block, name)
    if isinstance(block, dict):
        return block.get(name, default)
    return default


_TABLE_LABELS = frozenset({"table", "chart"})
_IMAGE_LABELS = frozenset({"image", "figure", "seal", "figure_title"})
_FORMULA_LABELS = frozenset({"display_formula", "formula", "inline_formula"})


def _make_table_item(content: str, confidence: Any) -> Dict[str, Any]:
    structured = html_table_to_structured(content)
    data: Dict[str, Any] = structured if structured else {
        "text": convert_html_to_markdown(content),
        "raw_html": content,
    }
    item: Dict[str, Any] = {"typer": "table", "data": data}
    if confidence is not None:
        item["confidence"] = confidence
    return item


def _make_image_item(block: Any, content: str, confidence: Any) -> Dict[str, Any]:
    image_info = _get_block_attr(block, "image", None)
    image_path = image_info.get("path") if isinstance(image_info, dict) else None
    data: Dict[str, Any] = {"image_path": image_path}
    if content:
        data["caption"] = convert_html_to_markdown(content)
    if confidence is not None:
        data["confidence"] = confidence
    return {"typer": "image", "data": data}


def _make_formula_item(block: Any, content: str, confidence: Any) -> Dict[str, Any]:
    latex_text = _get_block_attr(block, "latex", None) or content
    data: Dict[str, Any] = {
        "text": convert_html_to_markdown(content) if content else "",
        "latex": latex_text or "",
    }
    if confidence is not None:
        data["confidence"] = confidence
    return {"typer": "formula", "data": data}


def block_to_item(block: Any) -> Optional[Dict[str, Any]]:
    label = _get_block_attr(block, "label", None) or _get_block_attr(block, "block_label", None)
    content = (
        _get_block_attr(block, "block_content", "")
        or _get_block_attr(block, "content", "")
        or _get_block_attr(block, "text", "")
    )
    confidence = _get_block_attr(block, "score", None) or _get_block_attr(block, "confidence", None)
    if isinstance(content, str):
        content = content.strip()

    if label in _TABLE_LABELS:
        return _make_table_item(content or "", confidence)
    if label in _IMAGE_LABELS:
        return _make_image_item(block, content, confidence)
    if label in _FORMULA_LABELS:
        return _make_formula_item(block, content, confidence)
    if content:
        item: Dict[str, Any] = {"typer": "paragraph", "text": convert_html_to_markdown(content)}
        if confidence is not None:
            item["confidence"] = confidence
        return item
    return None


def text_to_paragraph_items(text: str) -> List[Dict[str, Any]]:
    if not text:
        return []
    blocks = [b.strip() for b in text.split("\n\n") if b.strip()]
    return [{"typer": "paragraph", "text": block} for block in blocks]

