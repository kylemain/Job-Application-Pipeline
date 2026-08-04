# Interview Prep — Upstart, Senior Security Engineer, Data Security

## Likely behavioral questions
1. Walk me through building DOE/NNSA's Security Data Integration platform from scratch — how did you decide
   what to build first, and how did you get cross-functional buy-in along the way?
2. Tell me about a time you had to push a least-privilege access model through when it created friction with a
   team that wanted broader/faster access — how did you make the tradeoff?
3. Describe mentoring or bringing another engineer up to speed on the multi-SIEM orchestration framework — what
   worked, what didn't?
4. Tell me about a time operational feedback (false positives, an access request pattern, a broken pipeline)
   forced you to redesign something you'd already built — what changed and why?
5. Describe a time you had to influence a non-technical stakeholder (compliance, legal, or business ops) to
   adopt a security control — how did you frame the ask?
6. Tell me about navigating ambiguity — a project where the scope wasn't clearly defined and you had to decide
   the direction yourself.
7. Describe a time you disagreed with a security tradeoff decision made by someone senior to you — what did you
   do?

## Likely technical questions
1. Walk through how you designed and implemented IAM policies/roles in AWS and GCP — what did your
   least-privilege model actually look like in practice, and how did you handle exceptions?
2. Describe how you created and governed API tokens, roles, and permissions across a dozen-plus SIEM platforms
   — how did you think about scoping, rotation, and periodic access review?
3. This role wants software engineering — APIs, services, internal tools — not just access-control policy. Walk
   through the most "software engineering" thing you've built (the GitLab CI/CD detection-as-code pipeline, or
   the per-platform API adapters) and be ready to go deep on the code/architecture, not just the outcome.
4. You haven't owned a DLP or DSPM initiative directly — how would you approach ramping up on data
   classification/posture-management concepts (BigID/Concentric/Varonis/Cyera-style tooling) given your
   access-governance and data-pipeline background?
5. Walk through the Common Information Model you built at Trend Micro/Cysiv — how would that kind of schema
   standardization work translate to classifying sensitive data (PII, financial, credit data) across Upstart's
   systems?
6. How would you design a system to detect and alert on overly broad access to sensitive data — what would you
   instrument, and what would trigger an alert?
7. Describe your approach to testing and safely rolling out a change to an access-control or detection system in
   production — walk through your actual staged-rollout/automated-testing practice.
8. How do you approach securing data across genuinely different domains (security telemetry vs. analytics vs.
   HR/people data) — where does a single access-governance framework hold up, and where would it break down?

## Questions to ask them
1. How mature is the data security program today — is this role building the first version of DLP/DSPM
   tooling, or maturing something that already exists?
2. What does "building software solutions — APIs, services, internal tools" look like concretely in this role
   day to day — is the team shipping a homegrown data-classification/DSPM platform, integrating a vendor tool
   (BigID/Concentric/Varonis/Cyera), or both?
3. How is success measured for this role in the first 6-12 months — what does "0 to 1" actually look like as a
   deliverable?
4. How does the security team currently partner with Engineering, Analytics, Product, Legal, Risk, and HR on
   data protection — is there an existing forum/process, or is part of this role's job to create one?
5. What's the current state of least-privilege access across the data estate — is this greenfield, or is there
   an existing access model this role would be refining?

## Salary anchor
Posted band: $164,800 – $228,400 (Remote - US). Midpoint ≈ $196,600, clears Kyle's $170K+ floor comfortably.
Anchor to the top third of the range (~$213,900–$228,400) once fit is confirmed.

## Closing-the-interview script
"The thread running through my background — Cloud IAM, API-level access governance across a dozen-plus
platforms, and hands-on data pipeline engineering at scale — is exactly the kind of technical foundation this
role needs to turn least-privilege from a principle into a working system. I'd love to understand where the
data security program is today and what the first 90 days of this role would actually look like."
