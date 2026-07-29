import sys, os
sys.path.insert(0, "/sessions/eloquent-festive-gauss/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Security Engineering Lead — Detection, Response & CI/CD Security")

dg.add_summary(doc,
    "Security engineer with 10+ years leading detection-and-response engineering and technical sprint priorities "
    "for a live SOC, building CI/CD-integrated detection-as-code across nine SIEM/EDR platforms, and implementing "
    "IAM policy/role work in AWS and GCP. Team-lead/sprint-lead experience mentoring detection engineers and "
    "coordinating cross-team technical priorities."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection & Response",
    "Creates and manages the detection and alerting content a live SOC runs incident response against (Splunk); "
    "2,300+ detection rules covering most of the MITRE ATT&CK matrix; signature, behavioral, statistical, "
    "time-series, and ML-based detection across nine SIEM/EDR platforms including CrowdStrike and SentinelOne")
dg.add_skills_line(doc, "CI/CD & Detection-as-Code Security",
    "Full CI/CD pipeline for detection-as-code in GitLab; writes automated unit/integration tests for the "
    "pipeline itself; formally tracks detection quality metrics (coverage, precision/false-positive rate) with "
    "staged rollout before full production")
dg.add_skills_line(doc, "Identity & Access Management",
    "Hands-on IAM policy/role implementation in AWS and GCP; created and managed API tokens, roles, and "
    "permissions across nine SIEM platforms as part of a detection orchestration framework")
dg.add_skills_line(doc, "Sprint & Technical Leadership",
    "Team-lead/sprint-lead experience directing sprint priorities and technical direction for a live SOC's "
    "detection content; mentors detection engineers; embedded partner working directly with SOC, IR, and "
    "platform teams")
dg.add_skills_line(doc, "Containers & Cloud",
    "Comfortable, hands-on Docker user; has worked within a Kubernetes-orchestrated platform; familiar with "
    "AWS and GCP cloud environments; production GenAI tooling for security automation and triage")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — directs sprint priorities and technical "
                   "direction for the Splunk-based detection and alerting content a live SOC runs incident "
                   "response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection layer, "
                   "data-quality monitoring, and alerting content on top.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer "
                   "telemetry.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms (including CrowdStrike and SentinelOne) via native APIs, with multithreading "
                   "to deploy detection content across many customers in parallel inside a full GitLab CI/CD "
                   "pipeline — including automated tests for the pipeline itself.")
dg.add_bullet(doc, "Created and managed API tokens, roles, and permissions across those nine platforms, and "
                   "implemented AWS/GCP IAM policies and roles as part of the platform's access-management "
                   "footprint.")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for false-positive "
                   "triage, automated detection-rule generation, and cross-platform rule conversion.")
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
dg.add_cover_paragraph(cl, "Security Engineering Hiring Team\nReverb")
dg.add_cover_paragraph(cl,
    "Musical instruments and detection engineering don't obviously belong in the same sentence, but the "
    "underlying job is familiar: protect a platform people trust, without slowing down the teams building on "
    "top of it."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built a Python-based detection-as-code orchestration framework spanning nine "
    "SIEM and EDR platforms — including CrowdStrike and SentinelOne — via their native APIs, run inside a full "
    "GitLab CI/CD pipeline with automated tests for the pipeline itself and staged rollout before full "
    "production. That work included creating and managing API tokens, roles, and permissions across every one "
    "of those platforms, plus hands-on IAM policy and role implementation in both AWS and GCP."
)
dg.add_cover_paragraph(cl,
    "Today at Shorepoint, I direct sprint priorities and technical direction for the detection and alerting "
    "content a live SOC runs its incident response against for Treasury — the same rhythm of sprint planning, "
    "prioritization, and cross-team coordination this role is built around. I'd welcome the chance to bring that "
    "combination of hands-on detection engineering and sprint leadership to Reverb's Security Engineering team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Reverb Security Engineering Manager package built.")
