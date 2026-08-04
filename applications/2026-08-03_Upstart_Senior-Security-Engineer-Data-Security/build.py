import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer — Data Security, Cloud IAM & Access Governance")

dg.add_summary(doc,
    "Security engineer with 12 years of experience building the identity, access-governance, and data pipeline "
    "systems that determine who and what can reach sensitive data. Hands-on Cloud IAM policy/role implementation "
    "in both AWS and GCP, plus API-level access governance — creating and managing tokens, roles, and permissions "
    "across a dozen-plus security platforms as part of a production orchestration framework built around "
    "least-privilege principles. Deep data-engineering background (220+ ingested source pipelines, schema "
    "standardization, large-scale cloud data processing) gives real technical grounding for data protection work "
    "across diverse data domains, backed by production Python engineering and full CI/CD ownership."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Cloud IAM & Least-Privilege Access Governance",
    "AWS and GCP IAM policy/role implementation; creation and governance of API tokens, roles, and permissions "
    "across 10+ security platforms as part of a production access-management framework built around "
    "least-privilege principles")
dg.add_skills_line(doc, "API-Level Access Management & Multi-Platform Orchestration",
    "Built per-platform API adapters and orchestration logic across Microsoft Sentinel, Microsoft Defender, "
    "Google SecOps (Chronicle), Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo, and ArcSight "
    "— real hands-on identity/access and permission-scoping work at the API level, not just rule management")
dg.add_skills_line(doc, "Data Engineering & Pipeline Building",
    "Designed and built a Common Information Model (data dictionary) standardizing field names/types across "
    "220+ ingested log sources; 50+ Logstash filters; multiple Elasticsearch Beats variants; GCP Dataflow/Apache "
    "Beam for large-scale historical data retrieval; PySpark on GCP Dataproc for analysis at scale")
dg.add_skills_line(doc, "Data Security & Detection Platforms",
    "Elasticsearch (queries, transforms, Beats, native detection rules, API); Splunk; data-quality monitoring "
    "and alerting for federal-scale ingestion platforms; security detection content across signature, "
    "statistical, behavioral, and ML-based rule types")
dg.add_skills_line(doc, "Engineering & Delivery",
    "Python, SQL, Git; GitLab CI/CD pipeline for detection-as-code with automated unit/integration tests, "
    "tracked rule-quality metrics, and staged/safe production rollout; comfortable Docker user")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics (Splunk saved searches) directly "
                   "supporting the Treasury Security Operations Center's incident response and case work, "
                   "operating under strict least-privilege access controls on sensitive federal data (Treasury "
                   "SOC / TSSOC, current project).")
dg.add_bullet(doc, "Built an entirely new security data ingestion platform for DOE/NNSA from the ground up — "
                   "CrowdStrike, Suricata, and Zeek telemetry into a central Elasticsearch environment — "
                   "including a UEBA detection layer on custom data transforms, data-quality monitoring/alerting "
                   "content, and custom dashboards (DOE/NNSA Security Data Integration project, completed).")
dg.add_bullet(doc, "Supported data ingestion and data-quality efforts within an Elasticsearch/Splunk environment "
                   "for DOE's Continuous Diagnostics and Mitigation (CDM) program (completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "behavioral, statistical, and ML-based detection content against massive-scale customer "
                   "telemetry on a cloud-based big-data platform.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Designed and built a Common Information Model — a data dictionary standardizing field names "
                   "and types across all parsed data — so every downstream system in a next-gen cloud SIEM could "
                   "consume 220+ heterogeneous log sources through one consistent schema, as a very early hire "
                   "building the data infrastructure and rules engine from scratch.")
dg.add_bullet(doc, "Owned data engineering for that ingestion pipeline at scale: built 50+ Logstash filters for "
                   "parsing/normalization, deployed multiple Elasticsearch Beats variants for collection, and "
                   "ran connector/collector health monitoring and troubleshooting to keep the pipeline reliable.")
dg.add_bullet(doc, "Created and managed 2,300+ individual detection rules covering most of the MITRE ATT&CK "
                   "matrix, and built a homegrown Apache Beam program on GCP Dataflow for large-scale historical "
                   "cold-storage data retrieval.")

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
dg.add_cover_paragraph(cl, "Hiring Team\nUpstart")
dg.add_cover_paragraph(cl,
    "Upstart's Data Security program is built on a principle I've spent years working from the access-control "
    "side: least-privilege only works if the systems governing it are engineered, not improvised. That's the "
    "problem I've been solving across identity/access governance and data pipeline engineering for the past "
    "several years."
)
cl_body = (
    "I've implemented Cloud IAM policies and roles in both AWS and GCP, and — as part of building a multi-SIEM "
    "detection-as-code orchestration framework — created and governed API tokens, roles, and permissions across "
    "a dozen-plus security platforms (Microsoft Sentinel, Microsoft Defender, Google SecOps, Splunk, CrowdStrike, "
    "SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo, and more), all via their native APIs. That framework runs on "
    "a GitLab CI/CD pipeline I built with automated unit/integration tests, tracked rule-quality metrics, and "
    "staged/safe rollout before anything reaches production — the same engineering discipline that turns a "
    "least-privilege access model from policy into something real and repeatable."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "On the data side, I was an early hire building a cloud SIEM startup's data infrastructure from scratch: I "
    "designed a Common Information Model standardizing field names and types across 220+ ingested log sources, "
    "owned 50+ Logstash parsing/normalization filters, and built a homegrown Apache Beam program on GCP Dataflow "
    "for large-scale historical data retrieval. More recently at Shorepoint, I built DOE/NNSA's entire security "
    "data ingestion platform from a blank canvas, with data-quality monitoring and alerting layered on top to "
    "keep it trustworthy over time. That combination — access governance engineering plus hands-on data "
    "pipeline ownership — is exactly the intersection this role sits at."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background applies to building Upstart's data security "
    "program."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Upstart Senior Security Engineer, Data Security package built.")
