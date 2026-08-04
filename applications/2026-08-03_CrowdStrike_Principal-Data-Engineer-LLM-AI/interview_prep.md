# Interview Prep — CrowdStrike, Principal Data Engineer, LLM/AI Platforms

## Likely behavioral questions
1. Walk me through building the DOE/NNSA Security Data Integration platform from scratch — how did you
   decide what to build first, and what would you do differently knowing what you know now?
2. Tell me about a time you had to mentor or bring another engineer up to speed on a complex system you
   built (e.g., the Common Information Model or the multi-SIEM detection-as-code pipeline) — how did you
   approach it?
3. Describe a time you had to ship something fast without compromising quality — what tradeoffs did you make,
   and how did your CI/CD/testing discipline protect you?
4. Tell me about a time a data-quality or pipeline-health problem surfaced in production — how did you find
   it, and what did you change to keep it from recurring?
5. Describe working cross-functionally with non-engineers (SOC analysts, DOE stakeholders) to turn a rough
   requirement into a production data pipeline.
6. Tell me about a time you had to learn a new tool or platform quickly to unblock a project — how did you
   approach the ramp-up?
7. Walk me through a technical decision you made that you later had to revisit or reverse — what did you
   learn?

## Likely technical questions
1. Walk through the Common Information Model you built at Cysiv — how did you decide on schema/normalization
   rules across 220+ heterogeneous sources, and how would that translate to semantic cataloging for LLM/RAG
   data?
2. Describe your GitLab CI/CD pipeline for detection-as-code in detail — how do automated testing and
   staged/safe rollout work together to catch a bad deployment before it reaches production?
3. You've used prompt engineering and GenAI tooling in production security workflows, but the JD wants
   hands-on LLM fine-tuning, RAG, and agentic workflow engineering (LangChain/LlamaIndex) — how would you
   approach ramping up on that gap, and what from your background transfers directly?
4. Walk through the Apache Beam/GCP Dataflow program you built for historical/cold-storage retrieval — how
   did you handle scale, failure recovery, and cost tradeoffs?
5. You've worked within a Kubernetes-orchestrated platform as a user but haven't administered a cluster
   directly — how comfortable would you be picking up container-orchestration ownership, and what adjacent
   experience (Docker, CI/CD) would you lean on?
6. How would you design a data pipeline/platform to support Retrieval-Augmented Generation at Exabyte scale,
   drawing on your experience designing the Common Information Model and large-scale ingestion architecture?
7. Describe your experience with Spark/PySpark at scale — how does that compare to what you understand about
   Dask or Flink, and how would you approach picking up whichever this team standardizes on?
8. What does "data-quality monitoring and alerting" look like in your systems — walk through how you'd apply
   that discipline to monitoring an LLM/agentic pipeline (as opposed to a log-ingestion pipeline).

## Questions to ask them
1. How much of this role is building new LLM/RAG data infrastructure from scratch versus operating and
   scaling what already exists on the Data Science Platform Engineering team?
2. What does "agent harnessing" mean concretely on this team today — what frameworks or in-house tooling are
   in production right now?
3. How is work split between platform/infrastructure ownership (Spark, Kafka, Kubernetes) and closer-to-model
   work (RAG, fine-tuning, agentic workflows) — is this one role wearing both hats, or a team with some
   specialization?
4. What does the path from research prototype to production service actually look like on this team — who
   owns that handoff?
5. Given the emphasis on mentorship and technical leadership in the JD, what does success in the first six
   months look like for whoever fills this role?

## Salary anchor
Posted band (US): $195,000 – $290,000 base (Canada: $210,000 – $320,000 CAD). Both comfortably clear Kyle's
$170,000+ floor. Anchor to the top third of the US band (~$258,000–$290,000) once fit is confirmed — this
role is a stretch on the LLM-platform-engineering specifics, so be prepared to let demonstrated data-
engineering depth and CI/CD discipline do the anchoring rather than overclaiming platform-engineering
seniority.

## Closing-the-interview script
"The data-platform discipline underneath this role — ingestion architecture, schema/metadata standardization,
and shipping through a tested, staged CI/CD pipeline — is exactly what I've spent 12 years building, most
recently with GenAI tooling layered directly into production workflows. I'm genuinely excited to go deeper on
the LLM/RAG/agentic engineering side of this role, and I'd love to understand where the team is furthest
along today so I know where to focus first."
