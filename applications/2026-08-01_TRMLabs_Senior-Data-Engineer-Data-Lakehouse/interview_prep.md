# Interview Prep — TRM Labs, Senior Data Engineer, Data Lakehouse Infrastructure

## Likely behavioral questions
1. Tell me about a time you built a data platform or schema standard from scratch that other teams
   had to rely on — walk through the Common Information Model build at Cysiv as your strongest
   example.
2. Describe a time you had to ramp up quickly on a new tool or technology to stay effective on a
   project (relevant given the Trino/Iceberg/Airflow gap — have a concrete ramp-up story ready, e.g.
   building "Loggify" as a Logstash replacement).
3. Tell me about a data quality or reliability issue you caught before it affected downstream
   consumers, and how you built monitoring/alerting to prevent recurrence.
4. Describe working across teams (data scientists, backend engineers, product) to deliver a data
   platform capability — TRM's JD explicitly calls out cross-department collaboration.
5. Walk through a time you owned a piece of infrastructure end to end — ingestion through
   transformation to the layer stakeholders consumed.
6. Tell me about operating in an early-stage or fast-scaling environment where the platform grew
   substantially while you were building it (Cysiv's growth from internal Trend Micro project to
   independent company is a strong analog to TRM's stated "petabyte scale" growth trajectory).
7. Describe a time you had to make a build-vs-adopt decision on tooling (e.g., Loggify replacing
   Logstash) — how did you evaluate the tradeoff?

## Likely technical questions
1. Be ready to speak directly and honestly to the biggest gap: "What's your hands-on experience with
   Iceberg, Hudi, Delta Lake, or Trino?" Answer honestly — none of these are confirmed hands-on
   experience. Pivot to: deep GCP/Spark/distributed-processing fundamentals, and the CIM/metadata-
   standardization work as directly transferable schema-governance discipline, even though it wasn't
   built on an Iceberg-compatible catalog specifically.
2. Walk through the Common Information Model build at Cysiv in technical detail — this is your
   strongest direct analog to the JD's "metadata management" and "data governance" asks. Be ready to
   describe the actual schema-design decisions, not just the high-level pitch.
3. What's your experience with Airflow or GCP Composer specifically? Answer honestly (GitLab CI/CD
   is the confirmed orchestration experience — staged rollout, automated testing, production
   deployment gating — frame it as adjacent pipeline-orchestration discipline, not Airflow/DAG
   experience).
4. Describe your GCP Dataflow/Apache Beam work in detail — this is a strong, concrete example
   directly relevant to "streaming/batch pipelines using GCP-native services."
5. How would you approach evaluating and adopting Trino or a new query engine you haven't used
   before, given your Spark background? Be honest this is new ground, but use your Loggify-build
   story to show you can get productive on unfamiliar tooling quickly.
6. Walk through how you'd design ingestion and data-quality monitoring for a new large-scale data
   source, using the 220+-source ingestion work at Cysiv as your concrete example.
7. What's your experience with Kafka specifically — depth of usage, not just exposure?

## Questions to ask them
1. How far along is the migration/build toward Iceberg and the GCP lakehouse stack (StarRocks,
   Trino) — is this greenfield, or is there an existing system to migrate off of?
2. What does the Airflow/Composer orchestration layer look like today, and how much of the role is
   building new DAGs vs. maintaining existing ones?
3. How is the data engineering team organized relative to data science and backend engineering — how
   tightly coupled is day-to-day collaboration?
4. What does "petabyte scale" mean concretely for this team today, and what's the growth trajectory
   expected over the next 12-18 months?
5. What does success look like in the first 90 days for someone joining with strong distributed-
   systems/GCP fundamentals but ramping up on Iceberg/Trino specifically?

## Salary anchor
Posted band is $190,000–$220,000 — both figures clear Kyle's $170K floor comfortably. Given real
gaps on the lakehouse-specific tooling (Iceberg/Hudi/Trino/StarRocks/Airflow), anchor initial
conversations around the middle of the band (~$205K) rather than the top, and let strong interview
performance on the fundamentals (GCP, Spark, pipeline ownership, metadata design) make the case for
moving higher — don't over-anchor at $220K given the tooling gap risk.

## Closing script
"I know my hands-on depth is strongest on the GCP/Spark/pipeline-ownership side and lighter on the
specific lakehouse tooling — Iceberg, Trino, Airflow — you're running today. But the underlying
problem you're solving, building one trustworthy, well-governed data platform that scales as new
sources and consumers get added, is exactly what I did from the ground up at my last company. I'd
want to understand what ramp-up support looks like for someone strong on the fundamentals but new to
this specific stack. What are the next steps from here?"
