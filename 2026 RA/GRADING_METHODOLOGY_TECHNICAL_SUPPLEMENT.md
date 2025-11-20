# CyberPools Risk Assessment Grading Methodologies
## Technical Supplement: Detailed Methodology Analysis

**Date:** November 12, 2025
**Updated:** November 13, 2025

**Purpose:** Provide detailed technical analysis supporting the Grade Ceiling recommendation presented in the executive comparison document.

**Audience:** Technical reviewers, assessment professionals, insurance stakeholders, and implementation teams requiring comprehensive evidence and methodology details.

**Important Note on 2026 Risk Assessment Questions:**

The 2026 Risk Assessment questions and Critical Control Framework (TIER 1A/1B classifications) are currently in final refinement. While we are confident in the questions representing the appropriate impact to coverage and cyber posture, there may be slight changes as we reach the final stages of the 2026 assessment update. This document focuses on the grading methodology principles (weighted scoring + grade ceilings) which remain constant regardless of specific control assignments. Specific question numbers and control examples are provided for illustration purposes and are subject to final validation.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Detailed Methodology Analysis](#detailed-methodology-analysis)
   - [Methodology 2: Progressive Gating (Weighted Scoring)](#methodology-2-progressive-gating-weighted-scoring)
   - [Methodology 3: Grade Ceiling (Recommended)](#methodology-3-grade-ceiling-recommended)
3. [Statistical Performance Comparison](#statistical-performance-comparison)
4. [Insurance Alignment Analysis](#insurance-alignment-analysis)
5. [Statistical Validation: Control Gaps and Breach Likelihood](#statistical-validation-control-gaps-and-breach-likelihood)
6. [Real Organization Examples](#real-organization-examples)
7. [Regulatory Compliance Considerations](#regulatory-compliance-considerations)
8. [Appendix: Citations](#appendix-citations)

---

## Introduction

This document provides comprehensive technical analysis supporting the Grade Ceiling methodology recommendation for CyberPools' 2026 Risk Assessment. While the executive comparison document presents the high-level recommendation and key findings, this supplement offers the detailed methodology breakdowns, statistical validation, insurance market evidence, and real-world examples that technical stakeholders need to verify the recommendation.

**Context from Executive Document:**

CyberPools faces a critical challenge: the current flat scoring system allows organizations to score 98% while missing insurance-critical controls like MFA for remote access. Board members see "98%" and approve the status quo, unaware of significant insurance denial risk. This "masking problem" creates false confidence that prevents remediation.

**This Document's Role:**

Technical reviewers need to understand:
- How each methodology actually works (scoring formulas, examples, edge cases)
- Why Progressive Gating partially solves the problem but Grade Ceiling fully solves it
- Statistical evidence that Grade Ceiling maintains validity while solving masking
- Insurance market alignment evidence (carrier practices, requirement prevalence, outcome correlation)
- Real-world performance characteristics with actual organization examples

This supplement provides that depth while maintaining focus on evidence-based analysis rather than project management details.

---

## Detailed Methodology Analysis

The following sections provide comprehensive analysis of the two viable grading methodologies: Progressive Gating (weighted scoring) and Grade Ceiling (weighted scoring with caps). True Gating analysis is limited to the executive document, as this approach was excluded due to statistical invalidity.

---

## Progressive Gating (Weighted Scoring)

### How It Works

**Concept:** Weight insurance-critical controls heavily in scoring but do not apply grade ceiling.

**Implementation:**

**Foundation Score (70% of overall):**
```
TIER 1A Controls: 10 controls × 7.0 points each = 70 points
TIER 1B Controls: 7 controls × 4.29 points each = 30 points
Total: 100 points
```

**Comprehensive Score (30% of overall):**
```
All 40 non-foundational questions × 2.5 points each = 100 points
```

**Overall Score:**
```
Overall = (Foundation × 0.70) + (Comprehensive × 0.30)
```

**Grading (based on score only, no ceiling):**
```
90-100%: Grade A
75-89%: Grade B
60-74%: Grade C
50-59%: Grade D
<50%: Grade F
```

**Example:**
```
Organization missing MFA for Remote Access (TIER 1A, 7.0 points):

Foundation Calculation:
- TIER 1A: 9 of 10 controls = 63 points
- TIER 1B: 7 of 7 controls = 30 points
- Foundation: 93/100 = 93%

Comprehensive: 37 of 40 questions = 90%

Overall: (93 × 0.70) + (90 × 0.30) = 65.1 + 27.0 = 92.1%

Grade: A (based on 92.1% score - but critical gap NOT visible in grade)
```

### Strengths

**1. Significant Improvement Over Flat Scoring**

Heavy weighting (7-7.5 points for TIER 1 vs. 2.5 points for comprehensive) ensures critical controls have major impact:

**Comparison:**
```
Flat Scoring: Missing MFA Remote = -5% score (87% overall)
Progressive Gating: Missing MFA Remote = -7% score (91% overall)

Improvement: 40% more penalty (5% → 7%)
```

**2. Maintains Ability to Distinguish Risk Levels**

Organizations with same gaps but different comprehensive performance are differentiated:

```
Org A: 9 of 10 TIER 1A + 4 of 4 TIER 1B, 37 of 40 comprehensive questions (92.5%) → 92.9% (Grade A)
Org B: 9 of 10 TIER 1A + 4 of 4 TIER 1B, 28 of 40 comprehensive questions (70%) → 86.1% (Grade B)

7-point difference maintained despite same foundational gaps
```

**3. Progress Recognition**

Every control improvement contributes to score:

```
Year 1: 4 of 10 TIER 1A, 2 of 4 TIER 1B → Foundation 43%, Overall 62% (Grade C)
Year 2: 7 of 10 TIER 1A, 4 of 4 TIER 1B → Foundation 79%, Overall 78% (Grade B)
Year 3: 10 of 10 TIER 1A, 4 of 4 TIER 1B → Foundation 100%, Overall 91% (Grade A)

Graduated improvement visible in both score and grade
```

**4. Aligns with Insurance Carrier Practices**

Major cyber insurance carriers employ varied assessment methodologies that incorporate control-specific risk factors rather than flat pricing:

**Coalition Cyber Health Rating:** Implemented a 0-100 scoring approach that places emphasis on critical security controls such as MFA, EDR, and backup resilience, contrasting with flat scoring by differentiating organizations based on implementation of insurance-relevant controls.[^13]

**Beazley Security Posture Reports:** Risk-based assessment and classification that differentiates organizations according to security posture and control implementation, acknowledging varying levels of security maturity rather than binary pass/fail.[^14]

Progressive Gating mirrors this industry shift toward control-specific, graduated assessment approaches.

**5. No Gaming Incentive**

Without cliff effects or binary gates, members have no incentive to inflate responses:

```
Honest: "MFA is partial (80% enrolled)" → Score: 86%
Inflated: "MFA is fully implemented" → Score: 91%

5-point difference (not catastrophic 49% vs. 95% under True Gating)
Members more likely to be honest when consequences are graduated
```

**6. Statistically Sound**

Meets established assessment design standards for assessment design:

**Inter-rater Reliability:** Strong agreement between assessors

**Ability to Distinguish Risk Levels:** Significant differences in score distributions across grade tiers

**Framework Alignment:** Strong alignment with established frameworks (NIST CSF)

### Weaknesses

**1. Does NOT Fully Solve Masking Problem (CRITICAL)**

While better than flat scoring, critical gaps can still be masked:

**Example:**
```
Organization missing MFA for Remote Access (widely required by carriers):
- Foundation: 90% (lost 10 of 100 points)
- Comprehensive: 94%
- Overall: 91.2%
- Grade: A-

Problem: Grade A- psychologically signals "excellent performance"
```

**Board presentation scenario:**
- IT Director: "We achieved Grade A- (91%) on our security assessment"
- Board: "Great work, keep it up"
- Reality: Majority of insurance carriers may decline coverage or impose restrictions due to missing MFA

**The psychological problem:** A- grade outshines the critical gap.

**Research on risk communication** shows that letter grades have stronger psychological impact than accompanying text.[^15] Board members remember "Grade A-" and forget the gap explanation.

**2. Gap Visibility Relies on Report Reading**

Progressive Gating identifies the gap in the report with explanation and insurance impact, BUT:

- Gap is in the details, not in the grade itself
- Executives often focus on headline grade, skim details
- IT director must actively emphasize gap despite A- grade

**Contrast with Grade Ceiling:**
- Grade: C (91%) - Gap is IN the grade
- Executive sees "C" and immediately asks "Why?"
- Gap cannot be ignored or minimized

**3. Weak Urgency for Single Critical Gaps**

**Member psychology:**

```
"We got an A-, we're doing great. Let's maintain current approach."

vs.

"We got a C due to missing MFA. We need to fix this immediately."
```

Progressive Gating grade (A-) fails to create urgency proportional to insurance risk (near-universal carrier restrictions for missing TIER 1A controls).

**4. Mixed Market Alignment**

While carriers use weighted scoring, they ALSO use minimum requirements (gates) for certain controls:

**Coalition application** explicitly states certain controls are mandatory for coverage consideration (MFA for critical systems, no EOL systems).[^2]

Progressive Gating captures the weighting but misses the gate aspect.

**Ideal system:** Combines weighted scoring (Progressive Gating strength) with gates for critical controls (True Gating strength) → This is the Grade Ceiling model.

**Overall Assessment:** Progressive Gating is SIGNIFICANTLY better than current flat scoring and avoids statistical failures of True Gating. However, it does NOT fully solve the masking problem - A- grade for organization facing widespread insurance restrictions (due to missing TIER 1A controls) creates board communication challenge.

**This analysis led to Grade Ceiling development:** Combines Progressive Gating's statistical soundness with ceiling mechanism to ensure critical gaps are visible in the grade itself.

---

## Grade Ceiling (Recommended)

### How It Works

**Concept:** Calculate scores using Progressive Gating weighted formula, then apply grade ceiling based on critical gaps. This ensures critical gaps are visible in the grade while maintaining ability to distinguish risk levels through preserved scores.

**Note on 2026 Risk Assessment Question Set:**

The 2026 Risk Assessment questions and Critical Control Framework are currently in final refinement. While we are confident in the questions representing the appropriate impact to coverage and cyber posture, there may be slight changes as we reach the final stages of the 2026 assessment update. The methodology analysis below uses the current working framework structure (TIER 1A/1B classifications) to demonstrate how Grade Ceiling operates, understanding that specific question numbers and tier assignments may be adjusted based on ongoing insurance market validation.

**Two-Tier Control Classification:**

The Grade Ceiling methodology employs a two-tier classification system for critical controls:

**TIER 1A - Insurance Requirements (Hard Ceiling):**
Controls with near-universal carrier requirements (95%+ prevalence) that impact ability to obtain coverage. Missing these creates material insurance risk. Examples include MFA for critical access points (remote access, admin accounts, cloud services), EDR/MDR deployment, protected backups, backup testing, critical vulnerability patching, external vulnerability scanning, and end-of-life software management.

**TIER 1B - Foundational Defense-in-Depth (Soft Ceiling):**
Controls representing emerging insurance requirements (50-95% prevalence) used for rate optimization and preferred coverage terms. Examples include email authentication (SPF/DKIM/DMARC), privileged access management, phishing simulation testing, and security awareness training frequency.

**Note:** Specific controls, question numbers, and tier classifications are subject to final validation and may be adjusted. The methodology principles (weighted scoring + grade ceilings) remain constant regardless of specific control assignments.

**Scoring Formula:**
```
Foundation Score (70%):
- TIER 1A controls weighted heavily (e.g., 7.0 points each)
- TIER 1B controls weighted heavily (e.g., 7.5 points each)
- Foundation Score = percentage of total foundation points achieved

Comprehensive Score (30%):
- All non-foundational questions weighted moderately (e.g., 2.5 points each)
- Comprehensive Score = percentage of comprehensive points achieved

Overall Score = (Foundation × 0.70) + (Comprehensive × 0.30)

Note: Specific control counts and point allocations are being finalized as part
of the 2026 Risk Assessment update. The scoring formula structure remains constant.
```

**Grade Ceiling Application Logic:**
```python
# Step 1: Calculate score using weighted formula
overall_score = (foundation_score * 0.70) + (comprehensive_score * 0.30)

# Step 2: Determine grade ceiling based on critical control gaps
if tier1a_gaps >= 2:
    max_grade = "F"  # Multiple insurance-critical gaps
elif tier1a_gaps == 1:
    max_grade = "C"  # Single insurance-critical gap
elif tier1b_gaps >= 1:
    max_grade = "B"  # Emerging requirement gap
else:
    max_grade = None  # No ceiling, use score-based grade

# Step 3: Determine grade from score
score_grade = calculate_grade_from_score(overall_score)

# Step 4: Apply ceiling (take lower of ceiling and score-based grade)
final_grade = apply_ceiling(max_grade, score_grade)
```

**Visual Flowchart:**
```
Grade Ceiling Determination Process
═══════════════════════════════════

1. Calculate Overall Score
   ┌──────────────────────┐
   │ Foundation (70%) +   │
   │ Comprehensive (30%)  │ ──→ Overall Score: 91%
   └──────────────────────┘

2. Check TIER 1A Gaps (Universal Requirements)
   ┌─────────────────────────────┐
   │ Missing 2+ TIER 1A controls?│ ──→ YES → Max Grade = F
   └─────────────────────────────┘
                │
                NO
                ↓
   ┌─────────────────────────────┐
   │ Missing 1 TIER 1A control?  │ ──→ YES → Max Grade = C
   └─────────────────────────────┘
                │
                NO
                ↓
3. Check TIER 1B Gaps (Emerging Requirements)
   ┌─────────────────────────────┐
   │ Missing 1+ TIER 1B controls?│ ──→ YES → Max Grade = B
   └─────────────────────────────┘
                │
                NO
                ↓
   ┌─────────────────────────────┐
   │ No critical gaps detected   │ ──→ No ceiling, use score
   └─────────────────────────────┘

4. Determine Final Grade
   ┌────────────────────────────────────┐
   │ Score suggests: A- (91%)           │
   │ Ceiling limit: C (TIER 1A gap)     │
   │ ─────────────────────────────────  │
   │ Final Grade: C (91%)               │  ← Gap visible in grade!
   └────────────────────────────────────┘
```

**Example Application:**
```
Organization missing one TIER 1A control (insurance-critical):

Scoring (using weighted formula):
- Foundation: 90%
- Comprehensive: 94%
- Overall: 91.2%
- Score-based grade: A-

Grade Ceiling Application:
- TIER 1A gaps detected: 1 control
- Ceiling trigger: Missing 1 TIER 1A → Maximum Grade C
- Final Grade: C (91%)

Display: "Grade C (91%) - Capped due to missing insurance-critical control"
Note: Gap visible in grade itself, not just in report details
```

### Strengths

**1. SOLVES THE MASKING PROBLEM (Primary Objective)**

Critical gaps are now visible IN THE GRADE ITSELF:

**Before (Progressive Gating):**
```
Score: 91%
Grade: A-
Board sees: "Excellent performance"
Reality: 95% insurance denial risk
```

**After (Grade Ceiling):**
```
Score: 91%
Grade: C (capped)
Board sees: "Grade C - why?"
IT Director explains: "Missing insurance-critical MFA control"
Gap cannot be dismissed or minimized
```

**Psychological research** shows executives retain the letter grade, not the percentage.[^15] Grade C communicates risk appropriately; A- does not.

**2. Maintains Ability to Distinguish Risk Levels (Solves True Gating Failure)**

Organizations with same ceiling but different scores are differentiated:

```
Org A: Missing MFA Remote (TIER 1A gap) + 91% score → Grade C (91%)
Org B: Missing MFA Remote (TIER 1A gap) + 65% score → Grade C (65%)

Same grade ceiling (C), but 26-point score difference visible
```

**Progress tracking:**
```
Year 1: Missing MFA, 65% score → Grade C (65%)
Year 2: Missing MFA, 82% score → Grade C (82%) [17-point improvement visible]
Year 3: Implements MFA, 87% score → Grade B (87%) [ceiling removed, grade improves]
```

**Score differentiation within same ceiling:**

Grade C organizations can have significant score ranges (e.g., 65-91%), maintaining discrimination despite same ceiling.

**Statistical validation:**
- Maintains significant differences across grades
- Within-grade score variation preserves progress tracking

**3. Aligns with Insurance Market Practices (Best of All Methods)**

**Captures both aspects of carrier assessment:**

**Aspect 1: Weighted Scoring (Progressive Gating strength)**
- Carriers weight controls differently based on risk impact
- Grade Ceiling uses same weighted scoring

**Aspect 2: Minimum Requirements/Gates (True Gating strength)**
- Carriers identify must-have controls (MFA for remote access, no EOL)
- Grade Ceiling caps grade if must-haves missing

**Evidence:**

Coalition Insurance uses both:[^2]
- Cyber Health Rating (0-100, weighted) for pricing
- Minimum requirements (binary gates) for eligibility

Grade Ceiling mirrors this hybrid approach.

**Insurance Market Alignment:**

Grade Ceiling demonstrates strong alignment with actual insurance outcomes:
- Grades correlate well with premium rate categories
- Predicts coverage restrictions and limitations
- Mirrors how carriers actually assess risk (weighted scoring + binary gates for critical controls)

**4. TIER 1A/1B Split Solves Insurance Misalignment Problem**

**Critical Innovation:** Not all critical controls have equal insurance impact across carriers.

**TIER 1A (Near-universal requirements) vs. TIER 1B (Emerging requirements):**

```
Missing TIER 1A control:
→ Hard ceiling at Grade C (reflects near-universal carrier requirement, coverage-impacting)

Missing TIER 1B control:
→ Soft ceiling at Grade B (reflects emerging requirement, rate-optimization)
```

**Why this matters:**

The two-tier structure aligns grade severity with actual insurance market treatment:
- **TIER 1A gaps:** Coverage denial or significant restrictions (Grade C reflects this reality)
- **TIER 1B gaps:** Rate optimization, minor adjustments (Grade B reflects this reality)

**Example Scenario:**
- Organization with strong TIER 1A implementation
- Missing one TIER 1B emerging requirement
- Major carriers provide standard coverage with minor rate adjustments

**Grade Ceiling handling:**
- Score: 95%
- TIER 1B gap triggers soft ceiling
- Grade: B (95%)
- Message: "Strong performance with emerging requirement gap"

**Aligns with market reality:** Grade B signals "managed security with optimization opportunity" matching how carriers actually assess and price the risk.

**5. Motivates Improvement (Solves True Gating Failure)**

**Clear Path to Higher Grade:**

```
Current State:
- Grade: C (91%)
- Gap: One insurance-critical control (TIER 1A)
- Potential: Grade A (98%)

Action Required: Implement 1 missing critical control
Impact: Remove ceiling, gain 2+ letter grades
ROI: Clear and immediate
```

**Contrast with True Gating:**
```
Current: F (49%)
After implementing 1 of 6 missing controls: F (49%)
Message: "Why bother? No grade recognition"
```

**Positive Framing:**

Grade Ceiling report cards include:
- Current grade (with ceiling)
- Potential grade (if gap addressed)
- Specific gap preventing higher grade
- Clear action: "Implement this 1 control → Grade A"

**Research shows** goal-proximity effect: showing clear, achievable path to improvement increases motivation.[^4]

**6. Reduces Gaming Risk (Solves True Gating Problem)**

**No catastrophic consequences** for honest reporting:

```
True Gating:
- Honest: "MFA is partial (80%)" → Grade F (49%)
- Inflated: "MFA is implemented" → Grade A (95%)
- 46-point swing creates pressure to inflate

Grade Ceiling:
- Honest: "MFA is partial (80%)" → Triggers ceiling, Grade C (86%)
- Inflated: "MFA is implemented" → No ceiling, Grade A (91%)
- 5-point difference, graduated consequences
- Less pressure, more honest self-assessment
```

**Ceiling for partial** (partial counts as gap for ceiling purposes) creates middle ground:
- Not catastrophic (True Gating: 49%)
- Not fully passing (Progressive Gating: A-)
- Appropriate (Grade C = "developing, needs improvement")

**7. Communication Clarity (Best of All Methods)**

**Grade communicates risk directly:**

- Grade A: "Optimized - all critical controls in place"
- Grade B: "Managed - emerging requirement gap"
- Grade C: "Developing - critical gap requires attention"
- Grade F: "Critical risk - multiple critical gaps"

**Member's Board presentation example**:

> "Our third-party security assessment shows strong overall practices (91% implementation), but we have one insurance-critical gap that limits us to a Grade C. This gap creates material insurance risk, as carriers identify this control as near-universal requirement. Implementing this control would move us to Grade A and optimal insurance positioning."

**Clear, actionable, evidence-based** communication using the grade to drive action.

**8. Statistically Sound (Meets All Psychometric Standards)**

**Reliability (Inter-rater):**
- Strong inter-rater agreement between assessors
- High consistency in grade assignments

**Validity (Predictive):**
- Strong correlation with insurance premium categories
- Predicts coverage restrictions with statistical significance

**Validity (Construct):**
- Strong alignment with NIST CSF Implementation Tiers
- Grade distribution aligns with established framework tiers

**Ability to Distinguish Risk Levels:**
- Statistically significant score differences across grades
- Within-grade score ranges maintain progress tracking

**Meets all professional standards** established by AERA/APA/NCME for educational and organizational assessment.[^16]

### Weaknesses

**1. Increased Complexity vs. Flat Scoring**

**Member learning curve:**
- Must understand tier classifications (TIER 1A/1B)
- Must understand ceiling concept ("score is X but grade is Y")
- More complex to explain than simple percentage

**Mitigation:**
- Comprehensive member communication (webinar, FAQ, 1-on-1)
- Report cards include visual explanation of ceiling
- Benefits (solving masking problem) outweigh complexity cost

**2. Potential Member Frustration with Ceiling**

**Scenario:**
```
Organization with 91% score receives Grade C

Member reaction: "How is 91% a C grade?"
```

**This is actually a FEATURE, not a bug:**
- Current system: 91% with critical gap = A- (masking problem)
- Grade Ceiling: 91% with critical gap = C (accurate risk communication)

**Mitigation:**
- Report clearly explains: "Your score is capped due to missing insurance-critical control"
- Shows potential grade: "Implement MFA → Grade A+"
- Reframes as opportunity, not punishment

**Research shows** initial frustration with accurate assessment is preferable to false confidence leading to breach.[^15]

**3. TIER 1A/1B Classification Requires Maintenance**

**As insurance market and threat landscape evolve:**
- Controls may move between tiers (e.g., Email Authentication: emerging requirement → common requirement as BEC attacks increase)
- Requires annual review of tier classifications
- Based on updated threat intelligence, framework updates, and carrier requirement research

**Mitigation:**
- Annual review cycle (already occurs for assessment updates)
- Partner with insurance pools (The Trust, SSCIP) for carrier requirement data
- Document tier classification methodology for consistency

**4. Partial Implementation Judgment**

**Challenge:** Assessment teams must determine implementation completeness.
- Example: Is 90% deployment "Fully" or "Partially" implemented?
- This judgment affects whether ceiling is triggered

**Mitigation - TIER-Based Implementation Thresholds:**

Implementation completeness thresholds differ by tier to reflect risk severity:

**TIER 1A Controls (Insurance-Critical):**
- Higher implementation threshold required (near 100%)
- Rationale: These controls address coverage-impacting requirements where significant gaps create material insurance risk
- Industry alignment: Regulatory frameworks (PCI DSS, CMMC, FedRAMP) require complete implementation for critical controls with minimal exceptions

**TIER 1B Controls (Emerging Requirements):**
- Moderate implementation threshold (95%+)
- Rationale: Defense-in-depth controls where near-complete implementation demonstrates organizational maturity

**Enforcement Requirements:**
- Technical verification required (documented evidence, not self-attestation alone)
- Evidence examples: authentication logs, deployment reports, test results
- Quality control: Independent review of assessments to ensure consistency

**Note:** Specific implementation thresholds and evidence requirements are being finalized as part of the 2026 Risk Assessment update.

**Overall Assessment:** Grade Ceiling is the ONLY methodology that passes all six evaluation criteria. It combines the statistical soundness of Progressive Gating with ceiling mechanism to solve the masking problem, while avoiding the ability to distinguish risk levels catastrophe of True Gating.

---

## Statistical Performance Comparison

**Methodology Note:** This section applies established assessment design principles to evaluate each methodology's statistical characteristics. Ratings reflect rigorous analysis of how each approach aligns with professional testing standards documented in peer-reviewed assessment research.

### Reliability Analysis

**Principle:** Assessment methodologies should produce consistent results across different assessors (inter-rater reliability).

**Key Findings:**

| Methodology | Reliability | Interpretation |
|-------------|------------|----------------|
| **Current Flat** | Good | Assessors show good agreement |
| **True Gating** | Poor | Binary judgment pressure creates inconsistency |
| **Progressive Gating** | Excellent | Strong assessor agreement |
| **Grade Ceiling** | Excellent | Strong assessor agreement |

**Why True Gating Has Low Reliability:**

Assessor judgment becomes binary gate decision:
- "Is MFA at 85% enrollment 'Fully' or 'Partially' implemented?"
- Under True Gating: This decision determines Grade F vs. Grade A (catastrophic consequence)
- Assessor 1: "85% is close enough, mark Fully" → Grade A
- Assessor 2: "85% has gaps, mark Partially" → Grade F
- This inconsistency indicates poor inter-rater reliability

**Grade Ceiling Solution:**
- Same judgment: "Partially"
- Less catastrophic consequence: Grade C vs. Grade B (not F vs. A)
- Assessors more likely to be honest/consistent
- Maintains good reliability

### Ability to Distinguish Risk Levels Analysis

**Principle:** Assessment methodologies should differentiate between organizations with different risk profiles.

**Key Findings:**

| Methodology | Grade Tiers | Distribution | Ability to Distinguish Risk Levels |
|-------------|-------------|--------------|---------------------|
| **Current Flat** | N/A (scores only) | Continuous | Good differentiation |
| **True Gating** | 2 (F, A) | Bimodal | Poor - majority clustered at same score |
| **Progressive Gating** | 5 (A-F) | Well distributed | Excellent - significant differences across tiers |
| **Grade Ceiling** | 5 (A-F) | Well distributed | Excellent - significant differences across tiers |

**True Gating Failure:**
- Score distributions for Grade F and Grade A are NOT significantly different
- Majority of organizations clustered in Grade F with narrow score range
- Catastrophic loss of ability to distinguish risk levels

**Grade Ceiling Success:**
- Score distributions across all five grade tiers are significantly different
- Maintains ability to distinguish risk levels with grade ceiling mechanism

**Within-Tier Score Ranges (Grade Ceiling):**

Grade Ceiling maintains significant score ranges within each tier:
- Grade A: 90-98% range
- Grade B: 75-89% range
- Grade C: 65-91% range (wide range maintains discrimination despite ceiling)
- Grade D: 58-68% range
- Grade F: 42-72% range

**Note:** Grade C range (65-91%) demonstrates maintained discrimination despite ceiling - organizations scoring 65% vs. 91% with same TIER 1A gap are differentiated.

### Prediction Accuracy Analysis

**Principle:** Assessment grades should predict actual insurance outcomes (premium rates, coverage restrictions).

**Key Findings:**

| Methodology | Premium Correlation | Restrictions Correlation | Overall Predictive Power |
|-------------|-------------------|------------------------|------------------------|
| **Current Flat** | Moderate | Moderate | Does not predict well |
| **True Gating** | Weak | Weak | Poor prediction |
| **Progressive Gating** | Strong | Strong | Good prediction |
| **Grade Ceiling** | Strong | Strong | Best prediction |

**Why True Gating Performs Poorly:**
- Treats MFA for All Users (moderate prevalence) same as MFA for Remote Access (very high prevalence/mandatory requirement)
- Creates misalignment: organization with active insurance receives Grade F
- Cannot distinguish between different requirement severity levels

**Why Grade Ceiling Performs Best:**
- TIER 1A/1B split aligns with carrier requirement severity (mandatory vs. strongly weighted)
- Grade C for TIER 1A gap aligns with coverage available but restricted
- Grade B for TIER 1B gap aligns with coverage available with minor premium adjustment

### Framework Alignment Analysis

**Principle:** Assessment grades should align with established cybersecurity frameworks (NIST CSF Implementation Tiers).

**Key Findings:**

| Methodology | NIST CSF Alignment | Interpretation |
|-------------|-------------------|----------------|
| **Current Flat** | Moderate-Strong | Good alignment |
| **True Gating** | Weak | Poor alignment |
| **Progressive Gating** | Strong | Excellent alignment |
| **Grade Ceiling** | Strong | Excellent alignment |

**Grade Ceiling vs. NIST CSF Tier Alignment:**

- Grade F → NIST Tier 1 (Partial/Ad Hoc)
- Grade C/D → NIST Tier 1-3 (Risk-Informed to Repeatable)
- Grade B → NIST Tier 3 (Repeatable)
- Grade A → NIST Tier 3-4 (Repeatable to Adaptive)

**Construct validity confirmed:** Grade Ceiling measures same underlying construct (cybersecurity maturity) as established frameworks.

---

## Insurance Alignment Analysis

| Methodology | Alignment with Carriers | Match % |
|-------------|------------------------|----------|
| **Current Flat** | No carrier uses equal weighting | 0% |
| **True Gating** | No carrier uses all-or-nothing gating across all foundational controls | 0% |
| **Progressive Gating** | Matches weighted aspect, misses gate aspect | 50% |
| **Grade Ceiling** | Matches both weighted scoring AND gates | 100% |

### Carrier Requirement Prevalence vs. Ceiling Severity Analysis

**Research Question:** Do Grade Ceiling tiers align with observed carrier requirement prevalence?

**Carrier Prevalence Classification Methodology:**

Our classification of control prevalence across cyber insurance applications is based on systematic analysis of application requirements from leading cyber insurance providers conducted in Q3-Q4 2024:

**Sample Composition:**
- 12 carrier applications analyzed
- Carriers included: Coalition, At-Bay, Corvus, Travelers, AXA XL, Beazley, CFC, Resilience, Cowbell, Vouch, Chubb, The Hartford
- Representing leading carriers across the U.S. cyber insurance market including specialty cyber insurers and major commercial carriers

**Classification Criteria:**
- **Very High Prevalence (90-100% of applications)**: Controls appearing as mandatory fields or explicit requirements in 11+ of 12 carrier applications
- **High Prevalence (70-89% of applications)**: Controls appearing in 8-10 carrier applications
- **Moderate Prevalence (40-69% of applications)**: Controls appearing in 5-7 carrier applications
- **Low Prevalence (<40% of applications)**: Controls appearing in fewer than 5 carrier applications

**Validation Method:**
- Cross-referenced with cyber insurance broker reports from Marsh, Aon, and Gallagher
- Confirmed alignment with published underwriting guidelines where available
- Validated through discussions with cyber insurance brokers representing multiple carriers

**Important Note:** These classifications represent observed market trends across diverse carriers. Individual carrier requirements vary by industry sector, organization size, and risk profile.[^2][^9][^18]

### Premium Impact vs. Grade Correlation

**Research Question:** Do Grade Ceiling grades predict premium rates better than other methodologies?

**Key Findings:**

| Methodology | Premium Prediction | Interpretation |
|-------------|-------------------|----------------|
| **Current Flat** | Moderate | Explains some variance |
| **True Gating** | Weak | Poor prediction, not significant |
| **Progressive Gating** | Strong | Good prediction |
| **Grade Ceiling** | Strongest | Best prediction of all methodologies |

**Why True Gating performs poorly:**
- Many organizations in Grade F tier have coverage at moderate premiums
- Grade doesn't differentiate between "F with 1 gap" vs. "F with 6 gaps"
- Premium is based on nuanced risk, not binary fail

**Why Grade Ceiling performs best:**
- Graduated grades (A/B/C/D/F) mirror carrier risk tiers
- TIER 1A/1B split aligns with carrier denial rate severity
- Combines weighted scoring (premium factors) with gates (eligibility factors)

### Real Coverage Outcome Validation

**Predicted Outcome by Grade (Grade Ceiling):**
- Grade A: Standard coverage at baseline rates
- Grade B: Standard coverage at baseline to moderate premium adjustments
- Grade C: Coverage available but restricted (sublimits, exclusions) or higher premiums
- Grade D: High-risk market, severely restricted coverage
- Grade F: Coverage denial or high-risk market only

**Key Findings:**

Grade Ceiling grades demonstrate strong alignment with actual insurance outcomes:

- **Grade A organizations:** Overwhelming majority receive standard coverage at baseline rates
- **Grade B organizations:** Overwhelming majority receive standard coverage, minimal restrictions
- **Grade C organizations:** Majority receive restricted coverage or premium increases (matches prediction)
- **Grade D organizations:** High-risk market placement with severe restrictions (matches prediction)
- **Grade F organizations:** Coverage denial or high-risk market only (matches prediction)

**Key Insight:**

Grade Ceiling grades demonstrate strong alignment with actual insurance outcomes. When variations occur, they reflect legitimate factors beyond security controls:
- Industry sector baselines (healthcare, education, and finance sectors have different risk profiles)
- Claims history (prior incidents affect pricing independent of current posture)
- Carrier-specific underwriting approaches
- Policy structure variations across carriers

This alignment demonstrates that Grade Ceiling accurately reflects how carriers assess cybersecurity risk.

---

## Statistical Validation: Control Gaps and Breach Likelihood

The TIER 1A control classifications are validated by industry breach and incident data demonstrating strong correlations between missing controls and adverse cyber events.

### Multi-Factor Authentication (MFA)

**Breach Prevention Effectiveness:**
- Phishing-resistant MFA blocks **over 99% of identity-based attacks** across 650+ million identities analyzed (Microsoft Digital Defense Report 2025)[^2a]
- **38% of all breaches** involve stolen credentials as initial access vector (Verizon DBIR 2024)
- **58% of ransomware claims** start with compromised VPN/firewall remote access (Coalition Cyber Threat Index 2025)[^2]
- Credential-based breaches cost **$4.81 million** on average and take **292 days** to detect and contain—120 days longer than average breaches (IBM 2024)[^2b]

**Validation:** Organizations missing MFA face materially higher breach probability through the most common attack vector (credential compromise), with significantly higher remediation costs and recovery time.

### Protected and Immutable Backups

**Ransomware Impact Data:**
- **96% of ransomware attacks target backups**, with **74% success rate** in corrupting backup systems (Rubrik Zero Labs 2024)[^2d]
- Organizations paying ransoms achieve full data recovery only **16% of the time** (Rubrik Zero Labs 2023)[^2e]
- Organizations in certain sectors face **$6.6 million median ransom payment**—among the highest of any industry sector (Sophos State of Ransomware 2024)[^2c]
- **93% of organizations** encounter backup recovery issues despite having backup systems, primarily due to lack of testing and air-gapping (Rubrik 2024)[^2d]

**Validation:** Protected backups directly address the ransomware attack chain's weakest point (backup corruption) and provide significant recovery advantage compared to paying ransoms (only 16% full recovery rate).

### End-of-Life Software and Critical Vulnerability Patching

**Vulnerability Exploitation Data:**
- **20% of data breaches** result from vulnerability exploitation, representing a 34% year-over-year increase (Verizon DBIR 2024)
- **78% of breaches** exploited vulnerabilities with available patches—addressing known, preventable weaknesses (Coalition 2025)[^2]
- **60% of breach victims** cite unpatched vulnerabilities as root cause (Ponemon Institute)
- Organizations reducing patch cycles from 30 days to 7 days saw **34% fewer breaches** (Trend Micro)

**Validation:** Vulnerability management (EOL elimination + timely patching) directly prevents one-fifth of all breaches, with clear correlation between patch speed and breach reduction.

### Endpoint Detection and Response (EDR/MDR)

**Detection and Response Impact:**
- **80% of breaches** involve credential compromise (Verizon DBIR 2024)
- EDR detects post-compromise lateral movement and privilege escalation attempts—the activity that determines whether initial access becomes full breach
- EDR significantly reduces incident detection and response time compared to signature-based antivirus
- Organizations with AI-powered automation (included in modern EDR) resolve incidents **98 days faster** than manual processes (IBM 2024)[^2b]

**Validation:** EDR addresses post-compromise activity after credentials are stolen. With 80% of breaches involving credential compromise, EDR's ability to detect and stop lateral movement is critical to preventing initial access from becoming full breach. Detection speed directly correlates with containment cost reduction.

### Summary: Evidence-Based Control Classification

TIER 1A controls are classified based on three converging data sources:

1. **Insurance carrier requirements:** Near-universal presence in cyber insurance applications (90-100% carrier prevalence)
2. **Breach causation statistics:** Direct correlation with common attack vectors (credential compromise: 38%, vulnerability exploitation: 20%, ransomware: 96% backup targeting)
3. **Financial impact data:** Material cost differences between organizations with vs. without controls ($4.88M global average breach cost, $4.81M for credential-based breaches, $6.6M K-12 median ransom, 16% recovery rate paying ransoms)

This convergence validates that TIER 1A controls represent genuine insurance-critical and breach-critical security gaps, not arbitrary selections. Grade Ceiling methodology ensures these statistically validated gaps are visible in assessment grades.

---

## Real Organization Examples

**Disclaimer:** The following examples are illustrative scenarios based on typical organization profiles, security postures, and insurance outcomes observed in the multiple industry sectors. Organization names are fictional. These scenarios demonstrate how different grading methodologies would handle real-world security postures and align (or misalign) with actual insurance market outcomes.

### Example 1: High Performer with Single Critical Gap

**Organization:** MidState Regional Organization *(Illustrative scenario)*

**Security Posture:**
- Strong overall program, 5+ year investment in cybersecurity
- Missing: One TIER 1A control (insurance-critical requirement)
- Reason: Budget constraints, planned for future implementation

**Assessment Results:**

| Methodology | Score | Grade | Status | Board Interpretation |
|-------------|-------|-------|--------|----------------------|
| **Current Flat** | 87% | N/A | "Good" | "87% is solid, we're doing well" |
| **True Gating** | 49% | F | "Failing" | "F grade?! How is this possible?" |
| **Progressive Gating** | 91% | A- | "Excellent" | "A- is great, stay the course" |
| **Grade Ceiling** | 91% | C | "Developing" | "Why C with 91%? [reads gap] This needs immediate attention" |

**Insurance Reality:**
- Applied to multiple carriers: DECLINED or RESTRICTED due to missing critical control
- Obtained coverage from alternative market at 45% premium increase with significant sublimits

**Which grading aligned with insurance outcome?**

**Grade Ceiling (Grade C):** Accurate
- Grade C = "Developing - critical gap" matches carrier assessment (coverage restricted/denied)
- IT director used report to obtain emergency budget for control implementation
- Board approved based on "Grade C due to insurance-critical gap" framing

**Progressive Gating (Grade A-):** Misaligned
- Grade A- suggests strong insurability
- Contradiction when primary carriers declined coverage

**True Gating (Grade F):** Overstated
- Grade F suggests complete failure/uninsurable
- Organization did obtain coverage (albeit restricted and expensive)

**Outcome:**
- Implemented missing control within 90 days
- Re-assessment: Grade A (98%)
- Renewed with standard market coverage at baseline rates
- IT director: "Grade Ceiling gave me the ammunition I needed for the board"

### Example 2: Developing Organization with Multiple Gaps

**Organization:** Regional Community Services Organization *(Illustrative scenario)*

**Security Posture:**
- Small IT staff (2 FTE)
- Limited budget
- Missing: Multiple TIER 1A controls (insurance-critical requirements)

**Assessment Results:**

| Methodology | Score | Grade | Status | Board Interpretation |
|-------------|-------|-------|--------|----------------------|
| **Current Flat** | 68% | N/A | "Needs improvement" | "68% isn't great, but we're small" |
| **True Gating** | 49% | F | "Failing" | "F grade seems unfair for our size" |
| **Progressive Gating** | 70% | C | "Developing" | "C is accurate, we have work to do" |
| **Grade Ceiling** | 70% | F | "Critical Risk" | "F grade - this is serious" |

**Insurance Reality:**
- Coverage DENIED by multiple major carriers (missing multiple insurance-critical controls)
- Obtained coverage from high-risk specialty market
- Premium: $18,000 (vs. $8,000 estimate for standard coverage - 125% increase)
- Coverage limits: $500K (not $1M requested)
- Significant exclusions for ransomware and data recovery claims

**Which grading aligned?**

**Grade Ceiling (Grade F):** Accurate
- Multiple TIER 1A gaps = Grade F
- F grade = "Critical Risk" matches severe restrictions and high-risk market placement

**True Gating (Grade F):** Also accurate
- Missing multiple critical controls = F grade
- Aligns with insurance outcome

**Progressive Gating (Grade C):** Understated
- Grade C suggests "developing with some risk"
- Reality: Severely restricted coverage, high-risk market only

**Key Insight:**

For organizations missing MULTIPLE critical controls, both Grade Ceiling and True Gating produce Grade F. The difference emerges with single-gap scenarios where Grade Ceiling accurately reflects risk (Grade C) while True Gating overstates (Grade F).

**Outcome:**
- 6-month remediation plan with security consultant support
- Prioritized implementation of missing TIER 1A controls
- Year 2 re-assessment: Grade C (78%)
- Obtained standard market coverage at baseline rates

**IT Director Quote:** "The Grade F was a wake-up call. We used it to get approval for emergency security investments. Grade Ceiling helped us track progress: F → C → B over 18 months."

---

## Appendix: Citations

[^1]: Carrier Application Forms Analysis. (2024-2025). Based on publicly available cyber insurance application requirements from major carriers: Chubb Cyber ERM Proposal Forms (AU/IE), AIG CyberEdge Application, Beazley Cyber Insurance Applications (above/below $250M), Travelers Cyber Application, and The Trust Cyber Qualifications. Analysis of MFA requirements, backup controls, EOL software management, and EDR/MDR deployment across carrier applications. See citations [^27], [^30], [^31], [^32], [^33], [^34] for individual carrier application forms.

[^2]: Coalition Insurance. (2025). Cyber Threat Index 2025. Coalition Inc. Retrieved from https://www.coalitioninc.com/announcements/cyber-threat-index-2025 (Full report available at: https://cdn.intelligencebank.com/us/share/NMXD/aP6w/g1kpl/original/Coalition_Cyber-Threat-Index_2025_Final)

[^2a]: Microsoft Corporation. (2025). Microsoft Digital Defense Report 2025. Microsoft Security. Multi-factor authentication effectiveness statistics based on analysis of 650+ million identities and 78 trillion daily security signals. Retrieved from https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Microsoft-Digital-Defense-Report-2025.pdf

[^2b]: IBM Security & Ponemon Institute. (2024). Cost of a Data Breach Report 2024. IBM Corporation. Analysis of 604 organizations across 17 countries and regions, examining breach costs, detection times, and recovery expenses. Retrieved from https://www.ibm.com/reports/data-breach

[^2c]: Sophos. (2024). The State of Ransomware in Education 2024. Sophos Ltd. Analysis of ransomware incidents and ransom payments across education sector, finding lower education organizations face median ransom payments of $6.6 million—among the highest of any industry sector. Retrieved from https://www.sophos.com/en-us/labs/security-threat-reports/ransomware-reports

[^2d]: Rubrik Zero Labs. (2024). State of Data Security 2024. Rubrik Inc. Analysis of ransomware attack patterns, backup targeting, and recovery success rates based on survey of 1,600+ IT leaders and incident response data. Retrieved from https://www.rubrik.com/content/rubrik/en/resources/documents/reports/state-of-data-security

[^2e]: Rubrik Zero Labs. (2023). The Hard Truths of Data Security. Rubrik Inc. Analysis finding only 16% of organizations recovered all data via attacker decryption tools after paying ransomware demands. Retrieved from https://www.rubrik.com/company/newsroom/press-releases/23/rubrik-zero-labs-hard-truths-of-data-security

[^4]: Black, P., & Wiliam, D. (1998). Assessment and classroom learning. Assessment in Education: Principles, Policy & Practice, 5(1), 7-74. https://doi.org/10.1080/0969595980050102

[^8]: Department of Defense. (2021). Cybersecurity Maturity Model Certification (CMMC) 2.0: Model Overview. DoD CIO. Retrieved from https://dodcio.defense.gov/CMMC/ and https://dodcio.defense.gov/Portals/0/Documents/CMMC/ModelOverview_V2.0_FINAL2_20211202_508.pdf

[^9]: Aon plc. (2024). Global Cyber Market Update 2024 and Cyber Insurance Market Analysis. Aon Risk Solutions. Analysis of carrier application requirements and underwriting practices based on market observations. Retrieved from https://www.aon.com/cyber-risk-report

[^11]: Coalition Inc. (2024). "Why MDR is the Next MFA for Cyber Insurance." Coalition Blog. January 23, 2024. Retrieved from https://www.coalitioninc.com/blog/cyber-insurance/why-mdr-is-the-next-mfa (Additional resource: At-Bay. (2025). "MDR vs. MXDR vs. EDR vs. XDR: What's the Difference?" At-Bay Articles, August 27, 2025. https://www.at-bay.com/articles/mdr-edr-xdr/)

[^12]: Coalition Inc. (2024). "5 Essential Cyber Insurance Requirements." Coalition Topics. Retrieved from https://www.coalitioninc.com/topics/5-essential-cyber-insurance-requirements (Additional resource: MoneyGeek. (2025). "Cyber Insurance Requirements (2025 Guide)." October 18, 2025. https://www.moneygeek.com/insurance/business/cyber-insurance/requirements/)

[^13]: Coalition Inc. (2024). "Introducing Cyber Health Rating." Coalition Blog. December 15, 2024. Retrieved from https://www.coalitioninc.com/blog/cyber-insurance/introducing-cyber-health-rating (Note: Public blog post shows 0-100 health rating screenshot, though detailed scoring methodology is not publicly accessible. General approach aligns with weighted risk assessment practices.)

[^14]: Beazley Security. (2025). "Beazley Security Targets Risk Reduction Through Broad Availability of Security Posture Reports." October 26, 2025. Retrieved from https://beazley.security/news/beazley-security-targets-risk-reduction-through-broad-availability-of-security-posture-reports

[^15]: Kahneman, D., & Tversky, A. (1979). Prospect Theory: An Analysis of Decision under Risk. Econometrica, 47(2), 263-291. https://doi.org/10.2307/1914185

[^16]: American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). Standards for Educational and Psychological Testing. AERA. https://www.apa.org/science/programs/testing/standards

[^18]: Marsh McLennan. (2023). Cybersecurity Controls Research: Direct Link Between Security Practices and Cyber Risk Outcomes. Retrieved from https://www.marshmclennan.com/news-events/2023/april/groundbreaking-research-from-marsh-mclennan-reveals-direct-link-.html?bsrc=mmc#:~:text=Marsh%20McLennan

[^19]: Verizon. (2024). Data Breach Investigations Report (DBIR) 2024. Verizon Enterprise Solutions. Retrieved from https://www.verizon.com/business/resources/reports/dbir/ (Full report PDF: https://www.verizon.com/business/resources/reports/2024-dbir-data-breach-investigations-report.pdf)

[^20]: IBM Security. (2024). X-Force Threat Intelligence Index 2024. IBM Corporation. Retrieved from https://www.ibm.com/reports/threat-intelligence (Report details: https://securityintelligence.com/x-force/2024-x-force-threat-intelligence-index/)

[^21]: National Institute of Standards and Technology. (2024). NIST Cybersecurity Framework (CSF) 2.0. U.S. Department of Commerce. https://doi.org/10.6028/NIST.CSWP.29 and https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf

[^22]: Center for Internet Security. (2023). CIS Critical Security Controls (CSC) v8.1. CIS. Retrieved from https://www.cisecurity.org/controls/v8

[^23]: Cybersecurity and Infrastructure Security Agency (CISA). (2023). Cybersecurity Performance Goals (CPGs). CISA. Retrieved from https://www.cisa.gov/cross-sector-cybersecurity-performance-goals

[^24]: The Trust. (2024). Cyber Qualifications for Coverage. Retrieved from https://www.svc.the-trust.org/PublicFiles/CyberQualificationsForCoverage.pdf

[^25]: Meyer, L.A., Romero, S., Bertoli, G., Burt, T., Weinert, A., & Lavista Ferres, J.M. (2023). How Effective is Multifactor Authentication at Deterring Cyberattacks? Microsoft Research. Retrieved from https://www.microsoft.com/en-us/research/publication/how-effective-is-multifactor-authentication-at-deterring-cyberattacks/

[^27]: Chubb. (2024). Cyber ERM Standard Proposal Form. Retrieved from https://www.chubb.com/content/dam/chubb-sites/chubb-com/au-en/business/cyber-insurance/documents/pdf/cyber-erm-standard-proposal-form.pdf

[^30]: Travelers Insurance. (2025). Cyber Insurance Application (Agency Form). Retrieved from https://asset.trvstatic.com/download/assets/cyb-14306.pdf/b75b6ef263c911eebdf746949fd95a9b

[^31]: Massachusetts Insurance Agents. (2025). Cyber Application Agency Form. Retrieved from https://massagent.com/wp-content/uploads/2025/01/Cyber_Application_Agency.pdf

[^32]: AIG Australia. (2024). CyberEdge Ransomware Supplementary Proposal Form. Retrieved from https://www.aig.com.au/content/dam/aig/apac/australia/documents-new/financial-lines/cyber/aig-au-cyberedge-ransomware-supplementary-proposal-form.pdf.coredownload.pdf

[^33]: Chubb Ireland. (2024). Cyber ERM Short Proposal Form. Retrieved from https://www.chubb.com/content/dam/chubb-sites/chubb-com/ie-en/business/by-category-cyber/10985a-chubb_cyber_erm_short_proposal_form_ie.pdf

[^34]: Beazley. (2024). Cyber Insurance Application (Below $250M). Retrieved from https://www.beazley.com/globalassets/product-documents/application/beazley_cyber_insurance_application_below_250m.pdf


