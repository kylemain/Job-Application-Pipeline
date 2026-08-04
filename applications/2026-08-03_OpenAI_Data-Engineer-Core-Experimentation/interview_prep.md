# Interview Prep — OpenAI, Data Engineer, Core Experimentation (Statsig team)

## Likely behavioral questions
1. Walk me through building the ingestion pipeline for 220+ log sources at Trend Micro/Cysiv — how did you
   prioritize which sources to onboard first, and how did you handle the long tail of one-off formats?
2. Tell me about designing the Common Information Model (CIM) — how did you decide on a standard schema
   across so many different source formats, and how did you handle sources that didn't fit cleanly?
3. Describe a time a data pipeline broke in production (yours or one you inherited) — how did you find out,
   and what did you change so it wouldn't happen again?
4. Tell me about a time you had to work across teams with different data needs (e.g., detection engineers vs.
   analysts) — how did you reconcile competing requirements into one pipeline/schema?
5. Describe a time you had to make a build-vs-adopt call — like building "Loggify" in-house instead of
   continuing with Logstash. What drove that decision and was it the right one in hindsight?
6. Tell me about a time you used exploratory data analysis to catch a data-quality problem before it became a
   bigger issue downstream.

## Likely technical questions
1. Walk through your Apache Beam / GCP Dataflow pipeline for historical cold-storage retrieval — how did you
   handle backfills, schema drift, and cost/performance tradeoffs at scale?
2. You've used PySpark/SparkSQL on GCP Dataproc — walk through how you'd debug a Spark job that's slow or
   failing on a large dataset. What's your actual process?
3. How would you design a canonical "core tables" layer for a company the size of OpenAI, given your CIM
   design experience — what would you standardize first, and how would you version the schema over time?
4. You haven't used Airflow, Dagster, or Prefect directly — how would you approach ramping up on a
   scheduler-orchestrated pipeline given your background building custom connector/collector health monitoring
   without one?
5. This role emphasizes fault-tolerant ingestion — walk through how you monitored and troubleshot connector/
   collector health at Cysiv, and how you'd extend that thinking to a fault-tolerant event-ingestion pipeline
   for product/experimentation data.
6. You have real time-series anomaly detection and clustering experience, but in a security context, not
   experimentation — how would you translate that statistical background to evaluating whether an A/B test
   result is trustworthy?
7. Given your Kafka/Flink exposure was hands-on-but-not-primary-ownership, how comfortable are you picking up
   deeper Flink/streaming ownership if this role requires it?

## Questions to ask them
1. How much of this role is scheduler/orchestration-framework work (Airflow/Dagster/Prefect) day to day versus
   pipeline/schema design — is the team standardized on one, and how deep does ownership go?
2. What does "canonical dataset" mean concretely on this team — a small number of heavily-governed core
   tables, or a broader catalog? Who owns schema changes once something's canonical?
3. How does the Core Experimentation team think about the line between data engineering and the statistical/
   causal-inference methodology work — are those separate roles, or does this role touch both?
4. What does the hybrid schedule actually look like in practice for this team — how many days in the
   Bellevue office, and how much flexibility is there?
5. What's the biggest current pain point in the data pipelines feeding experimentation results — where does
   this role make the most immediate impact?

## Salary anchor
Posted band: $293,000 – $325,000. Well above Kyle's $170K floor. Anchor to the top third of the posted range
(~$301,700–$325,000) once fit is confirmed and an offer conversation starts.

## Closing-the-interview script
"The core of this role — building reliable ingestion pipelines and canonical data models that other teams can
trust — is exactly what I did building the CIM and 220+ source ingestion pipeline at Cysiv, just applied to
experimentation data instead of security telemetry. I'd love to understand where the biggest gaps are in the
current pipeline architecture and how quickly I could start contributing there."
