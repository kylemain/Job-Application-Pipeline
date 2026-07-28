import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Staff Security Engineer — Vulnerability Management")

dg.add_summary(doc,
    "Security engineer with 10+ years building detection and vulnerability data platforms at cloud scale — "
    "including Tenable vulnerability scan ingestion into SIEM/analytics platforms with custom detection content "
    "on top, a Python-based orchestration framework spanning nine SIEM/EDR platforms, and production GenAI "
    "tooling for automated triage. Comfortable, hands-on Docker user with a full GitLab CI/CD pipeline "
    "background for shipping detection-as-code."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Vulnerability Management & Security Data Engineering",
    "Tenable vulnerability scan ingestion into SIEM/analytics platforms; detection content built directly on top "
    "of vulnerability scan data; vulnerability exposure evaluation across production environments; multi-vendor "
    "security control evaluation")
dg.add_skills_line(doc, "AI-Driven Triage & Automation",
    "Prompt engineering for false-positive triage and detection-content generation; GenAI-driven SIEM API "
    "orchestration; reusable GenAI-powered tooling for cross-platform rule conversion")
dg.add_skills_line(doc, "Platform Engineering at Scale",
    "Python-based orchestration framework across nine SIEM/EDR platforms (CrowdStrike, SentinelOne, Splunk, "
    "Google SecOps, Microsoft Sentinel/Defender, Sumo Logic, Palo Alto XSIAM, Devo) via native APIs; "
    "multithreaded parallel deployment across many customers; full GitLab CI/CD pipeline")
dg.add_skills_line(doc, "Cloud, Containers & Access",
    "AWS/GCP/Azure; hands-on IAM policy/role implementation in AWS and GCP; Docker (comfortable, hands-on user — "
    "managed containers/images, built reproducible detection-testing environments)")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead directing sprint priorities and "
                   "technical direction for the detection and alerting content (Splunk) a live SOC runs incident "
                   "response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection layer on top.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Evaluated vulnerability exposure and security controls across production environments, "
                   "including ingestion of Tenable vulnerability scan data into analytics platforms with "
                   "detection content built directly on top of that data.")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms via native APIs, implementing multithreading to deploy and manage "
                   "detection content across many customers in parallel inside a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Created and managed API tokens, roles, and IAM permissions across all nine platforms, plus "
                   "separate IAM policy/role implementation experience in AWS and GCP.")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for false-positive "
                   "triage, automated detection-rule generation, and cross-platform rule conversion.")
dg.add_bullet(doc, "Used Docker to build reproducible containerized environments for testing detection content "
                   "against real log data.")
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
dg.add_cover_paragraph(cl, "Vulnerability Management Hiring Team\nUber")
dg.add_cover_paragraph(cl,
    "Turning raw vulnerability scan data into detection content teams can actually act on is work I've been "
    "doing for years — and I'd love to bring that same data-engineering lens to Uber's Vulnerability Management "
    "Platform."
)
dg.add_cover_paragraph(cl,
    "At Forescout, I evaluated vulnerability exposure and security controls across production environments, "
    "ingesting Tenable vulnerability scan data into analytics platforms and building detection content directly "
    "on top of it. At Trend Micro/Cysiv, I architected a Python-based orchestration framework spanning nine "
    "SIEM/EDR platforms via native APIs, with multithreading to deploy detection content across many customers "
    "in parallel inside a full GitLab CI/CD pipeline — the same shift-left, automate-everything mindset this "
    "role calls for."
)
dg.add_cover_paragraph(cl,
    "I've also built production GenAI tooling for security automation — prompt engineering for triage and "
    "automated rule generation — and have hands-on IAM implementation experience in both AWS and GCP. I "
    "currently direct sprint priorities and technical direction for the Treasury SOC's detection team."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of vulnerability data engineering, multi-"
    "platform orchestration, and AI-driven automation fits the RBVM roadmap."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Uber Vulnerability Management package built.")
