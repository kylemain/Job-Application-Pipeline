# ATS Notes — OpenAI, Data Engineer, Core Experimentation

Posting: https://jobs.ashbyhq.com/openai/2796d32a-9f7c-4008-a2c5-50dd53b0f2fe
Team: Statsig — OpenAI's internal experimentation platform team (Applied AI department). Builds/operates the
experimentation platform powering product decisions, measurement, and statistical rigor across OpenAI.
Role scope (per full JD, not just the summary): design/build/manage data pipelines feeding the data warehouse,
develop canonical datasets tracking product metrics (growth, engagement, revenue), collaborate across
Infra/Data Science/Product/Marketing/Finance/Research, build fault-tolerant ingestion/processing systems,
participate in data architecture decisions, ensure data security/integrity/compliance.

**Location note:** Posting's location field says "Seattle," Location Type says "Hybrid," but the JD body text
states "This role is based in Bellevue. We use a hybrid work model..." — flagging both figures since they
conflict slightly; either way this is an in-person-hybrid Seattle-area role (Bellevue, WA), not remote.

## Keyword coverage (JD "you might thrive" section = the closest thing to a required-skills list)

| JD keyword/requirement | Coverage | Notes |
|---|---|---|
| 3+ yrs data engineer / 8+ yrs SWE (incl. data eng) | Direct match | Kyle's total professional experience is 12 years (since Jan 2015, Experian). Heaviest data-engineering depth is the Trend Micro/Cysiv era (Sep 2018–Aug 2022: 220+ log source pipelines, CIM design) plus Shorepoint's DOE/NNSA SDI ingestion build. Did not mirror the JD's "3+/8+" minimums back as Kyle's actual tenure — resume/cover letter state the real 12-year total. |
| Python, Scala, or Java (need one) | Direct match | Python confirmed extensively (master doc). Scala/Java: no evidence in master doc — not claimed, and JD only requires one language, which Python satisfies. |
| Spark — write/debug/optimize Spark code | Direct match | PySpark/SparkSQL confirmed at Trend Micro/Cysiv, run on GCP Dataproc clusters for EDA and data loading from cloud storage buckets. |
| Distributed processing — Hadoop | **Gap** | No evidence of Hadoop in master doc. Not claimed anywhere in resume/cover letter. |
| Distributed processing — Flink | Adjacent (exposure-only) | Master doc: "familiar with Kafka and Flink; has worked in an environment that used Flink jobs (not primary ownership/architecture)." Listed in resume as "working exposure to Kafka and Flink streaming jobs" — not overstated as ownership. |
| Distributed storage — HDFS | **Gap** | No evidence in master doc. Not claimed. |
| Distributed storage — S3 | Adjacent | AWS cloud experience is confirmed generally (cloud security/IAM), but no S3-specific data-engineering work is documented in the master doc. Not claimed as S3 pipeline experience. |
| ETL schedulers — Airflow, Dagster, Prefect | **Gap** | None of these are in the master doc's confirmed skills inventory. Not claimed anywhere. This is the most material gap against the JD's explicit "expertise with ETL schedulers" ask. |
| Data pipelines / data warehouse integration | Direct match | 220+ log source ingestion pipelines (Cysiv), BigQuery experience (GCP data warehouse), Apache Beam/GCP Dataflow for large-scale data movement. |
| Canonical datasets / data modeling | Direct match (adjacent framing) | CIM (Common Information Model) work is a direct analog to "canonical dataset" design — a data dictionary standardizing field names/types across all sources — surfaced explicitly in both resume and cover letter. |
| Fault-tolerant ingestion/processing systems | Adjacent | Connector/collector health monitoring and troubleshooting (Cysiv) is the closest documented analog; not a 1:1 match to formal fault-tolerance/reliability-engineering ownership, but a reasonable adjacent claim. |
| Statistical rigor / experimentation methodology (team's actual mission, not a bulleted requirement) | Adjacent | Strong statistics/data-science depth: time-series anomaly detection, unsupervised clustering, EDA at scale, M.S. Physics quantitative background. This is real and relevant to a team that cares about "statistical correctness," but it is security-domain statistics, not formal A/B-testing or causal-inference methodology. |
| Causal inference (mentioned in "About the Team" framing) | **Full gap** | No evidence anywhere in master doc of formal causal inference training/experience. Not claimed. |
| Experimentation-platform-specific tooling (e.g., Statsig itself, or any named A/B-testing framework) | **Full gap** | No evidence in master doc of hands-on experience with any dedicated experimentation platform (Statsig, Optimizely, GrowthBook, etc.). Not claimed. |

## Summary for Kyle
- Strong, honest matches: Spark/PySpark, large-scale data pipeline design (220+ sources), CIM/canonical-data-model design, Apache Beam/GCP Dataflow, GCP Dataproc/BigQuery, Python — this is the real core of the JD's stated day-to-day work.
- Real gaps, not papered over: Airflow/Dagster/Prefect (no confirmed experience with any ETL scheduler), Hadoop, HDFS. Flink is exposure-only, not ownership. None of these are claimed in the resume/cover letter.
- Full gaps: causal inference and any named experimentation-platform tooling (Statsig or equivalent) — this is genuinely new territory for Kyle, not just an adjacent-framing situation. Worth being ready to speak to directly in an interview as "statistics background transfers, platform-specific tooling would be new."
- Location: this is a Seattle/Bellevue hybrid, in-person role — not remote. Already accounted for in the fit score (6/10) per the initial screen; flagging again here for visibility since it's a firm mismatch against Kyle's stated remote-only preference.
