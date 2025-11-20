# POC Team Presentation Guide

## 30-Second Pitch

> "We've created a dual-score model that gives every client TWO grades from the same assessment: a **Foundation Status** showing they meet cyber insurance requirements, and a **Security Maturity Grade** showing overall posture. Same assessment, better storytelling, clearer value."

## The Problem We're Solving

**Current State:**
- We give everyone the same full assessment
- Single grade (A-F) doesn't distinguish between "meets minimums" and "excellence"
- Hard to differentiate basic compliance from comprehensive security
- Insurance compliance isn't explicitly called out

**Client Confusion:**
- "I got a C, but do I meet insurance requirements?"
- "What's the difference between your assessment and a checkbox audit?"
- "I'm a small org - is this overkill for me?"

## The Solution: Dual Scoring

### Same Assessment → Two Scores

**Everyone takes the full 51-question assessment**, but reports now show:

#### 1. Foundation Status (Cyber Insurance Focus)
- Calculated from **12 core controls** required by insurers
- Three levels:
  - ✅ **CERTIFIED** (85%+) - Meets all requirements
  - ⚠️ **MEETS FOUNDATION** (70-84%) - Meets minimums
  - ❌ **BELOW FOUNDATION** (<70%) - Critical gaps

#### 2. Security Maturity (Comprehensive Assessment)
- Calculated from **all questions** (existing logic)
- Letter grades A-F
- Shows overall security posture

## Live Demo

### Open the POC Report
`output/POC_Dual_Score_CBS-CBS.pdf`

### Key Pages to Show:

**Page 3 - Executive Summary**
- Side-by-side dual score boxes
- Visual icons (checkmark for certified, letter grade badge)
- Clear descriptions of what each score means
- "Understanding Your Results" explanation

**Page 7 - Foundation Requirements Analysis**
- All 12 foundation questions in a table
- Color-coded status (green=implemented, yellow=partial, red=not implemented)
- Summary stats showing breakdown
- Priority action recommendations

**Compare to Current Report**
- Open `output/Christian_Brothers_Services_Risk_Assessment_10-16-2025.pdf`
- Show how executive summary just has one score
- Highlight the difference

## Business Benefits

### 1. Marketing Differentiation
**Tagline:** "The only risk assessment that provides both compliance verification AND security maturity rating"

**Client Communication:**
- "You're **Foundation Certified** - you meet all cyber insurance requirements"
- "Your **Grade B Maturity** shows strong overall security with targeted improvement areas"

### 2. Natural Service Tiering

| What | Who | Price |
|------|-----|-------|
| **Foundation Report** | Small orgs, annual check-ins, new members | $X |
| **Comprehensive Report** | Most members, full analysis | $2X |
| **Strategic Advisory** | Large orgs, includes trends, benchmarking | $3X+ |

### 3. Upsell Opportunities

**Conversation Starters:**
- "You're Foundation Certified but Grade C - let's get you to B"
- "You're doing great on maturity (B) but missing 2 foundation controls - let's get you certified"
- "Let's track your foundation score over time to show improvement to your board"

### 4. Insurance Alignment

**Direct Value to Clients:**
- Foundation score = immediate answer to "Do we meet cyber insurance requirements?"
- Can use "Foundation Certified" badge on website/marketing
- Clear roadmap to certification if not there yet

## The Numbers (CBS-CBS Example)

```
Organization: Christian Brothers Services
Assessment Date: October 2025

RESULTS:
├─ Foundation Status: CERTIFIED (100%)
│  └─ All 12 core cyber insurance requirements met
│
└─ Security Maturity: Grade A (96%)
   └─ Exceptional security posture across 9 control categories
```

**What this tells us:**
- CBS is "best in class" - certified AND Grade A
- Perfect example to show what excellence looks like

## Potential Scenarios

### Scenario 1: Foundation Certified + High Maturity
- Status: CERTIFIED (95%)
- Maturity: Grade A (92%)
- **Story:** "Gold standard organization - meets all requirements and excels overall"

### Scenario 2: Foundation Certified + Moderate Maturity
- Status: CERTIFIED (85%)
- Maturity: Grade C (75%)
- **Story:** "Compliant but room for improvement - let's elevate your maturity"

### Scenario 3: Not Certified + Good Maturity
- Status: MEETS FOUNDATION (72%)
- Maturity: Grade B (84%)
- **Story:** "Strong security overall, but 3 critical insurance requirements need attention"

### Scenario 4: Both Need Work
- Status: BELOW FOUNDATION (65%)
- Maturity: Grade D (62%)
- **Story:** "Critical gaps requiring immediate attention - here's your roadmap"

## Implementation Timeline

### This Week (POC Phase)
- ✅ POC built and tested
- ⬜ Team review and feedback (this meeting!)
- ⬜ Generate POC reports for all 4 CBS schools
- ⬜ Refine based on feedback

### Next Week (Integration)
- Merge POC into production code
- Test with historical assessments
- Update documentation

### Week 3 (Soft Launch)
- Use dual-score on 2-3 new assessments
- Gather client feedback
- Refine messaging

### Month 2 (Full Rollout)
- Update all templates
- Train full team
- Update marketing materials
- Launch officially

## Questions to Answer

### For the Team:

1. **Clarity:** Do these two scores clearly communicate value?

2. **Thresholds:** Are the cutoffs right?
   - Certified: 85%+
   - Meets Foundation: 70-84%
   - Below Foundation: <70%

3. **Foundation Questions:** Are these the right 12 core controls? Should we add/remove any?

4. **Presentation:** Does the visual layout work? Any improvements?

5. **Pricing:** How would this affect our service tiers/pricing?

6. **Rollout:** Timeline feel realistic? Any concerns?

## Technical Details (For IT/Dev Team)

**What Changed:**
- Added dual scoring calculation (foundation vs maturity)
- Created new templates with dual-score display
- Added foundation breakdown section
- New CSS for visual elements

**What Didn't Change:**
- Assessment questions (same 51 questions)
- Scoring formula (same calculation logic)
- Data structure (same JSON format)
- Existing reports (POC is separate)

**Effort to Integrate:**
- Estimated: 8-12 hours
- Changes needed:
  1. Merge POC scoring into main script
  2. Update templates
  3. Add backward compatibility flag
  4. Test with historical data

## Decision Points

### Go/No-Go Decisions:

**Option 1: Full Speed Ahead**
- Approve POC for production integration
- Begin rollout next week
- Update all future assessments

**Option 2: Pilot Program**
- Test with 5-10 organizations
- Gather feedback
- Refine before full rollout

**Option 3: Modifications Needed**
- Approve concept but request changes:
  - Different thresholds?
  - Different foundation questions?
  - Different visual presentation?

**Option 4: Hold**
- Not ready for this change
- Need more information/discussion

## Next Steps (If Approved)

### Frank's Action Items:
1. Generate POC reports for all CBS schools
2. Schedule client feedback calls
3. Prepare marketing materials
4. Update CRM fields for dual scoring

### Development Action Items:
1. Integrate POC code into main codebase
2. Add feature flag for dual-score mode
3. Test with all historical data
4. Deploy to production

### Team Training:
1. How to explain dual scores to clients
2. How to use foundation status in sales conversations
3. How to position service tiers
4. How to handle edge cases

## Resources

- **POC Report:** `output/POC_Dual_Score_CBS-CBS.pdf`
- **POC Documentation:** `POC_DUAL_SCORE_README.md`
- **POC Script:** `scripts/transform_and_generate_POC.py`
- **POC Templates:** `templates_POC/`

## Questions?

**During the presentation:**
- Open the POC PDF and walk through it
- Compare side-by-side with current report
- Show how it addresses client questions
- Get feedback on visual presentation

**After the presentation:**
- Collect written feedback
- Schedule follow-up if needed
- Make decision on next steps

---

**Remember:** This is the SAME assessment clients already take. We're just telling the story better with two complementary scores instead of one.

**The value:** Clearer compliance verification + better differentiation + natural service tiering.
