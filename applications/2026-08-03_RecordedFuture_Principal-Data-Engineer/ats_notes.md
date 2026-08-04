# ATS Optimization Notes — Recorded Future, Principal Data Engineer

## Keyword coverage

**Direct matches (already in master doc, confirmed):**
- "Python" (JD: "5+ years of Python programming") — direct match; Kyle's total professional experience
  is 12 years, well beyond the stated minimum.
- "ElasticSearch" — strong direct match, deep cross-employer experience (queries/Query DSL, transforms,
  Logstash, Beats, native detection rules, Kibana, ES API) — led the resume per Kyle's positioning
  guidance and named at the specific sub-skill level rather than a generic "ELK Stack" bullet.
- "cloud computing tools" — direct match (AWS, GCP, Azure all confirmed).
- "Architecting and delivering production-grade applications and ETL/ELT pipelines" — direct match,
  220+ source ingestion pipelines built and operated end to end.
- "Applying statistical techniques to draw accurate, impactful conclusions" — direct match (clustering/
  unsupervised ML, time-series anomaly detection, EDA at scale).
- "Efficient & accurate problem solving skills, including the ability to debug both software and data" —
  direct match (connector/collector health monitoring and troubleshooting, data-quality alerting work).
- "Eagerness to continue learning and teaching new skills to team members" — direct match via team-
  lead/sprint-lead mentoring experience (see gap note below on scope).

**Adjacent/transferable (real experience exists, but not an exact match to the JD's phrasing):**
- "Message buses (e.g. Kafka, RabbitMQ)" — Kafka: confirmed familiarity and hands-on exposure, but not
  primary ownership/architecture at the "3+ years" depth the JD states. RabbitMQ: no confirmed
  experience. Framed in the resume as "working familiarity with Kafka," not 3+ years of message-bus
  architecture ownership.
- "AI approaches and productizing flagship LLM output" (preferred) — adjacent/strong: Kyle has real,
  confirmed prompt-engineering and GenAI-tooling experience (GenAI-powered "skills" for detection
  engineers, using GenAI to orchestrate SIEM APIs), framed honestly as that rather than claiming
  large-scale LLM product ownership.
- "Orchestration tools such as Argo CD, Kubernetes, Prefect" (preferred) — Kubernetes: confirmed
  hands-on experience as a user of a Kubernetes-orchestrated platform, not cluster administration.
  Argo CD and Prefect: no confirmed experience — not claimed.
- "Developing REST APIs with Python frameworks (e.g. Flask, Django, FastAPI)" (preferred) — adjacent,
  not direct: Kyle has built reusable per-technology API adapters/orchestration clients that consume
  many SIEM vendor REST APIs (listing alerts, tables, schemas, managing tokens/roles), which is real
  API-integration depth, but this is consuming/orchestrating third-party APIs, not confirmed hands-on
  building REST APIs with Flask/Django/FastAPI specifically. Not claimed directly in the resume.
- "Leadership experience" / "Mentor direct reports" — real gap in scope, not fabricated: Kyle has
  team-lead/sprint-lead experience and has mentored peers on rule/pipeline design (confirmed, and
  reflected honestly in the resume as "served in a team-lead capacity... mentoring detection
  engineers"), but has never held a formal people-management title or owned direct reports/headcount.
  This is a real gap against the JD's "mentor direct reports" language and should be addressed
  honestly in interviews rather than overclaimed.
- "Bachelor's/Master's degree in Computer Science, Mathematics, Statistics, Engineering" — Kyle holds
  M.S./B.S. Physics, not one of the named degrees directly, though Physics is a closely adjacent
  quantitative field and the JD includes an "or equivalent experience" clause. Not a hard blocker but
  worth noting as not a literal match.

**Gaps (real, not papered over — flagged here for Kyle's awareness, not surfaced in the cover letter):**
- **MongoDB** — no confirmed hands-on experience anywhere in the master doc. Stated as a required
  "3+ years" item alongside message buses and graph databases.
- **Graph databases (AWS Neptune / Neo4j)** — no confirmed hands-on experience. Also stated as part of
  the same required "3+ years" bucket. This is a real, material gap — the JD explicitly ties this to
  the "Intelligence Graph" the role works against.
- **RabbitMQ** — no confirmed experience (see message-bus note above).
- **Argo CD, Prefect** — no confirmed experience (preferred, not required).
- **Formal people-management / mentoring direct reports** — see leadership note above; team-lead/
  sprint-lead experience is real but this is not the same as owning direct reports.

## Formatting check
Single-column, no tables-for-layout, standard section headings ("Professional Experience," "Core
Skills," "Education & Certifications"), contact info in the document body (not header/footer),
standard Arial font throughout, no icons/images. One page confirmed via PDF render for both resume
and cover letter (resume_page-1.jpg, cover_page-1.jpg) — clean line wraps, no overflow, no orphaned
content on either document.

## Location / remote-policy finding
The live Greenhouse posting lists the location simply as "Boston, MA" with **no mention of remote or
hybrid anywhere in the full JD body** — no "remote," "hybrid," or distributed-team language at all, in
contrast to some postings that bury a remote-eligibility clause in the body text. This reads as an
on-site Boston role. This directly conflicts with Kyle's remote-only screening preference and should
be weighed accordingly — Kyle should confirm with a recruiter whether any remote flexibility exists
before investing further, since nothing on the public posting suggests it does.

## Summary for Kyle
Strong keyword coverage on the Elasticsearch/data-engineering/Python/statistical-technique side of the
JD — this is a genuinely good technical fit on the "build and own large-scale data pipelines" core of
the role. The real, un-papered-over gaps are (1) MongoDB and graph databases (Neo4j/Neptune), which the
JD ties directly to the Intelligence Graph the role works against, (2) message-bus depth beyond Kafka
familiarity (RabbitMQ unconfirmed, Kafka not at the stated 3+ year ownership level), and (3) the
"mentor direct reports" language implies formal people management that Kyle hasn't held — team-lead/
sprint-lead mentoring is real but narrower in scope. On top of the skills gaps, the on-site Boston, MA
location itself is a conflict with Kyle's remote-only preference and is worth resolving with the
recruiter early rather than late in the process.
