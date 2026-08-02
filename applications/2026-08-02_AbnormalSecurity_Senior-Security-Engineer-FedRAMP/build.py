import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer — Security Operations, SIEM Pipelines & Incident Response")

dg.add_summary(doc,
    "Senior security engineer with 12 years of experience building and running the detection, data, and "
    "access-management pipelines that keep regulated environments secure and audit-ready. Active federal "
    "security clearances (Top Secret, DOE Q, Public Trust) from direct work inside DOE, DOE/NNSA, and Treasury "
    "security programs — including live SOC incident response support, ground-up detection platform builds, and "
    "continuous data-quality/ingestion work in Elasticsearch and Splunk environments. Built and run a multi-SIEM "
    "detection-as-code CI/CD pipeline (GitLab) with automated testing, staged rollout, and rule-quality metrics "
    "tracking — the same operational discipline this role calls for applied to CI/CD, change review, and "
    "SIEM tuning."
)

dg.add_section_heading(doc, "Security Clearances")
dg.add_plain_line(doc,
    "Top Secret — current, sponsored by U.S. Treasury  |  DOE Q Clearance — held  |  Public Trust — held, "
    "sponsored by DOE",
    size=10, bold=True)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Security Operations & Incident Response",
    "SOC detection/alerting content creation and incident support; data ingestion and data-quality monitoring "
    "for federal continuous-diagnostics programs; UEBA baseline modeling and anomaly surfacing")
dg.add_skills_line(doc, "SIEM & Detection-as-Code",
    "Multi-SIEM rule/content orchestration via native APIs — Splunk, Microsoft Sentinel, Microsoft Defender, "
    "Google SecOps (Chronicle), CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight; "
    "GitLab CI/CD pipeline for detection-as-code with automated tests, rule-quality metrics, and staged/safe "
    "production rollout")
dg.add_skills_line(doc, "Access Management",
    "Cloud IAM policy/role implementation (AWS, GCP); creation and governance of API tokens, roles, and "
    "permissions across SIEM platforms as part of an orchestration framework")
dg.add_skills_line(doc, "Cloud & Data Platforms",
    "AWS, GCP, Azure (Sentinel/Defender API orchestration); Elasticsearch (queries, transforms, Beats, native "
    "detection rules, API), Splunk; Docker")
dg.add_skills_line(doc, "Engineering", "Python, SQL, Git, GitLab CI/CD, structured/tested pipeline code")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics (Splunk saved searches) directly "
                   "supporting the Treasury Security Operations Center's incident response and case work — the "
                   "same SIEM-tuning-for-accuracy discipline this role's \"manage logging and monitoring "
                   "pipelines\" responsibility calls for (Treasury SOC / TSSOC, current project).")
dg.add_bullet(doc, "Built an entirely new security data ingestion platform for DOE/NNSA from the ground up — "
                   "CrowdStrike, Suricata, and Zeek telemetry into a central Elasticsearch environment — "
                   "including a UEBA detection layer on custom data transforms, data-quality monitoring/alerting "
                   "content, and custom dashboards (DOE/NNSA Security Data Integration project, completed).")
dg.add_bullet(doc, "Supported data ingestion and data-quality efforts within an Elasticsearch/Splunk environment "
                   "for DOE's Continuous Diagnostics and Mitigation (CDM) program — a federal continuous-"
                   "monitoring initiative directly analogous to the continuous-monitoring and evidence-tracking "
                   "discipline FedRAMP environments require (CISA CDM at DOE, completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "behavioral, statistical, and ML-based detection content against massive-scale customer "
                   "telemetry on a cloud-based big-data platform.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Owned data engineering for a next-gen cloud SIEM at massive scale — 220+ ingested log "
                   "sources, 50+ Logstash parsing/normalization filters, and a Common Information Model "
                   "standardizing field names/types across all of it — plus connector/collector health "
                   "monitoring and troubleshooting to keep the ingestion pipeline reliable.")
dg.add_bullet(doc, "Created and managed 2,300+ individual detection rules covering most of the MITRE ATT&CK "
                   "matrix as a very early hire, building out the rules engine and detection content for the "
                   "startup from scratch.")

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
dg.add_cover_date(cl, "August 2, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nAbnormal Security")
dg.add_cover_paragraph(cl,
    "I've spent the last several years operating inside the kind of regulated, high-scrutiny environments "
    "Abnormal Gov needs to keep FedRAMP-compliant — with active Top Secret (Treasury), DOE Q, and Public Trust "
    "(DOE) clearances earned through direct work on federal security programs, not just adjacent exposure to "
    "them."
)
cl_body = (
    "At Shorepoint, I've worked three sequential federal security engagements that map directly onto this "
    "role's scope. I currently create and manage the detection and alerting analytics (Splunk saved searches) "
    "that support Treasury's Security Operations Center through live incident response and case work — the "
    "same logging-and-monitoring-pipeline ownership this role calls for. Before that, I built DOE/NNSA's "
    "entire Security Data Integration platform from scratch: ingesting CrowdStrike, Suricata, and Zeek "
    "telemetry into a new Elasticsearch environment, then layering UEBA detection, data-quality monitoring and "
    "alerting, and custom dashboards on top of it. And prior to that, I supported data ingestion and data-"
    "quality efforts for DOE's Continuous Diagnostics and Mitigation (CDM) program in an Elasticsearch/Splunk "
    "environment — the same continuous-monitoring discipline FedRAMP's ConMon requirements are built around."
)
dg.add_cover_paragraph(cl, cl_body)
dg.add_cover_paragraph(cl,
    "Beyond the federal-environment specifics, I've built and run a multi-SIEM detection-as-code CI/CD pipeline "
    "in GitLab — orchestrating rule and content deployment across Splunk, Microsoft Sentinel, Microsoft "
    "Defender, Google SecOps, CrowdStrike, SentinelOne, and more via their native APIs, with automated testing, "
    "staged/safe rollout, and rule-quality metrics tracked before anything reaches production. That includes "
    "hands-on creation and governance of API tokens, roles, and permissions across those platforms — the same "
    "access-management discipline this role's RBAC and account-provisioning responsibilities require — plus "
    "Cloud IAM policy work in both AWS and GCP."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that background applies to keeping Abnormal Gov's environment "
    "secure, resilient, and audit-ready."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Abnormal Security FedRAMP package built.")
