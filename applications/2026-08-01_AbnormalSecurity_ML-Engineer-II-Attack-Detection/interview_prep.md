# Interview Prep — Abnormal Security, Machine Learning Engineer II (Attack Detection)

## Likely behavioral questions
1. This role is scoped as working "with senior engineer guidance" — tell me about a time you worked under
   close technical direction versus a time you owned a project end-to-end. How do you adjust your working
   style between the two?
2. Tell me about a time you built something from a completely blank slate (echoes the DOE/NNSA SDI platform
   build) — how did you decide what to build first, and what would you do differently?
3. Describe a time your detection model or rule generated too many false positives (or missed a true
   positive) — how did you find out, and what did you change?
4. Tell me about a time you had to convince a colleague or team that a new feature/signal was worth
   productionizing — how did you make the case?
5. Walk through how you've balanced building new detection capability against maintaining/tuning existing
   detection content in production.
6. Describe working across teams (e.g., infra/systems engineers) to get a signal you built into production —
   what friction came up and how did you resolve it?
7. Tell me about a time you disagreed with a more senior engineer's technical direction — what did you do?

## Likely technical questions
1. Walk through how you built the ML-based device-clustering detection at Cysiv — what features did you use,
   how did you validate the clusters were meaningful, and how did you tune it for production?
2. Describe your time-series anomaly detection work on authentication behaviors (volume/geography) — how did
   you define "normal," and how did you handle baseline drift over time?
3. How would you approach building a discriminative signal at the message, sender, and recipient level for a
   detection system you've never worked in the domain of (email) before?
4. Walk through your EDA process on GCP Dataproc/PySpark — how do you go from "raw data" to "validated
   candidate signal" efficiently at scale?
5. How do you structure an automated model retraining pipeline (data generation → training → evaluation →
   deployment) to stay reproducible? What's your approach to versioning models and metrics?
6. You haven't worked specifically with TensorFlow — how would you ramp up given your PyTorch background?
7. Given a set of false-negative and false-positive attack samples, walk through how you'd categorize the
   gaps and decide whether the fix is a new feature, a new rule, or a model retrain.
8. How do you think about the trade-off between a highly generalizable auto-trained model versus a narrow,
   specific detector for a high-value attack category? When would you reach for each?

## Questions to ask them
1. The JD frames this as "Engineer II... with senior engineer guidance" — what does the senior/staff bench on
   this team look like, and how much ownership does an Engineer II typically have over a signal or detector
   end-to-end?
2. How does the team currently measure detector efficacy — what does the false-negative/false-positive review
   cadence actually look like day to day?
3. How much of the modeling work is building new generalizable/auto-trained models versus hand-tuning
   specific detectors for high-value attack categories?
4. What does the retraining pipeline's deployment gate look like — how do you decide a new model version is
   safe to promote to production against hundreds of millions of messages?
5. What's the split between message-level, sender-level, and recipient-level signal work on this team, and
   is there a preference for where a new hire would start?

## Salary anchor
Posted band: $160,700 – $231,000. Kyle's floor is $170,000+, and the band bottom is below that floor — do not
anchor low. Anchor to the top third of the posted range (~$207,767–$231,000) once fit is confirmed, and
raise compensation expectations directly if early conversations trend toward the bottom of the band.

## Closing-the-interview script
"The behavioral-detection methodology here — baselining normal activity and building discriminative signals
to catch deviation — is exactly the kind of problem I've built from scratch before, just on a different data
domain. I'd love to understand the timeline for this hire and what the next steps look like."
