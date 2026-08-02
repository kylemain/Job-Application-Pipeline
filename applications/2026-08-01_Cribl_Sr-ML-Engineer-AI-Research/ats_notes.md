# ATS Coverage & Fit Notes — Cribl, Sr Machine Learning Engineer, AI Research

## Salary check
Disclosed band: **$185,000 – $215,000 USD base**. Both ends clear Kyle's $170K floor comfortably —
no flag needed. Anchor negotiation to the top third of the band (~$205K–$215K) once fit is confirmed.

## Fit score: 6/10 (honest, not a cheerleading score)

**Why it's a real candidate, not just a keyword match:**
- **Cribl pipeline experience is a genuine, rare differentiator.** Kyle has confirmed hands-on experience
  creating and managing Cribl pipelines directly (master doc, not currently on his public resume). For a
  role building AI/ML features *into the Cribl product itself*, direct fluency with the product is a real
  edge over candidates with only generic ML backgrounds — this is the strongest single point in his favor
  and is surfaced prominently (resume skills section + cover letter opening line).
- **12 years total experience** (since Experian, Jan 2015) comfortably clears the JD's 4+ year bar.
- **M.S. Physics (numerical data analysis/modeling)** satisfies the "related field" degree requirement.
- **Real, hands-on ML model training/evaluation** — unsupervised clustering (device-behavior clustering)
  and time-series anomaly-detection models, built and evaluated in production against cloud-scale customer
  data (GCP Dataproc/PySpark). This is genuine "design, train, evaluate ML models" experience, not just
  ML-adjacent data engineering.
- **GenAI/LLM production experience is a strong, direct match** for "translate academic advances into
  practical, production-ready systems": prompt engineering for security use cases, GenAI-driven SIEM API
  orchestration, and reusable GenAI-powered "skills" for detection engineers (e.g., converting detection
  rules between SIEM syntaxes) — real shipped LLM-application tooling, not a one-off demo.
- Python, PyTorch, scikit-learn all directly confirmed.

**Why it's not higher — real gaps, stated honestly:**
- **No confirmed MLOps tooling experience (MLflow, Weights & Biases, Kubeflow, or similar).** This is
  explicitly listed in the JD's "if you've got it" section and is a genuine gap — not claimed anywhere in
  the resume or cover letter. Flagging this here for Kyle's awareness; if asked directly in an interview,
  the honest answer is "no hands-on experience with those specific tools, but real experience building and
  operating a rigorous experimentation/quality-tracking discipline" (the detection-as-code CI/CD pipeline
  with automated testing, staged rollout, and formally tracked quality metrics is the closest transferable
  evidence, and is worth mentioning as an analog).
- **"Deep hands-on experience training/evaluating ML models, including language models" is a partial
  match, not a full one.** Kyle's language-model experience is at the *application/orchestration* layer
  (prompt engineering, GenAI-powered tooling built on top of existing LLMs) — not hands-on training or
  fine-tuning of language models themselves. His direct "training and evaluating models" experience is in
  classical/unsupervised ML (clustering) and time-series models, which is real but narrower than what a
  title like "AI Research" might imply. Framed honestly in the resume/cover letter as what it actually is
  (production LLM tooling + classical ML training) rather than stretched into a false equivalence.
  Note: this is exactly the kind of gap the JD's "including language models" phrasing was written to gate
  on, so it may come up directly in a phone screen — worth having a straight answer ready (see
  interview_prep.md).
- **No confirmed computer vision or reinforcement learning experience** (JD lists these as "and/or" alongside
  NLP, so not necessarily disqualifying if the team's actual near-term work is NLP/LLM-focused, but flagging
  since the JD names all three).
- Not a federal contracting role, not on the exclusion list, fully remote — no other flags.

## Coverage summary
**Direct matches:** Python, PyTorch, ML model training/evaluation (clustering, time-series), GenAI/LLM
production-system experience, Cribl product fluency, 4+ years bar (exceeded at 12), related-field degree bar.

**Adjacent/transferable (framed honestly, not oversold):**
- "Language models" — real LLM *application* experience, not model *training*.
- NLP — touched via prompt engineering/LLM application work, not formal NLP modeling (embeddings,
  architectures, tokenization).
- Rigorous experimentation culture — evidenced via detection-as-code CI/CD testing/staged rollout/quality
  metrics tracking, not formal ML experiment-tracking tooling.

**Gaps (not claimed anywhere in resume/cover letter):**
- MLOps tooling: MLflow, Weights & Biases, Kubeflow, or similar.
- Computer vision.
- Reinforcement learning.
- Hands-on LM fine-tuning/architecture-level training.

## Formatting
Single-column, standard section headers (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, Arial throughout, exported as text-layer PDF. Resume and cover letter both
render cleanly at one page each (visual QA passed, no overflow or awkward wraps).
