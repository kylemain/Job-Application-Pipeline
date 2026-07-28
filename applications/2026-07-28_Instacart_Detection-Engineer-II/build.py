import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection Engineer — Detection-as-Code & Threat Hunting")

dg.add_summary(doc,
    "Senior detection engineer with 10+ years building detection-as-code pipelines, multi-cloud/EDR telemetry "
    "coverage, and MITRE ATT&CK-mapped detection content. Built and version-controlled 2,300+ detection rules "
    "through a full GitLab CI/CD pipeline across nine SIEM/EDR platforms; currently own live SOC detection "
    "content for a federal incident-response team."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection-as-Code & CI/CD",
    "Full GitLab CI/CD pipeline for detection content — version control, peer review, automated testing, "
    "deployment; reusable per-SIEM API adapters across CrowdStrike, SentinelOne, Splunk, Microsoft Sentinel/"
    "Defender, Google SecOps, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight")
dg.add_skills_line(doc, "Multi-Cloud & Endpoint Telemetry",
    "AWS, GCP, Azure; endpoint/EDR telemetry via CrowdStrike and SentinelOne; MITRE ATT&CK coverage mapping "
    "across most of the matrix")
dg.add_skills_line(doc, "Detection Engineering & Threat Hunting",
    "Signature, statistical, behavioral, aggregation/threshold, and ML-based detection rule development; "
    "time-series anomaly detection of entity behaviors (process chains, authentication patterns); UEBA content")
dg.add_skills_line(doc, "Automation & Scripting", "Python, SQL; GenAI-powered false-positive triage and "
    "cross-platform rule-conversion tooling; Docker for reproducible detection-testing environments")
dg.add_skills_line(doc, "Data Engineering", "220+ log-source pipelines, Common Information Model design, "
    "PySpark/Dataproc/BigQuery/Dataflow for large-scale investigative data pulls")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — own the detection and alerting content "
                   "(Splunk saved searches) the SOC runs day-to-day incident response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform "
                   "ingesting CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection layer, "
                   "dashboards, and data-quality alerting on top.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and quality work across a combined "
                   "Elasticsearch and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, "
                   "behavioral, statistical, time-series, and ML-based detection content against cloud-scale "
                   "customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built detection-as-code orchestration across nine SIEM/EDR platforms — including "
                   "CrowdStrike and SentinelOne — via native APIs, run through a full GitLab CI/CD pipeline "
                   "(version control, peer review, automated testing, deployment).")
dg.add_bullet(doc, "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix; "
                   "time-series anomaly detection on process chains and authentication behaviors.")
dg.add_bullet(doc, "Data engineering for 220+ log sources; used GCP Dataproc/Zeppelin/PySpark for exploratory "
                   "analysis at scale, including clustering devices on the network by behavioral feature.")
dg.add_bullet(doc, "Used Docker to build reproducible detection-testing environments for validating content "
                   "against real log data.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections; analyzed large-scale "
                   "security log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 28, 2026")
dg.add_cover_paragraph(cl, "Detection Engineering Hiring Team\nInstacart")
dg.add_cover_paragraph(cl,
    "Treating detection like a software discipline — versioned, tested, and deployed through repeatable "
    "pipelines rather than ad hoc rule-writing — is the exact model I've built my career around.")
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built detection-as-code orchestration across nine SIEM and EDR platforms, "
    "including CrowdStrike and SentinelOne, through their native APIs, run entirely through a GitLab CI/CD "
    "pipeline — version control, peer review, automated testing, and deployment for every rule. I created and "
    "managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix across a complex, multi-source "
    "environment, and built the telemetry pipelines for 220+ log sources that fed them.")
dg.add_cover_paragraph(cl,
    "Currently at Shorepoint, I own the detection and alerting content Treasury's SOC runs live incident "
    "response against, and earlier at DOE/NNSA I built an entire security data platform — from raw CrowdStrike, "
    "Suricata, and Zeek ingestion through a full UEBA detection layer. That combination of detection-as-code "
    "discipline, multi-cloud/EDR telemetry, and hands-on Python automation maps directly to how Instacart's "
    "Detection Engineering team operates.")
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background fits the team's detection coverage roadmap.")
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Instacart package built.")
