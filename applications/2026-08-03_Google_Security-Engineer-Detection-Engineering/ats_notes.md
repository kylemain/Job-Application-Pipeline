# ATS Coverage & Fit Notes — Google, Security Engineer, Enterprise Detection Engineering

## LOCATION FLAG — READ FIRST
**This role is ON-SITE in San Jose, CA — not remote.** The posting lists "San Jose, CA, USA" with no remote/hybrid
language anywhere in the JD body. This is a real deviation from Kyle's stated remote-only default preference.
Kyle has said he's open to relocating for the right role, and this posting already passed fit/salary screening
(7/10) with that understanding — but flagging it clearly here per his standing instruction: don't silently treat
an on-site req as remote. The cover letter proactively states Kyle is based in the Dallas/Ft. Worth area and
"ready to relocate to San Jose to do this work on-site," so this isn't sprung on the recruiter/hiring manager
after the fact.

## Salary check
Posted band: **$147,000 – $211,000 USD base** + 15% bonus target + equity + benefits.
Kyle's floor is $170,000+. Midpoint (~$179,000) clears the floor; top third (~$189,700–$211,000) clears it
comfortably. Anchor negotiation to the top third once fit is confirmed.

## Fit score: 7/10 (per initial screen — this build does not re-score)

## Keyword coverage summary

**Direct matches:**
- MITRE ATT&CK framework — confirmed directly (2,300+ rules covering most of the matrix at Trend Micro/Cysiv)
- Detection engineering (signature, statistical, behavioral, ML-based detection content) — confirmed, core of
  Kyle's career
- SOC / incident response experience — confirmed via current Treasury SOC (TSSOC) engagement
- Detection rule tuning for false-positive reduction — confirmed (formally tracks rule-quality metrics —
  coverage, precision/false-positive rate — with staged/safe rollout before production)
- Detection engineering pipeline automation / CI/CD — confirmed (GitLab CI/CD detection-as-code pipeline with
  automated unit/integration tests, multithreaded parallel deployment)
- Security engineering / computer & network security fundamentals — confirmed broadly across 12 years
- Coding experience in general-purpose languages — confirmed (Python, SQL)
- Endpoint telemetry exposure — confirmed via CrowdStrike (endpoint EDR) ingestion and detection-content
  development on top of it for the DOE/NNSA Security Data Integration platform
- Knowledge of AI/agentic systems — confirmed via GenAI-for-security work (prompt engineering for detection
  content/FP triage, GenAI-driven SIEM API orchestration, GenAI-powered rule-conversion tooling)

**Adjacent/transferable (named honestly, not oversold):**
- "Threat modeling methodologies" — Kyle's detection engineering work is inherently threat-informed (uses CTI/
  threat intel — including Forescout's Vedere Labs — to tune detection logic), but this is not the same as
  formal threat-modeling practice (e.g., STRIDE, attack-tree exercises). Framed in the resume/cover letter as
  detection-content design informed by threat intel, not as formal threat-modeling methodology ownership.
- "Security assessments or security design reviews" (a stated minimum-qualification bucket) — Kyle has evaluated
  security controls/products from many vendors (per master doc) but has not run formal security design review
  processes. Not directly claimed.
- Google Workspace/SaaS-surface detection specifically — Kyle's closest analog is Microsoft Sentinel/Defender
  API orchestration (a SaaS-platform detection-as-code target), not Google Workspace itself. Framed as
  multi-SIEM/multi-platform orchestration breadth, not direct Workspace experience.
- Resource-efficiency-driven detection tuning (the JD's specific GCU/RAM/Disk/P50-latency framing) — Kyle's
  data-engineering-at-scale background (220+ log sources, Dataproc/PySpark) is adjacent performance-and-scale
  work, but not the same as this JD's specific resource-budget/latency-SLA optimization framing. Not claimed
  as a direct match.

**Real gaps (not claimed anywhere in resume/cover letter):**
- No confirmed hands-on macOS/Linux/Windows corporate endpoint detection engineering specifically (Kyle's
  endpoint-adjacent work is via CrowdStrike EDR *data* ingestion/detection-content-building, not endpoint agent
  management or OS-level detection engineering).
- No confirmed Red Team/Purple Team exercise participation or post-exercise remediation-detection work (the JD
  calls this out as a specific responsibility).
- No confirmed "synthetic event generation" testing framework experience specifically — Kyle does write
  automated tests for his detection-as-code pipeline, but not the specific synthetic-event-generation technique
  named in the JD.
- 2-year minimum-qualification bars (security assessments, security engineering, coding) are trivially cleared
  by Kyle's 12 years of experience — his resume states his real total (12 years), not the JD's stated minimum,
  per standing instruction never to mirror a JD's minimum-years language back as Kyle's actual tenure.

## Formatting / parseability
Single-column, standard section headings (Professional Experience, Core Skills, Education & Certifications),
no tables/text boxes/icons, contact info in document body, standard fonts — passes the formatting rules in
`references/ats-optimization.md`.

## Recommendation
Package built as instructed (posting already passed fit/salary screening at 7/10). Biggest real risk in an
interview: the JD's "enterprise surfaces" framing (macOS/Linux/Windows/Workspace endpoint detection) is more
endpoint-agent-centric than Kyle's SIEM/data-platform-centric detection engineering background — be ready to
bridge that honestly (detection content built *on top of* endpoint EDR data like CrowdStrike, not endpoint
agent/OS-level engineering itself) rather than overclaiming direct endpoint-platform ownership. Also be ready to
speak plainly to the on-site/relocation question early in the process given Kyle's default remote preference.
