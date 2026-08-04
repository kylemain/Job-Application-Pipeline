# ATS Coverage & Fit Notes — Salesforce, Lead Machine Learning Engineer - Cyber Security (LMTS)

## Salary check
**Undisclosed.** The live posting includes no salary band — only a generic statement that US compensation
depends on location, level, and experience, with equity/benefits available. Cannot compare against Kyle's
$170,000+ floor until a number surfaces (recruiter screen or offer stage). Flag this to Kyle explicitly: don't
invest further time here without an early ask on the band, given the on-site/hybrid ask below.

## Location / remote flag — REAL DEVIATION FROM KYLE'S REMOTE-ONLY PREFERENCE
The posting title itself lists three specific on-site locations: **California – San Francisco, Washington –
Bellevue, California – Palo Alto.** No remote option is mentioned anywhere in the rendered JD body. This is a
genuine hybrid/on-site requirement, not a "hybrid header but remote-eligible body" situation — confirmed by
reading the full live JD text, not just the title. Kyle has said he's open to relocating for the right role, but
this is worth surfacing clearly before proceeding: it is a real deviation from his stated remote-only default,
and would mean relocating to one of three specific metro areas (all high cost-of-living relative to Dallas/Ft.
Worth).

## Title clarification — LMTS confirmed as an IC title
Confirmed on the live posting: "LMTS" = **Lead Member of Technical Staff**, and the page's own job-category
subheading reads "Lead member of technical staff - Machine Learning Engineering" under Job Category: Software
Engineering. This is an individual-contributor/technical-track title at Salesforce, not a people-management
title — so Kyle's documented gap ("no formal management title/headcount") is **not applicable** to this specific
req. The role does carry mentoring and force-multiplier expectations ("mentoring junior scientists and
engineers," "act as a force multiplier") but explicitly as an IC, not a manager.

## Fit score: 6/10 (screening already completed — this package reflects that result, not a re-screen)

## Keyword coverage summary (method per references/ats-optimization.md)

**Direct matches (confirmed in master doc, used in resume/cover letter as-is):**
- Anomaly detection — time-series anomaly detection (auth behavior, process-parent/child chains)
- Clustering / unsupervised ML — device/entity behavioral clustering, production UEBA detection layer
- Production ML/detection systems at scale — 2,300+ MITRE ATT&CK-mapped rules, DOE/NNSA UEBA build
- Python — confirmed, advanced
- PyTorch — confirmed
- Spark/PySpark — confirmed (PySpark, SparkSQL, GCP Dataproc)
- Docker / containerization — confirmed, comfortable hands-on user
- High autonomy on vague business problems — direct analog via DOE/NNSA SDI build-from-scratch
- Masters in a quantitative field (preferred) — M.S. Physics, direct match
- Explaining technical work across stakeholders — reasonable general claim given cross-team detection work,
  kept general in the cover letter rather than overclaimed with false specifics

**Adjacent/transferable (named honestly, not oversold with the JD's exact framing):**
- Kafka — "familiar with Kafka," worked in an environment that used it; not primary ownership — framed as
  "working familiarity," not deep streaming-architecture expertise
- Kubernetes — worked within a Kubernetes-orchestrated platform as a user; NOT cluster-admin or K8s architecture
  — resume explicitly says "operating within," not "managing," Kubernetes
- MLOps CI/CD, automated testing, model performance monitoring — Kyle's real, evidenced analog is the
  GitLab CI/CD detection-as-code pipeline (automated unit/integration tests, staged/safe rollout, tracked
  rule-quality metrics/precision/false-positive rate). This is genuine CI/CD + testing + monitoring discipline,
  but it's for detection *rules*, not trained ML *models* specifically — framed honestly as the closest existing
  analog, not as literal ML-model-CI/CD experience
- Feature engineering — implicit in the clustering/anomaly-detection feature work described, but "feature
  stores" specifically (the JD's exact ask) is not claimed
- Mentoring — team-lead/sprint-lead experience is confirmed; no formal mentoring program ownership documented,
  so not stated as a program claim
- ML governance / data security regulations — access-management and IAM work (SIEM API tokens/roles/permissions,
  AWS/GCP IAM) is real and adjacent, but not the same as formal ML governance policy authorship — not claimed
  as such

**Real gaps (honestly not claimed anywhere in resume or cover letter):**
- **Graph models / graph analytics** — no evidence in the master doc of graph-based detection modeling
  (the JD explicitly calls for "probabilistic modeling, graph analytics, supervised and unsupervised learning")
- **Snowflake** — not in Kyle's confirmed inventory at all
- **Flink** — confirmed only as "familiar/exposure," not ownership or architecture. Do not overstate; resume
  says "working familiarity... streaming," not "built/operated Flink pipelines"
- **Apache Airflow** — no mention anywhere in the master doc; not claimed
- **TensorFlow** — master doc confirms PyTorch/scikit-learn, not TensorFlow specifically; not claimed
- **Feature stores** (as a named system/discipline) — not confirmed
- **NLP expertise** (preferred) — not confirmed
- **Open-source contributions, conference presentations (Black Hat/DEF CON/BSides), offensive security/red
  teaming background, ML research-team collaboration, publications/patents** (all preferred, not required) —
  none confirmed in the master doc; none claimed

## Real gaps summary for Kyle (the ones that matter most for this specific req)
1. **Production MLOps CI/CD specifically for trained ML models** — Kyle has the adjacent, genuinely strong
   analog (detection-as-code CI/CD with testing and staged rollout), but it's not literally ML-model MLOps.
   Likely to come up directly in a technical interview; be ready to describe it as the closest real analog
   rather than claiming it's the same thing.
2. **Kubernetes at admin/architecture depth** — confirmed user-level exposure only.
3. **Snowflake, Kafka (ownership-level), Flink (ownership-level)** — Snowflake is a full gap; Kafka and Flink are
   exposure-only, not owned/architected. This trio is explicitly called out as required, hands-on stack
   knowledge in the JD ("Hands-on comfort with high-volume logs and proficiency with Spark/Pyspark, Snowflake,
   Flink and streaming services such as Apache Kafka") — this is the single biggest stack gap in the posting.
4. **Graph analytics / graph models** — a full gap, and one of the two named "unknown unknowns" detection
   techniques in the JD's "Your impact" section (the other, probabilistic modeling, overlaps reasonably with
   Kyle's statistical/behavioral detection work).

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, contact info in document body, standard fonts — passes the formatting rules in
`references/ats-optimization.md`. One page confirmed via visual QA (render to PDF + pdftoppm images).

## Recommendation
Package built as directed (fit screening already passed at 6/10 before this build started). Before Kyle invests
further time: (1) get the salary band early given the location trade-off, (2) go in clear-eyed that the
Snowflake/Kafka/Flink stack and graph-analytics gap are real and likely to surface in a technical screen, and
(3) confirm he's genuinely willing to relocate to SF, Bellevue, or Palo Alto — this is a real hybrid/on-site
role, not a remote-eligible one, despite Kyle's general remote-only preference.
