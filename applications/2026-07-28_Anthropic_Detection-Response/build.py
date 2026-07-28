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
    "Security engineer with 10+ years of detection engineering, incident response, and threat hunting — leading "
    "sprint priorities for a live SOC's detection content, building production GenAI tooling for triage and "
    "investigation, and orchestrating detection-as-code across nine SIEM/EDR platforms. Comfortable across AWS "
    "and GCP, with hands-on cloud IAM implementation."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Incident Response & Detection Engineering",
    "Directs detection and alerting content a live SOC runs incident response against; reviews detection quality "
    "metrics (coverage, precision/false-positive rate) and drives continuous improvement via staged rollout; "
    "2,300+ detection rules covering most of the MITRE ATT&CK matrix; signature, behavioral, statistical, "
    "time-series, and ML-based detection content")
dg.add_skills_line(doc, "LLM-Powered Detection & Response Tooling",
    "Production GenAI tooling for false-positive triage and automated detection-content generation; GenAI-driven "
    "SIEM API orchestration; built reusable GenAI-powered 'skills' automating repetitive detection-engineering "
    "workflows")
dg.add_skills_line(doc, "Multi-SIEM/EDR Orchestration & CI/CD",
    "Python-based orchestration framework across nine platforms (Sentinel, Defender, Google SecOps, Splunk, "
    "CrowdStrike, SentinelOne, Sumo Logic, XSIAM, Devo) via native APIs; multithreaded parallel deployment inside "
    "a full GitLab CI/CD pipeline; API-level token/role/permission management")
dg.add_skills_line(doc, "Cloud & Data Engineering",
    "Hands-on IAM policy/role implementation in AWS and GCP; data pipelines ingesting 220+ log sources; hands-on "
    "experience working within a Kubernetes-orchestrated platform plus Docker for reproducible detection-testing "
    "environments; comfortable with Python and SQL/query languages at scale")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead directing sprint priorities and "
                   "technical direction for the detection and alerting content a live SOC runs incident response "
                   "against; owns Incident Response metrics/procedures for that content.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection layer, data-quality "
                   "monitoring, and alerting content on top.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer "
                   "telemetry.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms via native APIs, with multithreading to deploy and manage detection content "
                   "across many customers in parallel inside a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for false-positive "
                   "triage, automated detection-rule generation, and cross-platform rule conversion — directly "
                   "analogous to leveraging LLMs to enhance detection, investigation, and response.")
dg.add_bullet(doc, "Created and managed API tokens, roles, and permissions across nine SIEM platforms as part of "
                   "the orchestration framework; investigated anomalous entity behavior at scale for threat "
                   "hunting (authentication anomalies, process-chain analysis).")
dg.add_bullet(doc, "Data engineering for 220+ log sources; created and managed 2,300+ detection rules covering "
                   "most of the MITRE ATT&CK matrix.")

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
dg.add_cover_paragraph(cl, "Security Hiring Team\nAnthropic")
dg.add_cover_paragraph(cl,
    "Building the detections and playbooks that let a team catch what matters fast, and layering AI onto that "
    "work to catch it faster, is exactly the shape of my last decade in security engineering."
)
dg.add_cover_paragraph(cl,
    "I currently direct sprint priorities and technical direction for the detection and alerting content a "
    "Treasury SOC runs its incident response against. Earlier, at Trend Micro/Cysiv, I architected a Python-based "
    "orchestration framework managing detection-rule lifecycle across nine SIEM and EDR platforms via their "
    "native APIs — including API-level token/role/permission management and multithreaded parallel deployment "
    "inside a full GitLab CI/CD pipeline — on top of which I created and maintain 2,300+ detection rules covering "
    "most of the MITRE ATT&CK matrix."
)
dg.add_cover_paragraph(cl,
    "I've also built production GenAI tooling that triages false positives, generates detection content, and "
    "converts rules between SIEM syntaxes automatically — the same direction of using LLMs to enhance detection, "
    "investigation, and response that this role is built to lead."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of incident response leadership, multi-platform "
    "detection engineering, and LLM-driven tooling fits Anthropic's Detection & Response work."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Anthropic Detection & Response package built.")
