import sys, os
sys.path.insert(0, "/sessions/eloquent-festive-gauss/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection Engineer — Threat Intelligence & Detection Content")

dg.add_summary(doc,
    "Security engineer integrating threat intelligence into detection engineering — using CTI (indicators, TTPs, "
    "actor/campaign context) to tune detection logic and enrich alerts, on top of a decade building "
    "detection-as-code across cloud and endpoint telemetry. Builds production AI/GenAI tooling for triage, "
    "signal enrichment, and detection-content generation. Hands-on across AWS, GCP, and multi-cloud identity."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Threat Intelligence Integration",
    "Integrates CTI into detection rule logic and alert enrichment — actor/campaign context and indicators used "
    "to tune detections and speed triage; uses threat intel directly for own research during investigations and "
    "false-positive analysis; worked across paid/commercial, open-source, and home-grown intel (Forescout's "
    "Vedere Labs threat research team)")
dg.add_skills_line(doc, "AI-Assisted Security Workflows",
    "Production GenAI tooling for alert triage, false-positive analysis, automated detection-rule generation, "
    "and cross-SIEM rule-syntax conversion; prompt engineering for security use cases; GenAI-driven SIEM API "
    "orchestration")
dg.add_skills_line(doc, "Multi-SIEM Detection-as-Code Orchestration",
    "Built rule-lifecycle orchestration across nine SIEM/EDR platforms (Microsoft Sentinel, Defender, Google "
    "SecOps/Chronicle, Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo) via native APIs; "
    "multithreaded parallel deployment inside a full GitLab CI/CD pipeline; formally tracks detection quality "
    "metrics (coverage, precision/false-positive rate) with staged rollout before full production")
dg.add_skills_line(doc, "Cloud & Data at Scale",
    "Python and SQL against large security datasets; hands-on IAM policy/role implementation in AWS and GCP; "
    "PySpark/Dataproc/BigQuery for exploratory analysis at scale; created and managed API tokens, roles, and "
    "permissions across nine SIEM platforms")
dg.add_skills_line(doc, "Detection Engineering & Threat Hunting",
    "2,300+ detection rules covering most of the MITRE ATT&CK matrix; signature, behavioral, statistical, "
    "time-series, and ML-based detection; time-series anomaly detection of entity behaviors (auth, process "
    "chains); team-lead/sprint-lead experience mentoring detection engineers")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — creates and manages the Splunk-based detection "
                   "and alerting content a live SOC runs incident response against, incorporating threat intel "
                   "context into detection logic and case enrichment to speed triage.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection layer, data-quality "
                   "monitoring, and alerting content on top.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team; drew on threat intel from "
                   "Vedere Labs (Forescout's in-house research team) plus paid and open-source CTI to build "
                   "signature, behavioral, statistical, time-series, and ML-based detection content at cloud "
                   "scale.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms via native APIs, with multithreading to deploy and manage detection content "
                   "across many customers in parallel inside a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Used threat intelligence (indicators, TTPs, actor/campaign context) to tune detection rule "
                   "logic and enrich alerts, and to validate true-positive vs. false-positive findings during "
                   "investigations across 2,300+ detection rules covering most of the MITRE ATT&CK matrix.")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for false-positive "
                   "triage, automated detection-rule generation, and cross-platform rule conversion; developed "
                   "reusable GenAI-powered 'skills' for detection engineers to automate repetitive tasks.")
dg.add_bullet(doc, "Data engineering for 220+ log data sources feeding the detection platform; 50+ Logstash "
                   "filters; created and managed API tokens, roles, and permissions across nine SIEM platforms as "
                   "part of the orchestration framework.")

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
dg.add_cover_paragraph(cl, "Global Security Hiring Team\nSnowflake")
dg.add_cover_paragraph(cl,
    "Threat intelligence is only as useful as what it changes downstream — the detection it tunes, the alert it "
    "enriches, the investigation it speeds up. That's the seam I've worked in for the past decade: turning "
    "intelligence into concrete defensive outcomes rather than treating it as a feed to file away."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I used threat intel — indicators, TTPs, actor and campaign context — to tune "
    "detection rule logic and enrich alerts across a library of 2,300+ detection rules covering most of the "
    "MITRE ATT&CK matrix, and to validate true-positive versus false-positive findings during my own "
    "investigations. On top of that, I built a Python-based orchestration framework managing detection-rule "
    "lifecycle across nine SIEM and EDR platforms via their native APIs, and shipped production GenAI tooling "
    "that automates false-positive triage, detection-content generation, and rule conversion between platforms — "
    "exactly the kind of AI-assisted intelligence workflow this role is chartered to build."
)
dg.add_cover_paragraph(cl,
    "At Forescout, I worked alongside intelligence from Vedere Labs — the company's in-house threat research "
    "team — plus paid/commercial and open-source CTI, giving me exposure to how varied intelligence sources get "
    "curated, evaluated, and turned into something detection engineers can actually use. Today at Shorepoint, I "
    "create and manage the detection and alerting content a live SOC runs its incident response against for "
    "Treasury, folding threat intel context into that content along the way. I'd welcome the chance to bring "
    "that same intelligence-to-detection instinct to Snowflake's Threat Intelligence program."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Snowflake Principal Security Engineer - Threat Intelligence package built.")
