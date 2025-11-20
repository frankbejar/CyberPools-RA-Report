# Dual-Score Model - Proof of Concept

## Overview

This POC demonstrates a **dual-score assessment model** that provides two complementary perspectives on cybersecurity posture:

1. **Foundation Status** - Measures compliance with 12 core cyber insurance requirements
2. **Security Maturity** - Evaluates comprehensive security posture across all assessment areas

## What's Been Built

### 1. Enhanced Scoring Engine
- **Foundation Score Calculation** - Isolates and scores the 12 `qReq` questions
- **Maturity Score Calculation** - Maintains existing comprehensive scoring
- **Status Determination** - Categorizes organizations as CERTIFIED, MEETS FOUNDATION, or BELOW FOUNDATION
- **Dual Grading** - Shows both foundation status and letter grade (A-F)

### 2. Updated Report Templates
- **Dual Score Display** - Visual side-by-side comparison in executive summary
- **Foundation Breakdown** - Dedicated section analyzing the 12 core requirements
- **Enhanced Visualizations** - Color-coded badges, SVG icons, and status indicators
- **Responsive Design** - Professional layout optimized for PDF rendering

### 3. New POC Files Created

```
cyberpools-RA-Report/
├── scripts/
│   └── transform_and_generate_POC.py       # POC generator script
├── templates_POC/
│   ├── main_template.html                   # Updated main template
│   └── partials/
│       ├── executive_summary.html           # Dual score display
│       └── foundation_breakdown.html        # Foundation requirements analysis
└── styles/
    └── dual_score_POC.css                   # Dual score styling
```

## Sample Output

**Generated Report:** `output/POC_Dual_Score_CBS-CBS.pdf`

### Test Results (CBS-CBS.json):
- **Foundation Status:** CERTIFIED (100%)
- **Security Maturity:** Grade A (96%)

## How to Use

### Generate a POC Report

```bash
cd /Users/frankbejar/Documents/github/cyberpools-RA-Report

python3 scripts/transform_and_generate_POC.py \
  --input input/CBS-CBS.json \
  --auto \
  --engine docraptor
```

### Test with Different Organizations

```bash
# Test with Rosary College Prep
python3 scripts/transform_and_generate_POC.py \
  --input "input/CBS-Rosary College Prep.json" \
  --auto --engine docraptor

# Test with Salesian College Preparatory
python3 scripts/transform_and_generate_POC.py \
  --input "input/CBS-Salesian College Prep.json" \
  --auto --engine docraptor

# Test with Santa Catalina School
python3 scripts/transform_and_generate_POC.py \
  --input "input/CBS-Santa Catalina School.json" \
  --auto --engine docraptor
```

### Generate Production PDFs (No Watermark)

```bash
python3 scripts/transform_and_generate_POC.py \
  --input input/CBS-CBS.json \
  --auto \
  --engine docraptor \
  --production
```

## Key Features

### Foundation Status Levels

1. **CERTIFIED (85%+)**
   - Green badge with checkmark icon
   - "Organization meets all core cyber insurance requirements"
   - Full compliance with foundation controls

2. **MEETS FOUNDATION (70-84%)**
   - Yellow/amber badge with warning icon
   - "Meets minimum foundation requirements with opportunities for improvement"
   - Basic compliance achieved

3. **BELOW FOUNDATION (<70%)**
   - Red badge with alert icon
   - "Critical gaps identified in foundation security controls"
   - Immediate remediation required

### Security Maturity Grades

- **Grade A (90%+):** Exceptional security posture
- **Grade B (80-89%):** Strong security posture
- **Grade C (70-79%):** Adequate security posture
- **Grade D (60-69%):** Below average security posture
- **Grade F (<60%):** Poor security posture

### Foundation Breakdown Section

The POC adds a dedicated "Foundation Requirements Analysis" section that shows:

- **Summary Stats:** Count of Fully/Partially/Not Implemented controls
- **Detailed Table:** All 12 foundation questions with status, impact, and risk
- **Priority Actions:** Specific recommendations when not certified
- **Visual Indicators:** Color-coded rows and badges for quick assessment

## Business Value Proposition

### Clear Differentiation

**Same Assessment → Two Perspectives:**
- Everyone takes the same full assessment (no "dumbed down" version)
- Reports show both compliance and maturity
- Natural tiering emerges from dual scores

### Marketing Benefits

1. **Foundation Certified Badge** - Clients can claim "CyberPools Foundation Certified"
2. **Insurance Alignment** - Foundation score directly maps to coverage requirements
3. **Growth Path** - Clear progression: "You're certified but Grade C - let's get you to B"
4. **Unique Position** - "Only RA that provides both compliance + maturity scoring"

### Pricing Flexibility

**Potential Service Tiers:**

| Tier | Deliverable | Focus | Price |
|------|-------------|-------|-------|
| Foundation | Foundation status + summary | Compliance only | $X |
| Standard | Full report (current) | Comprehensive | $2X |
| Premium | Full report + foundation analysis + trends | Strategic advisory | $3X |

## Implementation Roadmap

### Phase 1: Validation (This Week)
- ✅ POC created and tested
- ⬜ Generate reports for all 4 CBS schools
- ⬜ Internal team review and feedback
- ⬜ Refine scoring thresholds if needed

### Phase 2: Integration (Next Week)
- ⬜ Merge POC code into main `transform_and_generate.py`
- ⬜ Add `--dual-score` flag for backward compatibility
- ⬜ Update all templates to support both modes
- ⬜ Test with historical data

### Phase 3: Rollout (Week 3)
- ⬜ Update CRM to capture foundation vs maturity scores
- ⬜ Train assessment team on dual-score model
- ⬜ Update marketing materials
- ⬜ Create client-facing documentation

### Phase 4: Enhancement (Month 2)
- ⬜ Add trend tracking (foundation score over time)
- ⬜ Benchmarking (compare to industry averages)
- ⬜ Dashboard visualization
- ⬜ Automated remediation roadmaps

## Technical Details

### Scoring Formula

**Foundation Score:**
```python
# Only questions where qReq = true
foundation_questions = [q for q in all_questions if q.qReq == true]
foundation_score = calculate_overall_score(foundation_questions)
```

**Maturity Score:**
```python
# All questions (existing logic)
maturity_score = calculate_overall_score(all_questions)
```

### Question Mapping Enhancement

The POC uses the existing `qReq` field in question mappings:

```json
{
  "4c466f03-9478-f011-b4cb-000d3a34656f": {
    "number": "2.3",
    "text": "Is MFA enabled...",
    "impact_score": 5,
    "qReq": true  // Foundation requirement
  }
}
```

### Current Foundation Questions (12 total)

Based on `COMPLIANCE_QUESTION_NUMBERS`:
1. 1.4 - End-of-life software management
2. 2.3 - MFA for cloud resources
3. 2.4 - Privileged account management
4. 2.5 - User access reviews
5. 2.6 - Account deprovisioning
6. 4.3 - Patch management
7. 4.7 - Remote access security
8. 5.4 - Email security controls
9. 6.3 - Backup testing
10. 6.4 - Immutable backups
11. 7.2 - Security awareness training
12. 7.3 - Phishing simulation

## Comparison: Before vs. After

### Before (Current State)
```
Assessment Results
------------------
Overall Score: 96% (Grade A)
```

### After (Dual Score POC)
```
Assessment Results
------------------
Foundation Status: CERTIFIED (100%)
  ✓ Meets all core cyber insurance requirements

Security Maturity: Grade A (96%)
  Exceptional security posture across all areas
```

## Questions & Answers

### Q: Will existing reports break?
**A:** No. This is a separate POC. To integrate, we'd add a flag for dual-score mode.

### Q: Do we need to create new assessments?
**A:** No. Same assessment data, just displayed differently.

### Q: What if someone is Foundation CERTIFIED but Grade F?
**A:** Unlikely scenario, but possible. It means they nail the 12 critical controls but fail everywhere else. Report would highlight this gap.

### Q: Can we customize the 12 foundation questions?
**A:** Yes. Update `COMPLIANCE_QUESTION_NUMBERS` or modify questions with `qReq: true`.

### Q: What about organizations with different compliance needs?
**A:** Foundation questions could be customized per industry (education vs. healthcare) by maintaining separate question mapping files.

## Next Steps

### For Team Review:

1. **Open the POC Report:** `output/POC_Dual_Score_CBS-CBS.pdf`
2. **Review Key Sections:**
   - Executive Summary (pages 3) - Dual score display
   - Foundation Requirements Analysis (page 7) - Breakdown table
3. **Provide Feedback:**
   - Does this clearly communicate value?
   - Are the thresholds right (85% for certified, 70% for meets)?
   - Would clients understand this presentation?
   - What refinements would improve it?

### For Frank:

**Generate comparison reports** to show the difference:
```bash
# Generate all POC reports
for file in input/CBS-*.json; do
  python3 scripts/transform_and_generate_POC.py \
    --input "$file" \
    --auto \
    --engine docraptor \
    --production
done
```

**Decision Points:**
1. Approve concept for production integration?
2. Adjust scoring thresholds?
3. Add/remove foundation questions?
4. Timeline for rollout?

## Support

For questions or modifications to this POC:
- Review code: `scripts/transform_and_generate_POC.py`
- Review templates: `templates_POC/`
- Review styles: `styles/dual_score_POC.css`

---

**POC Created:** October 27, 2025
**Status:** Ready for Team Review
**Estimated Integration Effort:** 8-12 hours
