# Interview Prep — Cribl, Staff Security Operations Engineer

## Salary anchor
Disclosed band: $128,000 – $200,000 (geography-dependent). Anchor to the top third (~$176K+) once fit is
confirmed. The bottom of this band is below Kyle's $170K floor — if early conversations suggest the offer will
land in the lower half of the band, raise this directly and be prepared to walk rather than negotiate up from a
low anchor.

## Likely behavioral questions (Staff-level IC, cross-functional partner to Product Security/IT/Legal)
1. Tell me about a time you had to build detection or security tooling with significant ambiguity — no clear
   spec, evolving requirements. How did you scope it and know when it was "done enough" to ship?
2. Describe a security incident you helped investigate end to end. What was your role, and what changed in your
   detection posture afterward?
3. Walk me through a time you had to reduce false positives on a noisy detection rule without losing coverage of
   the real threat it was built for.
4. Tell me about a time you partnered with a non-security team (IT, Legal, engineering) to get a security
   initiative implemented. What friction came up and how did you resolve it?
5. Give an example of when you had to be the go-to subject-matter expert on something outside your core
   comfort zone. How did you get up to speed fast?
6. Describe a time your detection or security architecture recommendation was rejected or deprioritized. How
   did you respond?
7. Tell me about a mistake in a detection rule or security process you owned — what broke, how did you find it,
   what did you change afterward?
8. As a Staff-level IC without direct reports, how do you drive an initiative that requires other teams to
   change their behavior or priorities?

## Likely technical questions (based on JD's stated stack, pulling from real depth in the master doc)
1. Walk me through how you built and managed Cribl pipelines — what were they routing, and what problems did
   Cribl solve that a simpler tool (Logstash, raw forwarding) didn't?
2. You've built detection-rule orchestration across nine SIEM/EDR platforms via native APIs — walk through the
   architecture. How did you handle the differences between each platform's rule syntax and API model?
3. How did you implement staged/safe rollout for new detection rules, and what metrics did you track to decide
   a rule was ready for full production?
4. Describe your approach to mapping detection content to MITRE ATT&CK — how did you identify coverage gaps
   across 2,300+ rules?
5. Walk through how you've integrated threat intelligence (indicators, TTPs, actor context) into detection
   logic — give a concrete example of a detection you built or tuned because of specific CTI.
6. Cribl and this team likely lean on Elasticsearch/security data lakes — talk through the ES-based platform you
   built at DOE/NNSA: ingestion, transforms, and the UEBA detection layer on top.
7. This role calls for understanding of SAML/OpenID/OAuth2/SCIM. Be direct: "I've done API-level identity work —
   creating and managing tokens, roles, and permissions across many SIEM platforms, and IAM policy/role work on
   AWS/GCP — but I haven't personally configured SAML/OIDC federation flows. I'd want to ramp on that quickly if
   it's core to this role — how central is that to the day-to-day here?"
8. How would you evaluate whether Cribl itself should be expanded within a security stack — what would you look
   at to make that case internally?

## Sharp questions Kyle should ask them
1. "Cribl is obviously central to how this team operates — what does the security team's Cribl footprint look
   like today, and where do you see it expanding?"
2. "What SIEM/data lake is the detection team building against day to day, and how mature is the detection-as-
   code/CI pipeline around it?"
3. "How is the Staff Security Operations Engineer role scoped relative to the rest of the Security Engineering
   and Operations org under the CISO — is this primarily an IC technical-authority role, or does it carry
   informal team-lead expectations?"
4. "What does the SAML/OIDC/OAuth2/SCIM work actually look like in this role day to day — is it more about
   understanding auth flows for detection/investigation context, or hands-on IdP/SSO configuration ownership?"
5. "What's the current state of incident response tabletop exercises and purple-teaming here — is this role
   expected to build that program, or does it already exist?"

## Closing-the-interview script
"This role is a strong match for the detection-as-code and multi-platform SIEM orchestration work I've spent the
last several years building, and I genuinely have hands-on experience with Cribl itself, which isn't something I
get to say often. I'm also being straightforward that the SAML/OIDC/SCIM piece is an area where I have adjacent
but not direct experience — I'd want to know how central that is to the role so I can speak to how fast I'd ramp.
What would be most useful for me to expand on before we wrap up, and what are the next steps from here?"
