# ATS Coverage & Fit Notes — Corelight, Security Product Researcher

## Salary check
Posted band: **$146,000 – $198,000 USD.**
Kyle's floor is $170,000+. The bottom of this band ($146,000) sits well below floor. The midpoint (~$172,000)
just clears the floor by a thin margin; the top third (~$180,667–$198,000) clears comfortably. **Flag: this
band's bottom is meaningfully below floor, and even the midpoint only just clears it — this is a thinner margin
above the floor than most recently-built packages.** Anchor to the top third if it gets to an offer conversation.

## Location / remote check
Posting header lists location as **"North America"**, not an explicit "Remote" tag. Corelight's careers page and
company culture messaging describe a "geographically distributed culture," which is a positive signal, but this
specific requisition does not explicitly guarantee remote-anywhere-in-North-America status the way some postings
do. **Flag this for Kyle** — worth confirming remote status directly during a recruiter screen before assuming
it's fully remote-eligible on Kyle's terms.

## Fit score: 5/10 (per initial screen — not re-screened here, materials built as instructed)

## Real gap — stated plainly, not surfaced in the cover letter
The JD's core qualification is **"5+ years of experience in agile development within a full-stack environment
with demonstrated experience in LLM and agentic AI ecosystems."** This is a real, honest gap: Kyle's background
is detection-content engineering (building analytics/detection layers on Elasticsearch and across multiple SIEM
platforms), not full-stack product software development. He has not built or shipped full-stack applications in
an agile product-engineering sense — his engineering work is pipeline/detection-content/data-platform
construction, which is adjacent (real coding, scripting, and platform-building work) but is not the same résumé
line as "full-stack software developer." The application's screening question ("Do you have 5+ years of
experience in Agile full-stack software development, including hands-on experience with LLMs and agentic AI
technologies?") will likely be a hard filter — Kyle should go in aware that this is the single biggest risk to
this application clearing an initial screen, not something the resume can fully paper over. The GenAI/LLM half
of that qualification is a genuine, direct match; the "full-stack software development" half is the gap.

Secondary, smaller gap: the JD names **YARA** alongside Zeek and Suricata as Corelight's open-source foundation.
Kyle's confirmed master-doc experience covers Zeek and Suricata directly (DOE/NNSA SDI ingestion) but does not
include confirmed hands-on YARA experience — YARA is intentionally not claimed anywhere in the resume/cover
letter.

Education: JD prefers "a degree in Computer Science, Cybersecurity, or a related technical field (or equivalent
practical experience)." Kyle's M.S./B.S. are in Physics, not CS/Cybersecurity — adjacent quantitative/technical
degree, explicitly covered by the JD's "or equivalent practical experience" carve-out, but not a literal keyword
match.

## Keyword coverage summary

**Direct matches:**
- Zeek, Suricata — confirmed via DOE/NNSA Security Data Integration project (CrowdStrike/Suricata/Zeek into
  Elasticsearch)
- LLM / agentic AI / GenAI for security and software use cases — confirmed (prompt engineering for detection
  content and false-positive triage, GenAI-driven SIEM API orchestration, reusable GenAI tooling for detection
  engineers)
- Network detection and response (NDR) — confirmed via years of Zeek/Suricata/Elasticsearch-based detection
  platform work
- Cybersecurity landscape, threat hunting, incident response, security operations — confirmed via Treasury SOC/
  TSSOC current work and prior detection engineering roles
- SIEM (Splunk, Elastic) — confirmed, deep experience across both
- Data analytics, AI-assisted security decision-making, automation — confirmed via data science background and
  GenAI tooling

**Adjacent/transferable (named honestly, not oversold):**
- Agile development / distributed team environment — Kyle has team-lead/sprint-lead experience and has worked
  fully remote across multiple employers, but no formal "Agile practitioner" title or certification; framed as
  real practical Agile/remote-team experience, not claimed as a specific methodology certification
- OSI layers 2–7 / network security concepts (encryption, protocol abuse, attack patterns) — Kyle's Zeek/Suricata
  detection-content work is inherently built on deep network-traffic analysis at these layers, but the master doc
  doesn't document formal OSI-model coursework or certification — framed as practical detection-engineering
  exposure to protocol-level attack patterns, not formal networking-theory credentialing
- Degree in CS/Cybersecurity or related field — Physics degrees are adjacent technical/quantitative credentials,
  covered by the JD's own "or equivalent practical experience" language

**Gaps (not claimed anywhere):**
- 5+ years of full-stack agile software development specifically (see above — the single largest gap)
- YARA (Zeek and Suricata claimed directly; YARA is not)

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications), no
tables/text boxes/icons, contact info in the document body — passes the formatting rules in
`references/ats-optimization.md`.

## Recommendation
Package built per Kyle's instruction (posting already passed initial fit screening at 5/10). Go in with eyes open
on the full-stack-development screening question and the salary-band-bottom flag above; the GenAI/LLM and Zeek/
Suricata overlap are genuinely strong and worth leading with in any conversation that gets past the initial
screen.
