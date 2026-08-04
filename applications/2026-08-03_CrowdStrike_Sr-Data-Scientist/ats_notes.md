# ATS Coverage — CrowdStrike, req R29100 ("Sr. Software Engineer - Cloud (Hybrid)")

## Read this first: title/scope/location mismatch
The posting URL slug says "Sr-Engineer-Cloud--Remote-" and the original scan assumed a remote "Sr. Data
Scientist" role. The live page for this exact req (R29100) is titled **"Sr. Software Engineer - Cloud
(Hybrid)"** — a backend distributed-systems/Golang microservices engineering role on the Risk Analytics
team, building the platform behind risk-compounding, attack-path analysis, and posture scoring (not a
data-scientist IC role doing the modeling itself). The live JD states explicitly: **"This is a hybrid role
requiring 2-3 days in our Sunnyvale, CA office."** This directly conflicts with Kyle's remote-only standing
rule; the mismatch was invisible in the original salary/title summary. A separate, genuinely-titled
"Sr. Data Scientist (Hybrid)" req exists (R29023, NGSIEM Agentic AI team) but is also Hybrid/Sunnyvale and
asks for MS/PhD + published research/patents + production LLM/RAG/vector-search at enterprise scale — a
larger stretch than R29100, not a fix for the mismatch.

Given the actual req is backend/distributed-systems engineering, the resume/cover letter here are framed
around Kyle's strongest real overlap with the team's mission — large-scale data pipeline ownership plus
applied ML/detection content for risk-scoring/anomaly use cases — rather than forcing either a pure
Data Scientist or a pure backend-SWE narrative that oversells unconfirmed skills.

## Salary flag
$140,000–$215,000 disclosed on both R29100 and R29023. Midpoint ~$177,500 clears Kyle's $170K floor
comfortably. Anchor to top third (~$190K+) once/if a conversation happens.

## Coverage summary (against R29100's actual "What You'll Need" list)
**5 of 12 required items covered directly, 4 adjacent, 3 real gaps.**

### Direct matches
- Cloud infrastructure: AWS, GCP, Azure — confirmed multi-cloud, incl. Sentinel/Defender API orchestration
- Apache Spark — direct, extensive (PySpark/SparkSQL on GCP Dataproc, EDA at scale)
- Python — direct, core language across all roles
- Engineering best practices (testing, code review, resilient architecture) — direct via the multi-SIEM
  detection-as-code CI/CD pipeline (automated tests, staged/safe rollout, rule-quality metrics)
- Cybersecurity industry experience (bonus item) — direct, 12 years

### Adjacent/transferable (stated honestly, not oversold)
- "8-10 years production experience building/maintaining large-scale distributed systems" — Kyle has 12
  years total, with real large-scale data pipeline and SIEM-platform ownership (220+ log sources, next-gen
  cloud SIEM), but not specifically *backend distributed-systems service* ownership in the way this req
  means it (customer-facing microservices, not detection content/data pipelines)
- Kafka and Flink — confirmed familiarity and hands-on exposure (worked in an environment using Flink jobs),
  not primary ownership/architecture of either
- System troubleshooting for complex distributed architectures — adjacent via connector/collector health
  monitoring and troubleshooting, not backend-service-specific
- Mentoring junior engineers / technical decision-making — adjacent via confirmed team-lead/sprint-lead
  experience; no formal management title

### Real gaps (not claimed)
- **Golang** — not confirmed anywhere in the master reference. This is a primary/co-primary language
  requirement for R29100 ("we primarily use Golang and Python") and is the single biggest likely blocker.
- **Microservices / REST API architecture ownership** — Kyle's engineering work has been data
  pipelines/detection content, not designing/operating customer-facing REST microservices.
- **Graph databases, Cassandra/CQL** (bonus items) — no confirmed experience with either.

### Notes carried over from the original task framing (for R29023-style expectations, not R29100)
If evaluated against the *other* req's profile (8+ years AI/ML research leadership in cybersecurity
specifically, publications/patents, production LLM/RAG/vector-search at enterprise scale): Kyle's ML work
is applied/production (clustering, time-series anomaly detection, UEBA), not academic-research-track — no
confirmed publications or patents. Deep-learning-at-scale production ownership is not confirmed beyond
PyTorch familiarity. These would be real gaps if R29023 were the target; not directly applicable to R29100's
actual requirements, but worth having honest answers ready for in case the conversation moves toward the
NGSIEM/Agentic AI team instead.

## Formatting
Single-column, standard section headers, no tables/text boxes/icons, Arial throughout, exported as
text-layer PDF. Visual QA passed — one page each, no overflow or awkward wraps.
