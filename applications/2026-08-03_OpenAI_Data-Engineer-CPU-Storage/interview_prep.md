# Interview Prep — OpenAI, Data Engineer, CPU & Storage

Team: Scaling Analytics, Industrial Compute organization. Builds the data/software systems connecting CPU,
storage, capacity, hardware, and infrastructure-software data across internal platforms and vendor systems so
engineering/planning teams can understand and operate infrastructure at global scale.

## Likely behavioral questions
1. Walk me through the Common Information Model you designed at Cysiv — how did you decide on field
   names/types when every source system had its own conventions, and how did you handle a source that didn't
   fit the model cleanly?
2. Tell me about a time a connector or collector silently started dropping or corrupting data — how did you
   find out, and what did you build afterward to catch it sooner next time?
3. Describe a time you had to build an integration against a system you didn't fully understand yet — how did
   you figure out where it should live and how it should connect to everything else?
4. Tell me about onboarding a brand-new data source into an existing pipeline — what was reusable from prior
   sources, and what had to be built fresh?
5. Describe a disagreement with a partner team (e.g., the team that owned a source system) about how a data
   integration should work — how did you resolve it?
6. Tell me about the most fragile piece of infrastructure you've owned — what made it fragile, and what did you
   do to make it more reliable over time?

## Likely technical questions
1. Walk through the Common Information Model design at Cysiv end to end — ingest, parse/normalize, canonical
   schema, and how downstream consumers used it.
2. You built a homegrown Apache Beam program run via GCP Dataflow to pull historical cold-storage data on
   demand — why Beam/Dataflow for that job, and what would you reconsider if you designed it today?
3. Describe your reusable per-technology REST API adapter design for the multi-SIEM orchestration framework —
   how did you handle schema/interface differences across a dozen+ vendor APIs, and how did you decide what was
   common vs. platform-specific?
4. How did you approach data-quality and reconciliation monitoring for the DOE/NNSA ingestion platform — what
   counted as "missing, stale, or inconsistent," and how did alerting work?
5. This role explicitly isn't just "traditional analytical pipelines" — it's deciding whether a new integration
   belongs in an existing service, an orchestration framework, a scheduled workload, or a purpose-built app. How
   would you make that call for a new vendor data source you'd never seen before?
6. Walk through how you'd design data-quality checks to catch a stale or missing feed from a vendor system that
   doesn't tell you when it's broken.
7. You haven't worked directly with Airflow or hardware/fleet-management data — how would you ramp up on
   scheduling/orchestration tooling and hardware-lifecycle data models specifically, given your background in
   adjacent canonical-data-model and pipeline-reliability work?
8. Describe the multithreaded parallel orchestration you built for deploying rules across customers via SIEM
   APIs — what made it safe to parallelize, and what would break if you got that wrong?

## Questions to ask them
1. When new CPU/storage/vendor data sources show up, is the norm to build a dedicated integration per source,
   or is there already a common ingestion/normalization layer new sources plug into?
2. How does the team currently decide where a new integration should live — existing service, orchestration
   framework, scheduled workload, or purpose-built app — and who makes that call?
3. What does "data quality" failure look like in practice for CPU/storage data — stale inventory counts, drift
   between vendor and internal records, something else? How is that currently caught?
4. How much of this role is building new integrations vs. maintaining/hardening the reliability of ones that
   already exist?
5. What does the path from this team's data reaching "reliable and usable" look like for the engineering and
   capacity-planning teams that consume it — what's the current biggest gap?

## Salary anchor
Posted band: $293,000 – $385,000. This clears Kyle's $170,000+ floor comfortably. Anchor to the top third of
the posted range (~$354,000–$385,000) once fit is confirmed — this is a strong band overall, so there's no
reason to anchor lower.

## Closing-the-interview script
"The thread through my whole career has been the same problem this role is solving — pulling reliable,
canonical data out of fragmented, heterogeneous systems so the people who depend on it can trust it. I've done
that for security telemetry across 220+ sources and a dozen-plus vendor APIs; I'd love to bring that same
discipline to CPU and storage data at OpenAI's scale. What are the next steps, and is there anything about my
background you'd want to dig into further before then?"
