import sys, os
sys.path.insert(0, "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/2026-07-29_ScaleAI_Security-Engineer-DR"
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer, Detection & Response")

dg.add_summary(doc,
    "Detection engineer who treats detections as software: built a Python-based orchestration framework "
    "spanning nine SIEM/EDR platforms, ran it through a full CI/CD pipeline with version control, peer review, "
    "and staged rollout, and layered threat-intel enrichment and GenAI tooling on top. Comfortable owning the "
    "full loop from telemetry pipeline to shipped detection to incident investigation."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection Engineering as Software",
    "Python-based detection-as-code orchestration across nine SIEM/EDR platforms via native APIs (Microsoft "
    "Sentinel, Microsoft Defender, Google SecOps/Chronicle, Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo "
    "Alto XSIAM, Devo, plus prior ArcSight); full GitLab CI/CD pipeline with automated unit/integration tests, "
    "staged/safe rollout, and tracked coverage/precision/false-positive-rate metrics")
dg.add_skills_line(doc, "Telemetry Pipeline & Schema Engineering",
    "Data engineering for 220+ log sources; built a Common Information Model standardizing field names/types "
    "across all parsed data; 50+ Logstash filters and Elasticsearch Beats for collection; Apache Beam/GCP "
    "Dataflow for historical/cold-storage retrieval; connector/collector health monitoring")
dg.add_skills_line(doc, "Incident Response & Threat Intel Integration",
    "Analytically supports a live SOC's case/incident queue (Treasury SOC); builds detection content directly "
    "informed by threat intel (Vedere Labs CTI) rather than passively consuming feeds; enriches alerts with CTI "
    "context (actor attribution, known-bad indicators) to speed triage; time-series anomaly detection of entity "
    "behavior (auth patterns, process chains) for investigation support")
dg.add_skills_line(doc, "Cloud, IAM & Automation",
    "Hands-on IAM policy/role implementation in AWS and GCP; API token/role/permission management across nine "
    "SIEM platforms; event-driven serverless enrichment on GCP; multithreaded parallel deployment; comfortable "
    "Docker/container user; production-grade Python, not just scripts")
dg.add_skills_line(doc, "AI-Powered Security Tooling",
    "Production GenAI tooling for false-positive triage and automated detection-content generation/cross-"
    "platform rule conversion; reusable GenAI-powered \"skills\" for detection engineers")

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
dg.add_bullet(doc, "Fetched large volumes of historical cold-storage data using a homegrown Apache Beam program "
                   "run via GCP Dataflow; built production GenAI tooling for detection-rule generation and "
                   "cross-platform rule conversion; time-series anomaly detection on entity behavior (process "
                   "chains, authentication patterns) to support investigations.")
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
dg.add_cover_date(cl, "July 29, 2026")
dg.add_cover_paragraph(cl, "Security Engineering Hiring Team\nScale AI")
dg.add_cover_paragraph(cl,
    "Your posting describes detections as software — version control, peer review, measurable performance. "
    "That's exactly how I've operated for the last several years, just across a wider set of platforms than "
    "most detection engineers ever touch."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built a Python-based orchestration framework spanning nine SIEM and EDR platforms "
    "— Sentinel, Defender, Google SecOps, Splunk, CrowdStrike, SentinelOne, Sumo Logic, XSIAM, and Devo — with "
    "reusable per-technology adapters, API-level token/role management, and multithreaded parallel deployment, "
    "all running through a full GitLab CI/CD pipeline with automated tests and staged rollout before anything "
    "hit production. Underneath that sits telemetry engineering for 220+ log sources and a Common Information "
    "Model standardizing schema across all of it — the same mechanics behind mature, low-noise detection at scale."
)
dg.add_cover_paragraph(cl,
    "I currently support Treasury's SOC directly against live incidents, and I build detection content informed "
    "by threat intel rather than reacting to it after the fact — pulling CTI to tune rule logic and enrich "
    "alerts for faster triage. I've also shipped production GenAI tooling for false-positive triage and "
    "automated rule generation, the same class of AI-powered tooling this role is chartered to build and scale."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of platform-scale detection engineering, "
    "telemetry pipeline ownership, and incident response experience fits Scale AI's security engineering team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Scale AI Security Engineer, D&R package built.")
