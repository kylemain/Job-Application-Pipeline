import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Machine Learning Engineer — Detection & Behavioral Analytics")

dg.add_summary(doc,
    "Machine learning engineer and data scientist with 12 years of experience building systems that tell "
    "malicious behavior apart from normal behavior at scale — including 8+ years of hands-on ML detection "
    "engineering (unsupervised clustering models, time-series anomaly detection, and precision-tuned feature "
    "engineering) across massive telemetry volumes. Full-lifecycle ML "
    "experience: exploratory data analysis at scale (PySpark/SparkSQL on GCP Dataproc), model development "
    "with pandas/scikit-learn/PyTorch, and production deployment of detection content with continuous "
    "false-negative/false-positive analysis feeding back into feature engineering — the same efficacy loop "
    "central to this role."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "ML & Data Science",
    "Python, SQL, pandas, scikit-learn, NumPy, SciPy, PyTorch, clustering/unsupervised ML, time-series "
    "anomaly detection, R")
dg.add_skills_line(doc, "Data Analytics at Scale",
    "PySpark / SparkSQL, GCP Dataproc, Zeppelin notebooks, BigQuery, Apache Beam / GCP Dataflow")
dg.add_skills_line(doc, "Detection & Feature Engineering",
    "Signature, statistical, behavioral, and ML-based detection rule development; entity/behavior baseline "
    "modeling; false-negative/false-positive analysis and tuning across attack categories")
dg.add_skills_line(doc, "Production ML Pipelines",
    "Detection-as-code CI/CD (GitLab), automated testing, rule-quality metrics tracking, staged/safe "
    "production rollout")
dg.add_skills_line(doc, "Engineering", "Git, Docker, structured/tested Python code, Elasticsearch")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built a UEBA (User and Entity Behavior Analytics) detection layer on custom Elasticsearch "
                   "data transforms, modeling enterprise-wide behavioral baselines from CrowdStrike, Suricata, "
                   "and Zeek telemetry to surface deviations from normal activity (DOE/NNSA Security Data "
                   "Integration project, completed).")
dg.add_bullet(doc, "Currently build and tune production detection analytics for Treasury's SOC, translating "
                   "false-positive/false-negative investigation findings directly into refined detection logic "
                   "(current project, Treasury SOC).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "behavioral, statistical, time-series, and ML-based detection content against massive-scale "
                   "customer data on a cloud-based big-data platform.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built ML-based detection content clustering devices on the network by behavioral features "
                   "(unsupervised learning) to surface anomalies signature-based rules missed — part of "
                   "2,300+ detection rules covering the MITRE ATT&CK matrix.")
dg.add_bullet(doc, "Designed time-series anomaly detection models for entity behaviors — Outlook process "
                   "chains, parent/child process combinations, and authentication patterns (volume and "
                   "geography) — to flag deviation from an established baseline, directly analogous to "
                   "modeling communication-pattern baselines and combining discriminative signals into a "
                   "precise detection system.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc compute clusters via Zeppelin "
                   "notebooks and PySpark/SparkSQL, building a reusable analysis toolkit to validate new "
                   "detection signal candidates before productionizing them.")
dg.add_bullet(doc, "Owned data engineering feeding the detection pipeline — 220+ ingested sources, 50+ "
                   "Logstash filters, and a Common Information Model standardizing fields across all of it — "
                   "so model inputs stayed reliable at production scale.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security datasets to build custom models and algorithms identifying "
                   "emerging threats — DNS-based malware detection/mitigation and anomalous-behavior discovery "
                   "in log data.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 1, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nAbnormal Security")
dg.add_cover_paragraph(cl,
    "Abnormal AI's Attack Detection team is solving a problem I've spent 12 years on from a different angle — "
    "telling malicious behavior apart from normal behavior at massive scale, in near-real time, using models "
    "and rules built to catch what static signatures miss."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built machine-learning-based detection content that clustered devices on the "
    "network by behavioral features to flag anomalies invisible to signature-based rules, and designed "
    "time-series anomaly detection models against entity behaviors — Outlook process chains, parent/child "
    "process relationships, and authentication patterns across volume and geography — to catch deviation "
    "from an established baseline. That's the same modeling problem your team runs against communication "
    "patterns: building discriminative signals at the message, sender, and recipient level and combining "
    "them into a precise detection system."
)
dg.add_cover_paragraph(cl,
    "I ran exploratory data analysis at scale on GCP Dataproc clusters using PySpark and SparkSQL to find "
    "and validate new detection signal candidates, then took those signals into production as part of a "
    "rule set covering 2,300+ detection use cases across the MITRE ATT&CK matrix — running the same efficacy "
    "loop this role calls for: analyzing false-negative and false-positive datasets, feeding findings back "
    "into feature engineering and model tuning, and monitoring production detection rates against a shifting "
    "attack landscape. I'm fluent in Python and the core ML toolkit — pandas, scikit-learn, NumPy, PyTorch — "
    "and comfortable taking a well-defined dataset through training, evaluation, and production deployment."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background applies to catching the next attack pattern "
    "your Detection Engine hasn't seen yet."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Abnormal Security package built.")
