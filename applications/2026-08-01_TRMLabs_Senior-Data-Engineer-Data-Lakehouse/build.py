import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Data Engineer — Cloud Data Pipelines & Lakehouse Infrastructure")

dg.add_summary(doc,
    "Data engineer with 12 years building and operating large-scale data pipelines and analytics "
    "platforms, with deep hands-on GCP experience (Dataproc, BigQuery, Dataflow) and distributed "
    "processing via Spark/PySpark/SparkSQL. Built and scaled ingestion for 220+ heterogeneous data "
    "sources and designed a Common Information Model — a company-wide data dictionary standardizing "
    "schema and metadata across all of it — the same discipline modern lakehouse metadata/catalog "
    "management requires. Runs production pipelines through a full CI/CD process end to end, from "
    "ingestion through transformation to data-quality monitoring and alerting."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Cloud Data Platform (GCP)",
    "Dataproc, BigQuery, Dataflow, GCP serverless/event-driven enrichment pipelines, Apache Beam for "
    "large-scale historical/cold-storage data retrieval")
dg.add_skills_line(doc, "Distributed Processing & Streaming",
    "Spark / PySpark / SparkSQL for large-scale distributed analytical processing; Kafka")
dg.add_skills_line(doc, "Data Modeling & Metadata Management",
    "Designed and built a Common Information Model (CIM) — a data dictionary standardizing field "
    "names/types across 220+ ingested sources — direct, hands-on schema-governance and metadata-"
    "management discipline")
dg.add_skills_line(doc, "Data Pipeline Engineering",
    "ETL/ELT pipeline design and ingestion at scale (220+ distinct sources), 50+ Logstash filters for "
    "parsing/normalization, data-quality monitoring and alerting, staged/safe rollout for production "
    "deployments")
dg.add_skills_line(doc, "Orchestration, CI/CD & Languages",
    "Full CI/CD pipeline orchestration (GitLab) for production data pipeline deployment; Python, SQL")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Data/Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new data ingestion platform (DOE/NNSA project, completed) pulling "
                   "multiple large third-party data feeds into a central Elasticsearch environment — custom "
                   "data transforms, pipeline monitoring, and data-quality alerting built on top of it.")
dg.add_bullet(doc, "Supported data ingestion and data-quality engineering (CISA CDM project, completed) "
                   "across a combined Elasticsearch/Splunk environment for a large agency data platform.")
dg.add_bullet(doc, "Currently builds and maintains analytics content against a large-scale Splunk data "
                   "environment for Treasury's SOC (current project).")

dg.add_job_header(doc, "Senior Data Scientist / Engineer", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data engineering/data science team building pipelines and analytics "
                   "content against massive-scale customer data using cloud-based big-data tooling.")

dg.add_job_header(doc, "Data Engineer / Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Owned data engineering/pipelining for 220+ unique data sources feeding a next-gen "
                   "cloud-based analytics platform, from early-startup buildout through scale.")
dg.add_bullet(doc, "Built 50+ Logstash filters for parsing/normalization and authored a Common Information "
                   "Model — a data dictionary standardizing field names/types across every parsed source — "
                   "the single schema of record the rest of the platform was built on.")
dg.add_bullet(doc, "Built a homegrown Apache Beam program run via GCP Dataflow to fetch large volumes of "
                   "historical cold-storage data on request; owned pipeline/connector health monitoring and "
                   "troubleshooting.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc compute clusters using Zeppelin "
                   "notebooks and PySpark/SparkSQL to load and process data from cloud storage buckets.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale datasets to build custom models identifying anomalous patterns; "
                   "built DNS-based detection/mitigation logic on top of a production data pipeline.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 1, 2026")
dg.add_cover_paragraph(cl, "Data Engineering Hiring Team\nTRM Labs")
dg.add_cover_paragraph(cl,
    "A lakehouse is only as trustworthy as the metadata and schema discipline underneath it. That's "
    "the exact problem I solved as an early hire at a fast-growing security data platform: I built the "
    "data engineering layer for 220+ distinct, messy sources from the ground up, including a Common "
    "Information Model that standardized field names and types across every one of them — giving every "
    "downstream consumer one consistent schema to build on instead of 220 different ones."
)
dg.add_cover_paragraph(cl,
    "That ground-up ownership carries directly into the stack this role runs on. I've built and operated "
    "production pipelines on GCP end to end — Dataproc compute clusters for large-scale exploratory "
    "analysis, PySpark/SparkSQL for distributed processing, GCP Dataflow (via a homegrown Apache Beam "
    "program) for high-volume historical and cold-storage retrieval, and GCP serverless functions for "
    "event-driven enrichment. I've also worked with Kafka, and I run every pipeline change through a full "
    "CI/CD process with staged rollout and data-quality monitoring before it hits production — the same "
    "operational discipline a petabyte-scale lakehouse demands."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to bring that pipeline-ownership and metadata-management background to TRM "
    "Labs as you scale the lakehouse architecture powering your analytics platform."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("TRM Labs Senior Data Engineer, Data Lakehouse Infrastructure package built.")
