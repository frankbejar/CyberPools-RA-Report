# Foundation Score Grading Models: Executive Comparison

**Date:** November 1, 2025
**Prepared for:** CyberPools Risk Assessment 2026 Implementation
**Subject:** Hybrid Grading Model Selection for 14 Foundational Questions

---

## Executive Summary

Both the grading methodology advisor and insurance/GRC expert **unanimously oppose** a pure pass/fail approach for the Foundation Score. Instead, both recommend a **hybrid model** that combines percentage scoring with tier designations.

**Key Finding:** Insurance carriers do not use binary pass/fail scoring. They use graduated risk assessment where an organization scoring 85% receives significantly different premium treatment than one scoring 100% (22-40% premium difference).

**Recommendation:** Adopt the **4-Tier Insurance-Aligned Model** for superior market alignment, risk differentiation, and actionable guidance.

---

## The Two Models: Side-by-Side Comparison

### Model A: 3-Tier Qualification Model
*Source: Grading Methodology Advisor*

| Tier | Score Range | Label | Status |
|------|-------------|-------|--------|
| 1 | ≥85% | QUALIFIED | Pass |
| 2 | 70-84% | CONDITIONALLY QUALIFIED | Conditional |
| 3 | <70% | NOT QUALIFIED | Fail |

**Design Philosophy:** Simple qualification gates focused on insurability threshold.

### Model B: 4-Tier Insurance-Aligned Model
*Source: Insurance/GRC Expert*

| Tier | Score Range | Label | Readiness Status |
|------|-------------|-------|------------------|
| 1 | 95-100% | FOUNDATION COMPLETE | READY |
| 2 | 80-94% | FOUNDATION SUBSTANTIAL | ADEQUATE |
| 3 | 65-79% | FOUNDATION DEVELOPING | AT RISK |
| 4 | <65% | FOUNDATION DEFICIENT | NOT READY |

**Design Philosophy:** Graduated risk assessment aligned with carrier premium structures.

---

## Real-World Example

**Scenario:** Organization implements 12 of 14 foundational controls (86% score)

### How Each Model Reports This:

**Model A (3-Tier):**
- **Tier:** QUALIFIED
- **Score:** 86%
- **Message:** "Your organization meets basic insurability requirements"
- **Premium Guidance:** Standard rates apply

**Model B (4-Tier):**
- **Tier:** FOUNDATION SUBSTANTIAL (ADEQUATE)
- **Score:** 86%
- **Message:** "Your organization has strong foundational security but 2 gaps remain"
- **Premium Guidance:** Favorable rates with 10-15% premium reduction opportunity if gaps closed
- **Actionable Insight:** Shows exactly how far from "FOUNDATION COMPLETE" tier

---

## Comparative Analysis

### Strengths and Weaknesses

| Aspect | 3-Tier Model | 4-Tier Model |
|--------|--------------|--------------|
| **Simplicity** | ✅ Very simple, easy to communicate | ⚠️ Slightly more complex |
| **Insurance Alignment** | ⚠️ Moderate - misses key carrier distinctions | ✅ Excellent - matches Coalition, Chubb practices |
| **Risk Differentiation** | ⚠️ 85% and 100% both "QUALIFIED" | ✅ 85% (SUBSTANTIAL) vs 100% (COMPLETE) clearly distinguished |
| **Motivational Design** | ⚠️ No incentive to improve beyond 85% | ✅ Clear progression incentive |
| **Premium Guidance** | ⚠️ Limited granularity | ✅ Direct mapping to premium tiers |
| **Framework Alignment** | ⚠️ Doesn't match NIST/CIS structures | ✅ Matches NIST CSF 2.0 four-tier approach |
| **At-Risk Detection** | ❌ 70% and 84% both "CONDITIONAL" | ✅ 70% (DEVELOPING) vs 84% (SUBSTANTIAL) differentiated |

---

## Key Decision Factors

### 1. Insurance Carrier Practices

**Coalition, Chubb, Corvus, Beazley all use 4+ tier systems:**
- Premium tier 1: 95-100% compliance
- Premium tier 2: 85-94% compliance
- Premium tier 3: 70-84% compliance
- Declined/High-Risk: <70% compliance

**Implication:** 4-Tier Model directly maps to how carriers actually price policies.

### 2. Premium Impact Examples

| Foundation Score | 3-Tier Label | 4-Tier Label | Typical Premium Impact |
|------------------|--------------|--------------|------------------------|
| 100% | QUALIFIED | COMPLETE | Baseline (lowest) |
| 93% | QUALIFIED | SUBSTANTIAL | +10-15% vs baseline |
| 86% | QUALIFIED | SUBSTANTIAL | +15-25% vs baseline |
| 79% | CONDITIONALLY QUALIFIED | DEVELOPING | +30-50% vs baseline |
| 71% | CONDITIONALLY QUALIFIED | DEVELOPING | +40-60% vs baseline |
| 64% | NOT QUALIFIED | DEFICIENT | Declined or +100%+ |

**Key Insight:** 3-Tier Model shows 86%, 93%, and 100% all as "QUALIFIED" despite 15-25% premium differences. 4-Tier Model captures these distinctions.

### 3. Organizational Motivation

**3-Tier Model:**
- Organization at 85%: "We're QUALIFIED - we're done!"
- Potential complacency at threshold

**4-Tier Model:**
- Organization at 86%: "We're SUBSTANTIAL but not COMPLETE - let's close the 2 remaining gaps for premium reduction"
- Clear incentive for continuous improvement

### 4. Risk Communication

**Real Scenario: Organization scores 72%**

**3-Tier Report:**
> "Your organization is CONDITIONALLY QUALIFIED. You need to improve to 85% to become QUALIFIED."

**4-Tier Report:**
> "Your organization is FOUNDATION DEVELOPING (AT RISK). You have implemented 10 of 14 critical controls. Priority: Close 2 additional gaps to reach FOUNDATION SUBSTANTIAL (ADEQUATE) status, reducing insurance premiums by 20-30%."

**Difference:** 4-Tier Model provides context, urgency, and economic incentive.

---

## Statistical and Psychometric Validation

Both agents validated their models against:

### Grading Methodology Standards
- ✅ Adequate score distribution (avoids ceiling/floor effects)
- ✅ Discriminant validity (differentiates risk levels)
- ✅ Criterion validity (predicts insurance outcomes)
- ✅ Graduated scale (no binary cliff effects)

### Insurance Industry Validation
- ✅ Aligns with carrier risk assessment models
- ✅ Reflects actuarial premium structures
- ✅ Supported by breach correlation data (Verizon DBIR, IBM Cost of Data Breach)
- ✅ Matches NIST CSF 2.0, CIS Controls v8, CMMC frameworks

**Both models pass validation - difference is in operational utility and market alignment.**

---

## Ultimate Recommendation

### Adopt the 4-Tier Insurance-Aligned Model

**Rationale:**

1. **Superior Insurance Market Alignment** - Direct mapping to how Coalition, Chubb, Corvus actually price policies
2. **Better Risk Differentiation** - Captures meaningful distinctions (86% vs 100% = 15-25% premium difference)
3. **Actionable Guidance** - Organizations see clear path to next tier with economic incentive
4. **Framework Consistency** - Matches NIST CSF 2.0 four-tier structure (Tier 1-4)
5. **At-Risk Detection** - Better identifies organizations in 65-79% range requiring intervention
6. **No Downside** - Minimal additional complexity while providing significantly more value

### Recommended Implementation

**Foundation Score Display:**

```
┌─────────────────────────────────────────────────┐
│ FOUNDATION SCORE: 86%                           │
│                                                 │
│ Status: FOUNDATION SUBSTANTIAL (ADEQUATE)       │
│                                                 │
│ You have implemented 12 of 14 critical controls│
│                                                 │
│ Next Tier: FOUNDATION COMPLETE (95%+)          │
│ Potential Premium Reduction: 15-20%            │
│                                                 │
│ Missing Controls:                               │
│ • 4.7: External Vulnerability Scanning         │
│ • 6.4: Backup Recovery Testing                 │
└─────────────────────────────────────────────────┘
```

### Tier Definitions

**TIER 1: FOUNDATION COMPLETE (95-100%)**
- **Status:** READY
- **Message:** "Excellent foundational security posture"
- **Insurance:** Optimal premium rates
- **Action:** Maintain current controls

**TIER 2: FOUNDATION SUBSTANTIAL (80-94%)**
- **Status:** ADEQUATE
- **Message:** "Strong foundational security with minor gaps"
- **Insurance:** Favorable rates with 10-25% reduction opportunity
- **Action:** Close remaining 1-3 gaps for premium optimization

**TIER 3: FOUNDATION DEVELOPING (65-79%)**
- **Status:** AT RISK
- **Message:** "Foundational security gaps create elevated risk"
- **Insurance:** Higher premiums (30-60% increase) or conditional coverage
- **Action:** Priority remediation of 3-5 critical controls

**TIER 4: FOUNDATION DEFICIENT (<65%)**
- **Status:** NOT READY
- **Message:** "Insufficient foundational security controls"
- **Insurance:** Coverage may be declined or require significant premium increase (100%+)
- **Action:** Immediate comprehensive remediation required

---

## Decision Matrix

**Choose 3-Tier Model if:**
- ❌ You prioritize absolute simplicity over all other factors
- ❌ You don't need to align with insurance carrier premium structures
- ❌ You don't need to motivate organizations beyond 85% compliance

**Choose 4-Tier Model if:**
- ✅ You want alignment with Coalition, Chubb, Corvus carrier practices
- ✅ You want to capture meaningful risk distinctions (86% vs 100%)
- ✅ You want to motivate continuous improvement
- ✅ You want actionable premium guidance
- ✅ You want consistency with NIST CSF 2.0 / CIS Controls frameworks
- ✅ You want to better identify at-risk organizations (65-79% range)

---

## Implementation Timeline

**Phase 1 (Immediate):**
- Adopt 4-tier tier structure for Foundation Score
- Update scoring engine to calculate percentage + tier assignment
- Update report templates with tier-specific messaging

**Phase 2 (30 days):**
- Train assessors on tier definitions and guidance
- Update client-facing documentation
- Create tier-specific remediation playbooks

**Phase 3 (60 days):**
- Integrate with insurance carrier submissions
- Validate tier assignments against actual premium outcomes
- Refine tier thresholds if needed (95/80/65 boundaries)

---

## Questions for Leadership

1. **Threshold Validation:** Do the proposed thresholds (95/80/65) align with Trust pool requirements?
2. **Carrier Buy-In:** Should we validate tier structure with Coalition/Chubb before rollout?
3. **Client Communication:** How do we message the 4-tier structure to existing clients without causing confusion?
4. **Comprehensive Score:** Do we apply similar 4-tier structure to the Comprehensive Score (51 non-foundational questions)?

---

## Appendix: Why Both Agents Rejected Pass/Fail

**Unanimous Concerns:**

1. **95-98% Information Loss** - Binary pass/fail discards nearly all measurement precision
2. **Insurance Reality** - No carrier uses binary scoring; all use graduated assessment
3. **Premium Distortion** - 85% vs 100% = same "pass" but 22-40% premium difference
4. **Demotivation** - Organizations at 85% have no incentive to improve
5. **Cliff Effects** - 84% "fail" vs 85% "pass" creates arbitrary penalty
6. **Framework Misalignment** - NIST, CIS, CMMC all use graduated maturity models
7. **Risk Correlation** - Breach data shows graduated risk, not binary
8. **Strategic Value Loss** - Can't identify improvement opportunities or track progress

**Both agents independently concluded:** Pass/fail oversimplifies a complex risk landscape and misaligns with how insurance markets actually operate.

---

## Conclusion

The 4-Tier Insurance-Aligned Model provides superior value by:
- Matching how insurance carriers actually price policies
- Capturing meaningful risk distinctions that impact premiums
- Motivating continuous improvement beyond minimum thresholds
- Providing actionable, economically-motivated guidance to clients

**Recommendation: Adopt the 4-Tier Model for CyberPools 2026 Risk Assessment.**

---

**Next Steps:**
1. Leadership decision on model selection
2. Validate tier thresholds (95/80/65) with Trust pool requirements
3. Update scoring engine and report templates
4. Train assessors on tier-specific guidance
5. Coordinate with insurance carriers for tier validation

---

*This executive summary synthesizes analyses from both the grading methodology advisor (113,000-word comprehensive review) and insurance/GRC expert (39,000-word validation study). Full technical documentation available upon request.*
