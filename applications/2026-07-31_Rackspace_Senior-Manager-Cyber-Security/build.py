import sys, os
sys.path.insert(0, "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/2026-07-31_Rackspace_Senior-Manager-Cyber-Security"
os.makedirs(OUT, exist_ok=True)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Detection Engineering & Security Tooling Leader — SIEM/SOAR, Vulnerability Management, Multi-Platform Orchestration")

dg.add_summary(doc,
    "Security engineer and technical team lead with 11 years building, tuning, and scaling detection, SIEM/SOAR, "
    "and vulnerability-management capability — from founding-engineer buildout of a next-gen SIEM startup to "
    "architecting a nine-platform detection-as-code orchestration framework. Deep hands-on ownership of the full "
    "security-tooling lifecycle: deployment, telemetry validation, tuning, and measurable quality/coverage "
    "outcomes, with real technical team-lead and sprint-lead experience directing delivery across engineering teams."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Security Tooling & Detection Engineering Leadership",
    "Architected and led delivery of a native-API orchestration framework spanning nine SIEM/EDR platforms; "
    "directed adoption of automated testing, staged/safe rollout, and formal coverage/false-positive-rate "
    "tracking across the engineering team's detection-as-code pipeline (GitLab CI/CD)")
dg.add_skills_line(doc, "SIEM / SOAR / EDR Platforms",
    "Native-API detection authoring and tooling ownership across Splunk, Microsoft Sentinel, Microsoft Defender, "
    "Google SecOps (Chronicle), CrowdStrike, SentinelOne, Elasticsearch, Sumo Logic, Palo Alto XSIAM, and Devo; "
    "validates telemetry correctness, tuning, and signal-to-noise across every platform deployed")
dg.add_skills_line(doc, "Vulnerability Management & Exposure Data Engineering",
    "Ingests Tenable vulnerability-scan data into SIEM/analytics platforms and builds detection/analytics content "
    "on top of it — vulnerability data engineering and exposure analytics, not just scanner administration; "
    "hands-on security-control evaluation across many vendor tools")
dg.add_skills_line(doc, "Cloud Security, IAM & Automation",
    "AWS/GCP/Azure security telemetry and IAM policy implementation; Python automation with multithreaded "
    "orchestration of detection deployment across SIEM APIs; production GenAI tooling for triage and cross-SIEM "
    "rule conversion")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — owns detection/alerting content (Splunk saved "
                   "searches) as the team's core detection tooling, directly supporting incident investigation "
                   "and response.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built an entirely new Elasticsearch-based "
                   "detection platform from scratch — ingestion, UEBA detection logic, custom dashboards, and "
                   "data-quality monitoring/alerting.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering team owning signature, statistical, behavioral, "
                   "and ML-based detection content and tooling against massive customer telemetry.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Founding engineer who architected a Python-based detection-as-code orchestration framework "
                   "across nine SIEM platforms — served in a technical team-lead/sprint-lead capacity directing "
                   "adoption of automated testing, staged rollout, and coverage/false-positive-rate tracking "
                   "across the engineering team.")
dg.add_bullet(doc, "Built pipelining and detection tooling for 220+ log sources and created/managed 2,300+ "
                   "detection rules covering most of the MITRE ATT&CK matrix as an early hire at this startup.")
dg.add_bullet(doc, "Created and managed API tokens, roles, and permissions across nine SIEM platforms as part of "
                   "the orchestration framework — hands-on access-management/identity work at the platform level.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large security datasets to build custom models for emerging-threat identification, "
                   "including DNS-based malware detection and mitigation across the network.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 31, 2026")
dg.add_cover_paragraph(cl, "Cyber Security Hiring Team\nRackspace Technology")
dg.add_cover_paragraph(cl,
    "Standing up a new observability and vulnerability management team means proving the tooling actually works "
    "— that telemetry is complete, controls are tuned, and coverage is measurable — before it means anything else. "
    "That's the exact work I've done as a founding engineer building a next-gen SIEM from scratch and later "
    "architecting a detection-as-code orchestration framework across nine SIEM and EDR platforms, with automated "
    "testing, staged rollout, and formal coverage and false-positive-rate tracking built in from day one."
)
dg.add_cover_paragraph(cl,
    "That build includes native-API detection and tooling ownership across Splunk, Microsoft Sentinel, "
    "CrowdStrike, SentinelOne, Elasticsearch, and Google SecOps, plus vulnerability data engineering — ingesting "
    "Tenable scan data into analytics platforms and building exposure-analysis content on top of it, rather than "
    "just administering the scanner. I've directed delivery in a technical team-lead and sprint-lead capacity "
    "throughout, driving the testing and rollout discipline a new security tooling team needs to earn trust fast."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to bring that security tooling, detection engineering, and vulnerability management "
    "depth to Rackspace's new observability and vulnerability management team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Rackspace Senior Manager, Cyber Security package built.")
