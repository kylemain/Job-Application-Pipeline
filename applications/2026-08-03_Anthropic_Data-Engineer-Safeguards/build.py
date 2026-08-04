import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
_sec = doc.sections[0]
from docx.shared import Inches as _Inches
_sec.top_margin = _Inches(0.35)
_sec.bottom_margin = _Inches(0.3)
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Data Engineer — Large-Scale Pipelines, Analytics Infrastructure & Abuse-Detection Data Systems")

dg.add_summary(doc,
    "Data engineer with 12 years of experience designing and running the pipelines, warehousing, and analytics "
    "infrastructure that power large-scale detection and safety systems — including ETL/ELT ownership for 220+ "
    "ingested log/data sources, a company-wide Common Information Model standardizing schema across all of it, "
    "and Apache Beam programs run on GCP Dataflow for large-scale historical data retrieval. That foundation "
    "sits directly under years of hands-on abuse/threat detection content development and threat-intelligence "
    "integration — signature, statistical, behavioral, and ML-based detection logic built on the pipelines and "
    "data models I engineered, plus dashboarding and data-quality alerting for stakeholder self-service."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Data Pipelines & ETL/ELT",
    "Pipeline design and ownership for 220+ ingested log/data sources; Common Information Model (CIM) / data "
    "dictionary design standardizing field names and types across all ingested data; 50+ Logstash "
    "parsing/normalization filters; Apache Beam programs run via GCP Dataflow for large-scale historical/"
    "cold-storage data retrieval; connector/collector health monitoring and troubleshooting")
dg.add_skills_line(doc, "Cloud Data Platforms",
    "GCP (BigQuery, Dataproc, Dataflow, serverless event-driven enrichment), AWS, Azure; Elasticsearch as a "
    "large-scale analytical data store (Query DSL, transforms, Beats-based ingestion, API)")
dg.add_skills_line(doc, "Distributed Data Processing & Streaming",
    "PySpark / SparkSQL for large-scale exploratory data analysis on GCP Dataproc clusters with Zeppelin "
    "notebooks; familiarity with Kafka and Flink for event-streaming workloads")
dg.add_skills_line(doc, "Dashboards, Reporting & Data Quality",
    "Custom Kibana dashboards/visualizations on Elasticsearch transforms for stakeholder self-service reporting; "
    "data-quality monitoring and alerting to keep safety-critical data reliable")
dg.add_skills_line(doc, "Abuse & Threat Detection Data Systems",
    "Detection content development (signature, statistical, behavioral, ML-based) on engineered data pipelines — "
    "2,300+ detection rules across the MITRE ATT&CK matrix; threat-intelligence integration into detection "
    "logic and alert enrichment")
dg.add_skills_line(doc, "Languages & Data Science",
    "Python, SQL, Pandas, scikit-learn, NumPy; clustering/unsupervised ML; time-series anomaly detection; Git")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new security data ingestion platform for DOE/NNSA from the ground up — "
                   "CrowdStrike, Suricata, and Zeek telemetry into a central Elasticsearch environment — with "
                   "data transforms, a UEBA detection layer, data-quality alerting, and custom Kibana dashboards "
                   "(DOE/NNSA Security Data Integration project, completed).")
dg.add_bullet(doc, "Supported data ingestion and data-quality efforts within an Elasticsearch/Splunk environment "
                   "for DOE's Continuous Diagnostics and Mitigation (CDM) program, a federal continuous-"
                   "monitoring initiative (CISA CDM at DOE, completed).")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics (Splunk saved searches) directly "
                   "on top of ingested SOC data supporting Treasury's Security Operations Center incident "
                   "response and case work (Treasury SOC / TSSOC, current project).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "behavioral, statistical, and ML-based detection content against massive-scale customer "
                   "telemetry on a cloud-based big-data platform, incorporating threat-intelligence context "
                   "from Forescout's in-house research team (Vedere Labs) into detection logic and alert "
                   "enrichment.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Owned data engineering for a next-gen cloud SIEM at massive scale as a very early hire — "
                   "220+ ingested log sources, 50+ Logstash parsing/normalization filters, and a Common "
                   "Information Model standardizing field names/types across all of it — plus connector/"
                   "collector health monitoring and a homegrown Apache Beam program run via GCP Dataflow to "
                   "fetch large volumes of historical cold-storage data for customers.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc clusters using Zeppelin notebooks and "
                   "a homegrown analysis toolkit — Spark jobs loading data from buckets, PySpark/SparkSQL "
                   "analysis feeding detection-rule development.")
dg.add_bullet(doc, "Created and managed 2,300+ individual detection rules covering most of the MITRE ATT&CK "
                   "matrix, building out the rules engine and detection content for the startup from scratch, "
                   "with threat intelligence integrated into rule logic and used directly for false-positive "
                   "investigation research.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security log data to build custom detection models — DNS-based "
                   "malware detection/mitigation and anomalous-behavior discovery across the network.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nAnthropic — Safeguards")
dg.add_cover_paragraph(cl,
    "Robust data infrastructure is the thing that makes safety work possible at scale, and building that "
    "infrastructure is what I've spent 12 years doing — most recently underneath detection and abuse-monitoring "
    "systems that had to be right, fast, and auditable. I'd like to bring that same foundation to the Safeguards "
    "team's data pipelines, warehousing, and analytical tooling."
)
cl_body = (
    "At Trend Micro/Cysiv, I owned the data engineering for a next-gen cloud SIEM from its earliest days as a "
    "startup — ETL/ELT pipelines for 220+ ingested log sources, 50+ Logstash parsing/normalization filters, and "
    "a Common Information Model that standardized field names and types across every source so downstream "
    "detection and analytics could trust the data. I built a homegrown Apache Beam program run via GCP Dataflow "
    "to retrieve large volumes of historical cold-storage data on demand, and ran exploratory data analysis at "
    "scale on GCP Dataproc clusters using PySpark and SparkSQL. On top of that foundation, I created and managed "
    "2,300+ detection rules spanning most of the MITRE ATT&CK matrix — signature, statistical, behavioral, and "
    "ML-based logic — and integrated threat intelligence directly into that detection content and alert "
    "enrichment workflow, the same kind of abuse-pattern-detection work this role's data needs to support."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "At Shorepoint, I built DOE/NNSA's security data integration platform from scratch — ingesting CrowdStrike, "
    "Suricata, and Zeek telemetry into a new Elasticsearch environment, then layering a UEBA detection model, "
    "data-quality monitoring and alerting, and custom Kibana dashboards on top so stakeholders could see model "
    "behavior and anomalies without needing to query the raw data themselves. That combination — pipeline "
    "ownership, data modeling, dashboarding, and detection content built on a foundation of Python, SQL, and "
    "cloud data platforms (BigQuery, Dataproc, Dataflow) — is exactly the range this Safeguards role asks for."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background applies to giving Anthropic's Safeguards team "
    "the data foundation it needs to detect misuse and keep model behavior safe at scale."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Anthropic Data Engineer, Safeguards package built.")
