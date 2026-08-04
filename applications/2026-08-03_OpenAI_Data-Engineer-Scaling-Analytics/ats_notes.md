# ATS Notes — OpenAI, Data Engineer, Scaling Analytics

Posting: https://jobs.ashbyhq.com/openai/c59e2e83-59a6-45bc-82cd-665c6a8a5761
Department: Scaling. Team: Scaling Analytics, within OpenAI's Industrial Compute organization — the data
backbone for infrastructure deployment, hardware operations, supply chain, capacity planning, and site
execution as OpenAI scales its global data-center footprint (Stargate).

**Location:** San Francisco. Location Type on the posting is explicitly listed as **Hybrid** (not ambiguous —
no remote-eligible language anywhere in the body). Flagging clearly per Kyle's remote-only preference, even
though this posting was already fit-screened and passed before this build.

**Compensation:** $293,000 – $385,000 + equity. Comfortably clears Kyle's $170,000+ floor.

## Keyword coverage

| JD keyword/requirement | Coverage | Notes |
|---|---|---|
| 5+ years building/maintaining production data pipelines and analytical systems | Direct match | Kyle's total professional experience is 12 years (since Jan 2015, Experian) — real total stated in resume/cover letter, not the JD's stated minimum mirrored back. |
| Strong SQL, designing scalable data models | Direct match | SQL confirmed across all roles; Common Information Model / canonical data model design across 220+ sources is a direct, strong analog to "scalable data models." |
| Python or another data-engineering language | Direct match | Python confirmed extensively across all roles. |
| Modern data warehouses (Snowflake, BigQuery, Redshift) | Direct match (BigQuery) / **Gap** (Snowflake, Redshift) | BigQuery confirmed and used for large-scale analysis at Cysiv. No confirmed Snowflake or Redshift experience — not claimed. |
| Orchestration frameworks (Airflow, Dagster) | **Gap** | Not in the master doc's confirmed skills. Kyle's closest analog is GitLab CI/CD pipeline orchestration for detection-as-code (with automated testing and staged/safe rollout), which is real production-pipeline-orchestration discipline but not a DAG-based data scheduler — not claimed as Airflow/Dagster experience. |
| Designing reliable ETL/ELT workflows — maintainability, performance, operational excellence | Direct match | Core of the Cysiv-era ingestion pipeline work (220+ sources) and the DOE/NNSA ingestion platform build. |
| Partnering with cross-functional stakeholders to translate business requirements into technical solutions | Adjacent | Kyle has translated requirements from security analysts, SOC operators, and data scientists into pipelines/dashboards — real cross-functional delivery, but not specifically with Hardware Ops/Supply Chain/Finance-style business stakeholders. Framed honestly in the resume as cross-team stakeholder work, not claimed as infra/business-ops-specific. |
| Data quality checks, monitoring, and observability practices in production | Direct match | This is one of Kyle's strongest, most literal matches — data-quality monitoring/alerting content built at both DOE/NNSA SDI and Cysiv, plus connector/collector health monitoring. |
| Preferred: infrastructure, hardware ops, supply chain, manufacturing, logistics, capacity planning | **Gap** | No confirmed experience in these specific domains anywhere in the master doc. Not claimed; the cover letter draws an analog (operational telemetry → decision-ready dashboards) without pretending to have hardware/supply-chain domain experience. |
| Preferred: large-scale operational telemetry and business-critical reporting | Adjacent | Real, but the domain is security/SOC telemetry, not infrastructure/hardware telemetry — framed as an analog. |
| Preferred: distributed processing frameworks (Spark) | Direct match | PySpark/SparkSQL on GCP Dataproc confirmed directly. |
| Preferred: transformation frameworks (dbt) | **Gap** | Not in the master doc's confirmed skills. Not claimed. |
| Preferred: developing executive reporting and operational review metrics | Adjacent | Kibana dashboards and TSSOC analytics content serve as decision-support outputs for analysts/leadership, but this isn't the same as building formal executive/operational-review reporting for a business organization — framed honestly, not overstated. |
| Preferred: operating in fast-paced, ambiguous environments with evolving priorities | Direct match | Real and well-evidenced — Kyle was an early hire at Cysiv, building core data infrastructure as the company scaled from an internal Trend Micro project into an independent, established SIEM provider. |
| Preferred: interest in AI infrastructure at scale | N/A (soft signal) | Not a skill to claim — addressed narratively in the cover letter's framing rather than as a keyword match. |

## Summary for Kyle

**Real, honest matches this resume leans on:** production pipeline design/operation across 220+ heterogeneous
sources, Common Information Model / canonical data model design, ETL/normalization work, data-quality
monitoring and alerting, PySpark/Dataproc/BigQuery distributed processing, Apache Beam/GCP Dataflow batch
workloads, and dashboard-building for stakeholder decision-making. These map onto the JD's actual day-to-day
(pipeline engineering, canonical datasets, data-quality/observability, cross-team delivery) more literally
than a generic resume would, even though the target domain (infra/hardware ops) is new to Kyle.

**Real gaps, not papered over:**
- No confirmed Snowflake or Redshift experience (BigQuery is the confirmed warehouse).
- No confirmed Airflow or Dagster (or any DAG-based orchestration tool) — GitLab CI/CD pipeline orchestration
  is a real but different discipline, not claimed as equivalent.
- No confirmed dbt / transformation-framework experience.
- No confirmed hardware operations, supply chain, manufacturing, logistics, or capacity-planning domain
  experience — this is a genuinely new domain for Kyle; the resume/cover letter lean on the transferable data
  engineering discipline rather than claiming domain knowledge.
- Cross-functional stakeholder work is real but has been with security/SOC/data-science stakeholders, not
  Hardware Ops/Supply Chain/Finance-style business partners specifically.

**Location:** Confirmed hybrid, San Francisco — not a fully remote role. Flagging per Kyle's stated
remote-only preference even though this posting already cleared the fit screen (5/10) before this build.

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, contact info in the document body. Passes the formatting rules in
`references/ats-optimization.md`.
