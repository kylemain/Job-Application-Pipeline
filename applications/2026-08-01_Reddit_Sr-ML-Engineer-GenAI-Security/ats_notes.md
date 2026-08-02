# ATS Coverage & Fit Notes — Reddit, Senior Machine Learning Engineer, GenAI Security

## Salary check
Posted band: **$216,700 – $303,400 USD base.** Well above Kyle's $170,000+ floor across the entire range —
even the bottom of the band clears floor comfortably. No flag. Anchor negotiation language to the top third
(~$282,600–$303,400) once fit is confirmed, per standing rule.

## Remote / federal check
- **Remote:** Yes — "Remote - United States," fully remote, no location flag needed. Matches Kyle's
  remote-only requirement.
- **Federal contracting:** No. Not applicable here.
- **Exclusion list:** Reddit is not on the company exclusion list (Sophos, Binary Defense, Shorepoint,
  Dropzone AI). Clear to proceed.

## Fit score: 6/10

**The honest framing, up front:** Kyle's standout differentiator for this posting — his GenAI/LLM-for-security
work — is real and directly on-theme with the team name ("GenAI Security"), but it is not the same thing the
JD is actually asking for. Kyle's GenAI experience is *using GenAI as a tool* to do security work (prompt
engineering for triage/rule generation, LLM-orchestrated SIEM API interaction, GenAI-powered tooling for other
engineers). The JD's core ask is the inverse: *building ML models that secure and police Reddit's own GenAI
traffic* — guardrail models, semantic classifiers, and anomaly detectors that catch prompt injection,
jailbreaks, and data exfiltration in Reddit's AI systems. These are adjacent, thematically resonant, and both
genuinely differentiating in a stack of "generic ML engineer" resumes — but they are not the same domain, and
the resume/cover letter frame it as directly relevant adjacent experience rather than an exact match. Don't
let the shared "GenAI" language in both create a false impression of a 1:1 domain fit going into the
interview loop.

**Real strengths matching the JD:**
- **5+ years building/training/evaluating/deploying production ML models** — confirmed, and then some (12
  years total, with ML-specific work spanning Experian through present). PyTorch, scikit-learn, pandas, NumPy,
  SciPy all confirmed hands-on.
- **Full ML lifecycle ownership** — confirmed: problem definition, data pipelines, feature engineering,
  training, evaluation, deployment, monitoring, retraining-from-feedback are all evidenced across the
  Cysiv/Forescout/Shorepoint detection engineering work.
- **Rigorous model evaluation** — strong match: precision/recall, false-positive/false-negative analysis,
  threshold tuning, staged/safe rollout, formally tracked detection-quality metrics are all confirmed,
  real practices (not just claimed) from the multi-SIEM detection-as-code work.
- **Large-scale data pipelines** — confirmed: PySpark/SparkSQL on GCP Dataproc, 220+ ingested log sources,
  Apache Beam/Dataflow for cold-storage retrieval.
- **Production-quality software, Python** — confirmed (Go is not — no evidence of Go anywhere in the master
  doc; not claimed).
- **Applying ML to security/trust & safety/abuse prevention/adversarial ML** — confirmed as a strong plus
  signal: 2,300+ detection rules across MITRE ATT&CK, UEBA/anomaly detection, adversarial-style
  false-positive/false-negative tuning against a shifting threat landscape.
- **Communication with cross-functional partners on model behavior/risk tradeoffs** — reasonably inferable
  from the detection-as-code and SOC collaboration work, though not a headline-documented skill in the master
  doc; not oversold on the resume.

**Real gaps — flagged honestly, not papered over:**
- **No confirmed production deep-learning/transformer model training experience at this scale.** PyTorch is
  confirmed, but the master doc's evidenced ML work is predominantly classical/applied ML — clustering
  (unsupervised), time-series statistical anomaly detection, feature engineering for rule-based/hybrid
  systems — not training or fine-tuning neural network/transformer architectures on text data. The JD
  explicitly wants "modern deep learning architectures: neural networks, transformers, sequence models,
  embeddings, model distillation" and training/fine-tuning neural text models for long-context/structured/
  multi-turn/tool-call inputs. This is the single biggest gap against the JD's core technical ask and
  should not be overstated in interviews — be ready to speak honestly about PyTorch fluency without
  claiming production transformer-training depth that isn't backed by real project history.
- **No confirmed MLOps tooling stack.** The JD lists Airflow, Ray, MLflow, Triton, ONNX, Kubernetes as
  "plus" experience for production MLOps/model serving. None of these are confirmed in the master doc.
  Kubernetes exposure is confirmed but explicitly as a **platform user** (worked within a
  Kubernetes-orchestrated environment), not for ML model serving, cluster administration, or K8s-specific
  infrastructure ownership — framed that way on the resume ("Kubernetes-orchestrated platform experience"),
  not claimed as MLOps/model-serving expertise.
- **No confirmed labeling-strategy/hard-negative-mining/synthetic-data-generation/active-learning
  experience** — another named "plus" in the JD with no direct match in the master doc. Not claimed.
- **No confirmed Go experience** — JD says "Python and/or Go," so this isn't a hard blocker, but worth
  noting Python is the only confirmed language match.
- **No federal contracting involved, no exclusion-list company involved** — clean on both fronts, not a
  concern for this posting.

**Why 6, not higher or lower:** The JD's baseline requirements (5+ years shipping production ML, full
lifecycle ownership, rigorous evaluation practice, large-scale data pipelines, Python) are all solidly met,
and the GenAI-for-security + detection-engineering domain background is a real, differentiating asset that
most ML-generalist applicants won't have. But the JD's specific technical center of gravity — deep learning/
transformer model training and production MLOps tooling — is exactly where Kyle's confirmed experience is
thinnest. This is a strong "worth applying, go in with eyes open" case rather than a clear top-tier match.

## Keyword coverage summary

**Direct matches:**
- Production ML/deep learning models (5+ years) — confirmed, exceeded (12 years)
- PyTorch — confirmed
- Full ML lifecycle — confirmed
- Data pipelines / large-scale datasets — confirmed (PySpark, GCP Dataproc, Apache Beam/Dataflow)
- Model evaluation rigor (precision/recall, false-positive analysis, threshold tuning, holdout/regression
  practices, staged rollout) — confirmed, strong match
- Production-quality software, Python — confirmed
- ML applied to security/adversarial/abuse-prevention/GenAI-security-adjacent work — confirmed (adjacent,
  framed honestly per above)
- BS-or-equivalent technical field — confirmed (B.S. Physics, M.S. Physics)

**Adjacent/transferable (named honestly, not oversold):**
- "GenAI security" — Kyle's experience is GenAI *as* a security tool, not ML models that secure GenAI
  systems; framed explicitly as adjacent in resume/cover letter language ("adjacent half of that same
  problem"), not claimed as direct domain match.
- Kubernetes — platform-user exposure only, not model-serving/MLOps administration; framed as
  "Kubernetes-orchestrated platform experience," not "K8s MLOps."
- Cross-functional communication on model tradeoffs — inferable from detection-engineering collaboration,
  not a headline-documented skill; not oversold with specific claims not in the master doc.

**Gaps (not claimed anywhere):**
- Transformer/neural-text-model training or fine-tuning at production scale
- MLOps tooling: Airflow, Ray, MLflow, Triton, ONNX
- Labeling strategy, hard-negative mining, synthetic data generation, active learning
- Go

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, contact info in document body, standard Arial font — passes the formatting rules
in `references/ats-optimization.md`.

## Recommendation
Worth applying — salary is well above floor, remote, no federal/exclusion issues, and the GenAI-for-security
background is a real differentiator that few competing applicants will have. But go in clear-eyed that the
JD's core technical ask (deep learning/transformer model training, production MLOps tooling) is the area
where Kyle's confirmed experience is thinnest, and that the "GenAI Security" framing overlap with Kyle's
background is thematic/adjacent rather than an exact domain match. If asked directly in an interview, be
honest about the classical-ML vs. deep-learning distinction rather than letting the PyTorch line imply more
transformer-training depth than is actually backed by project history.
