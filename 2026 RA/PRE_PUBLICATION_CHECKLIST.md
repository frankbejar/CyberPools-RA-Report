# 2026 Risk Assessment - Pre-Publication Checklist

**Purpose:** Validate all documents before updating GitHub Pages documentation site
**Date Created:** November 20, 2025
**Status:** PENDING VALIDATION

---

## Critical Issues Found

### ISSUE 1: README References Missing Archive Folders
**Location:** `README.md` lines 89-112
**Problem:** References archive folders that don't exist:
- `archive/change-history/`
- `archive/audit-nov-2025/`
- `archive/research/`

**Status:** CRITICAL - README needs update to reflect actual folder structure
**Action Required:** Update README to remove references to missing archive folders

---

## Document Inventory

### Actual Files in 2026 RA/ Folder:
- [ ] `2026_RA_QUESTION_SET_v6.2_FINAL.md` (17 KB)
- [ ] `2026_RA_TIER_FRAMEWORK_JUSTIFICATION.md` (36 KB)
- [ ] `GRADING_METHODOLOGY_EXECUTIVE_R2.md` (23 KB)
- [ ] `GRADING_METHODOLOGY_TECHNICAL_SUPPLEMENT.md` (54 KB)
- [ ] `GITHUB_PAGES_REENGINEERING_PLAN.md` (28 KB)
- [ ] `README.md` (6 KB)

---

## 1. Document Count Consistency

### Question Count Verification
**Expected:** 57 total questions (10 TIER 1A + 7 TIER 1B + 40 Comprehensive)

#### Check Each Document States:
- [ ] **Question Set:** "57 questions" ✓ or ✗
- [ ] **TIER Framework:** "10 TIER 1A, 7 TIER 1B" ✓ or ✗
- [ ] **Grading Executive:** "57 questions" ✓ or ✗
- [ ] **Grading Technical:** "57 questions" ✓ or ✗
- [ ] **README:** "57 questions" ✓ or ✗

**If mismatches found:** Document which file has incorrect count

---

### Category Count Verification
**Expected:** 10 categories

#### Check Each Document States:
- [ ] **Question Set:** "10 categories" ✓ or ✗
- [ ] **README:** "10 categories" ✓ or ✗

---

### Framework Coverage Claims
**Expected:** CIS v8.1 IG1 coverage = 86% (48 of 56 safeguards)

#### Check Consistency:
- [ ] **Question Set:** States 86% coverage ✓ or ✗
- [ ] **README:** States 86% coverage ✓ or ✗
- [ ] **Actual Question Mappings:** Count CIS mappings in questions

---

## 2. TIER Classification Consistency

### TIER 1A Questions (Expected: 10)

#### From Question Set Document:
- [ ] Count all questions marked "TIER 1A"
- [ ] List question numbers: _________________
- [ ] Total count: _____ (should be 10)

#### Cross-check with TIER Framework Document:
- [ ] TIER Framework lists 10 TIER 1A justifications ✓ or ✗
- [ ] Question numbers match between documents ✓ or ✗

#### Specific Questions to Verify:
- [ ] Q1.4 - End-of-life software (TIER 1A)
- [ ] Q2.4 - MFA for remote access/VPN (TIER 1A)
- [ ] Q2.5 - MFA for cloud services (TIER 1A)
- [ ] Q2.6 - MFA for admin accounts (TIER 1A)
- [ ] Q2.7 - MFA for critical systems (TIER 1A)
- [ ] Q4.3 - Critical vulnerability patching (TIER 1A)
- [ ] Q4.7 - External vulnerability scanning (TIER 1A)
- [ ] Q5.4 - EDR/MDR deployment (TIER 1A)
- [ ] Q6.3 - Protected/air-gapped backups (TIER 1A)
- [ ] Q6.4 - Backup testing frequency (TIER 1A)

---

### TIER 1B Questions (Expected: 7)

#### From Question Set Document:
- [ ] Count all questions marked "TIER 1B"
- [ ] List question numbers: _________________
- [ ] Total count: _____ (should be 7)

#### Cross-check with TIER Framework Document:
- [ ] TIER Framework lists 7 TIER 1B justifications ✓ or ✗
- [ ] Question numbers match between documents ✓ or ✗

#### Specific Questions to Verify:
- [ ] Q2.9 - Access reviews (PAM merged here, elevated to TIER 1B)
- [ ] Q4.5 - Email authentication (SPF/DKIM/DMARC) (TIER 1B)
- [ ] Q4.14 - Change management (TIER 1B)
- [ ] Q6.2 - Backup encryption (TIER 1B)
- [ ] Q7.2 - Security awareness training (TIER 1B)
- [ ] Q7.3 - Phishing testing (quarterly) (TIER 1B)
- [ ] Q9.4 - Incident response plan (TIER 1B)

---

### Comprehensive Questions (Expected: 40)

- [ ] Count all questions NOT marked TIER 1A or TIER 1B
- [ ] Total count: _____ (should be 40)
- [ ] Math check: 10 + 7 + 40 = 57 ✓ or ✗

---

## 3. Citation Validation

### GRADING_METHODOLOGY_EXECUTIVE_R2.md

#### Check All Footnotes Resolve:
- [ ] [^1] - Defined? ✓ or ✗
- [ ] [^2] - Defined? ✓ or ✗
- [ ] [^3] - Defined? ✓ or ✗
- [ ] [^4] - Defined? ✓ or ✗
- [ ] Continue through all citations...
- [ ] Any orphaned footnotes (used but not defined)? List: _________
- [ ] Any unused footnotes (defined but not referenced)? List: _________

---

### GRADING_METHODOLOGY_TECHNICAL_SUPPLEMENT.md

#### Check All Footnotes Resolve:
- [ ] [^1] - Defined? ✓ or ✗
- [ ] [^2] - Coalition Cyber Threat Index 2025 ✓ or ✗
- [ ] [^2a] - Microsoft Digital Defense Report 2025 ✓ or ✗
- [ ] [^2b] - IBM Cost of Data Breach 2024 ✓ or ✗
- [ ] [^2c] - Sophos State of Ransomware Education 2024 ✓ or ✗
- [ ] [^2d] - Rubrik Zero Labs State of Data Security 2024 ✓ or ✗
- [ ] [^2e] - Rubrik Zero Labs Hard Truths 2023 ✓ or ✗
- [ ] Continue through [^4], [^8], [^9], [^11], [^12], [^13], [^14], [^15], [^16], [^18], [^19], [^20], [^21], [^22], [^23], [^24], [^25], [^27], [^30], [^31], [^32], [^33], [^34]
- [ ] Any orphaned footnotes? List: _________
- [ ] Any unused footnotes? List: _________

---

### TIER_FRAMEWORK_JUSTIFICATION.md

#### Check All Citations Are Properly Formatted:
- [ ] All threat intelligence sources cited (Verizon DBIR, IBM, Coalition, etc.)
- [ ] All carrier requirement claims cited
- [ ] All statistics have sources
- [ ] No unsupported claims

---

### URL Validation

#### Test All External URLs (Critical Sample):
- [ ] https://www.coalitioninc.com/announcements/cyber-threat-index-2025
- [ ] https://www.verizon.com/business/resources/reports/dbir/
- [ ] https://www.ibm.com/reports/data-breach
- [ ] https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf (NIST CSF 2.0)
- [ ] https://www.cisecurity.org/controls/v8 (CIS Controls)
- [ ] Any broken links found? List: _________

---

## 4. Cross-Document References

### Question Set → TIER Framework
- [ ] Every TIER 1A question in Question Set has corresponding justification in TIER Framework ✓ or ✗
- [ ] Every TIER 1B question in Question Set has corresponding justification in TIER Framework ✓ or ✗
- [ ] Question numbers match exactly ✓ or ✗

### Question Set → Grading Methodology
- [ ] Grading docs reference correct question counts (57) ✓ or ✗
- [ ] TIER structure mentioned in grading docs matches (10/7/40) ✓ or ✗

### README → All Documents
- [ ] README accurately describes all documents ✓ or ✗
- [ ] Version numbers consistent (v6.2 FINAL) ✓ or ✗
- [ ] Dates consistent (November 19, 2025) ✓ or ✗

---

## 5. Framework Mapping Accuracy

### CIS Controls v8.1 IG1 Mapping

#### Verify Coverage Claim (86% = 48 of 56):
- [ ] Count all unique CIS safeguards mapped in Question Set
- [ ] Total unique safeguards: _____ (should be 48)
- [ ] Calculate: _____ / 56 = _____% (should be 86%)

#### Verify CIS Safeguards NOT Covered (8 gaps):
- [ ] Document lists 8 specific gaps in Question Set ✓ or ✗
- [ ] Gaps justified (e.g., "organization-specific, not universal") ✓ or ✗

---

### NIST CSF 2.0 Mapping

#### Verify All Questions Have NIST Mappings:
- [ ] Every question has NIST CSF 2.0 Function code (GV, ID, PR, DE, RS, RC) ✓ or ✗
- [ ] No questions missing NIST mapping ✓ or ✗
- [ ] NIST CSF 2.0 link in citations works ✓ or ✗

---

## 6. Question Numbering Consistency

### Question Numbering Scheme

#### Verify Sequential Numbering:
- [ ] Category 1 questions: Q1.1, Q1.2, Q1.3... (check no gaps)
- [ ] Category 2 questions: Q2.1, Q2.2, Q2.3... (check no gaps)
- [ ] Category 3 questions: Q3.1, Q3.2, Q3.3... (check no gaps)
- [ ] Category 4 questions: Q4.1, Q4.2, Q4.3... (check no gaps)
- [ ] Category 5 questions: Q5.1, Q5.2, Q5.3... (check no gaps)
- [ ] Category 6 questions: Q6.1, Q6.2, Q6.3... (check no gaps)
- [ ] Category 7 questions: Q7.1, Q7.2, Q7.3... (check no gaps)
- [ ] Category 8 questions: Q8.1, Q8.2, Q8.3... (check no gaps)
- [ ] Category 9 questions: Q9.1, Q9.2, Q9.3... (check no gaps)
- [ ] Category 10 questions: Q10.1, Q10.2, Q10.3... (check no gaps)

#### Verify No Duplicate Question Numbers:
- [ ] No question number appears twice ✓ or ✗

---

## 7. Statistical Claims Verification

### Key Statistics to Verify Source Citations

#### Grading Methodology Documents:
- [ ] "99% of identity-based attacks blocked by MFA" - Microsoft Digital Defense Report 2025 cited ✓ or ✗
- [ ] "38% of all breaches involve stolen credentials" - Verizon DBIR 2024 cited ✓ or ✗
- [ ] "58% of ransomware claims start with compromised VPN/firewall" - Coalition 2025 cited ✓ or ✗
- [ ] "96% of ransomware attacks target backups" - Rubrik Zero Labs 2024 cited ✓ or ✗
- [ ] "74% success rate corrupting backup systems" - Rubrik Zero Labs 2024 cited ✓ or ✗
- [ ] "16% full recovery rate paying ransoms" - Rubrik Zero Labs 2023 cited ✓ or ✗
- [ ] "20% of breaches from vulnerability exploitation" - Verizon DBIR 2024 cited ✓ or ✗
- [ ] "78% of breaches exploited vulnerabilities with available patches" - Coalition 2025 cited ✓ or ✗

#### TIER Framework Document:
- [ ] All carrier prevalence claims cited (e.g., "95%+ carrier prevalence for MFA")
- [ ] All threat statistics cited with proper source
- [ ] No unsupported percentages or statistics

---

## 8. Sector-Neutral Language Verification

### Check for Sector-Specific References:
- [ ] No "K-12" references remaining ✓ or ✗
- [ ] No "school" or "district" references remaining ✓ or ✗
- [ ] No "religious organization" specific references remaining ✓ or ✗
- [ ] Language is sector-neutral throughout ✓ or ✗

**If found:** Document location and replace with sector-neutral equivalent

---

## 9. Grading Methodology Consistency

### Grade Ceiling Formula

#### Verify Consistent Formula Across Documents:
- [ ] Foundation Score = 70% of overall ✓ or ✗
- [ ] Comprehensive Score = 30% of overall ✓ or ✗
- [ ] TIER 1A point allocation consistent ✓ or ✗
- [ ] TIER 1B point allocation consistent ✓ or ✗

#### Verify Grade Ceiling Logic:
- [ ] Missing 2+ TIER 1A → Grade F ✓ or ✗
- [ ] Missing 1 TIER 1A → Grade C (max) ✓ or ✗
- [ ] Missing 1+ TIER 1B → Grade B (max) ✓ or ✗
- [ ] No critical gaps → No ceiling, use score ✓ or ✗

---

## 10. Content Completeness

### Check for Placeholders or TODO Items:
- [ ] No "TBD" or "TODO" markers ✓ or ✗
- [ ] No "[PLACEHOLDER]" text ✓ or ✗
- [ ] No empty sections ✓ or ✗
- [ ] No "DRAFT" or "WIP" markers ✓ or ✗

### Check for Missing Content:
- [ ] All questions have full text ✓ or ✗
- [ ] All questions have "Why This Matters" explanations ✓ or ✗
- [ ] All questions have framework mappings ✓ or ✗
- [ ] All TIER 1A/1B questions have justifications ✓ or ✗

---

## 11. Date and Version Consistency

### Check All Documents:
- [ ] All docs state "v6.2 FINAL" ✓ or ✗
- [ ] All docs state "November 19, 2025" or "November 20, 2025" ✓ or ✗
- [ ] No references to older versions (v6.0, v6.1) in main content ✓ or ✗

---

## 12. README Accuracy

### README Must Accurately Describe:
- [ ] Correct file list (6 markdown files) ✓ or ✗
- [ ] Remove references to missing archive folders (CRITICAL) ✗
- [ ] Correct question counts (57 total) ✓ or ✗
- [ ] Correct TIER breakdown (10/7/40) ✓ or ✗
- [ ] Correct version (v6.2 FINAL) ✓ or ✗
- [ ] Correct framework coverage (86% CIS IG1) ✓ or ✗

---

## 13. GitHub Pages Reengineering Plan Accuracy

### Verify Plan References Correct Counts:
- [ ] States "57 questions" ✓ or ✗
- [ ] States "10 categories" ✓ or ✗
- [ ] States "10 TIER 1A, 7 TIER 1B, 40 Comprehensive" ✓ or ✗
- [ ] References correct source documents ✓ or ✗

---

## 14. Formatting and Readability

### Check Markdown Formatting:
- [ ] All headers properly formatted (# ## ###) ✓ or ✗
- [ ] All lists properly formatted ✓ or ✗
- [ ] All tables properly formatted ✓ or ✗
- [ ] All code blocks properly formatted ✓ or ✗
- [ ] No broken markdown syntax ✓ or ✗

### Check for Typos:
- [ ] Spell check all documents ✓ or ✗
- [ ] Check for common typos (e.g., "teh" instead of "the") ✓ or ✗

---

## 15. Special Characters and Emojis

### NO EMOJIS POLICY CHECK:
- [ ] No emojis in Question Set ✓ or ✗
- [ ] No emojis in TIER Framework ✓ or ✗
- [ ] No emojis in Grading Methodology ✓ or ✗
- [ ] No emojis in README ✓ or ✗
- [ ] No checkmarks (✅), crosses (❌), warnings (⚠️) ✓ or ✗

**If found:** Remove and replace with text equivalents

---

## Priority Actions Before GitHub Pages Update

### CRITICAL (Must Fix):
1. [ ] **Update README.md** - Remove references to missing archive folders
2. [ ] **Validate all citations** - Ensure all footnotes resolve
3. [ ] **Verify question counts** - Ensure 57 total (10/7/40) across all docs
4. [ ] **Check TIER classifications** - Ensure all 17 questions classified correctly

### HIGH PRIORITY (Should Fix):
5. [ ] **Test all URLs** - Ensure no broken external links
6. [ ] **Verify CIS coverage** - Count actual mappings = 48 safeguards
7. [ ] **Check cross-references** - Ensure docs reference each other correctly
8. [ ] **Remove sector-specific language** - Ensure sector-neutral throughout

### MEDIUM PRIORITY (Good to Fix):
9. [ ] **Check for typos** - Spell check all documents
10. [ ] **Verify formatting** - Ensure proper markdown syntax
11. [ ] **Check for placeholders** - Remove any TODO or TBD markers
12. [ ] **Verify statistics** - Ensure all claims have source citations

---

## Sign-Off

### Validation Complete:
- [ ] All critical issues resolved
- [ ] All high priority issues resolved
- [ ] Documents ready for GitHub Pages publication

**Validated By:** _________________
**Date:** _________________
**Notes:** _________________

---

**Next Step:** Generate GitHub Pages content from validated documents using `docs-site/scripts/build_mkdocs_site.py`
