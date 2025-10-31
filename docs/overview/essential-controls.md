---
title: Cyber Essential Controls
tags:
  - Overview
  - Foundational
---

## Cyber Essential Controls (Foundational Questions)

### Overview

**Cyber Essential Controls** represent the **17 foundational questions** that are critical for cyber insurance eligibility and defense against the most prevalent threats. These controls address:

1. The most common attack vectors (credential abuse, phishing, ransomware)
2. Cyber insurance application requirements from major carriers
3. Regulatory baseline expectations (HIPAA, FERPA, state privacy laws)
4. Cost-effective, high-impact security measures suitable for organizations of all sizes

Organizations must prioritize implementation of these foundational controls to:
- Qualify for cyber insurance coverage or avoid exclusions/sub-limits
- Reduce risk of the most common and costly breaches
- Demonstrate baseline security due diligence to stakeholders, regulators, and insurers
- Establish security foundation for comprehensive maturity growth

### The Trust Requirements Mapping (Education Sector)

For education insurance pools, the **7 Trust Requirements** map to **12 foundational questions** in the assessment:

| Trust Requirement | Assessment Questions | Control Focus |
|-------------------|---------------------|---------------|
| **1. Software Security** | 1.4 | End-of-life software management |
| **2. Multi-Factor Authentication** | 2.3, 2.4, 2.5, 2.6 | MFA for VPN, cloud services, admin accounts, remote access |
| **3. Patch Management** | 4.3 | Vulnerability patching process |
| **4. Vulnerability Scanning** | 4.7 | External vulnerability scanning |
| **5. Endpoint Protection** | 5.4 | EDR/antivirus deployment |
| **6. Backup and Recovery** | 6.3, 6.4 | Air-gapped backups, backup testing |
| **7. Security Awareness** | 7.2, 7.3 | Phishing testing, security training |

### Expanded Foundational Questions (2026)

With the addition of 5 new foundational questions, the **Cyber Essential Controls** now include **17 total questions**:

#### Existing Foundational Questions (12)

**Category 1: Asset Inventory and Management**

- **1.4:** End-of-life software management (Trust Req #1)

**Category 2: Account Management and Access Control**

- **2.3:** MFA for remote access/VPN (Trust Req #2)
- **2.4:** MFA for cloud services (Microsoft 365, Google Workspace) (Trust Req #2)
- **2.5:** MFA for administrative accounts (Trust Req #2)
- **2.6:** MFA for all users accessing sensitive systems (Trust Req #2)

**Category 4: Secure Configuration and Vulnerability Management**

- **4.3:** Patch management process (Trust Req #3)
- **4.7:** External vulnerability scanning (Trust Req #4)

**Category 5: Malware Defense and Endpoint Security**

- **5.4:** EDR/antivirus deployment (Trust Req #5)

**Category 6: Data Recovery and Business Continuity**

- **6.3:** Air-gapped or offline backups (Trust Req #6)
- **6.4:** Backup testing frequency (Trust Req #6)

**Category 7: Security Awareness Training**

- **7.2:** Phishing simulation testing (Trust Req #7)
- **7.3:** Security awareness training (Trust Req #7)

#### New Foundational Questions (5)

**Category 3: Data Protection and Privacy**

- **3.5:** Privileged Access Management (PAM) Platform 🆕
  - **Insurance Pressure:** HIGH - 42% of organizations now required to have PAM for coverage
  - **Threat Justification:** 88% of breaches involve stolen credentials; privileged accounts are prime targets

**Category 4: Secure Configuration and Vulnerability Management**

- **4.14:** Centralized Logging and SIEM 🆕 *(Tiered: Foundational for organizations >500 users)*
  - **Insurance Pressure:** HIGH - Required for larger organizations and regulated industries
  - **Threat Justification:** Average 212 days to detect breaches; centralized logging essential for investigation

**Category 5: Malware Defense and Endpoint Security**

- **5.5:** Email Authentication Protocols (DMARC, SPF, DKIM) 🆕
  - **Insurance Pressure:** MODERATE-HIGH - Coalition lists email authentication on insurance checklist
  - **Threat Justification:** 84% increase in phishing emails; email remains #1 attack vector

**Category 7: Security Awareness Training**

- **7.4:** AI Acceptable Use Policy and Governance 🆕 *(Forward-looking)*
  - **Insurance Pressure:** EMERGING - Coalition offers "Affirmative AI Insurance" for AI-related events
  - **Threat Justification:** 67.4% of phishing attacks use AI; only 24% of AI projects properly secured

**Category 8: Vendor Risk Management**

- **8.8:** AI Tool Privacy and Security Vetting 🆕 *(Forward-looking)*
  - **Insurance Pressure:** EMERGING - Extends vendor risk management to AI-specific risks
  - **Threat Justification:** Vendor AI tools process sensitive data; compliance violations create breach liability

### Insurance Impact of Foundational Controls

**High Insurance Pressure (Mandatory or Near-Mandatory):**
1. Multi-Factor Authentication (Questions 2.3-2.6) - **82% of cyber insurance claims involved orgs lacking MFA**
2. Endpoint Detection and Response (Question 5.4) - **Universal requirement from all carriers**
3. Air-gapped Backups (Question 6.3) - **Required by Coalition, Corvus, Chubb**
4. Privileged Access Management (Question 3.5) - **42% of orgs required to have PAM in 2024**
5. Email Authentication (Question 5.5) - **Coalition explicitly lists DMARC/SPF/DKIM on checklist**

**Moderate-High Insurance Pressure (Strongly Preferred):**
6. Patch Management (Question 4.3) - **50% of perimeter vulnerabilities remain unpatched (Verizon DBIR)**
7. External Vulnerability Scanning (Question 4.7) - **Required quarterly by most carriers**
8. Security Awareness Training (Question 7.3) - **Human error involved in 74% of breaches**
9. Phishing Testing (Question 7.2) - **Demonstrates training effectiveness to insurers**
10. Centralized Logging/SIEM (Question 4.14) - **Required for larger organizations (>500 users)**

**Moderate Insurance Pressure (Expected for Coverage):**
11. End-of-life Software (Question 1.4) - **Unpatched legacy systems create known vulnerabilities**
12. Backup Testing (Question 6.4) - **Untested backups fail 25% of the time during ransomware recovery**

**Emerging Insurance Pressure (Forward-Looking):**
13. AI Acceptable Use Policy (Question 7.4) - **80% have AI initiatives; 43% lack policies; compliance gaps**
14. AI Tool Privacy Vetting (Question 8.8) - **Vendor AI tools create data breach exposure**

### Threat Landscape: Why These Controls Are Essential

**Universal Threats Across All Sectors (IBM X-Force 2025, Verizon DBIR 2024):**

1. **Credential Abuse (#1 Attack Vector):**

    - 30% of incidents involve account abuse
    - 88% of breaches involve stolen credentials
    - **Foundational Controls:** MFA (2.3-2.6), PAM (3.5)

2. **Ransomware (75% of Breaches):**

    - Significant increase from prior year
    - Average ransom demand: $1.5M; recovery costs: $4.5M
    - **Foundational Controls:** EDR (5.4), Air-gapped Backups (6.3), Backup Testing (6.4)

3. **Phishing and Social Engineering (84% Increase):**

    - 67.4% of phishing attacks now use AI
    - Email remains #1 initial access method
    - **Foundational Controls:** Email Authentication (5.5), Phishing Testing (7.2), Training (7.3), AI AUP (7.4)

4. **Unpatched Vulnerabilities (50% Remain Unpatched):**

    - Attackers exploit known CVEs within days of disclosure
    - End-of-life software cannot be patched (permanent vulnerability)
    - **Foundational Controls:** Patch Management (4.3), Vulnerability Scanning (4.7), EOL Software (1.4)

5. **Late Detection (212-Day Average):**

    - Organizations lack visibility into attacker lateral movement
    - Without centralized logging, incidents discovered via external notification
    - **Foundational Controls:** SIEM/Centralized Logging (4.14)

6. **AI-Enabled Attacks (442% Increase in Vishing):**

    - AI-generated phishing achieves 54% click-through rate vs. 12% for non-AI
    - Deepfake voice and video used for executive impersonation
    - Only 24% of generative AI projects properly secured
    - **Foundational Controls:** AI AUP (7.4), AI Tool Vetting (8.8)

### Implementation Priority

Organizations should implement foundational controls in the following priority order:

**Phase 1 (Immediate - 0-6 months):**
1. Multi-Factor Authentication for all users (2.3-2.6)
2. Endpoint Detection and Response deployment (5.4)
3. Air-gapped backup implementation (6.3)
4. Email authentication (SPF/DKIM/DMARC) (5.5)

**Phase 2 (High Priority - 6-12 months):**
5. Patch management process formalization (4.3)
6. External vulnerability scanning (quarterly) (4.7)
7. Security awareness training program (7.3)
8. Phishing simulation testing (7.2)
9. Privileged Access Management (PAM) platform (3.5)

**Phase 3 (Comprehensive - 12-18 months):**
10. End-of-life software inventory and replacement (1.4)
11. Backup testing procedures (6.4)
12. Centralized logging/SIEM (for organizations >500 users) (4.14)
13. AI Acceptable Use Policy (7.4)
14. AI Tool Privacy and Security Vetting (8.8)

---

<a name="category-1"></a>
