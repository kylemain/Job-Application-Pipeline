# Interview Prep — Elastic, Principal Security ML Research Engineer

## Likely behavioral questions
1. Tell me about a time you took an ML detection idea from prototype to production — how did you validate it
   before shipping?
2. Describe mentoring a more junior engineer on ML or detection-engineering best practices.
3. Tell me about a time you had to align a research/detection initiative with a product roadmap or
   cross-functional stakeholders.
4. Describe a time your detection work generated too many false positives — how did you diagnose and fix it?
5. Tell me about a time you had to explain a complex ML or security concept to a non-technical audience
   (leadership, customers, SOC analysts).
6. Describe your approach to staying current with the security research community given you don't have a
   traditional publication record — how do you engage with it today?
7. Tell me about a time you had to make a tradeoff between detection accuracy and latency/performance.

## Likely technical questions
1. Walk through the DOE/NNSA UEBA detection layer you built on Elasticsearch transforms — what features fed
   the models, and how did you validate detection quality?
2. This role wants vector search / RAG experience, which isn't strongly represented in your background — how
   would you ramp up on building a RAG-based investigation-assist workflow quickly?
3. You've built clustering-based detection (device behavior clustering) — how would you extend that to
   graph-algorithm-based threat-actor profiling, which the JD also calls for?
4. Walk through how you'd design an evaluation framework and benchmarking pipeline for a new ML detection
   model — what metrics, what test data, how do you catch model drift over time?
5. How would you test a security ML model's robustness against adversarial inputs or prompt injection, given
   you haven't done formal adversarial-robustness auditing before?
6. You have real production LLM-API integration experience (GenAI-driven SIEM orchestration across nine
   platforms) — how does that translate to prototyping "AI agent workflows" for incident investigation
   specifically?
7. Compare Elasticsearch's native detection-rule/ML-job capabilities to what you built by hand at Cysiv (custom
   rules engine) — where does native Elastic Security tooling fall short today, and how would you push on it as
   an insider?
8. You don't have a confirmed publication or conference-speaking record, which is an explicit requirement here
   — be ready to speak candidly about this. Possible honest angle: deep applied/production track record across
   three employers building real detection systems at scale, willingness and interest in writing up and
   presenting this work going forward, and asking what support/expectation Elastic has for building that record
   on the job.

## Questions to ask them
1. How is "Principal" scoped on this team concretely — deep IC research ownership, cross-team technical
   leadership, or both?
2. What does the research-publication/conference-speaking expectation look like in practice — is it something
   built up on the job, or is it treated as a pre-existing bar for candidates?
3. How mature is Elastic's internal vector search / RAG tooling for security use cases today, and where would
   this role plug into that specifically?
4. How does the Threat Research and Detection Engineering team's ML work make it into Elastic Security's
   product (native detection rules, ML jobs, Kibana) versus staying as internal research?
5. What does success look like for this role in the first six months to a year?

## Salary anchor
**Not disclosed in the posting.** Anchor to the $170,000+ floor at minimum; given this is a Principal-level
research-track IC role at a well-funded public company, expect (and aim to negotiate toward) a meaningfully
higher figure once a range is shared — ask for the band directly in the first recruiter conversation rather
than guessing.

## Closing-the-interview script
"I'm genuinely excited about the chance to work on Elastic Security's own ML detection research given how much
of my career has already been built on Elasticsearch — what does the roadmap look like for this team over the
next year, and is there anything about my background, including the research-publication gap, you'd like me to
address directly?"
