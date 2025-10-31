# CyberPools Risk Assessment Grading Model Approaches
## Strategic Analysis and Implementation Guide

**Document Version:** 1.0
**Date:** October 30, 2025
**Purpose:** Comprehensive analysis of grading model approaches for the CyberPools Risk Assessment service offering
**Audience:** CyberPools leadership, risk assessment team, insurance pool administrators

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Current Two-Tier Model Analysis](#current-two-tier-model-analysis)
3. [Alternative Grading Model Approaches](#alternative-grading-model-approaches)
4. [Threshold Framework and Insurance Implications](#threshold-framework-and-insurance-implications)
5. [Next Year's Gap Analysis and Question Additions](#next-years-gap-analysis-and-question-additions)
6. [Implementation Roadmap](#implementation-roadmap)
7. [Appendices](#appendices)

---

## Executive Summary

### Current State
CyberPools' risk assessment employs a **two-tier grading model** with aggressive foundation emphasis:
- **Tier I Score:** Foundation compliance (12 questions mapping to cyber insurance requirements)
- **Tier II Score:** Comprehensive maturity = (80% × Tier I) + (20% × All 51 questions)

### Key Findings
✅ **Validated:** Mathematical model is sound and achieves intended objective of prioritizing foundation controls
✅ **Effective:** Simulation results demonstrate fair treatment of strong performers while penalizing weak foundations
✅ **Insurance-Aligned:** Foundation questions directly map to underwriting requirements

⚠️ **Critical Gaps Identified:**
- Data Protection category severely inadequate (3 questions, missing FERPA requirements)
- No security monitoring/logging questions (0% NIST CSF Detection coverage)
- Self-reported responses lack evidence validation

### Recommendations

**Immediate Actions (0-3 months):**
1. Add 4 data protection questions (bringing total from 3 to 7)
2. Elevate 3 data protection questions to Tier I foundation (12 → 15 questions)
3. Implement evidence validation for all Tier I foundation questions

**Short-Term Actions (3-6 months):**
4. Add new Security Monitoring category (4 questions)
5. Elevate 2 monitoring questions to foundation (15 → 17 questions)
6. Develop HIPAA-specific assessment variant for healthcare expansion

**Assessment Expansion:**
- Current: 51 questions, 12 foundation (Tier I)
- Year 1: 59 questions, 17 foundation (Tier I)
- Year 2: 70 questions, 20 foundation (Tier I)

---

## Current Two-Tier Model Analysis

### Model Structure

**Formula:**
```
Tier I Score = Σ(Foundation Points Earned) / Σ(Foundation Points Possible) × 100

Tier II Score = (0.80 × Tier I Score) + (0.20 × Comprehensive Score)

Where:
- Foundation = 12 core questions (cyber insurance requirements)
- Comprehensive = All 51 questions
```

**Risk Scoring Per Question:**
```
Risk Score = Control Rating (0/1/3/5) × Impact Rating (1/3/5)
Result Range: 0-25

Control Ratings:
- 0 = Not Applicable
- 1 = Fully Implemented
- 3 = Partially Implemented
- 5 = Not Implemented

Impact Ratings:
- 1 = Low
- 3 = Moderate
- 5 = High

Risk Categories:
- Low: 0-9
- Moderate: 10-15
- High: 16-25
```

### Foundation Questions (Current 12)

| ID | Question | Category | Impact | Rationale |
|----|----------|----------|--------|-----------|
| 1.4 | EOL software retirement | Inventory | 5 | Unpatched legacy systems = common breach vector |
| 2.3 | MFA for cloud resources | Account Mgmt | 5 | Cloud service compromise prevention |
| 2.4 | MFA for remote access | Account Mgmt | 5 | VPN/remote compromise prevention |
| 2.5 | MFA for admin accounts | Account Mgmt | 5 | Privileged account protection |
| 2.6 | MFA for critical systems | Account Mgmt | 5 | Business-critical system protection |
| 4.3 | Patch management | Secure Config | 5 | Vulnerability exploitation prevention |
| 4.7 | External vulnerability scans | Secure Config | 5 | Attack surface visibility |
| 5.4 | EDR implementation | Malware Defense | 5 | Ransomware detection and response |
| 6.3 | Air gap/immutable backups | Data Recovery | 5 | Ransomware recovery capability |
| 6.4 | Backup testing | Data Recovery | 5 | Recovery validation |
| 7.2 | Phishing simulation | Security Awareness | 5 | Human vulnerability testing |
| 7.3 | Follow-up security training | Security Awareness | 5 | Remediation of human risk |

### Mathematical Properties and Validation

**Boundary Behavior Analysis:**

| Scenario | Tier I | Comprehensive | Tier II | Interpretation |
|----------|--------|---------------|---------|----------------|
| Perfect foundation, weak comprehensive | 100% | 50% | 90% | High Tier II despite weak comprehensive *(INTENDED)* |
| Weak foundation, perfect comprehensive | 50% | 100% | 60% | Low Tier II despite perfect comprehensive *(INTENDED)* |
| Balanced mediocrity | 70% | 70% | 70% | Tier II equals both inputs *(EXPECTED)* |
| Strong foundation, moderate comprehensive | 90% | 70% | 86% | Tier II reflects strong foundation *(INTENDED)* |
| Critical foundation gap | 30% | 90% | 42% | Cannot achieve passing score *(INTENDED)* |

**Key Mathematical Insights:**

1. **Maximum Tier II with Weak Foundation:**
   - If Tier I = 50%, maximum possible Tier II = 60% (even with 100% comprehensive)
   - Organizations with weak foundations **cannot achieve passing grades** regardless of comprehensive efforts
   - This creates **strong incentive** to prioritize foundation controls

2. **Leverage Analysis:**
   - 10% improvement in Tier I → 8% improvement in Tier II
   - 10% improvement in Comprehensive → 2% improvement in Tier II
   - Foundation improvements have **4× leverage** compared to comprehensive improvements

3. **Fairness Validation (Simulation Results):**

| Organization | Tier I | Tier II | Old Score | Impact | Assessment |
|--------------|--------|---------|-----------|--------|------------|
| CBS | 95% | 95% | 96% | -1% | Excellence maintained across both models |
| Santa Catalina | 86% | 85% | 82% | **+3%** | Strong foundation rewarded appropriately |
| Rosary | 79% | 79% | 80% | -1% | Near 85% threshold, neutral impact |
| Salesian | 67% | 69% | 77% | **-8%** | Weak foundation correctly penalized |

**Conclusion:** Model is **working as intended** with no mathematical anomalies or fairness concerns.

### Strengths of Current Model

1. ✅ **Insurance Alignment:** Foundation questions directly map to cyber insurance underwriting requirements
2. ✅ **Clear Incentives:** Organizations understand exactly which controls are prioritized
3. ✅ **Simplicity:** Two scores are easy to understand and communicate
4. ✅ **Fairness:** Strong performers rewarded, weak performers penalized appropriately
5. ✅ **Demonstrated Impact:** Simulation with real data validates effectiveness
6. ✅ **Actionable:** Organizations know to focus on foundation first, then comprehensive maturity

### Potential Concerns and Mitigations

**Concern 1: Gaming the System**

**Risk:** Organizations could focus exclusively on 12 Tier I questions to maximize score while ignoring 39 other questions.

**Example:** Organization achieves 95% Tier I but only 50% on non-foundation questions
- Tier II = (0.80 × 95%) + (0.20 × 50%) = 86% (appears strong)
- However, detailed report reveals massive gaps in non-foundation categories

**Mitigation:**
- ✅ Report displays **both** Tier I and comprehensive scores (transparency)
- ✅ Category-level breakdown reveals specific gaps
- ✅ Question-by-question detail prevents hiding weaknesses
- ✅ Recommendation: Add minimum category thresholds (must achieve 60%+ in all 9 categories)

**Concern 2: Threshold Sensitivity**

**Risk:** Organizations near the 85% "strong" threshold (e.g., 84%) may feel unfairly treated compared to those at 86%.

**Example:** Organization A (84% Tier I) vs. Organization B (86% Tier I) with same comprehensive scores
- Organization A: (0.80 × 84%) + (0.20 × 75%) = 82.2%
- Organization B: (0.80 × 86%) + (0.20 × 75%) = 83.8%
- Difference: 1.6 percentage points from 2% foundation difference

**Mitigation:**
- ✅ Thresholds should be **ranges** not hard cutoffs (85-89% = "Strong" rather than "must be 85%+")
- ✅ Establish appeal process for organizations within 2% of threshold boundaries
- ✅ Focus on trend over time rather than single assessment snapshot

**Concern 3: Foundation Question Granularity**

**Risk:** With only 12 foundation questions, each question represents 8.3% of Tier I score. Single question failure has large impact.

**Example:** Organization fails one foundation question (EDR implementation)
- 11/12 foundation questions = 91.7% (appears strong)
- 10/12 foundation questions = 83.3% (drops below "strong" threshold)

**Mitigation:**
- ✅ **Immediate action:** Expand foundation from 12 to 15 questions (reduces single-question impact to 6.67%)
- ✅ **Short-term action:** Expand to 17 questions (reduces to 5.88%)
- ✅ **Long-term action:** Expand to 20 questions (reduces to 5%)
- ✅ More questions = more granular scoring and fairer representation

**Concern 4: Self-Reporting Validity**

**Risk:** Without evidence validation, organizations could claim "Fully Implemented" when controls are partially deployed.

**Example:** Organization claims EDR on "all endpoints" but actually has 60% coverage
- Self-reported: Tier I includes full points for EDR (question 5.4)
- Reality: Control is partially implemented at best
- Result: **False sense of security** and inaccurate insurance risk assessment

**Mitigation:**
- ⚠️ **CRITICAL ACTION:** Implement evidence validation for all 12 (soon 15-17) foundation questions
- Evidence types: Screenshots, configuration exports, scan reports, admin console data
- Validation process: Member submits evidence during assessment, assessor validates before finalizing report
- Timeline: Implement for Tier I foundation questions within 3 months

---

## Alternative Grading Model Approaches

### Option 1: Equal Weighting Model (50/50)

**Formula:**
```
Tier II Score = (0.50 × Tier I Score) + (0.50 × Comprehensive Score)
```

**Characteristics:**
- Balanced emphasis between foundation and comprehensive maturity
- Foundation still important but comprehensive controls have equal weight

**Comparison with Current Model (80/20):**

| Organization | Tier I | Comprehensive | 80/20 Model | 50/50 Model | Difference |
|--------------|--------|---------------|-------------|-------------|------------|
| Strong foundation, weak comprehensive | 90% | 60% | 84% | 75% | -9% |
| Weak foundation, strong comprehensive | 60% | 90% | 66% | 75% | +9% |
| Balanced strong | 85% | 85% | 85% | 85% | 0% |

**Analysis:**
- ❌ **Reduces foundation incentive:** Organizations with weak foundations can compensate with comprehensive efforts
- ❌ **Insurance misalignment:** Cyber insurance underwriters prioritize foundation controls; 50/50 doesn't reflect this
- ✅ **Rewards comprehensive efforts:** Organizations investing in advanced controls see greater benefit
- ✅ **Less harsh on foundation gaps:** Transition-phase organizations not as heavily penalized

**Recommendation:** **Not recommended** for CyberPools due to insurance alignment requirements. However, could be viable for organizations that:
- Are not insurance-driven
- Serve highly mature organizations
- Prioritize defense-in-depth over foundational compliance

---

### Option 2: Moderate Weighting Model (70/30)

**Formula:**
```
Tier II Score = (0.70 × Tier I Score) + (0.30 × Comprehensive Score)
```

**Characteristics:**
- Still emphasizes foundation but less aggressively than 80/20
- Provides more credit for comprehensive controls

**Comparison with Current Model (80/20):**

| Organization | Tier I | Comprehensive | 80/20 Model | 70/30 Model | Difference |
|--------------|--------|---------------|-------------|-------------|------------|
| Strong foundation, weak comprehensive | 90% | 60% | 84% | 81% | -3% |
| Weak foundation, strong comprehensive | 60% | 90% | 66% | 69% | +3% |
| Balanced strong | 85% | 85% | 85% | 85% | 0% |

**Analysis:**
- ⚠️ **Softer foundation emphasis:** Still prioritizes foundation but with less impact
- ⚠️ **Weaker insurance alignment:** Moderate weighting may not align as strongly with underwriting priorities
- ✅ **More forgiving transition:** Organizations improving from weak foundation have easier path
- ✅ **Rewards investment:** Comprehensive improvements have 30% weight vs. 20%

**Recommendation:** **Consider for transition period** if current 80/20 model creates resistance. Could implement 70/30 for first year, then migrate to 80/20 once members adapt.

---

### Option 3: Maturity Level Model (Tiered Qualitative)

**Structure:**
Rather than percentage scores, assign maturity levels:

| Level | Tier I Requirement | Comprehensive Requirement | Grade |
|-------|-------------------|---------------------------|-------|
| **Level 5: Optimized** | 95%+ | 90%+ | A+ |
| **Level 4: Managed** | 85%+ | 80%+ | A |
| **Level 3: Defined** | 75%+ | 70%+ | B |
| **Level 2: Developing** | 60%+ | 60%+ | C |
| **Level 1: Initial** | <60% | <60% | D/F |

**Characteristics:**
- Both Tier I and comprehensive requirements must be met to achieve level
- Organizations cannot advance with weak foundation OR weak comprehensive
- Aligns with maturity models (CMMI, NIST CSF Tiers)

**Example Application:**

| Organization | Tier I | Comprehensive | Level | Grade | Rationale |
|--------------|--------|---------------|-------|-------|-----------|
| Strong Performer | 95% | 92% | 5 | A+ | Meets both requirements |
| Foundation-Focused | 95% | 72% | 3 | B | Comprehensive limits advancement despite strong foundation |
| Comprehensive-Focused | 72% | 95% | 3 | B | Foundation limits advancement despite strong comprehensive |
| Balanced Strong | 88% | 85% | 4 | A | Meets both requirements |

**Analysis:**
- ✅ **Holistic view:** Both foundation and comprehensive must be strong
- ✅ **Clear advancement path:** Organizations know exact requirements for each level
- ✅ **Maturity language:** "Level 4" resonates with IT/security professionals familiar with maturity models
- ❌ **More complex:** Requires meeting two separate thresholds instead of single score
- ❌ **Harsher on imbalanced organizations:** Organization with 95% foundation but 72% comprehensive only achieves Level 3

**Recommendation:** **Consider for future enhancement** (Year 2+). Provides richer context but requires member education on maturity model concepts.

---

### Option 4: Risk-Weighted Model

**Structure:**
Weight each question by both impact rating AND industry risk data (insurance claims frequency).

**Formula:**
```
Risk-Weighted Score = Σ(Question Score × Impact × Claims Frequency Weight) / Σ(Max Points × Impact × Claims Frequency Weight)

Example Weights:
- Ransomware-related controls: 2.0× (high claims frequency)
- Data breach-related controls: 1.8× (high claims frequency)
- Availability controls: 1.3× (moderate claims frequency)
- Compliance controls: 1.0× (baseline)
```

**Example Application:**

| Control | Impact | Base Points | Claims Weight | Weighted Points |
|---------|--------|-------------|---------------|-----------------|
| EDR Implementation | 5 | 5 | 2.0× (ransomware) | 10 |
| MFA for Remote Access | 5 | 5 | 1.8× (data breach) | 9 |
| Backup Testing | 5 | 5 | 2.0× (ransomware) | 10 |
| Data Classification | 3 | 3 | 1.0× (compliance) | 3 |

**Characteristics:**
- Scores reflect actual insurance risk exposure
- Weights updated annually based on claims data
- More sophisticated but harder to explain

**Analysis:**
- ✅ **Actuarially sound:** Directly ties to insurance claims experience
- ✅ **Dynamic adaptation:** Weights adjust as threat landscape evolves
- ✅ **Defensible:** Based on empirical data not subjective opinion
- ❌ **Complex to explain:** Members may not understand why weights change
- ❌ **Data requirements:** Requires clean claims data across pools
- ❌ **Volatility risk:** Scores could shift year-to-year based on claims trends

**Recommendation:** **Long-term strategic option** (Year 3+). Requires:
- Aggregated claims data across SSCIP, The Trust, VSBIT
- Statistical analysis linking control failures to claims
- Member education on risk-weighted methodology
- Stable baseline (2-3 years) before introducing dynamic weighting

---

### Option 5: Hybrid Categorical Model

**Structure:**
Different weightings for different categories based on organizational context.

**K-12 Education Weighting:**
```
Tier II = (0.30 × Data Protection) + (0.25 × Account Management) + (0.20 × Incident Response) + (0.15 × Security Awareness) + (0.10 × Other Categories)

Rationale:
- Data Protection (30%): FERPA compliance is non-negotiable
- Account Management (25%): Student/teacher accounts are prime targets
- Incident Response (20%): Downtime disrupts learning
- Security Awareness (15%): Teachers handle sensitive data
```

**Healthcare Weighting:**
```
Tier II = (0.35 × Data Protection) + (0.25 × Access Control) + (0.20 × Audit/Logging) + (0.10 × Incident Response) + (0.10 × Other Categories)

Rationale:
- Data Protection (35%): HIPAA Security Rule emphasis
- Access Control (25%): PHI access is strictly regulated
- Audit/Logging (20%): HIPAA requires audit trails
- Incident Response (10%): Breach notification requirements
```

**Analysis:**
- ✅ **Sector-specific:** Reflects unique compliance and risk profiles
- ✅ **Regulatory alignment:** Weights match regulatory emphasis (FERPA vs. HIPAA)
- ✅ **Clear differentiation:** Education vs. healthcare have different priorities
- ❌ **Complex administration:** Multiple scoring models to maintain
- ❌ **Comparison challenges:** Cannot directly compare K-12 vs. healthcare scores
- ❌ **Development effort:** Requires creating and validating multiple weighting schemes

**Recommendation:** **Consider for healthcare expansion** (Month 6-12). Current two-tier model works for K-12; healthcare variant could use hybrid categorical to emphasize HIPAA priorities.

---

### Comparison Matrix: All Models

| Model | Foundation Emphasis | Comprehensiveness | Insurance Alignment | Complexity | Implementation Effort | Recommendation |
|-------|-------------------|-------------------|-------------------|------------|----------------------|----------------|
| **80/20 (Current)** | Very High | Low | Excellent | Low | ✅ Complete | **APPROVED - Keep** |
| **50/50 Equal** | Moderate | High | Moderate | Low | 2 hours | Not recommended |
| **70/30 Moderate** | High | Moderate | Good | Low | 2 hours | Consider as transition |
| **Maturity Levels** | High | High | Good | Moderate | 16-24 hours | Consider Year 2+ |
| **Risk-Weighted** | Variable | Moderate | Excellent | High | 80-120 hours | Consider Year 3+ |
| **Hybrid Categorical** | Variable | High | Excellent | High | 40-60 hours per sector | Consider for healthcare |

---

## Threshold Framework and Insurance Implications

### Recommended Grading Thresholds

Based on the analysis, here is the recommended threshold framework for Tier I (Foundation) and Tier II (Comprehensive) scores:

| Grade | Tier I Requirement | Tier II Requirement | Insurance Implications | Assessment Frequency | Remediation Requirements |
|-------|-------------------|---------------------|----------------------|---------------------|--------------------------|
| **A+ (Excellent)** | 95%+ | 90%+ | Premium discount eligibility, Extended assessment cycle (18 months) | Every 18 months | None - exemplary performance |
| **A (Strong)** | 90-94% | 85-89% | Standard premium rates, Standard assessment cycle | Annual | None - strong performance |
| **B (Good)** | 85-89% | 75-84% | Standard premium rates, Standard assessment cycle | Annual | Recommended improvements provided |
| **C (Adequate)** | 70-84% | 65-74% | Standard rates, Remediation plan required within 6 months | Annual with 6-month checkpoint | Remediation plan must be submitted |
| **D (Below Standard)** | 60-69% | 55-64% | Premium increase OR 90-day remediation requirement | Quarterly until improved to C | Mandatory remediation with progress reports |
| **F (Critical)** | <60% | <55% | Insurance ineligibility OR significant premium increase pending immediate remediation | Monthly until improved to D | Immediate remediation required; executive engagement |

### Detailed Tier Descriptions

**A+ Grade (Excellent - 95%+ Tier I, 90%+ Tier II)**

**Profile:**
- Organization has implemented and validated all foundation controls
- Comprehensive security program with mature processes
- Demonstrates continuous improvement and proactive risk management
- Likely has dedicated IT security staff or strong vCISO relationship

**Characteristics:**
- All foundation questions fully implemented
- Advanced controls in place (SIEM, DLP, penetration testing)
- Regular testing and validation of controls
- Security awareness culture embedded in organization
- Incident response plan tested annually
- Vendor risk management program established

**Insurance Implications:**
- **Premium discount eligibility:** 10-15% reduction
- **Extended assessment cycle:** Every 18 months instead of annual
- **Fast-track claims processing:** Pre-established trust with insurer
- **Higher coverage limits available:** Proven risk management justifies increased limits

**CyberPools Support:**
- vCISO hours focused on strategic initiatives (threat intelligence, advanced controls)
- Vulnerability scanning emphasis on advanced attacks
- Phishing simulations use sophisticated social engineering techniques
- Annual board-level briefing on cyber risk posture

---

**A Grade (Strong - 90-94% Tier I, 85-89% Tier II)**

**Profile:**
- Organization has strong foundation with nearly complete implementation
- Good comprehensive coverage with few gaps
- Demonstrates commitment to cybersecurity
- May have 1-2 foundation controls partially implemented

**Characteristics:**
- 11-12 of 12 foundation questions fully implemented
- Most comprehensive controls in place
- Regular training and awareness programs
- Backup testing performed at least annually
- Incident response plan documented and reviewed

**Insurance Implications:**
- **Standard premium rates:** No discounts but no penalties
- **Standard assessment cycle:** Annual risk assessment
- **Full coverage availability:** All standard coverage options available
- **Claims processing:** Normal timeline and documentation

**CyberPools Support:**
- vCISO hours focused on closing foundation gaps and enhancing maturity
- Vulnerability scanning with standard frequency
- Phishing simulations with moderate difficulty
- Quarterly check-ins to monitor progress

---

**B Grade (Good - 85-89% Tier I, 75-84% Tier II)**

**Profile:**
- Organization has implemented most foundation controls
- Comprehensive controls have multiple gaps
- Demonstrates awareness of cybersecurity but resource constraints may exist
- Likely small IT team with limited security expertise

**Characteristics:**
- 10-11 of 12 foundation questions fully or partially implemented
- Some comprehensive controls missing or partially implemented
- Training program exists but may not be comprehensive
- Backups exist but testing may be inconsistent
- Incident response plan may need updating

**Insurance Implications:**
- **Standard premium rates:** No penalties at this level
- **Standard assessment cycle:** Annual with recommended improvements
- **Coverage restrictions possible:** Some high-limit endorsements may require improvement
- **Claims review:** Standard process with documentation expectations

**CyberPools Support:**
- vCISO hours focused on foundation control implementation
- Vulnerability scanning highlights critical findings
- Phishing simulations identify training needs
- Detailed remediation roadmap provided
- Quarterly progress reviews recommended

---

**C Grade (Adequate - 70-84% Tier I, 65-74% Tier II)**

**Profile:**
- Organization has significant foundation gaps requiring attention
- Comprehensive controls have major deficiencies
- May lack cybersecurity awareness or budget constraints limit implementation
- High risk for cyber incidents

**Characteristics:**
- 8-10 of 12 foundation questions implemented (2-4 gaps)
- Common gaps: MFA not fully deployed, EDR missing, backup testing inconsistent
- Training may be minimal or non-existent
- Incident response plan may not exist
- Patching may be irregular

**Insurance Implications:**
- **Remediation plan required:** Must submit plan within 30 days, implement within 6 months
- **6-month checkpoint assessment:** Required to verify progress
- **Coverage restrictions likely:** Higher deductibles or lower limits possible
- **Premium impact:** May see moderate increases (5-10%) until improved

**CyberPools Support:**
- **Intensive vCISO engagement:** Weekly or bi-weekly check-ins
- **Prioritized remediation roadmap:** Focus on highest-impact foundation controls first
- **Accelerated vulnerability scanning:** Monthly instead of quarterly
- **Mandatory phishing training:** All identified high-risk users must complete training
- **Executive escalation:** Pool administrator notified of critical gaps

---

**D Grade (Below Standard - 60-69% Tier I, 55-64% Tier II)**

**Profile:**
- Organization has critical foundation gaps creating unacceptable risk exposure
- Comprehensive security program is minimal or non-existent
- High likelihood of successful cyberattack
- May lack basic cybersecurity understanding

**Characteristics:**
- 7 or fewer of 12 foundation questions fully implemented (5+ gaps)
- Critical gaps likely: No MFA, no EDR, inconsistent backups, no training
- May be running end-of-life software
- Patch management may be ad-hoc or non-existent
- No incident response capability

**Insurance Implications:**
- **90-day mandatory remediation:** Must close foundation gaps within 90 days
- **Quarterly assessments required:** Progress measured every 90 days until improved to C
- **Premium increase:** 15-25% surcharge OR conditional coverage
- **Coverage restrictions:** Higher deductibles, lower limits, exclusions for certain attack types
- **Conditional coverage:** Insurance may require completion of specific controls before claims are covered

**CyberPools Support:**
- **Emergency response mode:** Immediate vCISO engagement
- **Executive-level escalation:** Senior leadership must be involved
- **Weekly progress reports:** Required documentation of remediation efforts
- **Hands-on implementation support:** CyberPools may assist with tool deployment
- **Vulnerability scanning:** Immediate scan to identify critical exposure
- **Board notification:** Pool administrator provides board-level notification

---

**F Grade (Critical - <60% Tier I, <55% Tier II)**

**Profile:**
- Organization poses critical risk to itself and potentially the insurance pool
- Minimal to no cybersecurity controls in place
- Likely unaware of current risk exposure
- Immediate intervention required

**Characteristics:**
- 6 or fewer of 12 foundation questions implemented (50% or less)
- Multiple critical gaps: Often no MFA, no EDR, no backups, no training, no patching
- May be actively under attack without awareness
- No incident response capability
- Likely running end-of-life or unsupported systems

**Insurance Implications:**
- **Insurance ineligibility:** Coverage may be suspended until foundation controls implemented
- **OR significant premium increase:** 50%+ surcharge with strict conditions
- **Immediate remediation required:** Foundation controls must be implemented within 30-60 days
- **Monthly assessments:** Progress measured monthly until improved to D
- **Restricted coverage:** Cyber incidents may not be covered until remediation complete
- **Pool exposure concern:** Organization poses risk to entire pool's loss ratio

**CyberPools Support:**
- **Crisis intervention:** Immediate vCISO engagement with daily check-ins
- **Executive/board engagement required:** Senior leadership and board must participate
- **Implementation assistance:** CyberPools provides hands-on deployment support for critical controls
- **Daily progress monitoring:** Required daily or weekly updates depending on severity
- **Vulnerability assessment:** Immediate comprehensive scan
- **Incident response readiness:** Assume breach may have occurred; may recommend forensic investigation
- **Pool administrator notification:** Executive-level communication about risk exposure

---

### Foundation Score vs. Comprehensive Score: Decision Matrix

Some organizations may have **imbalanced scores** (strong foundation but weak comprehensive, or vice versa). Here's how to interpret:

| Scenario | Tier I | Tier II | Tier II Formula Result | Grade | Interpretation | Insurance Decision |
|----------|--------|---------|----------------------|-------|----------------|-------------------|
| Excellent foundation, weak comprehensive | 95% | 70% | (0.80 × 95%) + (0.20 × 70%) = 90% | A | Foundation is solid; focus on maturity | Standard rates, encourage improvement |
| Strong foundation, adequate comprehensive | 90% | 75% | (0.80 × 90%) + (0.20 × 75%) = 87% | A | Good position; minor gaps | Standard rates |
| Adequate foundation, strong comprehensive | 80% | 85% | (0.80 × 80%) + (0.20 × 85%) = 81% | B | Foundation needs attention despite good comprehensive | Standard rates, remediation plan recommended |
| Weak foundation, excellent comprehensive | 65% | 95% | (0.80 × 65%) + (0.20 × 95%) = 71% | C | Foundation gaps are critical despite comprehensive efforts | Remediation plan required for foundation |
| Critical foundation, strong comprehensive | 55% | 90% | (0.80 × 55%) + (0.20 × 90%) = 62% | D | Foundation gaps create unacceptable risk | 90-day remediation required |

**Key Principle:** **Foundation score takes precedence for insurance decisions.** Organizations with weak foundations (<70%) require remediation regardless of comprehensive scores.

---

## Next Year's Gap Analysis and Question Additions

### Priority 1: Data Protection Expansion (Immediate - Next Assessment Cycle)

**Current State:** Only 3 questions covering entire Data Protection category
**Problem:** Massive domain with insufficient coverage; FERPA compliance gaps
**Solution:** Add 4 questions to bring total from 3 to 7

**New Questions to Add:**

**Question 3.4: Data Classification Framework**
- **Text:** "Does the organization classify data based on sensitivity levels (e.g., public, internal, confidential, restricted)?"
- **Control Ratings:** 0=N/A, 1=Fully Implemented, 3=Partially Implemented, 5=Not Implemented
- **Impact:** 5 (High)
- **Foundation:** **YES** (add to Tier I)
- **Rationale:** Data classification drives all other data protection controls; essential for FERPA compliance
- **Category:** 3.0 Data Protection

**Question 3.5: Data Retention and Disposal Policies (FERPA Requirement)**
- **Text:** "Does the organization have documented data retention and disposal policies for sensitive information that comply with legal and regulatory requirements (e.g., FERPA, HIPAA)?"
- **Control Ratings:** 0=N/A, 1=Fully Implemented, 3=Partially Implemented, 5=Not Implemented
- **Impact:** 5 (High)
- **Foundation:** **YES** (add to Tier I)
- **Rationale:** FERPA requires 5-year student record retention; disposal policies prevent data breaches
- **Category:** 3.0 Data Protection

**Question 3.6: Encryption in Transit**
- **Text:** "Are all systems that store or process sensitive data encrypted both at rest AND in transit using industry-standard protocols (TLS/HTTPS)?"
- **Control Ratings:** 0=N/A, 1=Fully Implemented, 3=Partially Implemented, 5=Not Implemented
- **Impact:** 5 (High)
- **Foundation:** **YES** (add to Tier I)
- **Rationale:** Current question 3.3 only covers encryption at rest; in-transit encryption is equally critical
- **Category:** 3.0 Data Protection

**Question 3.7: Least Privilege Access to Data**
- **Text:** "Does the organization restrict access to sensitive data based on job role and business need (principle of least privilege)?"
- **Control Ratings:** 0=N/A, 1=Fully Implemented, 3=Partially Implemented, 5=Not Implemented
- **Impact:** 5 (High)
- **Foundation:** No (comprehensive maturity control)
- **Rationale:** Prevents insider threats and limits breach exposure; best practice for data protection
- **Category:** 3.0 Data Protection

**Impact Analysis:**
- Data Protection category expands from 3 to 7 questions (133% increase)
- Foundation questions expand from 12 to 15 (adds 3.4, 3.5, 3.6)
- Single foundation question impact reduces from 8.3% to 6.67% (more granular)
- Assessment time increases by ~5-7 minutes (4 additional questions)

---

### Priority 2: Security Monitoring and Logging (Short-Term - Month 3-6)

**Current State:** ZERO questions covering security monitoring, logging, or detection
**Problem:** 0% NIST CSF Detection coverage; organizations could achieve A grade with no visibility
**Solution:** Add new Category 10.0 - Security Monitoring and Logging with 4 questions

**New Category: 10.0 - Security Monitoring and Logging**

**Question 10.1: Centralized Logging**
- **Text:** "Does the organization collect and centralize security logs from critical systems (firewalls, servers, endpoints, authentication systems)?"
- **Control Ratings:** 0=N/A, 1=Fully Implemented, 3=Partially Implemented, 5=Not Implemented
- **Impact:** 5 (High)
- **Foundation:** **YES** (add to Tier I)
- **Rationale:** Cannot detect breaches without logs; essential for incident response
- **Category:** 10.0 Security Monitoring and Logging

**Question 10.2: Log Retention Policies**
- **Text:** "Are security logs retained for a minimum of 90 days in accordance with compliance requirements and protected from unauthorized modification?"
- **Control Ratings:** 0=N/A, 1=Fully Implemented, 3=Partially Implemented, 5=Not Implemented
- **Impact:** 3 (Moderate)
- **Foundation:** No
- **Rationale:** Compliance requirement (HIPAA, PCI-DSS); enables forensic investigation
- **Category:** 10.0 Security Monitoring and Logging

**Question 10.3: Log Review and Monitoring**
- **Text:** "Does the organization regularly review security logs or use automated monitoring tools (SIEM) to detect anomalies and security events?"
- **Control Ratings:** 0=N/A, 1=Fully Implemented, 3=Partially Implemented, 5=Not Implemented
- **Impact:** 5 (High)
- **Foundation:** **YES** (add to Tier I)
- **Rationale:** Logs without review provide no value; detection capability is critical
- **Category:** 10.0 Security Monitoring and Logging

**Question 10.4: Alerting and Response Capabilities**
- **Text:** "Are automated alerts configured for critical security events (e.g., failed authentication attempts, privilege escalation, suspicious activity) with documented response procedures?"
- **Control Ratings:** 0=N/A, 1=Fully Implemented, 3=Partially Implemented, 5=Not Implemented
- **Impact:** 5 (High)
- **Foundation:** No
- **Rationale:** Alerts enable rapid response; reduces dwell time and breach impact
- **Category:** 10.0 Security Monitoring and Logging

**Impact Analysis:**
- New category adds 4 questions to assessment (51 → 55 total)
- Foundation questions expand from 15 to 17 (adds 10.1 and 10.3)
- Addresses NIST CSF DE.CM (Detection) gap (0% → 60% coverage)
- Addresses CIS Control 8 (Audit Log Management) gap (0% → 70% coverage)
- Assessment time increases by ~5-7 minutes

---

### Priority 3: Additional Recommended Questions (Medium-Term - Month 6-12)

**Question 5.5: Shadow IT and Unauthorized Cloud Services**
- **Text:** "Does the organization have controls to prevent or detect unauthorized use of cloud storage and file-sharing services (e.g., personal Dropbox, Google Drive) for organizational data?"
- **Impact:** 5 (High) - Huge issue in education sector
- **Foundation:** No
- **Category:** 5.0 Malware Defense (or new category if expanding)

**Question 5.6: Removable Media Controls**
- **Text:** "Does the organization have policies and technical controls to manage the security risks of removable media (USB drives, external hard drives)?"
- **Impact:** 3 (Moderate)
- **Foundation:** No
- **Category:** 5.0 Malware Defense

**Question 7.4: Role-Specific Security Training**
- **Text:** "Does the organization provide role-specific security training for employees who handle sensitive data or have administrative access?"
- **Impact:** 3 (Moderate)
- **Foundation:** No
- **Category:** 7.0 Security Awareness

**Question 7.5: Onboarding Security Training Requirement**
- **Text:** "Are all new employees required to complete security awareness training during onboarding before being granted access to organizational systems?"
- **Impact:** 5 (High)
- **Foundation:** **YES** (add to Tier I in Year 2)
- **Category:** 7.0 Security Awareness

**Question 8.6: Vendor Access Management**
- **Text:** "Does the organization have documented processes for granting, reviewing, and revoking vendor and third-party access to organizational systems and data?"
- **Impact:** 5 (High)
- **Foundation:** No
- **Category:** 8.0 Vendor Management

**Question 6.5: Documented Disaster Recovery Plan**
- **Text:** "Does the organization have a documented disaster recovery plan that includes recovery procedures, assigned roles and responsibilities, and defined Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)?"
- **Impact:** 5 (High)
- **Foundation:** **YES** (add to Tier I in Year 2)
- **Category:** 6.0 Data Recovery

**Question 2.10: Privileged Access Management (PAM)**
- **Text:** "Does the organization implement privileged access management controls such as session recording, just-in-time access, or privilege elevation for administrative activities?"
- **Impact:** 3 (Moderate)
- **Foundation:** No
- **Category:** 2.0 Account Management

---

### Assessment Expansion Roadmap

| Timeline | Total Questions | Foundation (Tier I) | Categories | Key Additions |
|----------|----------------|-------------------|------------|---------------|
| **Current** | 51 | 12 (23.5%) | 9 | Baseline |
| **Year 1 - Phase 1 (0-3 months)** | 55 | 15 (27.3%) | 9 | +4 Data Protection (3.4-3.7) |
| **Year 1 - Phase 2 (3-6 months)** | 59 | 17 (28.8%) | 10 | +4 Security Monitoring (10.1-10.4) |
| **Year 2 (6-12 months)** | 66 | 20 (30.3%) | 10 | +7 Questions (5.5, 5.6, 6.5, 7.4, 7.5, 8.6, 2.10) |
| **Year 3 (12-24 months)** | 70-75 | 20-22 (28-31%) | 11-12 | Physical Security, Advanced Controls |

**Rationale for Phased Approach:**
1. **Minimizes disruption:** Gradual expansion allows members to adapt
2. **Validates effectiveness:** Pilot with subset before full rollout
3. **Maintains completion rates:** Incremental changes less likely to impact 93% completion rate
4. **Enables learning:** Team can refine questions based on member feedback
5. **Spreads workload:** CRM updates, template modifications, training can be staged

---

### Standards Coverage Impact

**Current Coverage vs. Year 2 Projection:**

| Framework | Current Coverage | After Year 1 (59Q) | After Year 2 (66Q) | Target |
|-----------|------------------|-------------------|-------------------|--------|
| **Cyber Insurance Requirements** | 85% | 95% | 98% | 95%+ |
| **CIS Controls v8 (IG1)** | 85% | 90% | 93% | 90%+ |
| **NIST Cybersecurity Framework** | 66% | 75% | 80% | 80%+ |
| **ISO 27001:2022** | 44% | 52% | 60% | 65%+ |
| **FERPA (K-12 Education)** | 55% | 85% | 90% | 85%+ |
| **HIPAA Security Rule** | 50% | 58% | 70% | 75%+ |

**Conclusion:** Year 1 additions (Data Protection + Security Monitoring) dramatically improve FERPA compliance and lay groundwork for healthcare expansion.

---

## Implementation Roadmap

### Phase 1: Immediate Actions (0-3 Months)

**Objective:** Address critical Data Protection gaps and implement evidence validation

**Tasks:**

1. **Draft and Validate New Data Protection Questions (Week 1-2)**
   - Finalize wording for questions 3.4, 3.5, 3.6, 3.7
   - Create control descriptions and implementation guidance
   - Develop scoring rubric for each question
   - Review with vCISO team for clarity and feasibility

2. **Update Assessment Framework (Week 2-3)**
   - Update `question_mapping.json` with new questions
   - Modify Dynamics 365 CRM to include new fields
   - Update category scoring logic to account for expanded Data Protection
   - Modify foundation question list: 12 → 15 (add 3.4, 3.5, 3.6)
   - Recalculate Tier I percentages (8.3% → 6.67% per question)

3. **Update Report Templates (Week 3-4)**
   - Modify Jinja2 templates to display 4 new questions
   - Update Data Protection category section
   - Adjust Tier I/Tier II score display (now 15 foundation questions)
   - Update boilerplate text explaining expanded Data Protection focus
   - Regenerate sample reports with test data

4. **Implement Evidence Validation Process (Week 4-8)**
   - Design evidence submission portal (CRM-based or SharePoint)
   - Document evidence requirements for each of 15 foundation questions
   - Update assessment workflow: Request evidence during interview → Allow 1-week submission → Validate before finalizing
   - Train assessors on evidence validation procedures
   - Create evidence validation checklist

5. **Pilot with Select Members (Week 9-10)**
   - Identify 3-5 members for pilot (mix of high/medium/low performers)
   - Conduct assessments with new questions
   - Gather feedback on question clarity and evidence requirements
   - Measure time impact (expect +5-7 minutes)
   - Refine questions and process based on feedback

6. **Full Rollout (Week 11-12)**
   - Announce enhanced assessment to all members
   - Provide education on new Data Protection questions
   - Emphasize FERPA compliance improvements
   - Begin assessments with expanded framework

**Deliverables:**
- Updated `question_mapping.json` with 55 questions (51 → 55)
- Modified CRM fields and workflows
- Updated report templates with expanded Data Protection
- Evidence validation process documentation
- Assessor training materials
- Member communication materials

**Success Metrics:**
- All 15 foundation questions have evidence validation implemented
- Assessment completion rate maintains 90%+ (from current 93%)
- Member feedback on new questions is positive (>70% satisfaction)
- Average assessment time increases by <10 minutes

---

### Phase 2: Short-Term Actions (3-6 Months)

**Objective:** Add Security Monitoring category and develop HIPAA variant

**Tasks:**

1. **Develop Security Monitoring Category (Month 3-4)**
   - Finalize questions 10.1, 10.2, 10.3, 10.4
   - Create category description and overview
   - Develop implementation guidance for small organizations (affordable SIEM options, log management tools)
   - Define evidence requirements (screenshots of SIEM dashboards, log retention policies)
   - Add questions to `question_mapping.json`

2. **Update CRM and Templates (Month 4)**
   - Add Category 10.0 to Dynamics 365
   - Update foundation list: 15 → 17 (add 10.1, 10.3)
   - Modify report templates to include new category
   - Update category summary and overall findings sections
   - Recalculate Tier I percentages (6.67% → 5.88% per question)

3. **HIPAA Variant Development (Month 4-5)**
   - Analyze HIPAA Security Rule requirements
   - Map current 55 questions to HIPAA safeguards (administrative, physical, technical)
   - Identify additional questions needed for HIPAA compliance
   - Create HIPAA-specific boilerplate content
   - Develop HIPAA risk scoring methodology
   - Update CRM to support variant selection

4. **Pilot Security Monitoring Questions (Month 5)**
   - Pilot with 5 members (include Christian Brothers Services healthcare entities if possible)
   - Assess understanding of logging/SIEM questions
   - Validate that evidence requirements are achievable for small organizations
   - Measure time impact
   - Refine questions based on feedback

5. **Rollout Security Monitoring Category (Month 6)**
   - Full deployment to all members in next assessment cycle
   - Provide education webinar on importance of logging and monitoring
   - Offer vCISO guidance on affordable SIEM solutions
   - Monitor completion rates and member feedback

**Deliverables:**
- New Category 10.0 with 4 questions
- Assessment expanded to 59 questions, 17 foundation
- HIPAA variant assessment framework (design complete, ready for Year 2 implementation)
- Updated report templates and CRM workflows
- Educational materials on security monitoring

**Success Metrics:**
- Security Monitoring category successfully added
- Assessment completion rate maintains 90%+
- HIPAA variant design validated with healthcare stakeholders
- Member feedback on logging questions is positive

---

### Phase 3: Medium-Term Actions (6-12 Months / Year 2)

**Objective:** Expand to comprehensive 66-question assessment and implement HIPAA variant

**Tasks:**

1. **Add Year 2 Questions (Month 6-8)**
   - Develop questions 5.5, 5.6, 6.5, 7.4, 7.5, 8.6, 2.10 (7 questions total)
   - Update foundation list: 17 → 20 (add 6.5, 7.5, and one other high-impact question)
   - Update all documentation and templates

2. **HIPAA Variant Implementation (Month 8-10)**
   - Complete HIPAA-specific question development
   - Create HIPAA assessment variant in CRM
   - Develop HIPAA compliance report template
   - Train assessors on HIPAA requirements

3. **Self-Service Portal Planning (Month 10-12)**
   - Begin design of self-service assessment portal
   - Define requirements and user experience
   - Evaluate Power Apps vs. custom development
   - Create project plan for Year 3 implementation

**Deliverables:**
- 66-question comprehensive assessment
- 20 foundation questions (30.3% of total)
- HIPAA variant ready for healthcare members
- Self-service portal design and project plan

---

### Phase 4: Long-Term Strategic (12-24 Months / Year 3+)

**Objective:** Implement self-service portal, API integrations, and advanced grading models

**Tasks:**

1. **Self-Service Assessment Portal (Month 12-18)**
   - Develop web-based questionnaire
   - Integrate with Dynamics 365 CRM
   - Implement evidence upload capabilities
   - Build automated report generation

2. **API-Based Evidence Validation (Month 18-24)**
   - Integrate with EDR platforms (CrowdStrike, SentinelOne, Microsoft Defender)
   - Integrate with MFA platforms (Duo, Microsoft Entra, Okta)
   - Integrate with backup solutions (Veeam, Acronis, Datto)
   - Automate evidence collection for foundation questions

3. **Advanced Grading Models (Month 24+)**
   - Implement maturity level model (Option 3)
   - Develop risk-weighted scoring (Option 4)
   - Create Cyber Fusion Center dashboard
   - Enable continuous assessment model

**Deliverables:**
- Self-service portal in production
- 50% time reduction per assessment
- API integrations for automated evidence validation
- Advanced grading options available

---

## Appendices

### Appendix A: Foundation Question List (Year 1 - 17 Questions)

| ID | Question | Category | Impact | Added |
|----|----------|----------|--------|-------|
| 1.4 | EOL software retirement | Inventory | 5 | Baseline |
| 2.3 | MFA for cloud resources | Account Mgmt | 5 | Baseline |
| 2.4 | MFA for remote access | Account Mgmt | 5 | Baseline |
| 2.5 | MFA for admin accounts | Account Mgmt | 5 | Baseline |
| 2.6 | MFA for critical systems | Account Mgmt | 5 | Baseline |
| 4.3 | Patch management | Secure Config | 5 | Baseline |
| 4.7 | External vulnerability scans | Secure Config | 5 | Baseline |
| 5.4 | EDR implementation | Malware Defense | 5 | Baseline |
| 6.3 | Air gap/immutable backups | Data Recovery | 5 | Baseline |
| 6.4 | Backup testing | Data Recovery | 5 | Baseline |
| 7.2 | Phishing simulation | Security Awareness | 5 | Baseline |
| 7.3 | Follow-up security training | Security Awareness | 5 | Baseline |
| **3.4** | **Data classification framework** | **Data Protection** | **5** | **Phase 1** |
| **3.5** | **Data retention and disposal (FERPA)** | **Data Protection** | **5** | **Phase 1** |
| **3.6** | **Encryption in transit** | **Data Protection** | **5** | **Phase 1** |
| **10.1** | **Centralized logging** | **Security Monitoring** | **5** | **Phase 2** |
| **10.3** | **Log review and monitoring** | **Security Monitoring** | **5** | **Phase 2** |

### Appendix B: Evidence Validation Requirements

| Foundation Question | Evidence Type | Examples | Validation Criteria |
|-------------------|---------------|----------|-------------------|
| 1.4 - EOL software | Inventory report | Asset management system showing no EOL software | No EOL software present OR documented exception plan |
| 2.3-2.6 - MFA | Admin console screenshot | MFA enrollment report showing 90%+ coverage | 90%+ of accounts have MFA enabled |
| 4.3 - Patch management | Dashboard or report | Patch compliance dashboard from endpoint management | 80%+ compliance for critical patches within 30 days |
| 4.7 - Vulnerability scans | Scan report | Qualys or similar scan summary | External scan completed within 90 days |
| 5.4 - EDR | Console screenshot | EDR dashboard showing agent deployment | 90%+ endpoints have EDR agents installed and active |
| 6.3 - Air gap backups | Configuration screenshot | Backup system showing air-gap or immutability config | Backups are air-gapped or immutable |
| 6.4 - Backup testing | Test results | Last backup restoration test results | Test completed within 12 months with documented results |
| 7.2 - Phishing simulation | Campaign report | CyberPools phishing campaign results | CyberPools Guppy data (already collected) |
| 7.3 - Follow-up training | Training report | CyberPools training portal completion data | CyberPools training data (already collected) |
| 3.4 - Data classification | Policy document | Data classification policy with defined levels | Policy exists and defines at least 3 classification levels |
| 3.5 - Data retention | Policy document | Data retention and disposal policy | Policy exists and addresses legal/regulatory requirements |
| 3.6 - Encryption in transit | Configuration export | TLS/HTTPS configuration for key systems | All systems processing sensitive data use TLS 1.2+ |
| 10.1 - Centralized logging | SIEM screenshot | Log collection dashboard showing sources | Logs collected from at least 5 critical system types |
| 10.3 - Log monitoring | SIEM alert config | SIEM alert rules or review schedule | Automated monitoring OR weekly manual review documented |

### Appendix C: Sample Report Language

**Tier I (Foundation) Score Section:**
```
Your Tier I (Foundation) Score is 87%, indicating STRONG compliance with the core cybersecurity controls
that are essential for cyber insurance eligibility and basic risk management.

Foundation Score Interpretation:
- 90%+ (Excellent): All foundation controls implemented; eligible for premium discounts
- 85-89% (Strong): Nearly complete foundation; standard insurance rates
- 70-84% (Adequate): Foundation gaps exist; remediation plan recommended
- 60-69% (Below Standard): Critical foundation gaps; mandatory remediation required
- <60% (Critical): Immediate intervention required; insurance eligibility at risk

Your organization has successfully implemented 13 of 15 foundation controls. The following foundation
controls require attention:
- [List foundation gaps]
```

**Tier II (Comprehensive) Score Section:**
```
Your Tier II (Comprehensive) Score is 84%, reflecting your overall cybersecurity maturity across all
assessment categories.

The Tier II Score is calculated as: (80% × Foundation Score) + (20% × Comprehensive Score across all 59 questions)

This weighting emphasizes the critical importance of foundation controls while also recognizing investment
in comprehensive security maturity. Your Tier II score of 84% indicates GOOD overall cybersecurity posture
with opportunities for continued improvement.

Comprehensive Score Breakdown:
- Foundation Controls (Tier I): 87% (13 of 15 implemented)
- All Controls (59 questions): 82%
- Tier II Calculation: (0.80 × 87%) + (0.20 × 82%) = 84%
```

---

## Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | October 30, 2025 | CyberPools Risk Assessment Team | Initial version |

---

**END OF DOCUMENT**
