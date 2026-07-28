import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Staff Security Engineer — Detection & Response, AI-Driven Threat Hunting")

dg.add_summary(doc,
    "Security engineer with 10+ years building detection content, threat-hunting analytics, and incident-"
    "response tooling — with production GenAI experience automating triage and detection generation well past "
    "scripting. Built and operated a multithreaded, API-driven orchestration framework across nine SIEM/EDR "
    "platforms including CrowdStrike, SentinelOne, Splunk, and Google SecOps (Chronicle), and has led sprint "
    "planning and technical direction for a live SOC's detection team."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "AI-Driven Security Automation",
    "Prompt engineering for false-positive triage and detection-content generation; GenAI-driven SIEM API "
    "orchestration; reusable GenAI-powered tooling for cross-platform detection-rule conversion")
dg.add_skills_line(doc, "Threat Hunting & Investigation",
    "Entity-behavior time-series anomaly detection (authentication anomalies by country/volume, parent/child "
    "process chains), DNS-based malware detection and mitigation, MITRE ATT&CK-aligned detection content")
dg.add_skills_line(doc, "SIEM / EDR Platforms",
    "CrowdStrike, SentinelOne, Splunk, Google SecOps (Chronicle), Microsoft Sentinel, Microsoft Defender, Sumo "
    "Logic, Palo Alto XSIAM, Devo, ArcSight — native API integration across all nine")
dg.add_skills_line(doc, "Engineering & Technical Leadership",
    "Python (production, multithreaded API orchestration), GitLab CI/CD, team-lead/sprint-lead experience "
    "directing detection priorities for a live SOC, AWS/GCP/Azure")

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

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms — including CrowdStrike, SentinelOne, and Google SecOps (Chronicle) — via "
                   "native APIs, implementing multithreading to deploy and manage detection content across many "
                   "customers in parallel inside a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Created and managed API tokens, roles, and permissions across all nine platforms as part of "
                   "building that framework — hands-on access-management work at the API level.")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for false-positive "
                   "triage, automated detection-rule generation, and cross-platform rule conversion.")
dg.add_bullet(doc, "Investigated anomalous entity behavior at scale for threat hunting: authentication-attempt "
                   "anomalies by country/volume, parent/child process chains, and Outlook process-chain analysis.")
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
dg.add_cover_paragraph(cl, "Cyber Defense Hiring Team\nUber")
dg.add_cover_paragraph(cl,
    "Defending at machine speed against AI-driven adversaries is exactly the shift I've spent the last several "
    "years building toward — moving from manual detection content to production GenAI tooling that automates "
    "triage and response."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I architected a Python-based detection-as-code orchestration framework spanning nine "
    "SIEM/EDR platforms — including CrowdStrike, SentinelOne, Splunk, and Google SecOps (Chronicle) — all "
    "integrated via native APIs, with multithreading to deploy detection content across many customers in "
    "parallel inside a full GitLab CI/CD pipeline. On top of that framework, I built production GenAI tooling: "
    "prompt engineering for false-positive triage, automated detection-rule generation, and cross-platform rule "
    "conversion — the same class of AI-driven automation this role is built to scale."
)
dg.add_cover_paragraph(cl,
    "My threat-hunting background is hands-on and proactive: investigating anomalous entity behavior at scale "
    "(authentication anomalies by country and volume, parent/child process chains) and building the UEBA "
    "detection layer on top of a from-scratch security data platform for DOE/NNSA. I currently lead sprint "
    "planning and technical direction for the Treasury SOC's detection team, and created and managed 2,300+ "
    "detection rules covering most of the MITRE ATT&CK matrix over my career."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of AI-driven automation, multithreaded systems "
    "engineering, and hands-on threat hunting fits Uber's Cyber Defense roadmap."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Uber package built.")
