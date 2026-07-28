# Interview Prep — flexEngage, Senior Data Engineer

## Likely behavioral questions
1. Tell me about a time you were the first person to own a function (data engineering, in this case) at a company — how did you decide what to build first?
2. Describe setting a technical standard that other engineers had to adopt after you — how did you get buy-in?
3. Tell me about a messy, inconsistent data source you had to bring into a clean pipeline (echoes 220+ sources at Cysiv).
4. How have you balanced building new pipeline features against keeping existing pipelines healthy/monitored?
5. Describe a time a pipeline failed silently — how did you find out, and what did you change afterward?
6. Tell me about working with a small/lean team (startup context) versus a larger org — how did your approach change?
7. How do you decide when to buy/adopt an existing tool (e.g., Airflow) versus build something homegrown (like "Loggify")?

## Likely technical questions
1. Walk through how you'd design an ETL/ELT pipeline for flexEngage's transactional data (receipts, shipping notifications) from scratch.
2. What's your approach to schema standardization across many inconsistent source systems — walk through the Common Information Model work.
3. How would you approach data-quality monitoring and alerting for a new pipeline with no existing observability?
4. You haven't used Airflow — how would you ramp on it quickly, and what parallels does your Apache Beam/Dataflow experience give you?
5. Describe your SQL/data-warehouse experience — how would you approach modeling a new analytical warehouse (Snowflake) if you haven't used that specific platform?
6. How do you structure a CI/CD pipeline for data engineering code (testing data pipeline changes safely)?
7. What's your experience with cost-efficient pipeline design — how have you optimized a pipeline for cost or performance at scale?
8. How would you approach provisioning infrastructure as code if the team wants Terraform, given your CI/CD-centric (not deep IaC) background?

## Questions to ask them
1. What does "first full-time data engineer" mean in practice — is there existing pipeline code/infra I'd inherit, or is this greenfield?
2. What's the target data warehouse/stack decision status — is Snowflake already chosen, or still open?
3. How does the data engineering function fit alongside the existing product/engineering team structure as headcount grows?
4. What does success look like in the first 90 days for this role?
5. Given this is VC-backed and Series-stage, what's the runway/stability picture, and how does that shape the data roadmap?

## Salary anchor
**Compensation not disclosed in the posting.** Kyle's floor is $170,000+. This is a smaller VC-backed startup (YCombinator grad), so confirm the actual range early — don't assume it clears the floor. If the initial range comes in below $170K, weigh equity/upside explicitly against the cash gap before proceeding further.

## Closing-the-interview script
"This is exactly the kind of build-it-from-scratch problem I've done before — setting the pipeline standards that a growing team builds on. I'd love to understand the timeline for this hire and what the next steps look like."
