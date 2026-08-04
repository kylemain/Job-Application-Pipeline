# Interview Prep — Google, Security Engineer, Enterprise Detection Engineering

## Location note
This role is on-site in San Jose, CA. Be ready to speak plainly and early about relocation — Kyle is based in
the Dallas/Ft. Worth area and is open to relocating for this role, but it's a deviation from his default remote
preference, so don't let it come up as a surprise late in the process.

## Likely behavioral questions
1. Tell me about being a very early hire at Cysiv and building the detection rules engine from scratch — how did
   you decide what to prioritize first, and what would you build differently knowing what you know now?
2. Walk me through a time a detection rule you built generated too much noise in production — how did you find
   out, and what did you change to fix it?
3. Describe a time you had to scope a brand-new detection requirement with very little existing precedent (like
   the DOE/NNSA Security Data Integration platform) — how did you approach the unknowns?
4. Tell me about a time you had to balance detection coverage against performance/resource cost — how did you
   make the tradeoff?
5. Describe working with other teams (incident response, engineering, threat intel/Vedere Labs) to get a
   detection improvement into production — what friction came up?
6. Tell me about a time you used threat intelligence to change how you built or tuned a detection rule.
7. Why are you interested in an on-site role in San Jose after years of remote work — what's driving that?

## Likely technical questions
1. Walk through your MITRE ATT&CK-mapped detection rule catalog at Cysiv (2,300+ rules) — how did you organize
   and prioritize coverage across the matrix, and how did you know where the real gaps were?
2. This role talks about reducing detection latency to a P50 under 2 hours and minimizing GCU/RAM/disk usage —
   how would you approach profiling and optimizing an existing detection pipeline for both speed and resource
   cost?
3. Describe how you built the UEBA detection layer on top of Elasticsearch transforms for DOE/NNSA — what did
   the transform-to-detection pipeline look like end to end?
4. How do you approach reducing false positives without also cutting real detection coverage — walk through
   your actual rule-quality-metrics/staged-rollout process.
5. The role wants detection engineering across corporate endpoints (macOS/Linux/Windows) and SaaS surfaces —
   your background is more data-platform/SIEM-centric (e.g., CrowdStrike as an EDR data source). How would you
   ramp up on endpoint-agent-level detection engineering specifically?
6. Describe your GitLab CI/CD pipeline for detection-as-code — how do automated tests and staged/safe rollout
   work together to catch a bad rule before it reaches production?
7. How have you used GenAI/LLMs in your detection engineering workflow — walk through a concrete example (e.g.,
   FP triage or rule-syntax translation across SIEMs).
8. How would you approach a post-Red-Team-exercise gap analysis — turning a detection gap finding into a
   shipped remediation rule?

## Questions to ask them
1. What does the "Enterprise Detection" team's current surface coverage look like — is corporate endpoint,
   Workspace/SaaS, and AI/agentic-infrastructure detection owned by one team or split across specialized subteams?
2. How is detection latency (the P50 < 2 hours target) currently measured and enforced — what's the biggest
   bottleneck today, ingestion, rule logic, or triage?
3. How does the team run and learn from Red Team/Purple Team exercises — how often, and how directly do findings
   turn into new detection content?
4. What does the AI/agentic-threat detection work actually look like right now — is this genuinely new ground,
   or is there existing tooling/prior art on the team?
5. What does the path look like for someone relocating into this role — timeline expectations, and is there any
   flexibility on start date to manage a cross-country move?

## Salary anchor
Posted band: $147,000 – $211,000 + 15% bonus target + equity. Kyle's floor is $170,000+; the midpoint (~$179K)
clears it, and the top third (~$189,700–$211,000) clears it comfortably. Anchor to the top third once fit is
confirmed — and remember the 15% bonus target and equity are real components of total comp, not just the base
number.

## Closing-the-interview script
"Building detection content that actually holds up in production — not just detects, but does it accurately and
efficiently — is what I've spent 12 years doing, from building a rules engine from scratch at an early-stage SIEM
startup to running a multi-SIEM detection-as-code pipeline today. I'd love to understand how the Enterprise
Detection team is thinking about the AI/agentic threat surface specifically, since that's clearly where a lot of
the newest work is heading, and what the next steps look like."
