# ATS Coverage & Fit Notes — Anthropic, Threat Intelligence Engineer

## Salary check
Posted band: **$320,000 – $405,000 USD annual.** Well above Kyle's $170,000+ floor — anchor negotiation to the
top third of the band (~$375,000–$405,000) once fit is confirmed.

## Fit score: 7/10 (per original screening — this build does not re-screen)
Role sits on Anthropic's Threat Intelligence team: building automated detection systems from disparate
signals, YARA rule infrastructure, integrations with external CTI platforms via MCP servers, GenAI-powered
TTP extraction/hunting-query generation, behavioral analytics, and investigator feedback loops. "Remote-
Friendly" with ~25% office time expected (SF/DC) — Kyle has previously confirmed he's fine proceeding on this
basis for comparable Anthropic postings.

## Keyword coverage summary

**Direct matches:**
- Threat intelligence integration into detection logic (indicators, TTPs, actor/campaign context) — confirmed,
  real differentiator, not just passive CTI consumption
- Threat intel used for own research/false-positive validation — confirmed
- CTI source exposure — Vedere Labs (Forescout's in-house threat research team) named directly
- Building automated detection systems via external API integrations — confirmed via the nine-platform
  multi-SIEM/EDR orchestration framework (Sentinel, Defender, Chronicle, Splunk, CrowdStrike, SentinelOne,
  Sumo Logic, XSIAM, Devo, plus prior ArcSight)
- Strong Python/SQL for detection logic, pipelines, automation — confirmed
- Integrating external APIs / building data ingestion systems — confirmed, this is the core of the multi-SIEM
  orchestration work (per-technology adapters, not just one integration)
- GenAI/LLM understanding and using it for automation — confirmed: prompt engineering for security use cases,
  using GenAI to interact with SIEM APIs for orchestration, reusable GenAI-powered "skills" for cross-SIEM rule
  conversion — maps closely to the JD's "use Claude to extract TTPs and generate hunting queries"
- Behavioral analytics / anomaly detection systems — confirmed directly: UEBA detection layer built on
  Elasticsearch transforms, time-series anomaly detection (auth behaviors, process chains)
- Establishing feedback loops with investigators to tune detection and reduce false positives — confirmed via
  current TSSOC work supporting Treasury SOC analysts, and the formal rule-quality-metrics/staged-rollout
  practice in the multi-SIEM pipeline
- Translating investigator/stakeholder needs into technical requirements — confirmed via TSSOC (building
  analytics directly for SOC investigator workflows) and cross-team API/adapter work
- Comfortable taking v0 systems to production, iterating on feedback — confirmed via the multi-SIEM
  orchestration framework's staged/safe rollout practice
- Top Secret Clearance ("strong candidate" plus, explicitly listed) — confirmed, current, Treasury-sponsored

**Adjacent/transferable (framed honestly, not oversold):**
- Data pipeline orchestration tools (Airflow, DBT, or similar) — Kyle has no confirmed Airflow or DBT
  experience specifically. Framed instead via real pipeline-orchestration muscle that transfers conceptually:
  GitLab CI/CD-based detection-as-code pipeline, Apache Beam/GCP Dataflow for historical data retrieval, and
  Logstash/CIM data-engineering work. Not claimed as DBT/Airflow experience anywhere.
- MCP servers or similar AI tool integrations — not literally confirmed. Framed as adjacent: "using GenAI to
  interact with SIEM APIs for detection-content orchestration" is real, hands-on GenAI-to-API integration work,
  just not built on the MCP protocol specifically. Cover letter and resume describe this honestly as GenAI/API
  orchestration, not as MCP server development.
- Threat correlation techniques — confirmed via CTI-to-detection-rule integration and alert enrichment work,
  but not the specific multi-source correlation across named platforms (VirusTotal, Censys, Urlscan) called
  out in the JD. Cover letter draws the parallel to the multi-platform API integration work without claiming
  hands-on use of those specific tools.

**Real gaps (not claimed anywhere in resume or cover letter):**
- **YARA rules** — no confirmed hands-on YARA rule-writing experience in the master reference. Kyle's rule
  authoring is native SIEM/Elasticsearch detection rules and cross-SIEM rule-syntax conversion, not YARA
  specifically. Not claimed.
- **MISP / STIX/TAXII** — no confirmed experience with these specific threat-intel-sharing frameworks. Not
  claimed (this is listed as "strong candidates may also have," not a must-have).
- **Web scraping / data extraction at scale** — no confirmed experience scraping external sources; Kyle's
  data-ingestion work is log/telemetry pipeline engineering (Logstash, Beats, Beam/Dataflow), not web scraping.
  Not claimed.
- **DBT / Airflow specifically** — see adjacent note above; genuinely not used these named tools.
- **VirusTotal / Censys / Urlscan** — no confirmed direct hands-on use of these specific platforms.

## Formatting / parseability
Single-column, standard section headings (Security Clearance, Core Skills, Professional Experience, Education
& Certifications), no tables/text boxes/icons, contact info in the document body — passes the formatting rules
in `references/ats-optimization.md`.

## Recommendation
Strong package for this req — the threat-intel-integration + multi-platform API orchestration + GenAI-for-
security combination is a genuinely close match to a role most candidates would only hit one or two legs of.
Real gaps are concentrated in specific named tools (YARA, MISP/STIX-TAXII, Airflow/DBT, web scraping) rather
than the underlying skill categories — worth being ready to speak to how quickly those specific tools would be
picked up given the adjacent muscle memory, without overclaiming direct experience in the room.
