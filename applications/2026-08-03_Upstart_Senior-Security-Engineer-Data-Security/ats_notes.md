# ATS Coverage & Fit Notes — Upstart, Senior Security Engineer, Data Security

## Salary check
Posted band: **$164,800 – $228,400 USD (Remote - US).**
Midpoint ≈ $196,600 — clears Kyle's $170,000+ floor comfortably. Anchor negotiation to the top third
(~$213,900–$228,400) once fit is confirmed.

## Fit score
Already screened at 5/10 before this build was requested (per the calling instructions) — this note does not
re-run that screen, just gives an honest keyword/gap breakdown for Kyle's awareness.

## Keyword coverage summary

**Direct matches:**
- **Identity & Access Management (IAM)** — confirmed via hands-on Cloud IAM policy/role implementation in both
  AWS and GCP.
- **Least-privilege principles, applied at scale** — confirmed via the multi-SIEM orchestration framework's
  creation and governance of API tokens, roles, and permissions across 10+ platforms (Microsoft Sentinel,
  Microsoft Defender, Google SecOps/Chronicle, Splunk, CrowdStrike, SentinelOne, Sumo Logic, Palo Alto XSIAM,
  Devo, ArcSight) — real, hands-on access-scoping work at the API level.
- **0-to-1 build-out of new security capability** — confirmed via building DOE/NNSA's entire Security Data
  Integration platform from scratch (ingestion, detection layer, dashboards, data-quality monitoring), and via
  being a very early hire who built the rules engine/data infrastructure for a cloud SIEM startup.
- **Software engineering discipline applied to security tooling** — confirmed via the GitLab CI/CD pipeline for
  detection-as-code with automated unit/integration tests, tracked rule-quality metrics, and staged/safe
  production rollout.
- **Cross-functional stakeholder collaboration** — confirmed pattern via multi-team engagements (DOE, DOE/NNSA,
  Treasury SOC) working across security, data, and analytics stakeholders, though not the exact Engineering/
  Analytics/Product/Legal/Risk/HR stakeholder set named in this JD.
- **Data engineering across diverse, high-volume sources** — confirmed via 220+ ingested log source pipeline
  ownership, Common Information Model / schema standardization work, and large-scale cloud data processing
  (GCP Dataproc/Dataflow/Apache Beam).

**Adjacent/transferable (framed honestly, not oversold):**
- **"Architect and build software solutions (APIs, services, and internal tools)"** — Kyle's SIEM orchestration
  work involved building per-platform API *adapters* that call out to and manage access on other platforms'
  APIs (token/role/permission creation and governance), which is real, hands-on API-level identity/access work.
  It is not the same thing as owning production-grade internal APIs/services as a primary software-engineering
  deliverable (e.g., a DLP scanning service or a data-classification API that other teams call). The resume and
  cover letter frame this honestly as access-governance-at-the-API-level, not as "built and shipped an internal
  API product."
- **"Diverse data domains (analytics, reporting, business operations, or people data)"** — Kyle's data-pipeline
  experience is deep but domain-concentrated in security/telemetry data (SIEM logs, threat intel, detection
  content), not analytics/reporting/HR/business-ops data specifically. The schema-standardization and pipeline
  skills transfer conceptually; the specific data domains do not have confirmed evidence in the master doc.

**Real gaps (not claimed anywhere in the resume or cover letter):**
- **No confirmed DLP (Data Loss Prevention) or DSPM (Data Security Posture Management) initiative ownership.**
  This is the JD's single biggest named requirement ("experience owning or leading a Data Security, DLP, or
  DSPM initiative") and there is no direct match in the master reference — Kyle's access-governance and data
  pipeline work is real and adjacent, but he has not owned a DLP/DSPM program specifically.
- **No confirmed experience with the named preferred tooling** — BigID, Concentric AI, Varonis, Cyera, or
  similar data-classification/posture-management platforms. Not claimed.
- **No confirmed SOC 1, SOC 2, or SOX compliance framework experience.** Not claimed anywhere.
- **Production API/service ownership as a primary software-engineering deliverable is a partial gap.** See the
  adjacent/transferable note above — Kyle has real API-level engineering experience (orchestration adapters,
  token/permission management) but this JD's ask reads as building net-new internal API products/services as
  a core deliverable, which is a step beyond what's confirmed in the master doc. Not overstated in the
  materials.
- **No confirmed data classification / data tagging pipeline experience** (distinct from the schema-
  standardization work he has done). Not claimed.

**Bottom line for Kyle:** the resume and cover letter lead with the two strongest honest connective threads —
Cloud IAM + API-level least-privilege access governance across a dozen-plus platforms, and deep data-pipeline
engineering (220+ sources, schema standardization, large-scale cloud processing) — and do not claim DLP/DSPM
platform ownership, the named vendor tools, SOC1/SOC2/SOX, or production API/service ownership at the scope
this JD implies. If this reaches an interview, expect direct technical probing on DLP/DSPM program ownership
and on what "building production APIs/services" means in Kyle's background specifically — be ready to frame
the orchestration-adapter work honestly as API-level access engineering rather than a DLP/DSPM platform build.

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, contact info in the document body (not header/footer) — passes the formatting
rules in `references/ats-optimization.md`.
