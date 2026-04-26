# Report-to-Action AI
### Clinical Workflow Intelligence for Prioritization and Escalation in Medical Reporting

## Concept Brief
[From Report to Action: A Clinical AI Workflow Intelligence Layer for Prioritization and Escalation in Medical Reporting](paper/report_to_action_clinical_ai_workflow_intelligence.pdf)

## Live Demo
[Launch the Report-to-Action AI app](https://report-to-action-ai-xxtxaqkiou8nzqzvkaoru4.streamlit.app/)

---

## Overview

Report-to-Action AI is a clinical workflow intelligence prototype that transforms unstructured medical reports into actionable workflow decisions.

Rather than focusing on diagnosis, the system addresses a critical gap in clinical AI:

> Moving from **report interpretation → workflow action → safe escalation**

This project demonstrates how structured reasoning layers can support prioritization, uncertainty handling, and safe escalation in real-world clinical workflows.

**Design focus:** Safe, interpretable, and workflow-aligned clinical AI behavior under uncertainty.

---

## Core Concept

Clinical AI often stops at prediction.

This system models what happens *after* interpretation:

- Detect urgency signals  
- Identify uncertainty and quality issues  
- Apply a safety gateway  
- Recommend a workflow action  

---

## System Architecture

The pipeline follows a modular, decision-oriented structure:

1. **Report Parsing**  
   Extracts critical findings and uncertainty language  

2. **Urgency Engine**  
   Classifies reports into:  
   - Critical  
   - Urgent  
   - Routine  

3. **Quality Checker**  
   Detects:  
   - Missing clinical context  
   - Ambiguity  
   - Incomplete reporting  

4. **Safety Gateway**  
   Triggers escalation safeguards when:  
   - High-risk findings are present  
   - Uncertainty coexists with critical signals  
   - Key information is missing  

5. **Escalation Engine**  
   Determines:  
   - Escalation level  
   - Recommended action  
   - Communication channel  

6. **Explanation Layer**  
   Provides structured reasoning for decisions  

---

## Project Structure


```text
report-to-action-ai/
│
├── app.py                  # Streamlit interface
├── requirements.txt
├── README.md
│
├── src/
│   ├── report_parser.py    # Extract signals from report text
│   ├── urgency_engine.py   # Assign urgency level
│   ├── quality_checker.py  # Detect missing info / issues
│   ├── safety_gateway.py   # Trigger safety conditions
│   ├── escalation.py       # Determine escalation actions
│   ├── explanation.py      # Build reasoning output
│   └── sample_reports.py   # Example reports
│
├── paper/                  # (Optional) manuscript / writeup
└── assets/                 # Images / diagrams

```

## Installation

```bash
pip install -r requirements.txt
```

## Run 

```bash
streamlit run app.py
```

## Key Features

- Safety-aware workflow prioritization  
- Explicit uncertainty detection  
- Rule-based escalation logic  
- Transparent decision explanations  
- Audit trail for traceability  

---

## Example Output

**Input**

> CT abdomen and pelvis demonstrates free intraperitoneal air under the diaphragm with inflammatory changes near the sigmoid colon. Findings are concerning for bowel perforation. Recommend urgent surgical evaluation.


**System Output**

- **Urgency:** Critical  
- **Safety Gateway:** Triggered  
- **Escalation:** Immediate  
- **Action:** Direct clinician notification / emergency escalation  

---

## Why This Matters

Clinical workflows fail not only from missed diagnoses, but from:

- Delayed prioritization  
- Poor escalation  
- Uncertainty mismanagement  
- Incomplete communication  

This project reframes AI from:

> “What is the diagnosis?”  
to  
> “What should happen next, safely and reliably?”

---

## Potential Applications

- Radiology workflow prioritization  
- Critical results escalation systems  
- Clinical decision support layers  
- EHR-integrated workflow intelligence  
- Safety monitoring in AI-assisted care  

---

## Limitations

- Rule-based prototype (not ML-driven)  
- No real-world clinical validation yet  
- Simplified language parsing  
- Not integrated into live hospital systems  

---

## Future Directions

- Incorporation of NLP/LLM-based parsing  
- Integration with clinical data streams (EHR)  
- Probabilistic risk scoring  
- Human-in-the-loop escalation validation  
- Real-world pilot testing  

---

## Disclaimer

This is a research prototype for demonstration purposes only.  
It is not intended for clinical use, diagnosis, or patient management.

---

## Author

**Daniel Erhabor, MD, MPH**  
Physician and Clinical AI Systems Builder  
Focused on workflow, safety, and real-world deployment of clinical AI
