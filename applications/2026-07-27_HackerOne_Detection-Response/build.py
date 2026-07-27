import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer — Detection & Response")

dg.add_summary(doc,
    "Senior detection engineer and security data scientist with 10+ years building detection-as-code "
    "orchestration and GenAI-powered automation across nine SIEM/EDR platforms, including CrowdStrike and "
    "SentinelOne. Currently own detection and alerting content directly supporting a live SOC's incident "
    "response (Treasury), having previously built a security data platform from scratch for DOE/NNSA."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection & Response Engineering",
    "Detection-as-code across Splunk, ELK/Elasticsearch, CrowdStrike, SentinelOne, Microsoft Sentinel/Defender, "
    "Google SecOps, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight; MITRE ATT&CK; incident-response support")
dg.add_skills_line(doc, "GenAI / LLM Security Automation",
    "Prompt engineering for triage and false-positive identification; automated detection-rule generation; "
    "GenAI-driven SIEM API orchestration; reusable GenAI \"skills\" for cross-platform rule conversion")
dg.add_skills_line(doc, "Languages & Data Engineering",
    "Python, SQL; PySpark/SparkSQL, GCP Dataproc/BigQuery/Dataflow; 220+ log-source pipelines; Common "
    "Information Model data-dictionary design")
dg.add_skills_line(doc, "Cloud & Platforms", "AWS, GCP, Azure, Docker (reproducible detection-testing environments)")
dg.add_skills_line(doc, "Data Science / ML", "Clustering, time-series anomaly detection, UEBA")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — current project: own the detection and "
                   "alerting content (Splunk saved searches) that the SOC runs incident response against day "
                   "to day.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (prior project, completed): built a new security data "
                   "platform ingesting CrowdStrike, Suricata, and Zeek into Elasticsearch; designed the "
                   "detection/analytics layer on top — dashboards, data transforms, UEBA detection content, "
                   "data-quality monitoring/alerting.")
dg.add_bullet(doc, "CISA CDM at DOE (prior project, completed): data ingestion and data-quality work across a "
                   "combined Elasticsearch and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built detection-as-code orchestration across nine SIEM/EDR platforms — including CrowdStrike "
                   "and SentinelOne — via native APIs, run through a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Developed GenAI-powered tooling: automated false-positive triage, new detection-content "
                   "generation, and cross-SIEM rule conversion for other detection engineers.")
dg.add_bullet(doc, "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix; built "
                   "Python-based data engineering for 220+ log sources.")
dg.add_bullet(doc, "Used Docker to build reproducible detection-testing environments for validating content "
                   "against real log data.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections; analyzed large-scale security "
                   "log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 27, 2026")
dg.add_cover_paragraph(cl, "Detection & Response Hiring Team\nHackerOne")
dg.add_cover_paragraph(cl,
    "Rebuilding detection and response as an engineering discipline rather than a triage queue is precisely "
    "the model I've operated in for the last several years — building the pipeline and the automation, not "
    "just watching the alerts.")
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built detection-as-code orchestration across nine SIEM and EDR platforms — "
    "including CrowdStrike and SentinelOne — through their native APIs, running the whole system through a "
    "GitLab CI/CD pipeline. I paired that with GenAI-powered tooling: prompt engineering to identify false "
    "positives and generate new detection logic, and reusable GenAI \"skills\" that automate cross-platform "
    "rule conversion for other detection engineers — the same AI-powered, capacity-scaling model HackerOne is "
    "describing for this role.")
dg.add_cover_paragraph(cl,
    "Currently at Shorepoint, I own the detection and alerting content that Treasury's SOC runs incident "
    "response against, and I built an entire security data platform for DOE/NNSA from raw log ingestion "
    "(CrowdStrike, Suricata, Zeek) through a full UEBA detection layer — the same \"find the observability "
    "gap, ship the high-signal detection\" lifecycle this role centers on.")
dg.add_cover_paragraph(cl,
    "One honest note: my core language is Python rather than Go or Ruby, and my production-codebase experience "
    "lives inside detection/data pipelines rather than general application backends — but the discipline of "
    "shipping and maintaining code other engineers depend on is the same.")
dg.add_cover_paragraph(cl, "I'd welcome the chance to talk through how that background fits the team's roadmap.")
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("HackerOne package built.")
