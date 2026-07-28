import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Security Engineer — Cloud IAM, Identity Governance & Security Tooling (AWS/GCP)")

dg.add_summary(doc,
    "Security engineer with 10+ years of hands-on cloud security work across AWS, GCP, and Azure — including "
    "direct IAM policy and access-control implementation in both AWS and GCP, and building the API tokens, "
    "roles, and permissions layer for a nine-platform security orchestration framework. Builds scrappy internal "
    "tooling in Python and evaluates vendor/third-party integration security as a matter of course."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Cloud IAM & Identity Governance",
    "Hands-on IAM policy and access-control implementation in AWS and GCP; created and managed API tokens, "
    "roles, and permissions across nine SIEM/EDR platforms as the identity/access layer of a cross-platform "
    "orchestration framework — real API-level access-management work")
dg.add_skills_line(doc, "Cloud Security & Architecture",
    "AWS, GCP, Azure; threat assessment and security-control evaluation across a wide range of vendor platforms; "
    "securing third-party API integrations across nine distinct vendor ecosystems")
dg.add_skills_line(doc, "Tooling & Automation",
    "Python-based internal tooling and scripting for security automation; full CI/CD pipeline (GitLab) for "
    "tooling delivery; reusable per-vendor API adapters covering rule management, schemas, and platform objects")
dg.add_skills_line(doc, "Detection & Data Engineering",
    "MITRE ATT&CK-aligned detection content, multi-source data pipeline engineering (220+ sources), GCP "
    "Dataproc/BigQuery/Dataflow")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — own the detection and alerting content a live "
                   "SOC runs incident response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform "
                   "integrating three distinct vendor telemetry sources (CrowdStrike, Suricata, Zeek) into "
                   "Elasticsearch, including the data-quality monitoring and alerting layer on top.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and quality work across a combined Elasticsearch "
                   "and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Implemented IAM policies and access controls in both AWS and GCP environments as part of "
                   "ongoing cloud security engineering work.")
dg.add_bullet(doc, "Architected a Python-based orchestration framework spanning nine SIEM/EDR platforms — "
                   "Microsoft Sentinel, Microsoft Defender, Google SecOps (Chronicle), Splunk, CrowdStrike, "
                   "SentinelOne, Sumo Logic, Palo Alto XSIAM, and Devo — via each platform's native API, "
                   "including reusable per-vendor adapters and the API tokens/roles/permissions layer needed to "
                   "secure each third-party integration.")
dg.add_bullet(doc, "Delivered the framework through a full GitLab CI/CD pipeline, with multithreading to manage "
                   "concurrent operations across many customers and vendor platforms in parallel.")
dg.add_bullet(doc, "Evaluated security tooling and controls from this same wide range of vendors as part of "
                   "ongoing threat assessment and security-posture work.")
dg.add_bullet(doc, "Used GCP Dataproc compute clusters, Spark/PySpark, and Apache Beam/GCP Dataflow for "
                   "large-scale exploratory data analysis and historical data retrieval.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections; analyzed large-scale "
                   "security log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 28, 2026")
dg.add_cover_paragraph(cl, "Cloud Architecture, Tooling and Security (CATS) Team\nNetflix")
dg.add_cover_paragraph(cl,
    "Identity and access management at real scale is a tooling and data problem before it's a policy problem — "
    "which is exactly the lens I've built my career around, securing access across heterogeneous cloud and "
    "vendor ecosystems."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I implemented IAM policies and access controls directly in both AWS and GCP, and "
    "architected a Python-based orchestration framework spanning nine distinct SIEM/EDR platforms — building "
    "the API tokens, roles, and permissions layer needed to securely integrate each one via its native API. That "
    "meant designing secure access patterns for nine separate third-party integrations, each with its own "
    "authentication model, and building reusable adapters and scrappy internal tooling in Python to manage all "
    "of them at once."
)
dg.add_cover_paragraph(cl,
    "That framework ran through a full GitLab CI/CD pipeline, with multithreading to handle concurrent "
    "operations across many customers and vendor platforms in parallel — the same kind of self-serve, "
    "foundational tooling that a paved-path GCP/AWS access program depends on. I also evaluated security "
    "controls and tooling across this same wide vendor landscape as part of ongoing threat-assessment work."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that hands-on IAM and cross-platform access-management "
    "background fits the CATS team's roadmap."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Netflix CATS package built.")
