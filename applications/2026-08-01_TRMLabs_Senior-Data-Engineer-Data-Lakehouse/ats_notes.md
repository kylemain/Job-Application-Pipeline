# ATS Optimization Notes — TRM Labs, Senior Data Engineer, Data Lakehouse Infrastructure

## Keyword coverage

**Direct matches (already in master doc, confirmed):**
- "GCP" / Google Cloud Platform — direct match (Dataproc, BigQuery, Dataflow, GCP serverless/event-
  driven enrichment all confirmed)
- "Dataproc," "BigQuery," "Dataflow" — direct, named matches, called out explicitly in resume/cover
  letter rather than folded into a generic "cloud" bullet
- "Spark" — direct match (PySpark/SparkSQL, used at production scale for EDA and distributed
  processing) — covers the JD's "one or more query engines: Trino, Presto, Spark, or Snowflake" bar
- "Kafka" — direct match, confirmed familiarity
- "Python" / "SQL" / "SparkSQL" — direct match, JD calls for "exceptional Python skills; adept in
  SQL/SparkSQL"
- "metadata management" — adjacent-but-strong match: the Common Information Model (a data
  dictionary standardizing field names/types across 220+ sources) is real, hands-on schema/metadata
  governance work, framed honestly as the same discipline rather than claiming Iceberg-catalog-
  specific metadata tooling
- "data governance" — same CIM work applies; framed as data-dictionary/schema-standardization
  governance, not a formal data-governance-program title
- "streaming/batch pipelines using GCP-native services" — direct match via Dataflow/Beam (batch,
  historical/cold-storage retrieval at scale) and GCP serverless event-driven enrichment (near-
  streaming); Kafka exposure supports the streaming side generally
- "ETL/ELT pipelines" — direct match, 220+ source ingestion pipelines built and operated

**Gaps (real, not papered over — flagged here per Kyle's standing instruction, not in the cover letter):**
- **Trino / Presto** — no confirmed hands-on experience. JD explicitly lists Trino first among query
  engines and names it twice ("distributed query engines (Trino, Spark, or Snowflake)" and "high-
  performance data lakehouse... StarRocks, Apache Iceberg... Dataproc, Kafka"). Spark covers the
  "one or more query engines" minimum-qualification bar, but Trino specifically is unconfirmed.
- **Apache Iceberg / Hudi / Delta Lake** — no confirmed hands-on experience with any open table
  format. This is a stated requirement ("Experience with modern table formats: Apache Hudi, Iceberg,
  or Delta Lake") and central to the role's "impact" bullets (Iceberg named 3 times in the JD). This
  is the single largest gap on this application.
- **StarRocks** — no confirmed experience; named as part of TRM's specific GCP lakehouse stack.
- **Snowflake** — no confirmed experience (one of three acceptable query engines per the JD; Spark
  covers the requirement, but Snowflake itself is unconfirmed).
- **Apache Airflow** — no confirmed hands-on orchestration experience. JD explicitly wants "hands-on
  orchestration with Airflow." Kyle's orchestration experience is GitLab CI/CD-based — real pipeline-
  orchestration discipline (staged rollout, automated testing, production deployment gating), but not
  Airflow/DAG-based specifically. Framed in resume/cover letter as CI/CD pipeline orchestration
  without claiming Airflow.
- **GCP Composer** — not confirmed (Composer is GCP-managed Airflow; same gap as above).

## Formatting check
Single-column, no tables-for-layout, standard section headings ("Professional Experience,"
"Education & Certifications," "Core Skills"), contact info in document body (not header/footer),
standard Arial font throughout, no icons/images. One page confirmed via PDF render for both resume
and cover letter (resume_page-1.jpg, cover_page-1.jpg) — clean line wraps, no overflow, no orphaned
content.

## Summary for Kyle
Direct/strong keyword coverage on the GCP-specific stack (Dataproc/BigQuery/Dataflow), Spark/
PySpark/SparkSQL, Kafka, Python/SQL, and the metadata-management/data-governance angle via the CIM
work — this is a genuinely strong match on the "cloud-native architecture + distributed data
systems" side of the JD. The real, un-papered-over gap is the lakehouse table-format/catalog layer
specifically named throughout the JD (Iceberg/Hudi/Delta Lake, Trino, StarRocks) plus Airflow
orchestration — none of these are confirmed skills. Worth going into an interview with a clear,
honest story: strong distributed-systems/GCP fundamentals and a proven track record of learning a
new stack fast (Cysiv's Loggify tool, CIM design), rather than claiming hands-on Iceberg/Trino
experience Kyle doesn't have.
