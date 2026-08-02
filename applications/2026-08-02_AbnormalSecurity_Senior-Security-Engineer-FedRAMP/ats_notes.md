# ATS Coverage & Fit Notes — Abnormal Security, Senior Security Engineer, FedRAMP

## Salary check
Posted band: **$153,000 – $220,000 USD base.**
Kyle's floor is $170,000+. The bottom of this band ($153,000) is below floor; the midpoint (~$186,500) and top
third (~$197,667–$220,000) clear it comfortably. Anchor negotiation to the top third if it gets to that stage.

## Fit score: 7/10

**Why this scored higher than the typical borderline candidate:**
- **Clearances are the single strongest signal on the page for this specific req.** Kyle holds an active Top
  Secret clearance (sponsored by Treasury, tied to his current TSSOC engagement), a DOE Q Clearance, and a
  Public Trust (DOE) — all earned through real federal agency work, not adjacent private-sector exposure. A
  role built entirely around a FedRAMP/federal-compliance environment ("Abnormal Gov") will weight this
  extremely heavily; very few candidates outside the federal contracting space carry this combination.
- **Direct SecOps/incident-response overlap.** Kyle's current TSSOC role literally is SOC analytic/alerting
  content creation supporting a federal agency's (Treasury) incident response and case work — this is the
  "triage and respond to security incidents" and "manage logging and monitoring pipelines; tune SIEM ingestion
  and alerting" bullets almost verbatim, just for a different federal client (Treasury vs. Abnormal's own Gov
  environment).
- **Continuous-monitoring precedent.** The CISA CDM program at DOE is a federal continuous-diagnostics-and-
  mitigation initiative — conceptually the closest thing in Kyle's history to FedRAMP's ConMon (continuous
  monitoring) requirement, even though it's not FedRAMP itself.
- **Real CI/CD and access-management overlap.** Kyle's multi-SIEM detection-as-code pipeline (GitLab CI/CD,
  automated testing, staged/safe rollout, rule-quality metrics tracking) is genuine hands-on CI/CD pipeline
  ownership, and his API token/role/permission management across SIEM platforms plus Cloud IAM work in AWS/GCP
  covers the "govern access management" bullet directly, if at a smaller organizational scale than an
  enterprise-wide RBAC program.

**Real gaps, not glossed over:**
- **No confirmed NIST 800-53 experience specifically.** Kyle's federal work has been in ES/Splunk-based
  detection and data engineering, not formal control-framework implementation or continuous-monitoring
  documentation against NIST 800-53. Not claimed anywhere in the resume/cover letter.
- **No confirmed patch management or hardened-image ownership.** The master reference explicitly flags this as
  a confirmed gap ("has never owned a patch management process/strategy end-to-end") — not claimed.
- **No confirmed deep Infrastructure-as-Code (Terraform/CloudFormation) or Change Control Board review
  experience.** Kyle's CI/CD ownership is real but scoped to the detection-as-code pipeline itself, not
  general infra IaC or formal CCB process ownership. Framed honestly as CI/CD pipeline experience, not IaC/CCB
  experience.
- **No confirmed 3PAO audit support experience** (listed as "nice to have," not a must-have).
- **AWS depth is a partial gap.** Kyle's strongest cloud-native depth is GCP (Dataproc/Dataflow/serverless);
  AWS/GCP IAM policy work is confirmed but the JD's "proven delivery of AWS/SaaS security best practices" is a
  slightly stronger AWS-specific ask than what's confirmed in the master doc. Not overstated.

## Keyword coverage summary
**Direct matches:**
- Security operations engineering, incident response (Tier 1/2), SIEM pipeline/alerting tuning — confirmed via
  TSSOC and CISA CDM work
- CI/CD pipeline ownership — confirmed via GitLab detection-as-code pipeline
- Access management / RBAC / API token & role governance — confirmed via multi-SIEM orchestration framework
- Cloud IAM (AWS, GCP) — confirmed
- Federal / regulated cloud environment experience — confirmed directly (DOE, DOE/NNSA, Treasury)
- Active security clearances — confirmed (Top Secret, DOE Q, Public Trust), called out in its own section

**Adjacent/transferable (named honestly, not oversold):**
- NIST 800-53 / continuous monitoring — framed via the CDM program's conceptual overlap, not claimed as direct
  NIST 800-53 control experience
- Infrastructure-as-code / Change Control Board review — framed as CI/CD pipeline ownership, not general IaC

**Gaps (not claimed anywhere):**
- Patch management, hardened image pipelines, 3PAO audit support, formal NIST 800-53 control implementation

## Formatting / parseability
Single-column, standard section headings (Security Clearances called out as its own heading given how central
it is to this specific req), no tables/text boxes/icons, contact info in document body — passes the formatting
rules in `references/ats-optimization.md`.

## Recommendation
Built and worth submitting despite the federal-contracting-adjacent flag (Kyle confirmed he wants to proceed
given the unusually strong clearance/federal-experience match). Go in aware that the interview will likely
probe NIST 800-53 specifics and patch-management ownership directly — be ready to frame those honestly as
adjacent-but-not-direct experience rather than overclaiming in the room.
