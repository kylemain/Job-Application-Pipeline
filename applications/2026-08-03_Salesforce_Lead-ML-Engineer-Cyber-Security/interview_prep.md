# Interview Prep — Salesforce, Lead Machine Learning Engineer - Cyber Security (LMTS)

## Role context
LMTS = Lead Member of Technical Staff, confirmed on the live posting as an IC/technical-track title (Job
Category: Software Engineering), not a people-management title — so no need to defend a lack of formal
management experience here. The role is on Salesforce's Trust Intelligence Platform team, focused on building
scalable ML pipelines across the security engineering org, with heavy emphasis on translating ambiguous threat
problems into production detection systems (anomaly detection, clustering, graph analytics) plus real MLOps
rigor (CI/CD, testing, monitoring) and a "force multiplier"/mentoring expectation.

## Likely behavioral questions
1. Walk me through a time you took a vague, unscoped security problem (not a predefined ticket) and turned it
   into a concrete, shippable model — talk through the DOE/NNSA UEBA build from scratch.
2. Tell me about a time your detection work reduced alert fatigue or improved analyst trust in a model's output
   — what did you change, and how did you know it worked?
3. Describe a time you had to explain a technical/statistical concept to a non-technical stakeholder or
   executive — how did you adjust the explanation without losing the substance?
4. Tell me about mentoring or unblocking a less experienced engineer or analyst, even informally, without
   holding a formal management title.
5. Describe managing competing priorities or stakeholder expectations across more than one team or
   organization — what was the friction, and how did you resolve it?
6. Tell me about a time you had to kill a low-signal detection idea early rather than let it consume engineering
   time — how did you decide, and how did you communicate that decision?
7. Describe a time a model or detection rule you built didn't perform the way you expected in production — what
   did you do?

## Likely technical questions
1. Walk through how you built the unsupervised clustering model for grouping network devices by behavior —
   what features did you use, how did you validate cluster quality, and how did it get consumed downstream by
   detection logic?
2. Walk through your time-series anomaly detection work on authentication behavior — how did you handle
   seasonality/baseline drift, and how did you tune for false positives at scale?
3. You haven't worked directly with graph-based detection models (lateral movement, beaconing via graph
   analytics) — how would you approach ramping up on graph analytics given your statistical/behavioral
   detection background?
4. Your GitLab detection-as-code CI/CD pipeline (automated tests, staged/safe rollout, tracked rule-quality
   metrics) is the closest analog you have to formal MLOps — walk through how that pipeline works, and where you
   think the real differences are between CI/CD for detection rules versus CI/CD for trained ML models.
5. The role calls for hands-on Snowflake, Kafka, and Flink at ownership depth — you've got Spark/PySpark deeply
   and only exposure-level Kafka/Flink and no Snowflake. How would you approach ramping up on that specific
   stack quickly?
6. Walk through the exploratory data analysis workflow you used on GCP Dataproc (Zeppelin, PySpark/SparkSQL) —
   how did that process go from raw log data to a validated detection hypothesis?
7. How would you design a feature store for a security detection use case, given you haven't built one
   previously — what would you want it to guarantee for downstream models?
8. How do you think about ML governance and data security regulation adherence when building detection models
   on sensitive security telemetry?

## Questions to ask them
1. How is the Trust Intelligence Platform team currently splitting its Snowflake/Kafka/Flink stack from the
   Spark/PySpark work — is this greenfield build-out, or is there existing infrastructure to build on top of?
2. What does "force multiplier" actually look like day to day on this team — internal tooling and feature-store
   ownership, direct mentoring, or both?
3. Where is the team on graph-based detection (lateral movement, beaconing) today — early exploration, or
   already in production?
4. What does the path from "rapid prototype" to "production-trusted model the SOC relies on" actually look
   like here — who owns that transition, and how is model performance monitored once it's live?
5. Given the listed locations (San Francisco, Bellevue, Palo Alto), what does the on-site/hybrid expectation
   actually look like in practice — days per week, and is there any flexibility?

## Salary anchor
**Undisclosed on the posting.** No band listed anywhere in the JD. Kyle's floor is $170,000+ — get the band
early (ideally at the recruiter screen) before investing more time, especially given the on-site/hybrid
location trade-off. Anchor any negotiation to the top third of whatever band is eventually disclosed, and don't
volunteer a number first if avoidable.

## Closing-the-interview script
"The core of this role — turning ambiguous threat problems into production-grade anomaly detection and
clustering models the SOC actually trusts — is exactly the work I've been doing for over a decade, most recently
building an unsupervised UEBA layer from scratch for DOE/NNSA and running a CI/CD-disciplined detection pipeline
at scale. I'm genuinely energized by the graph-analytics and MLOps-maturity direction this team is headed, and
I'd love to understand what the next steps look like and where compensation typically lands for this level."
