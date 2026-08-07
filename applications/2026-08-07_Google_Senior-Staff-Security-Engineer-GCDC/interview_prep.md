# Interview Prep — Senior Staff Security Engineer, GCP Cyber Defense Center (Google)

## Likely behavioral questions
1. Tell me about a time you owned a security detection capability end to end, from design through production. (DOE/NNSA Elasticsearch platform build is the strongest story here.)
2. Describe a time you had to set technical direction or standards that other teams had to adopt. (GitLab CI/CD detection-as-code pipeline standards across nine SIEM platforms.)
3. Walk me through a high-severity incident you helped resolve and what changed afterward to prevent recurrence. (Treasury SOC case work — pick one with a concrete before/after fix.)
4. Tell me about a time you identified a systemic root cause behind multiple incidents rather than just patching one symptom.
5. Describe a disagreement with a peer or stakeholder about a security architecture decision and how you resolved it.
6. Tell me about a time you had to quickly learn a new security domain or tool to solve a problem.
7. Describe how you've mentored or influenced less senior engineers without having formal management authority.
8. Tell me about a time a detection you built generated too many false positives — what did you do?

## Likely technical questions
1. How would you design a detection pipeline that scales across a multi-tenant cloud platform with wildly different customer telemetry volumes?
2. Walk through how you'd triage a newly disclosed zero-day affecting cloud infrastructure — what's your first hour look like?
3. How do you measure whether a detection rule is "good"? What metrics do you track and how do you act on them? (Direct: coverage, precision, false-positive rate, staged rollout.)
4. How have you used AI/ML in a detection or incident-response workflow, and what were the failure modes you had to guard against?
5. Describe your approach to building a UEBA detection layer — what data do you need, and how do you avoid alert fatigue?
6. How would you architect detection content that needs to run consistently across AWS, GCP, and Azure?
7. What's your experience with Elasticsearch as a detection platform specifically (vs. just log storage)?
8. How do you approach IAM/permissions design when building tooling that needs API access across many security platforms?

## Questions to ask them
1. What does "own the multi-year technical vision" look like day to day for this role — is it mostly architecture/roadmap, or hands-on building?
2. How is GCDC's detection engineering work coordinated with product security teams across the rest of Google Cloud?
3. What does success look like in the first 6-12 months for someone in this seat?
4. How does the team currently measure detection coverage/quality, and where are the biggest gaps today?
5. What's the relocation/onboarding process like for someone moving from out of state into the Sunnyvale office?

## Salary anchor
Posted band is $262,000-$364,000 + 25% bonus target + equity. Given 12 years total experience and direct overlap with the role's core technical asks, anchor initial conversations to the top third of the band (~$330K+ base) rather than the midpoint.

## Closing-the-interview script
"This role is exactly the kind of platform-scale detection engineering work I've been building toward — from the ground-up Elasticsearch platform I built at DOE/NNSA to the multi-SIEM orchestration framework I run today. I'm genuinely excited about the chance to bring that to GCDC's mission, and I'm ready to relocate to Sunnyvale to do it in person. What would be a good next step from here?"
