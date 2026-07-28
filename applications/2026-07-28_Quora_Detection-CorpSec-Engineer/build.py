import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection Engineer & Security Data Scientist")

dg.add_summary(doc,
    "Detection engineer with 10+ years building and maintaining SIEM platforms, writing detection content, "
    "and investigating security incidents from raw log data through to root cause. Production-grade Python "
    "engineer with hands-on experience across nine SIEM/EDR platforms including CrowdStrike, plus deep AWS/GCP "
    "cloud security background."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "SIEM & Detection Engineering",
    "Building and maintaining SIEM platforms (Splunk, ELK/Elasticsearch); detection rule/alert writing — "
    "signature, statistical, behavioral, ML-based; CrowdStrike, SentinelOne, Microsoft Sentinel/Defender, "
    "Google SecOps, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight; MITRE ATT&CK coverage")
dg.add_skills_line(doc, "Security Investigations",
    "DNS-based malware detection and mitigation; anomalous-behavior log analysis; entity behavior time-series "
    "anomaly detection (auth attempts, process chains); data-quality/health monitoring and alerting")
dg.add_skills_line(doc, "Engineering & Automation", "Python (production-grade, reviewed and shipped alongside "
    "detection-as-code CI/CD pipelines in GitLab); GenAI-powered security automation for triage and detection "
    "generation")
dg.add_skills_line(doc, "Cloud & Data Science", "AWS, GCP, Azure; clustering/unsupervised ML (device/behavior "
    "clustering), Docker for reproducible detection-testing environments")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — own the detection and alerting content "
                   "(Splunk saved searches) the SOC runs day-to-day incident response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new security data platform ingesting "
                   "CrowdStrike, Suricata, and Zeek into Elasticsearch, plus the detection/analytics layer on "
                   "top — dashboards, data transforms, UEBA content, data-quality alerting.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and quality work across a combined Elasticsearch "
                   "and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built and maintained a next-gen cloud-based SIEM's rules engine — created and managed 2,300+ "
                   "detection rules covering most of the MITRE ATT&CK matrix, delivered through a production "
                   "GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Built detection-as-code orchestration across nine SIEM/EDR platforms — including "
                   "CrowdStrike and SentinelOne — via native APIs, plus GenAI-powered tooling for false-positive "
                   "triage and cross-SIEM rule conversion.")
dg.add_bullet(doc, "Investigated anomalous entity behavior at scale: authentication-attempt anomalies by "
                   "country/volume, parent/child process chains, and Outlook process-chain analysis.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections on the network; analyzed "
                   "large-scale security log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Security Clearances: Top Secret (current, Treasury) · DOE Q Clearance · Public Trust (DOE)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 28, 2026")
dg.add_cover_paragraph(cl, "Security Team\nQuora")
dg.add_cover_paragraph(cl,
    "A small, high-ownership security team that builds where commercial tools don't fit is exactly the kind "
    "of environment I've thrived in — building SIEM detection content and investigating incidents end to end, "
    "not just running someone else's playbook."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built and maintained a cloud-based SIEM's rules engine from the ground up, "
    "creating and managing 2,300+ detection rules covering most of the MITRE ATT&CK matrix, all delivered "
    "through a production Python codebase and GitLab CI/CD pipeline reviewed and shipped alongside other "
    "engineers. I also investigated anomalous entity behavior at scale — authentication anomalies, process-"
    "chain analysis — the same log-review-to-timeline-reconstruction work central to this role's incident "
    "investigations."
)
dg.add_cover_paragraph(cl,
    "Earlier at Experian, I built DNS-based detection and mitigation for malware infections directly, and "
    "currently at Shorepoint I own the detection content a live SOC runs incident response against. I've also "
    "built GenAI-powered tooling to automate security workflows — triage and detection generation — which maps "
    "directly onto the AI-leverage approach your team is taking."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that SIEM-building and investigation background fits Quora's "
    "security team."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Quora package built.")
