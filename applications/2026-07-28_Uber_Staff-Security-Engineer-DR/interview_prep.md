# Interview Prep — Uber, Staff Security Engineer, Detection & Response (AI-Driven Threat Hunting & IR)

## Likely behavioral questions
1. Tell me about a time you led a technical project without a formal management title — how did you set direction and get buy-in from the team?
2. Describe a time you built something (tooling, a framework) because no commercial product fit the problem.
3. Walk me through mentoring or "teaching" a less experienced engineer through a hard problem.
4. Tell me about a decision where you had to balance speed (shipping automation) against risk (false positives/negatives).
5. Describe a cross-functional collaboration where you had to explain a technical security issue to a non-security team.

## Likely technical questions
1. Walk through the architecture of your nine-platform SIEM/EDR orchestration framework — how did you handle API rate limits, auth token rotation, and failure/retry logic across nine different vendors?
2. How did you design the multithreading for parallel rule deployment — what concurrency model, and how did you handle partial failures across customers?
3. Describe your GenAI tooling for false-positive triage in detail — what's the prompt design, what's the feedback loop for improving it over time, and how do you guard against hallucinated/incorrect triage decisions?
4. How would you design an autonomous investigation agent that triages, contains, and remediates an incident end-to-end? What guardrails would you put around autonomous containment actions?
5. Walk through your most complex entity-behavior investigation — from anomaly signal to root cause.
6. How do you think about the tradeoff between hypothesis-driven threat hunting campaigns and building automated, continuous hunting platforms?

## Questions to ask them
1. How much autonomy do the "autonomous investigation agents" currently have in production — advisory only, or do they take containment actions directly?
2. What does the path from IC to more formal technical leadership look like on this team?
3. How is success measured for this role in the first 6 months — is it a shipped agent/platform milestone, or reduced MTTR, or something else?
4. What's the current in-office expectation for this role in practice, and is full-remote a realistic path given my location?
5. What's the split today between building new hunting/detection platforms versus running day-to-day incident response?

## Salary anchor
Posted range: **$232,000–$258,000 base** (consistent across NYC/Seattle/SF/Sunnyvale), plus bonus, equity, and 401(k) match. Well above your $170K floor — anchor to the top of the band once fit is confirmed, and factor in equity/bonus value when comparing total comp against other offers.

## Closing-the-interview script
"I'd love to bring that orchestration and GenAI-automation background to a team building at this scale — what does the roadmap look like for the autonomous agent work over the next year, and is there anything about my background you'd like me to expand on?"
