# Interview Prep — Netflix, Security Engineer (L5) - Cloud Architecture, Tooling and Security (CATS)

## Likely behavioral questions
1. Tell me about a time you had to secure a third-party integration you didn't fully control — how did you approach the access model?
2. Describe identifying high-leverage work and driving it independently, without explicit direction.
3. Tell me about a time you had to communicate a complex technical security tradeoff to a non-security engineering team.
4. Describe a security decision where you had to balance business enablement against risk.
5. Walk through a time you built internal tooling because nothing existing solved the problem.

## Likely technical questions
1. Walk through how you designed IAM policies and access controls in AWS and GCP — what was your approach to least-privilege and role design?
2. Your API-token/roles/permissions work spanned 9 SIEM/EDR platforms — how did you handle credential rotation, scoping, and revocation across that many vendors securely?
3. How would you approach designing a secure-by-default blueprint for GCP project lifecycle and service account management, starting from where Netflix is today?
4. Describe how you'd design metrics to gauge cloud security posture across a large, fast-moving AWS/GCP environment.
5. Walk through your framework's architecture — how would this scale conceptually to org-wide account governance rather than the per-vendor integration model you built it for?
6. How do you think about the tradeoff between self-serve tooling (letting engineering teams move fast) and centralized security guardrails?

## Questions to ask them
1. How is the CATS team's work split today between reactive access requests and proactive guardrail/paved-path building?
2. What does the onboarding ramp look like for someone strong on IAM implementation but newer to org-wide GCP account governance specifically?
3. How does CATS partner with the software engineering teams building new business verticals — what does that collaboration look like week to week?
4. What does success look like for an L5 in this role in the first 90 days?
5. How does the team measure "reducing tedious access management minutiae" — is there a specific metric or dashboard?

## Salary anchor
Posted range: **$400,000–$680,000/year** (salary-only comp structure — no bonus; you choose your salary/equity split annually). Exceptionally above your $170K floor. Given the real scope gap between your hands-on IAM experience and Netflix's org-wide governance ask, anchor expectations to the lower-to-middle third of the band rather than the top, and let the interview process (not the initial ask) surface whether the scope match supports going higher.

## Closing-the-interview script
"I'd love to bring that hands-on IAM and multi-vendor access-management background to a team operating at this scale — what would the first project look like for someone starting from implementation-level IAM work and growing into org-wide governance?"
