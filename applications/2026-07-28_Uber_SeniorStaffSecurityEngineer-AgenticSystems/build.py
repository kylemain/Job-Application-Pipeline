import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Staff Security Engineer — Enterprise Security, Endpoint & Vulnerability Platforms")

dg.add_summary(doc,
    "Security engineer with 10+ years building detection content, vulnerability data analytics, and cloud IAM "
    "programs — with production GenAI experience automating security workflows and a track record directing "
    "sprint priorities and technical direction for a live SOC's detection program. Architected a Python-based "
    "orchestration framework spanning nine SIEM/EDR platforms, hands-on IAM implementation across AWS and GCP, "
    "and vulnerability data pipelines built on Tenable scan data."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "AI-Driven Security Automation",
    "Prompt engineering for triage and detection-content generation; GenAI-driven SIEM API orchestration; "
    "applying frontier AI to reduce human-driven security workflows to automated ones")
dg.add_skills_line(doc, "Vulnerability & Endpoint Security Data",
    "Tenable vulnerability scan ingestion into SIEM/analytics platforms with custom detection content built on "
    "top; vulnerability exposure evaluation across production environments; multi-vendor security control "
    "evaluation")
dg.add_skills_line(doc, "Cloud IAM & Access Governance",
    "Hands-on IAM policy/role implementation in AWS and GCP; created and managed API tokens, roles, and "
    "permissions across nine SIEM/EDR platforms as part of a detection-as-code orchestration framework")
dg.add_skills_line(doc, "Engineering & Technical Leadership",
    "Python (production, multithreaded API orchestration), GitLab CI/CD, Docker, team-lead/sprint-lead "
    "experience directing detection priorities and technical direction for a live SOC")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — serve as team lead directing sprint priorities "
                   "and technical direction for the detection and alerting content (Splunk) a live SOC runs "
                   "incident response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection layer on top — "
                   "entity-behavior analytics purpose-built for proactive threat hunting.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and quality work across a combined Elasticsearch "
                   "and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data.")
dg.add_bullet(doc, "Evaluated vulnerability exposure and security controls across production environments, "
                   "including ingestion of Tenable vulnerability scan data into analytics platforms for "
                   "detection-content development.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms — including CrowdStrike, SentinelOne, and Google SecOps (Chronicle) — via "
                   "native APIs, implementing multithreading to deploy and manage detection content across many "
                   "customers in parallel inside a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Created and managed API tokens, roles, and IAM permissions across all nine platforms as part "
                   "of building that framework — hands-on access-management work at the API level, plus separate "
                   "IAM policy/role implementation experience in AWS and GCP.")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for false-positive "
                   "triage, automated detection-rule generation, and cross-platform rule conversion.")
dg.add_bullet(doc, "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix.")

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
dg.add_cover_paragraph(cl, "Enterprise Security Hiring Team\nUber")
dg.add_cover_paragraph(cl,
    "Transforming enterprise defense from human-driven to AI-driven is exactly the direction I've built my last "
    "several years toward — moving from manual detection content and vulnerability triage to production GenAI "
    "tooling that automates both."
)
cl_p2 = (
    "At Trend Micro/Cysiv, I architected a Python-based detection-as-code orchestration framework spanning nine "
    "SIEM/EDR platforms — including CrowdStrike, SentinelOne, and Google SecOps (Chronicle) — integrated via "
    "native APIs, with multithreading to deploy detection content across many customers in parallel inside a "
    "full GitLab CI/CD pipeline. Building that framework meant creating and managing API tokens, roles, and IAM "
    "permissions across all nine platforms, plus separate hands-on IAM policy and role implementation in both "
    "AWS and GCP."
)
dg.add_cover_paragraph(cl, cl_p2)
dg.add_cover_paragraph(cl,
    "On the vulnerability and endpoint side, I've ingested Tenable vulnerability scan data into analytics "
    "platforms and built detection content on top of it, and evaluated vulnerability exposure and security "
    "controls across production environments. I also built production GenAI tooling — prompt engineering for "
    "triage and automated detection-rule generation — and currently direct sprint priorities and technical "
    "direction for the Treasury SOC's detection team."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of AI-driven automation, multi-platform "
    "security engineering, and hands-on IAM and vulnerability data work fits the Enterprise Security team's "
    "roadmap."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Uber Agentic Systems package built.")
