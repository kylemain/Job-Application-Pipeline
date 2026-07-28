# Interview Prep — Instacart, Detection Engineer II

## Likely behavioral questions
1. Tell me about a time you raised the bar on detection coverage rather than just closing individual alerts.
2. Describe mentoring another engineer on detection logic or investigation technique.
3. Tell me about partnering with Engineering or a Red Team to validate a detection against real adversary behavior.
4. Describe a time you reduced noise/false positives in a high-volume alerting environment.
5. Tell me about balancing telemetry cost/volume against detection coverage.
6. Describe the hardest forensic investigation you've supported.

## Likely technical questions
1. Walk through your detection-as-code CI/CD pipeline — what runs at each stage before a rule ships?
2. How do you map existing detection coverage against MITRE ATT&CK to find real gaps (not just tool checklists)?
3. Describe building detection logic across AWS/GCP/Azure control-plane and audit logs — what differs by cloud?
4. Your endpoint telemetry experience has been through SIEM/EDR platforms like CrowdStrike/SentinelOne rather than raw macOS internals — how would you ramp on macOS-specific attacker techniques?
5. How would you design a SOAR playbook for triage/enrichment automation, given your GenAI-based triage tooling background?
6. Describe using ML for threat detection — walk through your clustering/anomaly-detection work.
7. How do you approach log ingestion pipeline cost/volume management while preserving detection quality?

## Questions to ask them
1. How is the Detection Engineering team split across endpoint, cloud, container, and SaaS coverage today — where are the biggest gaps?
2. What does the detection-as-code review/testing process look like day to day?
3. How does the team work with Red Team and Trust & Safety on validating detections?
4. What's the split between building new detection content vs. tuning/maintaining existing coverage?
5. Given the listed pay bands vary significantly by state, is there flexibility for a fully remote candidate outside the listed metro bands?

## Salary anchor
Posted band for TX-based candidates: **$157,000–$165,500** — below your $170K floor. Worth raising directly with the recruiter early: ask whether the band is tied strictly to state of residence or negotiable given the seniority/scope of your background, before anchoring further.

## Closing-the-interview script
"I'd love to help push detection coverage and quality forward here — what does success look like for this role in the first 90 days, and is there anything about my background you'd like me to expand on?"
