# ATS Notes — Cribl, Staff Security Operations Engineer

## Salary check
Disclosed band: $128,000 – $200,000 USD base (geography-dependent).
**Risk flag:** the bottom of this band ($128K) sits well below Kyle's $170K floor. The top ($200K) clears it
comfortably. Because it's geography-dependent, the actual offer for a Dallas/Ft. Worth-based remote candidate
could land anywhere in that range — this is a real risk, not just a formality. If pursued, anchor negotiation
language to the top third of the band (~$176K+) and be prepared to walk if the initial offer lands in the
bottom half. Worth confirming banding/geo-tier with the recruiter early rather than late in the process.

## Fit assessment — Score: 8/10
Remote: fully remote ("Remote - United States"), no on-site/hybrid component. No flag needed.
Federal contracting: none — Cribl is a private security/observability vendor, not a federal contractor. No flag.
Not on the company exclusion list.

**Why 8, not higher:** the core of this role — SIEM/detection-as-code, MITRE ATT&CK-mapped detection engineering,
incident response, threat intel integration, Python scripting — is an excellent, well-evidenced match against
Kyle's actual work history. The Cribl pipeline experience is a genuine, rare differentiator for this specific
employer that most other candidates won't have. It's not a 9-10 because several of the JD's named "nice to have"
tools/practices aren't confirmed in Kyle's history (see gaps below) — real, not fatal, gaps for a role titled
"Staff" that likely expects broad tooling breadth.

### Direct matches
- SIEM, detection as code, EDR, incident response/management — core of Kyle's 12-year security career, with
  8+ years specifically in dedicated detection/response roles (Cysiv/Trend Micro, Forescout, Shorepoint/Treasury
  SOC) on top of earlier security data science work at Experian (2015–2018).
- MITRE ATT&CK mapping — 2,300+ detection rules built and managed covering most of the matrix.
- Scripting/coding — Python, confirmed production-grade, used throughout the detection-as-code framework.
- Developing/implementing/maintaining high-fidelity detection rules across SIEM/EDR based on threat intel and
  MITRE ATT&CK, with continuous tuning to reduce false positives — directly evidenced (formal coverage/FP-rate
  tracking, staged/safe rollout, confirmed in master doc).
- Monitoring/triaging via SIEM tooling — core of the Treasury SOC (TSSOC) role and prior Cysiv work.
- Collaborating with threat intel to integrate IOCs/TTPs into detections — direct match (Vedere Labs sourcing,
  CTI-driven detection tuning, confirmed differentiator).
- Splunk SPL — confirmed (Splunk saved searches/detection content at Shorepoint, Splunk certifications).
- Cloud-native tooling exposure — AWS, GCP, Azure all confirmed (Azure specifically scoped to Sentinel/Defender
  API orchestration, not deeper Azure-native tooling).
- **Cribl** — the standout differentiator. Confirmed hands-on experience creating and managing Cribl pipelines
  directly. Not currently on Kyle's public resume; surfaced prominently here (skills section + cover letter
  opening) because this is literally the product this security team runs.

### Adjacent / transferable (framed honestly, not oversold)
- Auth schemes (SAML, OpenID, OAuth2, SCIM): **no confirmed hands-on experience.** What IS confirmed is
  substantial API-level identity/access work — creating and managing API tokens, roles, and permissions across
  nine SIEM platforms as part of the orchestration framework, plus IAM policy/role implementation on AWS and GCP.
  This is real access-management work but not the same as implementing/troubleshooting SAML/OIDC/OAuth2/SCIM
  federation flows. Framed in resume/cover letter as API token/role/permission management — never claimed as
  SAML/OIDC expertise. This is the one JD "must-have" bullet with a real gap; worth having a candid answer ready
  for the interview (e.g., "I've done adjacent identity work at the API/token level across many platforms, but
  haven't personally configured SAML/OIDC federation — happy to go deep on that fast").
- Panther SIEM: not confirmed as a platform Kyle has used, but the JD calls it "a plus," not required. Kyle's
  9-platform orchestration breadth (Sentinel, Defender, Chronicle, Splunk, CrowdStrike, SentinelOne, Sumo Logic,
  XSIAM, Devo, ArcSight) is a reasonable answer to "have you worked with X" pattern-matching even without Panther
  specifically — framed generically as broad multi-SIEM API orchestration experience.
- Wiz / CSPM tooling: not confirmed. Also listed as "a plus," not required — not surfaced as a claimed skill.
- Sigma / YARA rule formats: not confirmed by name in the master doc. Splunk SPL is confirmed and named directly;
  Sigma/YARA were not claimed anywhere in the resume/cover letter to avoid overstating.

### Real gaps (not surfaced to the employer — for Kyle's awareness only)
- No confirmed formal "incident response lead" / incident commander title — Kyle's IR work is described honestly
  as owning detection/alerting content a live SOC runs its investigations against, not as IC ownership of the
  incident lifecycle itself.
- No confirmed experience running tabletop exercises, formal purple-team engagements, or vulnerability
  penetration testing — the JD's "if you've got it" list includes threat hunts/purple team activities and
  leading IR tabletops; nothing in the master doc supports claiming this directly, so it wasn't included.
- Zero-trust networking is named in the JD's "modern security principles" list — no confirmed hands-on zero-trust
  architecture work in the master doc; not claimed.

## ATS keyword coverage
Required/core keywords: SIEM (direct), security data lakes (adjacent — Elasticsearch-based platforms built),
detection as code (direct), EDR (direct — CrowdStrike, SentinelOne), zero trust networking (gap, not claimed),
MITRE ATT&CK (direct), SAML/OpenID/OAuth2/SCIM (gap/adjacent, framed as API token/role/permission management),
Python (direct), incident response (direct).
"If you've got it" keywords: SIEM/CSPM/MSSP monitoring (direct via SIEM/EDR triage), detection rule
tuning/false-positive reduction (direct), IR lead (adjacent), security playbooks (not explicitly claimed —
absent from master doc, omitted rather than invented), threat hunts/purple team (gap, omitted), tabletop
exercises (gap, omitted), Cribl (direct — headline differentiator), threat intel to detection (direct), Panther
(gap, omitted), Wiz/cloud-native (gap, omitted), Sigma/YARA/SPL/KQL (SPL direct, others omitted).

Bottom line: strong direct coverage on every hard-required item except the auth-scheme bullet, which is honestly
framed as adjacent. The "if you've got it" list has more gaps, which is expected/acceptable for a preferred-skills
list — none of the omitted items were fabricated.

## Correction (2026-08-02)
Fixed a years-of-experience understatement: the resume summary and cover letter said "10+ years" / "a decade,"
and this notes file described SIEM/detection/IR work as "the last 8+ years" naming only the post-2018 employers.
Per the master reference's "Total Years of Experience" note, Kyle's real total is 12 years (since Jan 2015,
Experian) — Experian was already present in this resume's work history, so this was a framing/wording fix only,
no content was missing. Resume and cover letter now say "12 years"; rebuilt and re-confirmed single-page.
