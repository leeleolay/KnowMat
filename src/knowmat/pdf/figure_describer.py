"""Multimodal LLM figure description for KnowMat.

Uses the same OpenAI-compatible endpoint configured in .env (LLM_API_KEY,
LLM_BASE_URL, LLM_MODEL) to generate a concise textual description of a
figure image cropped from a scientific paper.

This module is intentionally dependency-light: it only requires ``openai``
(already a transitive dependency via langchain-openai) and the standard
library.  It never raises — failures are logged and an empty string is
returned so the main pipeline is never blocked.
"""

from __future__ import annotations

import base64
import logging
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

_SYSTEM_PROMPT = (
    "You are a materials science figure analyst. "
    "Describe the key information shown in this figure from a scientific paper. "
    "Focus on: microstructure features, scale bars, phase labels, measurement values, and trends. "
    "Be concise (2-4 sentences). Do not repeat the caption verbatim."
)


def _encode_image_base64(image_path: Path) -> Optional[str]:
    """Read an image file and return its base64-encoded content."""
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except OSError as exc:
        logger.warning("Cannot read figure image %s: %s", image_path, exc)
        return None


def _image_media_type(image_path: Path) -> str:
    suffix = image_path.suffix.lower()
    return {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }.get(suffix, "image/jpeg")


def describe_figure_image(
    image_path: Path,
    caption: str = "",
    *,
    model: Optional[str] = None,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
) -> str:
    """Generate a textual description of a figure image using a multimodal LLM.

    Parameters
    ----------
    image_path:
        Absolute or relative path to the figure image (JPEG/PNG).
    caption:
        Optional figure caption text for context (e.g. "Fig. 1. SEM image of...").
    model:
        Model ID to use.  Defaults to ``LLM_MODEL`` env var.
    api_key:
        API key.  Defaults to ``LLM_API_KEY`` env var.
    base_url:
        Base URL for OpenAI-compatible endpoint.  Defaults to ``LLM_BASE_URL`` env var.

    Returns
    -------
    str
        A concise description of the figure, or empty string on failure.
    """
    resolved_path = Path(image_path)
    if not resolved_path.is_file():
        logger.debug("Figure image not found, skipping description: %s", image_path)
        return ""

    b64 = _encode_image_base64(resolved_path)
    if b64 is None:
        return ""

    _api_key = api_key or os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY", "")
    _base_url = base_url or os.getenv("LLM_BASE_URL") or os.getenv("OPENAI_BASE_URL")
    _model = model or os.getenv("LLM_MODEL", "")

    if not _api_key:
        logger.warning("No LLM_API_KEY configured; skipping figure description.")
        return ""

    try:
        from openai import OpenAI  # type: ignore
    except ImportError:
        logger.warning("openai package not available; skipping figure description.")
        return ""

    user_text = "Please describe this scientific figure."
    if caption:
        user_text = f"Caption context: {caption}\n\n{user_text}"

    media_type = _image_media_type(resolved_path)

    messages = [
        {"role": "system", "content": _SYSTEM_PROMPT},
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{media_type};base64,{b64}",
                        "detail": "high",
                    },
                },
                {"type": "text", "text": user_text},
            ],
        },
    ]

    client_kwargs: dict = {"api_key": _api_key}
    if _base_url:
        client_kwargs["base_url"] = _base_url

    try:
        client = OpenAI(**client_kwargs)
        create_kwargs: dict = {
            "model": _model,
            "messages": messages,
            "max_tokens": 512,
        }
        # Some models (e.g. GPT-5) do not accept temperature
        _model_lower = (_model or "").lower()
        if not any(x in _model_lower for x in ("gpt-5",)):
            create_kwargs["temperature"] = 0.2

        response = client.chat.completions.create(**create_kwargs)
        content = response.choices[0].message.content or ""
        logger.debug("Figure description generated (%d chars) for %s", len(content), image_path)
        return content.strip()
    except Exception as exc:
        logger.warning("Figure description LLM call failed for %s: %s", image_path, exc)
        return ""


def inject_figure_descriptions(
    text: str,
    ocr_items: List[Dict[str, Any]],
) -> str:
    """Insert multimodal LLM descriptions above each figure caption in *text*.

    For each ``typer == "image"`` item with a valid ``image_path``, a description
    is generated and inserted above the matching ``Fig. N`` / ``Figure N`` line in
    *text*.  If no matching caption line is found the description is appended at the
    end.  Items without ``image_path`` are silently skipped.

    Called from the extraction stage (not OCR), so every LLM call here is
    intentional and gated by ``settings.figure_description_enabled``.
    """
    image_items = [
        it for it in ocr_items
        if it.get("typer") == "image" and it.get("data", {}).get("image_path")
    ]
    if not image_items:
        return text

    for item in image_items:
        data = item.get("data", {})
        raw_path = data.get("image_path", "")
        img_path = Path(raw_path)
        if not img_path.is_file():
            logger.debug("Figure image not found, skipping description injection: %s", img_path)
            continue

        caption = data.get("caption", "")
        figure_num = data.get("figure_num", "")
        description = describe_figure_image(img_path, caption=caption)
        if not description:
            continue

        label = f"Figure {figure_num}" if figure_num else "Figure"
        description_block = f"> [{label} AI Description]: {description}\n\n"

        # Try to find the caption line in the text and insert above it
        if figure_num:
            pattern = re.compile(
                r"((?:Fig\.?\s*|Figure\s*)" + re.escape(str(figure_num)) + r"[\s\.\:])",
                re.IGNORECASE,
            )
            match = pattern.search(text)
            if match:
                insert_pos = match.start()
                text = text[:insert_pos] + description_block + text[insert_pos:]
                logger.debug(
                    "Injected description for Figure %s at position %d", figure_num, insert_pos
                )
                continue

        # Fallback: append at end
        text = text + "\n\n" + description_block

    return text
