# ATS Coverage & Fit Notes — Elastic, Principal Security ML Research Engineer

## Salary check
**Not disclosed in the posting.** No band given anywhere in the JD text. Flagging per the salary-check rule —
Kyle should ask directly in a recruiter screen and anchor to the $170,000+ floor (this is a Principal-level
research-track IC role at a well-funded public company, so realistic expectations are meaningfully above floor,
but there's no posted number to anchor to yet).

## Fit score: 6/10

This is a dream-target **company** for Kyle (per his own watchlist) and the Elasticsearch angle is a genuine,
unusual differentiator — but it's a real stretch at the **Principal research-track** level this specific req is
leveled at, mainly because of the published-research/conference-speaking requirement. Honest breakdown:

**Strong, real matches:**
- **Elasticsearch depth across three employers** (DOE/NNSA SDI built from scratch including the UEBA layer on
  ES transforms; Trend Micro/Cysiv's ES/Kibana-based next-gen SIEM with direct Query DSL and native detection
  rule authorship; CISA CDM at DOE in a combined ES/Splunk environment). This is a massive, unusual
  differentiator specifically for Elastic — very few candidates will have this kind of full-lifecycle,
  cross-employer ES experience (queries, transforms, Logstash, Beats, native detection rules, ES API, Kibana).
- Behavioral anomaly detection in security telemetry — directly confirmed (UEBA layer, time-series anomaly
  detection of auth/process-chain behaviors).
- Clustering/unsupervised ML — directly confirmed (device clustering by network behavior).
- Scalable ML models that reduced false positives while improving detection — directly confirmed (formally
  tracked FP rates, staged/safe rollout, 2,300+ detection rules at Cysiv).
- Evaluation frameworks / benchmarking — adjacent/real: Kyle has formally tracked detection-rule quality
  metrics (coverage, precision/FP rate) and used staged rollout, which maps to "build evaluation frameworks for
  ML model performance" reasonably well, though not framed with the JD's specific "latency benchmarking" or
  "adversarial robustness auditing" language.
- LLM APIs into production — real and directly relevant: GenAI-driven orchestration of SIEM APIs across nine
  platforms, prompt engineering for detection triage/rule generation, GenAI-powered cross-SIEM rule-conversion
  tooling. This is genuine production LLM-integration experience, just not framed as "AI agent workflows for
  incident investigation" specifically (adjacent, not an exact match).

**Real gaps — being honest, not papering over these:**
- **No confirmed published research in security/ML journals or conference presentations.** This is an
  explicitly stated requirement for the role ("Published research... or presented at major security
  conferences") and Kyle has no confirmed publication or speaking record. This is the single biggest gap for a
  *Principal* research-track leveling — have a thoughtful, honest answer ready rather than trying to paper over
  it in the interview.
- **No confirmed hands-on RAG or vector-search experience.** Not claimed anywhere in the master doc — real gap
  against a named required skill.
- **Graph algorithms and xgboost** — not confirmed in the skills inventory; not claimed.
- **Deep learning specifically for security modeling** — PyTorch is confirmed as a framework, but there's no
  confirmed track record of training deep learning models (as opposed to clustering/classical ML) for security
  detection specifically. Framed carefully as "frameworks" rather than claiming deep-learning-model ownership.
- **Adversarial robustness / prompt-injection testing of models** — not confirmed; not claimed.
- **Master's degree "in CS, Cybersecurity, or related field"** — Kyle's M.S. Physics (Numerical Data Analysis &
  Modeling, Applied Physics) is a legitimately related quantitative field and reasonably satisfies "or related
  field," but it is not CS or Cybersecurity specifically — don't overstate this. Combined with the "OR 5+ years
  designing/implementing security ML models" alternate path, Kyle's clustering/anomaly-detection track record
  plus the graduate quantitative background likely clears the baseline bar, but this is a genuine stretch for a
  **Principal**-level research position specifically (vs. a senior IC security ML engineer role), given the
  research-publication expectation baked into the leveling.

## Screening rules check
- **Remote/location:** Elastic is a fully distributed/remote company — no on-site or hybrid flag. Clears the
  remote-only rule cleanly.
- **Federal contracting:** None. This is a private company (Elastic NV, public), not federal contracting work.
  Clears cleanly.
- **Exclusion list:** Elastic is not on the company exclusion list (Sophos, Binary Defense, Shorepoint, Dropzone
  AI). Clears.

## Keyword coverage summary
Roughly **7 of ~18 JD requirement clusters covered directly**, 5 adjacent/transferable, 6 real gaps.

**Direct matches:** Elasticsearch/Elastic Security platform depth (huge differentiator, not explicitly listed
as a keyword but is literally the company's core product), clustering, scikit-learn, PyTorch, behavioral
anomaly detection in security telemetry, guardrails/false-positive minimization, scalable ML models improving
detection while reducing FPs.

**Adjacent/transferable (framed honestly, not overstated):** ML architecture design / AI agent workflows for
investigation (GenAI SIEM orchestration is adjacent, not the same as agentic investigation workflows),
deep learning (PyTorch confirmed as a framework, not a confirmed security deep-learning model track record),
threat actor profiling via ML (real threat-intel integration experience, but not ML-specific actor profiling),
evaluation frameworks/benchmarking pipelines (real detection-quality metric tracking, not framed with the JD's
specific latency/robustness-audit language), Master's-or-5-years baseline (MS Physics + years of ML-adjacent
detection work is a reasonable but real stretch for Principal-level leveling).

**Gaps (not claimed anywhere):** vector search, RAG, graph algorithms, xgboost, adversarial-attack/prompt-
injection robustness testing, published research/conference speaking record.

## Formatting
Single-column, standard section headers (Elasticsearch & Elastic Security Depth / ML & Security Data Science /
Professional Experience / Education & Certifications), no tables/text boxes/icons, Arial throughout, exported
as text-layer PDF via LibreOffice/qpdf.

## Correction (2026-08-02)
The resume summary originally said "11+ years building Elasticsearch-native detection and analytics
platforms..." — this number was wrong on the high side, not just imprecise: per the master reference,
Elasticsearch-specific experience spans three employers (DOE/NNSA, CISA CDM, Trend Micro/Cysiv), all since
Sep 2018 (~8 years), not 11. Corrected to "12 years of security engineering experience, including 8+ years
building Elasticsearch-native detection and analytics platforms..." — 12 is Kyle's real total professional
experience (since Jan 2015, Experian, per the master doc's "Total Years of Experience" note), and 8+ years is
the accurate figure for the Elasticsearch-specific claim. Experian was already present in this resume's work
history — no content was missing, this was a numbers-accuracy fix only. Rebuilt and re-confirmed single-page.
