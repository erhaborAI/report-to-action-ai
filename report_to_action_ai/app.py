import streamlit as st
import pandas as pd

from src.sample_reports import SAMPLE_REPORTS
from src.report_parser import parse_report
from src.urgency_engine import classify_urgency
from src.quality_checker import check_quality
from src.safety_gateway import run_safety_gateway
from src.escalation import determine_escalation
from src.explanation import build_explanation


st.set_page_config(
    page_title="Report-to-Action AI",
    page_icon="🧠",
    layout="wide"
)

st.title("Report-to-Action AI")

st.header(
    "Clinical Workflow Intelligence for Prioritization and Escalation in Medical Reporting"
)

st.write(
    "This prototype demonstrates a clinical workflow intelligence layer that reads a medical report, "
    "detects urgency signals, identifies uncertainty or quality issues, and recommends a workflow action. "
    "It is not a diagnostic tool. It is a safety-aware workflow prioritization simulator."
)

selected = st.selectbox("Choose an example", list(SAMPLE_REPORTS.keys()))

default_report = SAMPLE_REPORTS[selected]

report_text = st.text_area(
    "Paste medical report",
    value=default_report,
    height=220
)

if st.button("Analyze report"):
    parsed = parse_report(report_text)
    urgency = classify_urgency(parsed)
    quality = check_quality(parsed, urgency)
    safety = run_safety_gateway(parsed, urgency, quality)
    escalation = determine_escalation(urgency.urgency, safety)

    explanation = build_explanation(
        parsed,
        urgency,
        quality,
        safety,
        escalation
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Urgency", urgency.urgency)
    col2.metric("Urgency Score", urgency.score)
    col3.metric(
        "Safety Gateway",
        "Triggered" if safety.triggered else "Not triggered"
    )
    col4.metric("Escalation", escalation["level"])

    st.divider()

    st.subheader("Workflow Action")
    st.success(escalation["action"])

    st.subheader("Explanation")
    st.write(explanation)

    st.subheader("Extracted Signals")

    signal_data = pd.DataFrame(
        {
            "Category": [
                "Critical terms",
                "Uncertainty terms",
                "Negated critical terms"
            ],
            "Detected": [
                ", ".join(parsed.critical_terms) if parsed.critical_terms else "None",
                ", ".join(parsed.uncertainty_terms) if parsed.uncertainty_terms else "None",
                ", ".join(parsed.negated_critical_terms) if parsed.negated_critical_terms else "None",
            ],
        }
    )

    st.dataframe(signal_data, use_container_width=True)

    st.subheader("Quality and Missing Information")

    q_col1, q_col2 = st.columns(2)

    with q_col1:
        st.markdown("### Quality flags")
        if quality.quality_flags:
            for flag in quality.quality_flags:
                st.warning(flag)
        else:
            st.write("No major quality flags detected.")

    with q_col2:
        st.markdown("### Missing information")
        if quality.missing_information:
            for item in quality.missing_information:
                st.info(item)
        else:
            st.write("No major missing information detected.")

    st.subheader("Audit Trail")

    audit_data = pd.DataFrame(
        {
            "Step": [
                "1. Report parsing",
                "2. Urgency classification",
                "3. Quality check",
                "4. Safety gateway",
                "5. Escalation decision",
            ],
            "Result": [
                f"{len(parsed.critical_terms)} active critical terms, {len(parsed.uncertainty_terms)} uncertainty terms",
                f"{urgency.urgency} with score {urgency.score}",
                f"{len(quality.quality_flags)} quality flags, {len(quality.missing_information)} missing info items",
                (
                    "Triggered: " + ", ".join(safety.reasons)
                    if safety.triggered
                    else "Not triggered"
                ),
                f"{escalation['level']}: {escalation['channel']}",
            ],
        }
    )

    st.dataframe(audit_data, use_container_width=True)

    st.subheader("Potential Risks / Failure Modes")

    st.markdown(
        """
        - Missed negation, for example “no perforation”
        - Ambiguous clinical language
        - Incomplete reports
        - Over-triggering escalation in uncertain cases
        - Rule-based limitations before real-world validation
        """
    )

    st.divider()

    st.caption(
        "Research prototype only. Not intended for clinical use, diagnosis, or patient management."
    )