# Interview Prep — CrowdStrike, req R29100 ("Sr. Software Engineer - Cloud (Hybrid)", Risk Analytics team)

## Read this first
This req is NOT a remote Data Scientist role — it's a hybrid (2-3 days/week, Sunnyvale, CA) backend
distributed-systems/Golang microservices engineering role on the Risk Analytics team. Confirm the
remote/hybrid question directly and early; don't assume it'll resolve in your favor. See ats_notes.md and
job_link.txt for the full mismatch writeup, including a separate, also-Hybrid "Sr. Data Scientist" req
(R29023) that may come up in conversation.

## Likely behavioral questions
1. Tell me about a time you owned a data platform end-to-end, from ingestion through the analytics/detection
   layer built on top of it.
2. Describe a project where you had to design something from scratch with no existing framework to build on
   (e.g., DOE/NNSA Security Data Integration).
3. Tell me about a time you had to balance model/detection quality against latency, cost, or scale
   constraints.
4. Describe mentoring a less experienced engineer through a technical problem.
5. Tell me about a cross-functional collaboration (e.g., with a SOC, Red Team, or product team) that shaped
   how you built or tuned a detection/analytics system.
6. Describe a time a system you built didn't scale the way you expected — what did you change?

## Likely technical questions
1. Walk through your GCP Dataproc/PySpark EDA workflow — how did you go from raw bucket-stored telemetry to
   a productionized detection model?
2. Describe your device-clustering ML work — what features did you use, and how did you validate the
   clusters were operationally meaningful?
3. Your Kafka/Flink experience has been exposure/familiarity rather than primary ownership — how would you
   ramp up to owning streaming ETL at production scale?
4. This role is primarily Golang — you don't have confirmed Golang experience. How would you approach
   picking up a new strongly-typed systems language quickly, and what's transferable from your Python
   background?
5. Walk through the multi-SIEM detection-as-code CI/CD pipeline you built — how did staged rollout and
   rule-quality metrics work in practice?
6. How would you design a risk-scoring/posture-scoring pipeline that aggregates signals across many data
   sources, given your UEBA/data-transform work at DOE/NNSA?
7. Describe the Common Information Model you built — how did you handle schema drift across 220+ sources?

## Questions to ask them
1. Given the JD lists this as hybrid in Sunnyvale — is there any flexibility for a fully remote candidate,
   or is the 2-3 days/week on-site a hard requirement?
2. How much of this role is building the AI/ML risk-scoring logic itself vs. the backend services and data
   infrastructure that logic runs on?
3. What does the split look like today between Golang and Python in the Risk Analytics team's codebase?
4. How does this team's work connect with the NGSIEM/Agentic AI team's data scientists — is there a path to
   work more directly on the modeling side over time?
5. What does success look like for this role in the first two quarters?

## Salary anchor
Posted band: $140,000–$215,000. Anchor to the top third (~$190,000+) once fit is mutually confirmed — the
$170K floor is cleared even at the band's midpoint.

## Closing-the-interview script
"I'd love to bring the data-pipeline-to-detection-content experience I've built over the last several years
to this team's risk-scoring work — what would you want to see from me in the first 90 days, and is there
anything about my background, including the Golang gap, you'd like me to speak to further?"
