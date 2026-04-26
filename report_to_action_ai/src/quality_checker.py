from dataclasses import dataclass


@dataclass
class QualityResult:
    quality_flags: list
    missing_information: list


def check_quality(parsed, urgency):
    quality_flags = []
    missing_information = []

    # Flag uncertainty in urgent or critical reports
    if parsed.uncertainty_terms and urgency.urgency in ["Critical", "Urgent"]:
        quality_flags.append(
            "Uncertainty language present in urgent or critical report"
        )

    # Flag possible contradiction if both active and negated critical terms appear
    if parsed.critical_terms and parsed.negated_critical_terms:
        quality_flags.append(
            "Both active and negated critical terms detected"
        )

    # Add missing clinical context based on urgency
    if urgency.urgency == "Critical":
        missing_information.extend([
            "Relevant vital signs",
            "Responsible clinician notification status",
            "Follow-up or escalation confirmation"
        ])

    elif urgency.urgency == "Urgent":
        missing_information.extend([
            "Clinical correlation",
            "Follow-up plan"
        ])

    return QualityResult(
        quality_flags=quality_flags,
        missing_information=missing_information
    )
