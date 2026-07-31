import sys, os
sys.path.insert(0, "/sessions/gallant-zealous-gates/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/gallant-zealous-gates/mnt/Job-Application-Pipeline/applications/2026-07-31_HackerOne_Manager-Data-Engineering"
os.makedirs(OUT, exist_ok=True)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Data Engineer — Pipelines, Data Modeling & Team Leadership")

dg.add_summary(doc,
    "Data engineer with 8 years building and operating high-volume data pipelines and source-of-truth data "
    "platforms at scale — 220+ ingestion sources, cloud-based big-data processing, and a standardized data "
    "model built from the ground up. Directs sprint priorities as a team lead and has architected and owned "
    "data infrastructure end to end, from ingestion through modeling to the dashboards stakeholders rely on."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Data Pipeline Engineering",
    "Built and operated ingestion pipelines for 220+ unique data sources; 50+ Logstash filters for parsing/"
    "normalization; Apache Beam / GCP Dataflow for historical and cold-storage data retrieval; PySpark / GCP "
    "Dataproc / BigQuery for large-scale distributed processing; GCP serverless/event-driven enrichment pipelines")
dg.add_skills_line(doc, "Data Modeling & Source-of-Truth Design",
    "Designed and built a Common Information Model (CIM) — a company-wide data dictionary standardizing field "
    "names and types across 220+ heterogeneous data sources — the same discipline a source-of-truth data-mart "
    "program requires: one consistent, trustworthy schema stakeholders can build on")
dg.add_skills_line(doc, "Dashboarding, SQL & Stakeholder-Facing Data",
    "SQL for data manipulation and analysis; built custom Kibana dashboards and visualizations directly on top "
    "of modeled data for stakeholder consumption; Python for automation and data tooling; comfortable presenting "
    "data-driven findings to both technical and non-technical audiences")
dg.add_skills_line(doc, "Team Leadership",
    "Team lead directing sprint priorities for a live SOC's detection and alerting content backlog, balancing "
    "new build work against incident-driven demands; built formal quality metrics and staged/safe-rollout "
    "practices for production deployments; mentors and elevates less experienced teammates")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead directing sprint priorities for the "
                   "team's content backlog, balancing new build work against incident-driven priorities.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new data platform from scratch — "
                   "ingestion, data transforms, and data-quality monitoring/alerting — a ground-up build owned "
                   "end to end, not an inherited program.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the data science and engineering team building analytics content against "
                   "massive customer data sets using cloud-based big-data tooling.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built the data engineering layer for 220+ unique data sources as an early hire at a startup: "
                   "50+ Logstash filters for parsing/normalization, multiple log-collection agent deployments, "
                   "and a Common Information Model standardizing field names/types across every source — the "
                   "single source of truth the rest of the platform was built on.")
dg.add_bullet(doc, "Used GCP Dataproc compute clusters, Zeppelin notebooks, and a home-grown reusable analysis "
                   "toolkit for exploratory data analysis at scale; wrote Spark jobs (PySpark/SparkSQL) to load "
                   "and analyze data from cloud storage buckets.")
dg.add_bullet(doc, "Built a home-grown Apache Beam program run via GCP Dataflow to fetch large volumes of "
                   "historical cold-storage data for customers on request.")
dg.add_bullet(doc, "Built custom dashboards and visualizations directly on top of modeled data for both internal "
                   "and customer-facing use; tracked data-quality metrics and used staged rollout before full "
                   "production deployment of new pipeline changes.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 31, 2026")
dg.add_cover_paragraph(cl, "Enterprise Data & AI Hiring Team\nHackerOne")
dg.add_cover_paragraph(cl,
    "A source of truth is only as good as the discipline behind it — one consistent schema everyone can trust, "
    "built to scale as new sources get added. That's the exact problem I solved as an early hire at a fast-"
    "growing security startup: I built the data engineering layer for 220+ unique data sources from scratch, "
    "including a Common Information Model that standardized field names and types across every one of them, so "
    "the rest of the platform had one trustworthy foundation to build on."
)
dg.add_cover_paragraph(cl,
    "That same ground-up ownership shows up throughout my background: cloud-based big-data pipelines (GCP "
    "Dataproc, PySpark, Apache Beam/Dataflow) for large-scale processing and historical data retrieval, custom "
    "dashboards built directly on modeled data for stakeholder consumption, and — on my current team — directing "
    "sprint priorities as team lead for a live SOC's technical backlog, balancing new build work against "
    "incident-driven demands in a fast-moving, early-stage-style environment."
)
dg.add_cover_paragraph(cl,
    "I'm drawn to HackerOne's mission of democratizing a single source of truth across a growing organization, "
    "and I'd welcome the chance to bring that same rigor around data modeling, pipeline ownership, and "
    "cross-team collaboration to the DataOne team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("HackerOne Manager, Data Engineering package built.")
