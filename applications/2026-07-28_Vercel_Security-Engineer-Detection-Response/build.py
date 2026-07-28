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
    "Senior detection engineer with 10+ years building SIEM detection content, security logging pipelines, "
    "and incident-response support across nine SIEM/EDR platforms. Hands-on with AWS cloud security, endpoint "
    "telemetry (CrowdStrike, SentinelOne), and Python automation; currently support live SOC incident response "
    "for a federal team."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Security Operations & Detection",
    "SIEM detection engineering and alerting across Splunk, Elasticsearch/ELK, CrowdStrike, SentinelOne, "
    "Microsoft Sentinel/Defender, Google SecOps, Sumo Logic, Palo Alto XSIAM, Devo; incident detection, triage, "
    "and investigation support")
dg.add_skills_line(doc, "Cloud & Infrastructure Security",
    "AWS, GCP, Azure cloud security; Docker for reproducible detection-testing environments; GitLab CI/CD for "
    "detection-as-code delivery")
dg.add_skills_line(doc, "Automation & Scripting",
    "Python, SQL; GenAI-powered triage automation; MITRE ATT&CK coverage mapping")
dg.add_skills_line(doc, "Data Engineering", "220+ log-source ingestion pipelines, log parsing/normalization/"
    "enrichment, Common Information Model design, data-quality monitoring and alerting")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — own the detection and alerting content "
                   "(Splunk saved searches) the SOC runs day-to-day incident response against; support "
                   "security incident and case investigations.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform "
                   "ingesting CrowdStrike, Suricata, and Zeek into Elasticsearch, plus custom dashboards, "
                   "UEBA detection content, and data-quality monitoring/alerting on top.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and quality work across a combined "
                   "Elasticsearch and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, "
                   "behavioral, statistical, time-series, and ML-based detection content against cloud-scale "
                   "customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built detection-as-code orchestration across nine SIEM/EDR platforms — including "
                   "CrowdStrike and SentinelOne — via native APIs, run through a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix; "
                   "50+ data filters for parsing and normalization across 220+ log sources.")
dg.add_bullet(doc, "Used Docker to build reproducible detection-testing environments for validating content "
                   "against real log data.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections; analyzed large-scale "
                   "security log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 28, 2026")
dg.add_cover_paragraph(cl, "Detection Response Hiring Team\nVercel")
dg.add_cover_paragraph(cl,
    "Keeping security visibility and logging infrastructure trustworthy — so alerts mean something when they "
    "fire — is work I've done across federal and commercial SOCs for the past decade.")
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built detection-as-code orchestration across nine SIEM and EDR platforms, "
    "including CrowdStrike and SentinelOne, through their native APIs, run through a full GitLab CI/CD "
    "pipeline, and created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix. I also "
    "built the telemetry layer itself: 50+ parsing/normalization filters across 220+ log sources, keeping "
    "signal quality high enough to act on.")
dg.add_cover_paragraph(cl,
    "Currently at Shorepoint, I own the detection and alerting content Treasury's SOC runs incident response "
    "against, working hands-on with AWS cloud security and endpoint telemetry to support live investigations "
    "and harden internal security posture.")
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background fits Vercel's CorpSec and detection roadmap.")
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Vercel package built.")
