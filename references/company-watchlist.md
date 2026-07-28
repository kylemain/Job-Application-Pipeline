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

## Maintenance notes

- If a URL 404s or redirects to a generic "all jobs" page with no way to filter, note it in the daily
  summary so Kyle can supply a corrected/direct link.
- Kyle may add or remove companies from this list at any time — treat it as the current source of truth
  for which employers to check, not the four-category keyword search.
