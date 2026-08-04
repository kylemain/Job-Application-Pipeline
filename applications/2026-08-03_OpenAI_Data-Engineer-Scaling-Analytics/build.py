import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Data Engineer — Data Pipelines, Data Quality & Operational Analytics at Scale")

dg.add_summary(doc,
    "Data engineer with 12 years of experience building the pipelines, canonical data models, and data-quality "
    "systems that turn fragmented operational data into trusted analytics — the same foundation Scaling "
    "Analytics needs to support infrastructure deployment, capacity planning, and operational decision-making. "
    "Built data ingestion and pipelining for 220+ unique data sources as an early startup hire, including a "
    "Common Information Model standardizing field names and types across every source. Deep hands-on "
    "experience with PySpark/GCP Dataproc for distributed processing and BigQuery for analytical data "
    "warehousing, plus a homegrown Apache Beam program on GCP Dataflow for large-scale batch data retrieval. "
    "Strong SQL/Python fundamentals with a track record of building data-quality monitoring and dashboards "
    "that stakeholders across engineering, operations, and leadership rely on for decisions."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Data Engineering & Pipelines",
    "Production data pipeline design and operation across 220+ heterogeneous sources; Common Information "
    "Model / canonical data model design and standardization; ETL/normalization (50+ Logstash filters); "
    "data-quality checks, monitoring, and alerting in production; connector/collector health monitoring and "
    "troubleshooting")
dg.add_skills_line(doc, "Distributed & Cloud Data Processing",
    "PySpark / SparkSQL on GCP Dataproc compute clusters, BigQuery, Apache Beam on GCP Dataflow for batch/"
    "historical data retrieval, GCS object storage, GCP serverless/event-driven data enrichment")
dg.add_skills_line(doc, "Programming & Analysis",
    "Python, SQL, Git, GitLab CI/CD with automated testing and staged/safe rollout; Pandas, NumPy, scikit-"
    "learn")
dg.add_skills_line(doc, "Reporting, Dashboards & Cross-Functional Delivery",
    "Kibana dashboard design for operational decision-making; translating cross-functional stakeholder "
    "requirements (security, data science, SOC operations) into technical data solutions; sustained delivery "
    "in fast-paced, evolving-priority environments")
dg.add_skills_line(doc, "Cloud Platforms", "GCP, AWS, Azure")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new data ingestion platform from the ground up, pipelining three "
                   "high-volume operational telemetry sources (CrowdStrike, Suricata, Zeek) into a central "
                   "Elasticsearch environment — data transforms, data-quality monitoring/alerting, and custom "
                   "dashboards that gave stakeholders real-time visibility into system health (DOE/NNSA "
                   "Security Data Integration, completed).")
dg.add_bullet(doc, "Currently builds and maintains analytics content that turns raw operational event data "
                   "into decision-ready outputs supporting a security operations center's case and incident "
                   "workflows (Treasury SOC / TSSOC, current project).")
dg.add_bullet(doc, "Supported data ingestion and data-quality engineering within an Elasticsearch/Splunk "
                   "environment for a large-scale continuous-monitoring data platform (CISA CDM at DOE, "
                   "completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and engineering team building analytics content against "
                   "massive-scale customer data on cloud-based big-data platforms — signature, statistical, "
                   "time-series, and ML-based analysis feeding operational decisions.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Owned data engineering for a next-gen cloud-based analytics platform at scale: built "
                   "ingestion pipelines for 220+ unique, heterogeneous data sources and designed a Common "
                   "Information Model — a canonical data dictionary standardizing field names and types across "
                   "every source, enabling consistent reporting and analysis.")
dg.add_bullet(doc, "Wrote 50+ Logstash parsing/normalization filters and owned connector/collector health "
                   "monitoring and troubleshooting to keep pipelines reliable in production; assisted building "
                   "\"Loggify,\" a homegrown log parsing/filtering tool that replaced Logstash.")
dg.add_bullet(doc, "Built a homegrown Apache Beam program run via GCP Dataflow to reliably retrieve large "
                   "volumes of historical/cold-storage data on demand; ran exploratory data analysis at scale "
                   "on GCP Dataproc compute clusters using PySpark/SparkSQL jobs against cloud storage buckets.")
dg.add_bullet(doc, "Built data-quality monitoring and alerting content to catch missing or inconsistent data "
                   "across the pipeline, and created custom dashboards translating raw data into metrics used "
                   "by analysts and leadership for day-to-day decisions.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale operational log datasets to build custom detection models — DNS-"
                   "based malware detection/mitigation and anomalous-behavior discovery across network data.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nOpenAI — Scaling Analytics")
dg.add_cover_paragraph(cl,
    "I've spent 12 years building the pipelines and canonical data models that turn fragmented, "
    "high-volume operational data into analytics people actually trust — the same discipline Scaling "
    "Analytics needs to give OpenAI's infrastructure organization visibility into hardware, capacity, and "
    "site operations at global scale."
)
cl_body1 = (
    "At Trend Micro/Cysiv, I owned data engineering for a next-gen analytics platform pulling in 220+ unique, "
    "heterogeneous data sources — designing a Common Information Model that gave every source a consistent "
    "schema for reporting and analysis, writing 50+ normalization filters, and owning connector/collector "
    "health monitoring so the pipelines stayed reliable in production. On the distributed-processing side, I "
    "built a homegrown Apache Beam program run on GCP Dataflow to reliably retrieve large volumes of "
    "historical data on demand, and used PySpark/SparkSQL on GCP Dataproc clusters alongside BigQuery for "
    "large-scale analysis. More recently at Shorepoint, I built a data ingestion and analytics platform from "
    "scratch for a federal client — pipelines, data-quality monitoring, and dashboards that gave operators "
    "real-time visibility into system health, the same shape of work as building trusted datasets for hardware "
    "and capacity operations."
)
dg.add_cover_paragraph(cl, cl_body1)
cl_body2 = (
    "Across every role, I've translated requirements from stakeholders outside my own team — security "
    "analysts, SOC operators, data scientists — into pipelines and dashboards they could rely on for daily "
    "decisions, and I've built the data-quality checks that catch problems before they reach those decisions. "
    "I'm comfortable operating in fast-moving, ambiguous environments — I was an early hire at Cysiv, building "
    "core data infrastructure as the company scaled from a small team into an established SIEM provider."
)
dg.add_cover_paragraph(cl, cl_body2)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background applies to building out the analytical "
    "foundations for OpenAI's infrastructure organization."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("OpenAI Data Engineer, Scaling Analytics package built.")
