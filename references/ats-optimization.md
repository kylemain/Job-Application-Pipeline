# ATS Optimization Reference

## Keyword extraction from the JD
1. Pull every hard skill, tool, platform, certification, and methodology named in the JD (e.g., "Splunk," "MITRE ATT&CK," "Kubernetes," "CISSP," "SIEM," "threat hunting").
2. Note which ones are in the "must-have/required" section vs. "nice to have/preferred."
3. Note the exact phrasing used (e.g., "SIEM platforms" vs. "security information and event management") — ATS keyword matching is often literal string matching, so mirror the JD's exact terms where Kyle genuinely has that skill, rather than only using a synonym.
4. Cross-reference against the master reference's skills inventory. Categorize each JD keyword as:
   - **Direct match** — already in master doc, confirmed
   - **Adjacent/transferable** — related experience exists but isn't the exact tool/term (state this honestly in the fit assessment, don't just insert the exact keyword if Kyle hasn't actually used it)
   - **Gap** — no evidence in master doc

## Formatting rules that break ATS parsers (avoid in resume)
- No tables for layout structure (single-column tables for actual tabular data are usually fine, but don't use tables to fake a two-column resume layout)
- No text inside headers/footers for content that should be parsed (contact info in a header can get dropped by some parsers — keep name/contact in the main document body, top of page)
- No text boxes or floating graphic elements containing real content
- No icons/images standing in for text (e.g., a phone icon instead of the word "Phone")
- Standard section headings ATS parsers recognize: "Experience" / "Work Experience," "Education," "Skills," "Certifications" — avoid overly creative section titles
- Standard, ATS-safe fonts (avoid script/decorative fonts)
- Save/export as .docx or standard-text-layer PDF, not a flattened image-based PDF

## Reporting coverage back to Kyle
After tailoring, give a short summary:
- X of Y required keywords covered directly
- Which ones are adjacent/transferable (and how they're being framed)
- Which real gaps exist (be honest — don't paper over these, flag them so Kyle can decide whether to address in the cover letter's gap-acknowledgment paragraph or just accept the gap)