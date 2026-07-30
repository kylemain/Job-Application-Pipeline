import sys, os
sys.path.insert(0, "/sessions/peaceful-great-babbage/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/peaceful-great-babbage/mnt/Job-Application-Pipeline/applications/2026-07-30_Fluidstack_Staff-Detection-Engineer"
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Staff Detection Engineer")

dg.add_summary(doc,
    "Detection engineer who has built and run a detection engineering function end-to-end — telemetry to shipped "
    "detection to incident response — across cloud (AWS/GCP/Azure), endpoint, and identity sources. Built a "
    "Python-based detection-as-code orchestration framework spanning nine SIEM/EDR platforms with full CI/CD "
    "and staged rollout, and currently supports a live SOC's incident queue directly."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection-as-Code & Coverage Ownership",
    "Python-based detection-as-code orchestration across nine SIEM/EDR platforms via native APIs (Microsoft "
    "Sentinel, Microsoft Defender, Google SecOps/Chronicle, Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo "
    "Alto XSIAM, Devo, plus prior ArcSight); full GitLab CI/CD with automated unit/integration tests, version "
    "control, staged/safe rollout, and tracked coverage/precision/false-positive-rate metrics — detections "
    "shipped like software, never hand-edited in a console")
dg.add_skills_line(doc, "Multi-Cloud & Endpoint Telemetry",
    "Cloud security across AWS, GCP, and Azure (Sentinel/Defender API orchestration); data engineering for "
    "220+ log sources including CrowdStrike, Suricata, and Zeek endpoint/network telemetry; built a Common "
    "Information Model standardizing schema across all parsed data; hands-on IAM and API token/role/permission "
    "management across nine SIEM platforms")
dg.add_skills_line(doc, "Incident Response & Automation",
    "Analytically supports a live SOC's case/incident queue (Treasury SOC) end to end; built UEBA detection "
    "content on top of a from-scratch security data platform (DOE/NNSA); multithreaded automation to deploy "
    "detection content across many customers/environments in parallel; production Python for triage/enrichment "
    "automation, not scripts spec'd for someone else to build")
dg.add_skills_line(doc, "Threat Intel & Detection Tuning",
    "Detection content directly informed by threat intel (Vedere Labs CTI) rather than passive feed consumption; "
    "alert enrichment with CTI context (actor attribution, known-bad indicators) to speed triage; time-series "
    "anomaly detection on entity behavior (process chains, authentication patterns) for investigation support")
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
                   "layer, custom dashboards, and data-quality monitoring/alerting on top — a ground-up build, "
                   "not an inherited program.")

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

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Security Clearances: Top Secret (current, Treasury) · DOE Q Clearance · Public Trust (DOE)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 30, 2026")
dg.add_cover_paragraph(cl, "Security & Corp IT Hiring Team\nFluidstack")
dg.add_cover_paragraph(cl,
    "Your posting asks for someone who has built a detection engineering function, not just operated inside one "
    "— telemetry pipelines, detection-as-code, and incident response, owned end to end. That is precisely the "
    "shape of the work I have been doing for the last several years."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built a Python-based orchestration framework spanning nine SIEM and EDR platforms "
    "— Sentinel, Defender, Google SecOps, Splunk, CrowdStrike, SentinelOne, Sumo Logic, XSIAM, and Devo — with "
    "reusable per-technology adapters, API-level token/role management, and multithreaded parallel deployment, "
    "all running through a full GitLab CI/CD pipeline with automated tests and staged rollout before anything "
    "reached production. Underneath that sits telemetry engineering for 220+ log sources, including endpoint and "
    "network telemetry (CrowdStrike, Suricata, Zeek), and a Common Information Model standardizing schema across "
    "all of it — exactly the kind of foundation your team is building for a company whose attack surface spans "
    "corporate IT and gigawatt-scale infrastructure."
)
dg.add_cover_paragraph(cl,
    "More recently, at DOE/NNSA, I built a security data platform from scratch — ingesting CrowdStrike, Suricata, "
    "and Zeek into a new Elasticsearch environment and layering UEBA detection content, dashboards, and data-"
    "quality monitoring on top, with no inherited program to build from. I currently support Treasury's SOC "
    "directly against live incidents, building detection content informed by threat intel rather than reacting "
    "to it after the fact, and I've shipped production GenAI tooling for triage automation and cross-platform "
    "rule conversion — the kind of force-multiplier your team can use without proportional headcount growth."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of ground-up detection program building, "
    "multi-cloud telemetry engineering, and direct incident response experience fits Fluidstack's Security & "
    "Corp IT team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Fluidstack Staff Detection Engineer package built.")
