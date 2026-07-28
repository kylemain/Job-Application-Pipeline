import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection Engineer — Detection, Response & Threat Intelligence")

dg.add_summary(doc,
    "11+ years building detection engineering programs and incident-response-supporting analytics, from an "
    "early-stage startup rules engine (2,300+ rules across the MITRE ATT&CK matrix) to currently owning "
    "detection content for a live federal SOC's incident response. Deep multi-SIEM/EDR orchestration "
    "experience (nine platforms including CrowdStrike) plus hands-on GenAI-powered detection automation."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection Engineering & Incident Response",
    "Automated detection system design across Splunk, ELK/Elasticsearch, CrowdStrike, SentinelOne, Microsoft "
    "Sentinel/Defender, Google SecOps, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight; MITRE ATT&CK; "
    "incident-response support for a live SOC; large-scale security logging infrastructure")
dg.add_skills_line(doc, "Threat Intelligence & Correlation",
    "Correlating telemetry across identity, cloud, and network sources to detect post-entry behavior; "
    "signature, statistical, behavioral, and ML-based detection logic; UEBA detection content")
dg.add_skills_line(doc, "Automation & Engineering", "Python, SQL; GitLab CI/CD detection-as-code pipelines; "
    "GenAI-powered automated detection systems — false-positive triage, new detection generation, cross-SIEM "
    "rule conversion")
dg.add_skills_line(doc, "Cloud & Data Science", "AWS, GCP, Azure; clustering/unsupervised ML, time-series "
    "anomaly detection")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — own the detection and alerting content "
                   "(Splunk saved searches) that drives the SOC's live incident response, day to day.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the full detection/analytics layer "
                   "on top — dashboards, data transforms, UEBA content, data-quality alerting.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and quality work across a combined Elasticsearch "
                   "and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built automated detection systems and orchestration across nine SIEM/EDR platforms — "
                   "including CrowdStrike — via native APIs, delivered through a full GitLab CI/CD pipeline; "
                   "created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix.")
dg.add_bullet(doc, "Developed GenAI-powered tooling for automated false-positive triage, new detection-content "
                   "generation, and cross-SIEM rule conversion for other detection engineers.")
dg.add_bullet(doc, "Data engineering/pipelining for 220+ log sources; led exploratory data analysis at scale "
                   "using GCP Dataproc, PySpark/SparkSQL.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections; analyzed large-scale "
                   "security log data to surface anomalous behavior.")

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
dg.add_cover_paragraph(cl, "Security, Detection & Response Team\nHubSpot")
dg.add_cover_paragraph(cl,
    "Building detection foundations and response systems that scale with an organization — rather than "
    "growing headcount to match alert volume — is the exact model I've run for the last 11 years, most "
    "recently supporting live incident response for a federal SOC."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built automated detection systems and orchestration across nine SIEM and EDR "
    "platforms, including CrowdStrike, through their native APIs, delivered via a full GitLab CI/CD pipeline, "
    "and created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix. I paired that "
    "with GenAI-powered automation for false-positive triage and detection-content generation, giving the team "
    "leverage without proportional headcount growth — the same automated-detection scaling model this role "
    "centers on."
)
dg.add_cover_paragraph(cl,
    "Currently at Shorepoint, I own the detection and alerting content that Treasury's SOC runs live incident "
    "response against, and I previously built an entire security data platform for DOE/NNSA from raw log "
    "ingestion (CrowdStrike, Suricata, Zeek) through a full UEBA detection layer — correlating telemetry across "
    "cloud, identity, and endpoint sources to catch post-entry behavior, not just individual signatures."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that detection-and-response background fits HubSpot's roadmap."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("HubSpot package built.")
