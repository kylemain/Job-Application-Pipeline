# Interview Prep — Google, Sr. Security Engineer, Uppercase Research

## Likely behavioral questions
1. Tell me about building something ambiguous from scratch with no clear spec (the DOE/NNSA security data platform).
2. Describe a time you had to convince stakeholders to adopt an automation-heavy approach over a manual process.
3. Tell me about a detection you shipped that turned out too noisy — how did you find out, and what did you do?
4. How have you balanced building new detection content with maintaining/tuning 2,300+ existing rules at scale?
5. Tell me about working across many disparate systems/APIs (nine SIEM platforms) — what made that hard?
6. How have you evaluated whether a GenAI-generated output (e.g., a detection rule) was safe/correct to ship?
7. Describe giving critical feedback on an existing security process or tool that people wanted to keep.
8. Tell me about navigating an incident under real time pressure (Treasury SOC context).

## Likely technical questions
1. Walk through your approach to orchestrating nine SIEM APIs — what did the shared abstraction layer look like?
2. How would you design a feedback loop between incident outcomes and detection tuning (regression testing, false-positive reduction)?
3. What's your approach to prompt engineering for detection-rule generation — how do you constrain an LLM against hallucinated logic?
4. How do you validate machine-written detection logic before deployment — what's your testing/staging strategy?
5. Describe your time-series anomaly detection approach for authentication behaviors — features and models used.
6. How would you design an agentic threat-hunting workflow that goes from raw signal to a scoped hypothesis?
7. Walk through how you defined a UEBA baseline of "normal" entity behavior.
8. How do you approach data-quality monitoring for a security data pipeline — what failure modes did you actually catch?

Be ready to be direct if asked about YARA-L specifically: you haven't confirmed hands-on YARA-L, but you've authored detection logic across many SIEM rule syntaxes and would expect to ramp fast.

## Questions to ask them
1. How much autonomy do the agentic pipelines have today — is a human always in the loop before a rule deploys, or are some fully autonomous?
2. What does success look like for Uppercase 12 months out — coverage metrics, false-positive reduction, time-to-detect?
3. How does the team handle YARA-L rule regression testing today — is there a formal test suite?
4. What's the current split between building new agent capabilities vs. maintaining/tuning existing detection content?
5. How does Uppercase interface with the rest of Google SecOps/Chronicle product engineering?

## Salary anchor
Posted range: **$174,000–$253,000 + 15% bonus target + equity.** Well above your $170K floor. Anchor to the top third (~$227K–$253K base) once fit is confirmed — factor in the bonus/equity when comparing total comp to other offers.

## Closing-the-interview script
"This is exactly the kind of problem I want to be solving — turning detection engineering from a manual, reactive discipline into something that scales with automation. I'd love to know what the next steps look like, and roughly what timeline you're working against."
