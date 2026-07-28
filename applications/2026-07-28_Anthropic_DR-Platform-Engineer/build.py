import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Security Software Engineer, Detection & Response Platform")

dg.add_summary(doc,
    "Security engineer who has built an internal detection-management platform from scratch: a Python-based "
    "orchestration layer spanning nine SIEM/EDR platforms, backed by data pipelines ingesting 220+ log sources "
    "and a full GitLab CI/CD delivery pipeline. Comfortable building and scaling services on cloud infrastructure, "
    "with production GenAI tooling layered directly on top of the detection platform."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Security Platform Engineering",
    "Architected a Python-based detection-as-code orchestration framework across nine SIEM/EDR platforms via "
    "native APIs — effectively an internal detection-management platform/abstraction layer across heterogeneous "
    "vendors; API token/role/permission management; multithreaded parallel deployment")
dg.add_skills_line(doc, "Data Pipelines at Scale",
    "Data engineering for 220+ log data sources; built a Common Information Model standardizing field "
    "names/types across all parsed data; Apache Beam / GCP Dataflow for historical/cold-storage retrieval; "
    "PySpark/SparkSQL and GCP Dataproc for large-scale exploratory analysis")
dg.add_skills_line(doc, "CI/CD & Cloud Services",
    "Full CI/CD pipeline for detection-as-code, run in GitLab, with automated unit/integration tests written "
    "against the orchestration framework itself; hands-on IAM policy/role implementation in AWS and GCP; built "
    "event-driven serverless enrichment on GCP; comfortable Docker/container user; familiarity with Kafka/Flink "
    "streaming pipelines")
dg.add_skills_line(doc, "AI-Powered Security Tooling",
    "Production GenAI tooling for false-positive triage and automated detection-content generation; built "
    "reusable GenAI-powered 'skills' for detection engineers to automate repetitive tasks")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead directing sprint priorities and "
                   "technical direction for the Splunk-based detection and alerting content a live SOC runs "
                   "incident response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform from "
                   "scratch ingesting CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection "
                   "layer, custom dashboards, data transforms, and data-quality monitoring/alerting on top.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building cloud-based big-data "
                   "detection content and infrastructure against massive customer telemetry.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms via native APIs — developing reusable per-technology adapters for every "
                   "interaction method (rule management, alerts, tables, schemas) — with multithreading to deploy "
                   "detection content across many customers in parallel inside a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Data engineering/pipelining for 220+ unique log data sources: 50+ Logstash filters, deployed "
                   "Elasticsearch Beats for log collection, built a Common Information Model standardizing field "
                   "names/types across all parsed data, and assisted building 'Loggify,' a homegrown log "
                   "parsing/filtering tool that replaced Logstash.")
dg.add_bullet(doc, "Fetched large volumes of historical cold-storage data using a homegrown Apache Beam program "
                   "run via GCP Dataflow; built production GenAI tooling for detection-rule generation and "
                   "cross-platform rule conversion.")
dg.add_bullet(doc, "Created and managed API tokens, roles, and permissions across the nine SIEM platforms; "
                   "created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix.")

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
dg.add_cover_paragraph(cl, "Security Hiring Team\nAnthropic")
dg.add_cover_paragraph(cl,
    "I've effectively built the kind of internal detection platform this role is chartered to create — just "
    "across a different set of underlying SIEM vendors rather than a single in-house system."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I architected a Python-based orchestration framework spanning nine SIEM and EDR "
    "platforms via their native APIs — reusable per-technology adapters, API-level token/role/permission "
    "management, and multithreaded parallel deployment across many customers inside a full GitLab CI/CD "
    "pipeline. Underneath that platform sits data engineering for 220+ log sources: 50+ parsing filters, a "
    "Common Information Model standardizing fields across all of it, and Apache Beam/GCP Dataflow jobs for "
    "large-scale historical retrieval."
)
dg.add_cover_paragraph(cl,
    "On top of that foundation, I built production GenAI tooling — automated detection-rule generation, "
    "cross-platform rule conversion, and false-positive triage — the same class of AI-powered security tooling "
    "this platform is meant to scale."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of platform engineering, large-scale data "
    "pipelines, and AI-powered detection tooling fits Anthropic's Detection Platform team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Anthropic D&R Platform Engineer package built.")
