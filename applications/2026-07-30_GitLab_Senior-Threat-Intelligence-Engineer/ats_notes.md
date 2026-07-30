# ATS Optimization Notes — GitLab, Senior Threat Intelligence Engineer

## Keyword coverage

**Direct matches (required/core JD asks):**
- "Provide actionable intelligence... get in front of threats before they materialize" → CTI-informed alert
  triage/false-positive validation at Forescout (Vedere Labs), closing the loop from intel to detection tuning
- "Leverage Python expertise as a force multiplier, expanding capabilities through automation and AI" → direct
  match — production Python automation for triage/enrichment, GenAI tooling for false-positive triage and
  detection-rule conversion
- "Monitor the threat landscape... raising awareness" → real precedent via CTI-driven detection tuning, framed
  honestly as intel-informed tuning rather than formal threat-landscape monitoring
- Elasticsearch/ELK depth (bonus, not explicitly asked but relevant to GitLab's own security tooling) → ES
  queries/transforms, Logstash, Beats, native ES detection rules, ES API, Kibana dashboarding across three
  employers

**Adjacent/transferable (framed honestly):**
- "Experience working with a Threat Intelligence Platform (TIP) and managing ingested/exported threat feeds" —
  Kyle has consumed and acted on CTI sourced by a dedicated research team (Vedere Labs), not personally
  administered a TIP or owned feed ingestion/export. Framed in the resume/cover letter as CTI-driven detection
  work, not TIP administration.
- "Experience researching adversaries using OSINT and structured analytical techniques" — Kyle's experience is
  using CTI context to validate whether an alert reflects real adversary activity (a triage/validation
  function), not primary OSINT research or attribution work. Same "bridge skill, not primary research"
  distinction used on other detection-engineering applications.

**Gaps (honest, not papered over):**
- No confirmed hands-on TIP administration (MISP, OpenCTI, Anomali, ThreatConnect, Recorded Future) — the JD's
  first screening question on the application form asks this directly; expect this to be a real point of
  friction in screening/interviews.
- No confirmed formal OSINT/threat-actor-attribution research experience.
- No confirmed malware reverse engineering experience (macOS/Linux) — JD lists this as "optional but valuable,"
  not required.
- Salary: band is $140,000–$200,000. Bottom is below Kyle's $170K floor; top clears it well. Built at Kyle's
  explicit request after reviewing this gap.
- Role is the sole dedicated member of GitLab's TI function — Kyle has real solo-ownership precedent elsewhere
  (Cysiv detection-as-code buildout, DOE/NNSA platform build), so "solo" itself isn't a mismatch; the specific
  TIP-administration/OSINT-attribution scope of this particular solo role is the actual gap.
- The GitLab application form includes two direct screening questions: "Do you have hands-on professional
  experience managing a Threat Intelligence Platform" and "This role involves automating tasks with python, do
  you have experience..." — the first should be answered honestly (No / limited, framed as CTI-consumption
  experience rather than TIP administration if the form allows free text; if it's a strict Yes/No gate, flag to
  Kyle before submitting since a bare "No" could auto-screen the application out).

## Formatting check
- Single-column, no tables-for-layout, standard section headings (Core Skills / Professional Experience /
  Education & Certifications), contact info in document body, standard Arial font. One page confirmed via PDF
  render (resume_page-1.jpg, cover_page-1.jpg). Passes ATS parseability rules per references/ats-optimization.md.
