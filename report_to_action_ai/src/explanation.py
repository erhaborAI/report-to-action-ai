from .report_parser import ParsedReport
from .urgency_engine import UrgencyResult
from .quality_checker import QualityResult
from .safety_gateway import SafetyGatewayResult
from .escalation import EscalationResult


def build_explanation(parsed, urgency, quality, safety, escalation):
    explanation_parts = []

    critical_terms = getattr(parsed, "critical_terms", [])
    uncertainty_terms = getattr(parsed, "uncertainty_terms", [])

    urgency_label = getattr(urgency, "urgency", str(urgency))
    safety_triggered = getattr(safety, "triggered", False)
    safety_reasons = getattr(safety, "reasons", [])

    escalation_level = escalation.get("level", "Not specified") if isinstance(escalation, dict) else getattr(escalation, "escalation_level", "Not specified")
    escalation_action = escalation.get("action", "Not specified") if isinstance(escalation, dict) else getattr(escalation, "recommended_channel", "Not specified")

    if "perforation" in critical_terms:
        explanation_parts.append(
            "Free intraperitoneal air or suspected perforation suggests a potentially life-threatening abdominal emergency."
        )

    if "intracranial hemorrhage" in critical_terms or "hemorrhage" in critical_terms:
        explanation_parts.append(
            "Intracranial hemorrhage is a critical finding that may require urgent clinician review and escalation."
        )

    if "pulmonary embolism" in critical_terms or "embolism" in critical_terms:
        explanation_parts.append(
            "Pulmonary embolism is a potentially life-threatening finding that may require urgent clinical action."
        )

    if "stroke" in critical_terms:
        explanation_parts.append(
            "Possible stroke requires time-sensitive evaluation and escalation because delayed action may affect outcomes."
        )

    if uncertainty_terms:
        explanation_parts.append(
            f"Uncertainty language was detected: {', '.join(uncertainty_terms)}."
        )

    if safety_triggered:
        explanation_parts.append(
            f"The safety gateway was triggered because: {', '.join(safety_reasons)}."
        )

    explanation_parts.append(
        f"Final workflow classification: {urgency_label} urgency."
    )

    explanation_parts.append(
        f"Recommended workflow action: {escalation_level} via {escalation_action}."
    )

    return " ".join(explanation_parts)
