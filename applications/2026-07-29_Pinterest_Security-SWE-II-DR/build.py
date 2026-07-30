import sys, os
sys.path.insert(0, "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/2026-07-29_Pinterest_Security-SWE-II-DR"
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Security Software Engineer, Detection and Response")

dg.add_summary(doc,
    "Detection engineer who builds alerting and automation, not just tickets: a Python-based orchestration "
    "framework across nine SIEM/EDR platforms, 2,300+ MITRE ATT&CK-mapped detection rules, and production GenAI "
    "tooling for triage and rule generation. Comfortable managing logging pipelines end to end, onboarding new "
    "telemetry sources, and hunting for what the rules haven't caught yet."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection & Alerting Automation",
    "Python-based detection-as-code orchestration across nine SIEM/EDR platforms via native APIs (Microsoft "
    "Sentinel, Microsoft Defender, Google SecOps/Chronicle, Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo "
    "Alto XSIAM, Devo); full GitLab CI/CD pipeline with automated tests and staged rollout; production Python "
    "automation, not just scripts")
dg.add_skills_line(doc, "Telemetry & Logging Pipelines",
    "Data engineering/pipelining for 220+ unique log sources; 50+ Logstash filters and Elasticsearch Beats for "
    "log collection; Common Information Model standardizing field names/types across all parsed data; connector/"
    "collector health monitoring and onboarding")
dg.add_skills_line(doc, "MITRE ATT&CK, Threat Intel & Investigation",
    "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix; builds detection "
    "content informed directly by threat intel (Vedere Labs CTI); time-series anomaly detection of entity "
    "behavior (process chains, authentication patterns) for investigation support; analytically supports a "
    "live SOC's incident/case queue (Treasury SOC)")
dg.add_skills_line(doc, "AI-Assisted Security Workflows",
    "Production GenAI tooling for false-positive triage and automated detection-content generation/cross-"
    "platform rule conversion, built and validated against real analyst judgment before trusting the output")
dg.add_skills_line(doc, "Cloud & IAM",
    "Hands-on IAM policy/role implementation in AWS and GCP; API token/role/permission management across nine "
    "SIEM platforms; event-driven serverless enrichment on GCP")

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
dg.add_bullet(doc, "Data engineering/pipelining for 220+ unique log data sources: 50+ Logstash filters, deployed "
                   "Elasticsearch Beats for log collection, built a Common Information Model standardizing field "
                   "names/types across all parsed data, and assisted building 'Loggify,' a homegrown log "
                   "parsing/filtering tool that replaced Logstash.")
dg.add_bullet(doc, "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix; built "
                   "production GenAI tooling for detection-rule generation and cross-platform rule conversion; "
                   "time-series anomaly detection on entity behavior (process chains, authentication patterns) "
                   "to support investigations.")

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
dg.add_cover_paragraph(cl, "Security Engineering Hiring Team\nPinterest")
dg.add_cover_paragraph(cl,
    "Your posting asks for someone who builds alerts and automation, manages logging pipelines, and leverages AI "
    "to streamline security engineering — three things I've spent the last several years doing across nine "
    "different SIEM and EDR platforms."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built a Python-based orchestration framework spanning Sentinel, Defender, Google "
    "SecOps, Splunk, CrowdStrike, SentinelOne, Sumo Logic, XSIAM, and Devo — with reusable adapters, a full "
    "GitLab CI/CD pipeline, and staged rollout before anything hit production. Underneath that sits telemetry "
    "engineering for 220+ log sources and a Common Information Model standardizing schema across all of it — "
    "exactly the kind of logging-pipeline ownership and new-source onboarding your role calls for."
)
dg.add_cover_paragraph(cl,
    "I created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix, and I've built "
    "production GenAI tooling for false-positive triage and automated rule generation — running those AI-"
    "assisted workflows alongside manual analysis until I trusted the output, not before. I currently support "
    "Treasury's SOC directly against live incidents, building detection content informed by threat intel rather "
    "than reacting to it after the fact."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of detection automation, telemetry pipeline "
    "ownership, and AI-assisted security engineering fits Pinterest's Detection and Response team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Pinterest Security Software Engineer II package built.")
