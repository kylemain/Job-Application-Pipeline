# ATS Optimization Notes — HackerOne, Manager, Data Engineering

## Keyword coverage

**Direct matches:**
- "8+ years of experience building and optimizing data pipelines, products, and solutions" → direct match —
  220+ source ingestion pipelines, PySpark/Dataproc, Apache Beam/Dataflow, GCP serverless enrichment
- "Proven track record of launching source of truth data marts" → adjacent/strong match, framed honestly —
  Kyle built a Common Information Model (a company-wide data dictionary standardizing schema across 220+
  sources), which is the same underlying discipline (one trustworthy, consistent schema) even though it wasn't
  branded as a "data mart" program specifically
- "Strong proficiency in SQL for data manipulation" → direct match
- "Strong proficiency in creating compelling data stories using data visualization tools" → adjacent — Kyle has
  built custom Kibana dashboards/visualizations directly on modeled data, but Looker/Tableau/Sigma/Domo/PowerBI
  specifically are not confirmed in the master doc; framed as dashboarding experience broadly, not claiming the
  named BI tools directly

**Gaps (real, not papered over):**
- **Tool stack mismatch**: the JD's minimum qualifications explicitly require "extensive experience" with
  Airflow, Snowflake, Meltano, Fivetran, and DBT. None of these are in Kyle's confirmed skills inventory — his
  data engineering stack is Elasticsearch/Logstash, GCP Dataproc/Dataflow/BigQuery, and PySpark. This is the
  same category of gap that failed the LeafLink Staff Data Engineer screen on 07-30 ("core required tool stack
  does not overlap... real tool-stack mismatch, not just adjacent framing") — this is a materially larger risk
  than a typical "adjacent" gap.
- **Leadership requirement**: JD requires "at least 3+ years in a leadership role" as a stated minimum
  qualification (not preferred). Kyle has team-lead/sprint-priority-direction experience on Treasury's SOC, but
  no formal management title, headcount, or tenure that would clearly satisfy "3+ years in a leadership role."
  This is a harder bar than the similar gap flagged on the Qualia EM application this week.
- **Domain framing**: the role explicitly wants an "Analytics Engineer, Business Intelligence Engineer, or
  similar" background building source-of-truth data marts for business stakeholders (Salesforce, Clari,
  Gainsight, Workday data referenced as "nice to have" source systems). Kyle's data engineering background is
  security-telemetry/SIEM-ingestion-flavored, not business-analytics/BI-flavored — a real specialization
  difference, not just a terminology gap.
- **Location**: role is listed "Remote" but the JD explicitly states it's "targeted for candidates within ~50
  miles of Boston, Austin, or Washington DC" for occasional in-person collaboration. Kyle is based in Dallas/
  Ft. Worth, outside all three hub radii — this is a real geographic-fit risk despite the "Remote" label, not a
  guaranteed pass through screening.
- **Deadline**: posting lists "Deadline to Apply: July 31, 2026 at 5:59 PM CDT" — the same day this package was
  built. If Kyle wants to actually submit, this needs to happen today.

## Formatting check
Single-column, no tables-for-layout, standard section headings, contact info in document body, standard Arial
font. One page confirmed via PDF render (resume_page-1.jpg, cover_page-1.jpg), clean line wraps, no overflow.
