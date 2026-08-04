import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Principal Data Engineer — Elasticsearch-Native Platforms & Large-Scale Data Pipelines")

dg.add_summary(doc,
    "Data engineer with 12 years building and operating large-scale data pipelines and analytics "
    "platforms, anchored by deep, cross-employer hands-on Elasticsearch experience — from ES queries "
    "and transforms to native detection rules and API-level cluster work. Built the data engineering "
    "layer for 220+ heterogeneous data sources from the ground up, including a Common Information "
    "Model standardizing schema across every source, plus GCP Dataflow/Apache Beam pipelines for "
    "large-scale historical data retrieval. Strong Python foundation with statistical/ML technique "
    "experience, real team-lead/sprint-lead history mentoring peers on pipeline and detection design, "
    "and direct experience integrating threat intelligence into data/detection content."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Elasticsearch & Search-Based Platforms",
    "ES queries (Query DSL), ES transforms, Logstash (50+ custom filters), ES Beats (multiple log-"
    "collection variants), native ES detection rules/alerting, ES API (cluster/index management), "
    "Kibana dashboarding — core platform across three consecutive employers")
dg.add_skills_line(doc, "Data Engineering at Scale",
    "220+ unique source ingestion pipelines, Apache Beam / GCP Dataflow for historical & cold-storage "
    "retrieval, Common Information Model / data-dictionary design, data-quality monitoring & alerting, "
    "staged/safe production rollout")
dg.add_skills_line(doc, "Python & Analytics",
    "Python, SQL, statistical & ML techniques (clustering, time-series anomaly detection), PySpark / "
    "SparkSQL / GCP Dataproc / BigQuery for large-scale distributed processing")
dg.add_skills_line(doc, "Cloud, Streaming & Orchestration",
    "AWS / GCP / Azure; working familiarity with Kafka and Flink; hands-on experience within a "
    "Kubernetes-orchestrated platform; GitLab CI/CD pipeline orchestration with automated testing and "
    "staged rollout")
dg.add_skills_line(doc, "AI/LLM Applications & Threat Intelligence",
    "Prompt engineering and GenAI-powered tooling for detection/data-analysis workflows; extensive "
    "experience integrating threat intelligence (CTI) into detection and data-analytics content")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built an entirely new Elasticsearch-based data platform (DOE/NNSA project, completed) "
                   "ingesting CrowdStrike, Suricata, and Zeek data streams — designed ES transforms "
                   "powering a UEBA detection layer, custom Kibana dashboards, and data-quality alerting.")
dg.add_bullet(doc, "Supported data ingestion and data-quality engineering (CISA CDM project, completed) "
                   "across a combined Elasticsearch/Splunk environment for a large federal data platform.")
dg.add_bullet(doc, "Currently builds and maintains detection/analytics content against a large-scale "
                   "Splunk data environment for Treasury's SOC (current project).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science/detection engineering team building pipelines and "
                   "analytics content — signature, statistical, behavioral, and ML-based — against "
                   "massive-scale customer data on cloud-based big-data tooling.")
dg.add_bullet(doc, "Integrated threat intelligence (Vedere Labs CTI) into detection logic and alert "
                   "enrichment, using actor/campaign context to speed triage and tune rule precision.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Early hire on a next-gen SIEM built natively on Elasticsearch/Kibana — wrote and "
                   "managed detection rules and queries directly against ES indexes as core detection "
                   "content, not just log shipping.")
dg.add_bullet(doc, "Owned data engineering/pipelining for 220+ unique log sources; built 50+ Logstash "
                   "filters for parsing/normalization and authored a Common Information Model — a data "
                   "dictionary standardizing field names/types across every parsed source.")
dg.add_bullet(doc, "Built a homegrown Apache Beam program run via GCP Dataflow to fetch high-volume "
                   "historical cold-storage data on request; owned connector/collector health monitoring.")
dg.add_bullet(doc, "Served in a team-lead capacity running sprints and mentoring detection engineers on "
                   "ES query/transform design, rule development, and pipeline architecture.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security datasets to build custom models for anomalous-behavior "
                   "detection; built DNS-based malware detection/mitigation logic on production data.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Digital Risk Protection Hiring Team\nRecorded Future")
dg.add_cover_paragraph(cl,
    "Data convergence across disparate risk data streams is a problem I've solved from the ground up "
    "before: as an early hire building a next-gen SIEM, I owned the data engineering layer for 220+ "
    "distinct, messy sources, including a Common Information Model that standardized field names and "
    "types across every one of them so every downstream consumer — dashboards, detection rules, "
    "analytics — could build on one consistent schema instead of managing 220 different ones. That's "
    "the exact discipline aligning and ingesting Malicious Sites, Identity, and Surface Web data into a "
    "unified Digital Risk Protection system and Intelligence Graph requires."
)
dg.add_cover_paragraph(cl,
    "Elasticsearch has been the core platform underneath nearly all of that work — across three "
    "consecutive employers I've written and tuned ES queries and transforms, deployed Beats for "
    "collection, built native ES detection rules and Kibana dashboards, and worked directly against the "
    "ES API for cluster and index management, not just through a UI. I've paired that with production "
    "GCP pipeline work (Dataproc, Dataflow via a homegrown Apache Beam program, PySpark/SparkSQL) and "
    "a strong Python foundation for the statistical and ML techniques this role calls for. I've also run "
    "point on integrating threat intelligence directly into detection and analytics content — using "
    "actor and campaign context to tune rule logic and speed triage — which maps directly onto the kind "
    "of digital risk data Recorded Future's Intelligence Graph is built to explain."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to bring that pipeline-ownership, Elasticsearch depth, and threat-"
    "intelligence background to Recorded Future's Digital Risk Protection team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Recorded Future Principal Data Engineer package built.")
