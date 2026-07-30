import sys, os
sys.path.insert(0, "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/2026-07-30_Fluidstack_Senior-Detection-Engineer"
os.makedirs(OUT, exist_ok=True)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection Engineer")

dg.add_summary(doc,
    "Detection engineer with 8 years owning detection engineering programs end-to-end — threat modeling, "
    "detection design, deployment, and tuning — across nine SIEM/EDR platforms via a Python-based "
    "detection-as-code pipeline with full CI/CD, version control, and measured false-positive rates. "
    "Currently builds and tunes the Splunk-based detection content a live SOC's on-call responders trust "
    "and act on directly."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection-as-Code & MITRE ATT&CK Coverage",
    "Python-based detection-as-code orchestration across nine SIEM/EDR platforms via native APIs (Splunk, "
    "Microsoft Sentinel, Microsoft Defender, Google SecOps/Chronicle, CrowdStrike, SentinelOne, Sumo Logic, "
    "Palo Alto XSIAM, Devo, plus prior ArcSight); full GitLab CI/CD with version control, automated unit/"
    "integration tests, and peer-reviewed staged rollout; 2,300+ detection rules created/managed covering "
    "most of the MITRE ATT&CK matrix, with coverage/precision/false-positive-rate tracked and tuned, not guessed")
dg.add_skills_line(doc, "SIEM/EDR Pipeline Health & Telemetry",
    "Data engineering for 220+ log sources feeding Splunk/Elasticsearch pipelines: 50+ Logstash filters, "
    "Elasticsearch Beats deployment, a Common Information Model standardizing schema across all parsed data, "
    "and connector/collector health monitoring so on-call responders can trust what pages them")
dg.add_skills_line(doc, "Incident Support & Detection Tuning",
    "Analytically supports a live SOC's (Treasury) case/incident queue end to end, building and tuning the "
    "Splunk detection and alerting content responders investigate against; knows the difference between a "
    "noisy rule and a broken one and tunes or retires detections before responders learn to ignore them")
dg.add_skills_line(doc, "Threat Intel-Informed Investigation",
    "Uses CTI (Vedere Labs and other sources) directly during alert triage and false-positive analysis to "
    "validate whether an alert reflects real adversary activity, and feeds that research back into detection "
    "logic — closing the loop from investigation to durable detection rather than one-off fixes")
dg.add_skills_line(doc, "Automation & AI-Powered Tooling",
    "Production Python automation for triage/enrichment and multithreaded parallel deployment of detection "
    "content across many environments; production GenAI tooling for false-positive triage and cross-platform "
    "detection-rule conversion, reducing manual triage load without proportional headcount")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead directing sprint priorities and "
                   "technical direction for the Splunk-based detection and alerting content a live SOC runs "
                   "incident investigations against; tunes rules on measured false-positive rate, not instinct.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform from "
                   "scratch ingesting CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the UEBA detection "
                   "layer, custom dashboards, and data-quality monitoring/alerting on top — a ground-up build, "
                   "not an inherited program.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building cloud-based big-data "
                   "detection content and infrastructure against massive customer telemetry; threat intel "
                   "sourced from Vedere Labs, Forescout's in-house research team, directly informed detection tuning.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected and built a Python-based detection-as-code orchestration framework across nine "
                   "SIEM/EDR platforms via native APIs — reusable per-technology adapters for every interaction "
                   "method (rule management, alerts, tables, schemas) — with multithreading to deploy detection "
                   "content across many customers in parallel inside a full GitLab CI/CD pipeline, including "
                   "automated unit/integration tests and staged rollout before full production deployment.")
dg.add_bullet(doc, "Data engineering/pipelining for 220+ unique log data sources: 50+ Logstash filters, deployed "
                   "Elasticsearch Beats for log collection, built a Common Information Model standardizing field "
                   "names/types across all parsed data, and assisted building 'Loggify,' a homegrown log "
                   "parsing/filtering tool that replaced Logstash.")
dg.add_bullet(doc, "Built time-series anomaly detection on entity behavior (process chains, authentication "
                   "patterns) to surface adversary activity existing signature-based rules missed, and built "
                   "production GenAI tooling for detection-rule generation and cross-platform rule conversion.")
dg.add_bullet(doc, "Created and managed API tokens, roles, and permissions across the nine SIEM platforms; "
                   "created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Security Clearances: Top Secret (current, Treasury) · DOE Q Clearance · Public Trust (DOE)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 30, 2026")
dg.add_cover_paragraph(cl, "Security & Corp IT Hiring Team\nFluidstack")
dg.add_cover_paragraph(cl,
    "Your posting asks for someone who owns a detection engineering program end to end — threat modeling, "
    "detection design, deployment, and tuning, with coverage mapped to MITRE ATT&CK and gaps documented rather "
    "than assumed away. That is precisely the shape of the work I've been doing for the last eight years."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I architected a Python-based detection-as-code framework spanning nine SIEM and EDR "
    "platforms — Splunk, Sentinel, Defender, Google SecOps, CrowdStrike, SentinelOne, Sumo Logic, XSIAM, and "
    "Devo — through a full GitLab CI/CD pipeline with version control, automated tests, and peer-reviewed "
    "staged rollout before anything shipped. I created and managed 2,300+ detection rules covering most of "
    "the MITRE ATT&CK matrix, with coverage, precision, and false-positive rate tracked and tuned rather than "
    "guessed — the difference between a noisy rule and a broken one matters when responders have to trust "
    "what pages them."
)
dg.add_cover_paragraph(cl,
    "I currently build and tune the Splunk detection content Treasury's SOC runs live incident investigations "
    "against, and before that built a security data platform from scratch at DOE/NNSA — ingesting CrowdStrike, "
    "Suricata, and Zeek into Elasticsearch and layering UEBA detection content on top with no inherited program "
    "to build from. Threat intel informs that tuning directly rather than sitting in a passive feed, and I've "
    "shipped production GenAI tooling that cuts manual triage load without adding headcount."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of detection-as-code ownership, MITRE-mapped "
    "coverage, and hands-on SIEM/EDR pipeline health fits the detection engineering work ahead for Fluidstack's "
    "Security & Corp IT team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Fluidstack Senior Detection Engineer package built.")
