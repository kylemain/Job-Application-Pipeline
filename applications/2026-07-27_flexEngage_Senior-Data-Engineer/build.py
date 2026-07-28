import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Data Engineer")

dg.add_summary(doc,
    "Senior data engineer with 10+ years building production data pipelines at scale — ingesting and "
    "normalizing data from 220+ distinct sources into centralized analytics platforms, designing a shared "
    "data dictionary (Common Information Model) to standardize schemas across all of it, and running the "
    "full pipeline through a GitLab CI/CD process. Deep hands-on experience with Python/SQL, cloud-scale "
    "distributed compute (GCP Dataproc, BigQuery, Dataflow), and building data-quality monitoring so "
    "downstream products and features can trust what's flowing through the pipeline."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Data Engineering & Pipelines",
    "ETL/ELT pipeline design and ingestion for 220+ distinct data sources, Apache Beam / GCP Dataflow for "
    "large-scale historical/cold-storage data retrieval, data-quality monitoring and alerting, Common "
    "Information Model (data dictionary) design and standardization")
dg.add_skills_line(doc, "Languages & Query",
    "Python, SQL, PySpark / SparkSQL")
dg.add_skills_line(doc, "Cloud & Distributed Compute",
    "GCP (Dataproc, BigQuery, Dataflow), AWS, Azure")
dg.add_skills_line(doc, "CI/CD & Tooling",
    "GitLab CI/CD pipelines, Git, Docker, Zeppelin notebooks")
dg.add_skills_line(doc, "Data Science / Analytics",
    "Pandas, scikit-learn, NumPy, SciPy, clustering / unsupervised ML, time-series analysis")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Data/Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new data ingestion platform (DOE/NNSA project, completed) pulling "
                   "multiple large third-party data feeds into a central Elasticsearch environment — custom "
                   "data transforms, pipeline monitoring, and data-quality alerting on top of the ingested data.")
dg.add_bullet(doc, "Supported data ingestion and data-quality engineering (CISA CDM project, completed) across "
                   "a combined Elasticsearch/Splunk environment for a federal agency data platform.")
dg.add_bullet(doc, "Currently build and maintain analytics content against a large-scale Splunk data "
                   "environment for Treasury's SOC (current project).")

dg.add_job_header(doc, "Senior Data Scientist / Engineer", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data engineering/data science team building pipelines and analytics "
                   "content against massive-scale customer data on cloud-based big data tooling.")

dg.add_job_header(doc, "Data Engineer / Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Owned data engineering/pipelining for 220+ unique data sources feeding a next-gen "
                   "cloud-based analytics platform, from early-startup buildout through scale.")
dg.add_bullet(doc, "Built 50+ Logstash filters for parsing/normalization, deployed Elasticsearch Beats for "
                   "collection, and authored a Common Information Model — a data dictionary standardizing "
                   "field names/types across every parsed source. Co-built \"Loggify,\" a homegrown log "
                   "parsing/filtering tool that replaced Logstash in production.")
dg.add_bullet(doc, "Built a homegrown Apache Beam program run via GCP Dataflow to fetch large volumes of "
                   "historical cold-storage data for customers; owned connector/collector health monitoring "
                   "and pipeline troubleshooting.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc compute clusters using Zeppelin "
                   "notebooks and PySpark/SparkSQL; built time-series and clustering-based analytics on top "
                   "of the pipeline output.")

dg.add_job_header(doc, "Data Scientist", "Experian", "Jan 2015 – Jan 2018")
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
dg.add_cover_date(cl, "July 27, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nflexEngage")
dg.add_cover_paragraph(cl,
    "Being the first full-time data engineer at flexEngage means setting the technology standards a whole "
    "team will build on later — that's the exact position I was in early at Cysiv, and it's the kind of "
    "problem I do my best work on.")
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv I owned data engineering for 220+ distinct, messy third-party data sources feeding "
    "a production analytics platform — writing the parsing/normalization layer (50+ Logstash filters), "
    "authoring a Common Information Model to give every downstream team one standardized data dictionary "
    "instead of 220 different schemas, and building a homegrown Apache Beam pipeline on GCP Dataflow to "
    "retrieve historical data at scale. That's the same shape of problem as building flexEngage's data "
    "warehouse and processing pipelines from a standing start: get the ingestion and standardization right "
    "so every feature built on top of it can trust the data.")
dg.add_cover_paragraph(cl,
    "I've also run production pipelines through a full CI/CD process (GitLab), written the exploratory "
    "analysis layer on top of pipeline output using PySpark/SparkSQL on GCP Dataproc, and worked daily in "
    "Python and SQL against large-scale cloud data platforms (BigQuery, Dataflow, plus general AWS cloud "
    "experience).")
dg.add_cover_paragraph(cl,
    "Two honest gaps against your stack: I haven't used Airflow or Snowflake specifically, and my "
    "infrastructure-as-code experience is CI/CD-centric (GitLab) rather than deep Terraform/CloudFormation/"
    "Ansible. The underlying skills transfer directly — pipeline orchestration, data-warehouse modeling, and "
    "provisioning-as-code concepts — and I'd expect to be productive on your specific toolchain quickly.")
dg.add_cover_paragraph(cl, "I'd welcome the chance to talk through how that background fits what you're building next.")
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("flexEngage package built.")
