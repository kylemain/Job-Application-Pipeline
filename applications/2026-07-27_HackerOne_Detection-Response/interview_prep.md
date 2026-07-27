# Interview Prep — HackerOne, Senior Security Engineer, Detection and Response

## Likely behavioral questions
1. Tell me about leading incident response under real pressure (Treasury SOC context).
2. Describe a time you shipped automation that materially reduced manual toil for a small team.
3. Tell me about scaling detection engineering with fewer people than the problem seemed to require.
4. Describe turning an ambiguous "gap in observability" into a concrete, shipped plan.
5. Tell me about giving or receiving pushback on a detection design decision.
6. Describe partnering with engineering/platform teams to expand logging or observability.
7. Tell me about the hardest issue you diagnosed in a production detection pipeline.

## Likely technical questions
1. Walk through your detection-as-code CI/CD pipeline in GitLab — what runs at each stage?
2. How do you structure a reusable per-SIEM API adapter — where's the abstraction boundary?
3. Describe using GenAI for false-positive triage — how do you measure precision/recall improvement?
4. How would you design automated investigation/response workflows to replace manual runbooks?
5. Your AWS experience is general cloud security rather than CloudTrail/GuardDuty/VPC flow logs specifically — how would you close that gap quickly?
6. Walk through building UEBA detection content on top of transform outputs — what features mattered most?
7. How do you build a feedback loop between incident retrospectives and detection tuning?
8. Your production code is Python inside data/detection pipelines rather than Go/Ruby application backends — how would you ramp on Go if the team needs it?

## Questions to ask them
1. How much of "detection and response" work today is manual triage vs. engineering — what's the target mix?
2. What does the AI/LLM tooling stack currently look like — built in-house or vendor-based?
3. How is success measured for this role in the first 90 days?
4. What's the on-call/incident-response rotation structure for this team?
5. Given the role is tied to specific metro hubs, how often does in-person collaboration actually happen?

## Salary anchor
Posted range: **$182,000–$202,000.** Comfortably above your $170K floor. Anchor to the top third (~$195K–$202K) once fit is confirmed.

## Closing-the-interview script
"I'm genuinely excited about the AI-first rebuild of detection and response here — it's the same shift I've been driving in my own work. What does the timeline look like from here, and is there anything about my background you'd like me to expand on?"
