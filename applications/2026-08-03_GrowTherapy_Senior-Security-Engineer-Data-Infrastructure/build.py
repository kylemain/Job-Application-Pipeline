import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer — Data Infrastructure, Cloud IAM & Data Pipeline Engineering")

dg.add_summary(doc,
    "Security engineer with 12 years of experience building the data pipelines, schema standards, and "
    "access-management frameworks that determine how data is ingested, modeled, and governed at scale. As an "
    "early hire at a cloud SIEM startup, built a Common Information Model — a data dictionary standardizing "
    "field names and types across 220+ ingested data sources — the same executable-schema discipline data "
    "classification and lineage propagation depend on. Hands-on Cloud IAM implementation in both AWS and GCP, "
    "plus API-level access governance (tokens, roles, permissions) across a dozen+ platforms. Comfortable "
    "writing production code and owning data infrastructure end to end, from architecture through operation."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Data Modeling & Classification-Adjacent Engineering",
    "Common Information Model (CIM) / data dictionary design — standardized field names and types across "
    "220+ ingested log sources so downstream systems could act on schema automatically; data lineage awareness "
    "from designing and troubleshooting multi-source ingestion pipelines end to end")
dg.add_skills_line(doc, "Cloud IAM & Access Governance",
    "AWS and GCP IAM policy/role implementation; creation and governance of API tokens, roles, and permissions "
    "across 10+ security/data platforms as part of a production access-management framework")
dg.add_skills_line(doc, "Data Pipeline Engineering",
    "220+ source data ingestion pipeline ownership; 50+ Logstash filters for parsing/normalization; GCP "
    "Dataflow/Apache Beam for large-scale historical data retrieval; PySpark on GCP Dataproc for exploratory "
    "analysis at scale; GCP serverless event-driven data enrichment")
dg.add_skills_line(doc, "Cloud & Data Platforms",
    "AWS, GCP, Azure (API orchestration); Elasticsearch (queries, transforms, Beats, API); Kafka/Flink exposure; "
    "Docker")
dg.add_skills_line(doc, "Engineering & Delivery",
    "Python, SQL, Git; GitLab CI/CD with automated testing and staged/safe rollout for pipeline and rule changes")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new security data ingestion platform for DOE/NNSA from the ground up — "
                   "architecting the pipeline that brought CrowdStrike, Suricata, and Zeek telemetry into a "
                   "central Elasticsearch environment, then layering data-quality monitoring/alerting and a "
                   "UEBA detection layer on top of custom data transforms (DOE/NNSA Security Data Integration "
                   "project, completed).")
dg.add_bullet(doc, "Supported data ingestion and data-quality efforts within an Elasticsearch/Splunk environment "
                   "for DOE's Continuous Diagnostics and Mitigation (CDM) program, a continuous-monitoring "
                   "initiative dependent on consistent, well-governed data models (CISA CDM at DOE, completed).")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics (Splunk saved searches) supporting "
                   "the Treasury Security Operations Center's incident response and case work, working directly "
                   "with sensitive federal security data under strict access controls (Treasury SOC / TSSOC, "
                   "current project).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "behavioral, statistical, and ML-based detection content against massive-scale customer "
                   "telemetry on a cloud-based big-data platform.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Designed and built a Common Information Model — a data dictionary standardizing field names "
                   "and types across all parsed data — so every downstream system in a next-gen cloud SIEM could "
                   "consume 220+ heterogeneous log sources through one consistent schema, the closest real "
                   "analog in this history to executable, lineage-aware data classification.")
dg.add_bullet(doc, "Owned data engineering for that ingestion pipeline at scale: built 50+ Logstash filters for "
                   "parsing/normalization, deployed multiple Elasticsearch Beats variants for collection, and "
                   "ran connector/collector health monitoring and troubleshooting to keep the pipeline reliable "
                   "as a very early hire building the system from scratch.")
dg.add_bullet(doc, "Built a homegrown Apache Beam program run on GCP Dataflow to fetch large volumes of "
                   "historical cold-storage data for customers, and used GCP Dataproc/PySpark/SparkSQL for "
                   "exploratory data analysis at scale.")

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
dg.add_cover_paragraph(cl, "Hiring Team\nGrow Therapy")
dg.add_cover_paragraph(cl,
    "Grow Therapy's Senior Security Engineer role is fundamentally about making data classification, "
    "governance, and access control executable rather than aspirational — building the pipelines and standards "
    "that let every other system act on data sensitivity automatically. That's the exact problem I spent four "
    "years solving as an early hire building a cloud SIEM startup's data infrastructure from scratch."
)
cl_body = (
    "At Trend Micro/Cysiv, I designed and built a Common Information Model — a data dictionary standardizing "
    "field names and types across 220+ heterogeneous log sources — so every downstream system in our next-gen "
    "SIEM could consume incoming data through one consistent, executable schema instead of guessing at it "
    "source by source. I owned that pipeline end to end: 50+ Logstash filters for parsing and normalization, "
    "multiple Elasticsearch Beats variants for collection, and a homegrown Apache Beam program on GCP Dataflow "
    "for large-scale historical data retrieval. That's the same discipline this role calls for — production "
    "code, real data pipelines, and a schema that the rest of the company can build on top of."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "More recently at Shorepoint, I built DOE/NNSA's entire security data ingestion platform from a blank "
    "canvas — CrowdStrike, Suricata, and Zeek telemetry into a new Elasticsearch environment, with data-quality "
    "monitoring and alerting layered on top to keep the pipeline trustworthy over time. Alongside that, I've "
    "implemented Cloud IAM policies and roles in both AWS and GCP, and created and governed API tokens, roles, "
    "and permissions across a dozen-plus platforms as part of a production access-management framework — the "
    "same access-governance instinct this role's secure-data-access requirement is built around."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that data-infrastructure background applies to making the "
    "secure path the default one at Grow Therapy."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Grow Therapy Senior Security Engineer, Data Infrastructure package built.")
