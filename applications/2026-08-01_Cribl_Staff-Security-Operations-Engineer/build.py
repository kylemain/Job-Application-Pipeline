import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Staff Security Operations & Detection Engineer")

dg.add_summary(doc,
    "Detection and security operations engineer with 12 years designing detection logic, leading incident "
    "investigations, and running the data pipelines security tooling depends on — including hands-on experience "
    "building and managing Cribl pipelines directly. Built a Python-based detection-as-code framework spanning "
    "nine SIEM/EDR platforms with 2,300+ MITRE ATT&CK-mapped rules, and currently supports live SOC incident "
    "response for a Treasury threat & research team."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Cribl",
    "Hands-on experience creating and managing Cribl pipelines for security/observability data routing — direct, "
    "real-world experience with Cribl's own product, not just adjacent data-engineering work")
dg.add_skills_line(doc, "Multi-SIEM Detection-as-Code & Orchestration",
    "Built and maintained detection-rule orchestration across nine platforms via native APIs — Microsoft Sentinel, "
    "Microsoft Defender, Google SecOps (Chronicle), Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, "
    "Devo, plus prior ArcSight — including API token/role/permission management, multithreaded parallel rule "
    "deployment, full GitLab CI/CD, automated pipeline tests, and staged/safe rollout with tracked coverage and "
    "false-positive metrics")
dg.add_skills_line(doc, "Detection Engineering & MITRE ATT&CK",
    "Created and managed 2,300+ individual detection rules covering most of the MITRE ATT&CK matrix; signature, "
    "statistical, behavioral, and ML-based detection content; Splunk SPL; continuous tuning to reduce false "
    "positives")
dg.add_skills_line(doc, "Incident Response & Threat Intelligence",
    "Leads day-to-day detection/alerting content a live SOC (Treasury) runs incident investigations against; "
    "built a UEBA detection layer from raw log ingestion (CrowdStrike, Suricata, Zeek) through detection at "
    "DOE/NNSA; integrates CTI (indicators, TTPs, actor/campaign context) directly into detection tuning and alert "
    "enrichment, sourced from commercial feeds, OSINT, and in-house research (Vedere Labs)")
dg.add_skills_line(doc, "Cloud, Identity & Scripting",
    "AWS, GCP, Azure (Sentinel/Defender API orchestration); IAM policy/role implementation on AWS and GCP; API "
    "token, role, and permission management across nine SIEM platforms; Python; Docker")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — own the detection and alerting content "
                   "(Splunk saved searches) the SOC runs day-to-day incident investigations against, mapped to "
                   "MITRE ATT&CK TTPs.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (completed): built a new Elasticsearch-based security "
                   "data platform ingesting CrowdStrike, Suricata, and Zeek, plus the detection/analytics layer "
                   "on top — custom dashboards, data transforms, UEBA detection content, data-quality alerting.")
dg.add_bullet(doc, "CISA CDM at DOE (completed): data ingestion and quality work across a combined Elasticsearch "
                   "and Splunk environment.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data; "
                   "integrated Vedere Labs threat intel into detection tuning and alert enrichment.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Built and maintained a next-gen cloud-based SIEM's rules engine — created and managed 2,300+ "
                   "detection rules covering most of the MITRE ATT&CK matrix, delivered through a production "
                   "GitLab CI/CD pipeline with automated tests and staged rollout.")
dg.add_bullet(doc, "Built detection-as-code orchestration across nine SIEM/EDR platforms — including CrowdStrike "
                   "and SentinelOne — via native APIs, with multithreaded parallel deployment and formal "
                   "coverage/false-positive-rate tracking.")
dg.add_bullet(doc, "Data engineering for 220+ log sources feeding SIEM detection content; built a Common "
                   "Information Model standardizing field names/types across all parsed data.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections on the network; analyzed "
                   "large-scale security log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 1, 2026")
dg.add_cover_paragraph(cl, "Information Security Team\nCribl")
dg.add_cover_paragraph(cl,
    "I've built and managed Cribl pipelines directly — hands-on, real experience with the exact product your "
    "security stack runs on, not just adjacent data-engineering work. Combined with 12 years of detection "
    "engineering and SOC incident response, I'd bring both a user's fluency with Cribl and the security "
    "operations depth this Staff role needs."
)
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I built a next-gen SIEM's rules engine from the ground up, creating and managing "
    "2,300+ detection rules covering most of the MITRE ATT&CK matrix, then extended that into a Python-based "
    "detection-as-code framework orchestrating rule deployment across nine SIEM and EDR platforms — Microsoft "
    "Sentinel, Microsoft Defender, Google SecOps, Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, "
    "and Devo — via native APIs, with multithreaded parallel deployment, full GitLab CI/CD, automated testing, "
    "and staged rollout tracked against coverage and false-positive metrics. I've also integrated threat "
    "intelligence directly into that detection logic, using indicators and TTPs from commercial feeds, OSINT, "
    "and in-house research to tune rules and enrich alerts for faster triage."
)
dg.add_cover_paragraph(cl,
    "More recently, at DOE/NNSA I built a security data platform from scratch — ingesting CrowdStrike, Suricata, "
    "and Zeek into Elasticsearch and layering a UEBA detection capability, dashboards, and data-quality "
    "monitoring on top — and I currently lead the detection and alerting content a live Treasury SOC runs its "
    "incident investigations against as part of its Threat & Research team. That combination of building the "
    "data pipeline, writing the detection logic, and supporting the incident response that follows is exactly "
    "the loop this role owns."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how this background fits the Staff Security Operations Engineer "
    "role."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Cribl Staff Security Operations Engineer package built.")
