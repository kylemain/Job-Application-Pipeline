import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Data Engineer — Large-Scale Data Pipelines & Cloud Analytics")

dg.add_summary(doc,
    "Data engineer with 12 years of experience designing and operating the data pipelines, canonical datasets, "
    "and data-quality systems that power analytics and downstream decision-making at scale. Built data "
    "ingestion and pipelining for 220+ unique data sources from the ground up as an early startup hire, "
    "including a Common Information Model (data dictionary) standardizing field names and types across every "
    "pipeline, plus a homegrown Apache Beam program on GCP Dataflow for historical/cold-storage data retrieval. "
    "Deep hands-on experience with PySpark, GCP Dataproc, and BigQuery for large-scale distributed data "
    "processing and analysis. Comfortable working across many stakeholder teams to translate business and "
    "product needs into reliable, fault-tolerant data infrastructure."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Data Engineering & Pipelines",
    "Data ingestion/pipelining for 220+ sources; Common Information Model / canonical dataset & data-dictionary "
    "design and standardization; data-quality monitoring and alerting; connector/collector health monitoring "
    "and troubleshooting; ETL parsing/normalization (50+ Logstash filters, homegrown parsing tooling)")
dg.add_skills_line(doc, "Distributed & Cloud Data Processing",
    "PySpark / SparkSQL, GCP Dataproc compute clusters, Apache Beam on GCP Dataflow (historical/cold-storage "
    "data retrieval), BigQuery, Zeppelin notebooks; working exposure to Kafka and Flink in a production "
    "streaming environment")
dg.add_skills_line(doc, "Programming & Analysis",
    "Python, SQL, Git; Pandas, NumPy, SciPy, scikit-learn; time-series and clustering analysis at scale")
dg.add_skills_line(doc, "Cloud Platforms",
    "GCP (Dataproc, Dataflow, BigQuery, serverless/event-driven data enrichment), AWS, Azure")
dg.add_skills_line(doc, "Data Governance & Cross-Team Delivery",
    "Data security/integrity/compliance monitoring; schema and access governance across heterogeneous "
    "platforms; sustained delivery working across engineering, data science, and business stakeholder teams")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new data ingestion platform from the ground up for a federal client — "
                   "three distinct high-volume telemetry sources (CrowdStrike, Suricata, Zeek) pipelined into "
                   "a central Elasticsearch analytics environment, including data transforms, a custom "
                   "analytics/detection layer built on top of the pipeline output, data-quality monitoring and "
                   "alerting content, and custom dashboards (DOE/NNSA Security Data Integration project, "
                   "completed).")
dg.add_bullet(doc, "Currently create and manage analytics content that turns raw event data into decision-"
                   "ready outputs for a SOC's case and incident workflows — the same data-to-insight pipeline "
                   "discipline this role's canonical-dataset and metrics work requires (Treasury SOC / TSSOC, "
                   "current project).")
dg.add_bullet(doc, "Supported data ingestion and data-quality efforts within an Elasticsearch/Splunk "
                   "environment for a federal continuous-monitoring program (CISA CDM at DOE, completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and engineering team processing and analyzing massive-"
                   "scale customer data on cloud-based big-data tooling, building statistical, time-series, "
                   "and ML-based analytical content on top of that data pipeline.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Owned data engineering for a next-gen cloud analytics platform at massive scale as a very "
                   "early startup hire — built ingestion/pipelining for 220+ unique data sources, 50+ Logstash "
                   "parsing/normalization filters, and a Common Information Model (data dictionary) "
                   "standardizing field names and types across every pipeline; also assisted building "
                   "\"Loggify,\" a homegrown log-parsing/filtering tool that replaced Logstash, plus ongoing "
                   "connector/collector health monitoring and troubleshooting.")
dg.add_bullet(doc, "Built a homegrown Apache Beam program run on GCP Dataflow to fetch large volumes of "
                   "historical cold-storage data for customers — real hands-on distributed batch-processing "
                   "pipeline ownership, not just streaming ingestion.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc compute clusters using Zeppelin "
                   "notebooks and a home-grown reusable analysis toolkit — Spark jobs loading data from cloud "
                   "storage buckets, PySpark/SparkSQL for analysis, supporting statistical, behavioral, and "
                   "ML-based (device clustering) analytical content.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale datasets to build custom detection models — DNS-based malware "
                   "detection/mitigation and anomalous-behavior discovery across the network.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nOpenAI")
dg.add_cover_paragraph(cl,
    "I'd like to bring my data engineering background to the Applied team's work building the pipelines and "
    "canonical datasets that power OpenAI's analyses, safety systems, and product growth."
)
cl_body = (
    "As one of the earliest engineers at Cysiv, a cybersecurity startup later acquired by Trend Micro and then "
    "Forescout, I built the data engineering foundation for our entire analytics platform from scratch: "
    "ingestion and pipelining for 220+ unique data sources, 50+ parsing/normalization filters, and a Common "
    "Information Model — a canonical data dictionary standardizing field names and types across every pipeline "
    "we ran. That last piece maps directly onto this role's charge to develop canonical datasets that track key "
    "metrics across a fast-growing product. I also built a homegrown Apache Beam program run on GCP Dataflow to "
    "retrieve large volumes of historical cold-storage data for customers, and ran exploratory data analysis at "
    "scale on GCP Dataproc clusters using PySpark and SparkSQL — the same distributed-processing muscle this "
    "role calls for with Spark."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "Throughout my career, I've worked cross-functionally with infrastructure, data science, and product "
    "stakeholders to turn raw, high-volume event data into reliable, fault-tolerant systems that downstream "
    "teams could trust for decision-making — the same collaborative, data-integrity-first approach this role "
    "requires working across Infrastructure, Data Science, Product, Marketing, Finance, and Research. I'm drawn "
    "to the chance to apply that background to data that directly powers safety systems and the researchers "
    "building OpenAI's models."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the opportunity to talk through how this experience applies to building OpenAI's next data "
    "pipelines."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("OpenAI Data Engineer (Applied AI) package built.")
