# Interview Prep — OpenAI, Data Engineer, People Innovation Labs

## Likely behavioral questions
1. Walk me through building the Common Information Model at Trend Micro/Cysiv — how did you decide what
   fields/schema to standardize across 220+ sources, and how did you get buy-in from teams already using the
   old, inconsistent schemas?
2. Tell me about a time you were the only (or primary) data engineer on a team — how did you prioritize what
   to build first, and what tradeoffs did you make under that constraint?
3. Describe a time a data-quality issue slipped through and reached a downstream consumer of your pipeline —
   what happened, and what did you change afterward?
4. This role means working with People Analytics and Compensation/Equity stakeholders who likely aren't
   deeply technical — tell me about a time you translated a non-technical stakeholder's ask into a concrete
   data engineering solution.
5. Tell me about a time you had to build something in a domain you had zero prior experience in (a fair
   parallel to moving from security data into HR/people data) — how did you ramp up quickly?
6. Describe a time you had to make a build-vs-buy call on a data tool (e.g., the decision to build "Loggify"
   instead of continuing with Logstash) — how did you make that call and was it the right one in hindsight?

## Likely technical questions
1. Walk through the Common Information Model in detail — how did you handle schema evolution when a new
   source needed a field that didn't fit the existing dictionary?
2. Walk through the homegrown Apache Beam program on GCP Dataflow — why Beam/Dataflow instead of a more
   standard scheduler, and how did you handle failure/retry logic for historical/cold-storage retrieval jobs?
3. You haven't used Databricks or Snowflake specifically — how would you map your GCP Dataproc/BigQuery
   experience onto a Databricks-centric warehouse, and what would you expect to be different?
4. You haven't owned a dedicated ETL scheduler (Airflow/Dagster/Prefect/Fivetran) — walk through how your
   GitLab CI/CD pipeline handled scheduling, dependency management, and failure alerting for detection content,
   and how that maps (or doesn't) onto a proper DAG-based scheduler.
5. How would you design a canonical "employee" or "candidate" dataset from scratch, given multiple upstream
   systems of record with inconsistent identifiers — walk through your actual CIM design process as the
   template.
6. Describe your PySpark/SparkSQL work on GCP Dataproc — what's the largest dataset you've processed, and
   what performance/tuning issues did you run into?
7. How do you think about data security, integrity, and compliance for people/HR data specifically, given your
   background is mostly securing security telemetry rather than employee PII?

## Questions to ask them
1. What does the current state of the Databricks warehouse and People Analytics data model look like today —
   greenfield, or is there existing technical debt I'd be inheriting?
2. How is work split between this role and the Data Platform / Data Science teams mentioned in the JD — where
   does People Innovation Labs' data engineering ownership start and stop?
3. OpenHouse sounds like a 0-to-1 product — how much of the data architecture is already decided versus still
   open for this hire to shape?
4. What does success look like in the first 90 days for this role, given it's described as "the primary data
   engineering expert" on the team?
5. How does the team think about the sensitivity of people data (compensation, performance, personal
   information) differently from typical product analytics data?

## Salary anchor
Posted band: $293,000 – $325,000, plus equity. Comfortably clears Kyle's $170,000+ floor. Anchor to the top
third (~$317,000–$325,000) once fit is confirmed.

## Closing-the-interview script
"Building a canonical data model from a standing start — figuring out the schema, getting buy-in from teams
already using inconsistent data, and making sure it holds up as new sources get added — is exactly what I did
building the Common Information Model at Cysiv. I'd love to bring that same approach to OpenHouse and the
People Analytics team's data platform, and I'm excited about what it'd look like to apply that discipline to a
completely new domain. What are the next steps from here?"
