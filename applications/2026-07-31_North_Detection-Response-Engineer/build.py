import sys, os
sys.path.insert(0, "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/2026-07-31_North_Detection-Response-Engineer"
os.makedirs(OUT, exist_ok=True)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Detection & Response Engineer — SIEM, AI-Enabled SOC & Security Automation")

dg.add_summary(doc,
    "Detection engineer with 8 years building, tuning, and improving detection and response capability across "
    "SIEM, EDR, and cloud telemetry. Deep MITRE ATT&CK-mapped coverage (2,300+ production detection rules), "
    "hands-on incident response support, and production experience applying GenAI/LLM tooling to SOC triage and "
    "detection-content automation — reducing analyst toil while keeping outcomes measurable and safe."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection Engineering & MITRE ATT&CK",
    "Designed, built, and tuned detection content (rules, correlation logic) across endpoint, network, cloud, "
    "and identity log sources; created/managed 2,300+ detection rules with formal coverage and gap analysis "
    "against the MITRE ATT&CK matrix; version-controlled, tested, staged-rollout detection-as-code pipeline in GitLab")
dg.add_skills_line(doc, "SIEM & EDR Platforms",
    "Native-API detection authoring across Splunk, Microsoft Sentinel, Microsoft Defender, Google SecOps "
    "(Chronicle), CrowdStrike, SentinelOne, Elasticsearch, Sumo Logic, Palo Alto XSIAM, and Devo; log analysis "
    "across endpoint, network, cloud, and identity sources")
dg.add_skills_line(doc, "AI-Enabled SOC & Automation",
    "Production GenAI/LLM tooling for false-positive triage, detection-rule generation, and cross-SIEM rule "
    "conversion; Python automation and multithreaded orchestration of detection deployment across SIEM APIs; "
    "applies sound judgment on where AI output needs human validation for high-confidence detections")
dg.add_skills_line(doc, "Incident Response & Threat Intel",
    "Supports incident investigation and response for a live Treasury SOC; integrates threat intelligence "
    "(indicators, TTPs, campaign context) into detection tuning and alert enrichment; hands-on with AWS, GCP, "
    "and Azure security telemetry")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — creates and manages detection/alerting content "
                   "(Splunk saved searches), directly supporting incident investigation and response.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new Elasticsearch-based detection "
                   "platform from scratch — ingestion, UEBA detection logic, data-quality alerting.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering team building signature, statistical, behavioral, "
                   "and ML-based detection content against massive customer telemetry.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected a Python-based detection-as-code orchestration framework across nine SIEM "
                   "platforms — automated tests, staged rollout, and quality-metric tracking (coverage, "
                   "false-positive rate) for every deployment.")
dg.add_bullet(doc, "Built pipelining and detection authoring for 220+ log sources and created/managed 2,300+ "
                   "detection rules covering most of the MITRE ATT&CK matrix as a founding engineer at this startup.")
dg.add_bullet(doc, "Developed production GenAI-powered tooling to automate false-positive triage, detection-rule "
                   "generation, and cross-platform rule conversion — a scalable model for AI-assisted SOC operations.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 31, 2026")
dg.add_cover_paragraph(cl, "Detection & Response Hiring Team\nNorth")
dg.add_cover_paragraph(cl,
    "Closing the gap between detection and resolution takes both engineering rigor and a willingness to put AI "
    "to work where it genuinely reduces toil. I've built exactly that combination: a detection-as-code pipeline "
    "spanning nine SIEM platforms with version control, automated testing, and staged rollout, alongside "
    "production GenAI tooling that automates false-positive triage and detection-rule generation for a live SOC."
)
dg.add_cover_paragraph(cl,
    "That build includes 2,300+ detection rules mapped to the MITRE ATT&CK matrix, native-API detection authoring "
    "across Splunk, Microsoft Sentinel, CrowdStrike, and Google SecOps, and Python automation orchestrating "
    "deployment across every platform in parallel. On my current team, I support incident investigation and "
    "response for a live Treasury SOC, using threat intelligence to tune detections and speed root-cause analysis "
    "— applying good judgment on when AI-assisted findings need human validation before acting on them."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to bring that detection engineering, AI-enabled SOC, and automation experience to "
    "North's Detection and Response team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("North Detection and Response Engineer package built.")
