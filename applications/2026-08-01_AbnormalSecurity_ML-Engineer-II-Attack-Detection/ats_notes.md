# ATS Coverage & Fit Notes — Abnormal Security, Machine Learning Engineer II (Attack Detection)

## Salary check
Posted band: **$160,700 – $231,000 USD base.**
Kyle's floor is $170,000+. **The bottom of this band ($160,700) is below floor.** The midpoint (~$195,850) and
top third (~$207,767–$231,000) clear the floor comfortably, so this isn't a hard disqualifier — but it's worth
flagging plainly: a low-ball offer near the bottom of the posted range would miss Kyle's floor. If pursued,
anchor negotiation language to the top third of the band ($207,767+), consistent with Kyle's standing rule.

## Fit score: 6/10

**Why not higher — real considerations, not glossed over:**
- **Level mismatch.** This is titled "Engineer II" and the JD explicitly says work is done "with senior
  engineer guidance" — language that signals a mid-level IC role. Kyle is senior/staff-level with 12 years of
  total professional experience (8+ years specifically in hands-on ML/detection engineering roles) and has
  been operating with significant autonomy (built entire detection platforms from scratch, e.g., DOE/NNSA
  SDI). This isn't disqualifying — Kyle could still be a strong technical fit and the comp band tops out well
  above senior-level pay — but there's a real chance the interview loop or leveling conversation surfaces this
  mismatch. Worth going in aware of it rather than surprised by it.
- **Domain gap: email security specifically.** Kyle's detection/ML work spans network, endpoint, and
  authentication telemetry (CrowdStrike, Suricata, Zeek, Elasticsearch/Splunk-based SIEM data) — not email
  content or message-level signals. The JD's core mission (distinguishing safe emails from attacks) is a
  different data domain than anything in Kyle's confirmed history. The *behavioral modeling methodology*
  transfers directly (baselining entity/communication patterns, building discriminative signals, combining
  them into a detection system) but the specific domain — email/message content and metadata — is new. Framed
  as adjacent/transferable in the resume and cover letter, not claimed as direct domain experience.
- **JD's "must have" ML domain list is a partial miss.** The JD's required 3+ years is scoped to "text
  understanding, entity recognition, NLP, computer vision, recommendation systems, or search." Kyle's ML work
  (device clustering, time-series anomaly detection on behavioral/auth telemetry) doesn't fall cleanly into
  any of those named categories — it's applied/unsupervised ML on security telemetry, not NLP/text/CV/search.
  This is a real gap against the letter of the requirement, softened by the fact that the requirement is
  clearly written with flexibility in mind (six very different named domains lumped into one bullet suggests
  the team cares more about "has shipped production ML" than the specific sub-domain).

**Why still worth pursuing (6, not lower):**
- Strong overlap on the *general* ML must-haves: Python/pandas/scikit-learn/PyTorch fluency (confirmed),
  1+ years of production-grade training/eval pipelines (confirmed via detection-as-code CI/CD work), SQL +
  pandas + Spark for data/metric pipelines (confirmed — PySpark/SparkSQL EDA at scale on GCP Dataproc), and a
  demonstrated debugging/efficacy-improvement loop (FN/FP analysis → feature engineering → rule tuning) that
  maps almost one-to-one onto this team's stated workflow.
- Remote (Remote - USA) — matches Kyle's remote-only requirement, no flag needed.
- Not federal contracting, not on the exclusion list.
- BS requirement: Kyle holds a B.S. Physics (Ball State) plus M.S. Physics (UNT) — satisfies "BS in Computer
  Science, Applied Sciences, Information Systems, or related engineering field" via the physics/quantitative
  science route.

## Keyword coverage summary
**Direct matches (JD must-haves):**
- Python, numpy, pandas, scikit-learn, PyTorch — confirmed, called out explicitly in Core Skills
- SQL + pandas + Spark for data/metric pipelines — confirmed (PySpark/SparkSQL, GCP Dataproc)
- Production-level pipelines for training/evaluation — confirmed via detection-as-code CI/CD (GitLab),
  automated testing, rule-quality metrics tracking, staged rollout
- Systematic debugging of data/system issues in ML/heuristics models — confirmed via FN/FP dataset analysis
  and detection tuning workflow described throughout resume/cover letter
- Feature engineering + combining rules/models into a detection system — confirmed, strong direct match
- Effective SWE skills (structured, tested, readable code) — confirmed, called out in Core Skills

**Adjacent/transferable (named honestly, not oversold):**
- "Text understanding, NLP, entity recognition, computer vision, recommendation systems, or search" — no
  direct match in any of these six categories. Framed instead as applied ML on behavioral/security telemetry
  (clustering, time-series anomaly detection), which is methodologically similar (discriminative feature
  engineering, baseline modeling, precision/recall tuning) but not the same data domain.
- Email/message-specific detection domain — no direct experience; positioned as directly transferable
  behavioral-detection methodology from network/endpoint/auth telemetry, not glossed over as equivalent.
- TensorFlow — not confirmed in master doc (PyTorch is confirmed); not claimed on resume.

**Gaps (not claimed anywhere):**
- No confirmed TensorFlow experience (PyTorch only).
- No confirmed email security / anti-phishing / message-content ML experience.

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, contact info in document body — passes the formatting rules in
`references/ats-optimization.md`.

## Recommendation
Worth applying given strong general-ML and pipeline-discipline overlap and a clean remote/non-federal fit,
but go in with eyes open on two fronts: (1) the leveling conversation may surface a mismatch between Kyle's
actual seniority and the "Engineer II ... with senior engineer guidance" framing, and (2) if an offer comes in
near the bottom of the posted band, it will miss Kyle's $170K floor — anchor hard to the top third if it gets
to that stage.

## Correction (2026-08-02)
The resume summary and cover letter originally said "10+ years" / "a decade," understating Kyle's real total.
Per the master reference's "Total Years of Experience" note, Kyle's total professional experience is 12 years
(since Jan 2015, Experian — Experian's job title was literally "Security Data Scientist," so the data-scientist
framing in this summary undercounted his own title history). Corrected resume summary to "12 years of
experience... including 8+ years of hands-on ML detection engineering" (8+ years is accurate for the specific
clustering/time-series ML work, which started at Trend Micro/Cysiv in 2018); cover letter's "a decade" changed
to "12 years." The level-mismatch note above was also updated to state the real total. Experian was already
present in this resume's work history — no content was missing, this was a numbers/wording fix only. Rebuilt
and re-confirmed single-page.
