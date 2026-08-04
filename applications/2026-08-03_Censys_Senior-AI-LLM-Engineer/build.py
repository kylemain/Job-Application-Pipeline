import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior AI/LLM Engineer — GenAI-Powered Security Detection & Investigation Tooling")

dg.add_summary(doc,
    "12 years building detection and investigation content for large-scale security operations, with hands-on "
    "experience putting GenAI/LLM tooling directly into live security workflows: prompt engineering for "
    "detection-content generation and false-positive analysis, LLM-driven orchestration of SIEM APIs, and "
    "reusable GenAI-powered tooling built for other detection engineers. Deep background integrating threat "
    "intelligence into detection and investigation content — directly relevant to SOC/threat-hunting "
    "investigation workflows — plus a strong Python and large-scale data engineering foundation (220+ ingested "
    "log sources, PySpark/GCP Dataproc, Elasticsearch)."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "GenAI/LLM for Security",
    "Prompt engineering for detection-content generation and false-positive/false-negative analysis; "
    "LLM-driven orchestration of SIEM APIs across 9 platforms for cross-customer detection deployment; "
    "reusable GenAI-powered tooling built for other engineers (e.g., automated cross-SIEM detection-rule "
    "conversion) — real production LLM-into-workflow experience")
dg.add_skills_line(doc, "Threat Intelligence Integration",
    "Integrating CTI (indicators, TTPs, actor/campaign context) into detection rule logic; enriching security "
    "alerts with threat intel for faster triage; using CTI directly during investigations and false-positive "
    "analysis (Forescout/Vedere Labs)")
dg.add_skills_line(doc, "Python & Data Engineering",
    "Python, SQL, pandas, NumPy, SciPy; data pipelines across 220+ ingested log sources; PySpark/SparkSQL on "
    "GCP Dataproc, Apache Beam/GCP Dataflow, BigQuery; Common Information Model / data standardization design")
dg.add_skills_line(doc, "Detection Engineering & SIEM",
    "Elasticsearch (queries, transforms, native detection rules, Beats, API), Splunk, MITRE ATT&CK-mapped "
    "detection content; GitLab CI/CD for detection-as-code with automated testing and staged/safe rollout")
dg.add_skills_line(doc, "Cloud Platforms",
    "AWS, GCP, Azure (Sentinel/Defender API orchestration); Docker; Kubernetes-orchestrated platform experience")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for "
                   "false-positive triage and detection-content generation, LLM-orchestrated interaction with "
                   "SIEM APIs across multiple platforms, and reusable GenAI-powered \"skills\" that convert "
                   "detection rules across SIEM syntaxes for other engineers.")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics (Splunk saved searches) directly "
                   "supporting Treasury's Security Operations Center investigation workflows — translating "
                   "threat-intel-informed and false-positive/false-negative investigation findings into "
                   "refined detection logic (Treasury SOC / TSSOC, current project).")
dg.add_bullet(doc, "Built an entirely new Elasticsearch-based security data platform from scratch for DOE/NNSA "
                   "— ingesting CrowdStrike, Suricata, and Zeek telemetry, with a UEBA detection layer on "
                   "custom data transforms, custom Kibana dashboards, and data-quality monitoring/alerting "
                   "(DOE/NNSA Security Data Integration, completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Integrated threat intelligence from Forescout's in-house Vedere Labs research team directly "
                   "into detection content and investigation workflows — using CTI to tune rule logic, enrich "
                   "alerts for faster triage, and validate findings during false-positive analysis as a senior "
                   "member of the data science and detection engineering team.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Owned data engineering for a next-gen cloud SIEM at scale — pipelines for 220+ log sources, "
                   "50+ Logstash filters, and a Common Information Model standardizing fields across all of "
                   "it — while creating and managing 2,300+ detection rules covering most of the MITRE ATT&CK "
                   "matrix as a very early startup hire.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale (PySpark/SparkSQL on GCP Dataproc, Zeppelin "
                   "notebooks) to validate new detection signal candidates before productionizing.")

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
dg.add_cover_paragraph(cl, "SOC/TH Team\nCensys")
dg.add_cover_paragraph(cl,
    "Censys is building AI-powered investigation workflows that help analysts and threat hunters triage "
    "malicious infrastructure at internet scale — I've spent the last several years doing the adjacent version "
    "of exactly that: putting GenAI and LLM tooling directly into live security detection and investigation "
    "workflows, on top of a decade-plus of building the detection content those workflows run on."
)
cl_body = (
    "At Shorepoint, I've built production GenAI tooling for security teams directly: prompt engineering for "
    "false-positive triage and automated detection-content generation, LLM-orchestrated interaction with SIEM "
    "APIs across nine platforms, and reusable GenAI-powered tooling that converts detection logic across SIEM "
    "syntaxes for other engineers. That's hands-on experience shaping how LLMs reason over security data and "
    "surface actionable findings — the same problem Censys is solving for internet-scale threat infrastructure."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "I also bring direct SOC/investigation-workflow relevance: at Forescout, I integrated threat intelligence "
    "from the Vedere Labs research team into detection content and alert enrichment, using CTI to tune rule "
    "logic and validate findings during false-positive analysis — the same investigation-support work Censys' "
    "SOC-TH team builds tooling around. And at Trend Micro/Cysiv, I built the data engineering and detection "
    "infrastructure underneath all of it: pipelines for 220+ log sources, a Common Information Model "
    "standardizing the data, and 2,300+ detection rules across the MITRE ATT&CK matrix — the kind of "
    "internet-scale, high-signal data foundation that AI-powered investigation tooling needs to reason over."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination — production GenAI-for-security experience "
    "plus deep detection and investigation-content engineering — applies to shaping Censys' AI-powered SOC "
    "platform."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Censys package built.")
