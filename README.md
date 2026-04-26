# Report-to-Action AI

## Clinical Workflow Intelligence for Prioritization and Escalation in Medical Reporting

Report-to-Action AI is a research prototype that demonstrates how a clinical workflow intelligence layer can convert unstructured medical reports into workflow-relevant actions.

The system does not diagnose patients. Instead, it evaluates whether a report contains signals that should affect workflow behavior, including urgency, escalation need, uncertainty, missing context, and safety-gateway triggers.

## Why this matters

Many clinical AI systems focus on prediction. Real clinical environments require more than prediction. They require systems that can help determine which information needs attention, which cases should be escalated, and when uncertainty should prevent premature reassurance.

This project demonstrates a workflow layer that sits between report text and clinical action.

## Core functions

- Parse report text
- Detect critical findings and uncertainty language
- Classify urgency
- Identify report quality issues
- Trigger a safety gateway when risk or uncertainty is high
- Recommend escalation workflow
- Generate an audit trail

## Project structure

```text
report_to_action_ai/
├── app.py
├── requirements.txt
├── README.md
├── src/
│   ├── report_parser.py
│   ├── urgency_engine.py
│   ├── quality_checker.py
│   ├── safety_gateway.py
│   ├── escalation.py
│   ├── explanation.py
│   └── sample_reports.py
└── paper/
    └── manuscript_outline.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

## Example output

Input:

> CT abdomen and pelvis demonstrates free intraperitoneal air under the diaphragm with inflammatory changes near the sigmoid colon. Findings are concerning for bowel perforation. Recommend urgent surgical evaluation.

Output:

- Urgency: Critical
- Safety gateway: Triggered
- Escalation: Immediate
- Final action: Immediate escalation to responsible clinician or emergency workflow

## Research positioning

Working paper title:

**From Report to Action: A Clinical Workflow Intelligence Layer for Prioritization and Escalation in Medical Reporting**

Core claim:

Clinical AI should not stop at prediction or text summarization. In real clinical environments, AI systems must help govern workflow behavior under uncertainty by prioritizing reports, escalating high-risk findings, identifying ambiguity, and producing an auditable rationale for action.

## Disclaimer

This is a research and education prototype only. It is not intended for clinical use, diagnosis, treatment, or patient management.
