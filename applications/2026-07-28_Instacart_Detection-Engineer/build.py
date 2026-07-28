import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection Engineer")

dg.add_summary(doc,
    "Detection engineer with 10+ years building detection-as-code pipelines and telemetry coverage across "
    "cloud, endpoint, and SIEM platforms. Built and ran a rules engine covering 2,300+ detections across most "
    "of the MITRE ATT&CK matrix, with full CI/CD delivery via GitLab and hands-on automation in Python."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection Engineering",
    "Detection-as-code (versioned, tested, CI/CD-deployed) across Splunk, ELK/Elasticsearch, CrowdStrike, "
    "SentinelOne, Microsoft Sentinel/Defender, Google SecOps, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight; "
    "MITRE ATT&CK coverage mapping; signature, behavioral, statistical, and ML-based detection logic")
dg.add_skills_line(doc, "Telemetry & Cloud",
    "AWS, GCP, Azure telemetry and log pipelines; 220+ ingested log sources; Common Information Model / "
    "data-dictionary standardization; Docker for reproducible detection-testing environments")
dg.add_skills_line(doc, "Automation & CI/CD", "Python, SQL; GitLab CI/CD detection-as-code pipelines; GenAI-powered "
    "triage automation and cross-SIEM rule conversion tooling")
dg.add_skills_line(doc, "Data Science / ML", "Clustering and unsupervised ML (device/behavior clustering), "
    "time-series anomaly detection, UEBA detection content")

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
dg.add_bullet(doc, "Built and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix, delivered "
                   "through a detection-as-code CI/CD pipeline in GitLab — every rule versioned and tested "
                   "before deploy.")
dg.add_bullet(doc, "Built detection-as-code orchestration across nine SIEM/EDR platforms (including CrowdStrike "
                   "and SentinelOne) via native APIs, plus GenAI-powered tooling for false-positive triage and "
                   "cross-SIEM rule conversion.")
dg.add_bullet(doc, "Data engineering for 220+ unique log sources; used Docker to build reproducible detection-"
                   "testing environments validated against real log data.")

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
dg.add_cover_paragraph(cl, "Detection Engineering Team\nInstacart")
dg.add_cover_paragraph(cl,
    "A detection-as-code mindset — everything versioned, tested, and deployed through repeatable pipelines — "
    "is exactly how I've built detection engineering programs for the last several years, and it's the model "
    "I'd bring to Instacart's Detection Engineering team."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built and managed 2,300+ detection rules covering most of the MITRE ATT&CK "
    "matrix, delivered through a full CI/CD pipeline in GitLab so every rule was versioned, peer-reviewed, "
    "and tested before it shipped — no hand-edited console rules. I paired that with data engineering across "
    "220+ log sources spanning cloud, endpoint, and SaaS telemetry, the same kind of multi-source coverage "
    "problem your team owns across endpoint, cloud, container, and SaaS."
)
dg.add_cover_paragraph(cl,
    "Currently at Shorepoint, I own the detection and alerting content that Treasury's SOC runs live incident "
    "response against, and I previously built an entire security data platform for DOE/NNSA — ingesting "
    "CrowdStrike, Suricata, and Zeek log data through to a full UEBA detection layer. I've also built GenAI-"
    "powered automation for triage and rule generation, which maps directly onto reducing analyst toil through "
    "automation and SOAR-style workflows."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that detection-as-code background fits the team's coverage "
    "priorities."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Instacart package built.")
