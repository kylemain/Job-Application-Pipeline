import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
# NOTE: the live posting at the given URL (req R29100) turned out to be "Sr. Software
# Engineer - Cloud (Hybrid)" -- a backend distributed-systems/Golang microservices role
# on CrowdStrike's Risk Analytics team, hybrid 2-3 days/week in Sunnyvale, CA -- not a
# remote Data Scientist role. Framing below leans on Kyle's strongest genuine overlap
# with that team's actual mission (data pipelines at scale + applied ML/detection
# content for risk-scoring/exposure-management use cases) rather than forcing a pure
# academic-research Data Scientist angle that doesn't match either the live req or the
# confirmed skills inventory. See ats_notes.md for the full mismatch writeup.

doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Data Engineer & Security Data Scientist — Risk Analytics & Detection Content")

dg.add_summary(doc,
    "Senior data engineer/data scientist with 12 years building large-scale data pipelines and applied ML "
    "detection content for security platforms — PySpark/GCP Dataproc exploratory analysis at scale, Kafka/Flink "
    "streaming exposure, and clustering/time-series anomaly-detection models productionized as live detection "
    "rules. Built and operated the ingestion, transform, and orchestration layers behind next-gen SIEM, UEBA, "
    "and multi-cloud detection platforms across AWS, GCP, and Azure, with hands-on Python across the full "
    "data-to-detection lifecycle."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Data Engineering & Distributed Pipelines",
    "PySpark, SparkSQL, GCP Dataproc, BigQuery, Apache Beam/GCP Dataflow; Kafka and Flink (streaming pipeline "
    "exposure); ingestion/normalization for 220+ log sources; Common Information Model / data-dictionary design")
dg.add_skills_line(doc, "Data Science / ML for Security",
    "Python, SQL, advanced mathematics; Pandas, scikit-learn, NumPy, SciPy, PyTorch; clustering/unsupervised ML "
    "(device behavior clustering); time-series anomaly detection; UEBA baseline modeling")
dg.add_skills_line(doc, "Cloud & Platform",
    "AWS, GCP, Azure (Sentinel/Defender API orchestration); Docker; GitLab CI/CD detection-as-code pipeline with "
    "automated testing, staged/safe rollout, and rule-quality metrics tracking")
dg.add_skills_line(doc, "Detection Engineering & Risk-Scoring Context",
    "Multi-SIEM/EDR detection-as-code orchestration via native APIs across nine platforms — including "
    "CrowdStrike, SentinelOne, Microsoft Sentinel/Defender, Google SecOps, Splunk; MITRE ATT&CK-mapped rule "
    "development (2,300+ rules); Elasticsearch (queries, transforms, Beats, native detection rules, API)")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team (current project) — build and manage the "
                   "Splunk-based detection/alerting analytics the SOC runs live incident response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new Elasticsearch data platform "
                   "ingesting CrowdStrike, Suricata, and Zeek telemetry from scratch, plus a UEBA detection "
                   "layer on custom data transforms, data-quality alerting, and custom dashboards.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and data-quality engineering across a combined "
                   "Elasticsearch/Splunk environment for a federal continuous-monitoring program.")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the data science/detection engineering team building signature, "
                   "behavioral, statistical, time-series, and ML-based detection content against cloud-scale "
                   "customer telemetry.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc clusters (Zeppelin notebooks, "
                   "PySpark/SparkSQL, Spark jobs against bucket-stored data) and built ML-based detection "
                   "content, including device clustering by network behavior and time-series anomaly detection "
                   "for entity behaviors (auth attempts by country, process-chain anomalies).")
dg.add_bullet(doc, "Owned data engineering for a next-gen cloud SIEM at scale — 220+ log sources, 50+ Logstash "
                   "filters, Elasticsearch Beats collection, and a Common Information Model standardizing field "
                   "names/types across all parsed data; used Apache Beam/GCP Dataflow to retrieve large volumes "
                   "of historical cold-storage data.")
dg.add_bullet(doc, "Built detection-as-code orchestration across nine SIEM/EDR platforms — including "
                   "CrowdStrike and SentinelOne — via native APIs through a full GitLab CI/CD pipeline; created "
                   "and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix as a very early "
                   "startup hire.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security log data to build custom detection models — DNS-based "
                   "malware detection/mitigation and anomalous-behavior discovery across the network.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University "
                       "(2011; Minors: Mathematics, Astrophysics)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins "
                       "(Coursera): R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Risk Analytics Team\nCrowdStrike")
dg.add_cover_paragraph(cl,
    "CrowdStrike's own platform is one of the systems I've already built detection-as-code orchestration "
    "against — a fitting starting point for a role centered on turning massive-scale security telemetry into "
    "risk intelligence."
)
cl_body = (
    "At Trend Micro/Cysiv, I ran exploratory data analysis at scale on GCP Dataproc — PySpark, SparkSQL, and "
    "Zeppelin notebooks against bucket-stored telemetry — and turned that analysis into production ML detection "
    "content: clustering devices by network behavior and building time-series anomaly detection for entity "
    "behaviors like authentication attempts and process-chain deviations. I also built the data engineering "
    "layer underneath all of it — ingestion and normalization for 220+ log sources, Elasticsearch Beats "
    "collection, and a Common Information Model standardizing field names and types across every parsed "
    "source. On top of that, I built detection-as-code orchestration across nine SIEM/EDR platforms, including "
    "CrowdStrike and SentinelOne, through their native APIs and a full GitLab CI/CD pipeline, creating and "
    "managing 2,300+ detection rules across the MITRE ATT&CK matrix."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "At DOE/NNSA, I built an entirely new Elasticsearch security data platform from scratch — ingesting "
    "CrowdStrike, Suricata, and Zeek telemetry — and layered a UEBA detection system, data transforms, and "
    "data-quality alerting on top of it. That combination of large-scale data pipeline ownership and applied "
    "ML for anomaly and risk signal detection is the same foundation this team's risk-scoring and posture "
    "work is built on."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that data engineering and applied ML background fits the "
    "Risk Analytics team's roadmap."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("CrowdStrike package built.")
