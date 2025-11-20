# CyberPools Risk Assessment Grading Model Options
## Strategic Analysis Based on Current Deployed Model

**Document Date:** October 30, 2025
**Current State:** Single-score model with 51 questions, 9 categories, 7 "Cyber Requirements" (from The Trust pool)
**Purpose:** Evaluate options for enhancing the grading methodology

---

## Important: Understanding "Cyber Requirements"

**The Trust Pool Integration:**
- The Trust pool created **7 simplified requirements** (e.g., "Does the organization use MFA?")
- CyberPools mapped **12 questions** from your 51-question assessment to these 7 requirements
- Each Trust requirement may be satisfied by multiple CyberPools questions
- This allows CyberPools detailed assessment to answer The Trust's simplified compliance questions
- Reports show: "9/12 questions met" → determines yes/no compliance for each of the 7 requirements

---

## Current Model Analysis (Deployed)

### What You Have Today

**Overall Scoring:**
```
Overall Score = Σ(Points Earned) / Σ(Max Possible Points) × 100
Where: Risk Score per question = Control Rating (1/3/5) × Impact (1/3/5)
```

**Current Scores Example (Santa Catalina):**
- Overall: 80%
- Inventory & Assets: 89%
- Account Management: 88%
- Data Protection: 72%
- Secure Configuration: 81%
- Malware Defense: 75%
- Data Recovery: 86%
- Security Awareness: 100%
- Vendor Management: 100%
- **Incident Response: 8%** ⚠️

**Cyber Requirements Compliance:**
- 7 requirements from The Trust pool (simplified questions like "Does the organization use MFA?")
- 12 questions from your 51-question assessment map to these 7 requirements
- Simple Yes/No compliance table per requirement
- Santa Catalina: 9/12 questions met → Determines compliance for each of the 7 requirements

### Strengths of Current Model

1. ✅ **Simple to understand** - One number, clear meaning
2. ✅ **Category visibility** - Members can see which areas need work
3. ✅ **Risk-based** - Control × Impact gives weighted importance
4. ✅ **Cyber Requirements table** - Highlights critical controls
5. ✅ **Proven delivery** - Working system with good completion rates

### Weaknesses of Current Model

1. ⚠️ **All categories weighted equally** - Incident Response (6 questions) = Data Protection (3 questions)
2. ⚠️ **No foundation emphasis** - 7 Cyber Requirements (12 questions) shown separately but don't drive overall score
3. ⚠️ **Category imbalance** - Secure Configuration (13Q) has 4× weight of Data Protection (3Q)
4. ⚠️ **Insurance disconnect** - 7 Cyber Requirements are insurance-critical but buried in report
5. ⚠️ **Score inflation** - Organization can score 80% overall while failing critical controls (EDR, vuln scans)

---

## Option 1: Keep Current Model + Minor Enhancements

### What Changes
- **Add more questions** to thin categories (Data Protection, Incident Response, Security Monitoring)
- **Weighted category scoring** - Critical categories (Data Protection, Incident Response) count more
- **Foundation threshold** - Require minimum Cyber Requirements compliance (e.g., 10/12 questions met = 6+/7 requirements) for certain grade levels

### Example Enhanced Scoring

```
Overall Score = Weighted Average of Categories

Category Weights:
- Data Protection: 20% (critical for insurance)
- Incident Response: 15% (critical for insurance)
- Account Management: 15% (MFA emphasis)
- Malware Defense: 15% (EDR emphasis)
- Data Recovery: 15% (backup/recovery critical)
- Secure Configuration: 10%
- Inventory & Assets: 5%
- Security Awareness: 5%
- Vendor Management: 5%
Total: 100%
```

**Impact on Santa Catalina:**
- Current: 80% overall
- Weighted: ~69% (Incident Response 8% tanks the score with 15% weight)
- **Result: More accurate risk representation**

### Foundation Threshold Enhancement

**Add requirement to report:**
> To achieve an "A" grade (90%+), organizations must meet 11/12 Cyber Requirements questions (all 7 requirements).
> To achieve a "B" grade (80%+), organizations must meet 10/12 Cyber Requirements questions (6+/7 requirements).

**Santa Catalina Impact:**
- Overall Score: 80% (current B grade)
- Cyber Requirements Questions: 9/12 met (75%)
- **New Grade: C** (fails foundation threshold despite 80% overall)

### Pros
- ✅ Minimal disruption to current system
- ✅ Easy to implement (scoring formula changes only)
- ✅ Maintains compatibility with existing reports
- ✅ Emphasizes critical controls without complex model

### Cons
- ❌ Still a single score (less granular)
- ❌ Foundation requirements feel like "gotcha" to members
- ❌ Doesn't clearly communicate "foundation vs. maturity"

---

## Option 2: Dual-Score Model (Foundation + Comprehensive)

### What Changes
- **Add a second score** specifically for the 7 Cyber Requirements (12 questions)
- **Report both scores prominently** on summary page
- **Use Foundation score for insurance/compliance decisions**
- **Use Comprehensive score for maturity tracking**

### Example Report Display

```
╔══════════════════════════════════════════════════════════╗
║  FOUNDATION CONTROLS                              75%  C  ║
║  (7 Trust requirements: 12 questions, 9/12 met)          ║
╠══════════════════════════════════════════════════════════╣
║  COMPREHENSIVE MATURITY                           80%  B  ║
║  (All 51 controls across 9 categories)                    ║
╚══════════════════════════════════════════════════════════╝
```

### Scoring Formulas

**Foundation Score (12 Questions mapping to 7 Trust Requirements):**
```
Foundation Score = Σ(12 Cyber Requirement Question Points) / Σ(Max Points) × 100
Note: 12 questions from 51-question assessment map to 7 simplified Trust requirements
```

**Comprehensive Score (51 Questions):**
```
Comprehensive Score = Σ(All Points) / Σ(Max Points) × 100
(Unchanged from current model)
```

### Santa Catalina Impact

| Metric | Current Model | Dual-Score Model |
|--------|---------------|------------------|
| Overall Score | 80% | — |
| **Foundation Score** | (not shown) | **75%** (9/12 questions) |
| **Comprehensive Score** | (same as overall) | **80%** (unchanged) |
| **Grade** | B | **Foundation: C, Comprehensive: B** |

### Pros
- ✅ **Clear separation** between "must-haves" and "nice-to-haves"
- ✅ **Insurance alignment** - Foundation score directly maps to underwriting
- ✅ **Maturity tracking** - Comprehensive score shows progress over time
- ✅ **No question changes** - Uses existing 51 questions, just reports differently
- ✅ **Member motivation** - Two scores create clear priorities

### Cons
- ❌ More complex communication (two scores to explain)
- ❌ May create confusion (which score matters?)
- ❌ Foundation score could be harsh (75% = C grade feels bad)
- ❌ Requires report template changes

---

## Option 3: Weighted Dual-Score Model (80/20 Concept)

### What Changes
- **Foundation Score** from 7 Cyber Requirements (12 questions)
- **Comprehensive Score** from all 51 questions
- **Overall Score** = (80% × Foundation) + (20% × Comprehensive)

### Scoring Formula

```
Foundation Score = Score on 12 questions (mapping to 7 Trust requirements)
Comprehensive Score = Score on all 51 questions
Overall Score = (0.80 × Foundation) + (0.20 × Comprehensive)
```

### Santa Catalina Example

```
Foundation: 75% (9/12 questions met)
Comprehensive: 80% (current overall)
Overall = (0.80 × 75%) + (0.20 × 80%) = 60% + 16% = 76%
```

**Result:** 76% overall (C grade) instead of 80% (B grade)

### Mathematical Properties

**Key Insight:** Foundation score dominates:
- 10% improvement in Foundation → 8% improvement in Overall
- 10% improvement in Comprehensive → 2% improvement in Overall
- **Foundation has 4× leverage** over comprehensive

**Maximum Score with Weak Foundation:**
- If Foundation = 50%, maximum Overall = 60% (even with 100% Comprehensive)
- Organizations **cannot achieve passing grades** without strong foundation
- Creates **strong incentive** to prioritize critical controls

### Pros
- ✅ **Mathematically emphasizes foundation** - Can't fake it with comprehensive efforts
- ✅ **Single overall score** - Easier to communicate than dual scores
- ✅ **Insurance-aligned** - Foundation controls directly impact overall grade
- ✅ **Fair to high performers** - Organizations with strong foundation + good comprehensive get rewarded
- ✅ **Penalizes weak foundation** - Organizations with gaps can't compensate with volume

### Cons
- ❌ Most complex to explain
- ❌ Can feel "unfair" to organizations improving comprehensive but not foundation
- ❌ Foundation score becomes make-or-break for overall grade
- ❌ May demotivate organizations that fail to see progress

---

## Option 4: Threshold-Based Grading Model

### What Changes
- **Keep single overall score** (current 80% model)
- **Add grade thresholds** that require foundation compliance
- **Grade letter depends on BOTH overall score AND foundation compliance**

### Grading Matrix

| Overall Score | Foundation Compliance (Questions Met) | Final Grade |
|---------------|--------------------------------------|-------------|
| 90-100% | 11-12/12 (all 7 requirements) | **A** |
| 90-100% | 10/12 or below | **B** (capped) |
| 80-89% | 10-12/12 (6-7/7 requirements) | **B** |
| 80-89% | 9/12 or below | **C** (capped) |
| 70-79% | 9-12/12 (5-7/7 requirements) | **C** |
| 70-79% | 8/12 or below | **D** (capped) |
| 60-69% | — | **D** |
| <60% | — | **F** |

### Santa Catalina Example

```
Overall Score: 80%
Foundation Questions: 9/12 met (75%)

Without thresholds: B grade
With thresholds: C grade (capped due to foundation < 10/12 questions)
```

### Pros
- ✅ **Simple to understand** - "You need foundation compliance to get top grades"
- ✅ **Preserves current model** - Minimal technical changes
- ✅ **Clear requirements** - Members know exactly what foundation controls are needed
- ✅ **Insurance-aligned** - Foundation threshold directly supports underwriting decisions

### Cons
- ❌ Feels like "gotcha" grading
- ❌ Organizations may perceive as unfair (80% should be B, not C)
- ❌ Single missed foundation control can drop grade significantly

---

## Comparison Matrix: All Options

| Criteria | Current | Option 1: Weighted Categories | Option 2: Dual Score | Option 3: 80/20 Weighted | Option 4: Threshold |
|----------|---------|-------------------------------|----------------------|-------------------------|---------------------|
| **Complexity** | Low | Low | Medium | High | Low |
| **Foundation Emphasis** | None | Moderate | High | Very High | High |
| **Insurance Alignment** | Moderate | Good | Excellent | Excellent | Excellent |
| **Member Understanding** | Easy | Easy | Moderate | Hard | Easy |
| **Implementation Effort** | 0 hours | 8-12 hours | 20-30 hours | 30-40 hours | 16-24 hours |
| **Report Changes Required** | None | Minimal | Significant | Significant | Moderate |
| **Fairness Perception** | Good | Good | Good | Moderate | Poor (feels like gotcha) |
| **Differentiation** | Low | Moderate | High | High | Moderate |
| **Santa Catalina Impact** | 80% (B) | ~69% (D) | 75% Foundation (C), 80% Comprehensive (B) | 76% (C) | 80% but capped to C |

---

## Recommendations

### **For Immediate Implementation (Next 3 Months)**

**Recommendation: Option 1 (Weighted Categories) + Enhanced Compliance Table**

**Why:**
1. Minimal disruption to current system
2. Easy to implement (scoring formula changes only)
3. Addresses category imbalance problem (Incident Response 8% hurts more)
4. Keeps single overall score (easy communication)
5. Foundation requirements still highlighted in Cyber Requirements table

**Implementation:**
```python
# Weighted category scoring
category_weights = {
    "Data Protection": 0.20,
    "Incident Response Management": 0.15,
    "Account Management": 0.15,
    "Malware Defense": 0.15,
    "Data Recovery": 0.15,
    "Secure Configuration of Enterprise Assets": 0.10,
    "Inventory and Control of Assets": 0.05,
    "Security Awareness": 0.05,
    "Vendor Management": 0.05
}

overall_score = sum(category_score * weight for category, weight in category_weights.items())
```

**Enhanced Cyber Requirements Table:**
Add summary at bottom:
```
╔══════════════════════════════════════════════════════════╗
║  CYBER REQUIREMENTS COMPLIANCE: 9/12 questions met       ║
║  (7 Trust requirements: 75% compliance)                  ║
║  Insurance Recommendation: Remediate 3 gaps              ║
╚══════════════════════════════════════════════════════════╝
```

**Expected Impact:**
- Santa Catalina: 80% → 69% (more accurate reflection of Incident Response gap)
- Members see weighted importance of categories
- Foundation gaps still clearly highlighted
- Insurance decisions can reference Cyber Requirements compliance percentage

---

### **For Medium-Term (6-12 Months)**

**Recommendation: Option 2 (Dual-Score Model)**

**Why:**
1. After members adapt to weighted categories, introduce dual scoring
2. Provides clearest differentiation between foundation and maturity
3. Aligns perfectly with insurance underwriting (Foundation) vs. maturity tracking (Comprehensive)
4. Members get two clear goals: "Fix foundation first, then improve maturity"

**Implementation Sequence:**
1. **Month 0-3:** Deploy weighted categories (Option 1)
2. **Month 4-6:** Add Foundation Score to reports (show both)
3. **Month 7-9:** Pilot dual-score grading with 10-15 members
4. **Month 10-12:** Full rollout with dual-score report format

**Transition Report Display:**
```
╔═══════════════════════════════════════════════════════════╗
║  FOUNDATION CONTROLS (Critical Insurance Requirements)    ║
║  Score: 75% (9/12 questions, 7 Trust requirements)       ║
║  Grade: C                                                 ║
╠═══════════════════════════════════════════════════════════╣
║  COMPREHENSIVE MATURITY (All Security Controls)           ║
║  Score: 80% (Strong across 9 categories)                 ║
║  Grade: B                                                 ║
╠═══════════════════════════════════════════════════════════╣
║  OVERALL WEIGHTED SCORE: 76%                     Grade: C  ║
║  (Foundation: 75% × 70%) + (Comprehensive: 80% × 30%)     ║
╚═══════════════════════════════════════════════════════════╝

Interpretation:
Your foundation controls (critical for cyber insurance) need immediate
attention. Focus on the 3 missing questions (EDR, vulnerability scans,
backup testing) to improve your foundation score to 85%+. Your
comprehensive maturity is good, showing strong practices across most areas.
```

---

### **NOT Recommended**

**Option 3 (80/20 Weighted Model):**
- Too aggressive (Santa Catalina drops from 80% to 76%)
- Creates confusion with single score that's actually a weighted blend
- Mathematical complexity reduces member trust
- Better to show two separate scores (Option 2) than blend them

**Option 4 (Threshold-Based):**
- Feels punitive ("gotcha" grading)
- Hard to explain why 80% becomes C
- May demotivate members who see score but different grade
- Thresholds are arbitrary and feel unfair

---

## Next Steps for Your Team

### **Decision Matrix Questions**

Ask yourselves:

1. **How much change can members handle?**
   - Low tolerance → Option 1 (weighted categories)
   - High tolerance → Option 2 (dual score)

2. **What's your primary goal?**
   - Better accuracy → Option 1 (weighted categories)
   - Insurance alignment → Option 2 (dual score)
   - Simplicity → Stay with current + add more questions

3. **How important is foundation emphasis?**
   - Critical → Option 2 or Option 3
   - Important but not dominant → Option 1
   - Current model is fine → Just add questions

4. **Timeline pressure?**
   - Need changes in 3 months → Option 1
   - Can wait 6-12 months → Option 2
   - Can wait 12-24 months → Option 3

### **Immediate Actions (This Week)**

1. **Review Santa Catalina report as a team**
   - Does 80% overall feel accurate given 8% Incident Response?
   - Does 9/12 questions met (mapping to 7 Trust requirements) feel accurate?
   - Should Incident Response matter more than Vendor Management?

2. **Decide on category weighting**
   - Do you want weighted categories (Option 1)?
   - If yes, what weights feel right?
   - Test on 3-5 existing assessments to see impact

3. **Test scoring models**
   - Run Santa Catalina through all 4 options
   - Show results to insurance pool administrators
   - Get feedback on which model makes most sense for underwriting

4. **Plan question expansion**
   - Regardless of scoring model, you need more questions:
     - Data Protection: 3 → 7 questions (add 4)
     - Security Monitoring: 0 → 4 questions (new category)
     - Incident Response: 6 → 8 questions (add 2)
   - Total: 51 → 62 questions

---

## Appendix: Question Expansion Recommendations

### Priority 1: Data Protection (Add 4 Questions)

**3.4 - Data Classification**
- Current gap: No question about data sensitivity levels
- Insurance impact: High (need to know what data requires protection)
- Impact Rating: 5 (High)

**3.5 - Data Retention & Disposal (FERPA)**
- Current gap: FERPA compliance violation
- Insurance impact: High (regulatory fines)
- Impact Rating: 5 (High)

**3.6 - Encryption in Transit**
- Current gap: Only encryption at rest covered (3.3)
- Insurance impact: High (data in transit equally vulnerable)
- Impact Rating: 5 (High)

**3.7 - Least Privilege Access to Data**
- Current gap: No question about data access controls
- Insurance impact: Moderate (insider threat mitigation)
- Impact Rating: 3 (Moderate)

### Priority 2: Security Monitoring (Add 4 Questions, New Category)

**10.1 - Centralized Logging**
- Current gap: 0% NIST CSF Detection coverage
- Insurance impact: High (can't detect breaches without logs)
- Impact Rating: 5 (High)

**10.2 - Log Retention**
- Current gap: No compliance with 90-day retention standards
- Insurance impact: Moderate (forensic investigation capability)
- Impact Rating: 3 (Moderate)

**10.3 - Log Review & Monitoring**
- Current gap: No detection capability questions
- Insurance impact: High (dwell time reduction)
- Impact Rating: 5 (High)

**10.4 - Security Alerting**
- Current gap: No real-time threat detection questions
- Insurance impact: High (rapid response capability)
- Impact Rating: 5 (High)

### Priority 3: Incident Response (Add 2 Questions)

**9.7 - Designated Incident Response Team**
- Current gap: No question about team composition
- Insurance impact: Moderate (response coordination)
- Impact Rating: 3 (Moderate)

**9.8 - Incident Response Metrics & Improvement**
- Current gap: No continuous improvement questions
- Insurance impact: Low (maturity indicator)
- Impact Rating: 1 (Low)

**Total Expansion: 51 → 61 questions**

---

**END OF DOCUMENT**
