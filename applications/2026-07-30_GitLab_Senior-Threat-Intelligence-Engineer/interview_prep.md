# Interview Prep — GitLab, Senior Threat Intelligence Engineer

## Likely behavioral questions
1. Tell me about a time threat intelligence changed how you approached a detection or an active investigation.
2. Describe a time you had to decide whether an alert reflected real adversary activity or benign behavior —
   walk through your reasoning.
3. Tell me about operating as the sole owner of a technical function, with minimal existing team structure
   around you (draw on the Cysiv detection-as-code buildout or the DOE/NNSA platform build).
4. Describe a time you built a relationship with an external partner or peer team to get better information/
   context for your work.
5. Tell me about a time you had to learn a new tool or platform quickly and become the go-to person for it.
6. Walk me through how you'd prioritize your first 90 days owning a new, established program (reporting
   templates, tooling, feeds already in place) versus building one from scratch.
7. Tell me about a time you used automation to remove a repetitive manual step from your own workflow.
8. Describe a disagreement with a teammate or stakeholder over how much weight to give an intelligence source.

## Likely technical questions
1. Be ready to answer honestly: "Have you personally administered a Threat Intelligence Platform (MISP,
   OpenCTI, Anomali, ThreatConnect)?" — this is a direct screening question on GitLab's application form. Your
   honest answer: you've consumed and acted on CTI sourced by a dedicated research team (Vedere Labs) rather
   than owned feed ingestion/export yourself — frame this as "closely adjacent, ready to own the platform side
   with the same rigor I've applied to consuming and acting on intel," not as equivalent experience.
2. How would you approach OSINT research on a new adversary group with no existing internal reporting? Be
   ready to acknowledge this is more primary-research-oriented than your current experience, and describe how
   you'd apply your existing CTI-validation instincts to it.
3. Walk through your Python automation experience — what have you automated, and how would that translate to
   maintaining a Threat Intelligence Platform's ingestion/enrichment pipeline?
4. How do you validate whether an indicator or TTP report is credible before acting on it?
5. Describe your Elasticsearch experience in the context of a security data platform — GitLab may ask how this
   maps to their own detection/logging stack (Security Logging is a listed peer team).
6. What's your experience with Purple Team exercises? (JD mentions "Purple Team Flash Operations" — be honest
   this is not a confirmed area; discuss your detection-tuning-from-threat-intel experience as the adjacent
   skill.)
7. How would you structure a Flash Report (ad-hoc threat awareness bulletin) for a technical vs. non-technical
   audience?
8. Malware reverse engineering is listed as "optional but valuable" — be ready to say plainly this isn't a
   confirmed skill, without over-explaining or downplaying your actual strengths elsewhere.

## Questions to ask them
1. What does the existing Threat Intelligence Platform and feed setup look like today, and what's the biggest
   gap in the current tooling I'd be inheriting?
2. How does this role collaborate day-to-day with the SIRT, Red Team, and Security Logging teams mentioned in
   the JD?
3. Since this is a solo TI function reporting to a manager based in Australia, how is the team's success
   measured, and how much autonomy does the role have in setting its own roadmap?
4. What would a strong first 6 months look like in this role, given the program's existing foundation?
5. How does GitLab's "AI as a core productivity multiplier" culture show up concretely in this specific role's
   day-to-day work?

## Salary anchor
Posted band is $140,000–$200,000. Given the real gaps on TIP administration and OSINT/attribution research,
anchor expectations toward the middle of the band rather than the top — this is a stretch role relative to
Kyle's strongest-fit detection engineering applications, and the comp conversation should reflect that honestly
rather than assuming top-of-band leverage.

## Closing script
"This role is a genuine stretch for me in a couple of specific ways — I haven't personally administered a TIP
before — but the core of what you're asking for, using intelligence to actually change detection outcomes, is
exactly what I've spent eight years doing. I'd want to talk through how much ramp-up time is realistic for the
platform-ownership side of the role. What are the next steps from here?"
