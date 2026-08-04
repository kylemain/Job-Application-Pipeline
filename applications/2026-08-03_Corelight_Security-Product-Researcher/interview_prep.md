# Interview Prep — Corelight, Security Product Researcher

## Likely behavioral questions
1. Tell me about a time you had to prove an idea could work before committing to building it at scale — walk
   through how you approached the DOE/NNSA Security Data Integration project from initial concept to a working
   platform.
2. Describe a time you had to move fast and iterate on a solution with limited direction — how did you decide
   what to build first, and how did you know when to change course?
3. This role asks for proactive, transparent communication — "sharing updates without prompting." Tell me about
   a time you kept stakeholders informed on a project without being asked to check in.
4. Tell me about a time you worked closely with product or engineering counterparts (not just other security
   engineers) to ship something — what friction came up, and how did you resolve it?
5. Describe a time you had to learn a new tool or technique quickly (e.g., adopting GenAI/LLM tooling into your
   workflow) — how did you ramp up, and what did you build with it?
6. Tell me about a detection or analytics project that didn't go the way you expected — what did you learn, and
   what would you do differently next time?
7. Describe your experience working in a fully distributed/remote team — what makes that work well for you?

## Likely technical questions
1. Walk through how you built the DOE/NNSA Security Data Integration platform — what did ingesting CrowdStrike,
   Suricata, and Zeek telemetry into Elasticsearch actually involve, end to end?
2. How would you approach rapid-prototyping a new detection idea using Zeek or Suricata — what's your actual
   process from hypothesis to a working proof of concept?
3. Describe your GenAI/LLM prompt-engineering work for security use cases in detail — how did you validate that
   AI-generated detection content or false-positive triage was actually correct before trusting it?
4. Walk through the reusable GenAI-powered tooling you built for detection engineers (e.g., cross-SIEM rule
   conversion) — how did you design it, and what were the failure modes you had to guard against?
5. You haven't worked in a full-stack agile software development role in the traditional sense — how do you
   think about the difference between building detection/data platforms and building full-stack product
   software, and where do you think your experience transfers cleanly vs. where you'd need to ramp up?
6. How would you evaluate whether a new detection technique should live in Zeek, Suricata, or as a downstream
   Elasticsearch-layer detection rule — walk through the tradeoffs.
7. Describe your understanding of network security concepts like protocol abuse and attack patterns — give a
   concrete example from your detection-content work.
8. How do you approach threat hunting and incident response in practice — walk through your current work
   supporting Treasury's SOC.

## Questions to ask them
1. How is the Security Product Researcher role scoped day to day — is it closer to research/prototyping that
   hands off to engineering, or does it include shipping code that reaches customers directly?
2. What does "full-stack" mean concretely in this role's context — is it mostly Python/backend prototyping
   around Zeek/Suricata, or does it extend into front-end/product-surface work too?
3. Where is the team in adopting agentic AI systems internally — is this role defining that direction, or
   joining an existing effort?
4. What does success look like in the first 90 days for someone in this role?
5. Is this role, and the team it sits on, fully remote, or tied to specific U.S./North America office
   expectations?

## Salary anchor
Posted band: $146,000 – $198,000. Kyle's floor is $170,000+; the band bottom sits below that floor and the
midpoint (~$172,000) only just clears it. Anchor to the top third of the posted range (~$180,667–$198,000) once
fit is confirmed — don't let an early conversation anchor low given how thin the margin above floor already is.

## Closing-the-interview script
"What excites me most about this role is that it's built on the same foundation I've spent years working
directly with — Zeek and Suricata — plus the chance to apply hands-on GenAI/LLM experience to real security
research instead of just talking about it. I'd love to understand how this role's prototyping work hands off to
engineering, and what the team's near-term roadmap looks like for agentic AI in the product."
