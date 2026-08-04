# ATS Coverage & Fit Notes — CrowdStrike, Principal Data Engineer, LLM/AI Platforms

## Salary check
Posted band (US): **$195,000 – $290,000 base.** Canada band: $210,000 – $320,000 CAD.
Well above Kyle's $170,000+ floor across the entire range. Anchor negotiation to the top third
(~$258,000–$290,000 US) once fit is confirmed.

## Remote / federal check
- **Remote:** Yes — "USA - Remote" plus several Canada-remote location options. Matches Kyle's remote-only
  requirement.
- **Federal contracting:** No. Not applicable — this is a private-sector AI/data platform engineering role.
- **Exclusion list:** CrowdStrike is not on the company exclusion list (Sophos, Binary Defense, Shorepoint,
  Dropzone AI). Clear to proceed.

## Fit score: 5/10 (already screened at intake — this note re-derives the reasoning for the record)

**Honest framing up front:** this is a Principal-level role whose core technical ask is production LLM
engineering (fine-tuning, RAG, agentic workflows via LangChain/LlamaIndex) at Exabyte scale, plus deep
ownership of distributed processing and orchestration infrastructure (Spark/Dask/Flink, Kafka/Pulsar,
Kubernetes, Airflow/Kubeflow, MLOps tooling). Kyle's strongest, most directly comparable experience is
classic data engineering (pipeline/ingestion architecture, schema/metadata design, CI/CD discipline) plus
GenAI *usage* at the prompt-engineering/tooling layer — not GenAI/LLM *platform construction*. The resume and
cover letter lead with the data-engineering material because that's the closest real overlap, and are honest
about not claiming the LLM-platform-engineering or infra-admin depth the JD centers on.

**Real strengths matching the JD:**
- **10+ years progressive data engineering** — confirmed and exceeded (12 years total). Ground-up ingestion
  architecture for 220+ heterogeneous sources, a Common Information Model (schema/metadata standardization —
  a real analog to the JD's "semantic cataloging" ask), and Apache Beam/GCP Dataflow for high-volume
  historical retrieval are all genuine, hands-on data-platform-engineering work.
- **Distributed processing** — Spark/PySpark/SparkSQL confirmed hands-on (GCP Dataproc); this is a direct
  match to the JD's named framework list ("e.g., Spark, Dask, Flink").
- **Cloud platform** — GCP confirmed deeply (Dataproc, BigQuery, Dataflow, serverless/event-driven). JD lists
  AWS/GCP/OCI as acceptable; GCP depth is real and specific.
- **CI/CD and production-deployment discipline** — a full GitLab CI/CD pipeline for detection-as-code, with
  automated unit/integration testing, staged/safe rollout, and formally tracked quality metrics before
  production — this is genuine "ship fast without compromising quality" evidence, a named JD priority.
- **GenAI/LLM usage in production workflows** — real, hands-on: prompt engineering for security triage/
  detection-content generation, and GenAI-driven orchestration of SIEM APIs across 9 platforms. This is
  legitimate LLM-in-production experience, just at the application/tooling layer rather than the
  platform-engineering layer the JD is centered on.
- **Cybersecurity industry background** — direct match to the JD's "bonus points" callout (cybersecurity,
  intelligence, high-compliance industries), and a nice natural tie-in: Kyle has hands-on experience
  ingesting CrowdStrike telemetry itself (DOE/NNSA Security Data Integration project).
- **Data Warehousing** — BigQuery confirmed; Snowflake not confirmed (see gaps).

**Real gaps — flagged honestly, not papered over (per Kyle's explicit request):**
- **Production LLM fine-tuning, RAG, and agentic system engineering is not confirmed.** This is the single
  biggest gap against the JD's core ask ("demonstrable hands-on experience in LLM engineering (fine-tuning,
  prompt engineering, deployment), RAG, and developing agentic workflows"). Kyle's GenAI depth is
  prompt-engineering and tooling-level (using LLMs to do security work), not model fine-tuning, RAG pipeline
  construction, or agent-harnessing/agentic-workflow-framework experience (LangChain, LlamaIndex — not
  confirmed anywhere in the master doc). Not claimed on the resume/cover letter.
- **Deep Spark/Kafka/Kubernetes-admin-level infrastructure is not confirmed.** Spark/PySpark usage for EDA is
  real, but not at the "sharding, partitioning, concurrency at Exabyte scale" systems-architecture level the
  JD wants. Kafka is confirmed only as working familiarity (not ownership); Pulsar and Dask are not confirmed
  at all. Docker is a comfortable-user-level skill; Kubernetes is confirmed only as working within a
  K8s-orchestrated platform as a user — no cluster-admin, node/control-plane ownership, or K8s architecture
  experience. None of this is overstated on the resume.
- **MLOps tooling stack not confirmed** — MLflow, Sagemaker, Vertex AI, Airflow, Kubeflow, Snowflake all
  named in the JD's tech stack with no evidence in the master doc. Not claimed.
- **Principal/Staff-level title and formal technical-leadership/mentorship track record not confirmed.** Kyle
  has served in team-lead/sprint-lead capacity but has never held a formal Principal or Staff engineering
  title, per the master reference. The JD explicitly wants "prior experience in a Principal or Staff level
  engineering role." Not claimed as a prior title anywhere.
- **Advanced degree in CS/Data Engineering not a direct match** — Kyle holds an M.S. Physics (not CS), though
  the JD accepts "equivalent practical experience" as an alternative.
- **"3+ years focused on architecting/building platforms for AI/ML or Data Science at massive scale"** is not
  a clean match — Kyle's data-engineering scale (220+ sources) is real, but it was built for a security-
  detection platform, not an AI/ML/LLM platform specifically. Framed honestly via the GenAI-tooling bullets
  rather than implied as AI/ML platform architecture ownership.

## Keyword coverage summary

**Direct matches:**
- Data Engineering/Platform Engineering, 10+ years — confirmed, exceeded (12 years)
- Distributed data processing (Spark/PySpark/SparkSQL) — confirmed
- Cloud platform (GCP: Dataproc, BigQuery, Dataflow) — confirmed
- CI/CD, automated testing, staged/safe rollout, quality metrics tracking — confirmed
- Data modeling / semantic cataloging (Common Information Model) — confirmed, strong analog
- Python, SQL — confirmed
- Cybersecurity industry experience (bonus point) — confirmed directly

**Adjacent/transferable (named honestly, not oversold):**
- GenAI/LLM experience — framed explicitly as prompt-engineering/tooling-level, not fine-tuning/RAG/agentic
  engineering
- Kafka, Flink — framed as "working familiarity" / "hands-on exposure," not ownership
- Docker/Kubernetes — framed as comfortable-user and platform-user level, not container-orchestration mastery
  or cluster administration
- Cloud IAM (AWS, GCP) — confirmed at real but smaller organizational scale than enterprise account
  governance

**Gaps (not claimed anywhere):**
- Production LLM fine-tuning, RAG pipeline construction, agentic workflow frameworks (LangChain, LlamaIndex)
- MLOps tooling: MLflow, Sagemaker, Vertex AI, Airflow, Kubeflow
- Snowflake, Pulsar, Dask
- Prior Principal/Staff engineering title
- Deep Kubernetes/cluster-admin infrastructure ownership

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, contact info in document body, standard Arial font — passes the formatting rules
in `references/ats-optimization.md`.

## Recommendation
Worth building and submitting given the salary and remote fit, and because the data-engineering + GenAI-
tooling + CI/CD-discipline combination is a genuine, differentiated story even though it's not a 1:1 match to
the JD's LLM-platform-engineering center of gravity. Go into any interview loop clear-eyed: expect early
screening questions to probe fine-tuning/RAG/agentic-framework depth and Kubernetes/infra-admin ownership
directly — be ready to answer honestly that Kyle's LLM experience is at the prompt-engineering/application
layer and his container/K8s experience is as a platform user, not an infrastructure owner, rather than
overclaiming either in the room.
