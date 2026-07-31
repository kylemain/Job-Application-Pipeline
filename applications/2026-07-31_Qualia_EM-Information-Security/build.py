import sys, os
sys.path.insert(0, "/sessions/gallant-zealous-gates/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/gallant-zealous-gates/mnt/Job-Application-Pipeline/applications/2026-07-31_Qualia_EM-Information-Security"
os.makedirs(OUT, exist_ok=True)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer — Detection Engineering, SecOps & AI-Assisted Automation")

dg.add_summary(doc,
    "Detection engineer and team lead with 8 years building and running detection/SIEM programs, directing sprint "
    "priorities for a live SOC's detection and alerting backlog, and shipping production automation — including "
    "GenAI-assisted triage and detection-rule tooling — that lets a small team cover more ground without growing "
    "headcount linearly. Comfortable moving between hands-on detection work, incident response, and cross-team "
    "risk communication."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection Engineering & SIEM/Log Monitoring",
    "Multi-SIEM detection-as-code framework across nine platforms (Splunk, Microsoft Sentinel/Defender, Google "
    "SecOps, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo) via native APIs; deep, cross-employer "
    "Elasticsearch/ELK experience (queries, transforms, Logstash, Beats, native ES detection rules, Kibana); "
    "created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix")
dg.add_skills_line(doc, "AI-Assisted Detection & Response Automation",
    "Production GenAI tooling for false-positive triage, detection-content generation, and cross-SIEM rule "
    "conversion; prompt engineering for security use cases; used GenAI to interact with SIEM APIs to orchestrate "
    "detection content across many customer environments in parallel — direct precedent for scaling a team's "
    "coverage through AI-assisted triage/investigation/response workflows rather than headcount growth")
dg.add_skills_line(doc, "Incident Response & Team Leadership",
    "Team lead directing sprint priorities for Treasury SOC's detection and alerting content backlog on the "
    "Threat & Research team; supports SOC incident investigation and false-positive analysis; built formal "
    "detection-quality metrics (coverage, precision/false-positive rate) and staged/safe-rollout practices before "
    "production deployment")
dg.add_skills_line(doc, "Cloud & Identity Security",
    "Hands-on IAM policy/role implementation in AWS and GCP; created and managed API tokens, roles, and "
    "permissions across nine SIEM platforms as part of a detection-orchestration framework; Microsoft Sentinel/"
    "Defender API orchestration on Azure")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead directing sprint priorities for the "
                   "detection and alerting content a live SOC's responders investigate against, balancing new "
                   "coverage work against incident-driven priorities.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new Elasticsearch-based security data "
                   "platform from scratch — ingestion, UEBA detection layer, Kibana dashboards, and data-quality "
                   "monitoring/alerting — a ground-up build owned end to end, not an inherited program.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building detection content "
                   "against massive customer telemetry; used threat intel from Vedere Labs during daily triage "
                   "and false-positive analysis to validate real adversary activity before escalating.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected a Python-based detection-as-code orchestration framework across nine SIEM/EDR "
                   "platforms via native APIs, with automated tests and staged rollout inside a full GitLab CI/CD "
                   "pipeline — including creating/managing API tokens, roles, and permissions across every platform.")
dg.add_bullet(doc, "Built production GenAI tooling for detection-rule generation, false-positive triage, and "
                   "cross-platform rule conversion — reusable automation that let a small detection team cover "
                   "more customer environments without proportional headcount growth.")
dg.add_bullet(doc, "Built the Elasticsearch-based data engineering layer for 220+ log sources (50+ Logstash "
                   "filters, multiple Beats deployments, a Common Information Model) and wrote detection rules "
                   "directly against ES indexes as core content in the team's next-gen ES/Kibana SIEM.")
dg.add_bullet(doc, "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix; "
                   "tracked detection-quality metrics (coverage, precision/false-positive rate) with staged "
                   "rollout before full production deployment.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Security Clearances: Top Secret (current, Treasury) · DOE Q Clearance · Public Trust (DOE)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 31, 2026")
dg.add_cover_paragraph(cl, "Information Security Hiring Team\nQualia")
dg.add_cover_paragraph(cl,
    "Home closings are among the highest-stakes, lowest-margin-for-error transactions most people ever make — "
    "which is exactly the kind of environment where detection work has to be both rigorous and fast. Your "
    "Information Security Engineering Manager posting describes a team mandate I've been living for the last two "
    "years: scale a security team's coverage through automation and AI rather than headcount alone, without "
    "losing the pragmatic, business-first judgment that keeps security from becoming a blocker."
)
dg.add_cover_paragraph(cl,
    "On Treasury's SOC, I direct sprint priorities for the detection and alerting content our responders "
    "investigate against — balancing new coverage work against incident-driven demands, the same operating "
    "rhythm your team runs day to day. At Trend Micro/Cysiv, I built production GenAI tooling that automated "
    "false-positive triage and detection-rule generation across a nine-platform detection-as-code framework, "
    "letting a small team cover far more ground than headcount alone would allow — directly the kind of "
    "AI-assisted triage-to-response workflow you're looking to make the default at Qualia."
)
dg.add_cover_paragraph(cl,
    "I also bring hands-on IAM implementation across AWS and GCP, deep Elasticsearch/SIEM detection-content "
    "experience, and a track record of shipping automation that changed how a team worked rather than just "
    "documenting the idea. I'd welcome the chance to bring that same automation-first, risk-based approach to "
    "Qualia's Information Security team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Qualia Engineering Manager, Information Security package built.")
