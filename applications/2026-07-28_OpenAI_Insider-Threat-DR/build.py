import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Security Engineer, Detection & Response")

dg.add_summary(doc,
    "Security engineer with 10+ years building detection content and investigating anomalous entity behavior at "
    "scale — authentication anomalies, process-chain analysis, data-movement patterns — plus production GenAI "
    "tooling for automated triage. Comfortable across macOS/Windows/Linux endpoints and multi-cloud "
    "infrastructure, with Python as a daily working language."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Entity-Behavior Detection & Investigation",
    "Time-series anomaly detection: authentication attempts by country/volume, parent/child process chains, "
    "Outlook process-chain analysis; DNS-based malware detection and mitigation; deep log/telemetry investigation "
    "to validate hypotheses and reach root cause")
dg.add_skills_line(doc, "AI-Accelerated Investigation Tooling",
    "Production GenAI tooling for false-positive triage and automated detection-content generation; built "
    "reusable GenAI-powered 'skills' for detection engineers to automate repetitive investigative tasks")
dg.add_skills_line(doc, "Cross-Platform Detection Engineering",
    "2,300+ detection rules across the MITRE ATT&CK matrix; multi-SIEM/EDR orchestration (CrowdStrike, "
    "SentinelOne, Splunk, Google SecOps, and six others) via native APIs; formally tracks detection quality "
    "metrics and tunes rules for sustainable operations; hands-on experience working within a "
    "Kubernetes-orchestrated platform plus comfortable Docker/container use")
dg.add_skills_line(doc, "Data Engineering & Scripting",
    "Python-based automation and orchestration; data pipelines ingesting 220+ log sources; GitLab CI/CD for "
    "detection-as-code; cloud IAM policy/role implementation in AWS and GCP")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — direct sprint priorities and technical "
                   "direction for the detection and alerting content a live SOC runs incident response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA entity-behavior detection "
                   "layer on top — purpose-built to catch anomalous access and data-movement patterns.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, and ML-based detection content against cloud-scale customer telemetry.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Investigated anomalous entity behavior at scale: authentication-attempt anomalies by "
                   "country/volume, parent/child process chains, and Outlook process-chain analysis — the same "
                   "behavioral-analytics techniques central to detecting access abuse and data exfiltration.")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for false-positive "
                   "triage and automated detection-rule generation, reducing manual investigation toil.")
dg.add_bullet(doc, "Architected a Python-based detection-as-code orchestration framework across nine SIEM/EDR "
                   "platforms via native APIs, including token/role/permission management at the API level, "
                   "inside a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Data engineering for 220+ log sources; created and managed 2,300+ detection rules covering "
                   "most of the MITRE ATT&CK matrix.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections on the network; analyzed "
                   "large-scale security log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Security Clearances: Top Secret (current, Treasury) · DOE Q Clearance · Public Trust (DOE)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 28, 2026")
dg.add_cover_paragraph(cl, "Security Hiring Team\nOpenAI")
dg.add_cover_paragraph(cl,
    "Spotting the anomaly that matters inside a sea of normal behavior — and proving it out fast — is the core "
    "skill I've built a career on, and it's the same instinct insider-risk investigations depend on."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I investigated anomalous entity behavior at scale for threat hunting and incident "
    "support: authentication-attempt anomalies by country and volume, parent/child process chains, and Outlook "
    "process-chain analysis — the same class of behavioral analytics that surfaces access abuse and unusual data "
    "movement. I built that analysis on top of a Python-based detection-as-code framework I architected across "
    "nine SIEM/EDR platforms, and created 2,300+ detection rules covering most of the MITRE ATT&CK matrix."
)
dg.add_cover_paragraph(cl,
    "I've also shipped production GenAI tooling for security automation — prompt engineering for triage and "
    "automated detection-content generation — cutting the manual work out of investigations, which is exactly "
    "the kind of AI-assisted leverage this role is chartered to bring to insider-threat work."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of entity-behavior investigation, detection "
    "engineering, and AI-driven tooling fits OpenAI's insider-threat program."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("OpenAI Insider Threat D&R package built.")
