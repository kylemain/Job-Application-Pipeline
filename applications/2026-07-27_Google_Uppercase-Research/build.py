import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer — Detection Engineering & Security Automation")

dg.add_summary(doc,
    "Senior detection engineer and security data scientist with 10+ years building detection-as-code "
    "orchestration across nine SIEM/EDR platforms — including Google SecOps (Chronicle) — plus real, "
    "hands-on GenAI/LLM tooling that automates detection-rule generation, false-positive triage, and "
    "cross-platform rule conversion. Currently own detection and alerting content for Treasury's SOC, having "
    "previously built a security data and UEBA detection platform from scratch for DOE/NNSA."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Multi-SIEM Detection-as-Code & Orchestration",
    "Google SecOps (Chronicle), Splunk, Microsoft Sentinel, Microsoft Defender, CrowdStrike, SentinelOne, "
    "Sumo Logic, Palo Alto XSIAM, Devo, ArcSight — reusable per-platform API adapters, full GitLab CI/CD")
dg.add_skills_line(doc, "GenAI / LLM for Security",
    "Prompt engineering for false-positive triage and detection-content generation; GenAI-driven SIEM API "
    "orchestration; reusable GenAI \"skills\" for cross-SIEM detection-rule conversion")
dg.add_skills_line(doc, "Detection Engineering",
    "Signature, statistical, behavioral, threshold, and ML-based rules; 2,300+ rules across the MITRE ATT&CK "
    "matrix; UEBA detection content")
dg.add_skills_line(doc, "Data Science / ML",
    "Python, SQL, PySpark/SparkSQL, GCP Dataproc/BigQuery/Dataflow, clustering, time-series anomaly detection")
dg.add_skills_line(doc, "Cloud & Platforms", "AWS, GCP, Azure, Elasticsearch/ELK, Docker")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — current project: build and maintain Splunk "
                   "saved-search analytics that serve as the SOC's core detection and alerting content.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (prior project, completed): built a new security data "
                   "platform ingesting CrowdStrike, Suricata, and Zeek into a central Elasticsearch environment; "
                   "designed the detection/analytics layer on top — custom dashboards, data transforms, UEBA "
                   "detection content, and data-quality monitoring/alerting.")
dg.add_bullet(doc, "CISA CDM at DOE (prior project, completed): data ingestion and data-quality work across a "
                   "combined Elasticsearch and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built and led detection-as-code orchestration across nine SIEM/EDR platforms — including "
                   "Google SecOps (Chronicle), Splunk, Sentinel, Defender, CrowdStrike, SentinelOne, Sumo Logic, "
                   "XSIAM, and Devo — via native APIs, run through a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Developed GenAI-powered tooling for detection engineers: prompt engineering to identify false "
                   "positives and generate new detection content, plus reusable GenAI \"skills\" that convert "
                   "detection rules between SIEM syntaxes.")
dg.add_bullet(doc, "Created and managed 2,300+ individual detection rules covering most of the MITRE ATT&CK "
                   "matrix; built data pipelines for 220+ log sources; authored a Common Information Model data "
                   "dictionary standardizing fields across all parsed data.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc/Zeppelin/PySpark; built time-series "
                   "anomaly detection for authentication behaviors and process-chain activity.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections; analyzed large-scale security "
                   "log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 27, 2026")
dg.add_cover_paragraph(cl, "Uppercase Research Hiring Team\nGoogle")
dg.add_cover_paragraph(cl,
    "Turning static detection workflows into self-correcting, LLM-driven pipelines inside Google SecOps is "
    "exactly the problem I've spent the last several years solving from the ground up.")
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built and led detection-as-code orchestration across nine SIEM and EDR platforms — "
    "including Google SecOps (Chronicle) itself — through each platform's native API, run end-to-end via a "
    "GitLab CI/CD pipeline. On top of that, I developed reusable GenAI-powered tooling for detection engineers: "
    "prompt engineering to identify false positives and generate new detection logic, and GenAI \"skills\" that "
    "automatically convert detection rules between SIEM syntaxes — functionally the same problem Uppercase is "
    "solving with autonomous rule-writing and tuning agents for YARA-L.")
dg.add_cover_paragraph(cl,
    "More recently at Shorepoint, I built an entirely new security data platform for DOE/NNSA — from raw "
    "ingestion of CrowdStrike, Suricata, and Zeek data through a full UEBA detection layer — and I currently "
    "own the core detection and alerting content for Treasury's SOC. The throughline across both is the same: "
    "design the data plumbing and the detection logic on top of it, then automate both to scale faster than the "
    "threat landscape.")
dg.add_cover_paragraph(cl,
    "One honest gap: my depth is in building and automating detection content rather than formal security-design-"
    "review or system threat-modeling engagements. But the operational discipline of running detection-as-code "
    "at scale across nine platforms translates directly to the rigor Uppercase needs in validating agentic "
    "detection output before it ships.")
dg.add_cover_paragraph(cl, "I'd welcome the chance to talk through how that background applies to Uppercase's roadmap.")
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Google package built.")
