import sys, os
sys.path.insert(0, "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/2026-07-29_6sense_Staff-Security-Engineer-SecOps"
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Staff Security Engineer, SecOps & Threats")

dg.add_summary(doc,
    "Detection and automation engineer with deep MITRE ATT&CK-mapped detection content (2,300+ rules) and a "
    "Python-based orchestration framework spanning nine SIEM/EDR platforms, built through a full CI/CD pipeline "
    "with staged rollout and tracked coverage/precision metrics. Builds the tools that let a security team operate "
    "at speed and scale, with hands-on AWS/GCP IAM and live SOC incident support behind it."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Security Automation & Tooling",
    "Python-based detection-as-code orchestration across nine SIEM/EDR platforms via native APIs (Microsoft "
    "Sentinel, Microsoft Defender, Google SecOps/Chronicle, Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo "
    "Alto XSIAM, Devo, plus prior ArcSight); full GitLab CI/CD pipeline with automated unit/integration tests, "
    "staged/safe rollout, and tracked coverage/precision/false-positive-rate metrics")
dg.add_skills_line(doc, "MITRE ATT&CK & Detection Engineering",
    "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix; signature, statistical, "
    "behavioral, and ML-based detection content; time-series anomaly detection of entity behavior (auth patterns, "
    "process chains) for investigation support")
dg.add_skills_line(doc, "Cloud, IAM & Vulnerability Data",
    "Hands-on IAM policy/role implementation in AWS and GCP; API token/role/permission management across nine "
    "SIEM platforms; ingested Tenable vulnerability scan data into a SIEM and built analytics/detection content on "
    "top of it; event-driven serverless enrichment on GCP")
dg.add_skills_line(doc, "Incident Response & Threat Intel Integration",
    "Analytically supports a live SOC's case/incident queue (Treasury SOC); builds detection content directly "
    "informed by threat intel (Vedere Labs CTI) rather than passively consuming feeds; enriches alerts with CTI "
    "context (actor attribution, known-bad indicators) to speed triage")
dg.add_skills_line(doc, "AI-Powered Security Tooling",
    "Production GenAI tooling for false-positive triage and automated detection-content generation/cross-platform "
    "rule conversion; reusable GenAI-powered \"skills\" for detection engineers")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead directing sprint priorities and "
                   "technical direction for the Splunk-based detection and alerting content a live SOC runs "
                   "incident investigations against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform from "
                   "scratch ingesting CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection "
                   "layer, custom dashboards, data transforms, and data-quality monitoring/alerting on top.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building cloud-based big-data "
                   "detection content and infrastructure against massive customer telemetry; threat intel "
                   "sourced from Vedere Labs, Forescout's in-house research team, informed detection tuning.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms via native APIs — reusable per-technology adapters for every interaction "
                   "method (rule management, alerts, tables, schemas) — with multithreading to deploy detection "
                   "content across many customers in parallel inside a full GitLab CI/CD pipeline, including "
                   "automated unit/integration tests and staged rollout before full production deployment.")
dg.add_bullet(doc, "Created and managed API tokens, roles, and permissions across the nine SIEM platforms; "
                   "created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix.")
dg.add_bullet(doc, "Data engineering/pipelining for 220+ unique log data sources; built production GenAI tooling "
                   "for detection-rule generation and cross-platform rule conversion; time-series anomaly "
                   "detection on entity behavior (process chains, authentication patterns) to support "
                   "investigations.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections on the network; analyzed "
                   "large-scale security log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Security Clearances: Top Secret (current, Treasury) · DOE Q Clearance · Public Trust (DOE)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 29, 2026")
dg.add_cover_paragraph(cl, "Security Operations & Threat Management Hiring Team\n6sense")
dg.add_cover_paragraph(cl,
    "Your team's mandate — protecting 6sense through prevention, detection, investigation, and response, while "
    "building the tools that let the team operate at speed and scale — maps directly onto how I've spent the "
    "last several years: building automation and detection infrastructure, not just running it."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built a Python-based orchestration framework spanning nine SIEM and EDR platforms "
    "— Sentinel, Defender, Google SecOps, Splunk, CrowdStrike, SentinelOne, Sumo Logic, XSIAM, and Devo — with "
    "reusable adapters, API-level token/role management, and multithreaded parallel deployment, all running "
    "through a full GitLab CI/CD pipeline with automated tests and staged rollout. I created and managed 2,300+ "
    "detection rules covering most of the MITRE ATT&CK matrix, and I've used that same ATT&CK fluency to inform "
    "investigations and anomaly detection, not just build a rule library."
)
dg.add_cover_paragraph(cl,
    "I currently support Treasury's SOC directly against live incidents, and I build detection content informed "
    "by threat intel rather than reacting to it after the fact. I've also shipped production GenAI tooling for "
    "false-positive triage and automated rule generation — the same class of AI-powered automation your team "
    "is chartered to build."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of multi-platform security automation, "
    "MITRE ATT&CK-based detection engineering, and live incident response fits 6sense's SecOps & Threats team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("6sense Staff Security Engineer package built.")
