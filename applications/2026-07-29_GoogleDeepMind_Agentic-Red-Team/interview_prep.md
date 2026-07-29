# Interview Prep — Google DeepMind, Senior Security Engineer, Agentic Red Team

**Heads up going in:** this role's stated minimum bar is 5 years of hands-on Red Teaming, Offensive Security, or Adversarial ML experience, plus experience developing exploits for GenAI models. Kyle's real background is defensive detection engineering + GenAI tooling, not offensive security. Expect this gap to come up directly and early — the prep below leans into how to answer that honestly while making the strongest possible case for transferable value.

## Likely behavioral questions
1. Walk me through your experience with red teaming or offensive security. (Answer honestly: primarily defensive/detection-side; pivot immediately to adversary-technique depth via ATT&CK-mapped detection work and genuine interest in moving toward the offensive side.)
2. Tell me about a time you had to think like an attacker to build an effective defense.
3. Describe a project where you had to learn a fundamentally new domain quickly.
4. How do you approach ambiguity when a "vulnerability" doesn't have a clean, deterministic reproduction path (relevant to non-deterministic LLM behavior)?
5. Tell me about a time you built a tool that changed how a team worked, not just automated a single task.
6. How do you communicate a technical security finding to a non-security engineering team so they'll actually act on it?

## Likely technical questions
1. How would you approach red-teaming an agentic AI system if you'd never done offensive security work before? (This is the central question of the interview — prepare a concrete, thoughtful answer: study existing attack taxonomies, pair with the team's Auto Red Teaming framework, apply detection-engineering intuition about attacker TTPs in reverse.)
2. What do you know about prompt injection, tool-use escalation, or training data extraction as attack classes? (Be honest about depth — conceptual understanding from security-industry exposure, not hands-on exploit development.)
3. Walk through your MITRE ATT&CK-based detection work — how does deep adversary-technique knowledge translate to anticipating novel attacks rather than just detecting known ones?
4. Describe your GenAI tooling work in detail — what were you actually using LLMs to do, and how comfortable are you with agentic workflows/chain-of-thought reasoning specifically?
5. How would you build an "Auto Red Teaming" regression framework, drawing on your CI/CD and automated-testing experience?
6. What's your approach to writing exploit code or attack tooling in Python, Go, or C++?

## Sharp questions to ask them
1. Given the 5-year red-teaming/offensive-security bar in the posting, what onboarding or ramp-up support exists for someone with deep adversarial-technique knowledge from the defensive side but limited hands-on offensive experience?
2. How does the Agentic Red Team's work feed back into the Auto Red Teaming regression framework mentioned in the JD — is that framework mature, or still being built out?
3. What does the balance look like between novel manual attack discovery and building the automated tooling to scale those findings?
4. How is success measured for this role — number of findings, severity, or something tied to launch-readiness timelines?
5. What's the actual on-site expectation across the three listed locations (Mountain View, NY, Zürich) — is any remote flexibility possible?

## Salary anchor
Posted range: $174,000–$253,000 (US) + 15% bonus target + equity + benefits. Anchor to the top third (~$226K+ base) if it gets to an offer — this comfortably clears Kyle's $170K+ floor even considering the stretch nature of the role.

## Location note
No remote option anywhere in the JD — Mountain View, NY, or Zürich only. Confirm actual flexibility directly; this was built and submitted (if it proceeds) with that constraint already flagged and accepted per Kyle's explicit instruction.

## Closing-the-interview script
"I know the core ask here is hands-on red-teaming and exploit development, which isn't where my track record is strongest — but I bring genuine depth in adversary-technique knowledge and GenAI tooling that I think transfers faster than starting from zero. I'd rather be upfront about that than oversell it. What would help you evaluate whether that gap is bridgeable in this role?"
