---
title: Category 8 - Third-Party and Vendor Risk Management
tags:
  - Category 8
  - Foundational
  - New
  - High Impact
  - Moderate Impact
---

## Category 8: Third-Party and Vendor Risk Management

**Overview:**

Third-party and vendor risk management addresses cybersecurity risks introduced through external organizations that access organizational systems, data, or provide critical services. Supply chain attacks and third-party breaches have doubled in recent years, making vendor risk management a critical security control.

**Importance:**

**Third-Party Breach Epidemic:**

- **Third-party breaches doubled from 2022 to 2024** (Verizon DBIR 2024)
- **54% of organizations experienced third-party data breach** in past year (Ponemon 2024)
- High-profile incidents: SolarWinds, Kaseya, MOVEit, demonstrate systemic third-party risk

**Insurance Requirements:**

- Cyber insurers increasingly require **vendor risk management programs**
- **Vendor security certifications** (SOC 2, ISO 27001) may be required for critical vendors
- **Vendor breach notification clauses** in contracts required by insurers

**Sector-Agnostic Relevance:**

- **All sectors** rely on third-party vendors (IT services, cloud providers, SaaS applications, MSPs)
- Vendor risk applies universally across Education, Healthcare, Religious/Nonprofit, General organizations
- **AI vendors** introduce new risks requiring specialized vetting (Question 8.8)

**Category 8 includes 8 questions:**

- Question 8.1: Third-Party Vendor Inventory
- Question 8.2: Vendor Security Assessment Process
- Question 8.3: Vendor Contract Security Requirements
- Question 8.4: Vendor Access Management
- Question 8.5: Vendor Off-boarding Process
- Question 8.6: Third-Party Security Certifications and Assessments 🆕
- Question 8.7: Vendor Continuous Monitoring and Incident Notification 🆕
- Question 8.8: AI Tool Privacy and Security Vetting 🔑 FOUNDATIONAL 🆕

---

### Question 8.1: Third-Party Vendor Inventory

**Question Text:**
Does the organization maintain an inventory of all third-party vendors with access to organizational systems, data, or networks?

**Response Options:**

- Fully implemented - comprehensive vendor inventory with risk ratings
- Partially implemented - informal vendor list, incomplete information
- Not implemented - no vendor inventory maintained

**Impact Rating:** Moderate (3)

**Foundational:** No (but foundational for vendor risk management program)

**Control Description:**

A vendor inventory provides visibility into all third-party relationships and serves as the foundation for vendor risk management. Effective inventories include:

**Inventory Components:**

- **Vendor Information:** Vendor name, primary contact, contract details
- **Access Level:** What systems/data does vendor access? (network, applications, sensitive data)
- **Service Description:** What services does vendor provide? (cloud hosting, SaaS, managed services, professional services)
- **Risk Rating:** High/Medium/Low risk based on access level, data sensitivity, criticality
- **Security Status:** SOC 2 report on file? Contract security requirements met? Last assessment date?

**Vendor Categories:**

- **IT/Cloud Providers:** AWS, Azure, Google Cloud, managed service providers
- **SaaS Applications:** Google Workspace, Microsoft 365, student information systems, donor management systems
- **Professional Services:** IT consultants, auditors, penetration testers
- **Infrastructure Vendors:** ISPs, telecommunications, physical security

**Insurance Rationale (Universal):**

**Vendor Visibility Requirement:**

- Cyber insurers may request vendor inventory during application/renewal
- Demonstrates organizational awareness of third-party attack surface
- High-risk vendors (those with data access) may require additional scrutiny

**Compliance Alignment:**

- **HIPAA:** Business Associate Agreements (BAAs) require knowing all vendors with PHI access
- **PCI DSS:** Service provider inventory required for organizations handling payment cards
- **SOC 2:** Vendor management controls require vendor inventory

**Threat Landscape Justification:**

**Third-Party Breaches:**

- **Third-party breaches doubled** from 2022 to 2024
- Organizations without vendor inventories cannot assess third-party risk exposure
- Inventory enables prioritization of vendor security assessments

**Supply Chain Attacks:**

- **SolarWinds (2020):** 18,000 organizations compromised via supply chain attack
- **Kaseya (2021):** 1,500 organizations ransomwared via MSP compromise
- Knowing which vendors have access enables rapid response to vendor incidents

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Common Vendors:** Student information systems (PowerSchool, Infinite Campus), learning platforms (Canvas, Google Classroom), cloud providers (Google, Microsoft)
- **FERPA Consideration:** Vendors with student data access must comply with FERPA; inventory identifies these vendors
- **Practical Implementation:** Spreadsheet or GRC platform (OneTrust, ServiceNow) tracking vendor relationships

**Healthcare:**

- **Common Vendors:** EHR vendors (Epic, Cerner), medical device vendors, billing services, cloud providers
- **HIPAA Requirement:** Business Associate Agreements required for all vendors with PHI access; inventory ensures all BAAs obtained
- **High-Risk Focus:** EHR vendors, billing services have extensive PHI access

**Religious/Nonprofit:**

- **Common Vendors:** Donor management systems (Salesforce Nonprofit Cloud, Blackbaud), accounting software (QuickBooks), cloud providers
- **Donor Data Protection:** Identify vendors with donor data access
- **Budget-Conscious:** Many nonprofits use free/discounted SaaS; inventory tracks these relationships

**General Organizations:**

- **Industry-Specific Vendors:** Varies by industry (payment processors for retail, logistics for manufacturing)
- **Compliance Drivers:** PCI DSS, SOC 2, ISO 27001 require vendor inventory
- **Cloud-First Organizations:** Extensive SaaS usage requires comprehensive inventory

**Citations:**

- CIS Controls v8: Control 15.1 (Establish and Maintain an Inventory of Service Providers)
- NIST CSF 2.0: ID.SC-1 (Cyber supply chain risk management processes are identified)
- **Verizon DBIR 2024:** Third-party breaches doubled from 2022 to 2024
- **Ponemon Third-Party Risk Study 2024:** 54% of organizations experienced third-party breach
- **HIPAA:** Business Associate requirements (45 CFR § 164.308(b))
- **PCI DSS 4.0:** Requirement 12.8 - Manage service providers

---

### Question 8.2: Vendor Security Assessment Process

**Question Text:**
Does the organization conduct security assessments of third-party vendors before granting access to systems or data?

**Response Options:**

- Fully implemented - formal assessment process with standardized questionnaires, risk-based approach
- Partially implemented - informal assessments, inconsistent process
- Not implemented - no vendor security assessments conducted

**Impact Rating:** High (5)

**Foundational:** No (but critical control)

**Control Description:**

Vendor security assessments evaluate third-party security posture before establishing relationships. Effective assessment processes include:

**Assessment Methods:**

- **Security Questionnaires:** Standardized questionnaires (SIG, CAIQ, custom) covering security controls, compliance, incident history
- **Documentation Review:** Review SOC 2 reports, ISO 27001 certificates, penetration test results, security policies
- **Risk-Based Approach:** High-risk vendors (data access, critical services) receive more rigorous assessment than low-risk vendors
- **Vendor Interviews:** For critical vendors, conduct interviews with vendor security teams

**Assessment Criteria:**

- **Security Controls:** Encryption, MFA, access controls, incident response, backup/DR
- **Compliance:** HIPAA, PCI DSS, FERPA, SOC 2, ISO 27001 certifications
- **Incident History:** Has vendor experienced breaches? How were they handled?
- **Financial Stability:** Is vendor financially viable long-term?
- **Data Handling:** Where is data stored? Who has access? Data residency requirements met?

**Assessment Workflow:**
1. **Pre-Contracting:** Assess vendor before signing contract
2. **Risk Rating:** Assign high/medium/low risk rating
3. **Approval:** Vendor approved, conditionally approved (with remediation), or rejected
4. **Documentation:** Maintain assessment records for audit, insurance

**Insurance Rationale (Universal):**

**Vendor Assessment Requirement:**

- Many cyber insurers require vendor security assessments for high-risk vendors
- Assessment documentation may be requested during policy application/renewal
- Demonstrates proactive third-party risk management

**Third-Party Breach Mitigation:**

- Vendor assessments identify security gaps before they cause breaches
- Organizations with formal assessment processes experience fewer third-party incidents

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Assessment Focus:** FERPA compliance, student data handling, security controls
- **Practical Implementation:** Use standardized education vendor questionnaire (CoSN, EdTech vendor assessment tools)
- **High-Risk Vendors:** Student information systems, learning platforms require rigorous assessment
- **Resource Constraints:** Small districts may use simplified questionnaires for low-risk vendors

**Healthcare:**

- **Assessment Focus:** HIPAA compliance, BAA requirements, PHI handling, security controls
- **HITRUST CSF:** Many healthcare organizations require vendors to complete HITRUST assessments
- **High-Risk Vendors:** EHR vendors, medical device vendors, billing services require extensive assessment
- **Compliance:** HIPAA requires "satisfactory assurances" of vendor security

**Religious/Nonprofit:**

- **Assessment Focus:** Donor data protection, financial controls, security basics
- **Practical Implementation:** Lightweight questionnaires for SaaS vendors; review SOC 2 reports when available
- **Budget-Conscious:** Prioritize assessments for vendors with donor data access

**General Organizations:**

- **Compliance Drivers:** SOC 2, ISO 27001, PCI DSS require vendor assessments
- **Enterprise Approach:** GRC platforms (OneTrust, ServiceNow) automate vendor assessments
- **Industry-Specific:** Financial services, defense contractors have rigorous vendor assessment requirements

**Citations:**

- CIS Controls v8: Control 15.2 (Establish and Maintain a Service Provider Management Policy)
- NIST CSF 2.0: ID.SC-2 (Suppliers and third-party partners are identified, prioritized, and assessed)
- **Ponemon 2024:** Organizations with vendor assessment processes experience 40% fewer third-party incidents
- **HIPAA:** 45 CFR § 164.308(b)(1) - Obtain satisfactory assurances from business associates
- **PCI DSS 4.0:** Requirement 12.8.2 - Maintain information about service providers
- **SOC 2:** Vendor management controls require security assessments

---

### Question 8.3: Vendor Contract Security Requirements

**Question Text:**
Do vendor contracts include security requirements such as encryption, incident notification, audit rights, and compliance obligations?

**Response Options:**

- Fully implemented - standardized security contract clauses, legal review, enforcement
- Partially implemented - some security requirements in contracts, inconsistent
- Not implemented - no security requirements in vendor contracts

**Impact Rating:** High (5)

**Foundational:** No (but critical control)

**Control Description:**

Vendor contracts formalize security expectations and provide legal recourse if vendors fail to meet obligations. Essential contract clauses include:

**Security Requirements:**

- **Data Protection:** Encryption requirements (at rest, in transit), data residency/location
- **Access Controls:** MFA requirements, least privilege, access logging
- **Incident Notification:** Vendor must notify organization of breaches within specified timeframe (24-72 hours)
- **Audit Rights:** Organization retains right to audit vendor security, review SOC 2 reports
- **Compliance:** Vendor must comply with applicable regulations (HIPAA, FERPA, PCI DSS, GDPR)
- **Subprocessor Notification:** Vendor must notify organization before using subcontractors
- **Data Return/Deletion:** Upon contract termination, vendor must return or securely delete organizational data

**Sector-Specific Clauses:**

- **HIPAA Business Associate Agreement (BAA):** Required for healthcare vendors with PHI access
- **FERPA Data Privacy Agreement:** Required for education vendors with student data access
- **PCI DSS Service Provider Agreement:** Required for payment processing vendors

**Insurance Rationale (Universal):**

**Contract Requirements for Coverage:**

- Many cyber insurers **require incident notification clauses** in vendor contracts
- Insurers expect audit rights, data protection requirements in high-risk vendor contracts
- Without contractual security requirements, insurers may deny claims for vendor-caused incidents

**Legal Recourse:**

- Contract security clauses provide legal basis for holding vendors accountable for breaches
- Enable recovery of breach costs from negligent vendors

**Threat Landscape Justification:**

**Vendor Breach Notification:**

- **Average detection time:** 212 days (IBM Cost of Data Breach 2024)
- Without contractual notification requirements, organizations may not learn of vendor breaches for months
- Rapid notification enables faster incident response

**Third-Party Negligence:**

- Many third-party breaches result from vendor security negligence
- Contractual security requirements establish baseline expectations

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **FERPA DPA Required:** Vendors with student data access must sign FERPA Data Privacy Agreement
- **Standard Clauses:** Use model DPA from CoSN, Future of Privacy Forum
- **Incident Notification:** 24-72 hour notification required for student data breaches
- **Practical Implementation:** Legal review of vendor MSAs, negotiate security addendums

**Healthcare:**

- **HIPAA BAA Required:** Mandatory for all vendors with PHI access (45 CFR § 164.308(b))
- **Breach Notification:** HIPAA requires vendors notify covered entities "without unreasonable delay"
- **High-Risk Vendors:** EHR vendors must agree to rigorous security requirements
- **Subcontractor BAAs:** Vendors must obtain BAAs from their subcontractors

**Religious/Nonprofit:**

- **Donor Data Protection Clauses:** Contractual requirements for protecting donor information
- **Incident Notification:** 48-hour notification for donor data breaches
- **Budget Considerations:** Negotiate security requirements even with discounted/donated services

**General Organizations:**

- **SOC 2/ISO 27001:** Compliance frameworks require vendor contract security clauses
- **GDPR Data Processing Agreements:** Required for EU data processing vendors
- **Industry-Specific:** Financial services, defense require extensive contractual security requirements

**Citations:**

- CIS Controls v8: Control 15.2 (Establish and Maintain a Service Provider Management Policy)
- NIST CSF 2.0: ID.SC-4 (Contracts with suppliers and third-party partners are used to implement appropriate measures)
- **IBM Cost of Data Breach 2024:** Average detection time 212 days
- **HIPAA:** 45 CFR § 164.308(b)(1) - Business Associate Agreements required
- **FERPA:** Vendor agreements must include FERPA-compliant data handling clauses
- **GDPR:** Article 28 - Data Processing Agreements required
- **PCI DSS 4.0:** Requirement 12.8.5 - Maintain information about service provider agreements

---

### Question 8.4: Vendor Access Management

**Question Text:**
Does the organization control and monitor third-party vendor access to systems, networks, and data using least privilege and access logging?

**Response Options:**

- Fully implemented - vendor-specific accounts, MFA required, access logged and reviewed
- Partially implemented - some vendor access controls, inconsistent monitoring
- Not implemented - vendors use shared accounts or admin credentials, no monitoring

**Impact Rating:** High (5)

**Foundational:** No (but critical control)

**Control Description:**

Vendor access management ensures third-party vendors have only the minimum access necessary and that access is monitored. Effective controls include:

**Access Controls:**

- **Unique Accounts:** Each vendor has individual accounts (no shared credentials)
- **MFA Required:** Vendors must use MFA for remote access (Questions 2.3-2.6)
- **Least Privilege:** Vendors granted only access necessary for their role
- **Time-Limited Access:** Vendor access expires after project completion or contract term
- **Access Logging:** All vendor access logged and reviewed (SIEM, privileged session monitoring)

**Vendor Access Methods:**

- **VPN:** For vendors requiring network access; enforce MFA, IP restrictions
- **Remote Support Tools:** TeamViewer, LogMeIn, ConnectWise with session recording
- **Cloud IAM:** For SaaS vendors, use identity federation (SAML, OIDC) with organizational MFA
- **Privileged Access Management (PAM):** For vendors requiring administrative access (Question 3.5)

**Access Review:**

- **Quarterly Review:** Review vendor access lists quarterly; revoke unnecessary access
- **Logging Review:** Monitor vendor access logs for anomalous activity
- **Incident Response:** Disable vendor access immediately if vendor experiences breach

**Insurance Rationale (Universal):**

**Vendor Access Control Requirement:**

- Cyber insurers expect vendor access to be controlled via MFA, least privilege
- Shared vendor credentials or excessive vendor access may result in coverage denial
- Vendor access logging demonstrates monitoring capability

**Third-Party Compromise:**

- Many breaches occur via compromised vendor credentials
- MFA for vendor access mitigates credential theft
- Access logging enables detection of vendor account compromise

**Threat Landscape Justification:**

**Vendor Credential Compromise:**

- **Attackers target vendors** to gain access to multiple client organizations
- **MSP Attacks:** Kaseya, ConnectWise, SolarWinds attacks compromised MSP access to clients
- MFA and access logging mitigate vendor credential attacks

**Lateral Movement:**

- Vendors with excessive access enable lateral movement if compromised
- Least privilege limits blast radius of vendor compromise

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Vendor Access Scenarios:** IT support vendors, SIS vendors, managed service providers
- **Practical Implementation:** Vendor-specific accounts in Active Directory/Azure AD, MFA via Google or Microsoft
- **Student Data Access:** Vendors with student data access must use unique accounts, MFA
- **FERPA Compliance:** Access logging demonstrates compliance with FERPA record-keeping requirements

**Healthcare:**

- **Vendor Access Scenarios:** EHR vendor support, medical device vendors, IT managed services
- **HIPAA Requirement:** Audit controls (logging) required for workforce members and vendors with PHI access
- **High-Risk Access:** EHR administrative access via PAM with session recording
- **Compliance:** Minimum necessary access principle applies to vendors

**Religious/Nonprofit:**

- **Vendor Access Scenarios:** IT support, donor system vendors, website developers
- **Donor Data Protection:** Vendors with donor database access must use MFA, unique accounts
- **Practical Implementation:** Cloud IAM for SaaS vendors; VPN with MFA for network access

**General Organizations:**

- **Compliance Drivers:** SOC 2, ISO 27001, PCI DSS require vendor access controls, logging
- **MSP Relationships:** Managed service providers often have extensive access; require MFA, PAM
- **Zero Trust Approach:** Vendors treated as untrusted; require verification at every access

**Citations:**

- CIS Controls v8: Control 15.5 (Audit Service Providers)
- NIST CSF 2.0: PR.AC-4 (Access permissions are managed), PR.AC-6 (Identities are proofed and bound to credentials)
- **Kaseya Ransomware (2021):** 1,500 organizations compromised via MSP access
- **SolarWinds (2020):** Supply chain attack via vendor access
- **HIPAA:** 45 CFR § 164.308(a)(1)(ii)(D) - Audit controls for vendor access
- **PCI DSS 4.0:** Requirement 8.2.2 - MFA for vendor access
- **SOC 2:** CC6.2 - Logical access controls for vendors

---

### Question 8.5: Vendor Off-boarding Process

**Question Text:**
Does the organization have a documented process for terminating vendor access and recovering organizational data when vendor relationships end?

**Response Options:**

- Fully implemented - documented off-boarding process, data return verified, access revoked
- Partially implemented - informal off-boarding, inconsistent execution
- Not implemented - no vendor off-boarding process

**Impact Rating:** Moderate (3)

**Foundational:** No

**Control Description:**

Vendor off-boarding ensures vendors no longer have access after contracts end and organizational data is properly returned or deleted. Effective processes include:

**Off-boarding Steps:**

- **Access Revocation:** Disable vendor accounts, VPN access, API keys immediately upon contract termination
- **Data Return/Deletion:** Vendor returns organizational data or provides certification of secure deletion
- **Equipment Return:** Recover any organizational equipment (laptops, tokens, badges)
- **Documentation:** Document off-boarding completion, data destruction certificates
- **Final Audit:** Review logs to confirm vendor access ceased

**Data Return Options:**

- **Data Export:** Vendor exports organizational data in portable format (JSON, CSV)
- **Secure Deletion:** Vendor securely deletes organizational data and provides certification (NIST 800-88 compliant)
- **Contract Clauses:** Vendor contracts should specify data return/deletion obligations (Question 8.3)

**Insurance Rationale (Universal):**

**Data Retention Risk:**

- Vendors retaining organizational data after contract termination creates data breach risk
- Cyber insurers expect vendor off-boarding processes that ensure data deletion

**Orphaned Vendor Access:**

- Forgotten vendor accounts are common attack vector
- Vendor off-boarding prevents orphaned credentials

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Data Return:** Student data must be returned or deleted per FERPA Data Privacy Agreements
- **Practical Implementation:** Checklist for vendor off-boarding; IT disables accounts, procurement verifies data return
- **FERPA Compliance:** Document data deletion for audit purposes

**Healthcare:**

- **Data Destruction:** HIPAA BAAs require vendors return or destroy PHI upon contract termination
- **Certification Required:** Vendors must certify PHI destruction in HIPAA-compliant manner
- **High-Risk Focus:** EHR vendor transitions require extensive data migration, deletion verification

**Religious/Nonprofit:**

- **Donor Data Return:** Donors expect data to be deleted when vendor relationships end
- **Practical Implementation:** Request data export before termination; verify deletion afterward

**General Organizations:**

- **Compliance:** SOC 2, ISO 27001 require vendor off-boarding procedures
- **Data Portability:** GDPR requires data portability; vendors must export data in portable format

**Citations:**

- CIS Controls v8: Control 5.3 (Disable Dormant Accounts)
- NIST CSF 2.0: PR.IP-6 (Data is destroyed according to policy)
- **HIPAA:** 45 CFR § 164.308(b)(2)(iv)(G) - Data disposal requirements in BAAs
- **FERPA:** Vendor data must be returned or destroyed per Data Privacy Agreements
- **NIST SP 800-88:** Guidelines for Media Sanitization (data destruction standards)

---

### Question 8.6: Third-Party Security Certifications and Assessments 🆕

**Question Text:**
Does the organization require high-risk third-party vendors to maintain recognized security certifications (SOC 2, ISO 27001, HITRUST) or undergo independent security assessments?

**Response Options:**

- Fully implemented - SOC 2/ISO 27001 required for high-risk vendors, assessments reviewed annually
- Partially implemented - certifications requested but not required
- Not implemented - no certification requirements for vendors

**Impact Rating:** High (5)

**Foundational:** No (but strongly recommended for high-risk vendors)

**Control Description:**

Third-party security certifications provide independent validation of vendor security controls, reducing organizational risk assessment burden. Common certifications include:

**Security Certifications:**

- **SOC 2 Type II:** Most common for SaaS vendors; audits security, availability, confidentiality controls over 6-12 month period
- **ISO/IEC 27001:** International standard for information security management systems
- **HITRUST CSF:** Healthcare-specific framework combining HIPAA, NIST, ISO requirements
- **PCI DSS:** Required for payment processing vendors
- **FedRAMP:** Required for cloud vendors serving US federal government
- **StateRAMP:** State-level cloud security authorization

**Risk-Based Approach:**

- **High-Risk Vendors:** Cloud infrastructure, SaaS with sensitive data, managed service providers → **require** SOC 2 or ISO 27001
- **Medium-Risk Vendors:** Professional services, consultants → **request** certifications or conduct security assessments
- **Low-Risk Vendors:** No data access, non-critical services → certifications optional

**Assessment Alternatives:**

- **Third-Party Audits:** Commission independent penetration tests, security assessments
- **Questionnaires:** For vendors without certifications, use standardized questionnaires (SIG, CAIQ)

**Insurance Rationale (Universal):**

**Vendor Certification Requirement:**

- Many cyber insurers **require SOC 2 for critical vendors** (cloud providers, SaaS with sensitive data)
- Certifications reduce insurer risk; may result in premium discounts
- Demonstrates proactive vendor risk management

**Third-Party Breach Mitigation:**

- **Certified vendors experience fewer breaches** than non-certified vendors
- SOC 2/ISO 27001 certifications validate baseline security controls

**Compliance Leverage:**

- SOC 2 audits cover controls required by multiple compliance frameworks (reducing audit burden)

**Threat Landscape Justification:**

**Third-Party Breaches:**

- **Third-party breaches doubled** from 2022 to 2024 (Verizon DBIR 2024)
- **54% of organizations experienced third-party breach** (Ponemon 2024)
- Requiring certifications filters out vendors with weak security

**Supply Chain Attacks:**

- High-profile attacks (SolarWinds, Kaseya, MOVEit) targeted vendors without rigorous security programs
- SOC 2/ISO 27001 certifications indicate mature security programs

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **High-Risk Vendors Requiring SOC 2:**
  - Student Information Systems (PowerSchool, Infinite Campus)
  - Learning Management Systems (Canvas, Schoology)
  - Cloud providers (Google Workspace, Microsoft 365 - both have SOC 2)
  - Data analytics platforms

- **Practical Implementation:** Request SOC 2 Type II reports during vendor selection; review annually
- **FERPA Compliance:** SOC 2 demonstrates vendor has controls to protect student data
- **Budget Constraints:** For smaller vendors without SOC 2, conduct security questionnaire assessment

**Healthcare:**

- **High-Risk Vendors Requiring HITRUST or SOC 2:**
  - EHR vendors (Epic, Cerner)
  - Medical device vendors with connectivity
  - Cloud providers, billing services
  - Telemedicine platforms

- **HITRUST CSF:** Preferred certification in healthcare; combines HIPAA, NIST, ISO requirements
- **HIPAA Compliance:** SOC 2/HITRUST demonstrates vendor has HIPAA-compliant controls
- **Business Associate Agreements:** Certifications supplement but don't replace BAAs

**Religious/Nonprofit:**

- **High-Risk Vendors Requiring SOC 2:**
  - Donor management systems (Salesforce Nonprofit Cloud, Blackbaud - both have SOC 2)
  - Cloud accounting platforms (QuickBooks Online, NetSuite)
  - Email/productivity suites (Google Workspace, Microsoft 365)

- **Practical Implementation:** Check vendor websites for SOC 2 reports; request directly if needed
- **Budget-Conscious:** Many enterprise vendors offer SOC 2 reports at no cost; leverage for due diligence

**General Organizations:**

- **Compliance Drivers:** SOC 2, ISO 27001, PCI DSS require vendor security assessments
- **Industry-Specific:** Financial services often require ISO 27001; government contractors may require FedRAMP
- **Enterprise Approach:** GRC platforms automate vendor certification tracking, expiration alerts

**Citations:**

- CIS Controls v8: Control 15.2 (Establish and Maintain a Service Provider Management Policy)
- NIST CSF 2.0: ID.SC-2 (Suppliers and third-party partners are identified, prioritized, and assessed)
- **Verizon DBIR 2024:** Third-party breaches doubled from 2022 to 2024
- **Ponemon 2024:** 54% of organizations experienced third-party breach
- **SOC 2:** AICPA auditing standard for service organizations
- **ISO/IEC 27001:2022:** International information security standard
- **HITRUST CSF:** Healthcare information security framework
- **PCI DSS 4.0:** Requirement 12.8 - Service provider security requirements

---

### Question 8.7: Vendor Continuous Monitoring and Incident Notification 🆕

**Question Text:**
Does the organization continuously monitor vendor security posture and require vendors to notify the organization of security incidents, breaches, or significant security changes?

**Response Options:**

- Fully implemented - automated vendor monitoring, incident notification clauses enforced, regular vendor reviews
- Partially implemented - annual vendor reviews, informal incident notifications
- Not implemented - no ongoing vendor monitoring or incident notification

**Impact Rating:** High (5)

**Foundational:** No (but critical for high-risk vendors)

**Control Description:**

Vendor continuous monitoring ensures vendor security posture remains acceptable throughout the relationship and enables rapid response to vendor incidents. Effective programs include:

**Continuous Monitoring Methods:**

- **Annual SOC 2 Review:** Request updated SOC 2 reports annually; review for new control deficiencies
- **Security News Monitoring:** Monitor vendor breach news via threat intelligence feeds, security mailing lists
- **Vendor Questionnaires:** Annual security questionnaire updates for high-risk vendors
- **Vendor Portals:** Use vendor risk platforms (SecurityScorecard, BitSight, UpGuard) for automated vendor security ratings
- **Contract Reviews:** Review vendor contracts during renewal for updated security requirements

**Incident Notification Requirements:**

- **Breach Notification:** Vendors must notify organization within 24-72 hours of data breaches
- **Security Changes:** Vendors must notify organization of:
  - Subprocessor changes (new third parties with data access)
  - Data location changes (data moved to new region/country)
  - Control changes (security controls discontinued, weakened)
  - Certification lapses (SOC 2 expired, not renewed)

**Incident Response Integration:**

- **Vendor Breach Playbook:** Define procedures when vendor notifies of breach (disable vendor access, assess impact, notify insurers)
- **Regular Communication:** Establish vendor security contact for incident escalation

**Insurance Rationale (Universal):**

**Incident Notification Requirement:**

- **Cyber insurers require incident notification clauses** in vendor contracts (Question 8.3)
- Rapid notification enables faster incident response, reduces breach impact
- Delayed notification can void insurance coverage

**Vendor Monitoring Demonstrates Due Diligence:**

- Insurers value continuous vendor monitoring programs
- Annual SOC 2 reviews demonstrate ongoing vendor oversight

**Third-Party Breach Response:**

- **Average third-party breach detection:** 212 days (IBM 2024)
- Vendor incident notification reduces detection time from months to days/hours

**Threat Landscape Justification:**

**Third-Party Breaches:**

- **Third-party breaches doubled** from 2022 to 2024 (Verizon DBIR 2024)
- **MOVEit Breach (2023):** File transfer vendor breach affected 2,000+ organizations
- Without incident notification, organizations remain unaware of vendor compromises

**Vendor Security Degradation:**

- Vendor security posture changes over time (budget cuts, staff turnover, control lapses)
- Annual SOC 2 reviews identify vendor security degradation

**Supply Chain Cascade:**

- **Kaseya Attack (2021):** MSP compromise cascaded to 1,500 downstream customers
- Rapid incident notification enabled faster customer response

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Critical Vendors Requiring Monitoring:**
  - Student Information Systems, learning platforms, cloud providers
  - Incident notification within 24 hours for student data breaches (FERPA notification timelines)

- **Practical Implementation:**
  - Request updated SOC 2 reports annually from SIS, LMS vendors
  - Subscribe to EdTech security mailing lists (CoSN, Cybersecurity & Infrastructure Security Agency)
  - FERPA DPAs include incident notification clauses

- **Vendor Incident Examples:** PowerSchool breach (2024), Illuminate Education breach (2023) - schools with notification clauses responded faster

**Healthcare:**

- **Critical Vendors Requiring Monitoring:**
  - EHR vendors, medical device vendors, billing services
  - Incident notification within 24 hours (HIPAA breach notification requirements)

- **Practical Implementation:**
  - Annual HITRUST or SOC 2 review for EHR, billing vendors
  - Healthcare security alerts (HHS HCCIC, FBI Healthcare Cyber Threat Briefs)
  - Business Associate Agreements include breach notification clauses (HIPAA requirement)

- **Vendor Incident Examples:** Change Healthcare breach (2024 affected millions), Elekta medical device breach (2023)

**Religious/Nonprofit:**

- **Critical Vendors Requiring Monitoring:**
  - Donor management systems, accounting platforms, cloud providers
  - Incident notification within 48 hours for donor data breaches

- **Practical Implementation:**
  - Annual SOC 2 review for donor management vendors (Salesforce, Blackbaud)
  - Subscribe to vendor security bulletins
  - Contracts include incident notification for donor data

- **Vendor Incident Examples:** Blackbaud ransomware (2020 affected thousands of nonprofits) - organizations with notification clauses responded faster

**General Organizations:**

- **Compliance Drivers:** SOC 2, ISO 27001, PCI DSS require ongoing vendor monitoring
- **Enterprise Approach:** Vendor risk platforms (SecurityScorecard, BitSight, Panorays) provide automated vendor monitoring
- **Incident Notification Integration:** Vendor breach notifications feed into incident response playbooks

**Citations:**

- CIS Controls v8: Control 15.5 (Audit Service Providers)
- NIST CSF 2.0: ID.SC-3 (Contracts with suppliers and third-party partners are used to implement appropriate measures)
- **Verizon DBIR 2024:** Third-party breaches doubled from 2022 to 2024
- **IBM Cost of Data Breach 2024:** Average detection time 212 days
- **MOVEit Breach (2023):** Affected 2,000+ organizations
- **Kaseya Ransomware (2021):** 1,500 organizations affected via MSP
- **HIPAA:** 45 CFR § 164.410 - Business associates must notify covered entities of breaches

---

### Question 8.8: AI Tool Privacy and Security Vetting 🔑 FOUNDATIONAL 🆕

**Question Text:**
Does the organization vet artificial intelligence (AI) tools and platforms for data privacy, security controls, and compliance before approving for organizational use?

**Response Options:**

- Fully implemented - formal AI vetting process, approved AI tools list, DPAs reviewed
- Partially implemented - informal AI tool vetting, inconsistent
- Not implemented - no AI tool vetting process

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (NEW 2026 - Forward-Looking Control)

**Control Description:**

AI tool vetting ensures AI platforms meet organizational data privacy, security, and compliance requirements before adoption. This control works in conjunction with AI Acceptable Use Policy (Question 7.4). Effective AI vetting includes:

**AI Vetting Criteria:**

- **Data Privacy:**
  - Does AI vendor retain user inputs for model training? (Disqualifying for sensitive data)
  - Where is data stored? (Data residency requirements - EU, US, on-premise)
  - Can data be deleted upon request? (GDPR right to erasure)
  - Does vendor offer zero-retention options for enterprise customers?

- **Security Controls:**
  - Encryption (at rest, in transit)?
  - MFA supported for user accounts?
  - SOC 2 Type II certification?
  - Vulnerability disclosure program?
  - Incident response process?

- **Compliance:**
  - **HIPAA:** Does vendor sign Business Associate Agreement (BAA)?
  - **FERPA:** Does vendor meet student data privacy requirements?
  - **GDPR:** Is vendor GDPR-compliant? (Data Processing Agreement available?)
  - **AI-Specific:** Does vendor comply with EU AI Act (if applicable)?

- **AI-Specific Risks:**
  - **Model Transparency:** Does vendor disclose training data sources?
  - **Bias Mitigation:** Does vendor test for algorithmic bias?
  - **Hallucinations:** Does vendor acknowledge AI output may be inaccurate?
  - **Copyright:** Does vendor indemnify against copyright infringement?

**Enterprise vs. Public AI Tools:**

- **Public AI Tools:** ChatGPT (free), Claude (web), Gemini (free) typically **retain data for training**; not acceptable for sensitive/confidential data
- **Enterprise AI Tools:** Microsoft 365 Copilot, Google Gemini Workspace, AWS Bedrock offer **zero-retention, data residency, compliance** (HIPAA, FERPA, SOC 2)

**Approved AI Tools List:**

- Maintain list of vetted, approved AI tools (links to Question 7.4 AI AUP)
- **Example Enterprise Approvals:**
  - Microsoft 365 Copilot (FERPA, HIPAA, SOC 2, data residency)
  - Google Gemini for Workspace (FERPA, HIPAA, SOC 2, data residency)
  - AWS Bedrock (HIPAA-eligible, SOC 2, customer-controlled data)

**Vetting Process:**

- **Pre-Adoption:** IT/Security team vets AI tool before procurement approval
- **Data Protection Impact Assessment (DPIA):** For high-risk AI uses (GDPR requirement)
- **Contract Review:** Legal reviews AI vendor Data Processing Agreements, AI-specific terms
- **Approval Documentation:** Document vetting decision, approved use cases, prohibited uses

**Insurance Rationale (Universal):**

**Emerging Insurance Requirement (2025-2026):**

- **Coalition "Affirmative AI Insurance"** (2024 launch) recommends AI tool vetting
- **Data Leakage Risk:** Insurers concerned about sensitive data entered into unvetted AI tools
- **Forward-Looking Control:** While not yet universally required, AI vetting anticipated to become standard by 2026

**Compliance Risk Mitigation:**

- **GDPR Violations:** Unvetted AI tools may violate data processing requirements (€20M fines)
- **HIPAA Breaches:** PHI entered into non-compliant AI tools triggers breach notification
- **FERPA Violations:** Student data in public AI tools violates FERPA
- AI vetting prevents unintentional compliance violations

**Vendor Risk Management Integration:**

- AI vendors are third-party vendors; vetting aligns with existing vendor risk program (Questions 8.1-8.7)
- SOC 2 certifications apply to AI vendors (OpenAI, Anthropic, Google, Microsoft all have SOC 2)

**Threat Landscape Justification:**

**Data Leakage via AI Tools:**

- **Samsung Leak (2023):** Engineers entered proprietary code into ChatGPT; Samsung banned ChatGPT
- **Amazon Leak (2023):** Employees entered confidential Amazon data into ChatGPT
- **Without vetting, employees use public AI tools with sensitive data** → data leakage, compliance violations

**AI Training Data Retention:**

- **Public AI tools retain inputs for model training** (OpenAI, Anthropic, Google free tiers)
- Organizational data becomes part of AI training corpus, accessible to other users
- Enterprise AI tools (Microsoft 365 Copilot, Google Workspace) offer zero-retention

**Compliance Violations:**

- **FERPA/COPPA:** Teachers entering student data into ChatGPT violates student privacy laws
- **HIPAA:** Healthcare staff entering PHI into public AI tools triggers breach notification (60-day deadline, potential OCR fines)
- **GDPR:** AI processing personal data requires GDPR compliance (DPAs, data residency)
- AI vetting identifies compliant tools before data exposure occurs

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Vetting Focus:** FERPA compliance, COPPA (K-12), student data privacy, AI model training data retention

- **Approved Enterprise AI Tools:**
  - **Microsoft 365 Copilot for Education:** FERPA-compliant, no student data used for training, data residency in US
  - **Google Gemini for Workspace Education:** FERPA-compliant, Student Data Privacy Agreement, no training on student data
  - **Khan Academy Khanmigo:** Education-specific AI, FERPA-compliant, SOC 2 certified

- **Prohibited Public AI Tools (for student data):**
  - ChatGPT (free tier), Claude (web), Gemini (free) - retain inputs for training, not FERPA-compliant

- **Practical Implementation:**
  - IT approves AI tools before purchase; maintains approved AI tools list
  - Review vendor FERPA Data Privacy Agreements, Student Data Privacy Pledges (studentprivacypledge.org)
  - Training: "Use approved AI tools (Copilot, Gemini Workspace) for lesson planning; don't enter student names, grades, IEPs into ChatGPT"

- **K-12 Specific Risks:** Teachers lack awareness of FERPA implications; clear approved tools list essential

**Healthcare:**

- **Vetting Focus:** HIPAA compliance, Business Associate Agreements, PHI handling, FDA AI medical device guidance

- **Approved Enterprise AI Tools:**
  - **Microsoft Azure Health Bot:** HIPAA-compliant, BAA available, designed for healthcare
  - **Google Cloud Healthcare AI:** HIPAA-compliant, BAA available, PHI processing controls
  - **Nuance DAX (Dragon Ambient eXperience):** Clinical documentation AI, HIPAA-compliant, SOC 2

- **Prohibited Public AI Tools (for PHI):**
  - ChatGPT (free tier), Claude (web), Gemini (free) - not HIPAA-compliant, no BAA, retain inputs

- **Practical Implementation:**
  - IT/Compliance vets AI tools; requires BAA before approval
  - Clinical staff training: "Never enter patient names, diagnoses, MRNs into public AI tools; use approved tools (Azure Health Bot) with BAA"
  - AI Medical Devices: FDA-cleared AI tools vetted separately (radiology AI, diagnostic AI)

- **Compliance:** HIPAA breach notification required if PHI entered into non-compliant AI tools (60-day deadline, OCR enforcement)

**Religious/Nonprofit:**

- **Vetting Focus:** Donor data privacy, financial data protection, AI model training data retention

- **Approved Enterprise AI Tools:**
  - **Microsoft 365 Copilot:** Business-tier, no training on organizational data, SOC 2 certified
  - **Salesforce Einstein (with Nonprofit Cloud):** Donor data AI, SOC 2 certified, no training on customer data

- **Prohibited Public AI Tools (for donor data):**
  - ChatGPT (free tier), Claude (web), Gemini (free) - retain inputs, not suitable for donor PII

- **Practical Implementation:**
  - Budget-conscious nonprofits prioritize free tools for public content, enterprise tools for donor data
  - Staff training: "Use free AI tools (ChatGPT) for drafting public newsletters; use Salesforce Einstein for donor data analysis"
  - Donor Trust: AI vetting demonstrates responsible stewardship of donor information

**General Organizations:**

- **Vetting Focus:** Trade secrets, proprietary data, customer PII, industry-specific compliance (GDPR, CCPA, PCI DSS)

- **Approved Enterprise AI Tools:**
  - **Microsoft 365 Copilot:** Enterprise-tier, Commercial Data Protection, SOC 2, EU Data Boundary
  - **Google Gemini Enterprise:** Data residency, no training on customer data, SOC 2
  - **AWS Bedrock:** Customer-controlled AI models, data not used for training, HIPAA-eligible

- **Prohibited Public AI Tools (for sensitive data):**
  - Public AI tools not suitable for trade secrets, customer PII, proprietary code

- **Compliance:**
  - **GDPR:** AI processing personal data requires Data Processing Agreements, data residency controls (EU)
  - **CCPA:** California consumer data privacy requirements apply to AI tools
  - **Industry-Specific:** Financial services (NYDFS), healthcare (HIPAA), government (FedRAMP) have specific AI requirements

- **Competitive Risk:** Proprietary data entered into public AI tools may benefit competitors (AI learns from inputs)

**Citations:**

- **NIST AI Risk Management Framework (AI RMF 1.0, January 2023):** Voluntary framework for AI governance, risk management
- **Coalition Cyber Insurance:** "Affirmative AI Insurance" product (2024); recommends AI tool vetting
- **EU AI Act (2024):** Regulation of high-risk AI systems in EU; compliance required for EU AI uses
- **Samsung ChatGPT Ban (2023):** Example of data leakage risk from unvetted AI tools
- **Microsoft Commercial Data Protection:** Zero-retention AI for Microsoft 365 Copilot
- **Google Workspace AI Data Use:** "Your data is your data" - not used for training
- **FERPA:** Student data privacy; applies to AI tools used for student data
- **HIPAA:** Business Associate Agreements required for AI vendors processing PHI
- **GDPR:** Article 28 - Data Processing Agreements required for AI vendors processing personal data
- CIS Controls v8: Control 15.1 (Establish and Maintain an Inventory of Service Providers) - AI vendors are service providers
- NIST CSF 2.0: ID.SC-2 (Suppliers and third-party partners are identified, prioritized, and assessed)

---

