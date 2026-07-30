# Interview Prep — Pinterest, Security Software Engineer II, Detection and Response

## Likely behavioral questions
1. Tell me about a time you onboarded a new logging/telemetry source and what challenges came up.
2. Describe how you've used AI to speed up your own work, and how you verified the output before trusting it.
3. Tell me about a time you had to hunt for a threat that existing rules hadn't caught.
4. How do you collaborate with cross-team partners when a detection gap spans multiple teams' systems?
5. Describe a time you had to learn a new platform or telemetry source quickly to close a detection gap.

## Likely technical questions
1. Walk through your nine-SIEM orchestration framework and how detection rules get from idea to production.
2. What's your experience with OS internals — macOS, Linux, or Windows persistence/privilege escalation techniques? (Be honest: this is a real gap — Kyle's depth is in telemetry/detection-content engineering, not host-level internals.)
3. How have you used AI/LLMs to improve speed and quality in a security engineering workflow, and how do you validate that the output is trustworthy?
4. Describe your approach to writing SIEM queries for threat hunting versus alerting.
5. What telemetry sources have you worked with beyond traditional SIEM logs (e.g., EDR, network)?
6. How do you approach networking fundamentals (TCP/IP) when investigating a network-layer incident?

## Sharp questions to ask them
1. The posting is titled "Security Software Engineer II" but the comp band and duties look Staff/Senior-level — what does leveling actually look like for this specific req?
2. How mature is the AI-assisted detection tooling today, and what would this role's first project look like?
3. What does the in-office cadence (1-2x per 6 months) look like in practice for someone based outside the hub cities?
4. How is success measured for this role — detection coverage, MTTD, or something else?
5. What's the current biggest gap in telemetry/logging pipeline coverage that this role would help close?

## Salary anchor
Posted range: $123,696–$254,667 (unusually wide). Anchor to the top third (~$220K+) given the Staff-level scope of the actual duties described, and confirm leveling/level-appropriate comp directly with the recruiter given the title/band mismatch noted in ats_notes.md.

## Honest gap to address directly if asked
OS internals depth (macOS/Linux/Windows persistence, privilege escalation) and Osquery specifically are not confirmed in Kyle's background — his strength is telemetry pipeline engineering and detection-as-code across many SIEM/EDR platforms, not host-level forensics. Be upfront rather than implying deeper OS-internals experience than exists.

## Closing-the-interview script
"The detection automation and telemetry pipeline work is exactly what I've spent the last several years doing, across a wider set of platforms than most detection engineers touch. Where I'd want to be upfront is OS-internals depth — that's not where my experience is deepest. What would help you evaluate whether that gap matters for this specific role?"
