"""Section/title normalization and noise filtering for OCR text."""

from __future__ import annotations

import re
from typing import List, Tuple

from .doi_extractor import DOI_RE, DOI_URL_RE

# ---------------------------------------------------------------------------
# Chemical element symbols (ordered longest-first to avoid prefix ambiguity).
# ---------------------------------------------------------------------------
_ELEMENT_SYMBOLS = (
    "Uut", "Uup", "Uus", "Uuo",
    "He", "Li", "Be", "Ne", "Na", "Mg", "Al", "Si", "Cl", "Ar",
    "Ca", "Sc", "Ti", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Zr", "Nb",
    "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb",
    "Te", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm",
    "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
    "Ta", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi",
    "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "Np", "Pu",
    "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf",
    "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv",
    "B", "C", "N", "O", "F", "P", "S", "K", "V", "Y", "I", "W",
    "U", "Y",
)
_ELEMENT_PAT = "|".join(re.escape(e) for e in _ELEMENT_SYMBOLS)

# Pattern: one or more (Element)(number with optional decimal) pairs, e.g.
# Ti42Hf21Nb21V16  or  Ni61.3Cr25.3  or  Ni61,3Cr25,3 (comma as decimal)
# The [.,] allows both period and comma as decimal separators; the comma
# variant is normalised to period inside _normalize_alloy_formula.
_ALLOY_FORMULA_RE = re.compile(
    r"\b((?:(?:" + _ELEMENT_PAT + r")\d+(?:[.,]\d+)?){2,})\b"
)

# Decimal normalisation: digit followed by Chinese comma / full-width period /
# middle dot, followed by digit  →  replace separator with ASCII period.
# (ASCII comma is handled separately inside chemical formula contexts.)
_DECIMAL_NOISE_RE = re.compile(r"(\d)[，、·。](\d)")

ALLOY_OCR_FIXES: List[Tuple[re.Pattern, str]] = [
    (re.compile(r"\bNb15\s*Ta1[oO]\s*W75\b"), "Nb15Ta10W75"),
    (re.compile(r"\bNb1[sS]\s*Ta10\s*W75\b"), "Nb15Ta10W75"),
    (re.compile(r"\bNb15\s*Ta1[oO]0\s*W75\b"), "Nb15Ta10W75"),
    (re.compile(r"\bNb15\s+Ta10\s*W75\b"), "Nb15Ta10W75"),
    (re.compile(r"\bNb15\s*Ta10\s+W75\b"), "Nb15Ta10W75"),
    (re.compile(r"\bNb15\s*Ta10\s*W\s*,"), "Nb15Ta10W75,"),
    (re.compile(r"\(Nb15\s*Ta1[oO]\s*W75\)"), "(Nb15Ta10W75)"),
    (re.compile(r"\(Nb15\s*Ta10\s+W75\)"), "(Nb15Ta10W75)"),
    (re.compile(r"\(Nb15\s+Ta10\s*W75\)"), "(Nb15Ta10W75)"),
]

SPACED_TITLE_RE = re.compile(r"^(#+\s+)?([A-Z](?:\s[A-Z]){3,})$")

SECTION_PATTERNS: List[Tuple[re.Pattern, str | None]] = [
    (re.compile(r"^(?:#+\s*)?A\s*B\s*S\s*T\s*R\s*A\s*C\s*T\s*$", re.IGNORECASE), "## ABSTRACT"),
    (re.compile(r"^(?:#+\s*)?ABSTRACT\s*$", re.IGNORECASE), "## ABSTRACT"),
    (re.compile(r"^(?:#+\s*)?ARTICLE\s+INFO\s*$", re.IGNORECASE), "## ARTICLE INFO"),
    (re.compile(r"^(?:#+\s*)?KEYWORDS?\s*:?\s*$", re.IGNORECASE), "## Keywords"),
    (re.compile(r"^(?:#+\s*)?(ACKNOWLEDGEMENTS?|ACKNOWLEDGMENTS?)\s*$", re.IGNORECASE), "## Acknowledgements"),
    (re.compile(r"^(?:#+\s*)?CRediT\s+authorship\s+contribution\s+statement\s*$", re.IGNORECASE), "## CRediT Authorship"),
    (re.compile(r"^(?:#+\s*)?DECLARATION\s+OF\s+(COMPETING\s+)?INTEREST.*$", re.IGNORECASE), "## Declaration of Interest"),
    (re.compile(r"^(?:#+\s*)?DATA\s+AVAILABILITY.*$", re.IGNORECASE), "## Data Availability"),
    (re.compile(r"^(?:#+\s*)?SUPPLEMENTARY\s+(DATA|MATERIAL|INFORMATION).*$", re.IGNORECASE), "## Supplementary Material"),
    (re.compile(r"^(?:#+\s*)?(\d+(?:\.\d+)*\.?)\s+(.+)$"), None),
]

NOISE_LINE_PATTERNS: List[Tuple[re.Pattern, bool]] = [
    (re.compile(r"^Materials Science and Engineering\s+\d", re.IGNORECASE), True),
    (re.compile(r"^Acta Materialia\s+\d", re.IGNORECASE), True),
    (re.compile(r"^Journal of Materials Science\s+\d", re.IGNORECASE), True),
    (re.compile(r"^International Journal of Plasticity\s+\d", re.IGNORECASE), True),
    (re.compile(r"^Journal of Alloys and Compounds\s+\d", re.IGNORECASE), True),
    (re.compile(r"^Scripta Materialia\s+\d", re.IGNORECASE), True),
    (re.compile(r"^Additive Manufacturing\s+\d", re.IGNORECASE), True),
    (re.compile(r"^Contents lists available at ScienceDirect", re.IGNORECASE), False),
    (re.compile(r"^Available online", re.IGNORECASE), False),
    (re.compile(r"^Received \d+", re.IGNORECASE), False),
    (re.compile(r"^Accepted \d+", re.IGNORECASE), False),
    (re.compile(r"^journal homepage", re.IGNORECASE), False),
    (re.compile(r"^https?://www\.(sciencedirect|elsevier|springer|wiley)", re.IGNORECASE), False),
    (re.compile(r"^Full length article\s*$", re.IGNORECASE), False),
    (re.compile(r"^\d{4}-\d{3}[\dX]/\s*�", re.IGNORECASE), False),
    (re.compile(r"^�\s*\d{4}", re.IGNORECASE), False),
    (re.compile(r"^Elsevier", re.IGNORECASE), False),
    (re.compile(r"^\* Corresponding author", re.IGNORECASE), False),
    (re.compile(r"^\*\* Corresponding author", re.IGNORECASE), False),
    (re.compile(r"^E-mail address", re.IGNORECASE), False),
    (re.compile(r"^\d+$"), False),
    (re.compile(r"^[A-Za-z]:\\"), False),
    (re.compile(r"^/tmp/"), False),
    (re.compile(r"^min\s*$", re.IGNORECASE), False),
    (re.compile(r"^general\s*$", re.IGNORECASE), False),
    (re.compile(r"^(STRUCTURE|PROPERTIES|MODELLING|MODELIINC|PROCESSING)\s*$"), False),
    (re.compile(r"^Check\s+for\s*$", re.IGNORECASE), False),
    (re.compile(r"^updates?\s*$", re.IGNORECASE), False),
    (re.compile(r"^Acta\s+Materialia\s*$", re.IGNORECASE), False),
    (re.compile(r"^Actd\s+Materialia\b", re.IGNORECASE), False),
    (re.compile(r"^Materialia\s*$", re.IGNORECASE), False),
    (re.compile(r"^Acta\s*$", re.IGNORECASE), False),
    (re.compile(r"^[A-Z]\.\s+\w+\s+et\s+al\.?\s*$", re.IGNORECASE), False),
]


# ---------------------------------------------------------------------------
# Greek symbol normalisation for materials science OCR.
# ---------------------------------------------------------------------------

# OCR commonly misreads Greek letters in phase/property contexts.
# Each entry: (wrong_char, correct_unicode, context_keywords).
# The fix is applied only when the line contains at least one context keyword.
_GREEK_OCR_FIXES: List[Tuple[str, str, Tuple[str, ...]]] = [
    # σ (sigma) phase, stress, yield strength context.
    # OCR often outputs 'o' or 'σ' (already correct) or 'ơ'.
    ("ơ", "σ", ("phase", "stress", "strength", "MPa", "GPa", "yield", "σ", "phase")),
    # μ (mu) phase context; OCR may output 'u' adjacent to 'phase' or 'μm'.
    # We only fix standalone 'u' that looks like a Greek mu in context.
    # Pattern: word-boundary 'u' followed by 'm' (μm) or before 'phase'.
    # Handled via regex below.
]

# Regex patterns for context-gated Greek symbol fixes.
# Each tuple: (compiled_pattern, replacement, context_keywords_tuple)
_GREEK_REGEX_FIXES: List[Tuple[re.Pattern, str, Tuple[str, ...]]] = [
    # 'o phase' / 'o-phase' → 'σ phase' / 'σ-phase' (sigma phase in HEA/steel)
    (
        re.compile(r"\bo\s*(?=-?phase\b)", re.IGNORECASE),
        "σ",
        ("phase", "precipitation", "intermetallic", "FeCoCrNi", "HEA", "steel"),
    ),
    # 'u phase' / 'u-phase' → 'μ phase' / 'μ-phase'
    (
        re.compile(r"\bu\s*(?=-?phase\b)", re.IGNORECASE),
        "μ",
        ("phase", "precipitation", "intermetallic"),
    ),
    # standalone 'um' as unit (e.g. '10 um') → '10 μm'
    (
        re.compile(r"(?<=\d\s)um\b"),
        "μm",
        ("grain", "size", "diameter", "thickness", "spacing", "μm", "nm"),
    ),
    # '10um' (no space) → '10μm'
    (
        re.compile(r"(?<=\d)um\b"),
        "μm",
        ("grain", "size", "diameter", "thickness", "spacing", "μm", "nm"),
    ),
]


def _is_phase_context(line: str, keywords: Tuple[str, ...]) -> bool:
    """Return True when the line contains at least one of the context keywords."""
    line_lower = line.lower()
    return any(kw.lower() in line_lower for kw in keywords)


def normalize_greek_symbols(text: str) -> str:
    """Apply context-gated Greek symbol normalisation to *text*.

    Only modifies lines that contain at least one of the required context
    keywords for each fix, avoiding false positives in non-physics text.
    """
    lines: List[str] = []
    for line in text.splitlines():
        for char_wrong, char_correct, keywords in _GREEK_OCR_FIXES:
            if char_wrong in line and _is_phase_context(line, keywords):
                line = line.replace(char_wrong, char_correct)
        for pat, repl, keywords in _GREEK_REGEX_FIXES:
            if _is_phase_context(line, keywords):
                line = pat.sub(repl, line)
        lines.append(line)
    return "\n".join(lines)


def _is_chemical_context(line: str) -> bool:
    """Return True when the line is likely to contain chemical formula notation."""
    # Must contain at least one element symbol followed immediately by a digit.
    return bool(re.search(r"(?:" + _ELEMENT_PAT + r")\d", line))


_DECIMAL_REPL = r"\1.\2"
_COMMA_DECIMAL_RE = re.compile(r"(\d),(\d)")


def _normalize_alloy_formula(match: re.Match) -> str:
    """Convert a raw alloy string like Ti42Hf21 to Ti_{42}Hf_{21}."""
    raw = match.group(0)
    # Normalise decimal separators: Chinese comma / ASCII comma → ASCII period.
    # ASCII comma is treated as a decimal separator only inside alloy formulas.
    raw = _DECIMAL_NOISE_RE.sub(_DECIMAL_REPL, raw)
    raw = _COMMA_DECIMAL_RE.sub(_DECIMAL_REPL, raw)
    # Insert LaTeX subscript notation around the numeric parts.
    result = re.sub(
        r"(\d+(?:\.\d+)?)",
        lambda m: "_{" + m.group(1) + "}",
        raw,
    )
    return result


def normalize_alloy_strings(text: str) -> str:
    """Apply OCR-specific fixes and chemical formula normalisation.

    Steps:
    1. Apply hard-coded alloy OCR fixes (specific known misreads).
    2. Normalise decimal separators (Chinese comma → ASCII period) in numeric
       contexts.
    3. Convert bare element-number sequences (e.g. Ti42Hf21) to LaTeX
       subscript notation (Ti_{42}Hf_{21}) when in a chemical context.
    4. Apply context-gated Greek symbol normalisation (σ/μ phase etc.).
    """
    for pat, repl in ALLOY_OCR_FIXES:
        text = pat.sub(repl, text)

    # Process line-by-line so the chemical context gate is per-line.
    lines: List[str] = []
    for line in text.splitlines():
        # Decimal normalisation: always safe within a numeric context.
        line = _DECIMAL_NOISE_RE.sub(_DECIMAL_REPL, line)
        # Alloy formula subscript normalisation: only in chemical contexts.
        if _is_chemical_context(line):
            line = _ALLOY_FORMULA_RE.sub(_normalize_alloy_formula, line)
        lines.append(line)
    text = "\n".join(lines)

    # Greek symbol normalisation (context-gated).
    text = normalize_greek_symbols(text)
    return text


def is_noise_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    numeric_unit = re.sub(r"^#+\s*", "", stripped)
    if re.match(r"^\d{1,4}(?:\.\d+)?\s*(um|nm|pm|°C|C)\b", numeric_unit):
        return True
    if re.match(r"^\d{1,4}(?:\.\d+)?\s*(?:°C|C)\s*[~\-]\s*\d{1,4}(?:\.\d+)?\s*(?:°C|C)\b", numeric_unit):
        return True

    has_doi = bool(DOI_RE.search(stripped)) or bool(DOI_URL_RE.search(stripped))
    for pat, skip_if_doi in NOISE_LINE_PATTERNS:
        if pat.match(stripped):
            if skip_if_doi and has_doi:
                return False
            return True
    return False


def structure_sections(text: str) -> str:
    output_lines: List[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if is_noise_line(stripped):
            continue
        matched = False
        for pat, replacement in SECTION_PATTERNS:
            m = pat.match(stripped)
            if m:
                if replacement:
                    output_lines.append("")
                    output_lines.append(replacement)
                    output_lines.append("")
                else:
                    sec_num = m.group(1).rstrip(".")
                    sec_title = m.group(2).strip()
                    output_lines.append("")
                    output_lines.append(f"## {sec_num}. {sec_title}")
                    output_lines.append("")
                matched = True
                break
        if matched:
            continue
        m = SPACED_TITLE_RE.match(stripped)
        if m:
            collapsed = m.group(2).replace(" ", "")
            output_lines.append("")
            output_lines.append(f"## {collapsed}")
            output_lines.append("")
            continue
        heading_match = re.match(r"^(#{3,6})\s+(.*)", stripped)
        if heading_match:
            title = heading_match.group(2).strip()
            output_lines.append(f"## {title}")
            continue
        if re.match(r"^##\s+Page\s+\d+\s*$", stripped):
            output_lines.append("")
            continue
        output_lines.append(line)

    result = "\n".join(output_lines)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip()


def strip_references_section(text: str) -> str:
    out: List[str] = []
    skipping_refs = False

    for line in text.splitlines():
        stripped = line.strip()

        # Check for References start
        if re.match(r"^#+\s*(references?|bibliography|citations?)\s*$", stripped, re.IGNORECASE) or re.match(
            r"^(references?|bibliography|citations?)\s*$", stripped, re.IGNORECASE
        ):
            skipping_refs = True
            continue

        # Check for Appendix / Supplementary start to stop skipping
        # Matches lines starting with # (header) and containing Appendix or Supplementary
        if skipping_refs and re.match(r"^#+\s*(appendix|supplementary)\b.*$", stripped, re.IGNORECASE):
            skipping_refs = False
            out.append(line)
            continue

        if not skipping_refs:
            out.append(line)

    return "\n".join(out).strip()

