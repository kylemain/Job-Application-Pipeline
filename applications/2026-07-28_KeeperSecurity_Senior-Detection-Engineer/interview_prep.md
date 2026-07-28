# Interview Prep — Keeper Security, Senior Detection Engineer (SIEM / Security Observability)

## Likely behavioral questions
1. Tell me about a time you improved alert quality by reducing false positives/noise.
2. Describe partnering with Security Operations, Infrastructure, and SRE teams to get telemetry you needed.
3. Tell me about a detection gap assessment you ran — how did you find and prioritize the gaps?
4. Describe a time you had to make a telemetry/logging standard stick across multiple teams.
5. Tell me about mentoring another engineer through a detection design problem.

## Likely technical questions
1. Walk through your Common Information Model work — how did you standardize field names/types across parsed sources, and why did that matter for detection quality?
2. You've worked across nine SIEM/EDR platforms rather than Datadog/SentinelOne/Wiz specifically — how would you ramp on those tools' native detection syntax?
3. Describe your detection-as-code CI/CD pipeline in GitLab — what does peer review and testing look like before a rule ships?
4. How do you map detection coverage against MITRE ATT&CK to find visibility gaps rather than just checking a tool box?
5. Walk through building 50+ Logstash filters for parsing/normalization — what were the hardest edge cases?
6. How would you approach reducing false positives in a high-volume, cloud-native environment?
7. Your scripting is Python rather than PowerShell — how would you close that gap quickly in a Windows-heavy environment?

## Questions to ask them
1. What does the current SIEM/telemetry stack look like today (Datadog, SentinelOne, Wiz) and what's the biggest visibility gap?
2. How does the team currently measure detection/alert quality — false-positive rate, MTTD, coverage against ATT&CK?
3. What's driving the hybrid option in El Dorado Hills/Chicago — is there an expectation of periodic on-site time for fully remote hires?
4. How is work split between building new detection logic vs. maintaining/tuning existing coverage?
5. What does the salary range look like for this role? (Not listed in the posting.)

## Salary anchor
Not disclosed in the posting. Raise early with the recruiter and anchor to your $170K+ floor once a range is shared; use the top third of whatever band comes back given the strength of the skills match.

## Closing-the-interview script
"I'd love to bring that telemetry-standardization and detection-as-code discipline to Keeper's SIEM work — what does the roadmap look like for detection maturity over the next year, and is there anything about my background you'd like me to expand on?"
