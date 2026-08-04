# ATS Coverage & Fit Notes — OpenAI, Data Engineer, People Innovation Labs

## Location flag
San Francisco, Hybrid. Not remote. Per the master reference, Kyle's default screening preference is fully
remote roles, and on-site/hybrid postings are flagged rather than built by default. This posting was
pre-screened and passed (fit score 5/10) with this location already known and factored in — see the
2026-08-03 watchlist entry in `applications/_lib/seen_jobs.log`. Flagging again here for visibility before
any submission decision.

## Salary check
Posted band: **$293,000 – $325,000 USD base, plus equity.** Comfortably clears Kyle's $170,000+ floor by a
wide margin. Anchor negotiation to the top third (~$317,000–$325,000) once fit is confirmed.

## Keyword coverage summary

**Direct matches:**
- Python — confirmed, core language
- Data pipeline design/build/management at scale — confirmed directly: 220+ unique data source ingestion
  pipelines built from scratch as an early startup hire (Trend Micro/Cysiv)
- "Canonical datasets" to track key metrics — strong direct match: Kyle's Common Information Model (CIM) is
  literally a canonical-schema/data-dictionary design and standardization effort across every pipeline, the
  same concept the JD names explicitly for tracking "key people metrics and People Innovation Labs product
  metrics"
- Spark — confirmed via PySpark/SparkSQL work at Trend Micro/Cysiv (GCP Dataproc clusters, Zeppelin
  notebooks, Spark jobs loading data from cloud storage buckets)
- Robust, fault-tolerant data ingestion/processing systems — confirmed via connector/collector health
  monitoring, data-quality monitoring/alerting content built at both Trend Micro/Cysiv and Shorepoint
- "Primary data engineering expert" on a team — confirmed: Kyle was a very early hire at Cysiv building the
  data engineering function from scratch, the same "primary DE on a small team" positioning this role calls for
- Data security, integrity, and compliance — confirmed via data-quality monitoring/alerting and a security
  background that maps onto data-integrity ownership
- Cross-team collaboration with multiple stakeholder groups (JD names Data Platform, Data Science, People
  Analytics, Compensation and Equity) — confirmed pattern of working across engineering, data science, and
  business-facing teams throughout career, though not with these specific named teams (see gaps below)
- 3+ years as a data engineer, 8+ years total software/data engineering — Kyle's real total is **12 years**
  (since Jan 2015, Experian), with dedicated data-engineering ownership concentrated in the Trend Micro/Cysiv
  (2018–2022) and Shorepoint (2023–present) roles. Comfortably clears both JD minimums; the JD's stated
  minimums are not mirrored back as Kyle's actual tenure anywhere in the resume/cover letter.

**Adjacent/transferable (named honestly, not oversold):**
- Distributed processing/storage (JD names Spark, Hadoop, Flink, HDFS, S3) — Kyle's confirmed cloud-storage
  and distributed-compute experience is GCP-native (Dataproc, Dataflow, BigQuery, GCS bucket-based Spark
  jobs), not AWS S3 or Hadoop/HDFS specifically. Flink/Kafka exposure is real but the master reference
  confirms it as "worked in an environment that used Flink jobs, not primary ownership/architecture" —
  surfaced on the resume as "working exposure ... in a production streaming environment," not primary
  ownership.
- Cross-team collaboration — real and confirmed as a pattern, but not specifically with People Analytics,
  Compensation and Equity, or other HR-domain stakeholder teams (see gap below).

**Real gaps (not claimed anywhere on the resume or in the cover letter):**
- **Databricks** — not confirmed anywhere in Kyle's skills inventory. The JD explicitly calls for data
  "seamlessly integrated into our Databricks warehouse." Kyle's warehouse/distributed-compute experience is
  GCP-native (Dataproc/BigQuery), not Databricks. Genuine gap.
- **Snowflake** — not confirmed. Genuine gap, same as flagged on the earlier OpenAI Applied AI application.
- **ETL schedulers (Fivetran, Airflow, Dagster, Prefect)** — none of these are confirmed in the master
  reference. Kyle's pipeline orchestration experience is real (GitLab CI/CD for detection-as-code, homegrown
  Apache Beam/Dataflow jobs) but not hands-on ownership of a dedicated ETL scheduler tool. Genuine gap.
- **Scala or Java** — the JD lists Python, Scala, or Java as acceptable languages; Kyle's confirmed
  programming languages are Python, SQL, and R. Not claimed.
- **Hadoop / HDFS / S3** — not confirmed. Kyle's distributed big-data work is GCP-native, not Hadoop/HDFS or
  AWS S3-specific. Genuine gap.
- **People/HR data domain experience** — this is the most important honest gap to flag for this specific
  req: every one of Kyle's data engineering roles has been in security/threat-data domains (SIEM telemetry,
  detection content, DNS/malware data), not HR, recruiting, or people-analytics data domains. He has no direct
  exposure to HRIS-style "business systems of record," people-metrics taxonomies, or HR-specific compliance
  considerations (e.g., PII/employee-data handling nuances beyond general data-security practice). The
  underlying data engineering skills (pipeline design, canonical datasets, data-quality ownership) transfer
  directly, but the domain itself is new. Not glossed over — this is the single biggest interview risk on this
  req.

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, contact info in the document body (not header/footer) — passes the formatting
rules in `references/ats-optimization.md`.

## Recommendation
Materials built as directed (posting already fit-screened and passed at 5/10 — a borderline-but-passing
score reflecting the strong data-engineering/canonical-dataset overlap weighed against the hybrid SF location,
the missing named-platform tooling (Databricks/Snowflake/Airflow-family), and the HR-domain gap). Genuine gaps
worth having ready answers for if this reaches a technical screen: no hands-on Databricks or Snowflake
experience, no dedicated ETL-scheduler ownership (Airflow/Dagster/Prefect/Fivetran), no Hadoop/HDFS/S3-specific
experience, and no prior People/HR data domain exposure. Kyle's canonical-dataset (CIM) work, Spark/PySpark
depth, and track record as the "first/primary data engineer" building a data function from scratch are strong,
directly relevant proof points for this specific req.
