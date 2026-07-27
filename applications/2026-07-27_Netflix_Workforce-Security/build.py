import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
import docgen as dg

OUT = os.path.dirname(__file__)
NAME = "Kyle Main"
CONTACT = "Dallas/Ft. Worth Area  |  469-545-3791  |  main.kyle87@gmail.com"

# ---------------- Resume ----------------
doc = dg.new_document()
dg.add_name_header(doc, NAME, CONTACT)
dg.add_title_line(doc, "Senior Security Engineer — Vulnerability & Detection Analytics")

dg.add_summary(doc,
    "Senior security engineer and data scientist with 10+ years bringing a data-engineering and analytics lens "
    "to security risk: ingesting vulnerability scan data (Tenable) alongside 220+ other log sources, building "
    "detection/analytics content on top of it, and evaluating environments and security controls for real-world "
    "exposure. Deep GenAI/LLM automation experience well beyond scripting."
)

dg.add_section_heading(doc, "Core Skills")
dg.add_skills_line(doc, "Vulnerability & Risk Analytics",
    "Tenable (vulnerability-scan data ingestion and analytics/detection content built on top of it), "
    "vulnerability analysis and environment exposure evaluation, security-control evaluation across many "
    "vendors (CrowdStrike, SentinelOne, Splunk, ELK, Sentinel, Defender, Google SecOps, Sumo Logic, XSIAM, Devo)")
dg.add_skills_line(doc, "GenAI-Powered Security Automation",
    "Prompt engineering for false-positive triage and detection-content generation; GenAI-driven SIEM API "
    "orchestration; reusable GenAI \"skills\" for cross-platform rule conversion")
dg.add_skills_line(doc, "Detection Engineering & Data Science",
    "2,300+ MITRE ATT&CK detection rules, UEBA, time-series anomaly detection, clustering, Python, SQL, PySpark")
dg.add_skills_line(doc, "Cloud & Platforms", "AWS, GCP, Azure, Docker, GitLab CI/CD")

dg.add_section_heading(doc, "Professional Experience")

dg.add_job_header(doc, "Senior Security Engineer", "Shorepoint", "Oct 2023 – Present")
dg.add_bullet(doc, "Treasury SOC (TSSOC), Threat & Research team — current project: build and maintain the "
                   "Splunk detection and alerting content the SOC runs incident response against.")
dg.add_bullet(doc, "DOE/NNSA Security Data Integration (prior project, completed): built a new security data "
                   "platform ingesting CrowdStrike, Suricata, and Zeek into Elasticsearch, including data-quality "
                   "monitoring and alerting used to catch degraded or blind-spot data sources — and the UEBA "
                   "detection layer built on top of it.")
dg.add_bullet(doc, "CISA CDM at DOE (prior project, completed): data ingestion and data-quality work across "
                   "Elasticsearch and Splunk.")

dg.add_job_header(doc, "Senior Threat Detection Engineer & Data Scientist", "Forescout", "Aug 2022 – Oct 2023")
dg.add_bullet(doc, "Senior member of the detection engineering/data science team building signature, behavioral, "
                   "statistical, time-series, and ML-based detection content against cloud-scale customer data.")

dg.add_job_header(doc, "Threat Detection Engineer & Data Scientist", "Trend Micro / Cysiv", "Sep 2018 – Aug 2022")
dg.add_bullet(doc, "Ingested Tenable vulnerability-scan data alongside 220+ other log sources into a central "
                   "platform and built analytics/detection content directly on top of it.")
dg.add_bullet(doc, "Performed vulnerability analysis and environment exposure evaluation as part of ongoing "
                   "detection engineering work.")
dg.add_bullet(doc, "Evaluated security tooling and controls from a wide range of vendors while building a "
                   "detection-as-code orchestration layer across nine SIEM/EDR platforms via native APIs, run "
                   "through a full GitLab CI/CD pipeline.")
dg.add_bullet(doc, "Built GenAI-powered tooling for security automation: prompt engineering for false-positive "
                   "triage, automated detection-rule generation, and cross-platform rule conversion.")
dg.add_bullet(doc, "Created and managed 2,300+ detection rules covering most of the MITRE ATT&CK matrix.")

dg.add_job_header(doc, "Security Data Scientist", "Experian", "Jan 2015 – Jan 2018")
dg.add_bullet(doc, "Built DNS-based detection and mitigation for malware infections; analyzed large-scale security "
                   "log data to surface anomalous behavior.")

dg.add_section_heading(doc, "Education & Certifications")
dg.add_plain_line(doc, "M.S. Physics — University of North Texas (2013)   |   B.S. Physics — Ball State University (2011)", size=9.5)
dg.add_plain_line(doc, "Splunk User Certification  ·  Splunk for Analytics and Data Science  ·  Johns Hopkins (Coursera): "
                       "R Programming, The Data Scientist's Toolbox", size=9.5)

dg.save(doc, os.path.join(OUT, "resume.docx"))

# ---------------- Cover Letter ----------------
cl = dg.new_document()
dg.add_name_header(cl, NAME, CONTACT)
dg.add_cover_date(cl, "July 27, 2026")
dg.add_cover_paragraph(cl, "Workforce Security Hiring Team\nNetflix")
dg.add_cover_paragraph(cl,
    "Vulnerability management done well is a data problem before it's a policy problem — prioritizing "
    "thousands of findings against real risk takes the same analytics discipline I've spent my career building "
    "for detection engineering.")
dg.add_cover_paragraph(cl,
    "At Trend Micro/Cysiv, I ingested Tenable vulnerability-scan data alongside 220+ other log sources into a "
    "central platform and built analytics/detection content directly on top of it — the same kind of work "
    "needed to apply threat intelligence toward prioritizing endpoint vulnerability remediation. I also "
    "evaluated security controls and tooling from a wide range of vendors while building a detection-as-code "
    "orchestration layer across nine SIEM/EDR platforms via their native APIs.")
dg.add_cover_paragraph(cl,
    "Beyond the data side, I've built real production GenAI tooling for security teams — prompt engineering for "
    "false-positive triage, automated detection-rule generation, and cross-platform rule conversion — well past "
    "the GenAI-assisted scripting bar this role calls for. I currently own the detection/analytics layer for a "
    "live SOC (Treasury), having previously built a from-scratch security data platform for DOE/NNSA.")
dg.add_cover_paragraph(cl,
    "I'll be direct about where I'm not a 1:1 match: I haven't administered an MDM platform like Intune (only "
    "used one as an end user), I don't have hands-on host-hardening experience, and I've never owned a patch "
    "management process end-to-end. What I'd bring instead is the data and analytics engineering discipline "
    "that a real Patch and Vulnerability Management strategy depends on, and I'd expect to ramp quickly on the "
    "endpoint-specific tooling.")
dg.add_cover_paragraph(cl, "I'd welcome the chance to talk through how that combination fits the Workforce Security team's roadmap.")
dg.add_cover_paragraph(cl, "Kyle Main", after=0)

dg.save(cl, os.path.join(OUT, "cover_letter.docx"))
print("Netflix package built.")
