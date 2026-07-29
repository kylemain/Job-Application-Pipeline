import sys, os
sys.path.insert(0, "/sessions/eloquent-festive-gauss/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Security Engineering Lead — Cloud & Data Security")

dg.add_summary(doc,
    "Security engineer with 10+ years building and leading detection, data-security, and cloud-IAM work across "
    "AWS and GCP — including hands-on IAM policy/role implementation and creating/managing API tokens, roles, "
    "and permissions across nine SIEM platforms. Team-lead/sprint-lead experience directing technical priorities "
    "for a live SOC. Builds production AI/GenAI tooling to scale security operations."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Cloud & Data Security",
    "Hands-on IAM policy/role implementation in AWS and GCP; data security and access-control work across "
    "SIEM/Elasticsearch platforms; created and managed API tokens, roles, and permissions across nine SIEM "
    "platforms as part of a detection orchestration framework")
dg.add_skills_line(doc, "Detection & Prevention Controls",
    "2,300+ detection rules covering most of the MITRE ATT&CK matrix; cloud-native and endpoint telemetry "
    "detection content; formally tracks detection quality metrics (coverage, precision/false-positive rate) with "
    "staged rollout before full production")
dg.add_skills_line(doc, "Containers & Infrastructure",
    "Comfortable, hands-on Docker user managing containers/images for reproducible detection-testing "
    "environments; has worked within a Kubernetes-orchestrated platform (user of the platform, not cluster "
    "administration); GitLab CI/CD as the backbone for detection-as-code pipelines")
dg.add_skills_line(doc, "Multi-SIEM Orchestration & AI Tooling",
    "Built rule-lifecycle orchestration across nine SIEM/EDR platforms (Microsoft Sentinel, Defender, Google "
    "SecOps/Chronicle, Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo) via native APIs; "
    "multithreaded parallel deployment; production GenAI tooling for triage, detection-rule generation, and "
    "cross-platform rule conversion")
dg.add_skills_line(doc, "Leadership & Partnership",
    "Team-lead/sprint-lead experience directing technical priorities and mentoring detection engineers; "
    "embedded-partner track record working directly with SOC, IR, and platform teams to ship secure-by-default "
    "detection content")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — directs sprint priorities and technical "
                   "direction for the Splunk-based detection and alerting content a live SOC runs incident "
                   "response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection layer, "
                   "data-quality monitoring, and alerting content on top — real hands-on data-security and "
                   "access-governance work on a platform other teams built on.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer "
                   "telemetry.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms via native APIs — including creating and managing API tokens, roles, and "
                   "permissions at the API level, and multithreaded parallel deployment across many customers "
                   "inside a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Implemented AWS and GCP IAM policies and roles as part of the platform's identity and "
                   "access-management footprint.")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for false-positive "
                   "triage, automated detection-rule generation, and cross-platform rule conversion; developed "
                   "reusable GenAI-powered 'skills' for detection engineers to automate repetitive tasks.")
dg.add_bullet(doc, "Data engineering for 220+ log data sources feeding the detection platform; used Docker for "
                   "reproducible detection-testing environments; created and managed 2,300+ detection rules "
                   "covering most of the MITRE ATT&CK matrix.")

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
dg.add_cover_date(cl, "July 29, 2026")
dg.add_cover_paragraph(cl, "Security Engineering Hiring Team\nAirbnb")
dg.add_cover_paragraph(cl,
    "Securing the infrastructure and data platforms that everything else runs on is quieter work than detection "
    "and response, but it's the same discipline: understand the system, find the gap, build the control that "
    "closes it without getting in engineers' way."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built a Python-based orchestration framework managing detection-rule lifecycle "
    "across nine SIEM and EDR platforms via their native APIs — which meant creating and managing API tokens, "
    "roles, and permissions across every one of those platforms, real hands-on identity and access-management "
    "work at the API level. I've implemented IAM policies and roles directly in both AWS and GCP, and built "
    "production GenAI tooling that automates triage and detection-content generation, cutting manual effort out "
    "of security operations."
)
dg.add_cover_paragraph(cl,
    "Today at Shorepoint, I direct the technical priorities for the detection and alerting content a live SOC "
    "runs its incident response against, and earlier built an entire security data platform from scratch for "
    "DOE/NNSA — ingesting CrowdStrike, Suricata, and Zeek telemetry into Elasticsearch and layering data-quality "
    "monitoring and access governance on top. I'd welcome the chance to bring that same builder-and-partner "
    "instinct to Airbnb's Cloud & Data Security team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Airbnb EM Cloud & Data Security package built.")
