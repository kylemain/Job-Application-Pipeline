# Interview Prep — Anthropic, Data Engineer, Safeguards

## Likely behavioral questions
1. Walk me through building DOE/NNSA's Security Data Integration platform from scratch — how did you decide
   what to ingest first, and what would you do differently knowing what you know now?
2. Tell me about a time a data-quality issue in a pipeline you owned went undetected for a while — how did you
   find it, and what did you change about your monitoring/alerting afterward?
3. Describe working with non-technical stakeholders who needed to understand what your data showed (e.g.,
   dashboards for SOC analysts or leadership) — how did you translate the complexity down?
4. Tell me about a time you had to pick up work outside your immediate scope because the situation called for
   it — the JD explicitly values this.
5. Describe a time you had to make a call about what data to standardize/model first when you had more sources
   than time (relevant to the Common Information Model work at Trend Micro/Cysiv).
6. Tell me about a disagreement with an engineer or data scientist about how a dataset should be modeled or
   partitioned — how did you resolve it?
7. Why do you want to work on AI safety specifically, versus staying in traditional cybersecurity detection
   engineering? (Be ready with a genuine answer — this is an explicit application-form question at Anthropic.)

## Likely technical questions
1. Walk through the Common Information Model you built at Trend Micro/Cysiv — how did you decide on field
   names/types across 220+ heterogeneous sources, and how did you handle schema drift over time?
2. Describe the Apache Beam/GCP Dataflow program you built for historical cold-storage retrieval — what made
   Beam/Dataflow the right choice over a simpler batch job, and how did you handle scale?
3. This role wants dbt/Airflow experience — you haven't used either directly. Walk through how your Logstash
   filter pipeline and CIM design map onto what dbt does conceptually (transform + test + document), and how
   fast you could ramp on the actual tool.
4. How would you design a data pipeline that ingests model outputs, user reports, and automated classifier
   results into one unified analytical layer — walk through your approach given your CIM/data-dictionary
   design experience.
5. You've used BigQuery/Dataproc/Dataflow on GCP — how would that experience transfer if this team's warehouse
   is Snowflake or Redshift instead?
6. Walk through how you'd design a data-quality monitoring and alerting framework for safety-critical data,
   drawing on what you built for the DOE/NNSA data-quality alerting content.
7. Your dashboarding experience is in Kibana, not Looker/Tableau/Metabase — what's your approach to picking up
   a new BI tool quickly, and what do you actually need from a dashboarding tool regardless of vendor?
8. Describe how you integrated threat intelligence into detection rule logic at Cysiv/Forescout — how would
   that same "external signal enrichment" pattern apply to enriching abuse-detection data with policy or
   classifier context?

## Questions to ask them
1. How is the Safeguards data team currently structured — is there dedicated data engineering ownership
   separate from the data scientists and policy teams, or is it more blended?
2. What does the current data stack actually look like end-to-end (warehouse, orchestration, transformation,
   BI layer) — the JD lists "such as" examples, so I'd like to know what's actually in production.
3. How mature is the data-quality/monitoring practice today — is this a build-from-scratch opportunity like my
   DOE/NNSA platform work, or is it more about scaling something that already exists?
4. How does the Safeguards team measure whether a safety intervention actually worked — what does that
   feedback loop from data back to model/policy changes look like in practice?
5. What's the split between building new pipelines/infrastructure versus maintaining and optimizing what
   already exists for this specific role?

## Salary anchor
Posted band: $320,000 – $405,000 annual salary. Comfortably clears Kyle's $170,000+ floor at every point.
Anchor to the top third (~$373,300–$405,000) once fit is confirmed — this band gives real room to negotiate
from strength given the 12 years of directly relevant pipeline/data-engineering depth.

## Closing-the-interview script
"The data engineering work I've done — standardizing schema across 220+ sources, building retrieval pipelines
on Apache Beam and Dataflow, and layering detection and data-quality monitoring on top of all of it — is exactly
the kind of foundation Safeguards needs to trust its data. I'm genuinely motivated by applying that to AI safety
specifically rather than traditional security. What are the next steps, and is there anything in my background
you'd like me to go deeper on before then?"
