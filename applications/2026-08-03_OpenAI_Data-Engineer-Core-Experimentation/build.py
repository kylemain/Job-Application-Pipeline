import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Data Engineer — Large-Scale Pipelines, Distributed Processing & Experimentation Analytics")

dg.add_summary(doc,
    "Data engineer with 12 years of experience building the ingestion pipelines, canonical data models, and "
    "distributed processing systems that large organizations rely on for trustworthy analytics at scale. Built "
    "and ran ingestion pipelines for 220+ unique log sources, designed a Common Information Model standardizing "
    "field names/types across all of it, and used Apache Beam/GCP Dataflow, PySpark, and GCP Dataproc for "
    "large-scale data processing and exploratory analysis. Deep, hands-on statistical and data-science "
    "background — time-series analysis, clustering, and EDA at scale — directly relevant to building data "
    "infrastructure that has to hold up to statistical scrutiny."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Data Engineering & Pipelines",
    "Data pipeline design and ingestion for 220+ unique log sources; ETL/data normalization (50+ Logstash "
    "filters); Common Information Model / data dictionary design and standardization; Apache Beam / GCP "
    "Dataflow for large-scale historical data processing; connector/collector health monitoring and "
    "troubleshooting; Python, SQL")
dg.add_skills_line(doc, "Distributed & Big Data Processing",
    "PySpark, SparkSQL (writing, debugging, and optimizing Spark jobs); GCP Dataproc compute clusters; "
    "BigQuery; GCP serverless/event-driven data enrichment; working exposure to Kafka and Flink streaming "
    "jobs")
dg.add_skills_line(doc, "Data Science / Statistics",
    "Exploratory data analysis at scale (Zeppelin notebooks, home-grown analysis toolkit); time-series "
    "anomaly detection; clustering/unsupervised ML; Pandas, scikit-learn, NumPy, SciPy, PyTorch, R; "
    "quantitative/numerical modeling background (M.S. Physics)")
dg.add_skills_line(doc, "Cloud & Engineering Tools", "GCP, AWS, Azure; Git; GitLab CI/CD; Docker")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new data ingestion platform for DOE/NNSA from the ground up — CrowdStrike, "
                   "Suricata, and Zeek telemetry into a central Elasticsearch environment — including custom "
                   "data transforms, a behavioral-analytics layer built on top of those transforms, and "
                   "data-quality monitoring/alerting content (DOE/NNSA Security Data Integration, completed).")
dg.add_bullet(doc, "Supported data ingestion and data-quality engineering within an Elasticsearch/Splunk "
                   "environment for DOE's Continuous Diagnostics and Mitigation (CDM) program, a large-scale "
                   "federal continuous-monitoring data platform (completed).")
dg.add_bullet(doc, "Currently builds and maintains analytics content (Splunk saved searches) supporting "
                   "Treasury's Security Operations Center (Treasury SOC / TSSOC, current project).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and engineering team building signature, statistical, "
                   "time-series, and ML-based analytics content against massive-scale customer data on "
                   "cloud-based big-data platforms.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Owned data engineering for a next-gen cloud-based SIEM at scale: built ingestion pipelines "
                   "for 220+ unique log sources, wrote 50+ Logstash parsing/normalization filters, and designed "
                   "a Common Information Model — a data dictionary standardizing field names and types across "
                   "all parsed data.")
dg.add_bullet(doc, "Built a homegrown Apache Beam program run via GCP Dataflow to fetch large volumes of "
                   "historical cold-storage data for customers; assisted building \"Loggify,\" a homegrown log "
                   "parsing/filtering tool that replaced Logstash; owned connector/collector health monitoring "
                   "and troubleshooting for the ingestion pipeline.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc compute clusters using Zeppelin "
                   "notebooks and a home-grown reusable analysis toolkit, with PySpark/SparkSQL jobs to load "
                   "and analyze data from cloud storage buckets.")
dg.add_bullet(doc, "Applied statistical and ML techniques to large-scale telemetry — time-series anomaly "
                   "detection (authentication behavior, process chains) and unsupervised clustering (device "
                   "behavior) — and built/managed 2,300+ detection rules covering most of the MITRE ATT&CK "
                   "matrix as a very early hire.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security log datasets to build custom detection models — DNS-based "
                   "malware detection/mitigation and anomalous-behavior discovery across network data.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nOpenAI — Statsig / Core Experimentation")
dg.add_cover_paragraph(cl,
    "I've spent 12 years building the data pipelines and canonical data models that organizations depend on "
    "for trustworthy, large-scale analytics — exactly the foundation the Core Experimentation team needs "
    "underneath every experiment result it ships to the rest of OpenAI."
)
cl_body1 = (
    "At Trend Micro/Cysiv, I owned data engineering for a next-gen cloud SIEM processing telemetry from 220+ "
    "unique log sources — building the ingestion pipelines, writing 50+ parsing/normalization filters, and "
    "designing a Common Information Model that standardized field names and types across every parsed data "
    "source, so downstream teams could query and analyze it consistently. I also built a homegrown Apache Beam "
    "program run via GCP Dataflow to retrieve large volumes of historical cold-storage data on demand, and used "
    "PySpark/SparkSQL on GCP Dataproc compute clusters for exploratory analysis at scale. That's the same "
    "shape of problem this role calls for: designing and managing pipelines that get raw event data cleanly "
    "into a data warehouse and turn it into canonical, trustworthy datasets."
)
dg.add_cover_paragraph(cl, cl_body1)
cl_body2 = (
    "Beyond the pipeline work, I bring a real statistics and data-science background to bear on that "
    "infrastructure — time-series anomaly detection, unsupervised clustering, and exploratory data analysis "
    "at scale, grounded in a quantitative M.S. Physics background in numerical data analysis and modeling. "
    "I understand what it takes to build data systems that hold up under statistical scrutiny, not just ones "
    "that move data from one place to another."
)
dg.add_cover_paragraph(cl, cl_body2)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background applies to building out Core Experimentation's "
    "data pipelines and canonical tables at OpenAI."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("OpenAI Data Engineer, Core Experimentation package built.")
