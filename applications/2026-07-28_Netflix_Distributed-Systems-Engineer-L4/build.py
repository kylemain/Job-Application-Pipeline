import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Distributed Systems / Data Platform Engineer")

dg.add_summary(doc,
    "Data and systems engineer with 10+ years building large-scale, fault-tolerant data pipelines and API "
    "orchestration systems in Python — including hands-on experience with Kafka and Flink in a production "
    "streaming environment, multithreaded concurrent processing across many customers/systems, and distributed "
    "compute at scale via GCP Dataproc and Spark."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Distributed Systems & Streaming",
    "Hands-on experience with Kafka and Flink in a production real-time data environment; multithreaded "
    "orchestration of concurrent, fault-tolerant workflows across many customers/systems inside a CI/CD pipeline")
dg.add_skills_line(doc, "Data Engineering & Pipelines",
    "Built and maintained pipelines ingesting 220+ unique log data sources; Apache Beam / GCP Dataflow for "
    "large-scale historical data retrieval; Common Information Model / schema standardization across "
    "heterogeneous data sources")
dg.add_skills_line(doc, "Programming & APIs",
    "Python (production, object-oriented); design and consumption of RESTful APIs across nine distinct SIEM/EDR "
    "platforms; full CI/CD delivery pipeline in GitLab")
dg.add_skills_line(doc, "Cloud & Distributed Compute",
    "GCP Dataproc compute clusters, Spark / PySpark / SparkSQL, Zeppelin notebooks; AWS, GCP, Azure")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new data platform ingesting three "
                   "distinct high-volume telemetry sources into Elasticsearch, including data transforms and "
                   "data-quality monitoring/alerting to catch pipeline degradation at scale.")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — build and maintain the analytics content "
                   "(Splunk) that processes and correlates high-volume security data in near real time.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the data science and detection engineering team building statistical, "
                   "time-series, and ML-based analytics against cloud-scale customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built and operated a Python-based orchestration framework integrating nine distinct SIEM/EDR "
                   "platforms via their native RESTful APIs, designing reusable per-platform adapters covering "
                   "rule management, schemas, and other platform objects.")
dg.add_bullet(doc, "Implemented multithreading to deploy and manage detection content across many customers in "
                   "parallel, delivered through a full GitLab CI/CD pipeline — concurrent, fault-tolerant systems "
                   "engineering at production scale.")
dg.add_bullet(doc, "Built data engineering pipelines ingesting 220+ unique log data sources, including 50+ "
                   "Logstash filters for parsing/normalization and a Common Information Model standardizing "
                   "field names/types across all parsed data.")
dg.add_bullet(doc, "Worked hands-on in a production environment built on Kafka for data transport and Flink for "
                   "real-time stream processing.")
dg.add_bullet(doc, "Performed exploratory data analysis at scale using GCP Dataproc compute clusters, Zeppelin "
                   "notebooks, and PySpark/SparkSQL, and used a homegrown Apache Beam program on GCP Dataflow to "
                   "retrieve large volumes of historical cold-storage data.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security log data to develop custom models identifying anomalous "
                   "network behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 28, 2026")
dg.add_cover_paragraph(cl, "Data Platform Hiring Team\nNetflix")
dg.add_cover_paragraph(cl,
    "Moving high-volume data reliably through fault-tolerant, concurrent pipelines is the engineering problem "
    "I've spent a decade solving — just applied to security telemetry instead of streaming content, which is "
    "the same underlying distributed-systems discipline your Data Platform teams need."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built and operated a Python-based orchestration framework integrating nine distinct "
    "platforms via their native RESTful APIs, and implemented multithreading to deploy and manage work across "
    "many customers in parallel inside a full GitLab CI/CD pipeline — real concurrent, fault-tolerant systems "
    "engineering, delivered and operated in production. I've also worked hands-on in a production environment "
    "built on Kafka for data transport and Flink for real-time processing, the same technologies at the core of "
    "your Data Movement Platform."
)
dg.add_cover_paragraph(cl,
    "My data engineering background runs deep: pipelines ingesting 220+ unique log sources, a Common "
    "Information Model standardizing schema across all of them, and large-scale distributed compute via GCP "
    "Dataproc, PySpark, and Apache Beam/Dataflow for historical data retrieval — the same schema-driven, "
    "scale-first thinking behind Data Discovery and Governance."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that distributed-systems and data-engineering background fits "
    "the Data Platform team's roadmap."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Netflix Distributed Systems package built.")
