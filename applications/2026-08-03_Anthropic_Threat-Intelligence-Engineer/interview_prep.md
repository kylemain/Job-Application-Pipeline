# Interview Prep — Anthropic, Threat Intelligence Engineer

## Likely behavioral questions
1. This is a small, high-impact team on a foundational engineering role — tell me about a time you took a
   project from proof-of-concept to production largely on your own, including the monitoring/documentation
   work that made it maintainable afterward.
2. Walk me through how you've worked directly with non-engineering stakeholders (investigators, SOC analysts)
   to understand their workflow and turn it into a technical system.
3. Tell me about a time a detection system you built generated too many false positives — how did you find
   out, and what did the feedback loop with the people triaging alerts actually look like?
4. Describe building something from scratch with very little existing infrastructure to lean on (e.g., the
   DOE/NNSA Security Data Integration platform) — how did you sequence what to build first?
5. Tell me about a time you had to integrate with an external platform/API you didn't control — how did you
   handle its quirks, rate limits, or schema changes without breaking downstream detection logic?
6. Describe a time you used a new tool (including AI tooling) to solve a problem faster than your existing
   process allowed — what convinced you it was worth the switch?
7. This role scales from one engineer to "a multi-person collections function" over time — tell me about a
   time you built something that had to be handed off or scaled to other people using it.

## Likely technical questions
1. Walk through the multi-SIEM/EDR orchestration framework you built at Trend Micro/Cysiv — how did the
   per-technology adapters work, and how would that pattern extend to integrating threat intel platforms like
   VirusTotal, Censys, or Urlscan?
2. You haven't built YARA rule infrastructure directly — how would you approach building tooling to write,
   validate, and test YARA rules against real data, drawing on your native SIEM/Elasticsearch detection-rule
   experience?
3. Describe how you've used GenAI to interact with SIEM APIs for orchestration — how would that translate to
   using Claude to extract TTPs from CTI news/RSS sources and generate targeted hunting queries?
4. Walk through the UEBA detection layer you built on Elasticsearch transforms at DOE/NNSA — what signals fed
   it, and how did you validate it was actually surfacing real anomalies versus noise?
5. You haven't used Airflow or DBT specifically — walk through how your GitLab CI/CD detection-as-code pipeline
   handles orchestration, testing, and staged rollout, and how you'd map that onto a DBT-based framework.
6. How do you think about correlating signal across multiple disparate external data sources to reduce false
   positives in an automated detection system, rather than relying on any single source?
7. Describe your approach to taking a detection system from "v0 proof of concept" to "production-grade with
   monitoring, documentation, and maintenance" — what's the minimum bar before you'd call something production?
8. How would you build a searchable audit-logging infrastructure for a detection system, and what would you
   want it to capture to make investigator review fast?

## Questions to ask them
1. Where is the Threat Intelligence team today in terms of headcount and maturity — is this genuinely the
   first dedicated engineering hire, or are there existing systems/tooling I'd be building on top of?
2. How much of the role is building brand-new detection capability versus maintaining/scaling what already
   exists for the investigators?
3. How does the team currently use Claude/GenAI in the threat-intel workflow today, and where are the biggest
   gaps between what's possible and what's actually built?
4. What does success look like in the first 90 days for this role, given how foundational it is?
5. How does this team's work connect to Anthropic's broader trust & safety / abuse-detection efforts —
   where's the boundary?

## Salary anchor
Posted band: $320,000 – $405,000. Well above Kyle's $170,000+ floor. Anchor to the top third
(~$375,000–$405,000) once fit is confirmed — this is a strong-fit, well-compensated req, no reason to anchor
low.

## Closing-the-interview script
"The combination this role needs — treating threat intelligence as an input to automated detection logic
rather than a passive feed, building durable integrations across external platforms, and using GenAI to scale
what a small team of investigators can cover — is exactly the shape of work I've been doing for years, just
across SIEM platforms instead of CTI sources specifically. I'd love to understand where the team is in scaling
from one engineer to that multi-person collections function, and what the next steps look like."
