# Interview Prep — Grow Therapy, Senior Security Engineer, Data Infrastructure

## Likely behavioral questions
1. Walk me through building the Common Information Model at Trend Micro/Cysiv from scratch — how did you
   decide what the schema should look like, and how did you get 220+ source teams/pipelines to actually adopt
   it?
2. Tell me about building DOE/NNSA's Security Data Integration platform from a blank canvas — how did you set
   direction for a year-out vision versus what you built first, and what would you do differently now?
3. Describe a time you had to make a system reliable and trustworthy over time (data-quality monitoring at
   DOE/NNSA or CDM) rather than just functional at launch — what broke, and how did you catch it?
4. Tell me about a time you had to decide between the "secure" way and the "fast" way to ship something — how
   did you make the call, and what was the outcome?
5. Describe managing API tokens, roles, and permissions across a dozen-plus different platforms — how did you
   think about least-privilege as the number of platforms and integrations grew?
6. Tell me about a time you had to influence other teams to adopt a standard (like the CIM schema) that wasn't
   mandatory — how did you get buy-in without authority over those teams?

## Likely technical questions
1. Walk through the CIM/data dictionary you built in detail — what did the schema actually look like, how did
   you version it, and how did downstream systems consume it?
2. This role wants automated classification pipelines that infer sensitivity and propagate tags through data
   lineage. Your CIM work standardized schema, not sensitivity classification — how would you extend that kind
   of thinking to infer and propagate sensitivity tags specifically?
3. You haven't owned field-level masking, tokenization, or redaction directly — how would you approach
   designing that system given your data-pipeline background? What would you build first?
4. You haven't owned application-layer or envelope encryption/key management directly — walk through how you'd
   ramp up on that, and what's the highest-leverage piece you'd tackle first if asked to own it in month one?
5. Describe your GCP Dataflow/Apache Beam program for historical data retrieval — how did you handle schema
   evolution or malformed records at scale?
6. How did you approach IAM policy design in AWS versus GCP — what's genuinely different between the two, and
   how did you decide on the boundary between roles?
7. Walk through the data-quality monitoring/alerting you built at DOE/NNSA — how did you decide what "bad data"
   looked like, and how did you avoid alert fatigue?
8. How would you design an automated pipeline that scans production data models and infers sensitivity without
   human tagging for every field — what signals would you use?

## Questions to ask them
1. How mature is the current Data Classification Policy — is this role writing that policy from scratch, or
   building automation against an already-defined framework?
2. What does "secure by default" look like today versus where you want it in a year — is the gap mostly
   tooling, mostly adoption, or both?
3. How is this role scoped relative to the rest of the security team — is encryption/key management, masking,
   classification, and AI-data-path security genuinely one person's remit, or split across a small team?
4. What AI tools is Grow currently connecting to production data, and what does the current security posture
   for those connectors look like today?
5. How do Data, Engineering, and Detection & Response currently collaborate with Security on data
   infrastructure — where does friction show up most?

## Salary anchor
Two disclosed bands: Hybrid $182K–$250K, Fully Remote $152K–$208K. Kyle is remote-only — anchor within the
**remote band's top third, roughly $195,000–$208,000**, once fit is confirmed. Do not let the higher hybrid
number pull the conversation toward an on-site commitment; the remote band's midpoint (~$180K) already clears
Kyle's $170K floor, so there's no salary reason to consider hybrid.

## Closing-the-interview script
"What excites me about this role is that it's building the same kind of executable, schema-first data
infrastructure I built from scratch at Cysiv — just applied to sensitivity classification and access control
instead of ingestion normalization. I'd love to understand where the team is furthest along today —
classification, masking, encryption, or the AI-data-path piece — so I know where I could have impact fastest."
