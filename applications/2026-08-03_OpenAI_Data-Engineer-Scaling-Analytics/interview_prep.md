# Interview Prep — OpenAI, Data Engineer, Scaling Analytics

## Likely behavioral questions
1. Walk me through building the Common Information Model at Trend Micro/Cysiv — how did you decide what to
   standardize across 220+ sources, and how did you keep it maintainable as new sources kept getting added?
2. This role means stepping into a domain you haven't worked in before (hardware operations, capacity
   planning, supply chain) — tell me about a time you had to build something in an unfamiliar domain and how
   you ramped up quickly.
3. Tell me about a time a data-quality issue slipped through and reached a downstream consumer of your
   pipeline — what happened, and what did you change afterward?
4. Describe a time you had to translate a non-technical stakeholder's ask (someone outside your own team) into
   a concrete data engineering solution.
5. Tell me about a time you were the primary or sole data engineer on a fast-moving team — how did you
   prioritize what to build first, and what tradeoffs did you make?
6. Describe a time you had to make a build-vs-buy call on a data tool (e.g., building "Loggify" instead of
   continuing with Logstash) — how did you make that call, and was it the right one in hindsight?
7. Walk through a time you built a dashboard or reporting output that changed how a team or leadership made a
   decision — how did you figure out what metrics actually mattered to them?

## Likely technical questions
1. Walk through the Common Information Model in detail — how did you handle schema evolution when a new
   source needed a field that didn't fit the existing dictionary?
2. You haven't used Snowflake or Redshift — how would you map your BigQuery/GCP Dataproc experience onto a
   Snowflake- or Redshift-centric warehouse, and what would you expect to be different?
3. You haven't owned a DAG-based scheduler like Airflow or Dagster — walk through how your GitLab CI/CD
   pipeline handled scheduling, dependency management, and failure alerting for detection content, and how
   that maps (or doesn't) onto a proper DAG-based orchestration tool.
4. Walk through the homegrown Apache Beam program on GCP Dataflow — why Beam/Dataflow instead of a more
   standard batch scheduler, and how did you handle failure/retry logic for large data-retrieval jobs?
5. How would you design a canonical dataset from scratch — e.g., a "hardware asset" or "site" dataset — given
   multiple upstream systems of record with inconsistent identifiers? Walk through your actual CIM design
   process as the template.
6. Describe your PySpark/SparkSQL work on GCP Dataproc — what's the largest dataset you've processed, and what
   performance/tuning issues did you run into?
7. How do you think about data-quality checks and observability in a production pipeline — walk through a
   specific alerting/monitoring setup you built and what it caught.
8. You haven't used dbt — how would you approach adopting a transformation framework like dbt given your
   existing ETL/normalization background (Logstash filters, CIM design)?

## Questions to ask them
1. Today, expertise on the team is concentrated in a few specialized domains (hardware health, GPU
   attribution, supply analytics) — which of those would this role touch first, and how much ramp-up time is
   built in for someone new to the domain?
2. What does the current data stack look like end-to-end — warehouse, orchestration, transformation layer —
   and how much of it is this hire expected to help mature versus operate as-is?
3. How is work divided between Scaling Analytics and the Hardware Operations, Capacity Planning, and Supply
   Chain teams it partners with — where does this role's data ownership start and stop?
4. As Stargate brings new sites online, how does the team decide which new data sources/problem spaces to take
   on first, and who makes that call?
5. What does success look like in the first 90 days for this role, given the team is trying to reduce
   operational bottlenecks and expand depth across critical infrastructure analytics functions?

## Salary anchor
Posted band: $293,000 – $385,000, plus equity. Comfortably clears Kyle's $170,000+ floor. Anchor to the top
third (~$362,000–$385,000) once fit is confirmed.

## Closing-the-interview script
"Every role I've had has come down to the same core problem: take fragmented, high-volume operational data
and turn it into pipelines and canonical datasets people can actually trust for decisions — whether that's
220+ log sources at Cysiv or a new ingestion platform I built from scratch at Shorepoint. I'd love to bring
that same discipline to Scaling Analytics as OpenAI's infrastructure footprint keeps growing. What would you
want to see from me in the first few months to know this was the right hire?"
