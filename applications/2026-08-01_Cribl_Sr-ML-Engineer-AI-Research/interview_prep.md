# Interview Prep — Cribl, Sr Machine Learning Engineer, AI Research

## Likely behavioral questions
1. Tell me about a time you had to decide fast vs. right — when did you prototype quickly vs. push for a
   more rigorous/productionized approach?
2. Describe a project where you translated an experimental or research-y idea into something that actually
   shipped and ran in production.
3. Tell me about presenting experimental or model results to a non-technical stakeholder — how did you
   adjust the message?
4. Describe a time a model or piece of detection logic didn't perform as expected — how did you debug and
   iterate?
5. Tell me about working closely with a small, fast-moving team (founding team, startup-stage team) rather
   than a large established org.
6. Describe how you've tracked and documented experiment/iteration results in past roles, even without a
   formal MLOps stack.
7. Tell me about a time you had to learn a new tool or platform quickly to keep a project moving.

## Likely technical questions
1. Walk through the unsupervised clustering model you built for network device classification — feature
   engineering, algorithm choice, how you evaluated cluster quality.
2. Walk through your time-series anomaly-detection models — how did you validate detection quality and
   manage false-positive rate?
3. Describe the GenAI-powered "skills" you built for detection engineers — architecture, prompt design, how
   you evaluated output quality/reliability before trusting it in production.
4. **Direct gap question to expect:** "The JD calls for deep hands-on experience training/evaluating
   language models specifically — walk me through your experience there." Be straight: your LM experience
   is at the application/orchestration layer (prompt engineering, building production tooling on top of
   existing LLMs), not hands-on fine-tuning or architecture-level training — pivot to your real training/
   evaluation depth in classical and time-series ML, and your genuine interest in going deeper on the LM
   side.
5. **Direct gap question to expect:** "What's your experience with MLflow, Weights & Biases, or Kubeflow?"
   Honest answer: none hands-on yet. Pivot to the detection-as-code CI/CD pipeline you built — automated
   testing, staged/safe rollout, formally tracked quality metrics (coverage, precision/false-positive rate)
   — as the closest transferable discipline, and that picking up a specific MLOps tool is a fast ramp given
   that background.
6. How would you approach fine-tuning or hyperparameter search for a model, given your PyTorch/scikit-learn
   background?
7. Walk through your Elasticsearch transform/UEBA work at DOE/NNSA — how is that similar to a feature-
   engineering pipeline feeding a model?
8. Given your hands-on Cribl pipeline experience already, how would you think about using Cribl's own data
   pipelines to feed training/evaluation data for Cribl's ML models?

## Questions to ask them
1. What does the AI Research team's current experimentation/tracking stack actually look like (MLflow,
   Weights & Biases, Kubeflow, something in-house)?
2. How much of this role, in practice, is training/fine-tuning models from scratch vs. applying and
   orchestrating existing LLMs against Cribl's product surfaces?
3. What's the current split between research exploration and shipping features directly into the Cribl
   product suite?
4. How does the team define "production-ready" for a model — what's the actual bar for promoting a research
   result out of experimentation?
5. What does the on-call/stand-by expectation look like in practice during research or deployment
   milestones?

## Salary anchor
Posted band is $185,000 – $215,000 base — both ends clear the $170K floor. Anchor to the top third of the
band (~$205K–$215K) once fit is confirmed in later rounds.

## Closing-the-interview script
"I'd love to bring hands-on Cribl pipeline experience plus my applied ML and GenAI-for-security background
to this team — what does success look like for this role in the first six months, and is there anything
about my background you'd like me to expand on, particularly around the MLOps tooling or language-model
training depth you use day to day?"
