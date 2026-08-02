import sys, os
sys.path.insert(0, "/sessions/keen-zen-rubin/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/keen-zen-rubin/mnt/Job-Application-Pipeline/applications/2026-08-01_Roblox_Principal-Detection-Response-Engineer"
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection & Response Engineer")

dg.add_summary(doc,
    "Detection and response engineer with 12 years of security experience, including 8+ years building custom "
    "security data pipelines, multi-platform detection content, and incident response programs across DOE/NNSA, "
    "Treasury's SOC, and Trend Micro/Cysiv. Built production ETL pipelines (PySpark, GCP Dataproc, BigQuery, "
    "Apache Beam/Dataflow) ingesting 220+ log sources, a nine-platform SIEM/EDR detection-as-code orchestration "
    "framework, and currently supports a live SOC's incident queue end to end."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Security Data Engineering & ETL Pipelines",
    "Designed and built production-grade ETL/streaming data pipelines end to end: PySpark and GCP Dataproc for "
    "large-scale analysis, BigQuery for warehousing/analytics, Apache Beam/GCP Dataflow for historical and "
    "streaming data retrieval; hands-on exposure to Kafka and Flink streaming jobs; pipelining for 220+ unique "
    "log sources with a Common Information Model standardizing schema across all parsed data")
dg.add_skills_line(doc, "Detection Engineering, SIEM & EDR",
    "Built and ran custom threat detection systems tuned for low false positives across nine SIEM/EDR/NDR "
    "platforms via native APIs (Microsoft Sentinel, Microsoft Defender, Google SecOps/Chronicle, Splunk, "
    "CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo, plus prior ArcSight) — including CrowdStrike "
    "and SentinelOne EDR log onboarding and custom detection/automation build-out; created and managed 2,300+ "
    "detection rules covering most of the MITRE ATT&CK matrix; deep Elasticsearch detection-rule, query (DSL), "
    "and transform experience")
dg.add_skills_line(doc, "Incident Response & Security Operations",
    "Actively supports Treasury's SOC (TSSOC) incident/case queue as a Threat & Research team lead, building and "
    "managing the Splunk-based detection and alerting content investigators run against; built the UEBA "
    "detection layer, dashboards, and data-quality alerting for a security data platform built from scratch at "
    "DOE/NNSA ingesting CrowdStrike, Suricata, and Zeek; threat hunting informed directly by threat intel "
    "(Vedere Labs CTI)")
dg.add_skills_line(doc, "Automation, Orchestration & Response Tooling",
    "Python-based orchestration framework: multithreaded parallel rule deployment, full GitLab CI/CD with "
    "automated tests and staged/safe rollout, tracked coverage/precision/false-positive-rate metrics; "
    "production GenAI tooling for false-positive triage and cross-platform rule conversion — a lightweight "
    "SOAR-style automation layer")
dg.add_skills_line(doc, "Cross-Domain Depth",
    "Network protocol/NDR telemetry (Suricata, Zeek); multi-cloud (AWS, GCP, Azure — Sentinel/Defender API "
    "orchestration); containers (Docker, Kubernetes-orchestrated platform experience); cloud IAM and API "
    "token/role/permission management across nine SIEM platforms")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead building and managing the "
                   "Splunk-based detection/alerting content a live SOC runs incident investigations against; "
                   "conducts structured incident response and root-cause analysis on flagged cases.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform from "
                   "scratch ingesting CrowdStrike, Suricata, and Zeek into Elasticsearch, including the UEBA "
                   "detection layer, custom Kibana dashboards, and data-quality monitoring/alerting.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building cloud-based, "
                   "big-data detection content against massive customer telemetry, tuned using threat intel "
                   "from Vedere Labs, Forescout's in-house research team.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built a Python-based detection-as-code orchestration framework across nine SIEM/EDR "
                   "platforms via native APIs — including CrowdStrike and SentinelOne EDR — with multithreaded "
                   "parallel deployment across customers, full GitLab CI/CD, automated tests, and staged "
                   "rollout before production; created and managed 2,300+ detection rules covering most of the "
                   "MITRE ATT&CK matrix while tracking and minimizing false-positive rates.")
dg.add_bullet(doc, "Designed and built ETL data pipelines end to end for 220+ unique log sources: "
                   "PySpark/SparkSQL on GCP Dataproc clusters, 50+ Logstash filters, Elasticsearch Beats log "
                   "collection, a Common Information Model standardizing schema across all parsed data, and a "
                   "homegrown Apache Beam program on GCP Dataflow for historical cold-storage retrieval.")

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
dg.add_cover_date(cl, "August 1, 2026")
dg.add_cover_paragraph(cl, "Detection & Response Hiring Team\nRoblox")
dg.add_cover_paragraph(cl,
    "Roblox's Detection & Response team needs someone who can design custom security data pipelines, build "
    "detection strategies that keep false positives low, and lead real-time incident response — not adjacent "
    "skills, but the exact work I've been doing across Experian, DOE/NNSA, Treasury's SOC, and Trend Micro/Cysiv "
    "over a 12-year security career."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built ETL data pipelines end to end for 220+ log sources — PySpark and SparkSQL "
    "analysis on GCP Dataproc, a homegrown Apache Beam program on GCP Dataflow for historical retrieval, and a "
    "Common Information Model standardizing schema across everything ingested — the same shape of work your "
    "team needs to keep Roblox's security data pipeline systems running at scale. On top of that data "
    "foundation, I built a Python-based detection-as-code orchestration framework spanning nine SIEM and EDR "
    "platforms, including CrowdStrike and SentinelOne, with multithreaded parallel deployment, full CI/CD, "
    "automated testing, and staged rollout — and created and managed 2,300+ detection rules covering most of "
    "the MITRE ATT&CK matrix while actively tracking false-positive rates."
)
dg.add_cover_paragraph(cl,
    "More recently, at DOE/NNSA I built a security data platform from scratch — ingesting CrowdStrike, "
    "Suricata, and Zeek into a new Elasticsearch environment and layering UEBA detection, dashboards, and "
    "data-quality monitoring on top — and I currently support Treasury's SOC directly against live incidents as "
    "a Threat & Research team lead, building the detection and alerting content investigators run against every "
    "day. I'd bring that same combination of pipeline engineering, multi-platform detection ownership, and "
    "hands-on incident response to Roblox's mission of keeping its community and enterprise safe."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how this experience maps to the Principal Detection and Response "
    "Engineer role."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Roblox Principal Detection and Response Engineer package built.")
