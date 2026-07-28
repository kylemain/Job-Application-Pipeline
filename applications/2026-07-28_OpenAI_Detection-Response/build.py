import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer, Detection & Response")

dg.add_summary(doc,
    "Security engineer with 10+ years building detection-as-code across cloud and endpoint telemetry, "
    "orchestrating rule lifecycle management across nine SIEM/EDR platforms via native APIs, and shipping "
    "production GenAI tooling that accelerates triage and investigation. Comfortable operating across AWS, GCP, "
    "and multi-cloud identity — with hands-on IAM policy/role implementation in both."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Multi-SIEM Detection-as-Code Orchestration",
    "Built rule-lifecycle orchestration across nine SIEM/EDR platforms (Microsoft Sentinel, Defender, Google "
    "SecOps/Chronicle, Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo) via native APIs; "
    "multithreaded parallel deployment inside a full GitLab CI/CD pipeline; formally tracks detection quality "
    "metrics (coverage, precision/false-positive rate) and uses staged rollout before full production")
dg.add_skills_line(doc, "AI/Agent-Driven Detection & Investigation",
    "Production GenAI tooling for false-positive triage, automated detection-rule generation, and cross-SIEM "
    "rule-syntax conversion; GenAI-driven API orchestration to accelerate response workflows")
dg.add_skills_line(doc, "Cloud & Identity",
    "Hands-on IAM policy/role implementation in AWS and GCP; created and managed API tokens, roles, and "
    "permissions across nine SIEM platforms as part of the orchestration framework")
dg.add_skills_line(doc, "Detection Engineering & Telemetry",
    "2,300+ detection rules covering most of the MITRE ATT&CK matrix; signature, behavioral, statistical, "
    "time-series, and ML-based detection across cloud-scale customer telemetry; hands-on experience working "
    "within a Kubernetes-orchestrated platform plus comfortable Docker/container use for reproducible "
    "detection-testing environments; familiar with Kafka/Flink-based streaming pipelines")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — direct sprint priorities and technical "
                   "direction for the Splunk-based detection and alerting content a live SOC runs incident "
                   "response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection layer, data-quality "
                   "monitoring, and alerting content on top.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer "
                   "telemetry.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms via native APIs, with multithreading to deploy and manage detection content "
                   "across many customers in parallel inside a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Created and managed API tokens, roles, and permissions across those nine platforms as part of "
                   "building the orchestration framework — hands-on access-management work at the API level.")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for false-positive "
                   "triage, automated detection-rule generation, and cross-platform rule conversion; developed "
                   "reusable GenAI-powered 'skills' for detection engineers to automate repetitive tasks.")
dg.add_bullet(doc, "Data engineering for 220+ log data sources feeding the detection platform; 50+ Logstash "
                   "filters; used Docker for reproducible detection-testing environments; created and managed "
                   "2,300+ detection rules covering most of the MITRE ATT&CK matrix.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections on the network; analyzed "
                   "large-scale security log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Security Clearances: Top Secret (current, Treasury) · DOE Q Clearance · Public Trust (DOE)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 28, 2026")
dg.add_cover_paragraph(cl, "Security Hiring Team\nOpenAI")
dg.add_cover_paragraph(cl,
    "High-signal detection and reliable operational response are the two things I've spent the last decade "
    "building — across cloud, endpoint, and identity telemetry, and now increasingly with AI doing more of the "
    "heavy lifting."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built a Python-based orchestration framework that manages detection-rule lifecycle "
    "across nine different SIEM and EDR platforms via their native APIs — including token/role/permission "
    "management at the API level and multithreaded parallel deployment across many customers inside a full "
    "GitLab CI/CD pipeline. On top of that platform, I created and maintain 2,300+ detection rules covering most "
    "of the MITRE ATT&CK matrix, and built production GenAI tooling that triages false positives, generates "
    "detection content, and converts rules between SIEM syntaxes automatically."
)
dg.add_cover_paragraph(cl,
    "Today, I direct the detection and alerting content a live SOC runs its incident response against, and "
    "earlier built an entity-behavior analytics platform from scratch for DOE/NNSA — the same instinct this role "
    "is chartered around: identify telemetry gaps, prioritize them, and build the automation that reduces the "
    "manual toil in triage and containment."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of multi-platform detection engineering, "
    "hands-on cloud IAM, and AI-driven automation fits OpenAI's Detection & Response work."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("OpenAI Detection and Response package built.")
