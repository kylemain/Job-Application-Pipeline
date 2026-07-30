# ATS Optimization Notes — Fluidstack, Senior Detection Engineer

## Keyword coverage

**Direct matches (required/core JD asks):**
- "Own the detection engineering program end to end: threat modeling, detection design, deployment, tuning, and retirement, with coverage mapped to MITRE ATT&CK" → 2,300+ detection rules created/managed covering most of the MITRE ATT&CK matrix (Trend Micro/Cysiv)
- "Build detection-as-code pipelines so every rule is version-controlled, tested, and peer-reviewed before it ships, and false-positive rates are measured, not guessed" → nine-SIEM Python orchestration framework, full GitLab CI/CD, automated unit/integration tests, staged rollout, tracked coverage/precision/false-positive-rate metrics
- "Drive SIEM and EDR pipeline health: log source onboarding, normalization, and alert quality" → 220+ log source data engineering, 50+ Logstash filters, Elasticsearch Beats, Common Information Model, connector/collector health monitoring
- "Lead triage and response for the alerts you build, and close out incidents with root-cause writeups" → Treasury SOC (TSSOC) detection/alerting content ownership, team-lead directing sprint priorities and technical direction
- "Build automation that removes manual triage steps" → production Python triage/enrichment automation, production GenAI tooling for false-positive triage
- 5+ years detection engineering/threat hunting → Kyle has ~8 years (Sep 2018–present)
- Deep hands-on SIEM/EDR (Splunk, Elastic, CrowdStrike) → direct match via multi-SIEM orchestration including Splunk, Elasticsearch, CrowdStrike
- Strong scripting/automation (Python, SQL) and detection-as-code workflow → direct match
- "Knows the difference between a noisy rule and a broken one" → explicitly tunes on measured false-positive rate rather than instinct

**Adjacent/transferable (framed honestly):**
- "Run threat hunts against real adversary behavior... convert findings into repeatable detections" — Kyle's real experience is threat-intel-informed detection tuning and CTI-based alert validation during triage/false-positive analysis (confirmed in master reference), not formal proactive threat-hunting campaigns. Framed in the resume/cover letter as "threat intel-informed investigation" — a genuine bridge skill, not overstated as formal threat hunting.

**Gaps (honest, not papered over):**
- No confirmed experience with formal, structured proactive threat hunting (as distinct from threat-intel-informed tuning/triage).
- Bonus: "experience securing physical infrastructure or OT/data center environments, purple team experience, or contributions to open-source detection content (Sigma)" — none of these confirmed in master reference, not claimed.
- Salary: band is $147K–$182K. Bottom is below Kyle's $170K floor; only the top ~20% of the band clears it. Kyle has explicitly decided to proceed anyway, expecting to land near the top of the range given his experience level — this is his call, not a screening pass on the band itself.
- This req is nearly a downleveled duplicate of the Staff Detection Engineer req at the same company (already applied to 2026-07-30), same team, very similar JD language, lower pay band. Worth being aware of in case Fluidstack's ATS or recruiter flags the two applications as redundant.

## Formatting check
- Single-column, no tables-for-layout, standard section headings (Core Skills / Professional Experience / Education & Certifications), contact info in document body, standard Arial font. One page confirmed via PDF render (resume_page-1.jpg, cover_page-1.jpg). Passes ATS parseability rules per references/ats-optimization.md.
