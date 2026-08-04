import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Security Product Researcher — Network Detection Platforms (Zeek/Suricata) & GenAI Security Tooling")

dg.add_summary(doc,
    "Security engineer and data scientist with 12 years of experience building detection and analytics platforms "
    "directly on Zeek and Suricata network telemetry, most recently designing a ground-up security data platform "
    "for DOE/NNSA from concept to deployment. Hands-on GenAI/LLM prompt engineering for security use cases — "
    "generating detection content, triaging false positives, and building reusable AI-powered tooling for "
    "detection engineers. Deep detection-content engineering background (signature, behavioral, statistical, and "
    "ML-based rules; 2,300+ rules across the MITRE ATT&CK matrix) with the rapid-prototyping, ship-it-to-prove-it "
    "instinct this role calls for."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Network Detection Platforms",
    "Zeek, Suricata, CrowdStrike telemetry ingestion and analysis; Elasticsearch full lifecycle — queries, "
    "transforms, Beats, native detection rules, API, Kibana dashboarding; OSI-layer network traffic analysis for "
    "protocol abuse and attack-pattern detection")
dg.add_skills_line(doc, "GenAI / LLM for Security",
    "Prompt engineering for security use cases — analyzing security data, identifying false positives, "
    "generating new detection content; using GenAI to interact with SIEM APIs for detection-content "
    "orchestration; built reusable GenAI-powered tooling for detection engineers (e.g., automated cross-SIEM "
    "rule-syntax conversion)")
dg.add_skills_line(doc, "Detection Content Engineering",
    "Signature, behavioral, statistical, and ML-based detection rules; MITRE ATT&CK coverage; threat intel "
    "integration into detection logic; multi-SIEM detection-as-code orchestration (Splunk, Microsoft Sentinel/"
    "Defender, Google SecOps, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo, ArcSight) via GitLab "
    "CI/CD with automated testing and staged rollout")
dg.add_skills_line(doc, "Data Science & Engineering",
    "Python, SQL, PySpark/GCP Dataproc/BigQuery/Dataflow; clustering and time-series anomaly detection; "
    "security operations, threat hunting, and SOC incident-response support (Splunk, Elastic)")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Designed and built an entirely new security data platform for DOE/NNSA from scratch — "
                   "ingesting CrowdStrike, Suricata, and Zeek network telemetry into a central Elasticsearch "
                   "environment and constructing the full analytics/detection layer on top of it: custom data "
                   "transforms, a UEBA detection layer, custom Kibana dashboards, and data-quality monitoring/"
                   "alerting content (DOE/NNSA Security Data Integration project, completed).")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics (Splunk saved searches) directly "
                   "supporting Treasury's Security Operations Center incident response and case work — real-time "
                   "threat hunting and SOC analytic-content ownership (Treasury SOC / TSSOC, current project).")
dg.add_bullet(doc, "Supported data ingestion and data-quality efforts within an Elasticsearch/Splunk environment "
                   "for DOE's Continuous Diagnostics and Mitigation (CDM) program (completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "behavioral, statistical, and ML-based detection content against massive-scale customer "
                   "network telemetry on a cloud-based big-data platform, with threat-intel integration to tune "
                   "rule logic and speed alert triage.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Very early hire who built the rules engine and detection content from scratch for a next-gen "
                   "cloud SIEM — created and managed 2,300+ individual detection rules covering most of the "
                   "MITRE ATT&CK matrix, backed by data engineering for 220+ ingested log sources and a Common "
                   "Information Model standardizing data across all of it.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Analyzed large-scale security log data to build custom detection models — DNS-based malware "
                   "detection/mitigation and anomalous-behavior discovery across the network.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "August 3, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nCorelight")
dg.add_cover_paragraph(cl,
    "Corelight's foundation on Zeek and Suricata caught my attention immediately — I've spent the last several "
    "years building detection and analytics platforms directly on that same network telemetry, and I'd welcome "
    "the chance to bring that background to a team defining what's next for network detection."
)
cl_body1 = (
    "At Shorepoint, I designed and built an entirely new security data platform for DOE/NNSA from the ground "
    "up: ingesting CrowdStrike, Suricata, and Zeek telemetry into a new Elasticsearch environment, then "
    "constructing the full analytics and detection layer on top of it — custom data transforms, a UEBA detection "
    "layer, custom dashboards, and data-quality monitoring and alerting. That project ran the full arc this role "
    "describes: proving out an idea, building it, and getting it into real use, with the same rapid-prototyping "
    "instinct Corelight is looking for."
)
dg.add_cover_paragraph(cl, cl_body1)
cl_body2 = (
    "I also bring hands-on GenAI/LLM experience applied specifically to security work: prompt engineering to "
    "analyze security data, identify false positives, and generate new detection content, plus using GenAI to "
    "interact directly with SIEM APIs for detection-content orchestration. I've built reusable GenAI-powered "
    "tooling for detection engineers — including automating the conversion of detection rules from one SIEM's "
    "rule syntax to another's — the kind of AI-for-both-software-and-security-work this role calls for."
)
dg.add_cover_paragraph(cl, cl_body2)
cl_body3 = (
    "That GenAI work sits on top of a deep detection-content engineering foundation: 2,300+ detection rules "
    "covering most of the MITRE ATT&CK matrix, a multi-SIEM detection-as-code pipeline orchestrating rule "
    "deployment across nine different platforms via their native APIs, and current work directly supporting "
    "Treasury's SOC through live incident response and threat hunting."
)
dg.add_cover_paragraph(cl, cl_body3)
dg.add_cover_paragraph(cl,
    "I'd welcome the opportunity to talk through how that background translates into Corelight's next generation "
    "of network security products."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Corelight Security Product Researcher package built.")
