# Interview Prep — Reddit, Senior Machine Learning Engineer, GenAI Security

## Likely behavioral questions
1. This role calls for you to "provide technical direction to other engineers" and be the "go-to ML expert"
   for SPACE — tell me about a time you set technical direction or standards for a project without having
   formal authority over the people involved (echoes the multi-SIEM detection-as-code framework and
   GenAI-tooling-for-other-engineers work).
2. Walk me through a time you built something from a completely blank slate, end-to-end (DOE/NNSA SDI
   platform build) — how did you decide what to build first, and what would you do differently?
3. Tell me about a time a model or detection rule you built generated too many false positives (or missed a
   true positive) in production — how did you find out, and what did you change?
4. This is a security-critical, adversarial domain — tell me about a time you had to think like an attacker
   to figure out how your detection logic could be evaded or bypassed.
5. Describe a time you had to translate a security problem into a measurable ML outcome for a
   non-ML-fluent stakeholder — how did you frame the tradeoffs (risk reduction vs. latency vs. false
   positives)?
6. Tell me about a time you worked across team boundaries (e.g., infrastructure, platform, or another
   security team) to get a model or signal into production — what friction came up and how did you resolve
   it?
7. Describe a time you had to learn a new technical domain quickly to be effective (relevant here — GenAI
   security specifically, versus your GenAI-as-a-tool background).

## Likely technical questions
1. Be ready to speak honestly here: your PyTorch/ML background is real, but it's mostly classical/applied ML
   (clustering, time-series anomaly detection) rather than deep learning/transformer training. If asked
   directly about transformer architecture or fine-tuning experience, don't overclaim — pivot to the
   adjacent strength (production LLM/GenAI tooling, rigorous evaluation practice, security-domain instincts)
   rather than implying depth you don't have.
2. Walk through how you built the ML-based device-clustering detection at Cysiv — what features did you
   use, how did you validate the clusters were meaningful, and how did you tune it for production?
3. Describe your time-series anomaly detection work on authentication behaviors (volume/geography) — how
   did you define "normal," and how did you handle baseline drift over time? (Directly maps to "anomalous
   usage" detection in the JD.)
4. Walk through the GenAI/LLM tooling you built for SIEM API orchestration and cross-SIEM rule conversion —
   what was the prompt engineering process, how did you evaluate output quality/correctness, and what
   guardrails did you put around it? (This is your strongest, most on-theme story for this specific team.)
5. Given Reddit's stated threats — prompt injection, jailbreak attempts, sensitive data exfiltration,
   unauthorized agent actions — how would you approach building an evaluation suite (adversarial examples,
   hard negatives, multi-turn workflows) for a semantic classifier? Reason through it from your
   false-positive/false-negative detection-tuning background even without direct prior art in this exact
   domain.
6. How would you approach designing a training pipeline you don't have direct production experience with
   (e.g., fine-tuning a transformer for a classification task) — how do you ramp on unfamiliar architecture
   quickly given your applied-ML foundation?
7. Walk through your EDA process on GCP Dataproc/PySpark — how do you go from "raw data" to "validated
   candidate signal" efficiently at scale, and how would that translate to building training/eval datasets
   for GenAI security models?
8. How do you think about the tradeoff between model latency/cost and detection precision/recall for a
   high-traffic, production-facing surface (e.g., an LLM gateway inline classifier)?
9. What's your approach to formally tracking model quality metrics and doing staged/safe rollout before full
   production deployment? (Strong, well-evidenced answer — lean into the detection-as-code CI/CD practices:
   automated testing, tracked precision/false-positive rates, staged rollout, rollback paths.)

## Questions to ask them
1. How mature is the GenAI Security team's current model stack — are you further along on classical
   ML/heuristics for these threats, or already running transformer-based classifiers in production? Where's
   the biggest gap between "what exists today" and "what this role needs to build"?
2. What does the retraining loop look like in practice — how much of it is human-labeled data vs. production
   feedback vs. synthetic/adversarial data generation?
3. How does the GenAI Security team's work interact with Reddit's LLM Gateway team — is model
   inference/serving owned by this team, or is it more "build the model, hand off to infra for serving"?
4. What does success look like in the first 6 months for this role — is it primarily model quality
   improvement on existing systems, or building net-new detection capability for a threat category that's
   not covered yet?
5. How is the team currently thinking about the tradeoff between fast-moving, hand-tuned detectors for
   specific attack patterns versus more generalizable, retrainable models — where do you want a senior hire
   to focus first?

## Salary anchor
Posted band: **$216,700 – $303,400 USD base.** This clears Kyle's $170,000+ floor comfortably even at the
bottom. Anchor to the top third of the band (~$282,600–$303,400) once fit is confirmed — no need to lead with
floor-framing language here given how strong the disclosed band already is.

## Closing-the-interview script
"The overlap between what I've built — production GenAI tooling for security workflows, plus a decade of
ML-based detection engineering with a real discipline around false-positive tuning and staged rollout — and
what this team needs is real, even though my direct experience is on the 'using GenAI for security' side
rather than 'building ML to secure GenAI' specifically. I'd love to understand how you're weighing that kind
of adjacent-but-strong background against candidates with more direct transformer/deep-learning production
experience, and what the timeline looks like for this hire."
