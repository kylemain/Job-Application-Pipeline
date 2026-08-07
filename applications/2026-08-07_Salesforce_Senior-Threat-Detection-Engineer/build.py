import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Threat Detection Engineer — SIEM/EDR/NDR, MITRE ATT&CK & Incident Response")

dg.add_summary(doc,
    "Threat detection engineer with 12 years of experience writing detection logic against multi-source security "
    "logs, correlating alerts across SIEM/EDR/NDR platforms, and tuning content to cut false positives. Early "
    "hire at a next-gen cloud SIEM startup (Cysiv, spun out of Trend Micro, later acquired by Forescout) where I built the "
    "detection rules engine from scratch and created/managed 2,300+ detection rules covering most of the MITRE "
    "ATT&CK matrix. Currently write and manage Splunk detection/alerting analytics for a federal SOC's incident "
    "response and case work. Run a multi-SIEM detection-as-code CI/CD pipeline across nine platforms — Splunk, "
    "Microsoft Sentinel, Google SecOps, CrowdStrike, SentinelOne, and more — with formally tracked "
    "precision/false-positive-rate metrics and staged rollout before production."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Threat Detection & MITRE ATT&CK",
    "2,300+ detection rules covering most of the MITRE ATT&CK matrix (signature, statistical, behavioral, "
    "aggregation/threshold, ML-based); attack-vector and TTP-aware detection-logic design; formal "
    "coverage/precision/false-positive-rate tracking with staged/safe rollout")
dg.add_skills_line(doc, "SIEM / EDR / NDR / SOAR",
    "Splunk (current, live SOC alerting/analytics); Elasticsearch/Elastic Security (native ES detection rules, "
    "Query DSL, transforms); CrowdStrike and SentinelOne (EDR) rule/content orchestration; Suricata and Zeek "
    "(NDR) telemetry ingestion and detection content; SOAR-style automated multi-SIEM rule deployment")
dg.add_skills_line(doc, "Log Correlation & Multi-Source Analysis",
    "Correlation across network, endpoint, cloud, and SaaS log sources; time-series anomaly detection on "
    "authentication and process-chain behaviors; Common Information Model standardizing fields across 220+ log sources")
dg.add_skills_line(doc, "Multi-SIEM Detection-as-Code & Orchestration",
    "Rule/content orchestration via native APIs across Microsoft Sentinel, Microsoft Defender, Google SecOps "
    "(Chronicle), Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight; GitLab CI/CD "
    "with automated tests and multithreaded parallel deployment")
dg.add_skills_line(doc, "Threat Intel Integration",
    "Uses CTI (indicators, TTPs, actor/campaign context) to tune detection logic and validate true- vs. "
    "false-positive activity; enriched alerts/cases with threat intel (Forescout's Vedere Labs) to speed investigation")
dg.add_skills_line(doc, "Engineering", "Python, SQL, Git, GitLab CI/CD, GCP Dataproc/BigQuery/Dataflow")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Currently write and manage Splunk detection/alerting analytics (saved searches) that serve "
                   "directly as a federal SOC's detection and alerting content, tuning for accuracy and coverage "
                   "against real incidents and cases (Treasury SOC / TSSOC, current project).")
dg.add_bullet(doc, "Built an entirely new detection platform from the ground up — CrowdStrike (EDR), Suricata, "
                   "and Zeek (NDR) telemetry into a central Elasticsearch environment — including a UEBA "
                   "detection layer, custom Kibana dashboards, and data-quality monitoring/alerting content "
                   "(DOE/NNSA Security Data Integration project, completed).")
dg.add_bullet(doc, "Supported data ingestion and data-quality efforts within an Elasticsearch/Splunk environment "
                   "for a federal continuous-monitoring program (CISA CDM at DOE, completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and threat detection engineering team building signature, "
                   "behavioral, statistical, and ML-based detection content against massive-scale customer log "
                   "data, incorporating threat intel from Forescout's in-house Vedere Labs research team to tune "
                   "detection logic and cut false positives.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Very early hire at a next-gen cloud SIEM startup — built the detection rules engine from "
                   "scratch and created/managed 2,300+ individual detection rules covering most of the MITRE "
                   "ATT&CK matrix, plus 50+ data filters, against 220+ ingested log sources.")
dg.add_bullet(doc, "Built time-series anomaly detection for entity behaviors — authentication attempts by "
                   "country/volume, parent/child process chains.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security log data to build custom detection models — DNS-based "
                   "malware detection/mitigation and anomalous-behavior discovery across the network.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 7, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nSalesforce — Threat Detection")
dg.add_cover_paragraph(cl,
    "I'm a threat detection engineer who has spent 12 years writing the detection logic and correlation queries "
    "that catch real attacks against network, endpoint, and cloud infrastructure — and I'd like to bring that "
    "background to Salesforce's Threat Detection team."
)
dg.add_cover_paragraph(cl,
    "As a very early hire at Cysiv (a next-gen cloud SIEM startup that spun out of Trend Micro, later acquired by Forescout), "
    "I built the detection rules engine from scratch and created and managed 2,300+ individual detection rules "
    "covering most of the MITRE ATT&CK matrix — signature, statistical, behavioral, and ML-based content, "
    "written and tuned against massive-scale customer log data across network, endpoint, and cloud sources. I "
    "currently write and manage Splunk detection/alerting analytics that serve directly as a federal SOC's "
    "detection content, and I've built native detection rules directly in Elasticsearch/Elastic Security — work "
    "that maps closely onto writing logic on security platforms to detect malicious activity and refining alert "
    "reliability with the incident response team."
)
dg.add_cover_paragraph(cl,
    "I run a multi-SIEM detection-as-code CI/CD pipeline in GitLab across nine platforms — Splunk, Microsoft "
    "Sentinel, Google SecOps, CrowdStrike, SentinelOne, and more — with formally tracked precision and "
    "false-positive-rate metrics, and I use threat intel directly to validate whether an alert reflects real "
    "adversary activity during triage and false-positive analysis. I'd welcome the chance to bring that same "
    "rigor to detecting attacks against Salesforce's infrastructure, products, employees, and customers."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Salesforce Senior Threat Detection Engineer package built.")
