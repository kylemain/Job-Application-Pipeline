# ATS Coverage — Snowflake, Principal Security Engineer - Threat Intelligence

## Coverage summary
Strong match, driven by a real and previously-undocumented skill: Kyle confirmed (2026-07-29) extensive hands-on experience integrating threat intelligence into detection content and alert enrichment, plus exposure to paid/commercial, open-source, and home-grown CTI (Vedere Labs at Forescout). This directly addresses the JD's core charter — "combine deep intelligence expertise with strong engineering and program leadership skills, with AI and automation as core primitives."

## Direct matches
- "Convert intelligence into detections, threat hunts, investigative pivots" — direct match: Kyle has used CTI (indicators, TTPs, actor/campaign context) to tune detection rule logic and enrich alerts across 2,300+ MITRE ATT&CK-aligned rules at Trend Micro/Cysiv.
- "Build AI-assisted intelligence workflows for report triage, signal enrichment, summarization" — direct match: production GenAI tooling for false-positive triage, automated detection-rule generation, and cross-SIEM rule conversion.
- "Experience writing code... to automate manual workflows or analyze security data at scale" — direct match: Python-based orchestration framework, PySpark/Dataproc/BigQuery for large-scale analysis.
- "Experience handling data programmatically using SQL and Python... against large datasets" — direct match.
- "Strong understanding of enterprise security controls, threat hunting, and detection methodologies" — direct match: 2,300+ detection rules, signature/behavioral/statistical/time-series/ML detection.
- "Experience with one or more major cloud providers (AWS, Azure, GCP)" — direct match on AWS/GCP (hands-on IAM); Azure via Microsoft Sentinel/Defender API orchestration (adjacent, noted honestly below).
- "Mentor other engineers and analysts" — partial match: team-lead/sprint-lead experience, no formal management title.

## Real gaps (not claimed — noted here only, never in the cover letter)
- **"Significant experience in threat intelligence, cyber threat research, intelligence engineering"** as a primary discipline — Kyle's CTI experience is real and hands-on but has always been in service of detection engineering (using intel to tune/enrich), not as an independent threat-intelligence-analyst or threat-actor-tracking role. The JD is titled "Principal Security Engineer - Threat Intelligence" and implies CTI is the primary specialization; Kyle's framing leads with the intel-to-detection integration angle rather than claiming standalone CTI program ownership.
- **"Experience leading or materially shaping a Threat Intelligence program at scale"** (preferred, not minimum) — not claimed; Kyle has not led a named CTI program, only integrated intel into detection work as an IC.
- **Azure depth** — confirmed only as Sentinel/Defender API orchestration, not deeper Azure-native security architecture.
- **Formal people management** — not claimed; "mentor" language in JD is light-touch and doesn't require a management title, so this is a minor gap rather than disqualifying.

## Read before applying / interviewing
Salary ($249,000–$311,000) clears the floor comfortably. Remote, United States confirmed directly on the posting (Global Security category). This is a Principal-level IC role blending CTI + engineering + AI automation — the real interview risk is depth of independent threat-actor/campaign research versus Kyle's detection-engineering-first framing of CTI use. Be ready to speak plainly in interviews about the distinction: Kyle has never owned a CTI program end-to-end, but has real, repeated hands-on experience being the person on the receiving end of intel who turns it into working detection logic and alert context — which is arguably the exact seam this JD describes ("combine deep intelligence expertise with strong engineering... leadership").

## Formatting
Single-column, standard section headers (Core Skills, Professional Experience, Education & Certifications), no tables/text boxes/icons, Arial throughout, exported as text-layer PDF.

## Application quirks / gotchas (2026-07-29)
- Snowflake's "Apply Now" button on careers.snowflake.com redirects out to a separate Ashby-hosted board (jobs.ashbyhq.com/snowflake/...) — same ATS family as HackerOne's listing, and fully fillable via standard browser automation (no iframe lock, unlike Airbnb's Greenhouse embed).
- No EEO/gender/race/veteran/disability section on this form at all — Snowflake's Ashby form skips voluntary demographic questions entirely. Instead it has several US-export-control/legal questions: work-authorization sponsorship (answered No), prior Snowflake employment (No), current work authorization (Yes), "U.S. person" status for export-control purposes (answered "I am a U.S. person"), and SEC/PwC auditor-independence conflict check (answered No — never employed by PwC). All answered directly from the master reference doc's confirmed facts (work authorization / EEO section).
- "Where have you most recently worked?" free-text field auto-populated as "Shorepoint" from resume parsing — confirmed correct, left as-is.
