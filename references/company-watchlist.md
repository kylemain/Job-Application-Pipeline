# Company Career-Page Watch List

Used by the `daily-job-search-pipeline` scheduled task to check specific employers' own career sites
for new openings matching Kyle's target roles, in addition to the Indeed/ZipRecruiter/Dice searches.

For each entry: check the listed URL (navigate + read rendered text, since most are JS-rendered).
Search/filter within the page for roles matching: detection engineering, threat hunting, security
data science/ML security, security engineering management/lead, and data engineering (general).

## Big Tech / Cloud

- Google — https://www.google.com/about/careers/applications/jobs/results (search "security engineer", "detection")
- Amazon — https://www.amazon.jobs/en/search?base_query=security+engineer
- Microsoft — https://jobs.careers.microsoft.com/global/en/search?q=security%20engineer
- Meta — https://www.metacareers.com/jobs/?q=security
- Netflix — https://explore.jobs.netflix.net/careers (confirmed working — used for the Workforce Security application)
- Roblox — https://careers.roblox.com/jobs
- Apple — https://jobs.apple.com/en-us/search?search=security
- Salesforce — https://careers.salesforce.com/en/jobs/
- Uber — https://www.uber.com/us/en/careers/list/?query=security
- Airbnb — https://careers.airbnb.com/positions/
- Databricks — https://www.databricks.com/company/careers/open-positions
- Snowflake — https://careers.snowflake.com/us/en/search-results?keywords=security

## Elasticsearch / ES-based stack (added 2026-07-30 — strong fit, see master reference)
Kyle has deep, cross-employer hands-on Elasticsearch experience (DOE/NNSA SDI, CISA CDM, and Trend Micro/Cysiv's next-gen SIEM were all ES/Kibana-based, including detection rules/queries written directly against ES indexes) plus hands-on Cribl pipeline experience — underrepresented on his current resume. Elastic itself and any company running an ES-based SIEM/security-analytics/data-pipeline stack should be treated as strong-fit targets; flag any posting that mentions Elasticsearch, ELK, Elastic Security, or Cribl even if the title doesn't obviously say "detection engineer."

- Elastic — https://www.elastic.co/careers (Elastic Security; fully remote-first company; direct match — Kyle has built next-gen SIEM content in ES/Kibana at Cysiv and an entire ES-based detection platform at DOE/NNSA)
- Cribl — https://cribl.io/careers/ (observability/data-pipeline company; Kyle has hands-on experience creating and managing Cribl pipelines directly)
- Datadog — https://careers.datadoghq.com/ (Cloud SIEM/security monitoring runs on their own log pipeline, ES-adjacent skill set)
- Chronosphere — https://chronosphere.io/careers/ (observability platform, data-pipeline overlap)

## AI Labs

- OpenAI — https://openai.com/careers/search/ (search "security engineer", "detection & response"; applications go through Ashby at jobs.ashbyhq.com/openai — added 2026-07-28 after applying to two D&R reqs)
- Anthropic — https://www.anthropic.com/jobs (search "security engineer", "detection & response"; applications go through Greenhouse at job-boards.greenhouse.io/anthropic — added 2026-07-28 after applying to two D&R reqs. Note: Anthropic's security roles have consistently required 25%+ in-office time, conflicting with Kyle's remote-only rule — still worth scanning and flagging per his explicit prior decision to proceed anyway on comparable postings)
- xAI — https://job-boards.greenhouse.io/xai (search "security engineer", "detection & response"; applications go through Greenhouse. Had an open D&R req (including a Japan-based one) as of 2026-07-27, but didn't clear the remote-only/salary-floor bars as cleanly as the OpenAI/Anthropic reqs at the time — re-check each scan since roles/locations change)
- Google DeepMind — https://www.google.com/about/careers/applications/jobs/results?company=DeepMind (the deepmind.google/careers marketing page has no listing widget; its "View open roles" button routes here, to Google's unified careers board filtered by company=DeepMind — search/filter within this URL, not the marketing page. Checked 2026-07-29: none of DeepMind's postings offer remote work, all are Mountain View/NY/London/Zurich/Tel Aviv on-site or hybrid — re-check each scan but expect the no-remote pattern to hold)
- Scale AI — https://scale.com/careers (search "security engineer", "detection & response" in the on-page search box — the listing widget (344+ roles) DOES render fully in a real browser, the earlier "stuck on LOADING POSITIONS" finding was a rendering-timing issue, not a broken page; give it 2-3 seconds after page load before reading. Job detail pages are at scale.com/careers/<job-id>, reached via the job title link — the "Apply" button opens an unrendered modal, not useful for reading the JD. Checked 2026-07-29: found and built a package for "Security Engineer, Detection & Response" — re-check each scan since new reqs open frequently)
- Perplexity — https://www.perplexity.ai/careers (search "security engineer", "detection & response"; checked 2026-07-27, same result as above — re-check each scan)
- Mistral — https://mistral.ai/careers (search "security engineer", "detection & response"; checked 2026-07-27, same result as above — re-check each scan)

## Cybersecurity / Detection & Response vendors

- CrowdStrike — https://www.crowdstrike.com/careers/
- SentinelOne — https://www.sentinelone.com/careers/
- Palo Alto Networks — https://jobs.paloaltonetworks.com/
- Arctic Wolf — https://arcticwolf.wd1.myworkdayjobs.com/External (Workday; careers landing page redirects here)
- Rapid7 — https://www.rapid7.com/careers/open-positions/
- Splunk (Cisco) — https://splunk.wd1.myworkdayjobs.com/splunkcareers
- Sumo Logic — https://www.sumologic.com/careers/
- Devo — https://www.devo.com/careers/
- Vectra AI — https://www.vectra.ai/about/jobs (confirmed working)
- Exabeam — https://www.exabeam.com/company/careers/
- Securonix — https://www.securonix.com/company/careers/
- Abnormal Security — https://abnormalsecurity.com/careers
- Dropzone AI — https://www.dropzone.ai/careers (confirmed working)
- Torq — https://torq.io/careers/
- Tines — https://www.tines.com/careers
- Panther — https://panther.com/careers (JS-rendered; use Chrome tools, not plain fetch)
- Anvilogic — https://www.anvilogic.com/careers
- Wiz — https://www.wiz.io/careers
- Cybereason — https://www.cybereason.com/careers
- Trellix — https://www.trellix.com/about/careers/
- HackerOne — https://www.hackerone.com/careers (already have one open application here — dedupe by exact posting URL, not by company, since a second/different role there is still fair game)
- Corelight — https://corelight.com/company/careers/ (network detection & response, built on Zeek — direct overlap with Kyle's Zeek/Suricata detection background)
- Exaforce — https://www.exaforce.com/careers (agentic AI SOC platform; $125M Series B, added 2026-07-27)
- Armis — https://www.armis.com/armis-careers/ (AI-driven asset intelligence & threat detection across IT/OT/IoT; $200M round at $4.4B valuation)
- Permiso Security — https://permiso.io/careers (identity threat detection & response / ITDR, including AI agent identity security)
- Radiant Security — https://radiantsecurity.ai/careers/ (AI-native SOC alert triage and investigation)
- Orca Security — https://orca.security/about/careers/ (cloud security/CNAPP, agentless — Wiz competitor)
- Fluidstack — https://jobs.ashbyhq.com/fluidstack (GPU-powered AI data center builder/operator; $830M Series A at $7.5B valuation Jan 2026, reportedly in talks for $1B more at $18B; building ~$50B of AI infra with Anthropic. Added 2026-07-30 after applying to Staff Detection Engineer. Note: postings so far require picking an in-person office location (Austin/NY/SF/Phoenix/Seattle/London) despite listing tags suggesting remote — flag this each time rather than assuming remote-eligible)
- Hunters.ai — https://www.hunters.ai/careers (SOC platform, detection-as-code framing — direct overlap with Kyle's multi-SIEM orchestration background)
- Query.ai — https://www.query.ai/careers/ (federated security data/threat-hunting query platform)
- GreyNoise — https://www.greynoise.io/careers (internet-scan threat intelligence)
- Recorded Future — https://www.recordedfuture.com/careers (threat intel, Mastercard-owned)
- Intezer — https://intezer.com/careers/ (AI-driven detection/triage automation)
- Netskope — https://www.netskope.com/careers
- Proofpoint — https://www.proofpoint.com/us/careers
- Darktrace — https://darktrace.com/careers
- Censys — https://censys.io/careers (already saw an open Staff AppSec Engineer posting here during a scan 2026-07-30 — screen carefully, that one was a domain mismatch, but other reqs may fit better)
- Chainguard — https://www.chainguard.dev/careers (seen during a scan 2026-07-30 — supply-chain/AppSec focus, screen for detection-specific reqs specifically)
- Axonius — https://www.axonius.com/careers (asset intelligence/attack surface management, same category as Armis)
- Obsidian Security — https://www.obsidiansecurity.com/careers (SaaS security posture/detection)
- Material Security — https://material.security/careers
- Push Security — https://pushsecurity.com/careers

## Fintech / Crypto Security

- Coinbase — https://www.coinbase.com/careers (remote-first, strong in-house security/detection team)
- Chainalysis — https://www.chainalysis.com/careers (blockchain-specific detection/threat intel)
- TRM Labs — https://www.trmlabs.com/careers (blockchain intelligence)

## Broader Remote-First Tech (screen for specific security-eng/data-eng reqs, not every open role)

- GitLab — https://about.gitlab.com/jobs/all-jobs/ (fully remote; has an in-house security team)
- Cloudflare — https://www.cloudflare.com/careers/jobs/
- Confluent — https://careers.confluent.io/
- Reddit — https://www.redditinc.com/careers
- Stripe — https://stripe.com/jobs/search

## Maintenance notes

- If a URL 404s or redirects to a generic "all jobs" page with no way to filter, note it in the daily
  summary so Kyle can supply a corrected/direct link.
- Kyle may add or remove companies from this list at any time — treat it as the current source of truth
  for which employers to check, not the four-category keyword search.
