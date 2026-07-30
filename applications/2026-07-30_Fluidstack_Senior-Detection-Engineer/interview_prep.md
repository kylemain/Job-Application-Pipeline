# Interview Prep — Fluidstack, Senior Detection Engineer

## Likely behavioral questions
1. Tell me about a time you owned a detection engineering program end to end, from threat modeling through retiring a rule.
2. Walk me through a detection you built that caught something real — how did you know it was working?
3. Describe a time you had to decide whether a noisy rule needed tuning or needed to be killed entirely.
4. Tell me about operating with minimal process — a time you had to scope your own work without a mature team structure around you.
5. Describe a disagreement with a teammate or stakeholder over detection priorities or coverage gaps. How did you resolve it?
6. Tell me about a time threat intel changed how you approached a detection or an active investigation.
7. How do you decide what NOT to build detections for? Walk through a coverage/prioritization tradeoff you've made.
8. Tell me about the most technically complex piece of automation you've built and why it mattered.

## Likely technical questions
1. Walk through your nine-SIEM detection-as-code orchestration framework — how did per-technology adapters work, and why native APIs instead of a common abstraction layer from day one?
2. How did you measure false-positive rate in production, and what did you do when a rule's FP rate crept up?
3. Explain your GitLab CI/CD pipeline for detection content — what did the automated tests actually check?
4. How do you approach mapping detection coverage to MITRE ATT&CK, and how do you decide where the real gaps are versus where coverage looks fine on paper but isn't?
5. Describe your data engineering work across 220+ log sources — how did you handle schema drift or a source going quiet?
6. What does your Common Information Model do, and why did you need one across CrowdStrike/Suricata/Zeek/other sources?
7. How would you approach securing detection coverage across cloud, endpoint, and data center environments simultaneously, given your DOE/NNSA build experience?
8. What's your experience with threat intel-informed tuning versus formal threat hunting — be ready to draw this distinction honestly, since it's a real gap versus the JD's "run threat hunts" language.

## Questions to ask them
1. What does "detection coverage mapped to MITRE ATT&CK, gaps documented rather than assumed away" look like in practice here — is there an existing coverage matrix, or is that part of what this role builds?
2. How is the on-call rotation structured for the responders who consume this team's detection content, and how much cross-team ownership does detection engineering have over alert quality?
3. Given Fluidstack's rapid infrastructure buildout, how does the detection engineering team keep pace with new log sources and environments coming online?
4. What does the path from Senior to Staff Detection Engineer look like here, given both reqs are currently open?
5. How does the team currently do proactive threat hunting, if at all, versus reactive tuning off of alerts and incidents?

## Salary anchor
Posted band is $147K–$182K. Anchor to the top of the band ($180K–$182K) given 8 years of directly relevant experience, the nine-SIEM orchestration build, and the MITRE ATT&CK-mapped detection content — this is Kyle's stated expectation for where he'd land if an offer were made.

## Closing script
"This maps closely to the work I've been doing for years — owning detection coverage end to end, not just writing individual rules. I'd want to make sure the comp reflects the senior end of the band given that depth, and I'm glad to talk through specifics once we're past this stage. What are the next steps from here?"
