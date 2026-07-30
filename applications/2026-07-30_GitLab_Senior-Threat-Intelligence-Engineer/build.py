import sys, os
sys.path.insert(0, "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/2026-07-30_GitLab_Senior-Threat-Intelligence-Engineer"
os.makedirs(OUT, exist_ok=True)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer — Detection Engineering & Threat Intelligence")

dg.add_summary(doc,
    "Detection engineer with 8 years using cyber threat intelligence to drive detection engineering decisions — "
    "validating alerts against real adversary activity, tuning detection logic based on CTI context, and closing "
    "the loop from intelligence to durable detection content. Builds Python-based automation and detection-as-code "
    "pipelines across nine SIEM/EDR platforms, with hands-on Elasticsearch/ELK experience spanning three employers."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Threat Intelligence Integration for Detection Engineering",
    "Uses CTI (indicators, TTPs, actor/campaign context) directly during alert triage and false-positive analysis "
    "to validate whether an alert reflects real adversary activity vs. benign behavior, then feeds that research "
    "back into detection logic; sourced from paid/commercial feeds, open-source intelligence, and in-house research "
    "(Vedere Labs, Forescout's threat research team) — closing the loop from intel to detection rather than "
    "passively consuming feeds")
dg.add_skills_line(doc, "Python Automation & Scripting",
    "Production Python automation for alert triage/enrichment and detection-content deployment; production GenAI "
    "tooling for false-positive triage and cross-platform detection-rule conversion; multithreaded orchestration "
    "across many customer environments in parallel")
dg.add_skills_line(doc, "Detection-as-Code & Multi-SIEM Orchestration",
    "Built a Python-based detection-as-code framework across nine SIEM/EDR platforms via native APIs (Splunk, "
    "Microsoft Sentinel, Microsoft Defender, Google SecOps, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, "
    "Devo) with full GitLab CI/CD, automated tests, and staged rollout; created/managed 2,300+ detection rules "
    "covering most of the MITRE ATT&CK matrix")
dg.add_skills_line(doc, "Elasticsearch / ELK Stack",
    "Deep, cross-employer Elasticsearch experience: ES queries and transforms, Logstash parsing/normalization, "
    "multiple Beats variants for log collection, native ES detection rules, the Elasticsearch API, and Kibana "
    "dashboarding — built an entire ES-based security data platform from scratch at DOE/NNSA and a next-gen "
    "ES/Kibana SIEM at Trend Micro/Cysiv")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead directing sprint priorities for the "
                   "detection and alerting content a live SOC's responders investigate against; uses threat intel "
                   "directly during triage/false-positive analysis to validate real adversary activity.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new Elasticsearch-based security data "
                   "platform from scratch ingesting CrowdStrike, Suricata, and Zeek, plus the UEBA detection layer, "
                   "Kibana dashboards, and data-quality monitoring/alerting — a ground-up build, not an inherited program.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building detection content against "
                   "massive customer telemetry; threat intel sourced directly from Vedere Labs, Forescout's in-house "
                   "research team, informed detection tuning and alert triage on a daily basis.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected a Python-based detection-as-code orchestration framework across nine SIEM/EDR "
                   "platforms via native APIs, with multithreaded deployment inside a full GitLab CI/CD pipeline "
                   "including automated tests and staged rollout before production.")
dg.add_bullet(doc, "Built the Elasticsearch-based data engineering layer for 220+ log sources: 50+ Logstash filters, "
                   "multiple Elasticsearch Beats deployments, a Common Information Model standardizing schema, and "
                   "wrote detection rules and queries directly against ES indexes as core detection content in the "
                   "team's next-gen ES/Kibana SIEM.")
dg.add_bullet(doc, "Built time-series anomaly detection on entity behavior (process chains, authentication patterns) "
                   "to surface adversary activity signature-based rules missed; built production GenAI tooling for "
                   "detection-rule generation and cross-platform rule conversion.")
dg.add_bullet(doc, "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix, informed "
                   "by threat intel context on adversary TTPs and campaign activity.")

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
dg.add_cover_paragraph(cl, "Security Operations Hiring Team\nGitLab")
dg.add_cover_paragraph(cl,
    "Your Threat Intelligence Engineer posting is about turning intelligence into action — getting in front of "
    "threats before they materialize, rather than passively consuming feeds. That's the same principle that's "
    "driven my detection engineering work for the last eight years: threat intel is only valuable when it changes "
    "what you detect and how fast you catch it."
)
dg.add_cover_paragraph(cl,
    "At Forescout, I used CTI directly from Vedere Labs, our in-house threat research team, during daily alert "
    "triage and false-positive analysis — validating whether an alert reflected real adversary activity, then "
    "feeding that research back into detection logic rather than treating it as a one-off fix. That same "
    "intel-to-detection loop shaped the 2,300+ detection rules I built at Trend Micro/Cysiv, mapped to most of "
    "the MITRE ATT&CK matrix across a nine-platform detection-as-code framework I architected from scratch."
)
dg.add_cover_paragraph(cl,
    "I bring strong Python automation skills — production tooling for alert enrichment, triage, and GenAI-assisted "
    "detection-rule conversion — plus deep, hands-on Elasticsearch experience across three employers, including "
    "building an entire ES-based security data platform from the ground up at DOE/NNSA. I'd welcome the chance to "
    "bring that same intelligence-driven detection mindset to GitLab's threat intelligence program."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("GitLab Senior Threat Intelligence Engineer package built.")
