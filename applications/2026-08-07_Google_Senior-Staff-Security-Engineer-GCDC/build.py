import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer — Detection Engineering, Multi-SIEM Orchestration & Incident Response")

dg.add_summary(doc,
    "Detection and incident-response engineer with 12 years of experience building the detection platforms, "
    "rules engines, and automated pipelines that find and resolve real security incidents at scale. Early hire "
    "at a next-gen cloud SIEM startup (Cysiv, spun out of Trend Micro, later acquired by Forescout) where I built the detection "
    "rules engine from scratch and created/managed 2,300+ detection rules covering most of the MITRE ATT&CK "
    "matrix. Built a central Elasticsearch cyber-defense platform from the ground up for a federal cloud-security "
    "program, and currently support live incident/case response for a federal SOC. Run a multi-SIEM "
    "detection-as-code CI/CD pipeline across nine platforms with automated testing, staged/safe rollout, and "
    "formally tracked detection-quality metrics — the same discipline this role's mandate to modernize threat "
    "detection and incident response at scale calls for."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection Engineering & Incident Response",
    "2,300+ detection rules covering most of the MITRE ATT&CK matrix (signature, statistical, behavioral, ML); "
    "current incident/case response for a federal SOC (Treasury); formal rule-quality metrics (coverage, "
    "precision/false-positive rate) with staged/safe rollout before production")
dg.add_skills_line(doc, "Cloud Security Platform Engineering",
    "Built an entire cyber-defense/detection platform from the ground up on Elasticsearch — CrowdStrike (EDR), "
    "Suricata, and Zeek telemetry ingestion, UEBA detection layer on custom data transforms, data-quality "
    "monitoring/alerting — for a DOE/NNSA cloud-adjacent security program")
dg.add_skills_line(doc, "Multi-SIEM Detection-as-Code & Orchestration",
    "Rule/content orchestration via native APIs across Microsoft Sentinel, Microsoft Defender, Google SecOps "
    "(Chronicle), Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight; GitLab CI/CD "
    "with automated unit/integration tests and multithreaded parallel rule deployment across many tenants")
dg.add_skills_line(doc, "AI/ML Applied to Security",
    "Prompt engineering to analyze security data, identify false positives, and generate new detection content; "
    "GenAI-driven SIEM API orchestration; reusable GenAI tooling to automate detection-rule translation between "
    "SIEM syntaxes — direct experience applying AI/ML to accelerate detection and response")
dg.add_skills_line(doc, "Cloud & IAM",
    "Hands-on IAM policy/role implementation in AWS and GCP; API-level token/role/permission management across "
    "nine SIEM platforms; GCP Dataproc/BigQuery/Dataflow, PySpark; Azure Sentinel/Defender API orchestration")
dg.add_skills_line(doc, "Engineering", "Python, SQL, Git, GitLab CI/CD, Docker")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics directly supporting a federal "
                   "SOC's live incident response and case work, tuning content for accuracy and coverage "
                   "(Treasury SOC / TSSOC, current project).")
dg.add_bullet(doc, "Built an entirely new cyber-defense platform from the ground up — CrowdStrike (EDR), "
                   "Suricata, and Zeek telemetry into a central Elasticsearch environment — including a UEBA "
                   "detection layer, custom Kibana dashboards, and data-quality monitoring/alerting content "
                   "(DOE/NNSA Security Data Integration project, completed).")
dg.add_bullet(doc, "Supported data ingestion and data-quality efforts within an Elasticsearch/Splunk environment "
                   "for a federal continuous-monitoring program, resolving systemic data-quality root causes "
                   "(CISA CDM at DOE, completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "behavioral, statistical, and ML-based detection content against massive-scale customer "
                   "telemetry on a cloud-based big-data platform, incorporating threat intel from Forescout's "
                   "in-house Vedere Labs research team to tune detection logic and reduce false positives.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Very early hire at a next-gen cloud SIEM startup — built the detection rules engine from "
                   "scratch and created/managed 2,300+ individual detection rules covering most of the MITRE "
                   "ATT&CK matrix, plus 50+ data filters, against 220+ ingested log sources.")
dg.add_bullet(doc, "Owned exploratory data analysis at scale (GCP Dataproc, PySpark/SparkSQL) to develop new "
                   "detection content and built a Common Information Model standardizing fields across all "
                   "parsed data feeding the detection layer — the kind of systemic-root-cause and standards work "
                   "this role's cross-organizational remediation mandate calls for.")

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
dg.add_cover_date(cl, "August 7, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nGoogle — GCP Cyber Defense Center")
dg.add_cover_paragraph(cl,
    "I'm a detection and incident-response engineer who has spent 12 years building the rules engines, cloud "
    "detection platforms, and automation pipelines that find and resolve real security incidents at scale — and "
    "I'm based in the Dallas/Ft. Worth area and ready to relocate to Sunnyvale to do this work on-site."
)
dg.add_cover_paragraph(cl,
    "As a very early hire at Cysiv (a next-gen cloud SIEM startup that spun out of Trend Micro, later acquired by Forescout), "
    "I built the detection rules engine from scratch and created and managed 2,300+ individual detection rules "
    "covering most of the MITRE ATT&CK matrix — signature, statistical, behavioral, and ML-based content, tuned "
    "against massive-scale customer telemetry. I've also built an entire cyber-defense platform from the ground "
    "up for a DOE/NNSA cloud-security program — ingesting CrowdStrike endpoint EDR, Suricata, and Zeek "
    "telemetry into Elasticsearch, then layering UEBA detection and data-quality alerting on top — and I "
    "currently support live incident and case response for a federal SOC, work that maps directly onto GCDC's "
    "mandate to rapidly triage, resolve, and systemically remediate critical security issues."
)
dg.add_cover_paragraph(cl,
    "I run a multi-SIEM detection-as-code CI/CD pipeline in GitLab across nine platforms — Microsoft Sentinel, "
    "Microsoft Defender, Google SecOps, CrowdStrike, SentinelOne, and more — with automated testing, staged/safe "
    "rollout, and formally tracked detection-quality metrics before anything reaches production. I've also "
    "applied GenAI directly to detection engineering: prompt-driven false-positive triage, new rule generation, "
    "and automated rule translation between SIEM syntaxes — directly relevant to GCDC's push to pioneer AI/ML "
    "capabilities that accelerate threat detection and automate response ahead of the next wave of AI-driven "
    "attacks."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how this background applies to modernizing Google Cloud's threat "
    "detection and incident response capabilities."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Google Senior Staff Security Engineer, GCP Cyber Defense Center package built.")
