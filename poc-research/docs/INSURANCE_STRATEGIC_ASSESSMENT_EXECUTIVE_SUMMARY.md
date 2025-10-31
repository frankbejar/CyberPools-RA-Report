# CyberPools 2026 Risk Assessment Strategy
## Executive Summary - Insurance Industry Alignment

**Date:** October 30, 2025
**Prepared by:** Cybersecurity Risk & Insurance Expert
**Purpose:** Strategic recommendations for 2026 grading model and question expansion

---

## Executive Overview

The cyber insurance market has fundamentally shifted from "best practices" to **binary minimum requirements** in 2024-2025. CyberPools' current single-score model (0-100%) allows organizations to score 80% overall while missing controls that are now **universally required for coverage**, creating significant business risk for both CyberPools and member organizations.

**Critical Example:** Santa Catalina School scores 80% overall (B grade) but lacks:
- EDR (Endpoint Detection & Response) - **universal insurance requirement**
- External vulnerability scanning - required by 70% of carriers
- Bi-annual backup testing - current standard vs. their annual testing

**Insurance Reality:** This organization would face **application denial or 30-50% premium increases** in the 2026 market, yet the 80% score suggests acceptable risk.

---

## Key Insurance Market Findings

### The "Big Four" Universal Requirements (2025-2026)

These controls are now **mandatory** (not optional) across all major carriers:

1. **Multi-Factor Authentication (MFA)** - All systems, all users
   - Missing MFA = 82% of denied claims (Coalition 2024)
   - Application denial from most carriers without MFA

2. **Endpoint Detection & Response (EDR)** - NOT traditional antivirus
   - CrowdStrike, SentinelOne, Microsoft Defender for Endpoint
   - Traditional antivirus (Webroot, Norton) **no longer sufficient**
   - #2 reason for application denial

3. **Encrypted/Air-gapped Backups** - Bi-annual testing minimum
   - 3-2-1 rule (3 copies, 2 media, 1 offsite)
   - Testing frequency increased: Annual → Bi-annual (2025) → Quarterly (2026 trend)

4. **Incident Response Plan** - Written, tested annually
   - Tabletop exercises now required for policies >$1M
   - Untested plans fail during actual incidents

### Market Statistics

- **41%** of insurance applications denied on first submission (Marsh McLennan 2024)
- **70%** of carriers now require external vulnerability scanning
- **60-70%** of carriers asking about SIEM/logging capabilities
- Premium increases: **15-20%** annually through 2026

---

## The Trust / Gallagher / RPA Relationship

**Hierarchy Confirmed:**
```
Gallagher (Major global insurance conglomerate)
    ↓
Risk Program Administrators (RPA) - Gallagher division
    ↓
The Trust (Insurance pool)
    ↓
7 simplified cyber requirements → mapped to 12 CyberPools questions
```

**Assessment of Trust's 7 Requirements:**
- ✅ Align with **2023-2024** insurance standards
- ⚠️ Need expansion to **10-12 requirements** for 2026 relevance
- **Missing:** Security monitoring/logging, endpoint encryption, session lockout, dormant account management

---

## Strategic Recommendation: Option 2 (Dual-Score Model)

### Why Dual-Score Model

**Insurance underwriting is a two-stage process:**
1. **Foundation Controls** → Binary qualification decision (approve/decline)
2. **Comprehensive Controls** → Premium tier decision (preferred/standard/substandard)

**Current single-score model combines these distinct decisions into one number, losing critical information underwriters need.**

### How It Works

**Two separate scores reported prominently:**

```
╔═══════════════════════════════════════════════════════════╗
║  FOUNDATION CONTROLS                              75%  C  ║
║  (7 Trust requirements: 12 questions, 9/12 met)          ║
╠═══════════════════════════════════════════════════════════╣
║  COMPREHENSIVE MATURITY                           80%  B  ║
║  (All 51 controls across 9 categories)                    ║
╚═══════════════════════════════════════════════════════════╝
```

**Member Value:**
- **Clear prioritization**: Fix foundation gaps first (affects insurability)
- **Better ROI**: Investment in foundation controls yields insurance qualification
- **Transparent**: Two scores show exactly where improvement is needed

**Insurance Carrier Value:**
- **Immediate qualification indicator**: Foundation score = insurability
- **Premium calculation**: Comprehensive score = rate tier
- **Efficient underwriting**: No need to read 51 questions to determine coverage decision

### Competitive Advantage

- CAI (competitor) launched similar model **July 2025** - validates market demand
- **No other K-12 assessment provider** offers dual-score insurance-aligned model
- Positions CyberPools as industry leader

---

## Critical Gap: Security Monitoring

**Current Coverage:** **ZERO questions** on detection/monitoring/logging

**Insurance Impact:**
- 60-70% of carriers now require evidence of detection capabilities
- Dwell time (breach detection time) is key underwriting factor
- Organizations without monitoring face 20-30% premium increases

**NIST CSF 2.0** elevated "Detect" function to equal status with "Protect"

**Recommended Addition (Priority 1 - Q1 2026):**

**Category 10.0: Security Monitoring (4 new questions)**
1. 10.1: Centralized Logging (SIEM)
2. 10.2: Log Retention (90-day minimum)
3. 10.3: Security Event Monitoring
4. 10.4: Alerting and Escalation

---

## Question Expansion Roadmap

### Phase 1 (Q1 2026): Critical Insurance Gaps - Add 9 Questions

**NEW: Security Monitoring (4 questions)**
- Centralized logging, retention, monitoring, alerting

**EXPAND: Data Protection (+5 questions)**
- Data classification (FERPA)
- Data retention & disposal
- Encryption in transit
- Least privilege access
- Data Loss Prevention (DLP)

**Total:** 51 → 60 questions

### Phase 2 (Q3 2026): Maturity Enhancements - Add 6 Questions

**EXPAND: Incident Response (+3)**
- IR team with documented roles
- Annual tabletop exercises
- Insurance notification understanding

**EXPAND: Account Management (+1)**
- Privileged Access Management (PAM)

**EXPAND: Secure Configuration (+1)**
- Critical system network segmentation

**EXPAND: Vendor Management (+1)**
- Vendor security assessments (SOC 2)

**Total:** 60 → 66 questions

---

## Business Risks If Not Implemented

### Risk 1: Loss of Insurance Market Relevance
**Likelihood:** HIGH (70-80%)
**Impact:** SEVERE
**Timeline:** 12-18 months

**Scenario:** The Trust conducts 2026 insurance renewal with Gallagher. Carrier requires Foundation control verification. CyberPools single-score reports don't clearly identify foundation gaps. The Trust evaluates alternative providers (CAI).

### Risk 2: Inadequate Detection Coverage
**Likelihood:** MODERATE-HIGH (60-70%)
**Impact:** MODERATE
**Timeline:** 6-12 months

**Scenario:** Member applies for standalone cyber insurance. Carrier asks about SIEM/logging. Member answers "No" (not covered in assessment). Carrier quotes 40% higher premium. Member perceives assessment as incomplete.

### Risk 3: Competitive Displacement
**Likelihood:** MODERATE (40-50%)
**Impact:** MODERATE-HIGH

**Competitors:** CAI launched insurance-focused assessment July 2025. SecurityScorecard offers automated scanning. CIS offers self-assessment tools.

**CyberPools' Defensible Advantages:**
- Insurance pool relationships (The Trust, etc.)
- K-12 sector expertise (FERPA, ed-tech)
- Assessment depth (66 questions vs. competitors' 10-20)
- Professional consulting model vs. automated scans

---

## Implementation Plan

### Q4 2025 (Now - December): Foundation Work

**November 2025:**
- Finalize dual-score model design (40 hours)
- Develop 9 new questions (60 hours)
- Report template redesign (80 hours)
- Present to The Trust leadership (20 hours)

**December 2025:**
- Technology implementation (120 hours)
- Beta test with 5 member schools (40 hours)
- Communication materials (40 hours)

**Resources:** ~400 hours (1 FTE for 10 weeks)
**Cost:** ~$60K internal + $10.5K external

### Q1 2026 (January - March): Launch

**January 2026:**
- Train assessors on new model
- Launch member communication campaign
- Coordinate with The Trust on expanded requirements

**February-March 2026:**
- Begin production assessments with dual-score model
- Monitor member feedback
- Engage insurance carriers (Coalition, Cowbell, Travelers)

**Resources:** ~130 hours
**Cost:** ~$17.5K

### Q2-Q3 2026: Expansion & Refinement

- Add Phase 2 questions (6 additional)
- NIST CSF 2.0 mapping
- Annual K-12 cyber insurance report publication
- Insurance carrier partnership formalization

**Resources:** ~250 hours
**Cost:** ~$45K

---

## Total Investment & ROI

**12-Month Program Investment:**
- **Internal Labor:** ~$110K-120K (900 hours)
- **External Costs:** ~$28K
- **Total:** ~$138K-148K

**Return on Investment:**
- Maintains The Trust relationship (estimated annual value: significant)
- Prevents competitive displacement
- Enables premium pricing as "insurance-aligned" assessment
- Opens broker referral channel
- Creates thought leadership positioning

**Estimated ROI:** 3:1 to 5:1 over 24 months (revenue increase/retention of $400K-700K)

---

## Immediate Next Steps (This Week)

### 1. Leadership Decision
**Decision Required:** Approve Option 2 (Dual-Score Model) and authorize $150K investment

### 2. The Trust Engagement
**Action:** Schedule presentation with The Trust leadership (November 2025)
- Present dual-score model demo
- Show insurance alignment evidence
- Propose expanding from 7 to 12 core requirements

### 3. Resource Allocation
**Action:** Assign dedicated team
- Assessment Director: Strategy and stakeholder management
- Assessment Developers: Question development
- Software Developer: Technology implementation
- Designer: Report template redesign

### 4. Beta Recruitment
**Action:** Identify 5 friendly member schools for January 2026 beta testing

---

## Key Takeaway

**The insurance market has already made the decision to require dual-tier evaluation (foundation + maturity). CyberPools' choice is whether to align proactively (Q1 2026) or reactively (after losing competitive positioning).**

The current single-score model creates a **false sense of security** - organizations scoring 80% may be uninsurable. The dual-score model provides:
- **Accurate risk representation** for insurance underwriting
- **Clear prioritization** for member remediation efforts
- **Competitive differentiation** in the K-12 assessment market
- **Future-proof architecture** as requirements evolve

**Recommendation: Proceed with Q1 2026 dual-score model implementation immediately.**

---

## Contact

For questions about this assessment:
- cyber@cyberpools.org

For full strategic memo (12,847 words) with detailed analysis, carrier comparison matrix, and question-by-question recommendations, see comprehensive version.
