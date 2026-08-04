import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
doc.sections[0].top_margin = dg.Inches(0.35)
doc.sections[0].bottom_margin = dg.Inches(0.35)
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Data Scientist — Anomaly Detection, ML & Security Analytics")

dg.add_summary(doc,
    "Security data scientist, 12 years, building statistical/ML detection systems against massive-scale "
    "telemetry — unsupervised clustering, time-series anomaly detection, and large-scale EDA (GCP Dataproc/"
    "PySpark) behind 220+ log sources and 2,300+ production detection rules across MITRE ATT&CK. Hands-on "
    "GenAI/LLM for security: prompt engineering for false-positive triage/rule generation, GenAI-orchestrated "
    "SIEM APIs. M.S. Physics (numerical data analysis & modeling)."
)

dg.add_section_heading(doc, "Data Science & Machine Learning")
dg.add_skills_line(doc, "Languages & Libraries",
    "Python, SQL, R; Pandas, scikit-learn, NumPy, SciPy, PyTorch")
dg.add_skills_line(doc, "Modeling Techniques",
    "Unsupervised/clustering ML (device behavior clustering on network telemetry), time-series anomaly "
    "detection (authentication volume/attempt anomalies, process-chain behaviors), statistical and behavioral "
    "detection modeling")
dg.add_skills_line(doc, "Big Data & Cloud ML Platforms",
    "GCP Dataproc/Zeppelin, PySpark/SparkSQL for large-scale EDA; Apache Beam/GCP Dataflow for high-volume "
    "batch retrieval; AWS, GCP, Azure cloud security")
dg.add_skills_line(doc, "GenAI / LLM for Security",
    "Prompt engineering for security use cases (false-positive triage, automated detection-content "
    "generation); GenAI-driven orchestration of SIEM APIs across customers/platforms; built reusable GenAI "
    "\"skills\" automating detection-rule translation between SIEM syntaxes")

dg.add_section_heading(doc, "Security Detection Engineering & Data Pipelines")
dg.add_skills_line(doc, "Detection Content",
    "2,300+ production detection rules (signature, statistical, behavioral, ML-based) across the MITRE "
    "ATT&CK matrix; multi-SIEM detection-as-code orchestration (Splunk, Sentinel, Defender, Google SecOps, "
    "CrowdStrike, SentinelOne) via native APIs, with GitLab CI/CD, automated testing, and staged rollout")
dg.add_skills_line(doc, "Data Engineering",
    "Pipelines ingesting 220+ unique log sources; 50+ Logstash normalization filters; Common Information "
    "Model (CIM) data-dictionary design; Elasticsearch (queries, transforms, Beats, detection rules, API), Splunk")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new security data ingestion and analytics platform for DOE/NNSA from the "
                   "ground up — CrowdStrike, Suricata, and Zeek telemetry into a central Elasticsearch "
                   "environment, with a UEBA (User and Entity Behavior Analytics) detection layer built on "
                   "custom data transforms to statistically surface anomalous entity behavior, plus data-"
                   "quality monitoring/alerting and custom dashboards (DOE/NNSA Security Data Integration "
                   "project, completed).")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics directly supporting Treasury's "
                   "Security Operations Center, translating security data patterns into actionable case "
                   "content for incident response analysts (Treasury SOC / TSSOC, current project).")
dg.add_bullet(doc, "Supported data ingestion/quality efforts in an Elasticsearch/Splunk environment for DOE's "
                   "Continuous Diagnostics and Mitigation (CDM) program (completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "statistical, behavioral, and ML-based detection models against massive-scale customer "
                   "telemetry on a cloud-based big-data platform, translating analytical findings into "
                   "production risk-detection content.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built unsupervised clustering models to group network devices by behavioral feature "
                   "similarity, and time-series anomaly-detection content for entity behaviors — authentication "
                   "volume/attempt anomalies by country, and parent/child process-chain deviations — as core "
                   "ML-based detection logic.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc compute clusters using Zeppelin "
                   "notebooks and a home-grown reusable analysis toolkit; wrote PySpark/SparkSQL jobs to load "
                   "and analyze bucketed data, and a homegrown Apache Beam/GCP Dataflow program to retrieve "
                   "high-volume historical cold-storage data for customer investigations.")
dg.add_bullet(doc, "Created and managed 2,300+ individual detection rules covering most of the MITRE ATT&CK "
                   "matrix as a very early hire, and owned data engineering for the pipeline feeding them — "
                   "220+ ingested log sources, 50+ Logstash normalization filters, and a Common Information "
                   "Model standardizing fields across all parsed data.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security log data to develop custom statistical models for DNS-based "
                   "malware detection/mitigation and anomalous network behavior discovery.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013) — Numerical Data Analysis & Modeling, "
                       "Applied Physics   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins "
                       "(Coursera): R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nAmazon — AWS Security")
dg.add_cover_paragraph(cl,
    "I've spent 12 years building the statistical and machine-learning models that find cyber threats inside "
    "massive-scale infrastructure telemetry — exactly the anomaly detection, predictive modeling, and real-time "
    "risk-assessment work this AWS Security data scientist role is built around."
)
cl_body = (
    "At Trend Micro/Cysiv, I built unsupervised clustering models to group network devices by behavioral "
    "feature similarity and time-series anomaly detection content covering authentication volume anomalies and "
    "process-chain deviations — production ML-based detection logic, not research exercises. I ran exploratory "
    "data analysis at scale on GCP Dataproc clusters using PySpark/SparkSQL and Zeppelin notebooks, and built a "
    "homegrown Apache Beam/Dataflow pipeline to retrieve high-volume historical data for investigations — the "
    "same big-data-processing muscle this role's SageMaker/EMR-scale work calls for, applied on a different "
    "hyperscale cloud. That statistical and ML detection work scaled into 2,300+ production detection rules "
    "across the MITRE ATT&CK matrix, built on a data-engineering pipeline I helped own spanning 220+ log "
    "sources."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "More recently at DOE/NNSA, I built a UEBA detection layer directly on top of custom data transforms to "
    "statistically surface anomalous entity behavior — the same automated risk-assessment and pattern-"
    "recognition work described in this role's key responsibilities. I also bring direct, hands-on GenAI "
    "experience applied to security: prompt engineering for false-positive triage and automated detection-"
    "content generation, and using GenAI to orchestrate detection-rule deployment across SIEM APIs — real "
    "groundwork for expanding LLM agent pipelines in a security context. My M.S. in Physics centered on "
    "numerical data analysis and modeling, the quantitative foundation behind all of it."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the opportunity to bring that same statistical rigor and security-focused ML experience to "
    "protecting AWS customers at scale."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Amazon AWS Security Data Scientist package built.")
