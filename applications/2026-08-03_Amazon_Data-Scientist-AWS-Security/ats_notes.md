# ATS Coverage & Fit Notes — Amazon, Data Scientist, AWS Security

## Salary check — FLAG
Posted band (confirmed on live posting): **$136,000 – $184,000 USD base** (location: USA, MD, Annapolis Junction).
Midpoint is **~$160,000** — meaningfully below Kyle's $170,000+ floor. Even the top of the band ($184,000)
only clears the floor by $14K, and that would require landing at the very top of the range. This is a real
salary concern, not a rounding issue. Flagging clearly per Kyle's standing rule, per the task instructions
(this posting was pre-screened at 7/10 and approved for building despite this) — Kyle should go in with eyes
open that a top-of-band outcome barely clears his floor, and a typical/mid-band outcome does not. If it
progresses, anchor negotiation hard to the top of the band and treat any offer below ~$175K as below-floor.

## Location / federal-contracting check — reviewed, NOT a federal-contracting concern
Location is confirmed as **Annapolis Junction, MD** (NSA/Fort Meade-adjacent, as flagged for review). The live
JD was read in full specifically to check this. Findings:
- No mention of a security clearance requirement anywhere in the posting.
- No mention of any government agency, cleared facility, or contract vehicle.
- The team's stated mission is protecting **Amazon's own AWS infrastructure and AWS customers** from security
  threats ("protect every AWS customer from security threats" using SageMaker/EMR) — this is Amazon's own
  product security data science team, not agency-embedded contractor work.
- The JD explicitly frames this as a normal corporate role: flexible hours, core business hours 10am–3pm EST,
  "it's not about clocking hours, it's about delivering results," standard on-call rotation (~1 week every 2
  months).
- **Conclusion: this is a normal Amazon corporate AWS Security data science role**, not cleared/agency-embedded
  contractor work. Annapolis Junction likely reflects where much of the existing team happens to sit (common
  in the DC/MD security talent market) rather than a signal of federal-contractor status. Proceeding with the
  build per the task's guidance was correct — no stop-and-flag warranted here.
- **Secondary flag (minor, not a stop condition):** the JD does not explicitly confirm the role is fully remote
  — it says the team is "distributed, though most of the team is located in Maryland and Virginia" and
  describes a flexible schedule rather than stating "remote eligible" outright. Worth confirming remote
  eligibility for Kyle's DFW location directly with the recruiter before/at the first screen, consistent with
  Kyle's remote-only standing preference.

## Fit score: 7/10 (per initial screen — not re-scored here; this document builds on that screen)

## Keyword coverage summary

**Direct matches:**
- 3+ years SQL/Python/statistical software — Kyle has 12 years, far exceeds minimum (Python, SQL, R all
  confirmed)
- 3+ years ML/statistical modeling and data analysis — confirmed via clustering, time-series anomaly detection,
  statistical/behavioral detection modeling across three employers
- Master's degree in STEM (basic qualification) — M.S. Physics, University of North Texas, directly satisfies
- ML concepts applied to reasoning/problem-solving — confirmed (unsupervised clustering, time-series anomaly
  models)
- Python as scripting language — confirmed
- Statistical analysis/data mining on large-scale security data — confirmed (EDA at scale via GCP
  Dataproc/PySpark/SparkSQL)
- Automated systems for real-time pattern recognition/risk assessment — confirmed (UEBA detection layer at
  DOE/NNSA, built directly on custom data transforms)
- Data pipelines/ETL for massive security datasets — confirmed (220+ log sources, Apache Beam/GCP Dataflow)
- Translating analytical findings into actionable security insights — confirmed (SOC detection/alerting
  analytics at Treasury)
- Applying quantitative analysis to business/security decisions — confirmed throughout

**Adjacent/transferable (named honestly, not oversold):**
- "Experience in a ML/data scientist role with a large technology company" — Kyle's roles have been at
  cybersecurity vendors (Trend Micro/Cysiv, Forescout), not a hyperscaler/big-tech company specifically. Framed
  as senior data-science/detection-engineering roles at established security companies, not claimed as
  big-tech-equivalent.
- "Expanding existing LLM agent pipelines" — Kyle's GenAI work is prompt engineering for security triage/rule
  generation and using GenAI to orchestrate SIEM APIs, which is real hands-on GenAI-for-security work but not
  confirmed as building/expanding a formal LLM *agent* framework specifically. Framed as adjacent groundwork,
  not an exact match.
- "Running experiments to assess potential risk of security responses" — closest confirmed analog is the
  rule-quality-metrics/staged-safe-rollout discipline in the multi-SIEM detection-as-code pipeline (measuring
  precision/false-positive rate before full production rollout), not a formal experimentation framework. Not
  overstated as identical.
- AWS specifically — Kyle has real AWS cloud security/IAM experience, but his deepest cloud-native *ML/big-data
  platform* experience (Dataproc, BigQuery, Dataflow, Zeppelin/PySpark) is on **GCP**, not AWS SageMaker/EMR
  specifically named in the JD. Resume and cover letter frame this honestly as equivalent big-data-processing
  experience "on a different hyperscale cloud" rather than claiming direct SageMaker/EMR hands-on time.

**Real gaps (not claimed anywhere in resume/cover letter):**
- No confirmed hands-on experience with **AWS SageMaker or EMR** specifically — the JD names these directly as
  the team's core tooling; Kyle's equivalent experience is GCP-based.
- No confirmed experience **defining/creating benchmarks for assessing GenAI model performance** — Kyle has
  applied GenAI to security workflows but hasn't built formal model-evaluation benchmarks.
- No Ph.D. (listed as preferred only, not required — Master's satisfies the basic qualification).
- No confirmed formal "post-mortem analysis for missed-signal identification" process, though false-positive
  analysis and root-cause work on noisy detection rules is closely adjacent.

## Formatting / parseability
Single-column, standard section headings (Data Science & Machine Learning; Security Detection Engineering &
Data Pipelines; Professional Experience; Education & Certifications), no tables/text boxes/icons, contact info
in document body, standard Arial font — passes the formatting rules in `references/ats-optimization.md`.

## Recommendation
Built per the pre-approved 7/10 fit screen. The salary midpoint (~$160K) sitting below Kyle's $170K floor is
the one real concern worth surfacing before he invests interview time — worth an early, direct conversation
with the recruiter about banding/level before going deep into the process. The Annapolis Junction location
checked out as Amazon's own corporate AWS Security team, not federal-contractor work, so no stop-and-flag
was warranted on that front. Confirm remote eligibility for Kyle's DFW location early given the JD's
non-explicit remote language.
