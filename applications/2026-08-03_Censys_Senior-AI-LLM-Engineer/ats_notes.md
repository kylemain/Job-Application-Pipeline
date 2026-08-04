# ATS Coverage & Fit Notes — Censys, Senior AI/LLM Engineer

## Salary check
Standard band: **$148,000 – $192,000 USD base.** HCOL band (San Francisco Bay, NYC, Seattle): **$179,000 –
$201,000 USD.** Plus bonus eligibility and equity.
Kyle's floor is $170,000+. The standard-band bottom ($148,000) sits below floor; the standard-band top
($192,000) clears it, and the entire HCOL band clears it comfortably. Anchor to the top third of whichever band
applies once fit is confirmed (~$178,700–$192,000 standard, or ~$186,300–$201,000 HCOL).

## Fit score: 5/10 (already screened — this package proceeds per that screen)
This posting already passed initial fit screening at 5/10. The honest framing for Kyle's own awareness:

**Real overlap:**
- Domain match is genuine — Censys' SOC/TH team builds AI-powered investigation workflows for analysts and
  threat hunters, which is directly adjacent to Kyle's GenAI-for-security work (prompt engineering for
  detection-content generation and false-positive/false-negative analysis, LLM-driven SIEM API orchestration,
  reusable GenAI-powered tooling for other detection engineers) and his threat-intel-integration work
  (Forescout/Vedere Labs — CTI-informed detection tuning, alert enrichment, investigation support).
- Python is a direct, strong match — core language across Kyle's entire career.
- CI/CD, test automation, and staged/safe rollout discipline are real and confirmed (GitLab detection-as-code
  pipeline with automated tests and rule-quality metrics tracking), though scoped to detection-rule deployment
  rather than AI-application deployment specifically.
- Cross-team collaboration (engineering + SOC/detection stakeholders) is well evidenced across all three
  Shorepoint projects and the Forescout/Cysiv detection-engineering work.

**Real gaps — flagged honestly, not papered over (per Kyle's instruction, not surfaced in the cover letter):**
- **Production RAG-pipeline engineering.** The JD's core ask is developing and fine-tuning LLMs and RAG
  pipelines to reason over internet-scale data, plus vector search and embedding models. Kyle's GenAI work is
  prompt-engineering and orchestration-tooling level (directing LLMs to analyze security data, generate
  detection content, and drive SIEM APIs) — not building/shipping a RAG product with retrieval infrastructure,
  vector search, or embedding-model work. Not claimed anywhere in the resume/cover letter.
- **LangSmith/LangChain-specific tooling and RAGAS regression testing.** The JD explicitly names RAGAS and
  LangSmith for RAG evaluation and regression testing of LLM pipelines. No evidence of hands-on LangSmith,
  LangChain, or RAGAS experience in the master reference — this is a clean gap, not adjacent.
- **Frontend integration / user-facing AI features.** The JD wants 2+ years building and scaling AI-powered
  *user-facing* features, collaboration with frontend teams, and optimizing AI models for low-latency
  real-time interactions in browser/frontend environments. Kyle's GenAI work has been internal tooling for
  detection engineers (backend/workflow automation), not shipped product features with a frontend surface —
  a real, structural gap against this JD's "heavier pure software engineering" ask.
- **LLM fine-tuning.** Not confirmed — Kyle's work is prompt engineering and orchestration against existing
  models, not model fine-tuning.
- This is the same shape of gap flagged during initial fit screening: strong GenAI-for-security domain overlap,
  but the JD's technical center of gravity (production RAG/LLM engineering + frontend integration) is a
  heavier software-engineering lift than Kyle's "GenAI as a tool for detection engineers" background.

## Keyword coverage summary

**Direct matches:**
- Python (backend/API services) — confirmed, core language across entire career
- Prompt engineering improving LLM accuracy/reasoning/consistency — confirmed (false-positive triage,
  detection-content generation)
- CI/CD pipelines, test automation, deployment best practices — confirmed via GitLab detection-as-code
  pipeline (automated tests, staged/safe rollout), though scoped to detection rules not AI apps specifically
- Cross-team collaboration — confirmed across Shorepoint/Forescout/Cysiv detection-engineering work
- Rapid iteration in a fast-paced environment — reasonably inferable from building reusable GenAI tooling and
  a 9-platform SIEM orchestration framework, not a headline-documented claim

**Adjacent/transferable (named honestly, not oversold):**
- "AI-powered automation systems / AI-driven analytics" — Kyle's LLM-driven SIEM API orchestration and
  reusable GenAI-powered detection-engineer tooling are real automation-via-AI experience, framed as
  orchestration/tooling rather than the JD's user-facing AI-feature framing
- Secure/responsible AI practices, guardrails — Kyle's security-domain background gives him real sensitivity
  to this, but no confirmed hands-on guardrail/safety-check implementation for LLM outputs specifically
- Deploying AI in cybersecurity/sensitive-data domains — confirmed the domain (all of Kyle's GenAI work is in
  a security context), but not the JD's specific "user-facing AI feature in production" framing

**Gaps (not claimed anywhere):**
- RAGAS, LangSmith, RAG evaluation/regression-testing frameworks specifically
- Production RAG pipelines, vector search, embedding models, LLM fine-tuning
- Building/scaling AI-powered user-facing features (2+ years specifically) or frontend integration
- Optimizing AI models for low-latency real-time browser/frontend interactions

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, contact info in document body, standard Arial font — passes the formatting rules
in `references/ats-optimization.md`.

## Recommendation
Worth submitting given the already-confirmed 5/10 screen and genuine GenAI-for-security domain overlap, but go
in aware that the interview will likely probe RAG/vector-search/LangSmith specifics and frontend-integration
experience directly — be ready to frame Kyle's background honestly as prompt-engineering/orchestration-tooling
depth rather than shipped-RAG-product-with-frontend depth.
