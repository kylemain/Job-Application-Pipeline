import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection Engineer — Threat Intelligence & Incident Response")

dg.add_summary(doc,
    "Senior detection engineer and threat researcher with 10+ years designing detection systems, correlating "
    "threat intelligence, and supporting live incident response. Currently own the Splunk-based detection and "
    "alerting content Treasury's SOC runs incident response against; built detection-as-code orchestration and "
    "CrowdStrike-integrated telemetry across nine SIEM/EDR platforms."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection Engineering & SIEM",
    "Splunk (certified), Elasticsearch/ELK, CrowdStrike, SentinelOne, Microsoft Sentinel/Defender, Google "
    "SecOps, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight; large-scale security logging infrastructure design")
dg.add_skills_line(doc, "Threat Intelligence & Incident Response",
    "MITRE ATT&CK coverage mapping; correlating multi-source telemetry (identity, cloud, endpoint) to detect "
    "post-entry behavior; incident investigation support for a live federal SOC")
dg.add_skills_line(doc, "Automation & Delivery",
    "Full detection-as-code CI/CD pipeline in GitLab; Python; GenAI-powered triage automation and cross-SIEM "
    "rule-conversion tooling for other detection engineers")
dg.add_skills_line(doc, "Data Engineering & Cloud", "220+ log-source pipelines, Common Information Model "
    "design; AWS, GCP, Azure")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — own the detection and alerting content "
                   "(Splunk saved searches) the SOC runs day-to-day incident response against; support "
                   "security incident and case investigations.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform "
                   "ingesting CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection "
                   "layer, dashboards, and data-quality alerting on top.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and quality work across a combined "
                   "Elasticsearch and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, "
                   "behavioral, statistical, time-series, and ML-based detection content against cloud-scale "
                   "customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built detection-as-code orchestration across nine SIEM/EDR platforms — including "
                   "CrowdStrike and SentinelOne — via native APIs, run through a full GitLab CI/CD pipeline; "
                   "created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix.")
dg.add_bullet(doc, "Built time-series anomaly detection for entity behaviors (process chains, authentication "
                   "patterns) and developed GenAI-powered tooling for automated false-positive triage.")
dg.add_bullet(doc, "Data engineering/pipelining for 220+ log sources, including a Common Information Model "
                   "standardizing field names/types across all parsed data.")

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
dg.add_cover_paragraph(cl, "Security, Detection & Response Hiring Team\nHubSpot")
dg.add_cover_paragraph(cl,
    "Building detection foundations that hold up under real incident response — not just passing a demo — is "
    "the standard I've worked to for the past decade across federal and commercial SOCs alike.")
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built detection-as-code orchestration across nine SIEM and EDR platforms, "
    "including CrowdStrike, through their native APIs, delivered through a full GitLab CI/CD pipeline, and "
    "created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix. I paired that with "
    "GenAI-powered automation for false-positive triage and cross-platform rule conversion — the same "
    "detection-in-depth, automation-first approach this role is built around.")
dg.add_cover_paragraph(cl,
    "Currently at Shorepoint, I own the Splunk-based detection and alerting content Treasury's SOC runs "
    "incident response against day to day, correlating telemetry across identity, cloud, and endpoint sources "
    "to support live case investigations. Earlier, at DOE/NNSA, I built an entire security data platform from "
    "raw ingestion through a full UEBA detection layer, including the large-scale logging infrastructure "
    "underneath it.")
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that detection engineering and incident-response background "
    "fits HubSpot's security roadmap.")
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("HubSpot package built.")
