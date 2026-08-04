# Interview Prep — Amazon, Data Scientist, AWS Security

## Likely behavioral questions
1. Tell me about a time you built a detection model from scratch with no existing infrastructure to lean on —
   walk through the DOE/NNSA Security Data Integration build and how you decided what to build first.
2. Amazon leadership principles show up hard in DS interviews — give an example of "Deliver Results" from your
   work building the 2,300+ detection rules at Trend Micro/Cysiv as a very early hire.
3. Tell me about a time a statistical or ML-based detection model you built generated too many false positives
   — how did you find out, and what did you change?
4. Describe a time you had to "disagree and commit" — pushed back on an approach to a detection or data
   pipeline, lost the argument, and executed anyway.
5. Tell me about translating a complex analytical finding into something a non-technical stakeholder (a SOC
   analyst, a customer) could act on quickly.
6. Describe a time you had to learn a new tool or platform quickly to keep a project moving (e.g., adapting
   GCP Dataproc/PySpark workflows to a new data source or scale requirement).
7. Tell me about a time you owned something end-to-end with ambiguous requirements — the DOE/NNSA SDI build is
   a strong example (built the ingestion, the UEBA layer, and the dashboards with no existing template).

## Likely technical questions
1. Walk through how you built the unsupervised clustering model to group network devices by behavioral
   feature — what features did you choose, how did you validate the clusters were meaningful, and how did that
   feed into detection?
2. Walk through your time-series anomaly detection work on authentication behavior (volume/attempts by
   country) — what did the actual modeling approach look like, and how did you set thresholds to avoid
   drowning analysts in noise?
3. Describe your exploratory data analysis workflow on GCP Dataproc/PySpark/SparkSQL at scale — how would that
   translate to AWS EMR/SageMaker if the underlying big-data tooling changed but the modeling problem didn't?
4. You haven't used AWS SageMaker or EMR directly — how would you ramp up on AWS-native ML tooling given your
   GCP-equivalent depth (Dataproc, Dataflow, BigQuery)?
5. Walk through the UEBA detection layer you built at DOE/NNSA — what did the data transforms look like, and
   how did you decide what "anomalous" meant statistically for that environment?
6. Describe your hands-on GenAI/prompt-engineering work for security — how did you use GenAI for false-positive
   triage and detection-rule generation, and what would it take to extend that into a formal LLM agent
   pipeline?
7. How would you design an experiment to assess the risk of a proposed automated security response before it
   goes to production — draw on your staged/safe-rollout and rule-quality-metrics experience from the
   multi-SIEM detection-as-code pipeline.
8. Walk through the data engineering behind your 220+ log-source pipeline (Logstash filters, Common Information
   Model) — how would you approach standardizing a new, messy data source at AWS's scale?

## Questions to ask them
1. How much of the team's current ML workflow runs through SageMaker/EMR versus other tooling, and what does
   the split look like between building new models and maintaining/tuning existing ones?
2. What does "expanding the LLM agent pipelines" actually look like right now — is this early-stage
   experimentation or are agents already in production making or recommending real security decisions?
3. How is success measured for a model here — is it precision/recall against labeled incidents, downstream
   analyst time saved, or something else?
4. What does the on-call rotation actually look like in practice — what's a typical page, and how often is it
   a real incident versus noise?
5. Since the team is distributed across MD/VA with some flexibility, how does that work for someone fully
   remote outside that area day to day — is there an expectation of periodic travel or overlap hours beyond the
   stated 10am–3pm EST core?

## Salary anchor
Posted band: **$136,000 – $184,000.** Kyle's floor is $170,000+, and the midpoint (~$160,000) sits below that
floor — this is a real gap, not a rounding issue. Do not anchor low. Anchor to the top of the posted band
(~$180,000–$184,000) once fit is confirmed, and treat the conversation about level/banding as something to
raise early rather than after an offer is drafted, since even the top of the range only clears Kyle's floor by
a small margin.

## Closing-the-interview script
"The anomaly detection and statistical modeling work I've done — clustering devices by behavior, time-series
detection on authentication and process activity, and more recently building a UEBA layer from scratch at
DOE/NNSA — is exactly the kind of large-scale pattern-recognition work this role is built around, just applied
to a different infrastructure. I'd love to understand where the SageMaker/EMR tooling and the LLM agent work
sit today, and what the next steps look like."
