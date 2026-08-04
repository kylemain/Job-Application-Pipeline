import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection Engineer — MITRE ATT&CK, Multi-SIEM Detection-as-Code & Elasticsearch")

dg.add_summary(doc,
    "Detection engineer with 12 years of experience building the detection content, data pipelines, and "
    "automation that find real threats at scale. Early hire at a next-gen SIEM startup (Cysiv, acquired by "
    "Trend Micro/Forescout) where I built the rules engine from scratch and created/managed 2,300+ detection "
    "rules covering most of the MITRE ATT&CK matrix — signature, statistical, behavioral, and ML-based. Built a "
    "central Elasticsearch detection platform ingesting CrowdStrike (endpoint EDR), Suricata, and Zeek telemetry "
    "from the ground up, and run a multi-SIEM detection-as-code CI/CD pipeline with automated testing, rule-"
    "quality metrics, and staged/safe rollout — the same false-positive-reduction and pipeline-automation "
    "discipline this role's detection engineering responsibilities call for."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection Engineering & MITRE ATT&CK",
    "Signature, statistical, behavioral, aggregation/threshold, and ML-based detection content; 2,300+ rules "
    "covering most of the MITRE ATT&CK matrix; formal rule-quality metrics tracking (coverage, precision/"
    "false-positive rate) with staged/safe rollout before production")
dg.add_skills_line(doc, "Endpoint & Enterprise Telemetry",
    "Built a detection platform ingesting CrowdStrike (endpoint EDR), Suricata, and Zeek telemetry into a "
    "central Elasticsearch environment; UEBA (User and Entity Behavior Analytics) detection on top of custom "
    "data transforms; time-series anomaly detection on process chains and authentication behaviors")
dg.add_skills_line(doc, "Multi-SIEM Detection-as-Code & Orchestration",
    "Rule/content orchestration via native APIs across Microsoft Sentinel, Microsoft Defender, Google SecOps "
    "(Chronicle), Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight; GitLab CI/CD "
    "pipeline with automated unit/integration tests and multithreaded parallel deployment")
dg.add_skills_line(doc, "Elasticsearch",
    "Query DSL, transforms, Logstash, multiple Beats variants, native ES detection rules/alerting, ES API, "
    "Kibana dashboarding — full-lifecycle detection content development, not just log shipping")
dg.add_skills_line(doc, "AI/GenAI for Detection Engineering",
    "Prompt engineering to analyze security data, identify false positives, and generate new detection content; "
    "GenAI-driven SIEM API orchestration across customers/platforms; built reusable GenAI-powered tooling to "
    "automate rule conversion between SIEM rule syntaxes")
dg.add_skills_line(doc, "Engineering", "Python, SQL, Git, GitLab CI/CD, PySpark/Dataproc/BigQuery/Dataflow")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics (Splunk saved searches) directly "
                   "supporting a federal SOC's incident response and case work, tuning content for accuracy and "
                   "coverage (Treasury SOC / TSSOC, current project).")
dg.add_bullet(doc, "Built an entirely new detection platform from the ground up — CrowdStrike (endpoint EDR), "
                   "Suricata, and Zeek telemetry into a central Elasticsearch environment — including a UEBA "
                   "detection layer on custom data transforms, custom Kibana dashboards, and data-quality "
                   "monitoring/alerting content (DOE/NNSA Security Data Integration project, completed).")
dg.add_bullet(doc, "Supported data ingestion and data-quality efforts within an Elasticsearch/Splunk environment "
                   "for a federal continuous-monitoring program (CISA CDM at DOE, completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "behavioral, statistical, and ML-based detection content against massive-scale customer "
                   "telemetry on a cloud-based big-data platform, incorporating threat intel from Forescout's "
                   "in-house Vedere Labs research team to tune detection logic.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Very early hire at a next-gen cloud SIEM startup — built the detection rules engine from "
                   "scratch and created/managed 2,300+ individual detection rules covering most of the MITRE "
                   "ATT&CK matrix, plus 50+ data filters, against 220+ ingested log sources.")
dg.add_bullet(doc, "Built time-series anomaly detection for entity behaviors (process chains, authentication "
                   "patterns) and ran exploratory data analysis at scale (GCP Dataproc, PySpark/SparkSQL) to "
                   "develop new detection content; built a Common Information Model standardizing fields across "
                   "all parsed data feeding the detection layer.")

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
dg.add_cover_paragraph(cl, "Hiring Team\nGoogle — Enterprise Detection Engineering")
dg.add_cover_paragraph(cl,
    "I'm a detection engineer who has spent 12 years building the rules engines, data platforms, and "
    "automation pipelines that turn raw telemetry into high-fidelity detections — and I'm based in the Dallas/"
    "Ft. Worth area and ready to relocate to San Jose to do this work on-site."
)
cl_body = (
    "As a very early hire at Cysiv (a next-gen cloud SIEM startup, later acquired by Trend Micro and Forescout), "
    "I built the detection rules engine from scratch and created and managed 2,300+ individual detection rules "
    "covering most of the MITRE ATT&CK matrix — signature, statistical, behavioral, and ML-based content, all "
    "developed and tuned against massive-scale customer telemetry. That work maps directly onto this role's "
    "core mandate: scoping detection requirements across enterprise surfaces and designing detection rules for "
    "systems with many interconnected components."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "I've also built a central Elasticsearch detection platform from the ground up for a DOE/NNSA security "
    "program — ingesting CrowdStrike endpoint EDR, Suricata, and Zeek telemetry, then layering UEBA detection, "
    "custom dashboards, and data-quality alerting on top of it. And I run a multi-SIEM detection-as-code CI/CD "
    "pipeline in GitLab across Microsoft Sentinel, Microsoft Defender, Google SecOps, CrowdStrike, SentinelOne, "
    "and more — with automated testing, staged/safe rollout, and formally tracked rule-quality metrics "
    "(coverage, precision, false-positive rate) before anything reaches production. I've also applied GenAI "
    "directly to detection engineering — prompt-driven false-positive triage, new rule generation, and "
    "automated rule translation between SIEM syntaxes — relevant to this team's focus on defending against "
    "AI/agentic threats at scale."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background applies to securing Google's enterprise "
    "endpoint and SaaS footprint."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Google Security Engineer, Enterprise Detection Engineering package built.")
