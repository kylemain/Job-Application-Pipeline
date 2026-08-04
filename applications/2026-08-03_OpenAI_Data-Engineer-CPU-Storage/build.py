import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Data Engineer — Infrastructure Data Integrations, Pipelines & Fleet-Scale Systems")

dg.add_summary(doc,
    "Data engineer with 12 years of experience connecting heterogeneous, fragmented systems into reliable, "
    "canonical data — the same core problem as unifying CPU, storage, and infrastructure telemetry across "
    "internal platforms and vendor systems. Built and ran ingestion integrations for 220+ unique log/data "
    "sources, owned connector/collector health monitoring and troubleshooting to keep integrations reliable in "
    "production, and designed a Common Information Model standardizing field names and types across every "
    "source. Built backend integrations against many third-party systems via native REST APIs, plus "
    "batch/scheduled data workloads with Apache Beam / GCP Dataflow, PySpark, and GCP Dataproc. Strong "
    "Python/SQL fundamentals with a track record of building data-quality and reconciliation checks that catch "
    "missing or inconsistent data."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Data Engineering & Systems Integration",
    "Ingestion pipeline design across 220+ heterogeneous data sources; connector/collector health monitoring "
    "and troubleshooting in production; Common Information Model / canonical data model design and "
    "standardization; data-quality and reconciliation monitoring/alerting to catch missing, stale, or "
    "inconsistent data; 50+ ETL/normalization filters (Logstash)")
dg.add_skills_line(doc, "Backend & API Integration",
    "Building integrations against third-party/vendor systems via native REST APIs across a dozen+ distinct "
    "platforms; reusable per-technology adapter design; API token/role/permission governance; multithreaded "
    "orchestration for parallel API-based workloads; GitLab CI/CD with automated testing and staged/safe "
    "production rollout")
dg.add_skills_line(doc, "Batch, Distributed & Cloud Data Processing",
    "Apache Beam / GCP Dataflow for large-scale batch data retrieval; PySpark / SparkSQL on GCP Dataproc "
    "compute clusters; BigQuery; cloud object storage (GCS buckets); GCP serverless/event-driven data "
    "enrichment; working exposure to Kafka and Flink")
dg.add_skills_line(doc, "Engineering Fundamentals", "Python, SQL, Git, GitLab CI/CD, automated testing, Docker; "
    "AWS, GCP, Azure")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new data ingestion platform for DOE/NNSA from the ground up, connecting "
                   "CrowdStrike, Suricata, and Zeek telemetry into a central Elasticsearch environment — data "
                   "transforms, data-quality monitoring/alerting to catch inconsistent or missing data, and "
                   "dashboards on top of it (DOE/NNSA Security Data Integration, completed).")
dg.add_bullet(doc, "Supported data ingestion and data-quality engineering within an Elasticsearch/Splunk "
                   "environment for DOE's Continuous Diagnostics and Mitigation (CDM) program, a large-scale "
                   "federal continuous-monitoring data platform (completed).")
dg.add_bullet(doc, "Currently builds and maintains analytics content (Splunk saved searches) supporting "
                   "Treasury's Security Operations Center (Treasury SOC / TSSOC, current project).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and engineering team building detection/analytics content "
                   "against massive-scale customer telemetry on cloud-based big-data platforms.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Owned data engineering for a next-gen cloud-based SIEM at scale: built ingestion "
                   "integrations for 220+ unique, heterogeneous log/data sources and designed a Common "
                   "Information Model — a canonical data dictionary standardizing field names and types across "
                   "every parsed source.")
dg.add_bullet(doc, "Owned connector/collector health monitoring and troubleshooting to keep ingestion reliable "
                   "in production; wrote 50+ Logstash parsing/normalization filters; assisted building "
                   "\"Loggify,\" a homegrown log parsing/filtering tool that replaced Logstash.")
dg.add_bullet(doc, "Built a homegrown Apache Beam program run via GCP Dataflow to reliably fetch large volumes "
                   "of historical cold-storage data on demand; ran exploratory data analysis at scale on GCP "
                   "Dataproc compute clusters using PySpark/SparkSQL jobs loading data from cloud storage "
                   "buckets.")
dg.add_bullet(doc, "Built reusable per-technology backend integrations against a dozen+ SIEM/security "
                   "platforms via native REST APIs as part of a broader orchestration framework, including API "
                   "token/role/permission governance and multithreaded parallel orchestration.")

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
dg.add_cover_paragraph(cl, "Hiring Team\nOpenAI — Scaling Analytics, Industrial Compute")
dg.add_cover_paragraph(cl,
    "I've spent 12 years solving the exact problem underneath this role: connecting fragmented, heterogeneous "
    "systems into data that engineering and planning teams can actually trust and use — just applied to "
    "security telemetry instead of CPU and storage infrastructure. The underlying engineering is the same."
)
cl_body1 = (
    "At Trend Micro/Cysiv, I owned data engineering for a next-gen cloud SIEM pulling in 220+ unique, "
    "heterogeneous log sources — designing a Common Information Model that gave every source a consistent "
    "representation of field names and types, and owning connector/collector health monitoring and "
    "troubleshooting to keep those integrations reliable in production. I also built reusable backend "
    "integrations against a dozen-plus SIEM and security platforms through their native REST APIs as part of a "
    "broader orchestration framework, including API token/role governance and multithreaded parallel "
    "execution — the same shape of work as connecting CPU/storage data across internal platforms, vendor APIs, "
    "and capacity systems. On the batch-processing side, I built a homegrown Apache Beam program run on GCP "
    "Dataflow to reliably retrieve large volumes of historical cold-storage data on demand, and used "
    "PySpark/SparkSQL on GCP Dataproc clusters for large-scale data analysis."
)
dg.add_cover_paragraph(cl, cl_body1)
cl_body2 = (
    "I'm comfortable navigating unfamiliar codebases and systems to figure out where a new integration should "
    "live, and I've built the data-quality and reconciliation monitoring that catches missing or inconsistent "
    "data before it reaches downstream consumers — direct experience with the reliability discipline this role "
    "needs applied to infrastructure data at scale."
)
dg.add_cover_paragraph(cl, cl_body2)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background applies to building out data integrations for "
    "Industrial Compute's CPU and storage platforms."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("OpenAI Data Engineer, CPU & Storage package built.")
