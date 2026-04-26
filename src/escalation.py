from dataclasses import dataclass
from .urgency_engine import UrgencyResult
from .safety_gateway import SafetyGatewayResult

@dataclass
class EscalationResult:
    escalation_level: str
    recommended_channel: str


def determine_escalation(urgency, safety):
    safety_triggered = False

    if isinstance(safety, dict):
        safety_triggered = safety.get("triggered", False)
    else:
        safety_triggered = bool(safety)

    if urgency == "Critical":
        return {
            "level": "Immediate",
            "action": "Immediate escalation to responsible clinician or emergency workflow",
            "channel": "Direct clinician notification / emergency escalation"
        }

    if urgency == "Urgent":
        return {
            "level": "Within hours",
            "action": "Priority clinician review within hours",
            "channel": "Urgent workflow queue"
        }

    if safety_triggered:
        return {
            "level": "Needs review",
            "action": "Clinician review recommended before routine handling",
            "channel": "Safety review queue"
        }

    return {
        "level": "Routine follow-up",
        "action": "Routine workflow follow-up",
        "channel": "Standard reporting workflow"
    }
