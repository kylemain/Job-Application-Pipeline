import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Machine Learning Engineer — Applied ML & GenAI Security")

dg.add_summary(doc,
    "12 years building production ML systems and security detection content — clustering, time-series "
    "anomaly detection, and precision/false-positive-tuned models deployed against massive-scale data — "
    "plus hands-on experience putting GenAI/LLM tooling directly into live security workflows: prompt "
    "engineering for security triage, LLM-driven orchestration of SIEM APIs, and reusable GenAI-powered "
    "tooling built for other engineers. Full ML lifecycle ownership: problem definition, data pipelines/EDA "
    "at scale (PySpark/GCP Dataproc), model development (PyTorch/scikit-learn), production deployment, and "
    "continuous precision/recall tuning fed by real production outcomes."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "GenAI/LLM for Security",
    "Prompt engineering for security triage and detection-content generation; GenAI-driven orchestration of "
    "SIEM APIs across 9 platforms; reusable GenAI-powered tooling built for other engineers (e.g., automated "
    "cross-SIEM detection-rule conversion) — real production LLM-into-workflow experience")
dg.add_skills_line(doc, "ML & Applied Data Science",
    "Python, SQL, pandas, scikit-learn, NumPy, SciPy, PyTorch, clustering/unsupervised ML, time-series "
    "anomaly detection, R")
dg.add_skills_line(doc, "Data Pipelines & EDA at Scale",
    "PySpark / SparkSQL, GCP Dataproc, Zeppelin notebooks, BigQuery, Apache Beam / GCP Dataflow, large-scale "
    "dataset construction across 220+ ingested sources")
dg.add_skills_line(doc, "Model Evaluation & Production Rigor",
    "Precision/recall and false-positive/false-negative analysis at production scale; formally tracked "
    "detection-quality metrics; staged/safe rollout before full production deployment; rollback paths")
dg.add_skills_line(doc, "Engineering & Platform",
    "Git, Docker, GitLab CI/CD (detection-as-code with automated testing), Kubernetes-orchestrated platform "
    "experience, Elasticsearch (queries, transforms, native detection rules, API)")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Built production GenAI tooling for security automation: prompt engineering for "
                   "false-positive triage, automated detection-content generation, and reusable "
                   "GenAI-powered \"skills\" that convert detection rules across SIEM syntaxes for other "
                   "engineers.")
dg.add_bullet(doc, "Currently own detection/alerting analytics (Splunk saved searches) for Treasury's SOC, "
                   "translating false-positive/false-negative investigation findings directly into refined "
                   "detection logic (TSSOC, current project).")
dg.add_bullet(doc, "Built an entirely new Elasticsearch-based security data platform from scratch for DOE/NNSA "
                   "— including a UEBA detection layer on custom data transforms modeling behavioral baselines "
                   "from CrowdStrike, Suricata, and Zeek telemetry (completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "statistical, behavioral, time-series, and ML-based detection content against massive-scale "
                   "customer data on a cloud-based big-data platform.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built ML-based detection content clustering devices on the network by behavioral features "
                   "(unsupervised learning), and designed time-series anomaly detection models for entity "
                   "behaviors — process chains, parent/child process patterns, authentication volume/geography "
                   "— as part of 2,300+ detection rules covering the MITRE ATT&CK matrix.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc via PySpark/SparkSQL to validate new "
                   "detection signal candidates before productionizing; owned data engineering for 220+ "
                   "ingested log sources feeding the detection pipeline.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security datasets to build custom models and algorithms identifying "
                   "emerging threats — DNS-based malware detection/mitigation and anomalous-behavior discovery "
                   "in log data.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 1, 2026")
dg.add_cover_paragraph(cl, "GenAI Security Team\nReddit")
dg.add_cover_paragraph(cl,
    "Reddit's GenAI Security team is building the layer that verifies identity, permissions, and intent "
    "across AI workflows — I've spent the last several years on the adjacent half of that same problem, "
    "putting GenAI directly into production security workflows and, for over a decade before that, building "
    "the ML systems that separate malicious behavior from normal behavior at scale."
)
dg.add_cover_paragraph(cl,
    "I've built production GenAI tooling for security teams directly: prompt engineering for detection triage "
    "and automated rule generation, LLM-driven orchestration of SIEM APIs across nine platforms, and reusable "
    "GenAI-powered tooling that converts detection logic across SIEM syntaxes for other engineers. That's "
    "hands-on experience shipping GenAI into live, production-facing security workflows — the same rigor "
    "around reliability, false positives, and operational trust that guardrail and semantic-classification "
    "models need."
)
dg.add_cover_paragraph(cl,
    "On the ML side, I've owned detection models end-to-end — clustering devices on the network by behavioral "
    "features with unsupervised learning, and designing time-series anomaly detection models against "
    "authentication and process-chain behaviors — as part of a rule set covering 2,300+ detection use cases "
    "across the MITRE ATT&CK matrix. I ran the same efficacy loop this role calls for: exploratory data "
    "analysis at scale (PySpark/SparkSQL on GCP Dataproc) to validate new signal candidates, model development "
    "in PyTorch and scikit-learn, and continuous precision/recall and false-positive tuning fed by real "
    "production outcomes, with staged rollout before full deployment."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that combination — production GenAI tooling plus full-lifecycle "
    "ML ownership in adversarial, high-stakes environments — applies to securing Reddit's GenAI traffic."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Reddit package built.")
