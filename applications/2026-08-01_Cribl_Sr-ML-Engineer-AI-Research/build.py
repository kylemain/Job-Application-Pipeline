import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Machine Learning Engineer — Applied AI & Security Data Science")

dg.add_summary(doc,
    "ML engineer and security data scientist with 12 years of experience (since 2015) training and evaluating "
    "ML models — clustering, time-series anomaly detection, and GenAI/LLM-powered automation — against "
    "security data at scale. Direct, hands-on experience creating and managing Cribl pipelines. Python/PyTorch/"
    "scikit-learn foundation, M.S. Physics (numerical modeling and data analysis)."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Cribl & Data Pipelines",
    "Hands-on experience creating and managing Cribl pipelines for security/observability data routing; "
    "broader pipeline engineering across 220+ log sources (Logstash, Elasticsearch Beats, Apache Beam/GCP Dataflow)")
dg.add_skills_line(doc, "GenAI / LLM Applications",
    "Prompt engineering for security use cases (false-positive triage, detection-content generation); "
    "GenAI-driven orchestration of SIEM APIs across 9 platforms; built reusable GenAI-powered \"skills\" "
    "automating detection-rule conversion between SIEM syntaxes")
dg.add_skills_line(doc, "ML & Data Science",
    "Python, PyTorch, scikit-learn, Pandas, NumPy, SciPy; trained/evaluated unsupervised clustering models "
    "(network device behavior); time-series anomaly-detection models (auth/process-chain behaviors); "
    "large-scale EDA via PySpark, GCP Dataproc, SparkSQL")
dg.add_skills_line(doc, "Platforms & Engineering",
    "Elasticsearch (queries, transforms, native detection rules, API), Kibana, Splunk; GitLab CI/CD pipeline "
    "with automated testing and staged rollout; Docker; AWS, GCP, Azure")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team (current): build and maintain Splunk-based "
                   "detection/analytics content the SOC runs incident response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new Elasticsearch-based security "
                   "data platform ingesting CrowdStrike, Suricata, and Zeek; built the UEBA detection layer on "
                   "ES transforms, plus dashboards and data-quality monitoring.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and quality engineering across a combined "
                   "Elasticsearch and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data-science team; built signature, behavioral, "
                   "statistical, time-series, and ML-based detection models against cloud-scale customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Trained and evaluated unsupervised ML models for network device clustering as part of a "
                   "next-gen SIEM's rules engine spanning 2,300+ detection rules across the MITRE ATT&CK matrix.")
dg.add_bullet(doc, "Built time-series anomaly-detection models for entity behavior — authentication attempts "
                   "by country/volume, parent/child process chains, Outlook process-chain analysis.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale on GCP Dataproc (PySpark/SparkSQL, Zeppelin "
                   "notebooks); built GenAI-powered tooling automating cross-SIEM detection-rule conversion "
                   "and false-positive triage — production LLM tooling, not a research exercise.")
dg.add_bullet(doc, "Data engineering: 220+ ingested log sources, 50+ Logstash filters, Common Information "
                   "Model (CIM) design, GCP Dataflow/Apache Beam for cold-storage retrieval.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation models for network malware infections; analyzed "
                   "large-scale security log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013, Numerical Data Analysis & Modeling)   |   "
                       "B.S. Physics — Ball State University (2011; Minors: Mathematics, Astrophysics)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins "
                       "(Coursera): R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 1, 2026")
dg.add_cover_paragraph(cl, "AI Research Team\nCribl")
dg.add_cover_paragraph(cl,
    "I've spent real, hands-on time creating and managing Cribl pipelines directly — not adjacent tooling, "
    "but Cribl's own observability/data-routing product, the exact system Cribl's AI/ML work is built to "
    "extend and orchestrate. That direct product fluency, paired with 12 years training and evaluating ML "
    "models against security data, is what draws me to this role."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I trained and evaluated unsupervised ML models for network device clustering and "
    "built time-series anomaly-detection models for entity behavior — production ML running against "
    "cloud-scale customer data on GCP Dataproc (PySpark/SparkSQL). I also built and shipped GenAI-powered "
    "tooling: prompt-engineered workflows that let detection engineers query SIEM APIs directly and convert "
    "detection rules between SIEM syntaxes automatically — reusable \"skills\" that turned language-model "
    "output into daily production tooling rather than a one-off demo."
)
dg.add_cover_paragraph(cl,
    "My M.S. in Physics gave me a strong numerical-modeling foundation that I've applied through clustering, "
    "time-series, and PyTorch/scikit-learn work across every security data platform I've touched since — most "
    "recently building the full ingestion-to-detection analytics layer, including Elasticsearch transforms and "
    "UEBA content, for a DOE/NNSA security data platform."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that Cribl-pipeline fluency and applied ML background could "
    "support Cribl's AI Research team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Cribl Sr ML Engineer, AI Research package built.")
