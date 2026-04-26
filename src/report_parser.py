import re
from dataclasses import dataclass, field

CRITICAL_TERMS = [
    "free air", "perforation", "intracranial hemorrhage", "hemorrhage", "mass effect",
    "tension pneumothorax", "pneumothorax", "pulmonary embol", "aortic dissection",
    "rupture", "acute infarct", "stroke", "appendicitis", "bowel obstruction",
    "sepsis", "ischemia", "necrosis", "abscess", "critical result"
]

UNCERTAINTY_TERMS = [
    "possible", "possibly", "may represent", "may reflect", "suggests", "suggestive",
    "concerning for", "cannot exclude", "limited", "artifact", "correlate clinically",
    "indeterminate", "equivocal", "nonspecific", "suboptimal"
]

NEGATION_PATTERNS = [
    r"no\s+{term}", r"without\s+{term}", r"negative\s+for\s+{term}", r"absence\s+of\s+{term}"
]

@dataclass
class ParsedReport:
    original_text: str
    normalized_text: str
    critical_terms: list[str] = field(default_factory=list)
    uncertainty_terms: list[str] = field(default_factory=list)
    negated_critical_terms: list[str] = field(default_factory=list)
    sentence_count: int = 0


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def is_negated(text: str, term: str) -> bool:
    escaped = re.escape(term)
    for pattern in NEGATION_PATTERNS:
        if re.search(pattern.format(term=escaped), text):
            return True
    return False


def find_terms(text: str, terms: list[str]) -> list[str]:
    found = []
    for term in terms:
        if term in text:
            found.append(term)
    return sorted(set(found))


def parse_report(report_text: str) -> ParsedReport:
    normalized = normalize_text(report_text)
    all_critical = find_terms(normalized, CRITICAL_TERMS)
    negated = [term for term in all_critical if is_negated(normalized, term)]
    active_critical = [term for term in all_critical if term not in negated]
    uncertainty = find_terms(normalized, UNCERTAINTY_TERMS)
    sentences = [s for s in re.split(r"[.!?]+", report_text) if s.strip()]
    return ParsedReport(
        original_text=report_text,
        normalized_text=normalized,
        critical_terms=active_critical,
        uncertainty_terms=uncertainty,
        negated_critical_terms=negated,
        sentence_count=len(sentences),
    )
