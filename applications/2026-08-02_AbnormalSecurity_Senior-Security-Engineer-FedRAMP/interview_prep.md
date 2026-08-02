# Interview Prep — Abnormal Security, Senior Security Engineer, FedRAMP

## Likely behavioral questions
1. Walk me through your current work supporting Treasury's SOC — what does a typical incident response
   engagement look like day to day, from alert to after-action reporting?
2. Tell me about building the DOE/NNSA Security Data Integration platform from scratch — how did you decide
   what to build first, and what would you do differently with what you know now?
3. Describe a time you had to balance security rigor against operational velocity (a recurring FedRAMP/ConMon
   tension) — how did you make the call?
4. Tell me about a time you had to document or explain a security decision for an audit or compliance review,
   even informally.
5. Describe working across teams (DevInfra/Compliance-style stakeholders) to get a security change through
   review — what friction came up and how did you resolve it?
6. Tell me about a time a detection rule or alert generated too much noise — how did you find out, and what did
   you change?

## Likely technical questions
1. Walk through the DOE CDM (Continuous Diagnostics and Mitigation) work — what did "continuous monitoring"
   actually look like in practice, and how does that compare to what you understand about FedRAMP's ConMon
   requirement?
2. How would you approach tuning SIEM ingestion and alerting for coverage *and* accuracy at the same time —
   walk through your actual process for the multi-SIEM orchestration pipeline you built.
3. Describe your GitLab CI/CD detection-as-code pipeline in detail — how do staged/safe rollout and automated
   testing work together to prevent a bad rule from reaching production?
4. You haven't owned formal NIST 800-53 control implementation directly — how would you ramp up on that
   framework given your continuous-monitoring and federal-environment background?
5. Walk through how you created and governed API tokens/roles/permissions across SIEM platforms — how did you
   think about least-privilege and periodic access review?
6. You haven't owned a patch management process end-to-end — how would you approach learning that scope
   quickly, and what adjacent experience would you lean on?
7. How do you approach triaging a security incident from alert to containment — walk through your actual
   workflow at Treasury SOC.

## Questions to ask them
1. What does "Abnormal Gov" actually look like architecturally — is it a fully separate environment/account
   boundary, or a compliance overlay on shared infrastructure?
2. Where is the team in the FedRAMP authorization lifecycle right now — initial ATO push, ConMon steady-state,
   or prepping for a 3PAO reassessment?
3. How is work split day to day between CI/CD pipeline ownership, access management, patch cycles, and
   incident response — is this one person wearing all these hats, or a team with some specialization?
4. What does the Change Control Board process look like in practice — how much of a bottleneck is it, and
   what's the team doing to keep velocity up without cutting corners?
5. What's the relationship between this team and DevInfra/FedOps day to day — who owns what?

## Salary anchor
Posted band: $153,000 – $220,000. Kyle's floor is $170,000+, and the band bottom is below that floor — do not
anchor low. Anchor to the top third of the posted range (~$197,667–$220,000) once fit is confirmed.

## Closing-the-interview script
"The federal-environment discipline here — continuous monitoring, access governance, and incident response
under real audit scrutiny — is exactly the kind of work I've been doing at DOE, DOE/NNSA, and Treasury for
years, just under a different compliance framework. I'd love to understand where this hire sits in the
FedRAMP authorization timeline and what the next steps look like."
