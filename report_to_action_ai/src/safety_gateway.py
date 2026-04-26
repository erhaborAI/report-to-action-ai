from dataclasses import dataclass


@dataclass
class SafetyGatewayResult:
    triggered: bool
    reasons: list


def run_safety_gateway(parsed, urgency, quality):
    reasons = []

    if urgency.urgency == "Critical":
        reasons.append("Critical urgency classification")

    if parsed.critical_terms and parsed.uncertainty_terms:
        reasons.append("Critical finding with uncertainty language")

    if quality.missing_information and urgency.urgency in ["Critical", "Urgent"]:
        reasons.append("Missing clinical context in urgent or critical case")

    if quality.quality_flags:
        reasons.append("Quality or consistency issue detected")

    triggered = len(reasons) > 0

    return SafetyGatewayResult(
        triggered=triggered,
        reasons=reasons
    )