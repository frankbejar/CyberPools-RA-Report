# Grading Models Visual Comparison
## Side-by-Side Comparison of All Approaches

**Document Date:** November 2, 2025
**Purpose:** Quick visual reference for comparing grading model options

---

## The Three Main Approaches

### Approach 1: Current Production Model (Baseline)
```
┌─────────────────────────────────────┐
│   OVERALL SECURITY SCORE            │
│                                     │
│           82%                       │
│         Grade: B                    │
│                                     │
│  (Single score, all 51 questions)   │
└─────────────────────────────────────┘
```

**How it works:** Simple average of all questions weighted by impact rating

**Example:**
- Organization scores 82% across all 51 questions
- Grade: B
- That's it. One number.

**Strengths:**
- ✅ Simple to understand
- ✅ Single number to track
- ✅ Proven delivery model

**Weaknesses:**
- ❌ No foundation emphasis
- ❌ Category size imbalance (13Q category has 4× weight of 3Q category)
- ❌ Can score 82% while missing EDR, MFA, or backups (insurance critical)
- ❌ Doesn't align with insurance underwriting process

---

### Approach 2: 80/20 Weighted Model (Your POC)
```
┌─────────────────────────────────────┐
│   FOUNDATION SCORE                  │
│   75% (9 of 12 questions met)       │
├─────────────────────────────────────┤
│   COMPREHENSIVE SCORE               │
│   88% (all 51 questions)            │
├─────────────────────────────────────┤
│   OVERALL SCORE                     │
│   78%  [weighted: 80% × 75%         │
│         + 20% × 88%]                │
│   Grade: C                          │
└─────────────────────────────────────┘
```

**How it works:**
```
Overall Score = (0.80 × Foundation Score) + (0.20 × Comprehensive Score)
Overall Score = (0.80 × 75%) + (0.20 × 88%)
Overall Score = 60% + 17.6% = 77.6% ≈ 78%
Grade: C
```

**Example:**
- Foundation: 75% (9/12 questions met - missing EDR, backup testing, vulnerability scanning)
- Comprehensive: 88% (strong across all categories)
- Overall: 78% (C grade)

**Strengths:**
- ✅ Foundation heavily emphasized (80% weight)
- ✅ Single overall score (easy to communicate)
- ✅ Penalizes weak foundation mathematically

**Weaknesses:**
- ❌ Where did 78% come from? (Members struggle with weighted formula)
- ❌ Blends two different measurement types (pass/fail foundation + continuous comprehensive)
- ❌ Can mask critical problems (see Edge Case A below)
- ❌ Doesn't map to how insurance underwriters actually make decisions

**Edge Case A: Can Mask Critical Problems**
```
Foundation: 100% (perfect compliance)
Comprehensive: 45% (major gaps in non-foundation controls)

80/20 Result: (0.80 × 100%) + (0.20 × 45%) = 80% + 9% = 89%
Grade: B+

BUT: 45% comprehensive means critical gaps in:
- Security monitoring (10%)
- Vendor management (15%)
- Inventory & assets (25%)
- Incident response (40%)

Member sees: B+ grade (looks good!)
Reality: Massive security gaps despite foundation compliance
Insurance Risk: High claim denial risk for negligence
```

This is a statistical artifact of the weighted formula masking a real problem.

---

### Approach 3: Progressive Gating Model (Recommended)
```
┌──────────────────────────────────────────────────┐
│   FOUNDATION SCORE: 75% - CONDITIONAL PASS       │
├──────────────────────────────────────────────────┤
│   ✓  TIER 1 Insurability: 7/7 (PASS)            │
│   ⚠  TIER 2 Standard Rates: 2/3 (SUBSTANTIAL)   │
│   ⚠  TIER 3 Pricing: 2/4 (PARTIAL)              │
├──────────────────────────────────────────────────┤
│   → Maximum Overall Grade: B (TIER 2 cap)       │
│   → TIER 3 Penalty: -5% to comprehensive        │
└──────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────┐
│   COMPREHENSIVE SCORE                            │
├──────────────────────────────────────────────────┤
│   Raw Score: 88% (STRONG)                        │
│   TIER 3 Penalty: -5%                            │
│   Adjusted Score: 83%                            │
│   → Potential Grade: B (83-86% range)            │
└──────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────┐
│   OVERALL GRADE: B                               │
├──────────────────────────────────────────────────┤
│   Determined by:                                 │
│   • Potential Grade from Comprehensive: B        │
│   • Maximum Allowed from Foundation: B           │
│   • Overall: min(B, B) = B                       │
└──────────────────────────────────────────────────┘
```

**How it works:**
```
Step 1: Check Foundation Tiers
  TIER 1: 7/7 ✓ → PASS (no auto-fail)
  TIER 2: 2/3 ⚠ → Maximum Grade = B (cap applied)
  TIER 3: 2/4 ⚠ → Penalty = -5%

Step 2: Calculate Comprehensive
  Raw: 88%
  Adjusted: 88% - 5% = 83%
  Potential Grade: B (83% falls in 83-86% B range)

Step 3: Apply Gate
  Overall Grade = min(Potential Grade, Max Allowed)
  Overall Grade = min(B from comprehensive, B from foundation)
  Overall Grade = B
```

**Example:**
- Foundation: 75% (TIER 1 complete, but missing 1 TIER 2 and 2 TIER 3 controls)
- Comprehensive: 88% raw → 83% adjusted (after -5% penalty)
- Overall: Grade B
- **Message:** "Your comprehensive score of 88% would qualify for B+ grade, but missing 1 TIER 2 control caps you at B. Fix that control to unlock B+ potential."

**Strengths:**
- ✅ Crystal clear logic: IF-THEN gates are easy to understand
- ✅ Cannot mask problems (see Edge Case A comparison below)
- ✅ Maps to insurance underwriting decision trees
- ✅ Motivating: "Fix 1 control → unlock next grade level"
- ✅ Transparent: every grade cap is explained with specific missing controls

**Weaknesses:**
- ❌ More complex than single number
- ❌ Can feel "harsh" (92% comprehensive capped at B due to 1 TIER 2 gap)
- ❌ Requires more explanation to members initially

**Edge Case A: Cannot Mask Problems**
```
Foundation: 100% (perfect compliance - all 14 controls met)
Comprehensive: 45% (major gaps in non-foundation controls)

Progressive Gating Result:
  Foundation: 100% → Max Grade = A+ (no cap)
  Comprehensive: 45% → Grade F (< 60%)
  Overall: min(F, A+) = F

Member sees: F grade (accurate signal)
Reality: Major security gaps despite foundation compliance
Insurance Risk: Same as above, but VISIBLE in grade
```

The F grade accurately reflects that 45% comprehensive is unacceptable, regardless of foundation perfection.

---

## Side-by-Side Comparison: Same Organization, Three Models

**Organization:** Riverside High School

**Raw Data:**
- Foundation Questions (14):
  - TIER 1 (7): All met ✓
  - TIER 2 (3): 2 met, 1 missing (MFA for cloud resources)
  - TIER 3 (4): 3 met, 1 missing (phishing simulation)
- Comprehensive Questions (65): 85% average across all categories

**Model 1: Current Production**
```
Overall Score: 85%
Grade: B

Simple. One number. Done.
```

**Model 2: 80/20 Weighted**
```
Foundation: 79% (13 of 14 met)
Comprehensive: 85%

Overall = (0.80 × 79%) + (0.20 × 85%)
        = 63.2% + 17%
        = 80.2%

Grade: B-

Foundation score of 79% pulls overall down despite 85% comprehensive.
```

**Model 3: Progressive Gating**
```
Foundation: 79%
  TIER 1: 7/7 ✓ → PASS
  TIER 2: 2/3 ⚠ → Max Grade = B
  TIER 3: 3/4 ⚠ → Penalty = -3%

Comprehensive: 85% raw
               82% adjusted (-3% penalty)

Potential Grade: B (82% falls in 80-82% B- range, wait no, let me recalculate)
Actually 82% is B- (80-82%), not B (83-86%)

Max Allowed: B (from TIER 2 cap)

Overall: min(B-, B) = B-

Grade: B-

Message: "Your comprehensive score of 85% would qualify for B grade,
but missing 1 TIER 2 control and 1 TIER 3 control results in B- grade.
Fix MFA for cloud resources (TIER 2) to unlock B potential, and add
phishing simulation (TIER 3) to recover the 3% penalty."
```

**Comparison:**
| Model | Grade | Member Understanding | Insurance Clarity |
|-------|-------|---------------------|-------------------|
| Current | B | "I got 85%" | Unclear - missing MFA not visible |
| 80/20 | B- | "Where did 80.2% come from?" | Somewhat - foundation score visible |
| Progressive Gating | B- | "I'm missing MFA for cloud + phishing simulation" | Perfect - specific gaps identified |

---

## Visual: How Grades Change Across Models

**10 Example Organizations:**

| Org | Foundation | Comprehensive | Current | 80/20 | Progressive Gating | Biggest Change |
|-----|------------|---------------|---------|-------|-------------------|----------------|
| **A** | 98% | 95% | A (95%) | A (97%) | A+ | +1 grade level (current → gating) |
| **B** | 92% | 88% | B+ (88%) | B+ (90%) | A- | +1 grade level (foundation unlocks A) |
| **C** | 86% | 82% | B (82%) | B (85%) | B | No change (TIER 2 complete) |
| **D** | 75% | 88% | B+ (88%) | C+ (77%) | **B** | -1 grade level (80/20 harsh) OR +1 (vs 80/20) |
| **E** | 79% | 75% | C+ (75%) | C+ (78%) | C | -1 grade level (TIER 2 cap at C+, wait...) |
| **F** | 65% | 72% | C (72%) | C- (71%) | **C-** | No major change |
| **G** | 52% | 85% | B (85%) | D (61%) | **D-** | -3 grade levels (TIER 1 fail exposed) |
| **H** | 100% | 45% | F (45%) | B+ (89%) | **F** | **CRITICAL:** 80/20 MASKS problem |
| **I** | 50% | 95% | A (95%) | D (59%) | **D-** | -4 grade levels (TIER 1 fail exposed) |
| **J** | 88% | 60% | D+ (60%) | D (66%) | D+ | Foundation strong, comprehensive weak |

**Key Insights:**

**Organizations Most Impacted by Progressive Gating:**
- **Org G & I:** TIER 1 failures exposed (current model hides these)
- **Org H:** Critical edge case where 80/20 MASKS major problem (89% looks good, but 45% comprehensive is catastrophic)

**Organizations Benefiting from Progressive Gating:**
- **Org A & B:** Strong foundation unlocks higher grades (A+, A-)
- **Org D:** TIER 2 complete means no cap (achieves B despite 75% foundation)

**Organizations Penalized by Progressive Gating:**
- **Org E:** TIER 2 gap caps at C+, comprehensive score of 75% can't overcome it

---

## Decision Matrix: Which Model Should You Choose?

### Choose **Current Model** (keep as-is) if:
- ❌ You don't have time/resources for changes (requires 0 effort)
- ❌ Members are resistant to any grading changes
- ❌ Insurance pools don't require foundation emphasis
- ❌ You're okay with lack of insurance alignment

**Reality Check:** Your POC research shows this model doesn't align with insurance underwriting. Choosing this means accepting the misalignment.

---

### Choose **80/20 Weighted Model** if:
- ✅ You want aggressive foundation emphasis (80% weight)
- ✅ You want a single overall score (simplicity)
- ✅ You're okay with mathematical opacity ("where did this number come from?")
- ⚠️ You're aware of Edge Case H problem (100% foundation + 45% comprehensive = 89% masks issue)

**Reality Check:** Your POC tested this and found it "aggressively emphasizes foundation." But it lacks transparency and can mask problems. Members in your POC struggled with the weighted formula.

---

### Choose **Progressive Gating Model** if:
- ✅ You want perfect insurance alignment (decision tree logic)
- ✅ You want transparency (clear IF-THEN rules)
- ✅ You want actionable member messaging ("fix these 2 controls to unlock B potential")
- ✅ You're willing to invest in member education (9-month implementation)
- ✅ You're okay with some members feeling the system is "harsh" (but accurate)

**Reality Check:** This is the most rigorous, defensible, and insurance-aligned approach. But it requires commitment to implementation and change management.

---

## Visual: Foundation Tier Logic Flow

**Progressive Gating Model - How Grades Are Determined:**

```
START
  ↓
[Calculate Foundation Score: 0-100%]
  ↓
┌──────────────────────┐
│ Check TIER 1 (7Qs)   │
│ Any question = 5?    │ ←─── "Not Implemented" rating
└───────┬──────────────┘
        │
    YES │ NO
        ↓ ↓
        │ └────────→ [TIER 1 PASS]
        │                ↓
        │           [Check TIER 2 (3Qs)]
        │           How many met?
        │                ↓
        │           ┌────┴────┬────────┐
        │           3/3       2/3      1/3 or 0/3
        │           ↓         ↓        ↓
        │        [No cap]  [Cap=B]  [Cap=C+]
        │           ↓         ↓        ↓
        │           └─────┬───┴────────┘
        │                 ↓
        │           [Check TIER 3 (4Qs)]
        │           How many met?
        │                 ↓
        │           ┌─────┴─────┬──────────┐
        │           4/4         3/4        2/4 or less
        │           ↓           ↓          ↓
        │        [No penalty]  [-3%]     [-5%]
        │           ↓           ↓          ↓
        │           └─────┬─────┴──────────┘
        │                 ↓
        │          [Max Grade Determined]
        │          [Penalty Determined]
        │                 ↓
        ↓                 ↓
[TIER 1 FAIL]     [Calculate Comprehensive]
        ↓           (All 65 questions)
[Max Grade = D-]          ↓
        ↓           [Apply TIER 3 penalty]
        │                 ↓
        │           [Adjusted Comprehensive]
        │                 ↓
        │           [Convert to Potential Grade]
        │                 ↓
        └────────→ [Overall Grade = min(Potential, Max Allowed)]
                          ↓
                      [FINAL GRADE]
```

---

## Member Communication Examples

### Scenario: Organization with 92% Comprehensive, Capped at B

**Current Model Message:**
> Your overall security score is 92%, earning you an A- grade. Excellent work!

**80/20 Weighted Model Message:**
> Your foundation score is 81% and your comprehensive score is 92%.
> Your overall score is 87% [(0.80 × 81%) + (0.20 × 92%)], earning you a B+ grade.

*Member reaction: "Wait, I got 92% but only B+? And where did 87% come from?"*

**Progressive Gating Model Message:**
> Your comprehensive score of 92% demonstrates excellent security maturity
> and would normally qualify for an A grade.
>
> However, your foundation assessment reveals you are missing 1 of 3 TIER 2
> controls: MFA for cloud resources (including email and document storage).
>
> Missing this critical control caps your maximum overall grade at B.
>
> **The good news:** You are ONE CONTROL away from unlocking A-grade potential.
> Implementing MFA for cloud resources will:
> • Remove the B-grade cap
> • Immediately elevate you to A grade (your 92% comprehensive qualifies)
> • Improve your cyber insurance rate classification
>
> Estimated time to implement: 2-4 weeks
> Estimated effort: 20-40 hours
>
> This is a high-ROI improvement: fixing one control unlocks a full grade
> level increase. We're here to help you implement this quickly.

*Member reaction: "Okay, I understand. I need MFA for cloud resources. That makes sense. Let me talk to IT about getting that set up."*

---

## The Bottom Line

**Three grading models. Three different philosophies.**

**Current Model:**
- Philosophy: "All controls are equally important"
- Reality: They're not. Missing EDR is catastrophic; missing annual security training is not.

**80/20 Weighted Model:**
- Philosophy: "Foundation is 4× more important than comprehensive"
- Reality: Mathematical emphasis works, but lacks transparency and can mask problems.

**Progressive Gating Model:**
- Philosophy: "Foundation controls are gates that must be passed to unlock higher grades"
- Reality: Mirrors insurance underwriting, transparent rules, actionable member messaging.

**Which one aligns with how insurance carriers actually make decisions?**

**Progressive Gating.** Insurance underwriters don't use weighted formulas. They use decision trees:
1. Do they have EDR? No → Decline coverage
2. Do they have MFA? No → Decline coverage
3. Do they have air-gapped backups? No → Decline coverage
4. Do they have vulnerability scanning? No → Premium increase 30%
5. ... and so on.

**That's gating logic, not weighted averaging.**

---

## Recommended Path Forward

1. **Read:** The comprehensive methodology document (30,000 words)
2. **Validate:** Share with insurance advisors - does this match underwriting process?
3. **Decide:** Progressive Gating (Option A), Phased Implementation (Option B), or Enhanced Current (Option C)
4. **Plan:** 9-month implementation if Option A, 3-year if Option B, 6-month if Option C
5. **Execute:** Follow implementation guide in main document

---

**Document Prepared By:** Grading Methodology Advisory Team
**Related Documents:**
- `2026_COMPREHENSIVE_GRADING_METHODOLOGY.md` (main document)
- `2026_GRADING_METHODOLOGY_EXECUTIVE_SUMMARY.md` (quick summary)

**Version:** 1.0
**Date:** November 2, 2025

---

*Visual comparisons help. But read the full methodology for statistical rigor and implementation details.*
