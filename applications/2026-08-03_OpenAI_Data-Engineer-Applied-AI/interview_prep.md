# Interview Prep — OpenAI, Data Engineer (Applied AI)

## Location / logistics reminder
This role is on-site in San Francisco only (relocation assistance offered) — not remote. Be ready to speak to
relocation timing/logistics directly and confidently if it comes up early in a screen.

## Likely behavioral questions
1. Tell me about a time you built a data pipeline from nothing — walk through how you scoped and sequenced the
   220+ source ingestion work at Trend Micro/Cysiv as a very early hire.
2. Describe a time you had to design a schema or data standard (like your Common Information Model) that other
   teams had to adopt — how did you get buy-in, and what pushback did you get?
3. Tell me about a time a data-quality issue slipped through and impacted downstream analysis or decisions —
   how did you find it, and what did you change afterward?
4. Describe working across many different stakeholder teams (engineering, data science, business) with
   different and sometimes conflicting data needs — how did you prioritize?
5. Tell me about a time you had to retrieve or reprocess a large volume of historical data under real
   constraints (cost, time, or system load) — walk through the Apache Beam/Dataflow cold-storage work.
6. Describe a time you had to make a fault-tolerance or reliability tradeoff in a pipeline you owned — what
   broke, and how did you redesign around it?
7. Tell me about a time you had to learn a new tool or framework quickly to unblock a data engineering project.

## Likely technical questions
1. Walk through how you'd design a pipeline to ingest raw user event data into a warehouse and produce a
   canonical "core table" — how does that compare to the Common Information Model work you did standardizing
   220+ data sources?
2. You've built pipelines with PySpark/SparkSQL on GCP Dataproc — walk through how you'd debug a Spark job that
   is slow or failing at scale. What's your actual process?
3. You have GCP-native distributed processing depth (Dataproc, Dataflow, BigQuery) but no confirmed hands-on
   Airflow/Dagster/Prefect experience — how would you approach picking up a new ETL scheduler quickly, and what
   from your Beam/Dataflow orchestration experience would transfer?
4. Describe the Apache Beam program you built on GCP Dataflow for historical/cold-storage retrieval — batch
   size, failure handling, and how you validated correctness of the retrieved data.
5. How would you design a fault-tolerant ingestion system for high-volume event data where downstream safety
   systems depend on data being both timely and accurate?
6. You have real but exposure-level (not primary-ownership) experience with Flink — what do you understand
   about how it differs from Spark for streaming workloads, and where would you want to ramp up?
7. Walk through your data-quality monitoring/alerting design at DOE/NNSA — how did you decide what to monitor
   and what thresholds triggered alerts?
8. How do you think about data security, integrity, and compliance in a pipeline you own — what's your actual
   practice, not just principle?

## Questions to ask them
1. What does a "canonical dataset" look like in practice here — is this team also responsible for defining the
   metrics themselves, or just building reliable pipelines to data science's/product's spec?
2. How is the data engineering team organized relative to Infrastructure and Data Science — where do the
   ownership boundaries sit day to day?
3. What does the on-call/reliability model look like for pipelines that feed safety systems specifically — is
   there a different bar for those than for product-metrics pipelines?
4. What's the current state of the ETL/orchestration stack (Airflow/Dagster/Prefect or similar) — is the team
   still evolving that tooling, or is it stable and mature?
5. What does the relocation and onboarding timeline typically look like for someone moving to San Francisco for
   this role?

## Salary anchor
Posted band: $230,000 – $385,000 plus equity. Comfortably clears Kyle's $170,000+ floor — anchor to the top
third of the range (~$282,000–$385,000) once fit is confirmed, and don't undersell given how strong this band
is relative to Kyle's floor.

## Closing-the-interview script
"The through-line in my background is building canonical, trustworthy data pipelines from scratch and keeping
them reliable at scale — the 220+ source ingestion and data-dictionary work I did as an early hire at Cysiv is
the same problem this role is solving for OpenAI's product and safety systems, just at a different scale and
mission. I'd love to understand how the team is thinking about the ETL/orchestration stack right now and what
the first 90 days would look like for this role."
