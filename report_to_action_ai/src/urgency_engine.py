from dataclasses import dataclass
from .report_parser import ParsedReport

@dataclass
class UrgencyResult:
    urgency: str
    score: int
    drivers: list[str]


def classify_urgency(parsed: ParsedReport) -> UrgencyResult:
    score = 0
    drivers = []

    if parsed.critical_terms:
        score += 4
        drivers.append("Critical finding terms detected: " + ", ".join(parsed.critical_terms))

    high_risk_combos = [
        ("free air", "perforation"),
        ("hemorrhage", "mass effect"),
        ("pulmonary embol", "limited"),
        ("ischemia", "bowel obstruction"),
    ]
    for a, b in high_risk_combos:
        if a in parsed.normalized_text and b in parsed.normalized_text:
            score += 2
            drivers.append(f"High-risk combination detected: {a} + {b}")

    if parsed.uncertainty_terms:
        score += 1
        drivers.append("Uncertainty language detected: " + ", ".join(parsed.uncertainty_terms))

    if "urgent" in parsed.normalized_text or "immediate" in parsed.normalized_text:
        score += 2
        drivers.append("Report explicitly recommends urgent or immediate attention")

    if not parsed.critical_terms and "no acute" in parsed.normalized_text:
        score -= 2
        drivers.append("Report states no acute abnormality")

    if score >= 5:
        urgency = "Critical"
    elif score >= 3:
        urgency = "Urgent"
    elif score >= 1:
        urgency = "Priority Review"
    else:
        urgency = "Routine"

    return UrgencyResult(urgency=urgency, score=max(score, 0), drivers=drivers)
