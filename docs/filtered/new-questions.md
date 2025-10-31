---
title: New Questions (12)
tags:
  - New
  - 2026 Expansion
---

# 🆕 New Questions for 2026

These 12 questions have been added based on 2024-2025 threat landscape analysis and insurance market requirements.

**5 New Foundational:**
- 3.5: PAM Platform
- 4.14: SIEM
- 5.5: Email Authentication
- 7.4: AI AUP
- 8.8: AI Vetting

**7 New Supporting:**
- 3.6: Data Classification
- 4.15: Cloud Security
- 4.16: Secure Remote Access
- 5.6: API Security
- 8.6: Vendor Certifications
- 8.7: Vendor Monitoring
- 9.7: MTTD/MTTR

---

### Question 3.5: Privileged Access Management (PAM) Platform 🔑 FOUNDATIONAL 🆕

**Question Text:**
Has the organization implemented a Privileged Access Management (PAM) solution to control, monitor, and audit access to privileged accounts (administrators, service accounts, shared credentials)?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (NEW 2026)

**Control Description:**

Privileged Access Management (PAM) provides centralized control over privileged accounts through:

**Core PAM Capabilities:**

- **Credential Vaulting:** Secure storage of privileged passwords, SSH keys, certificates
- **Session Monitoring/Recording:** Screen recording, keystroke logging of privileged sessions
- **Just-In-Time Access:** Time-limited elevation of privileges (request → approve → access for 4 hours → automatic revoke)
- **Automated Password Rotation:** Regular password changes for service accounts, local admin accounts
- **Privilege Elevation and Delegation:** Temporary admin rights without knowing password

**PAM Components:**

- **Password Vault:** Centralized credential repository (LastPass Enterprise, CyberArk, Thycotic Secret Server)
- **Privileged Session Manager:** Recording and monitoring of admin activities
- **Privileged Account Analytics:** Behavioral analytics to detect anomalous privileged account usage
- **Secrets Management:** API keys, database passwords, service account credentials

**PAM Implementation Approaches:**

- **Enterprise PAM Platforms:** CyberArk, BeyondTrust, Delinea (formerly Thycotic), Centrify
- **Cloud-Native PAM:** Azure Privileged Identity Management (PIM), AWS Secrets Manager, Google Secret Manager
- **SMB PAM:** ManageEngine PAM360 Cloud, Keeper Secrets Manager
- **Open Source:** Vault by HashiCorp (requires expertise)

**Insurance Rationale (Universal):**

**RAPID INSURANCE REQUIREMENT GROWTH:**

- **42% of organizations in 2024** required to have PAM for cyber insurance coverage (up from 36% in 2023) - Securden
- **Vast majority of cyberattacks** involve stolen credentials and misuse of privileged access - ManageEngine
- Organizations lacking robust PAM strategies face **policy rejection or cancellation**

**Insurer PAM Requirements:**

- **Removing local admin rights** from workstations - BeyondTrust
- **Enforcing principle of least privilege (PoLP)** - BeyondTrust
- **Consolidating and securing all privileged credentials** - Securden
- **Monitoring and recording privileged sessions** - ManageEngine
- **Auditing all privileged activities** with real-time alerts - Securden

Many insurers now mandate proof of adherence to regulatory standards (GDPR, HIPAA, PCI DSS) which require PAM controls.

**Threat Landscape Justification:**

**IBM X-Force 2025:**

- **Account abuse remains #1 initial access vector** (30% of incidents across all sectors)
- Attackers specifically target privileged accounts for maximum impact
- Privileged accounts enable lateral movement, data exfiltration, and ransomware deployment

**Verizon DBIR 2024:**

- **88% of breaches involved stolen credentials** (universal across industries)
- Privileged accounts with elevated permissions are prime targets
- Can modify systems, access ALL data, disable security controls (EDR, SIEM, backups)

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Shared Admin Credentials:** IT staff often share admin credentials across team
- **Service Accounts:** Student information systems (SIS), learning management systems (LMS) use service accounts with weak oversight
- **Limited Visibility:** Lack visibility into privileged activities - who accessed student database when?
- **Practical Implementation:** Cloud-based PAM (Delinea Secret Server Cloud) with EDU pricing
- **FERPA Compliance:** PAM provides accountability for who accessed student education records

**Healthcare:**

- **Hospital IT Shares Admin Credentials:** EHR systems (Epic, Cerner) often have shared admin passwords
- **Service Accounts:** Medical devices, lab systems, pharmacy systems use service accounts
- **HIPAA 2025 Security Rule:** Enhanced access controls required for ePHI systems
- **Compliance:** HIPAA Security Rule §164.312(a)(1) - access controls and audit controls require PAM
- **Practical Implementation:** PAM integrated with Active Directory for Windows-based EHR environments

**Religious/Nonprofit:**

- **Small IT Teams / Volunteers:** Often share admin passwords for donor systems, financial software
- **Limited Expertise:** Makes PAM especially valuable - managed service options available
- **Service Accounts:** Church management systems, donor databases use service accounts with static passwords
- **Practical Implementation:** Managed PAM services (Arctic Wolf, Huntress) handle deployment/operation

**General Organizations:**

- **Admin Access:** Financial systems, payroll, HR databases require privileged access
- **Service Accounts:** Active Directory, cloud platforms (AWS, Azure), infrastructure automation
- **Compliance:** SOX (if applicable), state data breach notification laws, industry regulations

**Citations:**

- **Securden (2024):** "42% of organizations required to have PAM for cyber insurance coverage" (up from 36% in 2023)
  - URL: https://www.securden.com/privileged-account-manager/pam-for-cyberinsurance.html
- **ManageEngine:** "Vast majority of cyberattacks due to stolen credentials and misuse of privileged access"
  - URL: https://www.manageengine.com/privileged-access-management/pam-for-cyberinsurance.html
- **BeyondTrust:** "Two basic requirements of many cyber insurers: removing admin rights and enforcing PoLP"
  - URL: https://www.beyondtrust.com/solutions/cyber-insurance
- **IBM X-Force Threat Intelligence Index 2025:** Account abuse #1 initial access vector (30% of incidents)
- **Verizon DBIR 2024:** 88% of breaches involved stolen credentials
- **CIS Controls v8:** Control 5.4 - Restrict administrator privileges to dedicated accounts
- **NIST CSF 2.0:** PR.AC-4 - Access permissions are managed
- **HIPAA Security Rule (2025):** Enhanced access controls for ePHI

---

### Question 3.6: Data Classification and Handling Procedures 🆕

**Question Text:**
Has the organization established a data classification system (e.g., public, internal, confidential, restricted) with documented handling procedures for each classification level?

**Impact Rating:** Moderate (3)

**Foundational:** NO - Comprehensive maturity indicator (NEW 2026)

**Control Description:**

Data classification systematically categorizes information based on sensitivity and impact of unauthorized disclosure:

**Classification Levels (Typical Organizational Scheme):**

**Public:**

- Information intended for public distribution
- **Education Examples:** School website content, newsletters, public event calendars
- **Healthcare Examples:** Hospital locations, public health information, marketing materials
- **Religious/Nonprofit Examples:** Service times, public ministry information, donation appeals
- **Handling:** No restrictions on distribution

**Internal:**

- Information for internal use only (not public but not highly sensitive)
- **Education Examples:** Staff directories, internal policies, meeting minutes
- **Healthcare Examples:** Staff schedules, internal procedures, facility maps
- **Religious/Nonprofit Examples:** Volunteer schedules, internal ministry plans
- **Handling:** Distribute to employees/members only; don't post publicly

**Confidential:**

- Sensitive information requiring protection from unauthorized disclosure
- **Education Examples:** Student education records (FERPA), employee PII, financial data, grades
- **Healthcare Examples:** Patient health information (HIPAA/PHI), employee health records, billing data
- **Religious/Nonprofit Examples:** Donor PII, credit card information, pastoral counseling notes
- **Handling:** Encryption required, access controls, confidentiality agreements

**Restricted:**

- Highly sensitive information with severe impact if disclosed
- **Education Examples:** Student SSNs, special education IEPs, investigation files
- **Healthcare Examples:** Substance abuse treatment records, HIV status, genetic information
- **Religious/Nonprofit Examples:** Abuse/misconduct investigation files, high-value donor confidential information
- **Handling:** Encryption mandatory, strict access controls, audit logging, need-to-know basis

**Handling Procedures for Each Level:**

**Storage Requirements:**

- **Confidential/Restricted:** Encrypted storage (at rest), access controls, secure file shares
- **Internal:** Access controls, not public-facing servers
- **Public:** Standard security

**Transmission Methods:**

- **Confidential/Restricted:** Encrypted email (TLS), secure file transfer (SFTP), secure portals
- **Internal:** Standard email (TLS)
- **Public:** No restrictions

**Sharing/Disclosure Rules:**

- **Confidential:** Requires data owner approval, data sharing agreements
- **Restricted:** Requires executive approval, legal review, strict agreements
- **Internal/Public:** Departmental discretion

**Retention and Destruction:**

- **Confidential/Restricted:** Defined retention period, secure deletion (see Question 3.4)
- **All Levels:** Documented in retention policy

**Labeling Requirements:**

- **Email Subject Tags:** [CONFIDENTIAL], [RESTRICTED]
- **Document Headers/Footers:** "Confidential - Student Education Records"
- **File Share Labels:** Folder naming conventions

**Technical Controls:**

- **Data Loss Prevention (DLP):** Prevent confidential data from leaving organization
- **Encryption Policies:** Automatic encryption for confidential/restricted data
- **Access Controls:** Role-based access to classified data

**Insurance Rationale (Universal):**

Data classification enables **targeted protection** and reduces breach impact:

**Breach Notification Scope:**

- Properly classified data enables rapid impact assessment
- Know immediately which data types were exposed
- Calculate notification requirements accurately

**Proportionate Protection:**

- Apply strongest controls (encryption, access restrictions) to restricted data
- Reduce costs by not over-protecting public/internal data

**Compliance Demonstration:**

- Shows understanding of what data organization holds
- Demonstrates appropriate controls applied based on sensitivity
- **FERPA:** Helps distinguish education records from directory information
- **HIPAA:** Identifies PHI requiring protection
- **State Privacy Laws (2025):** Data classification supports data minimization requirements

**Threat Landscape Justification:**

**Verizon DBIR 2024:**

- Breaches increasingly target specific data types (credentials, personal information, payment data)
- Data classification enables organizations to focus protection on highest-value targets

**State Privacy Laws (2025):**

- **Eight new state privacy laws** require data minimization and protection proportionate to sensitivity
- Data classification is foundational to compliance

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Public:** School calendars, sports schedules, lunch menus
- **Internal:** Staff handbooks, internal communications
- **Confidential:** Student grades, attendance, discipline records (FERPA-protected education records)
- **Restricted:** Student SSNs, special education IEPs, investigation files
- **FERPA Distinction:** Helps distinguish education records from directory information (which can be disclosed)
- **Challenge:** Many school staff lack clarity on FERPA-protected vs. public data

**Healthcare:**

- **Public:** Hospital visiting hours, physician directories
- **Internal:** Staff procedures, department communications
- **Confidential:** General patient health information (name, diagnosis, treatment) (PHI)
- **Restricted:** Substance abuse records, HIV status, genetic information (special protections under 42 CFR Part 2, state laws)
- **HIPAA:** Data classification helps implement "minimum necessary" standard

**Religious/Nonprofit:**

- **Public:** Service times, ministry events, donation appeals
- **Internal:** Volunteer schedules, ministry plans
- **Confidential:** Donor PII, contribution amounts, contact information
- **Restricted:** Pastoral counseling notes, abuse/misconduct investigations, high-value donor confidential agreements
- **Donor Trust:** Classification demonstrates stewardship of donor privacy

**General Organizations:**

- **Public:** Marketing materials, product information
- **Internal:** Policies, procedures, internal communications
- **Confidential:** Customer PII, financial records, employee data
- **Restricted:** Trade secrets, intellectual property, M&A information, executive compensation
- **SOX Compliance (if applicable):** Financial data classification required

**Citations:**

- **NIST CSF 2.0:** ID.AM-5 - "Resources are prioritized based on classification and business value"
- **CIS Controls v8:** Control 3.1 - "Establish and Maintain a Data Management Process"
- **State Privacy Laws (2025):** Data classification supports proportionate protection and minimization
- **FERPA:** Data classification helps distinguish education records from directory information
  - URL: https://studentprivacy.ed.gov/
- **HIPAA:** Minimum necessary standard requires understanding of data sensitivity
- **ISO 27001:** Annex A.8.2 - Information classification

---


<a name="category-4"></a>
### Question 4.14: Centralized Logging and SIEM 🔑 FOUNDATIONAL 🆕

**Question Text:**
Does the organization implement centralized logging with a Security Information and Event Management (SIEM) or log management solution to collect, correlate, and analyze security events from across networks, servers, endpoints, and security devices?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES (for larger organizations >500 users) / NO (for smaller organizations) - Tiered requirement (NEW 2026)

**Control Description:**

Centralized logging aggregates security events, system logs, and audit data from diverse sources into a unified platform:

**Log Sources:**

- **Firewalls:** Allowed/denied traffic, VPN connections, intrusion attempts
- **Endpoints:** Windows Event Logs, macOS Unified Logging, Linux syslog
- **Servers:** Authentication logs, application logs, database logs
- **Applications:** Web servers (IIS, Apache), email servers, line-of-business applications
- **Cloud Services:** Microsoft 365 audit logs, Google Workspace logs, AWS CloudTrail, Azure Monitor
- **Security Tools:** Antivirus/EDR alerts, IPS events, authentication failures

**SIEM Capabilities:**

- **Real-Time Correlation:** Identify patterns across multiple log sources (failed login from IP A, then successful login from IP B = credential compromise)
- **Threat Detection:** Pre-built rules detect known attack patterns (brute force, privilege escalation, data exfiltration)
- **Alerting:** Email/SMS/push notifications for security incidents
- **Forensic Investigation:** Search historical logs to trace attacker activities
- **Compliance Reporting:** Generate reports for HIPAA, PCI DSS, FERPA audit requirements

**SIEM Solutions:**

- **Enterprise:** Splunk Enterprise, IBM QRadar, LogRhythm, ArcSight
- **Cloud-Based (Recommended for Education/Healthcare):** Microsoft Sentinel, Splunk Cloud, Sumo Logic, Devo
- **Open Source:** Elastic Security (ELK Stack), Wazuh, OSSIM
- **Managed SOC Services:** Arctic Wolf, Huntress, Red Canary (include SIEM + 24/7 monitoring)

**Log Management (Without Full SIEM):**

- **Basic Centralization:** Graylog, Papertrail, Loggly (collect and store logs)
- **Limited Analytics:** Search capability but not full correlation/threat detection
- **Value:** Still provides forensic investigation capability, compliance audit trails

**Insurance Rationale (Universal):**

**SIEM/SOC Capabilities Required by Insurers:**

- **Larger Organizations:** SIEM now required for organizations >500 users or regulated industries
- **Continuous Monitoring:** Insurers require 24/7 security monitoring; managed SOC services provide practical solution
- **Audit Trails:** Log retention supports compliance (HIPAA, PCI DSS, state privacy laws)
- **Mean Time to Detect (MTTD):** SIEM improves MTTD, reducing breach costs and claim severity

**Citations:**

- **TechSolutions Inc (2024):** "SOC and SIEM no longer optional for cyber insurance"
  - URL: https://www.techsolutionsinc.com/blog/why-soc-and-siem-are-no-longer-optional-for-cyber-insurance/
- **Atlantic Digital (2024):** "SIEM among key requirements for cyber insurance in 2024"
  - URL: https://www.adiit.com/cyber-insurance-key-requirements-and-industry-insights/

**Threat Landscape Justification:**

**IBM X-Force 2025:**

- **Average time to detect breach: 212 days** across all sectors
- Organizations without centralized logging lack visibility into attacker lateral movement, credential abuse, data exfiltration
- SIEM reduces detection time from months to days/hours

**Verizon DBIR 2024:**

- **Third-party involvement in breaches doubled**
- Without centralized logging across on-premises and cloud environments, organizations cannot detect anomalous activities or trace attack paths

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Distributed Campus Logs:** Multiple buildings, cloud services (Google Workspace/Microsoft 365), student information systems
- **Cloud-Based SIEM:** Microsoft Sentinel (integrates with Microsoft 365 Education), Splunk Cloud (EDU pricing), Sumo Logic
- **FERPA Compliance:** Audit logs demonstrate who accessed student records and when
- **Practical Implementation:** Managed SOC services (Arctic Wolf, Huntress) provide 24/7 monitoring for districts without dedicated security staff
- **Challenge:** Limited IT staff; cloud-based solutions reduce on-premises infrastructure burden

**Healthcare:**

- **HIPAA 2025 Security Rule:** Audit controls mandatory (§164.312(b)) - logging required for ePHI access
- **Log Sources:** EHR systems, medical devices, lab systems, pharmacy systems, patient portals
- **24/7 Operations:** SIEM provides continuous monitoring for hospitals with round-the-clock patient care
- **Managed SOC:** Practical for smaller hospitals/clinics without dedicated security operations center
- **HIPAA Breach Investigation:** Centralized logs required to determine scope of PHI exposure

**Religious/Nonprofit:**

- **Basic Log Management:** Smaller organizations may start with basic centralization (Graylog, cloud logging)
- **Donor System Logs:** Track access to donor management systems, accounting software
- **Managed Services:** Arctic Wolf, Huntress provide SIEM + monitoring for nonprofits without IT security expertise
- **Challenge:** Budget constraints; managed SOC services offer predictable monthly cost vs. enterprise SIEM licensing

**General Organizations:**

- **Financial Systems:** Log access to financial systems, payroll, banking portals
- **Compliance:** SOX (if applicable), PCI DSS (logging required), state data breach laws
- **Operational Technology (OT/ICS):** SIEM monitors industrial control systems, SCADA

**Citations:**

- **IBM X-Force Threat Intelligence Index 2025:** Average 212-day detection time without centralized monitoring
- **Verizon DBIR 2024:** Third-party involvement doubled; centralized logging enables attack path tracing
- CIS Controls v8: Control 8 - Audit Log Management
- NIST CSF 2.0: DE.AE - Anomalies and Events are detected
- HIPAA Security Rule (2025 NPRM): §164.312(b) - Audit controls
- PCI DSS Requirement 10: Track and monitor all access to network resources and cardholder data
- **Parachute Cloud (2025):** "Industries governed by HIPAA, PCI DSS require centralized log management"
  - URL: https://parachute.cloud/blog/siem-for-cyber-insurance

---

### Question 4.15: Cloud Security Configuration Management 🆕

**Question Text:**
Does the organization use cloud security posture management (CSPM) tools or processes to continuously monitor and remediate misconfigurations in cloud environments (AWS, Azure, Google Cloud, Microsoft 365, Google Workspace)?

**Impact Rating:** High (5)

**Foundational:** NO - Comprehensive maturity indicator (NEW 2026)

**Control Description:**

Cloud Security Posture Management (CSPM) involves continuous assessment of cloud infrastructure configurations against security best practices and compliance frameworks:

**CSPM Scope:**

- **Cloud Storage:** S3 buckets (AWS), Azure Blob Storage, Google Cloud Storage - check for public access
- **Identity and Access Management (IAM):** Overly permissive roles, unused service accounts, MFA gaps
- **Network Security Groups:** Firewall rules allowing unnecessary inbound access
- **Encryption Settings:** Verify encryption at rest and in transit enabled
- **Logging and Monitoring:** Ensure CloudTrail (AWS), Azure Monitor, Google Cloud Logging enabled
- **Compliance Benchmarks:** CIS Benchmarks for AWS/Azure/GCP, NIST, PCI DSS, HIPAA

**CSPM Tools:**

- **Native Cloud Tools:**

  - AWS Security Hub (aggregates findings from AWS Config, GuardDuty, Inspector)
  - Azure Security Center / Microsoft Defender for Cloud
  - Google Security Command Center
  - Microsoft Secure Score (for Microsoft 365)
  - Google Workspace Security Health
- **Third-Party CSPM:** Prisma Cloud (Palo Alto), Wiz, Orca Security, Lacework
- **Open Source:** CloudSploit, Prowler (AWS), ScoutSuite

**Configuration Monitoring:**

- **Continuous Scanning:** Real-time detection of misconfigurations
- **Automated Remediation:** Auto-fix common issues (disable public S3 bucket access)
- **Alerting:** Notify security team of critical misconfigurations
- **Compliance Dashboard:** View compliance status against frameworks (CIS, NIST, PCI DSS)

**Common Cloud Misconfigurations:**

- **Public S3 Buckets:** Unintentional public access to sensitive data
- **Overly Permissive IAM:** Admin rights granted broadly instead of least-privilege
- **Disabled Encryption:** Data stored unencrypted in cloud
- **Disabled Logging:** CloudTrail, Azure logs turned off, preventing audit trail
- **Open Security Groups:** Firewall rules allowing 0.0.0.0/0 (entire internet) access to SSH/RDP

**Insurance Rationale (Universal):**

**95% of cloud breaches stem from misconfigurations** (GBHackers 2025), making CSPM essential for risk mitigation. As organizations adopt multi-cloud environments, insurers assess cloud security controls during underwriting:

**Insurer Concerns:**

- **Publicly Exposed Storage:** S3 buckets with PII, PHI, financial data accessible to internet
- **Overly Permissive IAM:** Enables lateral movement if single account compromised
- **Disabled Encryption/Logging:** Violates HIPAA, PCI DSS requirements
- **Compliance Failures:** NIST, CIS benchmark violations indicate immature security

Cloud-native applications and SaaS platforms are now primary attack surfaces for all sectors. Insurers increasingly require evidence of cloud security monitoring.

**Threat Landscape Justification:**

**Industry Research (2024-2025):**

- **95% of cloud breaches result from misconfigurations** (GBHackers 2025)
- Organizations need visibility across multi-cloud deployments regardless of sector
- "Proliferation of sophisticated attacks and challenge of managing dynamic cloud assets underscore critical need for advanced cloud security" (Orca Security 2025)

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Extensively Use Cloud:** Microsoft 365 Education, Google Workspace for Education (often with default configurations lacking security hardening)
- **Student Data:** Stored in cloud platforms (Google Classroom, Microsoft Teams, cloud SIS)
- **Practical Implementation:** Microsoft Secure Score (free with M365), Google Workspace Security Health (free)
- **FERPA:** Proper access controls, encryption, monitoring required for cloud-based education records

**Healthcare:**

- **EHR Systems in Cloud:** Epic on AWS, Cerner on Azure, cloud-based medical imaging (PACS)
- **HIPAA 2025 Security Rule:** Encryption mandated for ePHI at rest and in transit (cloud storage must be encrypted)
- **Cloud Misconfigurations:** Can expose patient health information (PHI)
- **Practical Implementation:** Azure Security Center for Azure-hosted EHR, AWS Security Hub for AWS

**Religious/Nonprofit:**

- **Cloud Services:** Microsoft 365, Google Workspace for donor communications, financial records
- **Donor Management:** Cloud-based platforms (Blackbaud, Planning Center)
- **Misconfigurations:** Can expose donor PII, credit card information
- **Practical Implementation:** Microsoft Secure Score, Google Workspace Security Health (free built-in tools)

**General Organizations:**

- **Multi-Cloud Environments:** AWS for infrastructure, Azure for SaaS, Google for productivity
- **Compliance:** SOX, PCI DSS, state privacy laws extend to cloud environments
- **Operational Technology (OT):** Increasingly cloud-managed

**Citations:**

- **GBHackers (2025):** "95% of cloud breaches stem from misconfigurations"
  - URL: https://gbhackers.com/best-cloud-security-companies/
- **Orca Security (2025):** "Multi-cloud compliance requires consistent security policies across AWS, Azure, GCP"
  - URL: https://orca.security/resources/blog/what-is-multi-cloud-compliance/
- **Microsoft Learn:** "Microsoft cloud security benchmark with ~180 AWS checks for multi-cloud"
- CIS Controls v8: Control 4 - Secure Configuration (extends to cloud)
- NIST CSF 2.0: PR.IP-1 - Baseline configurations for cloud services
- HIPAA Security Rule (2025): §164.312(a)(2)(iv) - Encryption at rest and in transit for cloud ePHI

---


### Question 4.16: Secure Remote Access Controls 🆕

**Question Text:**
Beyond MFA, does the organization implement additional remote access security controls such as conditional access policies (device compliance, location-based access), network access control (NAC), or zero-trust network access (ZTNA)?

**Impact Rating:** Moderate (3)

**Foundational:** NO - Comprehensive maturity indicator (NEW 2026)

**Control Description:**

Enhanced remote access security goes beyond VPN+MFA to include:

**Conditional Access Policies:**

- **Device Health Checks:** OS version current, encryption enabled, EDR running before granting access
- **Location-Based Policies:** Block access from high-risk countries, unusual geolocations
- **Risk-Based Authentication:** Unusual location/time triggers additional verification (step-up MFA)
- **Application-Specific Access:** Different requirements for email vs. financial systems

**Network Access Control (NAC):**

- **Device Posture Assessment:** Check device compliance before network access
- **Automated Quarantine:** Non-compliant devices moved to remediation VLAN
- **Guest Network Enforcement:** Automatically redirect unknown devices to guest network

**Zero Trust Network Access (ZTNA):**

- **Application-Level Access:** Grant access to specific applications, not entire network (vs. traditional VPN)
- **Least-Privilege Access:** Per-application access control
- **Continuous Verification:** Regularly re-authenticate and re-authorize during session

**Split Tunneling Controls:**

- **Full Tunnel VPN:** All traffic routes through VPN (more secure, impacts performance)
- **Split Tunnel VPN:** Only corporate traffic through VPN, internet direct (less secure, better performance)
- **Policy-Based Split Tunneling:** Microsoft 365 traffic direct, sensitive apps through VPN

**Remote Desktop Security:**

- **Disable RDP from Internet:** No direct RDP access from public internet
- **Require VPN+MFA for RDP:** Two-factor authentication before RDP access
- **RDP Gateway:** Centralized RDP gateway with MFA, audit logging
- **Limit RDP to Specific IP Ranges:** Restrict RDP access to known IP addresses

**Insurance Rationale (Universal):**

Remote work expanded attack surface post-COVID:

- **Coalition:** 82% of cyber insurance claims involved organizations lacking MFA
- **MFA Alone Insufficient:** Conditional access adds device compliance, location verification
- **BYOD Security:** Bring-Your-Own-Device policies require device compliance checks

**Insurers Assess:**

- Device compliance requirements (managed vs. unmanaged devices)
- Conditional access policies reducing risk-based access
- BYOD security controls
- VPN+MFA implementation quality (split tunneling risks, weak VPN protocols)

**Threat Landscape Justification:**

**IBM X-Force 2025:**

- **Most ransomware attacks start with compromised VPNs and remote access credentials**
- Advanced techniques exploit remote access technologies

**Verizon DBIR 2024:**

- Remote access exploitation is top attack path
- Attackers scan for VPN endpoints and attempt credential stuffing

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Remote Access Needs:** Teachers/administrators working from home, IT staff accessing systems remotely
- **Post-COVID:** Remote work now permanent for many staff roles
- **Conditional Access:** Microsoft 365/Google Workspace conditional access features (device compliance, location policies)
- **BYOD:** Teachers using personal laptops, tablets; conditional access ensures device meets security baseline
- **Practical Implementation:** Azure AD Conditional Access (built into Microsoft 365), Google Workspace Context-Aware Access

**Healthcare:**

- **Clinical Remote Access:** Physicians on-call, telehealth providers, remote nurses accessing EHR
- **Device Compliance:** Ensure physician personal devices have encryption, EDR before accessing PHI
- **HIPAA:** Remote access to PHI requires strong authentication and device security
- **24/7 Access Needs:** MFA fatigue mitigation through conditional access (reduce prompts for trusted devices/locations)
- **Challenge:** Balancing security with clinical workflow; device compliance checks can delay patient care

**Religious/Nonprofit:**

- **Remote Staff:** Ministry staff, accountants, volunteer coordinators working remotely
- **BYOD:** Staff using personal devices for ministry work
- **Conditional Access:** Microsoft 365/Google Workspace conditional access (free with business/enterprise subscriptions)
- **Challenge:** Limited IT budget for advanced ZTNA solutions; cloud platform conditional access provides practical option

**General Organizations:**

- **Work-From-Anywhere:** Permanent remote/hybrid work policies
- **Contractor Access:** Third-party contractors, vendors requiring temporary remote access
- **ZTNA:** Modern alternative to traditional VPN (Zscaler, Cloudflare Access, Microsoft Azure AD Application Proxy)

**Citations:**

- **Corvus Insurance (2024):** "BYOD introduces security risks leaving companies vulnerable"
  - URL: https://www.corvusinsurance.com/blog/byod-does-a-cyber-insurance-policy-cover-remote-workers
- **DeepStrike (2025):** "Remote work security requires VPN+MFA, EDR, encryption, DLP, BYOD/Zero Trust"
  - URL: https://deepstrike.io/blog/Remote-Work-Security-Risks-2025
- **Coalition (2024):** "82% of claims involved orgs lacking MFA; remote access primary attack vector"
- **Venn (2025):** "BYOD market $52B in 2024, growing 15% CAGR to $150B by 2035"
  - URL: https://www.venn.com/learn/byod/byod-security-best-practices/
- CIS Controls v8: Control 12.6 - Use secure network management and communication protocols
- NIST CSF 2.0: PR.AC-3 - Remote access is managed
- **Microsoft Conditional Access:** Built-in Azure AD feature for device compliance, location policies
- **Google Workspace Context-Aware Access:** Device and location-based access controls

---

*Category 4 Complete: Secure Configuration and Vulnerability Management (16 questions total, including 3 NEW questions: 4.14 SIEM, 4.15 Cloud Security, 4.16 Remote Access)*

---


<a name="category-5"></a>
### Question 5.5: Email Authentication Protocols (DMARC, SPF, DKIM) 🔑 FOUNDATIONAL 🆕

**Question Text:**
Has the organization implemented email authentication protocols including SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail), and DMARC (Domain-based Message Authentication, Reporting, and Conformance) to prevent email spoofing and impersonation attacks?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (NEW 2026)

**Control Description:**

Email authentication protocols work together to prevent domain spoofing and verify email legitimacy:

**SPF (Sender Policy Framework):**

- **Purpose:** Authorizes specific IP addresses to send email from your domain
- **DNS Record:** Publish SPF record listing authorized mail servers
- **Example:** "v=spf1 include:_spf.google.com ~all" (Google Workspace)

**DKIM (DomainKeys Identified Mail):**

- **Purpose:** Adds digital signature to verify message hasn't been tampered with in transit
- **Implementation:** Enable DKIM signing on outbound email server
- **Verification:** Receiving server checks signature against public key in DNS

**DMARC (Domain-based Message Authentication, Reporting, and Conformance):**

- **Purpose:** Provides policy for handling emails failing SPF/DKIM checks + generates reports
- **Policies:**

  - **p=none:** Monitor mode (collect reports, no enforcement)
  - **p=quarantine:** Failed emails go to spam folder
  - **p=reject:** Failed emails rejected entirely (strongest protection)
- **Reports:** Daily XML reports showing email authentication results, spoofing attempts

**Full Implementation:**

1. **Publish SPF record** in DNS listing authorized mail servers
2. **Enable DKIM signing** on outbound email (Google Workspace, Microsoft 365 admin consoles)
3. **Implement DMARC policy** starting with p=none for monitoring
4. **Monitor DMARC reports** to identify legitimate senders and spoofing attempts
5. **Strengthen DMARC to p=quarantine or p=reject** after validation period

**Insurance Rationale (Universal):**

Email remains **#1 attack vector** with phishing as top initial access method across all sectors:

**Business Email Compromise (BEC) Attacks:**

- Cost billions annually
- Attackers impersonate executives, administrators, or vendors to request wire transfers or credential disclosure
- Email authentication prevents domain impersonation (attacker can't send email appearing to be from your domain)

**Coalition Cyber Insurance:**

- Specifically lists **email authentication (SPF, DKIM, DMARC)** on cyber insurance coverage checklist
- Many BEC losses are excluded or sub-limited in cyber policies, making **prevention critical**

**Threat Landscape Justification:**

**IBM X-Force 2025:**

- **84% uptick in phishing emails** delivering infostealers
- Attackers increasingly use domain impersonation to appear legitimate

**Verizon DBIR 2024:**

- Phishing and pretexting remain **top causes of costly data breaches** (42% of attack patterns in education sector)
- Email-based social engineering dominates across all industries

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **K12 SIX (2024):** Updated framework for 2024-25 now considers **SPF and DKIM baseline protections**
- **Low Adoption:** Only 16% of Virginia school districts have implemented DMARC, just 8% with enforcement policies (p=quarantine/reject)
- **Superintendent Impersonation:** Common attack pattern - attacker impersonates superintendent to request wire transfers from business office
- **Parent Phishing:** Attackers impersonate school officials to phish parents for credentials, payment information
- **Practical Implementation:** Google Workspace, Microsoft 365 have built-in SPF/DKIM/DMARC configuration; free DMARC monitoring tools (DMARC Analyzer, MXToolbox)

**Healthcare:**

- **CEO/CFO Impersonation:** Attackers target finance staff for wire transfers
- **Physician Impersonation:** Fake prescription requests, patient data requests
- **HIPAA:** Email authentication protects communications containing PHI from interception/manipulation
- **Practical Implementation:** Microsoft 365, Google Workspace built-in authentication

**Religious/Nonprofit:**

- **Pastor/Priest Impersonation:** Attackers impersonate clergy to request donations or wire transfers from parishioners or staff
- **Donor Trust:** Email authentication protects organization's reputation (prevents spoofed fundraising emails)
- **Practical Implementation:** Free DMARC monitoring tools, built-in authentication in email platforms

**General Organizations:**

- **CFO/CEO Impersonation:** Classic BEC attack pattern
- **Vendor Impersonation:** Fake invoices, payment requests
- **Brand Protection:** Prevents attackers from spoofing company domain for phishing customers

**Citations:**

- **Coalition:** "Email authentication (SPF, DKIM, DMARC) on cyber insurance checklist"
  - URL: https://www.coalitioninc.com/topics/authenticating-email-using-SPF-DKIM-&-DMARC
- **K12 SIX (2024):** "SPF and DKIM now baseline protections in updated framework"
  - URL: https://www.govtech.com/education/k-12/k12-six-releases-updated-framework-for-school-cybersecurity
- **Virginia School Data (2024):** "84.6% SPF adoption, only 16% DMARC adoption, 8% with enforcement"
- **Clever Education (2024):** "Schools should implement SPF, DKIM, DMARC to protect against spoofing"
  - URL: https://www.clever.com/blog/2024/06/email-security-for-education
- **FBI IC3:** BEC remains top cybercrime by financial loss across all sectors
- CIS Controls v8: Control 9 - Email and Web Browser Protections
- NIST CSF 2.0: PR.DS-5 - Protections against data leaks

---

### Question 5.6: API Security Controls 🆕

*(Note: This question is under consideration for removal/trading per AI_QUESTION_RECOMMENDATIONS.md. Included here for completeness but may be deprioritized.)*

**Question Text:**
For organizations using APIs (application programming interfaces) to integrate systems or provide services, are API security controls implemented including authentication (OAuth 2.0), authorization, rate limiting, and API activity monitoring?

**Impact Rating:** Moderate (3)

**Foundational:** NO - Comprehensive maturity indicator (NEW 2026)

**Control Description:**

API security controls protect application programming interfaces from abuse and exploitation:

**Authentication:**

- **OAuth 2.0:** Industry-standard authorization framework for API access
- **API Keys:** Unique keys for each API client (rotate regularly)
- **Mutual TLS:** Certificate-based authentication for high-security APIs

**Authorization:**

- **Role-Based Access Control (RBAC):** Different API permissions for different user roles
- **Attribute-Based Access Control (ABAC):** Fine-grained permissions based on attributes
- **Least-Privilege:** Grant minimum API permissions necessary

**Rate Limiting:**

- **Throttling:** Limit API requests per client (e.g., 1000 requests/hour)
- **DDoS Protection:** Prevent abuse, resource exhaustion
- **Quotas:** Different rate limits for different subscription tiers

**Input Validation:**

- **Prevent Injection Attacks:** Sanitize user inputs (SQL injection, XSS, command injection)
- **Schema Validation:** Enforce expected data types, formats

**API Activity Monitoring:**

- **Logging:** All API requests/responses logged
- **Anomaly Detection:** Unusual access patterns trigger alerts
- **SIEM Integration:** API logs fed into SIEM for correlation

**API Inventory:**

- **Discover All APIs:** Public, internal, partner APIs
- **Shadow APIs:** Undocumented or forgotten APIs
- **Version Tracking:** Deprecate old API versions

**Insurance Rationale (Universal):**

APIs represent emerging attack surface:

- **78% of security professionals** experienced API security breach in 2023
- **API vulnerabilities cost $2.5 billion** in 2024 (remediation, fines, lost revenue)

While not yet universal insurance requirement, insurers are beginning to assess API security as organizations adopt cloud-native architectures with extensive API usage.

**Threat Landscape Justification:**

**Industry Research (2024-2025):**

- **99% of surveyed organizations** experienced API security issue in prior 12 months (Q1 2025)
- Only 10% had API posture governance strategy
- Successful API-related compromises projected to grow through 2025

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Most schools don't develop APIs** directly (consume APIs from vendors)
- **API Usage:** Student information systems syncing with learning management systems, single sign-on integrations, rostering APIs for EdTech platforms
- **Limited Applicability:** Vendor API security covered by Questions 8.6-8.8 (vendor risk management)

**Healthcare:**

- **HL7 FHIR APIs:** Health Level 7 Fast Healthcare Interoperability Resources for EHR data exchange
- **Patient Portal APIs:** Mobile app access to patient data
- **Medical Device APIs:** Integration with hospital systems
- **HIPAA:** API security protects PHI transmission

**Religious/Nonprofit:**

- **Limited API Development:** Most nonprofits consume APIs, don't develop
- **Donor Portal APIs:** Mobile giving apps, online donation platforms
- **Low Applicability:** Unless organization develops custom applications

**General Organizations:**

- **Cloud-Native Applications:** Microservices architectures rely heavily on APIs
- **Customer-Facing APIs:** Mobile apps, partner integrations, webhooks

**Citations:**

- **CybelAngel (2025):** "78% of security professionals experienced API breach in 2023"
  - URL: https://cybelangel.com/blog/the-api-threat-report-2025/
- **Imperva (2024):** "API vulnerabilities cost $2.5 billion in 2024"
  - URL: https://www.imperva.com/blog/state-of-api-security-in-2024/
- **APIsec (2025):** "99% of orgs experienced API security issue in prior 12 months"
  - URL: https://www.apisec.ai/blog/apisec-presents-the-2024-api-security-market-report
- **OWASP API Security Top 10 (2023):** Industry-standard API security framework
  - URL: https://owasp.org/API-Security/

---

*Category 5 Complete: Malware Defense and Endpoint Security (6 questions total, including 2 NEW questions: 5.5 Email Authentication, 5.6 API Security)*

---


<a name="category-6"></a>
### Question 7.4: AI Acceptable Use Policy and Governance 🔑 FOUNDATIONAL 🆕

**Question Text:**
Has the organization established an Artificial Intelligence (AI) Acceptable Use Policy that defines approved AI tools, prohibited uses, data privacy requirements, and staff/stakeholder responsibilities when using AI technologies (ChatGPT, Google Gemini, Microsoft Copilot, AI-enabled platforms)?

**Response Options:**

- Fully implemented - documented policy, approved AI tools list, staff trained, usage monitored
- Partially implemented - informal guidance exists, no formal policy
- Not implemented - no AI acceptable use policy

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (NEW 2026 - Forward-Looking Control)

**Control Description:**

An AI Acceptable Use Policy (AUP) provides governance for organizational use of artificial intelligence technologies, addressing risks including data leakage, privacy violations, bias, and compliance failures. Effective AI policies include:

**Policy Components:**

- **Approved AI Tools:** List of vetted AI tools authorized for organizational use (Microsoft Copilot, Google Gemini Workspace, domain-specific AI tools)
- **Prohibited Uses:** Define unacceptable AI usage:

  - **Data Privacy:** Prohibit entering sensitive/confidential data into public AI tools (ChatGPT free tier, Claude web interface)
  - **Decision-Making:** Prohibit using AI for high-stakes decisions without human review (hiring, patient diagnosis, financial decisions)
  - **Academic/Professional Integrity:** Define plagiarism/citation requirements for AI-generated content
  - **Compliance:** Prohibit AI uses that violate regulations (FERPA, HIPAA, GDPR, copyright law)

- **Data Classification Integration:** Link AI policy to data classification (Question 3.6):

  - **Public Data:** May be used with any AI tool
  - **Internal Data:** Only use with enterprise AI tools (Microsoft 365 Copilot with data residency)
  - **Confidential/Regulated Data:** Prohibited from AI tools unless specifically approved (zero-retention AI services)

- **Responsible AI Principles:**

  - **Transparency:** Disclose when AI is used to generate content/decisions
  - **Accuracy Verification:** Require human review of AI outputs (AI hallucinations common)
  - **Bias Mitigation:** Awareness of AI bias in hiring, customer service, content generation
  - **Intellectual Property:** Respect copyright, avoid generating content that infringes IP

**Policy Implementation:**

- **Training:** Include AI acceptable use in annual security awareness training (Question 7.3)
- **Technical Controls:** Network monitoring for unauthorized AI tool usage, DLP policies blocking sensitive data to AI services
- **Vendor Vetting:** Evaluate AI tools via third-party risk management process (Question 8.8)
- **Incident Response:** Define procedures for AI-related incidents (data leakage, compliance violations)

**Insurance Rationale (Universal):**

**Emerging Insurance Requirement (2025-2026):**

- **Coalition "Affirmative AI Insurance"**: Coalition offers AI-specific cyber insurance coverage (2024 launch)
- **AI Policy Required:** Coalition recommends AI acceptable use policies for organizations using AI tools
- **Data Leakage Risk:** Insurers concerned about sensitive data entered into public AI tools (GDPR violations, HIPAA breaches)
- **Forward-Looking Control:** While not yet required by all insurers, AI governance anticipated to become standard requirement by 2026

**Compliance and Legal Risk:**

- **GDPR/Privacy Laws:** Using AI tools that process personal data may violate data residency/processing requirements
- **Regulatory Guidance:** NIST AI RMF (2023), EU AI Act (2024), emerging US state AI laws
- **AI-Specific Lawsuits:** Copyright lawsuits against AI companies; organizations must protect against derivative liability

**Sector-Specific Insurance Impact:**

- **Education:** AI policies protect student data (FERPA, state student privacy laws)
- **Healthcare:** AI policies protect PHI (HIPAA); FDA guidance on AI medical devices
- **General:** AI policies demonstrate due diligence, reduce insurer risk

**Threat Landscape Justification:**

**Data Leakage via AI Tools:**

- **Samsung Leak (2023):** Engineers entered proprietary code into ChatGPT; Samsung banned ChatGPT
- **Amazon Leak (2023):** Employees entered confidential data into ChatGPT
- **Public AI Tools:** ChatGPT, Claude (web), Gemini (free) retain user inputs for model training (data leakage risk)
- **Enterprise AI Tools:** Microsoft 365 Copilot, Google Gemini Workspace offer data residency, zero-retention options

**AI-Powered Threats:**

- **67.4% of phishing uses generative AI** (Zscaler 2024), creating more convincing attacks
- **Deepfakes:** AI-generated voice/video used for social engineering, financial fraud
- **AI policy must address both** defensive (how we use AI safely) and offensive (how attackers use AI against us) dimensions

**Compliance Violations:**

- **FERPA/COPPA Violations:** Teachers entering student data into public AI tools violates student privacy laws
- **HIPAA Violations:** Healthcare staff entering PHI into ChatGPT triggers breach notification requirements
- **AI policy prevents unintentional compliance violations**

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Approved Tools:** Microsoft Copilot (M365 Education), Google Gemini (Workspace Education), approved educational AI platforms (Khan Academy Khanmigo)
- **Prohibited Uses:**

  - Entering student names, IDs, grades, IEPs, disciplinary records into public AI tools (FERPA violation)
  - Using AI to generate entire lesson plans without review (quality/accuracy concerns)
  - Students using AI for assignments without disclosure (academic integrity)

- **Practical Implementation:**

  - **Teacher Guidance:** "Use AI for brainstorming lesson ideas, but don't enter student-specific information"
  - **Student Policy:** Define AI citation requirements, prohibited uses for assignments
  - **Enterprise AI Adoption:** Microsoft Copilot for Education provides FERPA-compliant AI assistance

- **K-12 Specific Risks:** Teachers may not understand FERPA implications of AI; policy must be clear and accessible

**Healthcare:**

- **Approved Tools:** HIPAA-compliant AI tools with BAAs (Business Associate Agreements), enterprise AI platforms
- **Prohibited Uses:**

  - Entering PHI (patient names, diagnoses, medical record numbers) into public AI tools (HIPAA breach)
  - Using AI for clinical decision-making without physician oversight (FDA, standard of care concerns)
  - AI-generated clinical documentation without physician review

- **Practical Implementation:**

  - **Clinical Staff Training:** "Never enter patient-identifiable information into ChatGPT or public AI tools"
  - **AI Medical Devices:** Vet AI-enabled medical devices via vendor risk management (Question 8.8)
  - **Enterprise AI:** Microsoft Azure Health Bot, Google Cloud Healthcare AI (HIPAA-compliant options)

- **Compliance:** HIPAA breach notification required if PHI entered into non-compliant AI tools

**Religious/Nonprofit:**

- **Approved Tools:** Enterprise AI tools (Microsoft 365 Copilot), free tools for non-sensitive data
- **Prohibited Uses:**

  - Entering donor names, donation amounts, addresses into public AI tools (privacy, donor confidence)
  - Using AI to generate fundraising appeals without review (accuracy, brand voice)
  - AI-generated content without attribution (ethical concerns)

- **Practical Implementation:**

  - **Staff Guidance:** "Use AI for drafting communications, but don't include donor data"
  - **Budget-Conscious:** Define when free AI tools acceptable (public content generation) vs. when enterprise tools required (donor data analysis)
  - **Donor Trust:** AI policy demonstrates responsible stewardship of donor information

**General Organizations:**

- **Approved Tools:** Enterprise AI platforms (Microsoft Copilot, Google Gemini, AWS Bedrock), industry-specific AI tools
- **Prohibited Uses:**

  - Entering trade secrets, proprietary code, customer PII into public AI tools
  - Using AI for high-stakes decisions (hiring, credit decisions, legal analysis) without human review
  - AI-generated content that may infringe copyright

- **Compliance:** GDPR (EU), CCPA (California), NYDFS (New York financial services), industry-specific regulations
- **Competitive Risk:** Data leakage to AI providers may benefit competitors (AI learns from inputs)

**Citations:**

- **NIST AI Risk Management Framework (AI RMF 1.0, January 2023):** Voluntary framework for AI governance
- **Coalition Cyber Insurance:** "Affirmative AI Insurance" product launched 2024; recommends AI acceptable use policies
- **Zscaler ThreatLabz 2024:** "67.4% of phishing campaigns use generative AI"
- **EU AI Act (2024):** Regulation of high-risk AI systems in EU
- **Samsung ChatGPT Ban (2023):** Example of data leakage risk
- **FERPA:** Prohibits disclosure of student education records; applies to AI tools
- **HIPAA:** PHI entered into non-compliant AI tools constitutes breach
- **NIST CSF 2.0:** GV.RR-3 (Organizational leadership is responsible for managing technology risk)
- CIS Controls v8: Control 1.1 (Establish and Maintain Detailed Enterprise Asset Inventory) - adapted for AI tool inventory

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

### Question 9.7: Incident Detection and Response Capabilities (MTTD/MTTR) 🆕

**Question Text:**
Does the organization measure and track incident detection and response metrics such as Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR)?

**Response Options:**

- Fully implemented - MTTD/MTTR tracked, continuous improvement process, metrics reported to leadership
- Partially implemented - informal metrics tracking, no continuous improvement
- Not implemented - no incident detection/response metrics

**Impact Rating:** High (5)

**Foundational:** No (but emerging best practice)

**Control Description:**

Incident detection and response metrics enable organizations to measure IR effectiveness and drive continuous improvement. Key metrics include:

**Key IR Metrics:**

- **Mean Time to Detect (MTTD):** Average time from incident occurrence to detection
  - **Industry Average:** 212 days (IBM Cost of Data Breach 2024)
  - **Target:** <24 hours for mature organizations

- **Mean Time to Respond (MTTR):** Average time from detection to containment
  - **Target:** <1 hour for critical incidents

- **Mean Time to Recover (MTTR Recovery):** Average time to restore normal operations
  - **Ransomware Average:** 21 days without tested plan, 5-7 days with tested plan

**Additional IR Metrics:**

- **Incident Count:** Number of incidents by type, severity
- **False Positive Rate:** SIEM alerts requiring investigation vs. true incidents
- **Escalation Time:** Time to escalate incidents to IR team, executives
- **Breach Notification Compliance:** % of breaches notified within legal deadlines

**Metrics Tracking:**

- **SIEM/Security Tools:** Automated MTTD tracking via SIEM alert timestamps
- **Incident Tickets:** Track MTTR via incident ticketing systems
- **Quarterly Reviews:** Review IR metrics quarterly; identify trends, improvement opportunities
- **Executive Reporting:** Report key metrics to executives, board (demonstrates IR maturity)

**Insurance Rationale (Universal):**

**Emerging Insurer Interest:**

- Some cyber insurers request **MTTD/MTTR metrics** during policy renewal (demonstrates IR maturity)
- Organizations with mature IR metrics may receive **premium discounts**

**Faster Detection = Lower Costs:**

- **IBM Cost of Data Breach 2024:** Breaches detected in <200 days cost $1M less than breaches detected in 200+ days
- Insurers pay lower claims for organizations with fast detection, response

**Continuous Improvement:**

- IR metrics drive continuous improvement (reduce MTTD from 30 days to 5 days → lower breach costs)
- Demonstrates organizational commitment to IR maturity

**Threat Landscape Justification:**

**Long Detection Times:**

- **Average MTTD: 212 days** (IBM 2024)
- Attackers have 7+ months to exfiltrate data, deploy ransomware, cover tracks
- MTTD metrics drive investment in detection capabilities (SIEM, EDR, threat hunting)

**Dwell Time Reduction:**

- **Dwell time:** Time from initial compromise to detection
- Reducing dwell time from months to days/hours limits attacker impact

**Incident Response Maturity:**

- Organizations tracking MTTD/MTTR are in top quartile of IR maturity
- Metrics enable continuous improvement culture

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Metrics Tracking:** Track MTTD for phishing incidents (via email security tools), ransomware, unauthorized access
- **Practical Implementation:** Simple spreadsheet tracking incident dates, detection dates, containment dates
- **SIEM Integration:** Higher ed institutions with SIEMs can automate MTTD tracking
- **Goal Setting:** Reduce MTTD from weeks to days over time

**Healthcare:**

- **Patient Safety Metrics:** Track MTTR for incidents affecting patient care (EHR downtime, medical device compromises)
- **HIPAA Breach Metrics:** Track time to HIPAA breach notification (60-day compliance)
- **24/7 Operations:** Healthcare requires fast MTTR (target <1 hour for critical incidents)
- **Continuous Monitoring:** SIEM integration for automated MTTD tracking

**Religious/Nonprofit:**

- **Limited Resources:** Simple metrics tracking (spreadsheet); focus on high-impact incidents (ransomware, data breaches)
- **Quarterly Reviews:** Review IR metrics quarterly; identify patterns (e.g., phishing incidents increasing → more training)
- **Donor Reporting:** Report IR metrics to board, major donors (demonstrates security stewardship)

**General Organizations:**

- **Enterprise IR Maturity:** Automated MTTD/MTTR tracking via SIEM, SOAR platforms
- **SOC Metrics:** 24/7 SOCs track MTTD/MTTR for all alerts, incidents
- **Industry Benchmarking:** Compare MTTD/MTTR to industry benchmarks (IBM, Verizon reports)
- **Compliance:** SOC 2, ISO 27001 increasingly expect IR metrics

**Citations:**

- **IBM Cost of Data Breach 2024:** Average MTTD 212 days; breaches detected <200 days cost $1M less
- **Veeam Ransomware Trends 2024:** Average ransomware recovery 21 days
- **NIST CSF 2.0:** DE.CM-7 (Monitoring for unauthorized personnel, connections, devices, and software is performed), RS.AN-6 (Actions performed during an investigation are recorded)
- CIS Controls v8: Control 8.11 (Conduct Reviews of Audit Logs)
- **SANS Incident Response Metrics:** Best practices for MTTD/MTTR tracking

---

**END OF CATEGORY 9**

---

## APPENDIX: Comprehensive Citations and References

This appendix provides a centralized list of all sources cited throughout the Comprehensive Cybersecurity Risk Assessment Questionnaire, organized by source type for easy reference.

---

### Cybersecurity Frameworks and Standards

**NIST Cybersecurity Framework (CSF) 2.0**

- Published: February 2024
- National Institute of Standards and Technology
- Sector-agnostic cybersecurity framework with six functions: Govern, Identify, Protect, Detect, Respond, Recover
- URL: https://www.nist.gov/cyberframework
- Usage: Primary framework alignment for all questions

**CIS Controls v8**

- Published: May 2021
- Center for Internet Security
- 18 security controls organized into Implementation Groups (IG1, IG2, IG3)
- URL: https://www.cisecurity.org/controls/v8
- Usage: Control mapping for all categories

**NIST AI Risk Management Framework (AI RMF 1.0)**

- Published: January 2023
- National Institute of Standards and Technology
- Voluntary framework for AI governance with functions: Govern, Map, Measure, Manage
- URL: https://www.nist.gov/itl/ai-risk-management-framework
- Usage: AI-related questions (7.4, 8.8)

**NIST SP 800-61 Revision 2: Computer Security Incident Handling Guide**

- Published: August 2012
- Comprehensive guide for incident response
- URL: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf
- Usage: Category 9 (Incident Response)

**NIST SP 800-88: Guidelines for Media Sanitization**

- Published: December 2014 (Revision 1)
- Standards for secure data destruction
- Usage: Vendor off-boarding (8.5), data disposal

**ISO/IEC 27001:2022**

- International Organization for Standardization
- International standard for information security management systems
- Usage: Vendor certifications (8.6), compliance references

---

### Threat Intelligence and Breach Reports

**IBM X-Force Threat Intelligence Index 2025**

- IBM Security
- Annual threat intelligence report
- Key Finding: Account abuse is #1 initial access vector (30% of incidents)
- Usage: Threat landscape justifications throughout

**Verizon Data Breach Investigations Report (DBIR) 2024**

- Verizon Business
- Annual analysis of global data breaches
- Key Findings:

  - 68% of breaches involve human element
  - 36% of breaches involved phishing
  - 75% of breaches include ransomware
  - 88% of breaches involve stolen credentials
  - Third-party breaches doubled from 2022 to 2024
- URL: https://www.verizon.com/business/resources/reports/dbir/
- Usage: Most frequently cited source for threat statistics

**IBM Cost of Data Breach Report 2024**

- IBM Security and Ponemon Institute
- Annual study of data breach costs
- Key Findings:

  - Average breach cost: $4.45M globally, $9.48M in healthcare
  - Average detection time: 212 days
  - Breaches detected in <200 days cost $1M less
- Usage: Breach cost, detection time statistics

**Zscaler ThreatLabz 2024**

- Zscaler
- Key Finding: 67.4% of phishing campaigns now use generative AI
- Usage: AI-powered phishing threat justifications

**Veeam Ransomware Trends Report 2024**

- Veeam Software
- Annual ransomware study
- Key Findings:

  - Average ransomware recovery: 21 days without plan, 5-7 days with tested plan
- Usage: Backup testing, disaster recovery, incident response

**Sophos State of Ransomware 2024**

- Sophos
- Annual ransomware survey
- Key Findings:

  - Average ransom payment: $1.54M
  - Average ransomware recovery cost: $2.73M (including downtime)
- Usage: Ransomware financial impact

**Ponemon Third-Party Risk Study 2024**

- Ponemon Institute
- Annual third-party risk research
- Key Findings:

  - 54% of organizations experienced third-party data breach in past year
  - Organizations with vendor assessment processes experience 40% fewer third-party incidents
- Usage: Vendor risk management (Category 8)

**KnowBe4 Phishing Report 2024**

- KnowBe4
- Annual phishing simulation benchmarking
- Key Findings:

  - Organizations with training experience 70% fewer successful phishing attacks
  - Organizations conducting monthly simulations reduce click rates from 30%+ to <5% within 12 months
- Usage: Security awareness training (Category 7)

---

### Insurance Industry Sources

**Coalition Cyber Insurance**

- Coalition, Inc.
- Major cyber insurance carrier
- Key Offerings:

  - "Affirmative AI Insurance" product (2024 launch)
  - Recommends AI acceptable use policies, AI tool vetting
  - Requires: Weekly offline backups, MFA, EDR, annual training, phishing simulation
- Usage: Insurance requirements throughout questionnaire

**Securden PAM Market Report**

- Securden
- Key Finding: 42% of organizations in 2024 required to have PAM for cyber insurance coverage (up from 36% in 2023)
- Usage: PAM foundational control justification (Question 3.5)

**National Association of Insurance Commissioners (NAIC)**

- NAIC
- Cyber insurance market data and regulatory guidance
- Usage: Cyber insurance coverage (Question 9.5)

---

### Regulatory and Compliance References

**HIPAA (Health Insurance Portability and Accountability Act)**

- U.S. Department of Health and Human Services (HHS)
- Healthcare privacy and security regulations
- Key Requirements:

  - 45 CFR § 164.308(a)(5) - Annual security awareness training required
  - 45 CFR § 164.308(a)(6) - Security incident procedures required
  - 45 CFR § 164.308(a)(7) - Contingency plan (backup, disaster recovery, emergency mode operations)
  - 45 CFR § 164.308(b) - Business Associate Agreements required
  - 45 CFR § 164.404-164.408 - Breach notification (60 days for breaches affecting 500+ individuals)
  - 45 CFR § 164.410 - Business associates must notify covered entities of breaches
- Usage: Healthcare sector context throughout

**FERPA (Family Educational Rights and Privacy Act)**

- U.S. Department of Education
- Student data privacy law
- Requirements:

  - Prohibits disclosure of student education records
  - Applies to AI tools processing student data
  - Vendors must sign FERPA Data Privacy Agreements
  - Student data breach notification to Department of Education required
- Usage: Education sector context throughout

**GDPR (General Data Protection Regulation)**

- European Union
- EU data protection regulation
- Key Requirements:

  - Article 28 - Data Processing Agreements required for vendors
  - Article 33 - 72-hour breach notification to Data Protection Authorities
  - Right to erasure (applies to AI tool data retention)
  - Maximum fines: €20M or 4% of global annual revenue
- Usage: International compliance, AI tool vetting

**CCPA (California Consumer Privacy Act)**

- California, USA
- Cal. Civ. Code § 1798.82 - Breach notification requirements
- California Attorney General notification required for breaches
- Usage: State privacy law compliance

**PCI DSS 4.0 (Payment Card Industry Data Security Standard)**

- PCI Security Standards Council
- Security standard for payment card processing
- Key Requirements:

  - Requirement 8.2.2 - MFA for vendor access
  - Requirement 12.6 - Annual security awareness training required
  - Requirement 12.8 - Manage service providers (vendor risk management)
  - Requirement 12.10 - Incident response plan required
  - Requirement 12.10.6 - Test IR plan annually (tabletop exercises allowed)
- Usage: Payment card compliance, general security requirements

**COPPA (Children's Online Privacy Protection Act)**

- U.S. Federal Trade Commission (FTC)
- Privacy protection for children under 13
- Usage: K-12 education context, AI tool vetting

**EU AI Act (2024)**

- European Union
- Regulation of high-risk AI systems in EU
- Compliance required for EU AI uses
- Usage: AI governance (Questions 7.4, 8.8)

**NYDFS Cybersecurity Regulation**

- New York Department of Financial Services
- Cybersecurity requirements for financial services in New York
- Requires annual security awareness training
- Usage: Financial services compliance

---

### Industry Certifications and Auditing Standards

**SOC 2 (Service Organization Control 2)**

- AICPA (American Institute of CPAs)
- Auditing standard for service organizations
- Type II reports audit security, availability, confidentiality controls over 6-12 month period
- Trust Services Criteria: Security, Availability, Processing Integrity, Confidentiality, Privacy
- Usage: Vendor certifications (8.6), compliance alignment throughout

**HITRUST CSF (Health Information Trust Alliance Common Security Framework)**

- HITRUST Alliance
- Healthcare-specific framework combining HIPAA, NIST, ISO requirements
- Preferred certification in healthcare sector
- Usage: Healthcare vendor certifications

**FedRAMP (Federal Risk and Authorization Management Program)**

- U.S. General Services Administration (GSA)
- Cloud security authorization for U.S. federal government vendors
- Usage: Government contractor requirements

**StateRAMP**

- State-level cloud security authorization
- Usage: State government vendor requirements

**ISO 22301**

- International Organization for Standardization
- International standard for Business Continuity Management Systems
- Usage: Business continuity planning (6.5)

---

### Government and CISA Resources

**CISA (Cybersecurity and Infrastructure Security Agency)**

- U.S. Department of Homeland Security
- Free resources:

  - Tabletop exercise packages for various sectors
  - Security awareness training modules
  - Cyber hygiene services
  - Vulnerability scanning (CISA Cyber Hygiene Services)
- URL: https://www.cisa.gov
- Usage: Free resources for budget-conscious organizations, tabletop exercises

**FBI Cyber Division**

- Federal Bureau of Investigation
- Resources:

  - FBI Healthcare Cyber Threat Briefs
  - Cyber incident reporting (IC3.gov)
- Usage: Law enforcement engagement, incident response

**U.S. Secret Service**

- Electronic Crimes Task Forces
- Usage: Law enforcement engagement for financial crimes, cyber extortion

**HHS Office for Civil Rights (OCR)**

- U.S. Department of Health and Human Services
- HIPAA enforcement, breach notification portal
- Usage: Healthcare breach notification, HIPAA compliance

---

### Educational and Nonprofit Sector Resources

**CoSN (Consortium for School Networking)**

- K-12 education technology association
- Resources:

  - Education vendor assessment tools
  - Model FERPA Data Privacy Agreements
  - EdTech security mailing lists
- Usage: K-12 education resources

**Future of Privacy Forum**

- Privacy advocacy organization
- Student data privacy resources
- Model Data Privacy Agreements
- Usage: Education privacy compliance

**Student Privacy Pledge**

- Studentprivacypledge.org
- Vendor commitment to student data privacy
- Usage: Education vendor vetting

---

### AI Governance and Tools

**Microsoft Commercial Data Protection**

- Microsoft Corporation
- Zero-retention AI for Microsoft 365 Copilot
- FERPA-compliant, HIPAA-compliant (BAA available), SOC 2 certified
- Enterprise AI with data residency controls
- Usage: Approved enterprise AI tool example

**Google Workspace AI Data Use Policy**

- Google LLC
- "Your data is your data" - not used for model training
- Google Gemini for Workspace: FERPA-compliant, HIPAA-compliant (BAA available), SOC 2 certified
- Usage: Approved enterprise AI tool example

**AWS Bedrock**

- Amazon Web Services
- Customer-controlled AI models, data not used for training
- HIPAA-eligible, SOC 2 certified
- Usage: Approved enterprise AI tool example

**OpenAI, Anthropic, Google (Public AI Tools)**

- Public AI tools (ChatGPT free, Claude web, Gemini free) retain user inputs for model training
- Not suitable for sensitive/confidential data without enterprise agreements
- Usage: Examples of prohibited AI tools for sensitive data

**Samsung ChatGPT Ban (2023)**

- Samsung Electronics
- Example incident: Engineers entered proprietary code into ChatGPT
- Samsung subsequently banned ChatGPT
- Usage: Data leakage risk example for AI tools

**Amazon AI Data Leak (2023)**

- Amazon
- Employees entered confidential Amazon data into ChatGPT
- Usage: Data leakage risk example

---

### Notable Incidents and Examples

**SolarWinds Supply Chain Attack (2020)**

- 18,000 organizations compromised via supply chain attack
- State-sponsored attack affecting government agencies, Fortune 500 companies
- Usage: Supply chain risk, vendor access management

**Kaseya Ransomware Attack (2021)**

- Managed service provider (MSP) compromise
- 1,500 downstream organizations ransomwared via MSP access
- Usage: Vendor access risk, supply chain attacks

**MOVEit Breach (2023)**

- File transfer vendor breach
- Affected 2,000+ organizations
- Zero-day vulnerability exploited
- Usage: Vendor continuous monitoring, third-party risk

**Colonial Pipeline Ransomware (2021)**

- $4.4M ransom paid
- Backup restoration too slow (untested backups)
- Usage: Backup testing importance

**Baltimore Ransomware (2019)**

- Untested backups incomplete
- City paid $18M in recovery costs
- Usage: Backup testing failure example

**Scripps Health Ransomware (2021)**

- 30-day recovery without tested disaster recovery plan
- $113M total recovery cost
- Usage: Disaster recovery planning importance

**Change Healthcare Breach (2024)**

- Major healthcare data breach affecting millions
- EHR vendor breach
- Usage: Healthcare vendor incident example

**PowerSchool Breach (2024)**

- Student information system vendor breach
- Affected K-12 districts with student data exposure
- Usage: Education vendor incident example

**Blackbaud Ransomware (2020)**

- Donor management system vendor breach
- Affected thousands of nonprofits
- Organizations with incident notification clauses responded faster
- Usage: Nonprofit vendor incident, incident notification importance

---

### Additional Industry Sources

**Gartner**

- IT research and advisory firm
- Key Stat: Average cost of IT downtime $5,600/minute
- Usage: Disaster recovery cost justification

**SANS Institute**

- Cybersecurity training and certification
- Resources:

  - Incident Response Plan templates
  - Security Awareness training (free resources)
  - Incident Response Metrics best practices
- Usage: Incident response guidance, training resources

**National Conference of State Legislatures (NCSL)**

- State breach notification law tracker
- All 50 US states have data breach notification laws (timelines vary: 30-90 days)
- Usage: Breach notification compliance

**U.S. Department of Education**

- FERPA enforcement
- Student data breach notification recipient
- K-12 cybersecurity resources
- Usage: Education compliance, student data breaches

**Khan Academy Khanmigo**

- Education-specific AI platform
- FERPA-compliant, SOC 2 certified
- Usage: Approved AI tool for education

**Salesforce Nonprofit Cloud / Blackbaud**

- Donor management systems
- Both have SOC 2 certifications
- Usage: Nonprofit vendor examples

**HealthStream, Relias**

- Healthcare training platforms
- HIPAA training modules
- Usage: Healthcare training resources

**Nuance DAX (Dragon Ambient eXperience)**

- Clinical documentation AI
- HIPAA-compliant, SOC 2 certified, BAA available
- Usage: Healthcare-approved AI tool

**Microsoft Azure Health Bot / Google Cloud Healthcare AI**

- HIPAA-compliant AI platforms for healthcare
- BAAs available, PHI processing controls
- Usage: Healthcare AI tools

---

### Framework Cross-References

**Trust Requirements for Education (The Trust Insurance Pool)**

- 7 simplified cyber requirements for K-12 education insurance
- Maps to 12 foundational questions in this assessment
- Requirements:

  1. End-of-life software management (Q1.4)
  2. Multi-factor authentication (Q2.3-2.6)
  3. Patch management (Q4.3)
  4. External vulnerability scanning (Q4.7)
  5. EDR/Antivirus deployment (Q5.4)
  6. Air-gapped backups + backup testing (Q6.3-6.4)
  7. Phishing simulation + security awareness training (Q7.2-7.3)
- Usage: Foundational questions mapping

**CyberPools Insurance Pools**

- K-12 Education pools (SSCIP, The Trust, VSBIT)
- Healthcare expansion (Vitalant)
- Religious organizations (Christian Brothers Services)
- Usage: Multi-sector insurance context

---

**END OF APPENDIX**

---


