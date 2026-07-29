import sys, os
sys.path.insert(0, "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/_lib")
import docgen as dg

OUT = "/sessions/adoring-peaceful-noether/mnt/Job-Application-Pipeline/applications/2026-07-29_GoogleDeepMind_Agentic-Red-Team"
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer — Detection Engineering & GenAI Security Tooling")

dg.add_summary(doc,
    "Security engineer whose work sits at the defensive side of the same problem this role attacks from the "
    "offensive side: understanding adversary behavior deeply enough to build detection and automation against "
    "it. Built production GenAI/LLM tooling for security workflows, deep MITRE ATT&CK-based detection content "
    "covering thousands of adversary techniques, and a Python-based automation framework spanning nine security "
    "platforms — strong technical foundation for a red-team/adversarial-AI function, though hands-on exploit "
    "development against GenAI models is not part of the current track record."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "GenAI / LLM Applications for Security",
    "Production GenAI tooling for security workflows: prompt engineering for analyzing security data and "
    "generating detection content, using GenAI to orchestrate SIEM APIs across many platforms/customers, "
    "reusable GenAI-powered \"skills\" that convert detection rules between rule syntaxes")
dg.add_skills_line(doc, "Adversary Technique Depth (MITRE ATT&CK)",
    "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix — signature, "
    "statistical, behavioral, and ML-based detections built directly against real adversary TTPs, informed "
    "by hands-on threat-intel integration (Vedere Labs) rather than generic rule libraries")
dg.add_skills_line(doc, "Security Automation & Tooling (Python)",
    "Production-grade Python, not scripts: built a detection-as-code orchestration framework across nine "
    "SIEM/EDR platforms via native APIs, run through a full GitLab CI/CD pipeline with automated tests and "
    "staged rollout; comfortable building and maintaining security tooling end to end")
dg.add_skills_line(doc, "Anomaly & Behavioral Detection",
    "Time-series and behavioral anomaly detection on entity behavior (process chains, authentication patterns); "
    "unsupervised ML/clustering for device behavior classification; statistical and ML-based detection content "
    "development")
dg.add_skills_line(doc, "Cloud & Data Platforms",
    "Hands-on IAM in AWS and GCP; event-driven serverless enrichment on GCP; PySpark/GCP Dataproc for large-"
    "scale exploratory analysis; comfortable Docker/container user")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — team lead directing sprint priorities and "
                   "technical direction for detection and alerting content built against real adversary TTPs.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform from "
                   "scratch ingesting CrowdStrike, Suricata, and Zeek into Elasticsearch, plus a UEBA "
                   "(behavioral anomaly) detection layer on top.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, "
                   "statistical, behavioral, and ML-based detection content against massive customer telemetry.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Architected a Python-based detection-as-code orchestration framework across nine SIEM/EDR "
                   "platforms via native APIs — reusable per-technology adapters, multithreaded parallel "
                   "deployment, full GitLab CI/CD pipeline with automated tests and staged rollout.")
dg.add_bullet(doc, "Built production GenAI tooling for detection-rule generation and cross-platform rule "
                   "conversion; developed reusable GenAI-powered \"skills\" automating repetitive detection-"
                   "engineering tasks.")
dg.add_bullet(doc, "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix; "
                   "time-series anomaly detection on entity behavior (Outlook process chains, authentication "
                   "patterns) and unsupervised ML clustering for device behavior classification.")
dg.add_bullet(doc, "Data engineering for 220+ log sources feeding all detection content: Common Information "
                   "Model standardizing schema, 50+ Logstash filters, Apache Beam/GCP Dataflow for historical "
                   "retrieval.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections; analyzed large-scale "
                   "security log data to surface anomalous behavior using statistical/ML methods.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Security Clearances: Top Secret (current, Treasury) · DOE Q Clearance · Public Trust (DOE)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 29, 2026")
dg.add_cover_paragraph(cl, "DeepMind Security Hiring Team\nGoogle DeepMind")
dg.add_cover_paragraph(cl,
    "Closing the Agentic Launch Gap requires understanding adversary behavior well enough to anticipate it — "
    "that's the discipline I've built my career on, from the defensive side of the same problem."
)
dg.add_cover_paragraph(cl,
    "I've created and maintained 2,300+ detection rules covering most of the MITRE ATT&CK matrix, which means "
    "thinking in adversary TTPs every day: how an attacker chains techniques, what a novel technique looks like "
    "before it's been catalogued, and how to turn that understanding into something automated and repeatable. "
    "I've also shipped production GenAI tooling directly into security workflows — using LLMs to generate and "
    "convert detection content and to orchestrate SIEM APIs across nine different platforms — so I'm comfortable "
    "operating at the intersection of GenAI systems and security engineering, not just security engineering alone."
)
dg.add_cover_paragraph(cl,
    "The engineering muscle behind that work — a Python-based automation framework running through a full "
    "CI/CD pipeline with automated testing and staged rollout — is exactly the kind of infrastructure needed to "
    "turn one-off findings into durable, reusable guardrails."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination of deep adversary-technique fluency, GenAI "
    "tooling experience, and production automation engineering could translate to the Agentic Red Team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("DeepMind Agentic Red Team package built.")
