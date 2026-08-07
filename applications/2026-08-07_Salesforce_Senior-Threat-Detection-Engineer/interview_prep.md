# Interview Prep — Senior Threat Detection Engineer (Salesforce)

## Likely behavioral questions
1. Tell me about a detection rule or piece of logic you built that caught something a previous approach missed.
2. Describe a time you had to reduce false positives on a noisy detection without losing true-positive coverage.
3. Walk me through owning a technical area end to end — how did you scope it, and how did you know you were done?
4. Tell me about a cross-team collaboration with an incident-response or engineering team that improved detection quality.
5. Describe a time you had to learn a new query language or platform quickly to get a detection into production.
6. Tell me about a significant security incident you helped investigate — what was your specific contribution?
7. How do you prioritize which detection gaps to close first when you can't do everything at once?
8. Tell me about a time you used threat intelligence to change how you approached a detection or an investigation.

## Likely technical questions
1. Walk through how you'd write a detection for a specific TTP (e.g., anomalous authentication volume by country) from data source to alert.
2. How do you approach log normalization and correlation across network, endpoint, cloud, and SaaS sources?
3. What's your experience with SPL specifically — walk through a complex search you've built.
4. How would you evaluate whether a new EDR or NDR data source is ready to have detection content built on top of it?
5. Describe how you'd build and test an attack-simulation scenario to validate a new detection rule.
6. What's your experience with Elastic Security / native ES detection rules vs. Kibana dashboards?
7. How do you decide when a detection rule should be retired or replaced rather than tuned further?
8. How have you integrated CTI (indicators, TTPs, actor context) directly into detection logic rather than just using it for manual triage?

## Questions to ask them
1. What does "complete ownership of a technical area" typically look like on this team — how much latitude is there to set direction vs. execute an existing roadmap?
2. Which log sources or platforms are the biggest current gaps in detection coverage?
3. How does the Threat Detection team work with CSIRT day to day — is it a formal handoff process or more embedded collaboration?
4. What does the on-call or incident-response rotation look like for this role, if any?
5. Is this role fully based out of Bellevue, or is there flexibility on location/remote work given the team is described as globally distributed?

## Salary anchor
Salesforce's own posting doesn't disclose a band; third-party estimates suggest roughly $149K-$224K for this req. Ask the recruiter for the actual posted range early, and anchor to the top third once known — don't accept the lower end given 12 years of directly relevant experience.

## Closing-the-interview script
"This role lines up almost one-to-one with what I've spent my career doing — writing detection logic against real telemetry, tuning it to cut false positives, and mapping it to MITRE ATT&CK. I'd love to bring that directly to Salesforce's Threat Detection team. What's the next step in your process?"
