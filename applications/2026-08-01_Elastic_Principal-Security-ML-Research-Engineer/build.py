import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Data Scientist & Detection Engineer — Elasticsearch-Native ML Threat Detection")

dg.add_summary(doc,
    "12 years of security engineering experience, including 8+ years building Elasticsearch-native detection "
    "and analytics platforms and ML-based threat detection content — from an ES/Kibana-based next-gen SIEM at "
    "an early-stage startup to a from-scratch DOE/NNSA security data platform with a full UEBA layer on ES "
    "transforms. Deep clustering, time-series anomaly detection, and false-positive-reduction ML work, plus "
    "hands-on GenAI/LLM production tooling for security automation."
)

dg.add_section_heading(doc, "Elasticsearch & Elastic Security Depth")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration: built an entirely new Elasticsearch-based security "
                   "platform ingesting CrowdStrike, Suricata, and Zeek — including a UEBA detection layer built "
                   "on ES transforms, custom Kibana dashboards, and native ES data-quality alerting.")
dg.add_bullet(doc, "Trend Micro/Cysiv next-gen SIEM: wrote and tuned Elasticsearch Query DSL and native ES "
                   "detection rules directly against production indexes as core detection content; built 50+ "
                   "Logstash filters and deployed multiple Elastic Beats variants for log collection into ES.")
dg.add_bullet(doc, "CISA CDM at DOE: data ingestion and data-quality engineering across a combined "
                   "Elasticsearch/Splunk environment supporting a federal SOC.")
dg.add_plain_line(doc, "Full ES lifecycle across three employers: ES API, ES transforms, Query DSL, native "
                       "detection rules/alerting, Beats collection, and Kibana dashboarding — not just log "
                       "shipping.", size=9.5, italic=True)

dg.add_section_heading(doc, "ML & Security Data Science")
dg.add_skills_line(doc, "Detection & Anomaly Modeling",
    "Clustering/unsupervised ML for device behavior classification; time-series anomaly detection for entity "
    "behaviors (auth volume/geography, process-chain deviations); signature, statistical, behavioral, and "
    "ML-based detection rule development with formally tracked false-positive rates and staged rollout")
dg.add_skills_line(doc, "ML Frameworks & Languages", "Python, pandas, scikit-learn, NumPy, SciPy, PyTorch, SQL, R")
dg.add_skills_line(doc, "GenAI/LLM for Security",
    "Prompt engineering for detection triage and rule generation; GenAI-driven orchestration of SIEM APIs "
    "across 9 platforms; GenAI-powered cross-SIEM rule-conversion tooling for other engineers — hands-on "
    "LLM-API-into-production experience")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team: own the detection/alerting content (Splunk "
                   "saved searches) driving live SOC incident response. Previously built DOE/NNSA's "
                   "Elasticsearch security platform (above) and supported CISA CDM data-quality work at DOE.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the data science/detection engineering team building signature, "
                   "behavioral, statistical, time-series, and ML-based detection content against cloud-scale "
                   "customer data; incorporated Vedere Labs threat intelligence into detection tuning.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Early hire building the ES/Kibana-based next-gen SIEM's rules engine and detection content "
                   "— 2,300+ rules across most of the MITRE ATT&CK matrix; data engineering for 220+ log "
                   "sources; GCP Dataproc/PySpark exploratory data analysis at scale.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections; analyzed large-scale "
                   "security log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013), Numerical Data Analysis & Modeling, "
                       "Applied Physics   |   B.S. Physics — Ball State University (2011), Minors: Mathematics, "
                       "Astrophysics", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins "
                       "(Coursera): R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 1, 2026")
dg.add_cover_paragraph(cl, "Threat Research and Detection Engineering Team\nElastic")
dg.add_cover_paragraph(cl,
    "Elasticsearch has been the core detection and analytics platform across nearly my entire career — not a "
    "peripheral tool, but the system I've built from the ground up. At DOE/NNSA I built an entirely new "
    "Elasticsearch-based security data platform from scratch, including its full UEBA detection layer; at "
    "Trend Micro/Cysiv I wrote and tuned Elasticsearch Query DSL and native detection rules as core content for "
    "an ES/Kibana-based next-gen SIEM; and at DOE I supported data ingestion and data-quality work inside a "
    "combined Elasticsearch/Splunk environment. Few candidates bring that kind of direct, cross-employer, "
    "full-lifecycle Elasticsearch depth to a Principal Security ML Research Engineer role."
)
dg.add_cover_paragraph(cl,
    "Beyond Elasticsearch, my work has centered on ML-based threat detection: clustering devices on the "
    "network by behavioral features, time-series anomaly detection across authentication and process-chain "
    "behaviors, and building signature, statistical, behavioral, and ML detection rules with formally tracked "
    "false-positive rates and staged rollout before full production deployment. At Trend Micro/Cysiv, this work "
    "scaled to 2,300+ detection rules across most of the MITRE ATT&CK matrix, engineered to catch real threats "
    "while minimizing false positives for analysts downstream."
)
dg.add_cover_paragraph(cl,
    "I've also put LLM APIs into production for security use cases directly — prompt engineering for detection "
    "triage and rule generation, GenAI-driven orchestration of SIEM APIs across nine platforms, and "
    "GenAI-powered tooling that converts detection rules between SIEM syntaxes for other engineers. That "
    "combination of deep Elasticsearch expertise, ML detection engineering, and hands-on production LLM "
    "integration maps directly to what this role is asking for."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how this background could contribute to Elastic Security's threat "
    "research roadmap."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Elastic package built.")
