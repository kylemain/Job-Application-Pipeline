import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
doc.sections[0].top_margin = dg.Inches(0.35)
doc.sections[0].bottom_margin = dg.Inches(0.35)
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Threat Intelligence Engineer — Detection Infrastructure, Multi-Source Intel Integration & GenAI Tooling")

dg.add_summary(doc,
    "Security engineer with 12 years building the detection infrastructure and multi-source data integrations "
    "that turn threat intelligence into automated detection and hunting capability — integrating CTI directly "
    "into detection rule logic and alert enrichment, building automated detection systems via native API "
    "integrations across nine external platforms, and applying GenAI/LLM tooling to generate detection content."
)

dg.add_section_heading(doc, "Security Clearance")
dg.add_plain_line(doc,
    "Top Secret — current, sponsored by U.S. Treasury  |  DOE Q Clearance — held  |  Public Trust — held, "
    "sponsored by DOE",
    size=10, bold=True)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Threat Intelligence Integration",
    "Integrating CTI (indicators, TTPs, actor/campaign context) directly into detection rule logic and alert "
    "enrichment; own-research use of threat intel for false-positive analysis; direct exposure to Vedere Labs "
    "(Forescout's in-house threat research team) as a CTI source")
dg.add_skills_line(doc, "GenAI/LLM for Security Automation",
    "Prompt engineering to analyze security data, identify false positives, and generate detection content; "
    "using GenAI to interact with SIEM APIs for content orchestration; built reusable GenAI-powered \"skills\" "
    "for cross-SIEM rule syntax conversion")
dg.add_skills_line(doc, "Automated Detection Systems & Multi-Platform API Integration",
    "Python-based orchestration framework integrating nine external SIEM/EDR platforms via native APIs "
    "(Sentinel, Defender, Chronicle, Splunk, CrowdStrike, SentinelOne, Sumo Logic, XSIAM, Devo) — reusable "
    "adapters, API token/role governance, multithreaded deployment, GitLab CI/CD with automated tests and "
    "staged rollout")
dg.add_skills_line(doc, "Behavioral Analytics & Detection Content",
    "UEBA detection layer on Elasticsearch transforms; time-series anomaly detection; signature/statistical/"
    "behavioral/ML-based detection rules across most of MITRE ATT&CK (2,300+ rules); investigator feedback "
    "loops to tune detection and reduce false positives")
dg.add_skills_line(doc, "Data Engineering & Pipelines",
    "Python, SQL; 220+ ingested log sources (Logstash, Elasticsearch Beats, Common Information Model); "
    "PySpark/GCP Dataproc; Apache Beam/GCP Dataflow for historical retrieval; Elasticsearch queries, "
    "transforms, and API")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics (Splunk saved searches) directly "
                   "supporting Treasury's Security Operations Center — establishing feedback loops with SOC "
                   "investigators to tune detection logic and reduce false positives (Treasury SOC / TSSOC, "
                   "current project).")
dg.add_bullet(doc, "Built an entirely new security data ingestion and behavioral-analytics platform for "
                   "DOE/NNSA from the ground up — CrowdStrike, Suricata, and Zeek telemetry into a central "
                   "Elasticsearch environment, with a UEBA detection layer, data-quality monitoring/alerting, "
                   "and custom dashboards (DOE/NNSA Security Data Integration, completed). Earlier, supported "
                   "data ingestion/quality for DOE's Continuous Diagnostics and Mitigation program in the same "
                   "Elasticsearch/Splunk environment (CISA CDM at DOE, completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "statistical, behavioral, and ML-based detection content against massive-scale customer "
                   "telemetry; incorporated threat intelligence from Vedere Labs, Forescout's in-house threat "
                   "research team, into detection tuning and alert enrichment.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected a Python-based detection-as-code orchestration framework integrating nine "
                   "SIEM/EDR platforms via native APIs — reusable adapters, API token/role governance, and "
                   "multithreaded parallel deployment inside a GitLab CI/CD pipeline — then layered production "
                   "GenAI tooling on top for detection-content generation and cross-platform rule conversion.")
dg.add_bullet(doc, "Very early hire — built the rules engine and detection content for the startup from "
                   "scratch: 2,300+ detection rules covering most of the MITRE ATT&CK matrix, plus data "
                   "engineering for 220+ log sources (Logstash, Elasticsearch Beats, Common Information Model) "
                   "and PySpark/Dataproc EDA at scale.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security log data to build DNS-based malware detection/mitigation "
                   "models and surface anomalous behavior — early foundation translating raw signal into "
                   "automated detection logic.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera) Data Science coursework", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Threat Intelligence Hiring Team\nAnthropic")
dg.add_cover_paragraph(cl,
    "Your Threat Intelligence Engineer role is asking for someone who already lives at the intersection of "
    "threat intelligence and detection engineering — building automated detection systems from disparate "
    "signals, integrating external platforms via APIs, and using GenAI to scale an investigation team's "
    "impact. That combination is exactly what I've spent the last several years building."
)
dg.add_cover_paragraph(cl,
    "At Forescout, I worked threat intelligence from Vedere Labs directly into detection tuning and alert "
    "enrichment — using CTI (indicators, TTPs, actor/campaign context) to validate real adversary activity "
    "versus noise, not just passively consuming a feed. Currently at Shorepoint, I create and manage the "
    "detection analytics that support Treasury's Security Operations Center, and I've built the same "
    "investigator-feedback loop your team needs: working directly with analysts to tune detection logic and "
    "drive down false positives so lead generation stays high-signal."
)
dg.add_cover_paragraph(cl,
    "On the infrastructure side, I architected a Python-based orchestration framework integrating nine "
    "external SIEM/EDR platforms via their native APIs — reusable per-technology adapters, API token/role "
    "governance, and multithreaded parallel deployment inside a full GitLab CI/CD pipeline with automated "
    "testing and staged rollout. That's the same class of problem as correlating signal across VirusTotal, "
    "Censys, and Urlscan-style platforms: building durable, tested integrations rather than one-off scripts."
)
dg.add_cover_paragraph(cl,
    "I've also layered production GenAI tooling directly on top of that detection platform — prompt "
    "engineering to analyze security data and identify false positives, using GenAI to interact with SIEM "
    "APIs for content orchestration, and building reusable GenAI-powered \"skills\" that convert detection "
    "rules between platforms. I'd bring that same instinct to using Claude for TTP extraction and hunting-"
    "query generation here, backed by a UEBA/time-series behavioral analytics background and an active Top "
    "Secret clearance."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background applies to scaling Anthropic's threat "
    "discovery capabilities."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Anthropic Threat Intelligence Engineer package built.")
