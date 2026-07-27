---
name: job-application-pipeline
description: "Use this skill whenever Kyle Main pastes in a job description, a job posting URL, or asks to apply to a job, tailor a resume, write a cover letter, check ATS compatibility, assess fit/salary for a role, or prep for an interview. Also trigger for requests to update the master reference doc with new skills, roles, or history. This covers the full application pipeline: fit/salary screening, resume tailoring, cover letter writing, ATS optimization, visual QA, and interview prep — make sure to use this any time a JD or posting is shared, even if the user just says 'what do you think of this job' or pastes a listing with no explicit instruction."
---

# Job Application Pipeline (Kyle Main)

Codified judgment for screening, tailoring, and producing job application materials, so decisions (fit, positioning, formatting) are made consistently instead of re-derived every time.

## Step 0 — Always read the master reference first

Before doing anything else in this skill, read `master-reference/kyle-main-master.md` in full. It contains:
- Complete work history (including the expanded Shorepoint section — SDI/NNSA and TSSOC projects that are NOT on the current public-facing resume)
- Full skills inventory, including skills confirmed by Kyle but not yet reflected on his resume (multi-SIEM detection-as-code/orchestration, GenAI-for-security tooling, Docker/containers, GitLab CI/CD)
- Salary floor ($170,000+)
- Fit/screening rules (no federal contracting roles)
- Formatting rules

Never invent or infer a skill/experience that isn't in this file. If a JD wants something adjacent to a confirmed skill but not actually confirmed (e.g., deep Kubernetes architecture vs. confirmed "comfortable Docker user"), ask Kyle rather than assuming, or note it as a stretch/learning-oriented point rather than claimed expertise.

## Fixed per-application workflow

Run these steps **in order**. Don't skip the screening steps to jump to building documents.

### 1. Salary check
State the posting's disclosed band (or note if unlisted). Compare to the $170,000+ floor. If the band tops out below floor, or the realistic midpoint is meaningfully below it, say so plainly up front — don't bury this after building materials.

### 2. Fit assessment + fit score
Give an honest fit assessment (not just a cheerleading summary):
- Score fit 1-10 based on how well the confirmed skills inventory matches the JD's actual requirements
- Explicitly flag: is this remote? Kyle only wants fully remote roles — flag on-site/hybrid/relocation requirements clearly, still let him decide, but don't proceed to build materials by default
- Explicitly flag: is this a federal contracting role? (Kyle no longer wants these — flag clearly, still let him decide, but don't proceed to build materials for federal roles without him confirming he wants to anyway)
- Flag any real mismatches (seniority level, domain, tech stack) rather than glossing over them
- If fit is weak (score ≤ 4) or it's a flagged federal role, stop here and ask Kyle whether he still wants materials built, rather than assuming yes

### 3. Resume tailoring
- Start from the master reference, not the existing PDF resume — the master doc has more content (SDI/NNSA, TSSOC, multi-SIEM orchestration, GenAI tooling) than what's currently public
- Reorder/select experience and skills to bubble up whatever the JD asks for most:
  - If JD emphasizes multi-cloud SIEM/detection platform work → lead with the multi-SIEM orchestration + CI/CD detection-as-code material
  - If JD emphasizes ML/data science → lead with EDA, clustering, time-series anomaly detection, PySpark/Dataproc work
  - If JD is a non-security data engineering role → lead with the data pipeline/CIM/Dataflow work, de-emphasize security-specific framing without misrepresenting it
  - If JD emphasizes GenAI/LLM applications → lead with the prompt-engineering-for-security and SIEM-orchestration-via-GenAI work
- One page. Titles can be lightly adjusted toward the target positioning (e.g., "Senior Detection Engineer" vs. "Senior Cybersecurity Engineer") without misrepresenting the actual work done
- See `references/ats-optimization.md` for keyword/formatting rules to run against the JD before finalizing
- Build as .docx per the docx skill (`/mnt/skills/public/docx/SKILL.md`) — read that skill before generating

### 4. Cover letter
One page: sharp opening tied to the specific role/company → 1-2 proof-point paragraphs mapped directly to the JD's top requirements, pulling from master doc specifics (real project names, real numbers — e.g., "2,300+ detection rules across the MITRE ATT&CK matrix") → honest gap acknowledgment if there's a real one → one-line close. No confidentiality masking needed — DOE, CISA, NNSA, Treasury, Shorepoint, Cysiv, Trend Micro, Forescout, Experian can all be named directly.

### 5. ATS optimization pass
Run the tailored resume against the JD per `references/ats-optimization.md`: keyword coverage check, formatting/parseability check, and a summary of what's covered vs. still missing.

### 6. Visual QA
Render the resume and cover letter docx files to PDF and then to images (see the docx skill's verify-output steps: `soffice.py --convert-to pdf` then `pdftoppm`) and view the images to catch page overflow, awkward line wraps, or layout issues before calling it done.

### 7. Merge and deliver
Merge resume + cover letter into a single PDF using `qpdf --empty --pages resume.pdf cover-letter.pdf -- application-package.pdf` (see the pdf skill for alternatives). Use filename convention:
`Kyle_Main_[Company]_[Role]_[YYYY-MM-DD].pdf`
Present both the merged PDF and the individual .docx files (docx files are useful if Kyle wants to hand-edit before submitting).

Also save a plain `job_link.txt` in the application's directory containing the role title and the original posting URL — this is the source-of-truth reference back to the JD once it's been tailored into resume/cover-letter language.

### 8. Interview prep companion
Same JD triggers a matching prep doc (markdown is fine, doesn't need to be a formal file unless Kyle asks):
- 5-8 likely behavioral questions specific to the role level (IC vs. lead) and domain
- 5-8 likely technical questions based on the JD's stated stack, pulling from real depth in the master doc so Kyle can speak concretely
- 3-5 sharp questions Kyle should ask them
- Salary anchor reminder (top third of posted band, or $170K+ floor framing if unlisted)
- A short closing-the-interview script

## When Kyle wants to update the master doc

If Kyle mentions a new skill, cert, project, or a change in target roles/salary/constraints, update `master-reference/kyle-main-master.md` directly rather than treating it as one-off context for the current conversation. Confirm what changed before writing it.

## Output format defaults
Both .docx (working/editable) and PDF (final, polished) for resume and cover letter, per Kyle's preference. Interview prep can stay as an inline doc or markdown file — no need to over-format it.

## Reference files
- `master-reference/kyle-main-master.md` — full source of truth, read every time
- `references/ats-optimization.md` — keyword extraction method, formatting rules that break ATS parsers, how to score/report coverage
