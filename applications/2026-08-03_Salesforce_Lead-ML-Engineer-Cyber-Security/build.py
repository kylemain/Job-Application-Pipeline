import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Machine Learning Engineer & Security Data Scientist — Anomaly Detection, Clustering & Detection-as-Code")

dg.add_summary(doc,
    "Security data scientist and ML engineer with 12 years of experience building unsupervised and time-series "
    "anomaly detection systems that run in production against massive-scale security telemetry — clustering "
    "network devices and entities by behavior, detecting anomalous authentication and process-chain patterns, "
    "and running exploratory analysis at scale on PySpark/Dataproc/BigQuery. Built and operate a multi-SIEM "
    "detection-as-code CI/CD pipeline (GitLab) with automated testing, staged/safe rollout, and rule-quality "
    "metrics tracking before production — the same engineering rigor this role asks for, already applied at "
    "scale (2,300+ rules across the MITRE ATT&CK matrix). M.S. Physics underpins the quantitative foundation."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Machine Learning & Data Science",
    "Clustering/unsupervised ML for device and entity behavior; time-series anomaly detection (authentication "
    "volume/velocity, process-parent/child chains); exploratory data analysis at scale; Python, PyTorch, "
    "scikit-learn, pandas, NumPy, SciPy")
dg.add_skills_line(doc, "Big Data & Distributed Compute",
    "PySpark, SparkSQL, GCP Dataproc, BigQuery, Apache Beam/Dataflow; working familiarity with Kafka and Flink "
    "streaming; cloud: GCP, AWS, Azure")
dg.add_skills_line(doc, "MLOps / Detection-as-Code Pipelines",
    "GitLab CI/CD pipeline for detection-as-code with automated unit/integration tests, staged/safe rollout, "
    "and formally tracked rule-quality metrics (coverage, precision/false-positive rate) before production "
    "deployment; multithreaded orchestration across customer environments")
dg.add_skills_line(doc, "Containers & Orchestration",
    "Docker (built and managed custom images; containerized reproducible detection-testing environments); "
    "hands-on experience operating within Kubernetes-orchestrated platforms")
dg.add_skills_line(doc, "Cybersecurity Domain Depth",
    "MITRE ATT&CK-mapped detection content (2,300+ rules); multi-SIEM API orchestration (Splunk, Microsoft "
    "Sentinel/Defender, Google SecOps, CrowdStrike, SentinelOne, Sumo Logic, XSIAM, Devo, ArcSight); threat "
    "intel integration into detection logic")
dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Design and manage statistical and behavioral detection analytics (Splunk saved searches) "
                   "directly supporting Treasury's Security Operations Center incident response and case work "
                   "(Treasury SOC / TSSOC, current project).")
dg.add_bullet(doc, "Architected an unsupervised UEBA (User and Entity Behavior Analytics) detection layer from "
                   "scratch for DOE/NNSA — Elasticsearch transforms baselining entity behavior across "
                   "CrowdStrike, Suricata, and Zeek telemetry, plus anomaly-surfacing content, data-quality "
                   "monitoring, and custom dashboards (DOE/NNSA Security Data Integration, completed) — turning "
                   "a vague threat-visibility mandate into a concrete production system.")
dg.add_bullet(doc, "Supported data ingestion and data-quality efforts within an Elasticsearch/Splunk environment "
                   "for DOE's Continuous Diagnostics and Mitigation (CDM) program (completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building statistical, "
                   "behavioral, time-series, and ML-based (clustering) detection models against massive-scale "
                   "customer telemetry, with a direct mandate to reduce alert fatigue and improve analyst trust.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built unsupervised clustering models to group devices on the network by behavioral feature "
                   "for anomaly surfacing, and time-series anomaly detection covering authentication behavior "
                   "(anomalous volume/attempt patterns by country over time) and process-chain behavior "
                   "(parent/child process combinations), as core production detection content.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc (Zeppelin notebooks, a home-grown "
                   "reusable analysis toolkit, PySpark/SparkSQL) to mine 220+ ingested log sources for signal.")
dg.add_bullet(doc, "Created and managed 2,300+ individual detection rules covering most of the MITRE ATT&CK "
                   "matrix as a very early hire, building the rules engine and detection content for the "
                   "startup from scratch — plus the data engineering (50+ Logstash filters, Common Information "
                   "Model) underneath it.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Developed custom statistical models and algorithms for DNS-based detection and mitigation "
                   "of malware infections on the network, and analyzed large-scale security log data to "
                   "surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Trust Intelligence Platform Hiring Team\nSalesforce")
dg.add_cover_paragraph(cl,
    "Moving detection beyond signatures into probabilistic modeling and unsupervised learning is work I've "
    "already been doing for over a decade in production security environments — clustering entities by "
    "behavior, surfacing anomalies in time-series data, and building the pipelines that let that content "
    "actually ship. I'd like to bring that background to the Lead Machine Learning Engineer role on Salesforce's "
    "Trust Intelligence Platform team."
)
cl_body = (
    "At Trend Micro/Cysiv and Forescout, I built unsupervised clustering models to group devices on the network "
    "by behavioral feature, and time-series anomaly detection covering authentication patterns and process-"
    "chain behavior — production detection content, not research prototypes, running against massive-scale "
    "customer telemetry and covering most of the MITRE ATT&CK matrix across 2,300+ individual rules. At DOE/"
    "NNSA, I took a vague mandate — give the SOC visibility into unknown threats — and turned it into a "
    "concrete system: an unsupervised UEBA detection layer built on Elasticsearch transforms I designed from "
    "scratch, exactly the kind of translating-ambiguity-into-a-data-driven-solution this role calls for. All of "
    "this exploratory and model-development work ran at scale on GCP Dataproc, PySpark, and SparkSQL."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "I've also already built the operational discipline this role's MLOps mandate asks for: a multi-SIEM "
    "detection-as-code CI/CD pipeline in GitLab, orchestrating rule and content deployment across Splunk, "
    "Microsoft Sentinel, Microsoft Defender, Google SecOps, CrowdStrike, and more via their native APIs, with "
    "automated testing, staged/safe rollout, and formally tracked quality metrics before anything reaches "
    "production — the same rigor that keeps a SOC trusting the models it's given. I've built this as a force "
    "multiplier for other engineers, not just for myself, developing reusable per-platform adapters and tooling "
    "the whole detection team relies on. My M.S. in Physics underpins the quantitative side of all of it."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to bring that same combination of production ML depth and engineering rigor to "
    "Salesforce's security data science team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Salesforce Lead ML Engineer Cyber Security package built.")
