# ATS Coverage & Fit Notes — Grow Therapy, Senior Security Engineer, Data Infrastructure

## Salary check — REMOTE VS. HYBRID TRACK (read this before applying)
This posting has two disclosed bands:
- **Hybrid Commitment (NYC/SF/Seattle, 3 days/week):** $182,000 – $250,000 USD annually
- **Fully Remote Commitment:** $152,000 – $208,000 USD annually

Kyle is remote-only per the master reference. **He should select/confirm the fully-remote track**
($152K–$208K) on the application, not the hybrid option — even though hybrid pays more on paper. The remote
band's midpoint (~$180K) still clears Kyle's $170K floor, and the remote top third (~$195K–$208K) is a
reasonable anchor once fit is confirmed in later-stage conversations. Hybrid would require 3 days/week on-site
in NYC, SF, or Seattle, which conflicts with his remote-only constraint regardless of the higher pay — do not
let the bigger hybrid number pull the negotiation toward accepting an on-site commitment.

## Fit score
Already screened at 6/10 before this build was requested (per the calling instructions) — this note does not
re-run that screen, just flags the honest gaps below for Kyle's awareness.

## Keyword coverage summary

**Direct matches:**
- Hands-on production code / data pipeline and service design — confirmed via 220+ source ingestion pipeline
  ownership at Trend Micro/Cysiv, 50+ Logstash filters, homegrown Apache Beam/GCP Dataflow program
- Cloud IAM (AWS + GCP) — confirmed, though at a smaller organizational scale than enterprise-wide governance
- Secure/governed data access at the API level — confirmed via creation and governance of API tokens, roles,
  and permissions across 10+ SIEM/security platforms as part of an orchestration framework
- "Set direction and execute on a blank canvas" — confirmed via building DOE/NNSA's entire Security Data
  Integration platform from scratch (architecture, ingestion, detection layer, dashboards, data-quality
  monitoring, all built by Kyle)
- Data-quality / trustworthy-pipeline discipline — confirmed via data-quality monitoring/alerting content
  built at both DOE/NNSA and DOE CDM

**Adjacent/transferable (framed honestly, not oversold):**
- **Data classification / automated tagging pipelines that scan production data models and propagate tags
  through lineage** — this is the JD's single biggest ask, and Kyle's closest real analog is the Common
  Information Model (CIM) / data dictionary he designed and built at Trend Micro/Cysiv: standardizing field
  names and types across 220+ log sources so downstream systems could consume data through one consistent
  schema. This is schema standardization, not sensitivity classification or tag propagation specifically —
  the resume and cover letter both frame it explicitly as "the closest real analog," not as literal data-
  classification-pipeline experience.
- **Data lineage** — Kyle has real exposure to lineage-adjacent problems (troubleshooting a multi-source
  ingestion pipeline requires understanding where data came from and how it transformed), but no confirmed
  experience with a formal data-lineage tool or lineage-tracking system. Framed as "awareness," not ownership.

**Real gaps (not claimed anywhere in the resume or cover letter):**
- **Encryption / key management.** No confirmed experience in the master reference with application-layer or
  field-level encryption, envelope encryption, or key-management systems. This is one of the JD's four core
  pillars and a genuine, material gap.
- **Masking, tokenization, redaction.** No confirmed experience building field-level dynamic masking,
  tokenization, or redaction driven by classification tags. Another of the JD's four core pillars, and a
  genuine gap — Kyle's access-governance experience (API tokens/roles/permissions across SIEM platforms) is
  real but is coarse-grained platform access control, not field-level data masking.
- **Securing the data path into AI tooling specifically.** Kyle has real GenAI-for-security experience (prompt
  engineering for detection use cases, using GenAI to orchestrate SIEM APIs), but that is a different thing
  from what this JD asks for — owning authentication/authorization/observability for data connectors and
  pipelines feeding AI tools. Not conflated in the materials.
- **Formal Data Classification Policy authorship/alignment.** No confirmed experience building pipelines
  against a written data classification policy specifically.
- **Communicating security tradeoffs to executive/clinical non-technical audiences.** No specific confirmed
  evidence in the master reference of this exact audience type; not claimed in the materials beyond what's
  generically true of Kyle's work history.

**Bottom line for Kyle:** the resume and cover letter lead with the strongest honest connective tissue (CIM/data
dictionary design, 220+ source pipeline ownership, Cloud IAM, API-level access governance, 0-to-1 platform
building) and do not claim encryption, key management, or masking/tokenization depth anywhere. If this reaches
an interview, expect direct technical probing on the encryption/key-management and masking/tokenization pillars
— be ready to speak to them as adjacent-but-not-owned experience rather than overclaiming in the room.

## Formatting / parseability
Single-column, standard section headings (Core Skills, Professional Experience, Education & Certifications),
no tables/text boxes/icons, contact info in the document body (not header/footer) — passes the formatting
rules in `references/ats-optimization.md`.
