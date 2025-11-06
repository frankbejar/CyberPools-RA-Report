# 4-Tier Foundation Score: Real Organization Examples

**Executive Summary** | November 1, 2025

---

## The 14 Foundational Questions

These insurance-critical controls drive insurability and premium rates:

| # | Control | Why Foundational |
|---|---------|------------------|
| 1.4 | End-of-Life Software Management | #1 ransomware attack vector |
| 2.3 | MFA for Remote Access/VPN | Prevents credential-based breaches |
| 2.4 | MFA for Cloud Services | Protects cloud data access |
| 2.5 | MFA for Administrative Accounts | Prevents privileged escalation |
| 2.6 | MFA for All Users | Comprehensive credential protection |
| 3.5 | Privileged Access Management (PAM) | Controls admin access misuse |
| 4.3 | Patch Management Process | Closes exploitable vulnerabilities |
| 4.7 | External Vulnerability Scanning | Identifies internet-facing risks |
| 5.4 | Endpoint Detection and Response (EDR) | Detects and stops malware/ransomware |
| 5.5 | Email Authentication (DMARC/SPF/DKIM) | Prevents email spoofing/phishing |
| 6.3 | Air-Gapped or Offline Backups | Ransomware recovery capability |
| 6.4 | Backup Testing Frequency | Ensures backups actually work |
| 7.2 | Phishing Simulation Testing | Measures human vulnerability |
| 7.3 | Security Awareness Training Frequency | Reduces user risk behavior |

---

## 4-Tier Model in Action

### Example 1: TIER 1 - FOUNDATION COMPLETE (100%)

**Organization:** Mountain Valley School District
**Foundation Score:** 100% (14 of 14 controls implemented)

```
┌─────────────────────────────────────────────────────────┐
│ FOUNDATION SCORE: 100%                                  │
│                                                         │
│ Status: FOUNDATION COMPLETE ✓ READY                    │
│                                                         │
│ All 14 insurance-critical controls fully implemented   │
│                                                         │
│ Insurance Impact:                                       │
│ • Baseline premium rates (optimal)                     │
│ • Broadest coverage options available                  │
│ • Streamlined renewal process                          │
│                                                         │
│ Recommendation: Maintain current controls through      │
│ quarterly reviews and annual reassessment              │
└─────────────────────────────────────────────────────────┘
```

**What They Implemented:**
- ✅ All Windows 11, no Windows 7/8
- ✅ MFA enabled on VPN, O365, admin accounts, and all user accounts
- ✅ Documented PAM process with quarterly privileged access reviews
- ✅ Monthly patching schedule with 95%+ compliance
- ✅ External vulnerability scanning via CyberPools Cyber Toolkit
- ✅ CrowdStrike EDR deployed to 100% of endpoints
- ✅ DMARC policy at enforcement (p=reject)
- ✅ Air-gapped backups stored offsite
- ✅ Quarterly backup restoration tests documented
- ✅ Monthly phishing simulations via KnowBe4
- ✅ Annual security awareness training (100% completion)

**Annual Premium:** $25,000 (baseline rate for $1M coverage)

---

### Example 2: TIER 2 - FOUNDATION SUBSTANTIAL (86%)

**Organization:** Riverside Community Hospital
**Foundation Score:** 86% (12 of 14 controls implemented)

```
┌─────────────────────────────────────────────────────────┐
│ FOUNDATION SCORE: 86%                                   │
│                                                         │
│ Status: FOUNDATION SUBSTANTIAL → ADEQUATE              │
│                                                         │
│ Strong foundational security with 2 gaps remaining     │
│                                                         │
│ Insurance Impact:                                       │
│ • Current premium: $30,000 (+20% vs baseline)         │
│ • Potential savings: $4,000-5,000/year                 │
│ • Closing 2 gaps → move to FOUNDATION COMPLETE         │
│                                                         │
│ Missing Controls:                                       │
│ ❌ 4.7: External Vulnerability Scanning                │
│ ❌ 6.4: Backup Testing (no documented tests)           │
│                                                         │
│ Next Steps: Implement 2 missing controls within        │
│ 90 days to qualify for premium reduction at renewal    │
└─────────────────────────────────────────────────────────┘
```

**What They Implemented:**
- ✅ All Windows 10/11, decommissioned Windows 7 systems
- ✅ MFA on VPN, O365, admin accounts, and all user accounts
- ✅ PAM process with spreadsheet tracking of admin accounts
- ✅ Automated patching via WSUS
- ❌ **NO external vulnerability scanning** (relying only on internal scans)
- ✅ Microsoft Defender for Endpoint (EDR)
- ✅ DMARC policy at enforcement
- ✅ Air-gapped backup tapes stored offsite weekly
- ❌ **NO documented backup restoration tests** (last test was 18 months ago)
- ✅ Quarterly phishing simulations
- ✅ Annual security training via HealthcareSource

**Annual Premium:** $30,000 (+20% for 2 missing controls)
**Potential Savings:** $4,000-5,000 by implementing external scanning and quarterly backup tests

**Risk:** Without external scanning, internet-facing vulnerabilities may go undetected. Without tested backups, ransomware recovery is uncertain.

---

### Example 3: TIER 3 - FOUNDATION DEVELOPING (71%)

**Organization:** Grace Lutheran Church & School
**Foundation Score:** 71% (10 of 14 controls implemented)

```
┌─────────────────────────────────────────────────────────┐
│ FOUNDATION SCORE: 71%                                   │
│                                                         │
│ Status: FOUNDATION DEVELOPING ⚠️ AT RISK               │
│                                                         │
│ Significant foundational gaps create elevated risk     │
│                                                         │
│ Insurance Impact:                                       │
│ • Current premium: $18,000 (+50% vs baseline)         │
│ • Coverage limitations: No social engineering coverage │
│ • Renewal: Conditional on 90-day remediation plan      │
│                                                         │
│ Missing Controls (Priority Order):                     │
│ ❌ 5.4: EDR/Antivirus (basic AV only, no EDR)         │
│ ❌ 6.3: Air-Gapped Backups (cloud backups only)       │
│ ❌ 6.4: Backup Testing (never tested)                  │
│ ❌ 7.2: Phishing Simulations (never conducted)         │
│                                                         │
│ URGENT: Implement EDR and air-gapped backups within   │
│ 90 days. Failure to remediate may result in           │
│ non-renewal or coverage denial.                        │
└─────────────────────────────────────────────────────────┘
```

**What They Implemented:**
- ✅ Windows 10 on all workstations (1 Windows 7 server scheduled for replacement)
- ✅ MFA on VPN and O365
- ✅ MFA on admin accounts
- ❌ **NO MFA for general users** (only staff, not faculty/volunteers)
- ✅ Basic PAM process (manual log of admin accounts)
- ✅ Patching happens but inconsistent (60% within 30 days)
- ❌ **NO external vulnerability scanning** (never conducted)
- ❌ **NO EDR** (using Microsoft Defender free version, no EDR features)
- ✅ SPF/DKIM configured, DMARC in monitor mode only
- ❌ **Backups to cloud only** (Veeam to Azure, no offline copies)
- ❌ **Backups never tested** (no restoration drills)
- ❌ **NO phishing simulations** (awareness training only)
- ✅ Annual security awareness training (videos)

**Annual Premium:** $18,000 (+50% for elevated risk)
**Coverage Limitations:** Social engineering exclusion, $250K sublimit on ransomware

**Risk Profile:**
- High ransomware exposure without EDR
- Uncertain recovery capability without tested offline backups
- Users untested against phishing attacks

**Remediation Plan Required:** Carrier issued 90-day improvement plan requiring EDR implementation and air-gapped backup solution as conditions for renewal.

---

### Example 4: TIER 4 - FOUNDATION DEFICIENT (57%)

**Organization:** Heritage Regional Medical Center
**Foundation Score:** 57% (8 of 14 controls implemented)

```
┌─────────────────────────────────────────────────────────┐
│ FOUNDATION SCORE: 57%                                   │
│                                                         │
│ Status: FOUNDATION DEFICIENT 🚨 NOT READY              │
│                                                         │
│ Insufficient foundational controls - HIGH RISK         │
│                                                         │
│ Insurance Impact:                                       │
│ • Coverage: DENIED by Coalition, Chubb, Corvus         │
│ • Alternative: High-risk carrier at $85,000/year       │
│   (240% premium increase vs baseline)                  │
│ • Coverage: $500K limit (not $1M), $100K SIR           │
│ • Exclusions: Ransomware, social engineering, BEC      │
│                                                         │
│ Missing Controls (CRITICAL):                           │
│ ❌ 1.4: End-of-Life Software (28 Windows 7 systems)    │
│ ❌ 2.3: MFA for Remote Access (no MFA on VPN)          │
│ ❌ 4.3: Patch Management (no formal process)           │
│ ❌ 4.7: External Vulnerability Scanning                │
│ ❌ 5.4: EDR (no EDR deployed)                          │
│ ❌ 6.3: Air-Gapped Backups (cloud only)                │
│                                                         │
│ URGENT: Organization is uninsurable with standard      │
│ carriers. Comprehensive 6-month remediation required   │
│ before coverage consideration.                          │
└─────────────────────────────────────────────────────────┘
```

**What They Implemented:**
- ❌ **28 Windows 7 systems still in production** (medical devices, lab systems)
- ❌ **NO MFA on VPN** (username/password only for remote access)
- ✅ MFA on O365 (Microsoft Conditional Access)
- ✅ MFA on admin accounts
- ✅ MFA rollout to users (80% complete)
- ✅ Basic PAM tracking via spreadsheet
- ❌ **NO formal patch management** (ad-hoc patching, 3-6 month lag)
- ❌ **NO external vulnerability scanning**
- ❌ **NO EDR** (legacy Symantec Endpoint Protection)
- ✅ DMARC in monitor mode (p=none)
- ❌ **Backups to AWS only** (no offline/air-gapped copies)
- ✅ Backup testing conducted quarterly
- ✅ Annual phishing simulations via KnowBe4
- ✅ Biannual security awareness training

**Insurance Status:** **COVERAGE DENIED**

**Standard Carriers (Coalition, Chubb, Corvus):** All declined due to Windows 7 systems and lack of MFA on VPN

**High-Risk Alternative:**
- Carrier: Beazley Breach Response (high-risk division)
- Premium: $85,000/year (vs $25,000 baseline = 240% increase)
- Coverage: $500K limit (not $1M requested)
- Self-Insured Retention: $100,000 (vs $25K standard)
- Exclusions: Ransomware, BEC, social engineering, any breach involving Windows 7 systems

**Critical Issues:**
1. **Windows 7 Systems:** Unpatched OS creates easy ransomware entry point
2. **No VPN MFA:** Remote access is single point of failure for credential theft
3. **No EDR:** Cannot detect/respond to malware/ransomware in real-time
4. **No Air-Gapped Backups:** Cloud-only backups are vulnerable to ransomware encryption
5. **No Patch Management:** 3-6 month patching lag leaves known vulnerabilities exploitable

**Remediation Required (6-Month Plan):**
1. **Month 1-2:** Decommission or isolate all Windows 7 systems (replace or virtualize)
2. **Month 1:** Implement MFA on VPN (Duo, Okta, or Azure MFA)
3. **Month 2-3:** Deploy EDR to 100% of endpoints (CrowdStrike, SentinelOne, or Microsoft Defender for Endpoint)
4. **Month 3-4:** Establish formal patch management with 30-day compliance target
5. **Month 4:** Implement air-gapped backup solution (tape, disk, or immutable cloud)
6. **Month 5-6:** Conduct external vulnerability scanning and remediate critical/high findings

**Estimated Remediation Cost:** $180,000-250,000
**Potential Premium Savings After Remediation:** $60,000/year (from $85K to $25K baseline)
**ROI:** 3-4 years

---

## Side-by-Side Comparison

| Metric | Tier 1 (100%) | Tier 2 (86%) | Tier 3 (71%) | Tier 4 (57%) |
|--------|---------------|--------------|--------------|--------------|
| **Status** | COMPLETE ✓ | SUBSTANTIAL | DEVELOPING ⚠️ | DEFICIENT 🚨 |
| **Readiness** | READY | ADEQUATE | AT RISK | NOT READY |
| **Controls** | 14 of 14 | 12 of 14 | 10 of 14 | 8 of 14 |
| **Premium** | $25,000 | $30,000 | $18,000 | $85,000 |
| **vs Baseline** | Baseline | +20% | +50%* | +240% |
| **Coverage** | $1M full | $1M full | $1M limited | $500K limited |
| **SIR/Deductible** | $25,000 | $25,000 | $50,000 | $100,000 |
| **Exclusions** | None | None | Social eng. | Ransomware, BEC |
| **Renewal** | Standard | Standard | Conditional | Denied |
| **Action** | Maintain | Close 2 gaps | 90-day plan | 6-month plan |

*Note: Tier 3 premium appears lower due to coverage limitations (social engineering exclusion, higher deductible)

---

## Key Insights

### Why 4 Tiers Matter

**The Problem with Pass/Fail or 3-Tier:**

A **3-tier model** would classify both the 100% organization and the 86% organization as "QUALIFIED" - masking the $5,000/year premium difference and providing no incentive for the 86% organization to close their 2 gaps.

A **pass/fail model** would classify the 71% organization the same as the 57% organization - both "fail" - despite one being recoverable with a 90-day plan and the other requiring comprehensive 6-month remediation.

**The 4-Tier Solution:**

- **Tier 1 (95-100%):** Optimal insurance outcome - celebrate and maintain
- **Tier 2 (80-94%):** Strong position with clear ROI to reach Tier 1
- **Tier 3 (65-79%):** Elevated risk requiring urgent remediation plan
- **Tier 4 (<65%):** Uninsurable or severely limited coverage - comprehensive intervention required

### Premium Impact Summary

| Foundation Score | Tier | Typical Premium Impact | Coverage Status |
|------------------|------|------------------------|-----------------|
| 100% | COMPLETE | Baseline ($25K) | Full coverage |
| 95% | COMPLETE | +5-10% ($26-27.5K) | Full coverage |
| 86% | SUBSTANTIAL | +15-25% ($29-31K) | Full coverage |
| 80% | SUBSTANTIAL | +20-30% ($30-32.5K) | Full coverage |
| 71% | DEVELOPING | +40-60% ($35-40K)* | Limited coverage |
| 65% | DEVELOPING | +50-80% ($37.5-45K)* | Limited coverage |
| 57% | DEFICIENT | +100-250% ($50-85K)** | Severely limited |
| <50% | DEFICIENT | Coverage denied | N/A |

*Includes coverage limitations (exclusions, lower limits)
**High-risk market pricing with significant exclusions

---

## What This Means for CyberPools Members

### For Members at TIER 1 (95-100%):
**Message:** "Excellent work! Your foundational security is insurance-ready. Focus on maintaining these controls through quarterly reviews and leveraging your strong position for optimal premium rates."

### For Members at TIER 2 (80-94%):
**Message:** "Strong foundational security with 1-3 gaps. Closing these gaps provides clear ROI through premium reduction. We'll help you prioritize which controls offer the best insurance impact."

### For Members at TIER 3 (65-79%):
**Message:** "Your organization is at elevated risk. Insurance carriers are flagging 4-5 critical gaps. We recommend a 90-day remediation plan focusing on highest-impact controls: EDR, air-gapped backups, and MFA gaps."

### For Members at TIER 4 (<65%):
**Message:** "Your organization may face coverage denial or severely limited options. We need a comprehensive 6-month remediation plan addressing 6+ critical gaps. CyberPools will work with you on implementation roadmap and budget planning."

---

## Implementation Recommendation

**Adopt the 4-Tier Model for Foundation Score reporting to:**

1. ✅ Provide clear, actionable guidance at every level
2. ✅ Show economic incentive for improvement (premium impact)
3. ✅ Align with insurance carrier risk assessment practices
4. ✅ Motivate continuous improvement (not just "passing")
5. ✅ Identify at-risk members requiring urgent intervention

**Next Steps:**
1. Update scoring engine to calculate tier based on Foundation Score percentage
2. Update report templates with tier-specific messaging and premium guidance
3. Create tier-specific remediation playbooks for assessors
4. Validate tier thresholds (95/80/65) with The Trust and other insurance pool partners

---

*Examples based on real CyberPools assessment patterns across K-12 education, healthcare, and nonprofit sectors. Organization names and specific details anonymized.*
