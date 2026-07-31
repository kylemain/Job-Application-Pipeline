import sys, os
sys.path.insert(0, "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/2026-07-31_Reco_Security-Researcher-Threat-Detection-Engineer"
os.makedirs(OUT, exist_ok=True)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Threat Detection Engineer — SaaS/Identity Threat Detection, SIEM/XDR, Large-Scale Security Data Analysis")

dg.add_summary(doc,
    "Threat detection engineer and security data scientist with 11 years turning terabytes of security telemetry "
    "into accurate, low-noise detection content. Founding-engineer experience building a next-gen SIEM's rules "
    "engine and data pipelines from scratch, plus a nine-platform detection-as-code orchestration framework across "
    "Splunk, Microsoft Sentinel, and Google SecOps (Chronicle). Deep hands-on background in identity/auth anomaly "
    "detection, false-positive reduction, and correlating signals across dozens of disparate log sources — the "
    "same core discipline SaaS/identity threat detection demands."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Threat Detection & SIEM/XDR Engineering",
    "Native-API detection content authoring, tuning, and false-positive-rate tracking across Splunk, Microsoft "
    "Sentinel, Google SecOps (Chronicle), CrowdStrike, SentinelOne, Elasticsearch, Sumo Logic, Palo Alto XSIAM, "
    "and Devo; created/managed 2,300+ detection rules spanning the MITRE ATT&CK matrix")
dg.add_skills_line(doc, "Identity & Behavioral Anomaly Detection",
    "Time-series anomaly detection of authentication behaviors (auth attempts by country, anomalous volume/attempt "
    "patterns) and process-chain behaviors; unsupervised ML for device/entity clustering; SQL-based querying and "
    "correlation of security events across large event volumes")
dg.add_skills_line(doc, "Large-Scale Security Data Analysis",
    "GCP Dataproc/PySpark/SparkSQL exploratory data analysis at scale; data engineering and correlation across "
    "220+ heterogeneous log sources via a purpose-built Common Information Model; GenAI-assisted triage and "
    "detection-content generation for reducing false positives")
dg.add_skills_line(doc, "Data Engineering, APIs & Automation",
    "Reusable per-platform API adapters for ingesting and correlating security telemetry across SIEM/XDR "
    "platforms; Python automation; GitLab CI/CD for detection-as-code; AWS/GCP/Azure security telemetry")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — builds and maintains Splunk-based detection/"
                   "alerting content used directly for incident investigation, tuning content to cut false "
                   "positives while preserving detection coverage.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built an Elasticsearch-based detection "
                   "platform from scratch, including UEBA (behavioral anomaly) detection logic and data-quality "
                   "monitoring/alerting across multiple ingested log sources.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering team building signature, statistical, behavioral, "
                   "and ML-based detection content against massive customer telemetry, with a continuous focus on "
                   "reducing false-positive rates without sacrificing true-positive coverage.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Founding engineer: built data engineering/pipelining for 220+ unique log sources into a "
                   "next-gen cloud SIEM, correlating signals across sources via a homegrown Common Information "
                   "Model (standardized data dictionary) — the same integration/correlation discipline SaaS "
                   "threat detection across many app APIs requires.")
dg.add_bullet(doc, "Created and managed 2,300+ individual detection rules covering most of the MITRE ATT&CK "
                   "matrix, plus 50+ data filters; architected a Python-based detection-as-code orchestration "
                   "framework across nine SIEM/EDR platforms with automated testing and false-positive-rate "
                   "tracking built in.")
dg.add_bullet(doc, "Time-series anomaly detection of identity and entity behaviors: authentication attempts by "
                   "country over time, anomalous auth volume/attempt detection, and process-chain (parent/child) "
                   "behavioral analysis — direct precedent for identity-based SaaS threat detection.")
dg.add_bullet(doc, "Exploratory data analysis at scale using GCP Dataproc, PySpark/SparkSQL, and Zeppelin "
                   "notebooks; built a homegrown reusable analysis toolkit for investigating large volumes of "
                   "security event data.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large security datasets to build custom detection models for emerging threats, "
                   "including DNS-based malware detection and anomalous-behavior discovery across network log data.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 31, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nReco")
dg.add_cover_paragraph(cl,
    "Detecting identity-based threats across a sprawling set of SaaS applications is fundamentally a data "
    "correlation and false-positive-reduction problem — the exact discipline I've spent 11 years on. As a "
    "founding engineer at Cysiv (later acquired by Trend Micro/Forescout), I built the data pipelines and "
    "detection rules engine for a next-gen cloud SIEM from scratch: 220+ heterogeneous log sources correlated "
    "through a homegrown Common Information Model, and 2,300+ detection rules across the MITRE ATT&CK matrix, "
    "all built with false-positive-rate tracking as a first-class requirement rather than an afterthought."
)
dg.add_cover_paragraph(cl,
    "That same correlation discipline extends directly to identity: I've built time-series anomaly detection for "
    "authentication behaviors — auth attempts by country over time, anomalous volume/attempt patterns — the same "
    "shape of problem as flagging OAuth risk or identity-provider misconfigurations in a SaaS environment. I later "
    "architected a detection-as-code orchestration framework spanning nine SIEM/XDR platforms, including Microsoft "
    "Sentinel and Google SecOps (Chronicle), with automated testing and staged rollout built into every deployment."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the opportunity to bring that large-scale security data analysis and detection engineering "
    "background to Reco's threat detection team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Reco Security Researcher / Threat Detection Engineer package built.")
