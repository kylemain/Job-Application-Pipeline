# ATS Notes — OpenAI, Data Engineer, CPU & Storage

Posting: https://jobs.ashbyhq.com/openai/0c0fe7aa-24fb-4bad-aa30-3f68f1418e37
Team: Scaling Analytics, within OpenAI's Industrial Compute organization. Builds the data/software systems that
help Industrial Compute understand, plan, and operate infrastructure (capacity, hardware, storage, infra
software, operations) at global scale.

**Role scope (per full JD, not just the initial-scan summary):** This is much more backend/software
engineering than a traditional analytics-pipeline role. It's about building integrations and services that
collect, normalize, and reconcile CPU/storage/capacity/inventory/operational data from internal infra
platforms, vendor APIs, databases, object storage, and capacity-management systems — deciding where those
integrations should live (existing service, orchestration framework, scheduled workload, or purpose-built app)
and building data-quality/reconciliation mechanisms to catch missing, stale, or inconsistent data across
sources. It is not primarily about hardware-telemetry monitoring/dashboarding itself — it's the plumbing
underneath that kind of reporting.

**Location:** San Francisco. Listed by Kyle as hybrid in the initial scan; the rendered JD body itself does not
state a specific in-office cadence, only "Location: San Francisco" with no remote option mentioned anywhere.
Treating this as an SF hybrid/in-person role, not remote — flagging clearly per Kyle's remote-only preference,
even though this posting was already fit-screened and passed before this build.

## Keyword coverage

| JD keyword/requirement | Coverage | Notes |
|---|---|---|
| 4+ years SWE/data eng/backend/infra eng | Direct match | Kyle's total professional experience is 12 years (since Jan 2015, Experian) — real total stated in resume/cover letter, not the JD's stated minimum mirrored back. |
| Strong Python programming, production software/services/automation/data integrations | Direct match | Python confirmed extensively across all roles; production data-integration work is the core of the Cysiv era and the multi-SIEM orchestration framework. |
| Strong SQL, relational databases, large operational datasets | Direct match | SQL confirmed in master doc; large-scale operational log/security data is the core of Kyle's entire career. |
| Integrating systems via REST APIs, SDKs, databases, object storage, messaging systems | Direct match (APIs, databases, object storage) / Adjacent (SDKs, messaging) | Native REST API integration confirmed directly (multi-SIEM orchestration framework — Splunk, Sentinel, Defender, Google SecOps, CrowdStrike, SentinelOne, Sumo Logic, XSIAM, Devo, ArcSight, plus ES API). Object storage confirmed via GCS buckets (Spark jobs loading data from cloud storage). SDK-specific integration work is not separately documented — not claimed as a distinct SDK claim. Messaging systems: Kafka/Flink exposure is real but described honestly in resume as "working exposure," not ownership. |
| Building reliable batch/scheduled/async workloads in production | Direct match | Apache Beam / GCP Dataflow program built and run in production to retrieve historical cold-storage data on demand. |
| SWE fundamentals: testing, debugging, version control, observability, maintainable system design | Direct match (testing, version control) / Adjacent (observability) | Automated testing and staged/safe rollout confirmed via the GitLab CI/CD detection-as-code pipeline; Git confirmed. "Observability" as a named discipline/toolset (e.g., Prometheus/Grafana-style infra monitoring) is not confirmed in the master doc — Kyle's closest analog is Kibana dashboarding and data-quality monitoring/alerting on Elasticsearch, which is real but not general infra-observability tooling. Framed honestly, not claimed as Prometheus/Grafana experience. |
| Reasoning about data schemas, system boundaries, data ownership, consistency, failure modes across distributed systems | Direct match | Common Information Model (canonical data model) design across 220+ sources is a direct, strong analog; connector/collector health monitoring and data-quality/reconciliation work covers consistency and failure-mode reasoning. |
| Navigating unfamiliar codebases/infra environments | Adjacent | Real, evidenced by onboarding new log sources/connectors continuously across employers, but not framed as literal "codebase" navigation in a general-purpose software engineering sense — resume/cover letter keep this honest. |
| Partnering with infrastructure, backend, platform, or systems engineering teams | Adjacent | Kyle has partnered cross-functionally on detection/data platforms, but not specifically with infrastructure/systems engineering teams in a hardware/compute context — not overstated. |
| Preferred: compute, storage, capacity, fleet management, inventory, or hardware lifecycle data | **Gap** | No confirmed hardware/GPU-cluster/fleet-management/hardware-lifecycle-data experience anywhere in the master doc. Connector/collector health monitoring (Cysiv) is a data-pipeline-reliability analog, not literal hardware/fleet telemetry — framed as an analog in the cover letter, not claimed as direct fleet-management experience. |
| Preferred: Airflow or similar scheduling/orchestration | **Gap** | Not in the master doc's confirmed skills. Not claimed anywhere. |
| Preferred: relational DBs, object storage, offline tables, analytical data systems | Direct match | BigQuery, GCS object storage, PySpark/Dataproc analytical processing all confirmed. |
| Preferred: data-quality/reconciliation mechanisms across systems | Direct match | This is one of Kyle's strongest, most literal matches — data-quality monitoring/alerting content built at both DOE/NNSA SDI and Cysiv. |
| Preferred: CPU platforms, storage systems, distributed systems, cloud infrastructure | Adjacent (distributed systems, cloud infra) / **Gap** (CPU platforms, storage systems specifically) | Cloud infra (AWS/GCP/Azure) and light distributed-systems exposure (Kafka/Flink) are confirmed; no confirmed CPU-platform or storage-system-specific engineering experience. Not claimed. |
| Preferred: hyperscale/cloud/AI infra environments | **Gap** | No confirmed direct hyperscale/AI-infra environment experience (Kyle's cloud work is GCP/AWS/Azure at the scale of security data platforms, not hyperscale compute/storage infra). Not claimed. |

## Summary for Kyle

**Real, honest matches this resume leans on:** the Common Information Model/canonical-data-model work across
220+ heterogeneous sources, connector/collector health monitoring and troubleshooting, data-quality/
reconciliation monitoring, native REST API integration work across a dozen+ third-party platforms (with token/
role governance and multithreaded orchestration), Apache Beam/GCP Dataflow batch workloads, and PySpark/
Dataproc/BigQuery. These map onto the JD's actual day-to-day (integration engineering across heterogeneous
systems, data-quality/reconciliation, batch workloads) more literally than a generic "data engineer" resume
would.

**Real gaps, not papered over:**
- No confirmed hardware/GPU-cluster-specific telemetry, fleet-management, or hardware-lifecycle-data
  experience — the connector/collector health-monitoring work is offered as an analog, not a direct claim.
- No confirmed C/C++ or low-level systems programming (not mentioned in the JD's required skills, but a
  reasonable follow-up assumption for infra-adjacent SWE roles — not claimed).
- No confirmed Airflow or equivalent scheduler/orchestration tool.
- No confirmed Prometheus/Grafana-style infra-monitoring tooling — Kibana/ES-based monitoring is real but not
  the same category of general infra observability tooling.
- No confirmed hyperscale/AI-infra-specific environment experience.

**Location:** SF-based, hybrid per Kyle's initial note; the rendered JD itself doesn't restate a remote option.
Not a fully remote role — flagging per Kyle's stated remote-only preference even though this posting already
cleared the fit screen.

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, contact info in the document body. Passes the formatting rules in
`references/ats-optimization.md`.
