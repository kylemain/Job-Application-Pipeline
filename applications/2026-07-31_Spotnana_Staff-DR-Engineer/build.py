import sys, os
sys.path.insert(0, "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/2026-07-31_Spotnana_Staff-DR-Engineer"
os.makedirs(OUT, exist_ok=True)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Staff Detection & Response Engineer — Detection-as-Code, SIEM & Incident Response")

dg.add_summary(doc,
    "Detection engineer with 8 years building and operating detection-as-code pipelines and incident response "
    "capabilities across multi-SIEM, multi-cloud environments. Owns the full detect-and-respond lifecycle — "
    "authoring version-controlled detection logic in CI/CD, investigating and triaging alerts end to end, and "
    "supporting incident response — with deep MITRE ATT&CK-mapped coverage across 2,300+ production detection rules."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection-as-Code & CI/CD",
    "Built a full CI/CD pipeline for detection-as-code in GitLab — version-controlled, peer-reviewed, tested "
    "(unit/integration) detection rules with staged/safe rollout before production; formally tracks coverage and "
    "false-positive-rate quality metrics")
dg.add_skills_line(doc, "Multi-SIEM & EDR Detection Authoring",
    "Custom detection rule authoring across nine SIEM platforms via native APIs — Splunk, Microsoft Sentinel, "
    "Google SecOps (Chronicle), CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo, and Elasticsearch/ES|QL "
    "— plus prior ArcSight experience; created and managed API tokens/roles/permissions across these platforms")
dg.add_skills_line(doc, "Incident Response & Threat Hunting",
    "Supports incident investigation and response for a live Treasury SOC, mapping alerts and threat-hunt findings "
    "to MITRE ATT&CK; integrates threat intelligence (indicators, TTPs, campaign context) directly into detection "
    "tuning and alert enrichment to speed triage and root-cause analysis")
dg.add_skills_line(doc, "Automation, Cloud & Identity",
    "Python automation and multithreaded orchestration across SIEM APIs; hands-on IAM policy/role implementation "
    "in AWS and GCP; comfortable working across AWS, GCP, and Azure security telemetry; Git version control")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — creates and manages detection/alerting content "
                   "(Splunk saved searches) supporting incident investigation and response for a live SOC.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new Elasticsearch-based detection "
                   "platform from scratch — ingestion, UEBA detection logic, data-quality alerting — end to end.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering team building signature, statistical, behavioral, "
                   "and ML-based detection content against massive customer telemetry using cloud-based big-data tooling.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework spanning nine "
                   "SIEM platforms — with automated tests, staged rollout, and quality-metric tracking (coverage, "
                   "false-positive rate) for every deployment.")
dg.add_bullet(doc, "Built pipelining and detection-authoring for 220+ ingested log sources and created/managed "
                   "2,300+ detection rules mapped to the MITRE ATT&CK matrix as a founding engineer at this startup.")
dg.add_bullet(doc, "Data engineered a Common Information Model (CIM) — a data dictionary standardizing schema "
                   "across every ingested source — and wrote detection rules directly against ES indexes as core "
                   "detection content, not just pipeline/ingestion work.")
dg.add_bullet(doc, "Developed GenAI-powered tooling for false-positive triage, detection-rule generation, and "
                   "cross-SIEM rule conversion as part of scaling detection-engineering throughput.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 31, 2026")
dg.add_cover_paragraph(cl, "Threat Detection & Response Hiring Team\nSpotnana")
dg.add_cover_paragraph(cl,
    "Detection logic that isn't version-controlled, tested, and safely rolled out is a liability waiting to "
    "happen. I built exactly that discipline as a founding engineer at a security startup: a full CI/CD pipeline "
    "for detection-as-code across nine SIEM platforms, with automated tests, staged rollout, and formal tracking "
    "of coverage and false-positive rate on every deployment — the same rigor a modern cloud-native detect-and-"
    "respond stack demands."
)
dg.add_cover_paragraph(cl,
    "That build included 2,300+ production detection rules mapped to the MITRE ATT&CK matrix, custom authoring "
    "against Elasticsearch, Splunk, Microsoft Sentinel, CrowdStrike, and Google SecOps via native APIs, and Python "
    "automation orchestrating rule deployment across every one of those platforms in parallel. On my current team, "
    "I support incident investigation and response for a live Treasury SOC, integrating threat intelligence "
    "directly into detection tuning and alert triage to drive faster root-cause analysis."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to bring that same detection-as-code discipline and full-lifecycle ownership — from "
    "authoring through investigation to response — to Spotnana's Threat Detection & Response team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Spotnana Staff Detection & Response Engineer package built.")
