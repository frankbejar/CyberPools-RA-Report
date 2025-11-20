# 2026 Risk Assessment - Production Documents

**Last Updated:** November 19, 2025
**Version:** v6.2 FINAL
**Status:** Production-ready, final 2026 question set approved

---

## Production Documents (3)

### 1. 2026_RA_QUESTION_SET_v6.2_FINAL.md
**Primary question set document**

**Contents:**
- 57 questions across 10 categories
- TIER classifications (10 TIER 1A, 7 TIER 1B, 40 Comprehensive)
- Framework mappings: CIS v8.1 IG1, NIST CSF 2.0 (Functions only)
- Category introductions with "why it matters" context
- CIS IG1 coverage: 86% (48 of 56 safeguards)

**Key Features:**
- Final 2026 question set (November 19, 2025)
- PAM merged with Access Reviews (Q2.9, elevated to TIER 1B)
- Framework streamlined: CIS v8.1 IG1 + NIST CSF 2.0 Functions only
- NIST 800-53 and ISO 27001 mappings removed for clarity
- Sector-neutral language throughout

**Use Case:** Assessment delivery, member education, stakeholder presentations

---

### 2. 2026_RA_TIER_FRAMEWORK_JUSTIFICATION.md
**TIER 1A/1B control justification**

**Contents:**
- Individual justification for all 10 TIER 1A controls
- Individual justification for all 7 TIER 1B controls
- Each includes: Carrier Requirements, Threat Intelligence, Control Effectiveness
- TIER framework validation methodology
- Threat intelligence alignment analysis

**Key Features:**
- Dual evidence model (carrier requirements + threat research)
- Statistics corrected from audit (Verizon DBIR, IBM, Coalition)
- The Trust requirements verified (quarterly testing, twice-yearly backup testing)
- Carrier prevalence documented

**Use Case:** Insurance carrier discussions, TIER classification defense, risk manager education

---

### 3. Grading Methodology Documents
**Grade Ceiling methodology justification**

**Documents:**
- `grading/GRADING_METHODOLOGY_EXECUTIVE_R2.md` - Executive comparison and recommendation
- `grading/GRADING_METHODOLOGY_TECHNICAL_SUPPLEMENT.md` - Detailed technical analysis

**Contents:**
- Grade Ceiling methodology (weighted scoring + grade caps)
- Comparison with Progressive Gating and True Gating approaches
- Statistical validation and insurance market alignment
- Real organization examples

**Use Case:** Stakeholder education, methodology defense, grading system explanation

---

## Quality Assurance

**Latest Update:** November 19, 2025 (v6.2)

**v6.2 Changes:**
1. Question count: 53 → 57 (added hardware/software inventory, account management enhancements)
2. TIER 1A: 10 questions
3. TIER 1B: 8 → 7 questions (PAM merged with Access Reviews Q2.9)
4. Comprehensive: 36 → 40 questions
5. Framework mappings: Removed NIST 800-53 and ISO 27001, kept CIS v8.1 IG1 + NIST CSF 2.0 Functions
6. Sector neutralization: Removed K-12 and religious organization specific references
7. CIS IG1 coverage: 86% (48 of 56 safeguards)

**Agents Used:**
- cybersecurity-risk-pm (framework accuracy)
- cyber-insurance-analyst (carrier requirements)
- cyber-research-analyst (threat intelligence citations)

---

## Archive Structure

### archive/change-history/
Version control and change documentation:
- `2026_RA_v5_to_v6_CHANGES_SUMMARY.md` - v5.0 → v6.0 changes
- `2026_RA_v6.0_to_v6.1_CHANGE_SUMMARY.md` - v6.0 → v6.1 changes (includes audit corrections)
- `2026_RA_QUESTION_SET_v6.0_UPDATED.md` - v6.0 reference copy

### archive/audit-nov-2025/
Completed audit documentation:
- `AUDIT_ISSUES_TRACKER.md` - Consolidated issue tracker (8 critical issues resolved)
- `CITATION_AUDIT_FINDINGS.md` - cyber-research-analyst report
- `INSURANCE_CLAIMS_VERIFICATION_AUDIT.md` - cyber-insurance-analyst report

### archive/research/
Research and analysis documents:
- `2026_RA_FOUNDATIONAL_FRAMEWORK_GAP_ANALYSIS.md` - CIS IG1 coverage analysis
- `2026_RA_QUESTION_REFINEMENT_REVIEW.md` - Question refinement process

### archive/
Other archived materials:
- `2026_RA_ASSESSMENT_GUIDANCE_v6.1.md` - Assessor guidance (12 clarifications)
- Previous cleanup archives (2024-11-11, 2024-11-12)

---

## Document Lineage

**v5.0** (October 2024)
- 51 questions, 9 categories
- Initial TIER structure

**v6.0** (November 2024)
- Added Q1.1, Q1.2 (hardware/software inventory, CIS IG1 coverage)
- Enhanced EDR, backup, phishing questions
- 53 questions total

**v6.1** (November 18, 2025)
- Enhanced Q2.3 (password policy with lockout)
- Enhanced Q5.2 (web + DNS filtering)
- Enhanced Q7.3 (quarterly phishing frequency)
- All statistics verified and corrected
- NIST CSF 2.0 mappings updated
- The Trust requirements verified

**v6.2** (November 19, 2025)
- Added 4 questions (Q1.1, Q1.2, Q2.1-2.3 inventory/unauthorized assets)
- Merged PAM (Q3.4) into Access Reviews (Q2.9), elevated to TIER 1B
- Removed NIST 800-53 and ISO 27001 mappings
- Sector-neutral language (removed K-12/religious org references)
- Final question count: 57 (10 TIER 1A, 7 TIER 1B, 40 Comprehensive)

---

## Usage Notes

**For Assessment Delivery:**
Use `2026_RA_QUESTION_SET_v6.2_FINAL.md` as the primary reference.

**For Insurance Discussions:**
Use `2026_RA_TIER_FRAMEWORK_JUSTIFICATION.md` to defend TIER classifications and demonstrate carrier alignment.

**For Grading Methodology:**
Use `grading/GRADING_METHODOLOGY_EXECUTIVE_R2.md` for executive-level explanation or `grading/GRADING_METHODOLOGY_TECHNICAL_SUPPLEMENT.md` for technical deep-dive.

**For Framework Mapping:**
CIS Controls v8.1 IG1 and NIST CSF 2.0 mappings are included in the v6.2 question set.

---

## Maintenance

**Next Review Planned:** Following Q1 2026 assessment cycle completion

**Monitoring:**
- Insurance carrier requirement changes (quarterly review)
- Threat intelligence updates (IBM, Verizon, Coalition annual reports)
- Framework updates (CIS, NIST revisions)

**Contact:** cyber@cyberpools.org
