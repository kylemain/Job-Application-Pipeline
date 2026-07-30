# Interview Prep — Fluidstack, Staff Detection Engineer

## Likely behavioral questions
1. Tell me about a time you built something from zero — no inherited program, no existing team practice to lean on.
2. Describe a high-severity incident you led end to end, from first alert through postmortem.
3. How do you prioritize what to build first when a security function has broad, undefined scope?
4. Tell me about a time you had to get telemetry or a fix from another team without formal authority to compel it.
5. Walk me through a detection you shipped that turned out to be wrong or noisy — how did you catch it and what changed?
6. How do you balance "extreme ownership" of a problem against knowing when to escalate or ask for help?
7. Describe a time you translated a vague threat landscape into a concrete, prioritized roadmap for leadership.
8. Tell me about the most technically complex system you've built end-to-end, from design to production.

## Likely technical questions
1. Walk through your nine-SIEM detection-as-code orchestration framework — how did versioning, testing, and staged rollout actually work in practice?
2. How would you design detection coverage across AWS/GCP/Azure control-plane and audit logs from scratch?
3. What's your approach to writing detections against EDR event streams and OS-level telemetry, versus SIEM log data?
4. How do you use threat intel to inform detection logic rather than just react to indicators after the fact?
5. Describe the Common Information Model you built — how did it solve schema normalization across 220+ sources?
6. How would you structure a detection-as-code CI/CD pipeline in a smaller, leaner engineering org than your past employers?
7. What's your experience with Python-based automation for alert triage/enrichment — walk through a specific example.
8. How do you measure whether a detection is "good" (coverage, precision, false-positive rate) and act on that data?

## Questions Kyle should ask them
1. Is this truly a from-scratch security function, or is there existing tooling/telemetry access already in place?
2. What does the on-call/incident-response rotation look like today, and how is it likely to change as the team grows?
3. How is success measured for this role in the first 6–12 months?
4. What's the current state of cloud telemetry access (AWS/GCP/Azure audit logs) — is that infrastructure already built, or part of this role's scope?
5. Given the "remote in New York, NY" posting language alongside an "on-site" tag, what does the actual remote/in-office expectation look like day to day?

## Salary anchor
Posted range: $224,000–$275,000. Anchor to the top third (~$266K+) given Kyle's ~8 years of directly relevant detection engineering and platform-orchestration experience, consistent with his $170K+ floor and this range being well above it.

## Closing-the-interview script
"This role is exactly the kind of end-to-end ownership I've been building toward — a detection engineering function treated as software, across cloud and endpoint telemetry, tied directly to incident response. I'd welcome the opportunity to bring the same approach I used building a nine-SIEM orchestration framework to Fluidstack's security program. What would the next steps look like from here?"
