import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Incident Commander")

dg.add_summary(doc,
    "Security engineer with 10+ years of hands-on technical investigation, MITRE ATT&CK-aligned detection "
    "content, and entity-behavior threat hunting supporting live SOC incident response — plus production GenAI "
    "tooling for automated triage and investigation. Currently directs sprint priorities and technical direction "
    "for the detection and alerting content a Treasury SOC runs incident response against."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Technical Investigation & Threat Hunting",
    "Deep, hands-on log/telemetry analysis to validate hypotheses and determine root cause; entity-behavior "
    "time-series anomaly detection (authentication anomalies by country/volume, parent/child process chains, "
    "Outlook process-chain analysis); DNS-based malware detection and mitigation")
dg.add_skills_line(doc, "MITRE ATT&CK-Aligned Detection Content",
    "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix; signature, "
    "behavioral, statistical, time-series, and ML-based detection content across cloud-scale customer data")
dg.add_skills_line(doc, "AI-Driven Response Tooling",
    "Production GenAI tooling for false-positive triage and automated detection-content generation; GenAI-driven "
    "SIEM API orchestration across nine platforms to speed investigation and response workflows")
dg.add_skills_line(doc, "SOC-Facing Technical Leadership",
    "Team-lead/sprint-lead directing detection and alerting priorities for a live SOC's incident response "
    "program; Python, GitLab CI/CD, multi-SIEM/EDR platform engineering (CrowdStrike, SentinelOne, Splunk, "
    "Google SecOps, and six others)")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead directing sprint priorities and "
                   "technical direction for the detection and alerting content (Splunk) a live SOC runs incident "
                   "response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection layer on top — "
                   "entity-behavior analytics purpose-built for proactive threat hunting and investigation.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data "
                   "supporting downstream incident response and investigation.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms — including CrowdStrike, SentinelOne, and Google SecOps (Chronicle) — via "
                   "native APIs, with multithreading to deploy and manage detection content across many "
                   "customers in parallel inside a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Investigated anomalous entity behavior at scale for threat hunting and incident support: "
                   "authentication-attempt anomalies by country/volume, parent/child process chains, and "
                   "Outlook process-chain analysis.")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for false-positive "
                   "triage, automated detection-rule generation, and cross-platform rule conversion.")
dg.add_bullet(doc, "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections on the network; analyzed "
                   "large-scale security log data to surface anomalous behavior for incident investigation.")

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
dg.add_cover_paragraph(cl, "Incident Command Hiring Team\nUber")
dg.add_cover_paragraph(cl,
    "Getting to root cause fast, under pressure, with incomplete information is the daily reality of detection "
    "engineering work — and it's the same instinct this role is built around at a much larger scale."
)
dg.add_cover_paragraph(cl,
    "I currently direct sprint priorities and technical direction for the detection and alerting content a "
    "Treasury SOC runs its incident response against, and built the entity-behavior analytics layer (UEBA) on "
    "top of a from-scratch security data platform for DOE/NNSA — purpose-built for proactive threat hunting. "
    "Earlier, at Trend Micro/Cysiv, I investigated anomalous entity behavior at scale for threat hunting and "
    "incident support: authentication anomalies by country and volume, parent/child process chains, and Outlook "
    "process-chain analysis, on top of 2,300+ detection rules I created and managed covering most of the MITRE "
    "ATT&CK matrix."
)
dg.add_cover_paragraph(cl,
    "I've also built production GenAI tooling for security automation — prompt engineering for triage and "
    "automated detection-rule generation — the same class of AI-assisted investigation and response tooling "
    "this role is chartered to mature."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of deep technical investigation, MITRE ATT&CK-"
    "aligned detection engineering, and AI-driven tooling fits Uber's incident response program."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Uber Incident Commander package built.")
