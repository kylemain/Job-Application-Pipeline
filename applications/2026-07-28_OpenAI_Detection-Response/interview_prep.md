# Interview Prep — OpenAI, Security Engineer, Detection and Response

## Likely behavioral questions
1. Tell me about a time you built a detection from scratch that caught something real — walk through the whole lifecycle.
2. Describe a time you had to reduce false positives on a noisy detection without losing coverage.
3. Tell me about a time you had to move fast on a security response with incomplete information.
4. Describe how you've used AI/LLM tooling to accelerate a security workflow — what worked, what didn't.
5. Tell me about a time you had to advocate for a telemetry or instrumentation gap to be fixed by another team.
6. Describe a project where you had to learn a new platform or technology quickly to solve a security problem.
7. Tell me about a disagreement with a teammate over detection design or response process — how did you resolve it?
8. What's the largest-scale detection or data pipeline you've owned end to end?

## Likely technical questions
1. Walk through how you'd design a detection pipeline for a new cloud service with no existing telemetry.
2. How would you measure detection quality — coverage, precision, latency — and what tradeoffs do you make?
3. Explain your approach to orchestrating detection content across multiple SIEM/EDR platforms with different APIs and rule syntaxes.
4. How do you think about detecting anomalous behavior from AI agents operating across infrastructure at scale?
5. Walk through a time-series anomaly detection approach you've built (e.g., authentication anomalies).
6. What's your approach to Kubernetes security monitoring? (Honest answer: you've worked on a platform that used Kubernetes for container orchestration, but didn't manage/administer the cluster yourself — real hands-on exposure to how the platform behaves day to day, not cluster-admin or K8s-specific detection engineering. Pivot to your track record learning new platforms fast, e.g., Kafka/Flink familiarity, GCP Dataproc, and offer that you'd ramp on cluster-level detection specifics quickly.)
7. How would you build a lightweight automation to reduce triage toil for a specific alert type?
8. Explain your multithreaded orchestration approach for deploying detection content across many customers/environments in parallel.

## Sharp questions to ask them
1. What does "high-signal detection" mean concretely on this team right now — what's the current false-positive rate you're trying to improve?
2. How much of the D&R team's roadmap is defensive (catching known threats) vs. proactive (threat modeling new AI infrastructure surfaces)?
3. How is the team thinking about detection coverage for agentic systems specifically, since that's called out as a novel area?
4. What does the on-call/incident-response rotation actually look like day to day?
5. How does this team work with infrastructure owners to get telemetry built into new systems from day one — what's that partnership like in practice?

## Salary anchor
Posted range $293K–$385K. Anchor conversation toward the top third (~$355K–$385K) once fit is confirmed — this is the highest disclosed base in Kyle's current pipeline, so there's real room to negotiate from a position of strength rather than defaulting to a $170K floor framing.

## Closing script
"This role's emphasis on high-signal detection and AI-driven automation across infrastructure is exactly the kind of work I've spent the last several years building — multi-platform orchestration, GenAI tooling, and detection content at scale. I'd love to talk about what the next 90 days would look like on this team, and what a strong first project might be."
