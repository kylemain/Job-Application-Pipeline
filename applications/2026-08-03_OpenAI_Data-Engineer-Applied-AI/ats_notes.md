# ATS Coverage & Fit Notes — OpenAI, Data Engineer (Applied AI)

## Location flag — read this first
**This role is exclusively based at OpenAI's San Francisco HQ — not remote, not hybrid.** The JD states plainly:
"This role is exclusively based in our San Francisco HQ. We offer relocation assistance to new employees."
Per the master reference, Kyle's default screening preference is fully remote roles, and on-site/relocation
postings are flagged rather than built by default. This posting was pre-screened and passed (fit score 6/10)
with this location explicitly known and accepted — Kyle has said he's open to relocating for the right role.
Flagging again here for visibility before any submission decision: this is a hard on-site requirement in San
Francisco, with employer-provided relocation assistance, not a remote or hybrid arrangement.

## Salary check
Posted band: **$230,000 – $385,000 USD base, plus equity.** Comfortably clears Kyle's $170,000+ floor by a wide
margin — this is one of the strongest disclosed bands seen in the pipeline. Anchor negotiation to the top third
(~$282,000–$385,000) once fit is confirmed.

## Keyword coverage summary

**Direct matches:**
- Python — confirmed, core language
- SQL — confirmed
- Spark / "solid understanding of Spark, ability to write, debug, and optimize Spark code" — confirmed via
  PySpark/SparkSQL work at Trend Micro/Cysiv (GCP Dataproc clusters, Zeppelin notebooks, Spark jobs loading data
  from cloud storage buckets)
- Distributed processing / cloud storage — confirmed via GCP Dataproc, GCS bucket-based Spark jobs, and Apache
  Beam on GCP Dataflow for historical/cold-storage data retrieval
- Data pipeline design/ownership at scale — confirmed directly: 220+ unique data source ingestion pipelines
  built from scratch as an early startup hire (Trend Micro/Cysiv)
- "Canonical datasets" — strong direct match: Kyle's Common Information Model (CIM) work is literally a
  canonical-schema/data-dictionary design and standardization effort across every pipeline, the same concept
  the JD names explicitly
- Data quality / data integrity monitoring — confirmed via data-quality monitoring/alerting content built at
  both Trend Micro/Cysiv and Shorepoint (DOE/NNSA SDI, CISA CDM)
- Cross-team collaboration with many stakeholder groups — confirmed pattern (worked across engineering,
  data science, and business-facing teams throughout career)
- 3+ years as a data engineer, 8+ years total software/data engineering — Kyle's real total is **12 years**
  (since Jan 2015, Experian), with dedicated data-engineering ownership concentrated in the Trend Micro/Cysiv
  (2018–2022) and Shorepoint (2023–present) roles. This comfortably clears both JD minimums; the JD's stated
  minimums are not mirrored back as Kyle's actual tenure anywhere in the resume/cover letter.

**Adjacent/transferable (named honestly, not oversold):**
- Distributed storage systems (JD names S3/HDFS specifically) — Kyle's confirmed cloud-storage experience is
  GCS (Google Cloud Storage) bucket-based Spark jobs, plus general AWS platform experience. Not the same named
  systems as the JD lists, but the same conceptual pattern (cloud object storage feeding distributed compute).
  Framed as GCP-based cloud storage experience, not claimed as direct S3/HDFS ownership.
- Kafka/Flink exposure — master reference confirms Kyle has "worked in an environment that used Flink jobs, not
  primary ownership/architecture of the Flink deployment, but real hands-on exposure," alongside Kafka
  familiarity. Surfaced on the resume as "working exposure ... in a production streaming environment" — not
  framed as primary Flink ownership or deep streaming-architecture expertise, since that's not confirmed.

**Real gaps (not claimed anywhere on the resume or in the cover letter):**
- **Hadoop** — not confirmed anywhere in Kyle's skills inventory. His distributed big-data work is GCP-native
  (Dataproc/Dataflow/BigQuery), not Hadoop/HDFS-specific. Genuine gap.
- **Airflow / Dagster / Prefect (ETL schedulers)** — none of these are confirmed in the master reference. Kyle's
  pipeline orchestration experience is real (detection-as-code CI/CD via GitLab, homegrown Apache Beam jobs) but
  not the same as hands-on ownership of a dedicated ETL scheduler like Airflow. Genuine gap, not papered over.
- **Scala or Java** — the JD lists Python, Scala, or Java as acceptable languages; Kyle's confirmed programming
  languages are Python, SQL, and R. No confirmed Scala/Java experience. Not claimed.

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications), no
tables/text boxes/icons, contact info in the document body (not header/footer) — passes the formatting rules in
`references/ats-optimization.md`.

## Recommendation
Materials built as directed (posting already fit-screened and passed at 6/10). Genuine gaps worth having ready
answers for if this reaches a technical screen: no hands-on Airflow/Dagster/Prefect experience, no Hadoop-
specific experience, and Flink/Kafka exposure is real but not primary ownership. Kyle's Spark, GCP-native
distributed processing, and — especially — the canonical-dataset/data-dictionary (CIM) experience are strong,
directly relevant proof points for this specific req.
