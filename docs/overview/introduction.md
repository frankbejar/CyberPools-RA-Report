---
title: Introduction
tags:
  - Overview
---

# CyberPools Comprehensive Cybersecurity Risk Assessment Questionnaire
## Sector-Neutral Framework - Version 2.0 (2026)

**Document Version:** 2.0
**Effective Date:** January 2026 (Proposed)
**Total Questions:** 65 (52 existing + 13 new)
**Foundational Questions:** 17 (12 existing + 5 new)
**Assessment Categories:** 9

---

## Table of Contents

1. [Introduction: Cyber Risk Assessment and Methodology](#introduction)
2. [Cyber Essential Controls (Foundational Questions)](#cyber-essential-controls)
3. [Category 1: Asset Inventory and Management](#category-1)
4. [Category 2: Account Management and Access Control](#category-2)
5. [Category 3: Data Protection and Privacy](#category-3)
6. [Category 4: Secure Configuration and Vulnerability Management](#category-4)
7. [Category 5: Malware Defense and Endpoint Security](#category-5)
8. [Category 6: Data Recovery and Business Continuity](#category-6)
9. [Category 7: Security Awareness Training and Education](#category-7)
10. [Category 8: Third-Party and Vendor Risk Management](#category-8)
11. [Category 9: Incident Response and Recovery](#category-9)
12. [Appendix: Citations and References](#citations)

---

<a name="introduction"></a>
## Introduction: Cyber Risk Assessment and Methodology

### What is the CyberPools Cyber Risk Assessment?

The CyberPools Cybersecurity Risk Assessment is a comprehensive evaluation tool designed to measure an organization's cybersecurity posture against industry-leading frameworks and cyber insurance requirements.

**1. Insurance Alignment:**

- Maps directly to cyber insurance application requirements from major carriers
    - Coalition, Chubb, Corvus
- Identifies gaps that could impact:
    - Insurance eligibility
    - Coverage limits
    - Premium rates
- Provides insurance-ready documentation of security controls
- Demonstrates due diligence and risk management maturity to underwriters

**2. Risk Quantification:**

- **65 security controls** across **9 categories** covering the complete cybersecurity lifecycle
- Risk scores based on:
    - **Control Rating**: Fully / Partially / Not Implemented
    - **Impact Rating**: Low / Moderate / High
- **Dual scores** provided:
    - **Foundation Score** - insurance-critical controls
    - **Comprehensive Score** - full security maturity
- Enables tracking of risk reduction over time through annual assessments

**3. Framework Compliance:**

- **NIST Cybersecurity Framework (CSF) 2.0**
    - Sector-agnostic standard
    - Functions: Govern, Identify, Protect, Detect, Respond, Recover
- **CIS Controls v8**
    - Prioritized security controls for all organization sizes
- **NIST AI Risk Management Framework**
    - Voluntary guidance for AI governance
- **Sector-specific regulations**
    - FERPA, HIPAA, state privacy laws

**4. Actionable Remediation:**

- Identifies high-risk gaps requiring immediate attention
- Provides prioritized recommendations based on:
    - Insurance requirements
    - Current threat landscape
- Delivers sector-specific guidance:
    - Education (K-12/Higher Ed)
    - Healthcare
    - Religious/Nonprofit
    - General organizations
- Supports integration with **CyberPools Cyber Toolkit** services:
    - Vulnerability scanning
    - Phishing simulations
    - vCISO

### Assessment Methodology

The CyberPools Risk Assessment employs a **dual-score model** to differentiate between insurance-critical baseline controls and comprehensive security maturity:

#### Foundation Score (Insurance-Critical Controls)

**Purpose:** Measures implementation of **17 foundational questions** that are:
- Required or strongly preferred by cyber insurance carriers
- Address the most common and costly attack vectors (credential abuse, ransomware, phishing)
- Represent baseline security hygiene expected of all organizations

**Scoring:**
- Foundation Score = (Points Earned / Total Possible Points) × 100%
- Each foundational question scored: Control Rating (1/3/5) × Impact Rating (1/3/5)
- Minimum acceptable Foundation Score varies by insurance pool requirements

**Insurance Impact:**
- Foundation Score directly influences insurance eligibility and premium rates
- Gaps in foundational controls may result in coverage exclusions or sub-limits
- Annual improvement in Foundation Score demonstrates risk reduction to insurers

#### Comprehensive Score (Full Security Maturity)

**Purpose:** Measures implementation of **all 65 questions** across the cybersecurity lifecycle:
- Includes foundational controls (17 questions)
- Plus comprehensive maturity indicators (48 questions)
- Demonstrates advanced security operations and defense-in-depth

**Scoring:**
- Comprehensive Score = (Points Earned / Total Possible Points) × 100%
- Same formula: Control Rating (1/3/5) × Impact Rating (1/3/5)
- Reflects organization's overall cybersecurity maturity

**Value:**
- Identifies opportunities for continuous improvement beyond insurance minimums
- Benchmarks against peer organizations in similar sectors
- Guides multi-year security roadmap and budget planning

#### Risk Rating Calculation

**Control Rating (Implementation Level):**
- **1 (Fully Implemented):** Control is comprehensively deployed, documented, and tested
- **3 (Partially Implemented):** Control exists but has gaps in coverage, documentation, or testing
- **5 (Not Implemented):** Control is absent or planning stage only

**Impact Rating (Assigned per Question):**
- **1 (Low Impact):** Limited consequence if control fails; affects single system or small user group
- **3 (Moderate Impact):** Significant consequence if control fails; affects multiple systems or broader operations
- **5 (High Impact):** Severe consequence if control fails; affects entire organization, critical systems, or sensitive data

**Risk Score per Question:**
```
Risk Score = Control Rating (1/3/5) × Impact Rating (1/3/5)
```

**Risk Level Interpretation:**
- **0-5:** Low Risk (green) - Control well-implemented for impact level
- **6-15:** Moderate Risk (yellow) - Control partially implemented; improvement needed
- **16-25:** High Risk (red) - Critical gap requiring immediate attention

**Example:**
- Question: "Has the organization implemented MFA for all users?"
- Impact Rating: **5 (High)** - credential abuse is #1 attack vector
- Organization Answer: **3 (Partially Implemented)** - MFA on VPN only, not email/cloud
- Risk Score: 3 × 5 = **15 (Moderate Risk)**
- Recommendation: Expand MFA to all systems to reduce risk score to 5 (Low Risk)

### Sector-Neutral Design

The CyberPools assessment is **sector-agnostic** by design, serving organizations across:

**Education Sector:**
- K-12 school districts, colleges, universities
- Compliance emphasis: FERPA (student privacy), COPPA (under-13 online privacy)
- Common technology: Google Workspace for Education, Microsoft 365 Education, student information systems (SIS), learning management systems (LMS)

**Healthcare Sector:**
- Hospitals, clinics, blood banks, medical practices
- Compliance emphasis: HIPAA Security Rule (2025 updates), HITECH Act
- Common technology: Electronic health records (EHR), medical devices, lab systems, PACS imaging

**Religious/Nonprofit Sector:**
- Churches, dioceses, ministries, faith-based organizations, charitable nonprofits
- Compliance emphasis: State privacy laws, PCI DSS (payment processing), donor trust
- Common technology: Donor management systems, accounting software, Microsoft 365/Google Workspace

**General Organizations:**
- Municipalities, government agencies, critical infrastructure, businesses
- Compliance emphasis: SOX (if applicable), GDPR, CCPA, state data breach laws, industry-specific regulations
- Common technology: Cloud infrastructure (AWS/Azure/GCP), financial systems, operational technology (OT)

**Universal Security Principles:**

Regardless of sector, all organizations must protect the **CIA triad**:
- **Confidentiality:** Prevent unauthorized access to sensitive data (PII, PHI, education records, financial data)
- **Integrity:** Ensure data accuracy and prevent unauthorized modification
- **Availability:** Maintain access to systems and data when needed (resilience against ransomware, DDoS)

The assessment questions use sector-neutral language, with sector-specific context and examples provided in guidance materials.

### Assessment Process

**1. Preparation (Organization):**
- Review assessment questionnaire and gather documentation (policies, vendor contracts, system inventories)
- Identify stakeholders: IT leadership, security team, compliance officer, executive sponsor
- Schedule assessment interview (typically 2-4 hours depending on organization size)

**2. Assessment Interview (CyberPools Assessor):**
- Trained assessor conducts structured interview with organization's stakeholders
- Reviews evidence and documentation for each control
- Assigns control ratings (Fully/Partially/Not Implemented) based on evidence
- Documents notes, gaps, and observations

**3. Scoring and Analysis (CyberPools):**
- Calculate Foundation Score and Comprehensive Score
- Identify high-risk gaps (risk score ≥16)
- Compare to insurance requirements and peer benchmarks
- Generate prioritized recommendations

**4. Report Delivery (Organization):**
- Receive comprehensive PDF report including:
  - Executive summary with Foundation and Comprehensive scores
  - Category-by-category analysis
  - High-risk findings requiring immediate attention
  - Insurance compliance table (mapping to carrier requirements)
  - Remediation roadmap with prioritized recommendations
  - Sector-specific implementation guidance

**5. Continuous Improvement:**
- Address high-risk findings (typically 6-12 month remediation cycle)
- Implement recommended controls and policies
- Leverage CyberPools Cyber Toolkit services (vulnerability scanning, phishing simulations, vCISO consulting)
- Annual re-assessment to measure improvement and maintain insurance compliance

### Alignment with Industry Frameworks

**NIST Cybersecurity Framework (CSF) 2.0:**
- **Govern (GV):** Category 1 (Asset Management), Category 8 (Vendor Risk), AI governance questions
- **Identify (ID):** Category 1 (Asset Inventory), Category 3 (Data Protection), Category 4 (Vulnerability Management)
- **Protect (PR):** Category 2 (Access Control), Category 3 (Data Protection), Category 5 (Endpoint Security), Category 7 (Training)
- **Detect (DE):** Category 4 (Logging/SIEM), Category 5 (EDR), Category 9 (Incident Detection)
- **Respond (RS):** Category 9 (Incident Response)
- **Recover (RC):** Category 6 (Data Recovery, Business Continuity)

**CIS Controls v8:**
- **IG1 (Basic Cyber Hygiene):** Foundational questions cover essential controls for all organizations
- **IG2 (Intermediate Security):** Comprehensive questions address controls for organizations with more resources
- **IG3 (Advanced Security):** Advanced maturity questions (SIEM, PAM, incident detection metrics)

**NIST AI Risk Management Framework:**
- **Govern:** AI acceptable use policy (Question 7.4)
- **Map:** AI tool risk assessment (Question 8.8)
- **Measure:** Ongoing vendor monitoring for AI tools
- **Manage:** Implementation and enforcement of AI governance

---

<a name="cyber-essential-controls"></a>
