# ATS Optimization Notes — Roblox, Principal Detection and Response Engineer

## Fit score: 7/10

Strong domain match on the JD's core D&R asks (detection engineering, security data pipelines, SIEM/EDR,
structured incident response), pulled almost entirely from confirmed, already-differentiated master-reference
material (nine-platform SIEM/EDR orchestration, 220+ log source ETL pipelining, DOE/NNSA ground-up build,
live Treasury SOC support). The score is held at 7 rather than higher for two real reasons: (1) the JD's SWE
requirement explicitly asks for "mastery" of C, Golang, or Java — Kyle's programming depth is Python-centric,
a genuine gap for a role this senior/SWE-leaning; (2) this is a hybrid in-office role (Tue/Wed/Thu onsite,
San Mateo, CA) against Kyle's remote-only default, which doesn't lower the skills-fit score itself but is a
material candidacy consideration flagged separately below and in job_link.txt / interview_prep.md.

## Location / work-mode flag (read before proceeding)
JD states plainly: "This is a hybrid in-office role" — onsite Tuesday/Wednesday/Thursday, optional Monday/Friday,
based in San Mateo, CA. This is not an ambiguous header-tag situation; the JD body is explicit. Kyle is
remote-only by default per his standing fit rules, but has indicated he's open to relocating/hybrid for the
right role — and at $295K–$345K base with a strong skills match, this qualifies as worth surfacing rather than
auto-rejecting. Confirm relocation logistics and the real day-to-day hybrid cadence directly in the interview
process before advancing.

## Keyword coverage

| JD requirement | Coverage | Notes |
|---|---|---|
| 8+ years Detection and/or Response | **Direct** | 12 years total professional security experience (since Jan 2015, Experian) — including 8+ years in dedicated detection/response roles (Sep 2018–present) across Trend Micro/Cysiv, Forescout, Shorepoint/Treasury SOC |
| 4+ years Security Data Engineering, streaming pipelines (Kafka/PubSub, Spark/Flink, Athena/BigQuery) | **Direct/Adjacent** | PySpark, GCP Dataproc, BigQuery, Apache Beam/Dataflow are direct hands-on ownership (4+ years, Trend Micro/Cysiv); Kafka and Flink are confirmed hands-on exposure but not primary pipeline ownership — framed honestly as "exposure," not "built end-to-end," in the resume. Athena itself (AWS) not used directly, but BigQuery is the exact same class of tool the JD names as "or similar" |
| SWE mastery: C, Golang, or Java, CI/CD deployed scalable systems | **Gap** | Kyle's programming background is Python — no confirmed C/Golang/Java experience in the master reference. Real, honest gap; not claimed anywhere in resume or cover letter. CI/CD (GitLab) and production-grade system-building are strong (detection-as-code orchestration framework), just not in the JD's named languages |
| SIEM, EDR, NDR, SOAR — onboarding logs, custom detections/automations | **Direct/Adjacent** | SIEM: nine-platform orchestration (Sentinel, Defender, Google SecOps, Splunk, CrowdStrike, SentinelOne, Sumo Logic, XSIAM, Devo, plus ArcSight) — direct. EDR: CrowdStrike and SentinelOne native API work — direct. NDR: Suricata/Zeek ingestion and detection — direct. SOAR: no named SOAR platform (Splunk SOAR/Phantom/Demisto/Tines) — the Python orchestration/automation framework functions as a SOAR-style automation layer and is framed that way, not claimed as formal SOAR platform ownership |
| Structured, mature incident response processes | **Direct** | Active Treasury SOC (TSSOC) incident/case queue support, team-lead role; structured IR and root-cause analysis |
| Network protocols, OS, cloud, virtualized hosts, containers | **Direct/Adjacent** | Network protocols via Suricata/Zeek NDR telemetry; multi-cloud (AWS/GCP/Azure); containers (Docker, comfortable user; Kubernetes-orchestrated platform experience as a user, not administrator — framed accurately) |
| Analytical thinking, crisis management, root cause analysis | **Direct** | Structured IR/RCA at Treasury SOC; false-positive tracking and detection tuning across nine platforms |
| Grow the D&R team, mentor junior engineers, contribute to hiring | **Adjacent** | Team-lead/sprint-lead experience confirmed in master reference; no formal management title or hiring-process ownership — not claimed as such |

**Summary: 6 of 8 core JD requirement areas are direct matches, 1 is adjacent/transferable (SOAR framing,
Kafka/Flink exposure), 1 is a real, unconcealed gap (C/Golang/Java "mastery").**

## Formatting check
Single-column, no tables-for-layout, standard section headings (Core Skills / Professional Experience /
Education & Certifications), contact info in document body (not header/footer), standard Arial font throughout.
One page confirmed via PDF render and visual inspection of resume_page-1.jpg / cover_page-1.jpg — no overflow,
no awkward line wraps. Passes ATS parseability rules per references/ats-optimization.md.

## Visual QA notes
Initial resume render overflowed to a 2-page PDF (Education/Certifications section pushed onto page 2 by ~2
lines). Trimmed summary and three Core Skills lines plus two experience bullets for density; rebuilt and
re-rendered — confirmed single page on the second pass. Cover letter rendered clean at one page on the first
pass, no changes needed.

## Correction (2026-08-02)
This package originally understated Kyle's experience and dropped a real role: the summary and cover letter
said "8+ years" (mirroring the JD's stated minimum back as if it were Kyle's actual tenure) and the resume's
work history omitted Experian (Jan 2015 – Jan 2018, Security Data Scientist) entirely. Per the master
reference's "Total Years of Experience" note, Kyle's real total is 12 years (since Jan 2015). Fixed: summary
now reads "12 years of security experience, including 8+ years building..." (the 8+ years figure is accurate
and kept as the scoped tenure for dedicated detection/response roles since Sep 2018); cover letter now names
Experian and says "12-year security career"; Experian was added back to the resume's Professional Experience
section (compressed to one bullet to preserve the one-page limit — three bullets/lines trimmed elsewhere to
make room); resume re-rendered and confirmed single-page. interview_prep.md's closing script updated to match.
