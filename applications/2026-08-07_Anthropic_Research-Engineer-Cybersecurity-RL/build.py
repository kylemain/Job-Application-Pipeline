import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Detection & Response Engineer — GenAI for Defensive Security, Detection-as-Code")

dg.add_summary(doc,
    "Senior detection and response engineer with 12 years building the detection content and defensive tooling that "
    "protect real production environments, plus genuine hands-on experience applying generative AI directly to "
    "defensive security workflows. Built the detection rules engine from scratch at a next-gen cloud SIEM "
    "startup (Cysiv, spun out of Trend Micro, later acquired by Forescout), creating 2,300+ MITRE ATT&CK-covering rules. Currently "
    "support live incident/case response for a federal SOC. Applied GenAI directly to detection engineering — "
    "prompt-driven false-positive triage, new detection-content generation, and automated rule translation "
    "across SIEM syntaxes — the kind of AI-for-defensive-security work this role's mandate to safely advance "
    "model capability in secure coding and vulnerability remediation calls for."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Detection & Response",
    "2,300+ detection rules covering most of the MITRE ATT&CK matrix; current incident/case response for a "
    "federal SOC; formal detection-quality metrics (coverage, precision/false-positive rate) with staged/safe "
    "rollout before production")
dg.add_skills_line(doc, "GenAI / LLM Applied to Defensive Security",
    "Prompt engineering to analyze security data, identify false positives, and generate new detection content; "
    "GenAI-driven SIEM API orchestration across customers/platforms; built reusable GenAI-powered tooling that "
    "automates detection-rule translation between SIEM rule syntaxes — hands-on experience directing model "
    "output toward real defensive-security outcomes and validating it against analyst judgment before trusting it")
dg.add_skills_line(doc, "Multi-SIEM Detection-as-Code & Orchestration",
    "Rule/content orchestration via native APIs across nine SIEM platforms (Microsoft Sentinel, Microsoft "
    "Defender, Google SecOps, Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo); GitLab CI/CD "
    "with automated tests and multithreaded parallel deployment")
dg.add_skills_line(doc, "Vulnerability & Data Engineering",
    "Ingested Tenable vulnerability scan data into a SIEM platform and built analytics/detection content on top "
    "of it; 220+ log source data engineering; Common Information Model design")
dg.add_skills_line(doc, "Cloud Security Platform Engineering",
    "Built a cyber-defense platform from the ground up on Elasticsearch — CrowdStrike (EDR), Suricata, and Zeek "
    "telemetry, UEBA detection layer, data-quality monitoring — for a DOE/NNSA cloud-adjacent security program")
dg.add_skills_line(doc, "Engineering", "Python, SQL, PyTorch/scikit-learn, Git, GitLab CI/CD, Docker")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Cybersecurity Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Currently create and manage detection/alerting analytics directly supporting a federal "
                   "SOC's live incident response and case work (Treasury SOC / TSSOC, current project).")
dg.add_bullet(doc, "Built an entirely new cyber-defense platform from the ground up — CrowdStrike (EDR), "
                   "Suricata, and Zeek telemetry into a central Elasticsearch environment — including a UEBA "
                   "detection layer and data-quality monitoring/alerting content (DOE/NNSA, completed).")

dg.add_job_header(doc, "Senior Threat Detection Engineer and Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of a data science and detection engineering team building signature, "
                   "behavioral, statistical, and ML-based detection content against massive-scale customer "
                   "telemetry, incorporating threat intel from Forescout's in-house Vedere Labs research team.")

dg.add_job_header(doc, "Threat Detection Engineer and Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Very early hire at a next-gen cloud SIEM startup — built the detection rules engine from "
                   "scratch and created/managed 2,300+ individual detection rules covering most of the MITRE "
                   "ATT&CK matrix, plus 50+ data filters, against 220+ ingested log sources.")
dg.add_bullet(doc, "Applied GenAI directly to detection engineering: prompt engineering for false-positive "
                   "identification and new rule generation, and reusable GenAI-powered tooling that automates "
                   "converting detection rules between SIEM rule syntaxes.")
dg.add_bullet(doc, "Ran exploratory data analysis at scale (GCP Dataproc, PySpark/SparkSQL) using clustering "
                   "and time-series anomaly detection to develop new detection content.")

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
dg.add_cover_date(cl, "August 7, 2026")
dg.add_cover_paragraph(cl, "Hiring Team\nAnthropic — Horizons, Cybersecurity RL")
dg.add_cover_paragraph(cl,
    "I'm a detection and response engineer who has spent 12 years building defensive security content, and for "
    "the last several years I've been applying generative AI directly to that work — which is exactly the "
    "intersection this role sits at. I'd like to bring that background to the Cybersecurity RL team."
)
dg.add_cover_paragraph(cl,
    "As a very early hire at Cysiv (a next-gen cloud SIEM startup that spun out of Trend Micro, later acquired by Forescout), "
    "I built the detection rules engine from scratch and created and managed 2,300+ individual detection rules "
    "covering most of the MITRE ATT&CK matrix. On top of that core detection-engineering work, I've built "
    "real, hands-on GenAI tooling for defensive security: prompt engineering to analyze security data and "
    "identify false positives, GenAI-driven orchestration of detection content across nine SIEM platforms, and "
    "reusable GenAI-powered tooling that automates translating detection rules between SIEM syntaxes. I "
    "currently support live incident and case response for a federal SOC, so I bring the applied "
    "defensive-work perspective this role is built around — someone who has lived inside detection and "
    "response and is now curious about how models can meaningfully augment that work."
)
dg.add_cover_paragraph(cl,
    "I've also built detection content directly on top of ingested vulnerability-scan data (Tenable), giving me "
    "real working familiarity with the secure-coding and vulnerability-remediation problem space this team is "
    "advancing model capability in — not just detection after the fact, but understanding where the underlying "
    "weaknesses come from."
)
dg.add_cover_paragraph(cl,
    "I'd welcome the chance to talk through how that domain expertise could support the Cybersecurity RL "
    "team's work advancing Claude's capabilities in secure coding and vulnerability remediation."
)
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Anthropic Research Engineer, Cybersecurity RL package built.")
