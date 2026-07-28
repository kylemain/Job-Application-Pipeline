# Master Reference — Kyle Main

> Source of truth for every job application. Claude reads this file in full before doing any work in the job-application-pipeline skill. Nothing here should need to be re-explained per application.

## Contact
Kyle Main | Dallas/Ft. Worth Area | 469-545-3791 | main.kyle87@gmail.com
Home address (for application forms, not shown to employers/not on resume): 5829 Humber Ln, Aubrey, TX 76227
GitHub: https://github.com/kylemain (use for application forms with a dedicated GitHub/portfolio field)

## Voluntary EEO / Self-Identification (for application forms only — never put any of this on a resume or cover letter)
- Gender: Male
- Race/ethnicity: Caucasian/White, not Hispanic or Latino
- Veteran status: Not a veteran
- Disability status: No disability
- Work authorization: Does not require visa sponsorship, authorized to work in the US

## Target Positioning
Senior Cybersecurity Detection Engineer & Data Scientist — with a secondary, equally valid lane as a **Data Engineer** (security-adjacent experience transfers cleanly to non-security data engineering roles).

## Roles Currently Targeting
- Detection Engineering / Threat Hunting
- Security Data Science / ML for Security
- Security Engineering Management / Lead roles
- Data Engineering (general, non-security orgs) — transferable via pipeline-building experience

## Salary
- **Target floor: $170,000+.** Flag any posting whose disclosed band tops out below this, or whose midpoint is meaningfully below it, before doing any other work on the application.
- Anchor negotiation language to the top third of the posted band once a fit is confirmed.

## Fit / Screening Rules (apply BEFORE building anything)
- **Remote only.** Kyle is only interested in fully remote roles. Flag and deprioritize any posting that requires on-site, hybrid, or relocation — even if everything else about the role is a strong match. State this clearly in the fit assessment rather than building materials for an in-office/hybrid role by default.
- **No federal government contracting roles.** Kyle is no longer interested in this space — too slow/restrictive. Flag and deprioritize any posting that is primarily a federal contracting role (agency SOC support via a contractor, cleared federal work, etc.), even if technically a strong skills match. Note this clearly in the fit assessment rather than silently building a resume for it.
- No security clearance requirement is a plus signal, not a hard requirement — but a *cleared, on-site, agency-embedded* role should be flagged as likely a poor culture/pace fit.
- No confidentiality masking needed anywhere — Kyle has no NDAs or IP restrictions from past employers. All employer names, agency names (DOE, CISA, NNSA, Treasury), and project names can be referenced freely in resumes and cover letters.

## Formatting Rules
- One-page resume by default (senior IC/lead roles — density matters more than exhaustive history; older/less relevant roles get compressed).
- Reverse chronological.
- Lead the skills section with whatever's most relevant to the specific JD (reorder per application — don't just copy the master list top to bottom).
- Cover letter: one page. Sharp opening → 1-2 proof-point paragraphs tied directly to JD requirements → one-line close. Do not call out skill/experience gaps in the cover letter — keep it entirely proof-point/strengths-focused. (Gaps can still be noted honestly in ats_notes.md for Kyle's own awareness — just not surfaced to the employer in the letter itself.)

---

## Full Work History

### Senior Cybersecurity Engineer — Shorepoint
**October 2023 – Present**
**Location (for application forms): Remote — worked from home in the Dallas/Ft. Worth area.**
Shorepoint is a cybersecurity consulting company supporting US federal government agencies. Note: Kyle is moving away from wanting more federal contracting work, but this experience is real and can be referenced.

Three sequential projects under this role. As of 2026-07-27, only TSSOC is Kyle's current/active project — CDM and NNSA/SDI have both ended. Use past tense for CDM and NNSA/SDI in resumes and cover letters; present tense only for TSSOC.

**1. CISA CDM (Continuous Diagnostics and Mitigation) at DOE — COMPLETED**
Supported data ingestion and data quality efforts within an Elasticsearch and Splunk environment.

**2. Security Data Integration (SDI) — DOE NNSA — COMPLETED**
Built an entirely new system for ingesting security data (CrowdStrike, Suricata, Zeek) into a central Elasticsearch platform and built the analytics/detection layer on top of it. Specifics:
- Custom dashboards
- Data transforms
- UEBA (User and Entity Behavior Analytics) detection content built on top of the transform outputs
- Data quality monitoring content and alerting

**3. Treasury SOC (TSSOC) — CURRENT project, Threat & Research (T&R) team**
Analytically supports Treasury's SOC for security incidents/cases. Creates and manages analytics (saved searches) in Splunk that serve as the SOC's detection and alerting content.

### Senior Threat Detection Engineer and Data Scientist — Forescout
**August 2022 – October 2023**
**Location (for application forms): Remote — worked from home in the Dallas/Ft. Worth area.**
Cysiv was acquired by Forescout in August 2022; this is a continuation of the Cysiv role below. Senior member of the data science and threat detection engineering team creating content to detect cyber threats in massive customer data — cloud-based big data tools, signature/behavioral/statistical/time-series/ML-based detection rules.

### Threat Detection Engineer and Data Scientist — Trend Micro/Cysiv
**September 2018 – August 2022**
**Location (for application forms): On-site — Irving, TX (Dallas/Ft. Worth metroplex).**
Cysiv started as an internal Trend Micro team project, spun out as its own company in 2020. Very early hire — built out the rules engine, detection content, and data engineering for the startup.
- Data engineering/pipelining for 220+ unique log data sources
- Built detection content in a next-gen cloud-based SIEM
- Created/managed 2,300+ individual detection rules covering most of the MITRE ATT&CK Matrix
- 50+ data filters

**Detailed project history (pull specific bullets per JD):**
- *Detection rule development:* signature-based, statistical-based, behavioral, aggregation/threshold, and ML rules (clustering devices on the network by feature)
- *Time-series anomaly detection of entity behaviors:* Outlook process chains; child/parent process combinations and chains; authentication behaviors (auth attempts by country over time, anomalous volume/attempt detection)
- *Exploratory Data Analysis at scale:* GCP Dataproc compute clusters, Zeppelin notebooks, home-grown reusable analysis toolkit, Spark jobs to load data from buckets, PySpark/SparkSQL for analysis
- *Data engineering:* 50+ Logstash filters for parsing/normalization; deployed Elasticsearch Beats for log collection; built a Common Information Model (CIM) — a data dictionary standardizing field names/types across all parsed data; assisted building "Loggify," a homegrown log parsing/filtering tool that replaced Logstash; connector/collector health monitoring and troubleshooting; fetched large volumes of historical cold-storage data for customers using a homegrown Apache Beam program run via GCP Dataflow

### Security Data Scientist — Experian
**January 2015 – January 2018**
**Location (for application forms): On-site — Allen, TX (Dallas/Ft. Worth metroplex).**
Provided analytical support/guidance to Information Security teams. Analyzed large datasets to develop custom models/algorithms supporting identification and handling of emerging threats.
- DNS-based detection and mitigation of malware infections on a network
- Security log data analysis for discovery of anomalous behavior

---

## Complete Skills Inventory

### Core Detection Engineering / SIEM (on resume)
- ELK Stack (Elasticsearch, Logstash, Kibana, Beats)
- Splunk
- MITRE ATT&CK
- Security detection content development (signature, statistical, behavioral, ML-based)
- Cloud/distributed big data: PySpark, Dataproc, BigQuery, Dataflow
- Cloud security: AWS, GCP, Azure
- Version control: Git

### Multi-SIEM Detection-as-Code & Orchestration (NOT on current resume — significant differentiator, surface prominently for detection engineering / security leadership roles)
- Built rule/content orchestration across many SIEM platforms via their native APIs: **Microsoft Sentinel, Microsoft Defender, Google SecOps (Chronicle), Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM, Devo**, plus prior experience with **ArcSight**
- Developed reusable per-technology adapters containing all interaction methods for each SIEM's API — not just rule management, but listing alerts, tables, schemas, and other platform objects
- Full CI/CD pipeline implementation for detection-as-code, run in **GitLab**
- This is essentially building an internal detection-management platform/abstraction layer across heterogeneous SIEM vendors — a strong signal for detection engineering leadership, security platform engineering, or MSSP/MDR-style roles

### GenAI / LLM Applications for Security (NOT on current resume — differentiator, especially for security-AI hybrid roles)
- Prompt engineering for security use cases: analyzing security data, identifying false positives, generating new detection content/rules
- Using GenAI to interact with SIEM APIs for detection-content orchestration across many customers and SIEM platforms
- Developed reusable GenAI-powered "skills" for detection engineers to automate repetitive tasks (e.g., converting detection rules from one SIEM's rule syntax to another's)

### Containers/Orchestration (NOT on current resume — comfortable user level)
- Docker: managed containers and images, built reusable custom images
- Used containers to test detection content against real log data (reproducible detection-testing environments)
- Level: comfortable, hands-on user — not claiming deep Kubernetes architecture experience unless a specific role requires probing further

### IaC / DevOps (NOT on current resume)
- GitLab CI/CD as the backbone for detection-as-code pipelines described above
- (No deep Terraform/CloudFormation claims — CI/CD via GitLab is the well-evidenced piece; don't overstate IaC beyond this unless Kyle confirms more)

### Vulnerability Management / Endpoint Security (NOT on current resume — confirmed 2026-07-27, limited scope)
- Tenable: hands-on user of the tool, and has ingested Tenable vulnerability scan logs into a SIEM/analytics platform and built analytics/detection content on top of that data (this is the differentiated angle — vulnerability *data engineering/analytics*, not vulnerability scanner administration)
- Vulnerability analysis: has evaluated environments/systems to determine vulnerability exposure
- Security control evaluation: has evaluated security controls/products from many vendors, but has NOT done formal risk-based control right-sizing/prioritization frameworks
- Microsoft Intune: used only as an end-user/customer of a managed device — has NOT administered or configured Intune/MDM policy
- Confirmed gaps (do not claim): no host-hardening experience (CIS benchmarks/baseline config design for Mac/Windows/Linux); has never owned a patch management process/strategy end-to-end

### Data Science / ML
- Python, SQL, advanced mathematics
- Pandas, scikit-learn, NumPy, SciPy, PyTorch
- Clustering/unsupervised ML (device clustering on network behavior)
- Time-series anomaly detection
- R (via Johns Hopkins Coursera specialization)

### Data Engineering (transferable outside security)
- Built data pipelines ingesting logs from 220+ sources into SIEM/Elasticsearch across multiple employers
- Apache Beam / GCP Dataflow for historical/cold-storage data retrieval
- Common Information Model / data dictionary design and standardization
- This experience is directly relevant to general data engineering roles outside cybersecurity — position it that way when the JD is a non-security data eng role

## Education
- M.S. Physics — University of North Texas, Dec 2013 (Optics/Photonics; Numerical Data Analysis & Modeling; Organic/Inorganic Materials — FRET mechanism; Applied Physics). Graduate Assistant Tuition Scholarship, Competitive Tuition Waiver.
- B.S. Physics — Ball State University, May 2011. Minors: Mathematics, Astrophysics. Thesis: "Luminescence Properties and a Whispering Gallery Mode Microlaser in AlN:Ti." SPS Physics Honor Society, Dean's List.

## Certifications
- Splunk User Certification — Splunk Education, June 2017
- Splunk for Analytics and Data Science — Splunk Education, Jan 2017
- R Programming — Johns Hopkins via Coursera, Aug 2015
- The Data Scientist's Toolbox — Johns Hopkins via Coursera, Aug 2015
- (In progress, unconfirmed on resume) A Cloud Guru's Elastic Certified Engineer exam prep course

No certifications currently in active progress beyond what's listed.

## Security Clearances
Include this on resumes in the Education/Certifications area (or its own "Security Clearances" line) — strong signal for federal/security-adjacent roles.
- **Top Secret** — current, sponsored by Treasury (active, tied to the TSSOC engagement)
- **DOE Q Clearance** — held (DOE)
- **Public Trust** — held, sponsored by DOE

## Memberships
Data Science and Machine Learning Community · American Institute of Physics (AIP) · Optical Society of America (OSA) · IEEE Student Member, Photonics Society subgroup

---

## Notes for Claude
- When a JD calls for skills in the "NOT on current resume" categories above, it's fair game to surface them — Kyle has confirmed real hands-on experience, not aspirational skills.
- Always ask before inventing any new skill/experience not captured in this document — do not infer skills from adjacency (e.g., don't assume Kubernetes architecture experience just because Docker is confirmed).
- Update this file whenever Kyle confirms a new skill, certification, role change, or constraint — this document should stay current so it never needs to be re-explained.
