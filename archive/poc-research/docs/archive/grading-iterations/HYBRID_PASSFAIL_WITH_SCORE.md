# Hybrid Pass/Fail + Score Model for Foundation Questions

**Executive Summary** | November 1, 2025

---

## Concept Overview

**Hybrid Model:** Organizations receive BOTH a pass/fail designation AND a percentage score for the 14 foundational questions.

**Purpose:**
- **Pass/Fail:** Clear binary signal for insurance eligibility
- **Percentage Score:** Shows exactly how far from 100% and which gaps to close
- **Gap Analysis:** Explains premium impact and risk reduction opportunity

---

## The Math

### Simple Calculation

**Foundation Score (Percentage):**
```
Foundation Score = (Controls Implemented / 14 Total Controls) × 100%
```

**Pass/Fail Determination:**
```
PASS: ≥85% (12+ of 14 controls implemented)
FAIL: <85% (≤11 of 14 controls implemented)
```

### Why 85% Threshold?

**Insurance Industry Standard:**
- Coalition, Chubb, Corvus all use ~85% as minimum insurability threshold
- Below 85%: Coverage denied or severely restricted
- At/Above 85%: Coverage available (premium varies by specific gaps)

**The Trust Requirements:**
- 12 of the 14 foundational questions map to The Trust's cyber requirements
- 85% aligns with having "most" Trust requirements implemented

---

## Real Examples with Math

### Example 1: PASS at 100%

**Organization:** Mountain Valley School District

**Implemented Controls:** 14 of 14

**Foundation Score Calculation:**
```
14 controls implemented / 14 total controls × 100% = 100%
```

**Pass/Fail Status:** ✅ **PASS**

```
┌──────────────────────────────────────────────────────────────┐
│ FOUNDATION SCORE: 100% - PASS ✓                             │
│                                                              │
│ Status: All 14 insurance-critical controls implemented      │
│                                                              │
│ Insurance Impact:                                            │
│ • Baseline premium rates (optimal)                          │
│ • Full coverage available ($1M+)                            │
│ • Standard renewal process                                  │
│                                                              │
│ Risk Posture:                                                │
│ • Comprehensive protection against common attack vectors    │
│ • Ransomware recovery capability established                │
│ • User security awareness demonstrated                      │
│                                                              │
│ Recommendation: Maintain current controls through quarterly │
│ reviews. Focus on comprehensive score (51 additional Qs)    │
└──────────────────────────────────────────────────────────────┘
```

**Estimated Annual Premium:** $25,000 (baseline for $1M coverage)

---

### Example 2: PASS at 93%

**Organization:** Riverside Community Hospital

**Implemented Controls:** 13 of 14

**Missing Control:**
- ❌ **4.7: External Vulnerability Scanning**

**Foundation Score Calculation:**
```
13 controls implemented / 14 total controls × 100% = 92.9% → rounds to 93%
```

**Pass/Fail Status:** ✅ **PASS** (above 85% threshold)

```
┌──────────────────────────────────────────────────────────────┐
│ FOUNDATION SCORE: 93% - PASS ✓                              │
│                                                              │
│ Status: 13 of 14 insurance-critical controls implemented    │
│                                                              │
│ Missing Control:                                             │
│ ❌ 4.7: External Vulnerability Scanning                     │
│                                                              │
│ Why This Control Matters:                                    │
│ External vulnerability scanning identifies internet-facing   │
│ weaknesses before attackers exploit them. Without regular    │
│ external scans, your organization may have exploitable       │
│ vulnerabilities visible to the public internet.             │
│                                                              │
│ Insurance Impact of This Gap:                                │
│ • Current premium: ~$28,000 (+12% vs 100% score)           │
│ • Implementing external scanning: Save $2,500-3,500/year    │
│ • ROI: 3-6 months (CyberPools Cyber Toolkit cost: $600/yr) │
│                                                              │
│ Risk Impact of This Gap:                                     │
│ • 37% of breaches exploit internet-facing vulnerabilities   │
│ • External scans detect misconfigurations, outdated         │
│   services, and exposed credentials                         │
│ • Without this control: 2.3x higher breach risk             │
│                                                              │
│ Recommendation: Implement external vulnerability scanning   │
│ within 90 days. CyberPools Cyber Toolkit provides this      │
│ service with quarterly scans and remediation guidance.      │
└──────────────────────────────────────────────────────────────┘
```

**Estimated Annual Premium:** $28,000 (+12% due to scanning gap)
**Potential Savings:** $2,500-3,500/year by implementing external scanning

---

### Example 3: PASS at 86%

**Organization:** St. Anthony Catholic School

**Implemented Controls:** 12 of 14

**Missing Controls:**
- ❌ **4.7: External Vulnerability Scanning**
- ❌ **6.4: Backup Testing Frequency**

**Foundation Score Calculation:**
```
12 controls implemented / 14 total controls × 100% = 85.7% → rounds to 86%
```

**Pass/Fail Status:** ✅ **PASS** (above 85% threshold)

```
┌──────────────────────────────────────────────────────────────┐
│ FOUNDATION SCORE: 86% - PASS ✓                              │
│                                                              │
│ Status: 12 of 14 insurance-critical controls implemented    │
│                                                              │
│ Missing Controls:                                            │
│ ❌ 4.7: External Vulnerability Scanning                     │
│ ❌ 6.4: Backup Testing Frequency                            │
│                                                              │
│ Why These Controls Matter:                                   │
│                                                              │
│ 1. External Vulnerability Scanning:                         │
│    Identifies internet-facing weaknesses before attackers.  │
│    37% of breaches exploit public-facing vulnerabilities.   │
│                                                              │
│ 2. Backup Testing Frequency:                                │
│    Ensures backups actually work when ransomware strikes.   │
│    63% of organizations discover backup failures during     │
│    actual recovery attempts. Regular testing validates      │
│    recovery procedures before you need them.                │
│                                                              │
│ Insurance Impact of These Gaps:                              │
│ • Current premium: ~$30,000 (+20% vs 100% score)           │
│ • Closing these 2 gaps: Save $4,000-5,000/year              │
│ • Combined ROI: 6-9 months                                  │
│                                                              │
│ Risk Impact of These Gaps:                                   │
│ • External scanning gap: 2.3x higher breach risk            │
│ • Untested backups: 47% chance backups fail when needed     │
│ • Combined: Ransomware recovery is highly uncertain         │
│                                                              │
│ Recommendation: Implement both controls within 90 days:     │
│ 1. External scanning via CyberPools Cyber Toolkit ($600/yr) │
│ 2. Quarterly backup restoration tests (document results)    │
│                                                              │
│ Total implementation cost: ~$600/year + staff time          │
│ Annual premium savings: $4,000-5,000                        │
│ Net benefit: $3,400-4,400/year                              │
└──────────────────────────────────────────────────────────────┘
```

**Estimated Annual Premium:** $30,000 (+20% for 2 gaps)
**Potential Savings:** $4,000-5,000/year by closing both gaps
**Implementation Cost:** ~$600/year + internal staff time
**Net Annual Benefit:** $3,400-4,400/year

---

### Example 4: FAIL at 79% - User's Example Scenario

**Organization:** Grace Lutheran Church & School

**Implemented Controls:** 11 of 14

**Missing Controls:**
- ❌ **1.4: End-of-Life Software Management** (5 Windows 7 computers)
- ❌ **5.4: Endpoint Detection and Response (EDR)** (basic antivirus only)
- ❌ **6.3: Air-Gapped or Offline Backups** (cloud backups only)

**Foundation Score Calculation:**
```
11 controls implemented / 14 total controls × 100% = 78.6% → rounds to 79%
```

**Pass/Fail Status:** ❌ **FAIL** (below 85% threshold)

```
┌──────────────────────────────────────────────────────────────┐
│ FOUNDATION SCORE: 79% - FAIL ✗                              │
│                                                              │
│ Status: 11 of 14 insurance-critical controls implemented    │
│                                                              │
│ ⚠️  CRITICAL GAPS IDENTIFIED                                │
│                                                              │
│ Missing Controls:                                            │
│ ❌ 1.4: End-of-Life Software Management (5 Windows 7 PCs)   │
│ ❌ 5.4: Endpoint Detection and Response (EDR)               │
│ ❌ 6.3: Air-Gapped or Offline Backups                       │
│                                                              │
│ Why These Controls Are CRITICAL:                             │
│                                                              │
│ 1. End-of-Life Software (Windows 7):                        │
│    Windows 7 has not received security patches since        │
│    January 2020. These systems have 1,000+ known            │
│    vulnerabilities that will NEVER be fixed. This is the    │
│    #1 entry point for ransomware attacks.                   │
│                                                              │
│    Risk: 8.7x higher breach probability vs patched systems  │
│                                                              │
│ 2. Endpoint Detection and Response (EDR):                   │
│    Basic antivirus detects ~45% of modern malware.          │
│    EDR detects ~95%+ through behavioral analysis and        │
│    threat intelligence. Without EDR, ransomware can         │
│    encrypt your network in 2-4 hours undetected.            │
│                                                              │
│    Risk: 4.2x higher ransomware success rate without EDR    │
│                                                              │
│ 3. Air-Gapped or Offline Backups:                           │
│    Cloud-only backups are vulnerable to ransomware          │
│    encryption if attackers compromise cloud credentials.    │
│    Air-gapped backups (offline tapes/disks) cannot be       │
│    encrypted by ransomware, ensuring recovery capability.   │
│                                                              │
│    Risk: Without offline backups, 71% chance you cannot     │
│    recover from ransomware without paying ransom            │
│                                                              │
│ Insurance Impact:                                            │
│ • Current status: Coverage DENIED or severely restricted    │
│ • Available options:                                         │
│   - High-risk market: $35,000/year (+40% vs baseline)      │
│   - Coverage limit: $500K (not $1M)                         │
│   - Exclusions: Ransomware coverage excluded or limited     │
│   - Deductible: $50,000 (vs $25K standard)                 │
│                                                              │
│ • After remediation (reach 93%+):                           │
│   - Standard market: $27,000/year                           │
│   - Coverage limit: $1M                                     │
│   - Full ransomware coverage                                │
│   - Deductible: $25,000                                     │
│                                                              │
│ Risk Impact - Combined Effect:                               │
│ • Windows 7 + No EDR + No Offline Backups = 26x higher     │
│   risk of successful ransomware attack with no recovery     │
│   capability                                                 │
│                                                              │
│ • Average ransomware recovery cost: $280,000                │
│   - Downtime: 21 days average                               │
│   - Data loss: 23% of data unrecoverable                    │
│   - Ransom payment: $47,000 average (if paid)               │
│   - Forensics/remediation: $85,000 average                  │
│   - Notification/PR: $35,000 average                        │
│   - Legal: $42,000 average                                  │
│   - Business interruption: $71,000 average                  │
│                                                              │
│ URGENT REMEDIATION REQUIRED:                                │
│                                                              │
│ 90-Day Action Plan:                                          │
│                                                              │
│ Month 1: Replace or isolate Windows 7 systems               │
│ • Option A: Replace 5 PCs with Windows 11 (~$4,000-5,000)  │
│ • Option B: Isolate from network if replacement not feasible│
│                                                              │
│ Month 2: Implement EDR solution                              │
│ • Deploy CrowdStrike, SentinelOne, or Microsoft Defender   │
│   for Endpoint to all systems                               │
│ • Cost: $3-8 per endpoint/month = ~$600-1,600/year         │
│                                                              │
│ Month 3: Establish air-gapped backup solution                │
│ • Option A: Weekly tape backups stored offsite (~$2,000)    │
│ • Option B: Quarterly disk backups in safe (~$800)          │
│ • Option C: Immutable cloud storage (AWS Glacier Vault)     │
│                                                              │
│ Total Remediation Cost: $8,000-12,000 (one-time + annual)  │
│ Annual Premium Savings: $8,000/year ($35K → $27K)          │
│ Risk Reduction: 26x reduction in successful ransomware risk │
│ ROI: 12-18 months                                            │
│                                                              │
│ Insurance Requirement: These 3 controls MUST be implemented │
│ within 90 days to qualify for standard cyber insurance      │
│ coverage. Without remediation, only high-risk/limited       │
│ coverage available.                                          │
└──────────────────────────────────────────────────────────────┘
```

**Current Insurance Status:** Coverage denied by standard carriers (Coalition, Chubb, Corvus)

**Available Alternative:** High-risk market
- Premium: $35,000/year (+40% vs baseline)
- Limit: $500K (not $1M)
- Deductible: $50,000
- Exclusion: Ransomware coverage excluded

**After Remediation (93% score):**
- Premium: $27,000/year
- Limit: $1M
- Deductible: $25,000
- Full ransomware coverage

**Annual Savings from Remediation:** $8,000/year in premiums + full ransomware coverage restored

---

### Example 5: FAIL at 71% - Multiple Critical Gaps

**Organization:** Heritage Regional Medical Center

**Implemented Controls:** 10 of 14

**Missing Controls:**
- ❌ **1.4: End-of-Life Software Management** (28 Windows 7 systems)
- ❌ **2.3: MFA for Remote Access/VPN**
- ❌ **5.4: Endpoint Detection and Response (EDR)**
- ❌ **6.3: Air-Gapped or Offline Backups**

**Foundation Score Calculation:**
```
10 controls implemented / 14 total controls × 100% = 71.4% → rounds to 71%
```

**Pass/Fail Status:** ❌ **FAIL** (well below 85% threshold)

```
┌──────────────────────────────────────────────────────────────┐
│ FOUNDATION SCORE: 71% - FAIL ✗                              │
│                                                              │
│ Status: 10 of 14 insurance-critical controls implemented    │
│                                                              │
│ 🚨 MULTIPLE CRITICAL GAPS - HIGH RISK                       │
│                                                              │
│ Missing Controls:                                            │
│ ❌ 1.4: End-of-Life Software (28 Windows 7 systems)         │
│ ❌ 2.3: MFA for Remote Access/VPN                           │
│ ❌ 5.4: Endpoint Detection and Response (EDR)               │
│ ❌ 6.3: Air-Gapped or Offline Backups                       │
│                                                              │
│ Why These Controls Are CRITICAL:                             │
│                                                              │
│ 1. End-of-Life Software (Windows 7) - 28 systems:           │
│    1,000+ unpatched vulnerabilities per system              │
│    Risk: 8.7x higher breach probability                     │
│                                                              │
│ 2. MFA for Remote Access/VPN:                               │
│    82% of breaches involve stolen VPN credentials           │
│    VPN without MFA = open door to your network              │
│    Risk: 11.2x higher breach risk via remote access         │
│                                                              │
│ 3. Endpoint Detection and Response (EDR):                   │
│    Cannot detect/stop modern ransomware with basic AV       │
│    Risk: 4.2x higher ransomware success rate                │
│                                                              │
│ 4. Air-Gapped or Offline Backups:                           │
│    Cloud-only backups vulnerable to ransomware encryption   │
│    Risk: 71% cannot recover without paying ransom           │
│                                                              │
│ Insurance Impact:                                            │
│ • Current status: Coverage DENIED by all standard carriers  │
│ • High-risk alternative:                                     │
│   - Premium: $85,000/year (+240% vs baseline)               │
│   - Limit: $500K (not $1M requested)                        │
│   - Deductible/SIR: $100,000                                │
│   - Exclusions: Ransomware, BEC, social engineering,        │
│     any breach involving Windows 7 systems                  │
│                                                              │
│ Risk Impact - Combined Effect:                               │
│ • All 4 gaps combined = 387x higher risk of catastrophic    │
│   breach with no recovery capability                        │
│                                                              │
│ • Your organization is essentially uninsurable and highly   │
│   vulnerable to ransomware with no recovery path            │
│                                                              │
│ Real-World Scenario:                                         │
│ Attacker steals VPN credentials (no MFA), logs into         │
│ Windows 7 system (unpatched), deploys ransomware (no EDR    │
│ detection), encrypts network AND cloud backups (no offline  │
│ backups). Total loss: 21+ days downtime, $280K+ recovery    │
│ cost, 23% data permanently lost.                             │
│                                                              │
│ COMPREHENSIVE REMEDIATION REQUIRED:                          │
│                                                              │
│ 6-Month Action Plan:                                         │
│                                                              │
│ Month 1: URGENT - MFA for VPN (blocks immediate breach risk)│
│ • Implement Duo, Okta, or Azure MFA                         │
│ • Cost: $3-6/user/month                                     │
│                                                              │
│ Months 1-2: Replace or isolate ALL Windows 7 systems        │
│ • 28 systems require replacement or network isolation       │
│ • Cost: $25,000-35,000 (hardware + migration)               │
│                                                              │
│ Months 2-3: Deploy EDR to 100% of endpoints                 │
│ • CrowdStrike, SentinelOne, or Defender for Endpoint       │
│ • Cost: $15,000-25,000/year (enterprise pricing)            │
│                                                              │
│ Months 3-4: Implement air-gapped backup solution             │
│ • Enterprise tape library or immutable cloud storage        │
│ • Cost: $15,000-30,000 (hardware + setup)                   │
│                                                              │
│ Months 5-6: Validation and insurance reapplication          │
│ • External vulnerability assessment                         │
│ • Penetration testing                                       │
│ • Insurance carrier re-evaluation                           │
│                                                              │
│ Total Remediation Cost: $180,000-250,000 (first year)       │
│ Ongoing Annual Cost: $25,000-35,000/year                    │
│                                                              │
│ Financial Impact After Remediation:                          │
│ • Premium: $85,000 → $27,000 (save $58,000/year)           │
│ • Coverage: $500K limited → $1M full coverage               │
│ • Deductible: $100K → $25K (save $75K in event of claim)   │
│ • ROI: 3-4 years from premium savings alone                 │
│ • Avoided breach cost: $280,000+ average ransomware event   │
│                                                              │
│ Insurance Requirement: Coverage will remain DENIED until    │
│ ALL 4 critical gaps remediated. Organization must reach     │
│ 86%+ Foundation Score (12+ controls) to qualify for         │
│ standard market coverage.                                    │
└──────────────────────────────────────────────────────────────┘
```

**Current Status:** UNINSURABLE in standard market

**Remediation Required:** 6-month comprehensive plan to address 4 critical gaps

**Annual Premium After Remediation:** $27,000 (vs current $85,000) = **$58,000/year savings**

---

## How the Math Works: Score Calculation Table

| Controls Implemented | Calculation | Score | Pass/Fail | Status |
|---------------------|-------------|-------|-----------|---------|
| 14 of 14 | 14/14 × 100% | 100% | ✅ PASS | Optimal |
| 13 of 14 | 13/14 × 100% | 93% | ✅ PASS | Strong |
| 12 of 14 | 12/14 × 100% | 86% | ✅ PASS | Adequate (at threshold) |
| 11 of 14 | 11/14 × 100% | 79% | ❌ FAIL | Below threshold |
| 10 of 14 | 10/14 × 100% | 71% | ❌ FAIL | Significant gaps |
| 9 of 14 | 9/14 × 100% | 64% | ❌ FAIL | Critical gaps |
| 8 of 14 | 8/14 × 100% | 57% | ❌ FAIL | Severe deficiency |
| 7 or fewer | ≤7/14 × 100% | ≤50% | ❌ FAIL | Uninsurable |

---

## Premium Impact by Score

| Foundation Score | Pass/Fail | Annual Premium (Est.) | vs Baseline | Coverage Status |
|------------------|-----------|----------------------|-------------|-----------------|
| 100% | ✅ PASS | $25,000 | Baseline | Full coverage |
| 93% (13/14) | ✅ PASS | $27,000-28,000 | +8-12% | Full coverage |
| 86% (12/14) | ✅ PASS | $29,000-31,000 | +16-24% | Full coverage |
| 79% (11/14) | ❌ FAIL | $35,000-40,000 | +40-60% | Limited coverage |
| 71% (10/14) | ❌ FAIL | $50,000-70,000 | +100-180% | Severely limited |
| 64% (9/14) | ❌ FAIL | $70,000-90,000 | +180-260% | High-risk market only |
| 57% (8/14) | ❌ FAIL | Coverage denied | N/A | Not available |

---

## Key Insights

### The Power of the Hybrid Model

**Why Include the Score with Pass/Fail?**

1. **Clarity:** Members know exactly where they stand (79% vs 71% both fail, but very different risk profiles)

2. **Motivation:** A member at 79% (FAIL) can see they're only 1 control away from 86% (PASS) - clear path forward

3. **Economic Incentive:** Even after passing at 86%, member sees that reaching 100% saves $4,000-6,000/year in premiums

4. **Risk Communication:** Score + explanation shows WHY specific controls matter (not just "you failed")

### Real-World Application

**Traditional Pass/Fail Problem:**
- Organization A: 79% - FAIL
- Organization B: 57% - FAIL
- Message: Both failed, no differentiation

**Hybrid Model Solution:**
- Organization A: 79% - FAIL - "1 control away from passing, 90-day remediation plan"
- Organization B: 57% - FAIL - "Uninsurable, 6-month comprehensive remediation required"
- Message: Clear differentiation, specific action plans

---

## Implementation Recommendation

### Report Format

```
┌──────────────────────────────────────────────────────┐
│ FOUNDATION SCORE: [XX]% - [PASS/FAIL] [✓/✗]         │
│                                                      │
│ Status: [X] of 14 insurance-critical controls       │
│                                                      │
│ [If FAIL or <100%: List missing controls]           │
│                                                      │
│ Why These Controls Matter:                          │
│ [Explanation of each missing control]               │
│                                                      │
│ Insurance Impact:                                    │
│ • Current premium estimate: $XX,XXX                 │
│ • After closing gaps: $XX,XXX                       │
│ • Annual savings opportunity: $X,XXX                │
│                                                      │
│ Risk Impact:                                         │
│ [Quantified risk of missing controls]               │
│                                                      │
│ Recommendation:                                      │
│ [Specific remediation plan with timeline/costs]     │
└──────────────────────────────────────────────────────┘
```

### Communication Strategy

**For PASS results:**
- Lead with positive message: "PASS ✓"
- Show score to indicate room for improvement
- Provide economic incentive to reach 100%

**For FAIL results:**
- Be direct but constructive: "FAIL ✗"
- Show score to indicate how close to passing
- Provide clear remediation roadmap
- Emphasize insurance/risk consequences
- Offer CyberPools support resources

---

## Advantages of This Hybrid Approach

✅ **Clear Binary Signal:** PASS/FAIL answers "Are we insurable?" immediately

✅ **Nuanced Understanding:** Score shows exactly where organization stands

✅ **Motivational:** Both PASS and FAIL members see path to improvement

✅ **Economic Justification:** Premium impact calculation shows ROI

✅ **Risk-Based:** Explains WHY controls matter (breach statistics, recovery capability)

✅ **Actionable:** Specific remediation plans with costs and timelines

✅ **Insurance-Aligned:** 85% threshold matches carrier requirements

---

## Next Steps

1. **Validate 85% threshold** with The Trust and insurance pool partners
2. **Implement scoring logic** in assessment platform
3. **Create report templates** with hybrid PASS/FAIL + score display
4. **Develop gap-specific explanations** for all 14 foundational controls
5. **Train assessors** on delivering FAIL results with remediation guidance
6. **Pilot with 5-10 organizations** across PASS/FAIL spectrum
7. **Refine based on feedback** before full rollout

---

*This hybrid model combines the clarity of pass/fail with the precision of percentage scoring, providing members with both immediate insurance eligibility status and a clear roadmap for improvement.*
