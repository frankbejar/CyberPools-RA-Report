# 2026 Risk Assessment: Critical Control Framework & Question Set

**Date:** November 19, 2025
**Version:** 6.2
**Status:** Final - Complete Revision
**Purpose:** Complete 2026 Risk Assessment framework with evidence-based question set and framework alignment

---

## Framework Alignment

This assessment maps to two authoritative security frameworks:

- **CIS Controls v8.1 IG1:** [https://www.cisecurity.org/controls/v8](https://www.cisecurity.org/controls/v8) - 85%+ coverage of IG1 safeguards
- **NIST Cybersecurity Framework 2.0:** [https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework) - Released February 2024

---

## Document Overview

**Total Questions: 57**
- **TIER 1A:** 10 control questions (insurance-critical, coverage-impacting)
- **TIER 1B:** 7 control questions (foundational defense-in-depth, emerging requirements)
- **Comprehensive:** 40 control questions (defense-in-depth and maturity)

---

## TIER DEFINITIONS

### TIER 1A: Insurance Requirements (Coverage-Impacting)
Near-universal carrier requirements (95%+ prevalence). Missing these control questions impacts ability to obtain coverage or results in significant restrictions/sub-limits.

**Criteria:**
- Explicit carrier application requirement across major carriers (Chubb, AIG, Travelers, The Trust)
- Evidence of coverage denial or restrictions when absent
- Universal or near-universal prevalence in underwriting

### TIER 1B: Foundational Defense-in-Depth (Emerging Requirements)
Critical defense layers that are emerging insurance requirements. Used for rate optimization and preferred coverage terms, but absence does not block coverage eligibility. These control questions provide foundational security practices.

**Criteria:**
- Asked by 50-95% of carriers
- Used for rate optimization (premium discounts/penalties)
- Strong threat validation but not yet coverage-blocking
- May become TIER 1A in future

---

## TIER 1A CONTROLS (10 Questions)

| Q# | Question Text | Impact | CIS v8.1 IG1 | NIST CSF 2.0 |
|----|---------------|--------|--------------|--------------|
| 1.4 | End-of-life software removed/isolated | 5 | 2.2, 4.1, 7.1 | ID.RA, PR.IP |
| 2.4 | MFA for remote access/VPN | 5 | 6.3, 6.4 | PR.AA, PR.PT |
| 2.5 | MFA for cloud services | 5 | 6.3, 6.4 | PR.AA, PR.PT |
| 2.6 | MFA for administrative accounts | 5 | 6.3, 6.5 | PR.AA, PR.PT |
| 2.7 | MFA for critical systems/data | 5 | 6.3 | PR.AA, PR.PT |
| 4.2 | Patch management (OS/apps/Network Infrastructure, 30/7 days critical) | 5 | 7.1, 7.2, 7.3, 12.1 | PR.IP, DE.CM, RS.MI |
| 4.5 | External vulnerability scanning (quarterly) | 5 | 7.1 | ID.RA, DE.CM |
| 5.3 | EDR/MDR deployment to all endpoints (end user devices and servers) | 5 | 10.1 | DE.CM, DE.AE, RS.AN |
| 6.2 | Air-gapped/immutable backups with encryption (WORM if SaaS) | 5 | 11.3, 11.4 | PR.IP, PR.DS, RC.RP |
| 6.3 | Backup testing frequency x2 per year | 5 | 11.1 | PR.IP, RC.RP |

**TIER 1A Rationale:**
These 10 control questions represent near-universal carrier requirements with explicit coverage implications. Missing any single control question creates material insurance risk, as evidenced by Hamilton City's $5M claim denial for incomplete MFA [35] and industry-wide carrier application requirements [1][27][30][32][34].

---

## TIER 1B CONTROLS (7 Questions)

| Q# | Question Text | Impact | CIS v8.1 IG1 | NIST CSF 2.0 |
|----|---------------|--------|--------------|--------------|
| 2.9 | Access reviews and privileged credential management (minimum semi-annual review of all accounts, privileges/roles, and administrative credential access) | 5 | 5.1, 5.3, 5.4, 6.8 | PR.AC, PR.PT, DE.CM |
| 3.2 | Data encryption at rest (including full disk encryption) | 5 | 3.6 | PR.DS, PR.PT |
| 3.3 | Data retention and secure deletion | 5 | 3.4, 3.5 | PR.DS, PR.IP |
| 5.4 | Email authentication (SPF/DKIM/DMARC) | 5 | 9.1 | PR.PT, DE.AE |
| 7.2 | Security awareness training frequency (annual minimum, quarterly preferred) | 5 | 14.1, 14.2, 14.3, 14.4, 14.5 | PR.AT |
| 7.3 | Phishing simulation testing (quarterly minimum) | 5 | 14.2 | PR.AT, DE.AE |
| 9.1 | Documented cyber incident response plan (reviewed/revised annually) | 5 | 17.1, 17.2, 17.3 | RS.MA, RS.RP |

**TIER 1B Rationale:**
These 7 control questions represent foundational defense-in-depth practices that are emerging cyber carrier requirements. Used by carriers for rate optimization (premium discounts 10-15%) rather than coverage eligibility [9]. Strong threat validation but not yet coverage-blocking. Expected to migrate toward TIER 1A prevalence over next 2-3 years.

---

## COMPREHENSIVE QUESTIONS BY CATEGORY

### Category 1: Inventory and Control of Assets

**What it is:** Knowing what you have (hardware, software, cloud services) to protect it.

**Why it matters:** Can't protect what you don't know exists. 72% of breaches involve unknown/shadow IT assets [19]. Foundation for all other controls.

| Q# | Question Text | Impact | TIER | CIS v8.1 | NIST CSF 2.0 |
|----|---------------|--------|------|----------|--------------|
| 1.1 | Establish and maintain a comprehensive enterprise asset inventory | 5 | Comp | 1.1, 1.2 | ID.AM |
| 1.2 | Address unauthorized assets | 5 | Comp | 1.2 | DE.CM |
| 2.1 | Establish and maintain an up-to-date software inventory | 3 | Comp | 2.1 | ID.AM |
| 2.3 | Address unauthorized software/services (shadow IT) | 3 | Comp | 2.3 | ID.AM, DE.CM |
| 1.3 | Cloud services/SaaS inventory | 3 | Comp | 2.1, 15.1 | ID.AM, ID.SC |
| 1.4 | End-of-life software removed/isolated | 5 | T1A | 2.2, 4.1, 7.1 | ID.RA, PR.IP |

---

### Category 2: Account Management

**What it is:** Controlling who has access to what, how they authenticate, and lifecycle management.

**Why it matters:** Identity compromise = 24% of breaches as initial action (Verizon DBIR 2024). Credential theft = primary attack vector. Proper account management prevents unauthorized access and lateral movement.

| Q# | Question Text | Impact | TIER | CIS v8.1 | NIST CSF 2.0 |
|----|---------------|--------|------|----------|--------------|
| 2.1 | Account inventory (user, administrative, service, and system accounts) | 5 | Comp | 5.1 | ID.AM, PR.AC |
| 2.2 | Onboarding/position change procedures | 3 | Comp | 6.1 | PR.AC, PR.IP |
| 2.3 | Password policy (12+ character minimum, complexity requirements) | 3 | Comp | 5.2 | PR.AC, PR.AA |
| 2.4 | MFA for remote access/VPN | 5 | T1A | 6.3, 6.4 | PR.AA, PR.PT |
| 2.5 | MFA for cloud services (email, data repositories/libraries, collaboration platforms, data processing platforms) | 5 | T1A | 6.3, 6.4 | PR.AA, PR.PT |
| 2.6 | MFA for administrative accounts | 5 | T1A | 6.3, 6.5 | PR.AA, PR.PT |
| 2.7 | MFA for critical systems/data (all other systems not covered by other MFA questions - example: on-premise applications, QuickBooks, etc.) | 5 | T1A | 6.3 | PR.AA, PR.PT |
| 2.8 | Privileged account separation (admin accounts) | 5 | Comp | 5.4 | PR.AC, PR.PT |
| 2.9 | Access reviews and privileged credential management (minimum semi-annual review of all accounts, privileges/roles, and administrative credential access) | 5 | T1B | 5.1, 5.3, 5.4, 6.8 | PR.AC, PR.PT, DE.CM |
| 2.10 | Disable dormant accounts (accounts that have not been used for at least 45 days) | 5 | Comp | 5.3 | PR.AC, DE.CM |
| 2.11 | Account lockout policy (brute force protection) | 3 | Comp | 5.2 | PR.AC, PR.AA |
| 2.12 | Principle of least privilege (POLP) for all accounts | 5 | Comp | 5.4, 6.8 | PR.AC, PR.PT |
| 2.13 | Separation of duties | 3 | Comp | 5.4 | PR.AC |
| 2.14 | Offboarding procedures | 5 | Comp | 6.2 | PR.AC, PR.IP |

---

### Category 3: Data Protection

**What it is:** Protecting sensitive data through encryption, classification, retention, and access controls.

**Why it matters:** Data breach average cost = $4.88M [2b]. Encryption and proper handling reduce breach impact and regulatory penalties.

| Q# | Question Text | Impact | TIER | CIS v8.1 | NIST CSF 2.0 |
|----|---------------|--------|------|----------|--------------|
| 3.1 | Sensitive data inventory with classification - example: proprietary, PHI, FERPA, Confidential (on-premise and cloud) | 3 | Comp | 3.1, 3.2 | ID.AM, PR.DS |
| 3.2 | Data encryption at rest (including full disk encryption) | 5 | T1B | 3.6 | PR.DS, PR.PT |
| 3.3 | Data retention and secure deletion | 5 | T1B | 3.4, 3.5 | PR.DS, PR.IP |
| 3.5 | Data classification system | 3 | Comp | 3.2 | ID.AM, PR.DS |
| 3.7 | Data encryption in transit (HTTPS/SSH) | 5 | Comp | 3.3 | PR.DS |

---

### Category 4: Secure Configuration of Enterprise Assets

**What it is:** Hardening systems, networks, and infrastructure to prevent exploitation.

**Why it matters:** Misconfigurations = 23% of breaches [19]. Proper configuration reduces attack surface and prevents common exploitation paths. Network segmentation limits lateral movement.

| Q# | Question Text | Impact | TIER | CIS v8.1 | NIST CSF 2.0 |
|----|---------------|--------|------|----------|--------------|
| 4.1 | Firewall deployment with IDS and/or IPS at the perimeter of the network | 5 | Comp | 4.4, 4.5 | PR.AC, PR.PT, DE.AE |
| 4.2 | Patch management (OS/apps/Network Infrastructure, 30/7 days critical) | 5 | T1A | 7.1, 7.2, 7.3, 12.1 | PR.IP, DE.CM, RS.MI |
| 4.4 | Wireless security (WPA2/3, guest isolation) | 5 | Comp | 4.1 | PR.AC, PR.DS |
| 4.5 | External vulnerability scanning (quarterly) | 5 | T1A | 7.1 | ID.RA, DE.CM |
| 4.6 | Network segmentation (Ops Network/HR Network/Server network) | 3 | Comp | 12.1 | PR.AC, PR.DS, PR.PT |
| 4.7 | NTP (time synchronization) | 1 | Comp | 8.1 | PR.PT, DE.AE |
| 4.8 | Change management process | 1 | Comp | 4.1 | PR.IP, PR.MA |
| 4.9 | Centralized logging with a minimum 90-day retention | 3 | Comp | 8.1, 8.2, 8.3 | DE.AE, DE.CM |
| 4.10 | Cloud security posture management (CSPM - Microsoft Secure Score or Google Security Dashboard) | 5 | Comp | 3.12, 15.1 | ID.RA, PR.DS |
| 4.11 | Physical security controls (locks, badges) | 3 | Comp | - | PR.AC, PR.PT |
| 4.12 | Web application security (WAF or related controls to protect websites and/or web applications) | 5 | Comp | 16.11 | PR.IP, PR.DS |
| 4.14 | Network device secure configuration (hardening) | 5 | Comp | 4.1, 4.2, 12.1 | PR.IP, PR.AC |

---

### Category 5: Malware Defense

**What it is:** Detecting and blocking malware, phishing, and malicious communications.

**Why it matters:** Ransomware = 24% of breaches [19]. Organizations in certain sectors face median ransom payments among the highest recorded [2c]. Malware defense blocks attacks before encryption/data theft.

| Q# | Question Text | Impact | TIER | CIS v8.1 | NIST CSF 2.0 |
|----|---------------|--------|------|----------|--------------|
| 5.1 | Email security gateway (spam filter) | 3 | Comp | 9.1 | PR.PT, DE.CM |
| 5.2 | Web filtering and/or DNS filtering services | 3 | Comp | 9.2 | PR.PT, DE.CM |
| 5.3 | EDR/MDR deployment to all endpoints (end user devices and servers) | 5 | T1A | 10.1 | DE.CM, DE.AE, RS.AN |
| 5.4 | Email authentication (SPF/DKIM/DMARC) | 5 | T1B | 9.1 | PR.PT, DE.AE |

---

### Category 6: Data Recovery

**What it is:** Ensuring ability to recover from ransomware, disasters, or system failures.

**Why it matters:** 96% ransomware targets backups [2d]. Organizations paying ransom recover only 16% of data [2e]. Protected, tested backups = only reliable recovery path.

| Q# | Question Text | Impact | TIER | CIS v8.1 | NIST CSF 2.0 |
|----|---------------|--------|------|----------|--------------|
| 6.2 | Air-gapped/immutable backups with encryption (WORM if SaaS) | 5 | T1A | 11.3, 11.4 | PR.IP, PR.DS, RC.RP |
| 6.3 | Backup testing frequency x2 per year | 5 | T1A | 11.1 | PR.IP, RC.RP |

---

### Category 7: Security Awareness

**What it is:** Training users to recognize and report threats, particularly phishing.

**Why it matters:** 68% of breaches involve human element [19]. Trained users = last line of defense. Phishing = most common initial access vector.

| Q# | Question Text | Impact | TIER | CIS v8.1 | NIST CSF 2.0 |
|----|---------------|--------|------|----------|--------------|
| 7.1 | Documented security awareness program (roles, curriculum, schedule) | 5 | Comp | 14.1 | PR.AT |
| 7.2 | Security awareness training frequency (annual minimum, quarterly preferred) | 5 | T1B | 14.1, 14.2, 14.3, 14.4, 14.5 | PR.AT |
| 7.3 | Phishing simulation testing (quarterly minimum) | 5 | T1B | 14.2 | PR.AT, DE.AE |

---

### Category 8: Vendor Management

**What it is:** Managing security risks from third-party vendors with access to systems/data.

**Why it matters:** 30% breaches involve third parties [19]. Vendor compromise = backdoor into your organization. Proper vendor management prevents supply chain attacks.

| Q# | Question Text | Impact | TIER | CIS v8.1 | NIST CSF 2.0 |
|----|---------------|--------|------|----------|--------------|
| 8.1 | Vendor inventory | 3 | Comp | 15.1 | ID.AM, ID.SC |
| 8.2 | Security questionnaires/attestations (SOC 2/ISO) | 3 | Comp | 15.1 | ID.SC |
| 8.4 | Critical vendor access reviews | 5 | Comp | 15.1 | ID.SC, PR.AC |

---

### Category 9: Incident Response

**What it is:** Documented processes and team for detecting, responding to, and recovering from cyber incidents.

**Why it matters:** IR plan saves $2.03M per breach [2b]. Tested IR teams contain breaches 74 days faster [2b]. Rapid response = reduced impact.

| Q# | Question Text | Impact | TIER | CIS v8.1 | NIST CSF 2.0 |
|----|---------------|--------|------|----------|--------------|
| 9.1 | Documented cyber incident response plan (reviewed/revised annually) | 5 | T1B | 17.1, 17.2, 17.3 | RS.MA, RS.RP |
| 9.2 | CIRP team with defined roles | 3 | Comp | 17.1 | RS.MA, RS.RP |
| 9.3 | CIRP testing frequency (tabletops) | 5 | Comp | 17.3 | RS.MA |

---

### Category 10: Information Security Policies

**What it is:** Documented policies governing acceptable use, remote work, vendor management, and BYOD.

**Why it matters:** Policies establish security expectations, enable enforcement, and demonstrate due diligence for compliance and insurance.

| Q# | Question Text | Impact | TIER | CIS v8.1 | NIST CSF 2.0 |
|----|---------------|--------|------|----------|--------------|
| 10.1 | Information security policies (documented, deployed, annually reviewed - any general policies - extra points for the below) | 1 | Comp | - | GV.PO, GV.RM |
| 10.2 | Acceptable use policy | 1 | Comp | - | GV.PO |
| 10.3 | Remote work security policy | 1 | Comp | - | GV.PO |
| 10.4 | Vendor Management policy | 1 | Comp | 15.1 | GV.PO, ID.SC |
| 10.5 | Bring your own device (BYOD) policy | 1 | Comp | - | GV.PO |

---

## NIST CSF 2.0 FUNCTION REFERENCE

**Govern (GV):** Organizational context, risk management strategy, roles/responsibilities, policies, oversight

**Identify (ID):** Asset management, risk assessment, improvement

**Protect (PR):** Identity management, awareness training, data security, platform security, technology infrastructure resilience

**Detect (DE):** Continuous monitoring, adverse event analysis

**Respond (RS):** Incident management, analysis, mitigation, reporting, communication

**Recover (RC):** Incident recovery planning, improvements, communications

---

## CIS CONTROLS v8.1 IG1 COVERAGE SUMMARY

**Total IG1 Safeguards:** 56
**Covered by 2026 RA:** 48 safeguards (86% coverage)

**Coverage by Control:**
- Control 1 (Enterprise Assets): 100% (2/2)
- Control 2 (Software Assets): 100% (3/3)
- Control 3 (Data Protection): 100% (6/6)
- Control 4 (Secure Configuration): 71% (5/7)
- Control 5 (Account Management): 100% (4/4)
- Control 6 (Access Control): 100% (5/5)
- Control 7 (Vulnerability Management): 75% (3/4)
- Control 8 (Audit Logs): 100% (3/3)
- Control 9 (Email/Web Protections): 100% (2/2)
- Control 10 (Malware Defense): 100% via EDR (3/3 superseded)
- Control 11 (Data Recovery): 75% (3/4)
- Control 12 (Network Infrastructure): 100% (1/1)
- Control 14 (Security Awareness): 100% consolidated (8/8 addressed)
- Control 15 (Service Provider): 100% (1/1)
- Control 17 (Incident Response): 100% (3/3)

**Safeguards NOT Covered (by design):**
- 4.6: Infrastructure-as-code management (IG2/IG3 control, not applicable to most small/mid-size organizations)
- 7.4: Automated application patching (covered via 7.3, consolidated)
- 8.3: Adequate log storage (covered by 8.2 minimum 90-day retention)
- 10.1, 10.2, 10.3: Legacy AV controls (superseded by EDR/MDR in 5.3)
- 11.2: Automated backup process (implied by 11.3/11.4 requirements)

---

## SUMMARY

**Total Questions:** 57
- Category 1: 6 questions
- Category 2: 14 questions
- Category 3: 5 questions
- Category 4: 12 questions
- Category 5: 4 questions
- Category 6: 2 questions
- Category 7: 3 questions
- Category 8: 3 questions
- Category 9: 3 questions
- Category 10: 5 questions

**TIER Distribution:**
- TIER 1A: 10 questions (18%)
- TIER 1B: 7 questions (12%)
- Comprehensive: 40 questions (70%)

**Framework Coverage:**
- CIS Controls v8.1 IG1: 86% (48 of 56 safeguards)
- NIST CSF 2.0: All 6 functions represented

---

**Document Version History:**
- v6.0: Initial 2026 question set
- v6.1: Categories 1-3 refinement (November 17, 2025)
- v6.2: Complete revision - All categories updated, PAM merged, frameworks streamlined (November 19, 2025)
