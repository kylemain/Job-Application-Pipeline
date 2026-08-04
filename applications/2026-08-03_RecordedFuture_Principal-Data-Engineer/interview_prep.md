# Interview Prep — Recorded Future, Principal Data Engineer

## Likely behavioral questions
1. Tell me about a time you owned data convergence across multiple disparate systems/data streams —
   walk through the Common Information Model build at Cysiv (220+ sources standardized into one schema)
   as your strongest direct analog to unifying Malicious Sites/Identity/Surface Web data.
2. Describe a time you mentored or brought along less-experienced team members — be ready to speak
   honestly here: real team-lead/sprint-lead experience mentoring detection engineers on rule/pipeline
   design, but no formal people-management title or direct-report headcount. Have a concrete story
   ready (e.g., ramping a peer up on ES transforms or Logstash filter design) rather than overclaiming
   scope.
3. Tell me about a time you had to build something end to end, from data ingestion through to the
   analytics/detection layer stakeholders actually used.
4. Describe a project where you worked across multiple teams or functions to deliver a shared data
   platform capability (JD explicitly calls out working with Malicious Sites, Identity, and Surface Web
   teams).
5. Tell me about a time you had to communicate a technical approach to stakeholders with varying levels
   of technical depth.
6. Describe a data-quality or reliability issue you caught early and how you built monitoring to prevent
   recurrence.
7. Tell me about a time you had to quickly get productive on a new tool or technology you hadn't used
   before (relevant given the MongoDB/graph-database gap).

## Likely technical questions
1. Be ready to answer honestly: "What's your hands-on experience with MongoDB or graph databases like
   Neo4j/Neptune?" Answer directly — no confirmed hands-on experience with either. Pivot to deep,
   cross-employer Elasticsearch experience (queries, transforms, native detection rules, API-level
   cluster work) as the closest analog, and the CIM/schema-standardization work as directly transferable
   data-modeling discipline.
2. Walk through your Elasticsearch experience in technical depth — ES queries/Query DSL, transforms,
   Beats variants, native detection rules, and direct ES API usage (not just Kibana). This is the
   strongest, most concrete part of the story for this role.
3. What's your experience with Kafka or other message buses? Answer honestly — real familiarity and
   hands-on exposure, not 3+ years of primary message-bus ownership/architecture. Be ready to describe
   what that exposure actually looked like.
4. Describe your Apache Beam/GCP Dataflow work for historical/cold-storage data retrieval in detail.
5. What's your experience building or consuming REST APIs in Python? Speak to the SIEM API adapter/
   orchestration work (listing alerts, tables, schemas, managing tokens/roles across many vendor APIs)
   — real API-integration depth, though not confirmed hands-on building APIs with Flask/Django/FastAPI
   specifically.
6. How have you applied AI/LLM approaches in your work? Speak to real, confirmed experience: prompt
   engineering for detection/data-analysis use cases and GenAI-powered tooling built for detection
   engineers — frame honestly as applied tooling, not large-scale LLM productization ownership.
7. Walk through the multi-SIEM detection-as-code orchestration work — API token/role management across
   many platforms, multithreaded parallel rule deployment, CI/CD with staged rollout — strong evidence
   of production-grade pipeline/tooling ownership even outside the ES-specific work.

## Questions to ask them
1. Is there any flexibility on the Boston, MA location, or is this strictly on-site? (The public posting
   has no remote/hybrid language at all — worth confirming directly and early, since Kyle's search is
   remote-only.)
2. What does the current data model/schema look like across the Malicious Sites, Identity, and Surface
   Web systems today — is "data convergence" largely greenfield, or is there significant existing
   integration to reconcile?
3. How is the Intelligence Graph itself built today — what graph database or storage layer backs it,
   and how much of the role is extending that vs. building new ingestion into it?
4. What does "mentor direct reports" look like day to day for this role — is this a formal people-
   management position with headcount, or team/technical leadership without direct reports?
5. What does success look like in the first 90 days for someone joining with strong Elasticsearch/data-
   pipeline fundamentals but less direct MongoDB/graph-database exposure?

## Salary anchor
Posted band is $152,000–$228,500. Given the real gaps (MongoDB, graph databases, message-bus depth
beyond Kafka familiarity, and the location conflict), anchor initial conversations in the top third of
the band (~$205,000–$215,000) once fit is otherwise confirmed strong on the Elasticsearch/data-
engineering fundamentals — don't over-anchor at the very top ($228,500) given the stated gaps, but the
band comfortably clears Kyle's $170K floor either way.

## Closing script
"My strongest, most direct experience lines up with the Elasticsearch and large-scale data-pipeline
core of this role — I've built that exact kind of platform from the ground up before, including the
schema-standardization work a data-convergence project like this needs. I'll be upfront that MongoDB
and graph databases like Neo4j aren't tools I've used hands-on, and my leadership experience has been
team-lead/mentoring rather than formal people management — but I've consistently shown I can get
productive fast on new tooling when the underlying data-engineering problem is the same one I've solved
before. I'd also want to understand the on-site expectations for the Boston location in more detail.
What would the next steps look like from here?"
