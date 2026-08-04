import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Data Engineer — Large-Scale Pipelines, GenAI/LLM Tooling & Platform Engineering")

dg.add_summary(doc,
    "Data engineer with 12 years building large-scale data pipelines and detection-content platforms, "
    "including ground-up ingestion architecture for 220+ heterogeneous data sources, a Common Information "
    "Model standardizing schema across all of it, and Apache Beam/GCP Dataflow pipelines for high-volume "
    "historical retrieval. Direct, hands-on GenAI/LLM experience applying prompt engineering to production "
    "security workflows and orchestrating SIEM APIs via GenAI-powered tooling, plus a full CI/CD pipeline "
    "(GitLab) with automated testing, staged/safe rollout, and quality-metrics tracking — the same discipline "
    "this role's AI/ML data platforms require. Cybersecurity background includes hands-on ingestion and "
    "detection work built directly on CrowdStrike telemetry."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Data Engineering & Pipeline Architecture",
    "Ground-up ingestion pipelines for 220+ heterogeneous log/data sources; Common Information Model design — "
    "a data dictionary standardizing field names/types/schema across every source; 50+ Logstash filters for "
    "parsing/normalization; data-quality monitoring and alerting; homegrown Apache Beam program on GCP "
    "Dataflow for high-volume historical/cold-storage retrieval")
dg.add_skills_line(doc, "Cloud & Distributed Data Processing",
    "GCP (Dataproc, BigQuery, Dataflow); Spark/PySpark/SparkSQL for large-scale distributed processing; GCP "
    "serverless/event-driven enrichment; working familiarity with Kafka and Flink (hands-on exposure to a "
    "Flink-job environment)")
dg.add_skills_line(doc, "GenAI / LLM Applications & Tooling",
    "Prompt engineering for security use cases — data analysis, false-positive identification, automated "
    "detection-content generation; GenAI-driven orchestration of SIEM APIs across 9 platforms; reusable "
    "GenAI-powered tooling built for other engineers (e.g., automated cross-SIEM detection-rule conversion)")
dg.add_skills_line(doc, "Multi-Platform Orchestration & CI/CD",
    "Built and run a full CI/CD pipeline (GitLab) for detection/content deployment across 9 platforms via "
    "native APIs, with automated unit/integration testing, staged/safe production rollout, formally tracked "
    "quality metrics, and multithreaded parallel deployment")
dg.add_skills_line(doc, "Platform & Access Engineering",
    "Python, SQL, Git; Docker (custom images, containerized test environments); worked within a "
    "Kubernetes-orchestrated platform as a user; Cloud IAM policy/role implementation (AWS, GCP)")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new data ingestion platform from scratch (DOE/NNSA project, completed) "
                   "pulling CrowdStrike, Suricata, and Zeek telemetry into a central Elasticsearch "
                   "environment — custom data transforms, a UEBA detection layer built on top of them, "
                   "data-quality monitoring/alerting, and custom dashboards.")
dg.add_bullet(doc, "Building production GenAI tooling for security automation (current): prompt engineering "
                   "for detection-content generation and false-positive triage, plus GenAI-driven "
                   "orchestration of SIEM APIs across multiple platforms.")
dg.add_bullet(doc, "Supported data ingestion/quality engineering (CISA CDM at DOE, completed) across a "
                   "combined Elasticsearch/Splunk environment; currently manages detection/alerting analytics "
                   "(Splunk saved searches) for Treasury's SOC (TSSOC, current project).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "statistical, behavioral, and ML-based detection content and pipelines against "
                   "massive-scale customer data on a cloud-based big-data platform.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Owned data engineering for a next-gen cloud-based analytics platform at massive scale — "
                   "220+ ingested log sources, 50+ Logstash parsing/normalization filters, and a Common "
                   "Information Model standardizing field names/types across all of it — as a very early hire "
                   "building the pipeline from scratch.")
dg.add_bullet(doc, "Built a homegrown Apache Beam program run via GCP Dataflow to fetch high-volume "
                   "historical/cold-storage data on request; owned connector/pipeline health monitoring and "
                   "troubleshooting.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc using Zeppelin notebooks and "
                   "PySpark/SparkSQL; created/managed 2,300+ detection rules covering most of the MITRE "
                   "ATT&CK matrix, including ML-based clustering and time-series anomaly detection models.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security log data to build custom detection models — DNS-based "
                   "malware detection/mitigation and anomalous-behavior discovery across the network.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox  ·  Security Clearances: Top Secret (current), "
                       "DOE Q (held), Public Trust (held)", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Data Science Platform Engineering Team\nCrowdStrike")
dg.add_cover_paragraph(cl,
    "Before applying to help build data infrastructure for CrowdStrike's AI-driven security products, I "
    "built a security data platform that ingested CrowdStrike telemetry itself — a ground-up Elasticsearch-"
    "based ingestion and detection platform I built from scratch for a DOE/NNSA security program, pulling in "
    "CrowdStrike, Suricata, and Zeek data streams, then layering UEBA detection, data-quality monitoring, and "
    "custom dashboards on top of it."
)
cl_body = (
    "That ground-up ownership runs through my whole career. I built the data engineering layer for 220+ "
    "heterogeneous log sources at a fast-growing security data company, including a Common Information Model "
    "that standardized schema and field types across every one of them — the same semantic-cataloging "
    "discipline large-scale AI/ML data platforms depend on. I've run large-scale distributed processing on "
    "GCP (Dataproc, PySpark/SparkSQL, BigQuery, Dataflow via a homegrown Apache Beam program), and I run "
    "every pipeline change through a full CI/CD process — a GitLab-based pipeline with automated testing, "
    "staged/safe rollout, and quality-metrics tracking before anything reaches production."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "On the AI side, I've put GenAI directly into production security workflows: prompt engineering for "
    "detection-content generation and false-positive triage, and GenAI-driven orchestration of SIEM APIs "
    "across multiple platforms — real, hands-on experience shipping LLM-powered tooling into live operational "
    "use, which I'm eager to build on at the scale and depth this role calls for."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination — ground-up data pipeline ownership, CI/CD "
    "discipline, and hands-on GenAI tooling experience — applies to building CrowdStrike's next generation of "
    "AI-driven security data infrastructure."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("CrowdStrike Principal Data Engineer, LLM/AI Platforms package built.")
