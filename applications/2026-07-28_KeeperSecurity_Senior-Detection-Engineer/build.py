import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection Engineer — SIEM & Security Observability")

dg.add_summary(doc,
    "Senior detection engineer with 10+ years building SIEM detection content, telemetry pipelines, and "
    "security observability across nine SIEM/EDR platforms. Deep hands-on Splunk background (certified) "
    "paired with detection-as-code delivery through full CI/CD pipelines and MITRE ATT&CK coverage mapping."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "SIEM & Detection Engineering",
    "Splunk (certified), ELK/Elasticsearch, CrowdStrike, SentinelOne, Microsoft Sentinel/Defender, Google "
    "SecOps, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight; MITRE ATT&CK coverage mapping; detection rule "
    "development — signature, statistical, behavioral, aggregation/threshold, ML-based")
dg.add_skills_line(doc, "Telemetry & Log Pipelines",
    "220+ ingested log sources; 50+ Logstash filters for parsing/normalization; Common Information Model "
    "data-dictionary design standardizing field names/types across all parsed data; connector/collector "
    "health monitoring")
dg.add_skills_line(doc, "Automation & CI/CD", "Python, SQL; GitLab CI/CD detection-as-code pipelines; GenAI-"
    "powered triage automation and cross-SIEM rule conversion tooling")
dg.add_skills_line(doc, "Cloud & Data Science", "AWS, GCP, Azure; clustering/unsupervised ML, time-series "
    "anomaly detection, UEBA detection content")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — own the detection and alerting content "
                   "(Splunk saved searches) the SOC runs day-to-day incident response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the detection/analytics layer on "
                   "top — dashboards, data transforms, UEBA content, data-quality alerting.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and quality work across a combined Elasticsearch "
                   "and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built detection-as-code orchestration across nine SIEM/EDR platforms — including CrowdStrike "
                   "and SentinelOne — via native APIs, run through a full GitLab CI/CD pipeline; created and "
                   "managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix.")
dg.add_bullet(doc, "Data engineering/pipelining for 220+ log sources: 50+ Logstash filters for parsing and "
                   "normalization, deployed Elasticsearch Beats for log collection, built a Common Information "
                   "Model standardizing field names/types across all parsed data.")
dg.add_bullet(doc, "Developed GenAI-powered tooling for automated false-positive triage and cross-SIEM rule "
                   "conversion for other detection engineers.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections; analyzed large-scale "
                   "security log data to surface anomalous behavior.")

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
dg.add_cover_paragraph(cl, "Detection Engineering Team\nKeeper Security")
dg.add_cover_paragraph(cl,
    "Turning security telemetry into operational value — reducing noise, tuning signal quality, and mapping "
    "coverage against MITRE ATT&CK — is the core of what I've built across the last several SIEM detection "
    "engineering roles."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built detection-as-code orchestration across nine SIEM and EDR platforms, "
    "including CrowdStrike and SentinelOne, through their native APIs, and created and managed 2,300+ "
    "detection rules covering most of the MITRE ATT&CK matrix — all delivered through a full GitLab CI/CD "
    "pipeline so every rule was version-controlled and tested. I also built the log parsing and normalization "
    "layer myself: 50+ Logstash filters and a Common Information Model standardizing field names and types "
    "across every parsed data source, which is the same telemetry-quality problem your Senior Detection "
    "Engineer role centers on."
)
dg.add_cover_paragraph(cl,
    "Currently at Shorepoint, I own the Splunk-based detection and alerting content Treasury's SOC runs "
    "incident response against day to day, and I hold a Splunk User Certification along with certification "
    "in Splunk for Analytics and Data Science. I've also built GenAI-powered automation for false-positive "
    "triage and cross-platform rule conversion — the kind of signal-quality improvement your team is scaling."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that SIEM and telemetry background fits Keeper's detection "
    "maturity roadmap."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Keeper Security package built.")
