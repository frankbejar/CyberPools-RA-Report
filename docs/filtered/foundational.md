---
title: Foundational Questions (17)
tags:
  - Foundational
  - Insurance Critical
---

# 🔑 Foundational Questions

These 17 questions are **insurance-critical** controls required by most cyber insurance carriers.

**12 Existing Foundational** (Trust Requirements for Education):
- 1.4: End-of-Life Software Management
- 2.3-2.6: Multi-Factor Authentication (4 questions)
- 4.3: Patch Management
- 4.7: External Vulnerability Scanning
- 5.4: EDR/Antivirus Deployment
- 6.3-6.4: Air-gapped Backups + Testing
- 7.2-7.3: Phishing Simulation + Training

**5 NEW Foundational** (2026 Additions):
- 3.5: Privileged Access Management (PAM)
- 4.14: Centralized Logging and SIEM
- 5.5: Email Authentication (DMARC/SPF/DKIM)
- 7.4: AI Acceptable Use Policy
- 8.8: AI Tool Privacy and Security Vetting

---

### Question 1.4: End-of-Life Software Management 🔑 FOUNDATIONAL

**Question Text:**
Has the organization identified and removed or isolated all software and operating systems that are end-of-life (no longer supported by the vendor)?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #1 for Education)

**Control Description:**

End-of-life (EOL) software is software that the vendor no longer supports with security patches or updates. Common examples:

- **Operating Systems:** Windows Server 2008/2012, Windows 7/8, macOS versions older than 3 years, Ubuntu LTS past support date
- **Applications:** Adobe Flash, Internet Explorer, older versions of Java, Microsoft Office 2010/2013
- **Databases:** SQL Server 2008, Oracle 11g, MySQL 5.5
- **Web Servers:** Apache 2.2, IIS 6.0

**EOL Software Management Process:**

1. **Discovery:** Identify all EOL software via software inventory (see Question 1.2)
2. **Risk Assessment:** Evaluate business criticality and exposure (internet-facing vs. internal)
3. **Mitigation Options:**

    - **Upgrade:** Migrate to supported version (preferred)
    - **Replace:** Migrate to alternative supported software
    - **Isolate:** Network segmentation if immediate replacement impossible (temporary)
    - **Decommission:** Turn off if no longer needed
4. **Timeline:** Establish upgrade/replacement timeline (typically 6-12 months)
5. **Exceptions:** Document exceptions with compensating controls (air-gapped systems, vendor-managed medical devices)

**Insurance Rationale (Universal):**

**Critical Insurance Concern:**

- EOL software has **known, unpatched vulnerabilities** that attackers actively exploit
- **WannaCry ransomware (2017):** Exploited Windows XP/Server 2003 systems (EOL at time)
- **NotPetya (2017):** Similar exploitation of unsupported systems

Cyber insurance carriers:

- May **deny coverage** for breaches originating from EOL software (negligence)
- Require attestation that EOL software has been removed or isolated
- Some carriers offer reduced premiums for organizations with no EOL software

**Threat Landscape Justification:**

- **50% of perimeter vulnerabilities remain unpatched** (Verizon DBIR 2024)
- EOL software creates **permanent vulnerability** (patches will never be released)
- Attackers maintain exploit databases for EOL software (Windows XP, Server 2008)
- **Supply chain attacks:** Outdated web servers, databases enable attackers to compromise organizations

**Sector-Specific Context:**

**Education:**

- **Common EOL Software:** Windows Server 2008/2012 running student information systems, older macOS on teacher laptops, Adobe Flash for legacy learning content
- **Challenge:** Budget constraints delay upgrades; testing compatibility with educational software
- **FERPA:** EOL systems with student data create data breach risk

**Healthcare:**

- **Common EOL Software:** Windows XP/7 embedded in medical devices (infusion pumps, imaging equipment), older EHR systems
- **Challenge:** Medical devices have long lifecycles (10-15 years); vendor controls firmware updates
- **HIPAA 2025 Security Rule:** Enhanced security requirements may mandate medical device upgrades
- **Compensating Controls:** Network segmentation isolates medical devices from general network

**Religious/Nonprofit:**

- **Common EOL Software:** Windows Server 2008 for file sharing, Office 2010, outdated accounting software
- **Challenge:** Limited IT budgets, reliance on donated equipment, lack of IT expertise

**General:**

- **Common EOL Software:** Legacy industrial control systems (OT/ICS), mainframes, specialized business applications
- **Challenge:** Custom applications built for EOL platforms, high migration costs

**Citations:**

- **The Trust (Education Insurance):** Requirement #1 - End-of-life software management
- **Coalition:** Cyber insurance applications ask: "Are any systems running unsupported operating systems?"
- CIS Controls v8: Control 2.2 (Ensure Authorized Software is Currently Supported)
- NIST CSF 2.0: ID.AM-2 (Software inventory), PR.IP-2 (Secure software development lifecycle)
- **WannaCry Case Study:** 2017 ransomware attack exploited Windows XP/Server 2003 (EOL), cost organizations $4 billion globally

---

*(Continuing in next message due to length...)*


<a name="category-2"></a>
### Question 2.3: MFA for Remote Access/VPN 🔑 FOUNDATIONAL

**Question Text:**
Does the organization require multi-factor authentication (MFA) for all remote access, including VPN connections?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #2 for Education)

**Control Description:**

Multi-factor authentication (MFA) requires two or more verification factors:

- **Something you know:** Password, PIN
- **Something you have:** Smartphone app (authenticator), hardware token, SMS code
- **Something you are:** Biometric (fingerprint, facial recognition)

**Remote Access MFA Implementation:**

- **VPN:** MFA required before VPN connection established (Cisco AnyConnect, Palo Alto GlobalProtect with Duo/Okta/Azure MFA)
- **Remote Desktop (RDP):** MFA via gateway or conditional access policies
- **SSH:** Public key authentication with MFA for privileged access
- **Cloud VPN:** Azure VPN Gateway, AWS Client VPN with MFA integration

**MFA Methods (Ranked by Security):**

1. **FIDO2/WebAuthn Hardware Keys** (Yubikey, Titan) - Phishing-resistant
2. **Authenticator Apps** (Microsoft Authenticator, Google Authenticator, Duo Push) - Time-based codes or push notifications
3. **SMS Codes** (Least secure but better than no MFA) - Vulnerable to SIM swapping

**Exceptions and Conditional Access:**

- Trusted devices/locations may reduce MFA prompts (remember device for 30 days)
- Service accounts require alternative MFA methods (certificate-based authentication)

**Insurance Rationale (Universal):**

**CRITICAL Insurance Requirement:**

- **82% of cyber insurance claims** involved organizations lacking MFA (Coalition 2024)
- **Most ransomware attacks** start with compromised VPN credentials (Coalition 2025 Threat Index)
- Cyber insurance carriers **require MFA attestation** in applications; many deny coverage without MFA

Coalition, Chubb, Corvus all list VPN/remote access MFA as **mandatory** control.

**Threat Landscape Justification:**

- **IBM X-Force 2025:** Most ransomware attacks start with compromised VPNs and remote access credentials
- **Verizon DBIR 2024:** Remote access exploitation is top attack path; MFA prevents 99.9% of automated credential attacks
- **COVID-19 Impact:** Remote work explosion increased VPN attack surface permanently

**Sector-Specific Context:**

**Education:**

- **Remote Access Needs:** IT staff, administrators, teachers accessing systems from home
- **Summer/Weekend Access:** Custodians, maintenance staff working outside business hours
- **Challenge:** Training non-technical staff on MFA usage; smartphone app deployment

**Healthcare:**

- **Clinical Remote Access:** Physicians on-call, telehealth providers, remote nurses
- **HIPAA:** Remote access to PHI requires strong authentication
- **Challenge:** 24/7 access needs; MFA fatigue for frequently logging in staff

**Religious/Nonprofit:**

- **Remote Staff:** Ministry staff, accountants, volunteer coordinators working remotely
- **Challenge:** Limited IT budget for MFA solutions; smartphone ownership among older volunteers

**Citations:**

- **The Trust (Education Insurance):** Requirement #2 - Multi-Factor Authentication
- **Coalition:** "82% of cyber insurance claims involved orgs lacking MFA"
- **IBM X-Force 2025:** "Most ransomware attacks start with compromised VPNs"
- CIS Controls v8: Control 6.3 (Require MFA for Externally-Exposed Applications)
- NIST CSF 2.0: PR.AC-7 (Users are authenticated)
- HIPAA Security Rule: §164.312(d) - Person or entity authentication

---


### Question 2.4: MFA for Cloud Services 🔑 FOUNDATIONAL

**Question Text:**
Does the organization require multi-factor authentication (MFA) for all cloud services and SaaS applications (Microsoft 365, Google Workspace, AWS, Azure, etc.)?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #2 for Education)

**Control Description:**

Cloud services MFA covers:

- **Microsoft 365:** Azure AD MFA for all users (email, Teams, SharePoint, OneDrive)
- **Google Workspace:** 2-Step Verification for all users (Gmail, Drive, Calendar, Classroom)
- **AWS/Azure/GCP:** MFA for console access and privileged operations
- **SaaS Applications:** Single Sign-On (SSO) with MFA for all business applications (Salesforce, Workday, etc.)

**Implementation Methods:**

- **Microsoft 365:** Azure AD Conditional Access policies enforcing MFA
- **Google Workspace:** 2-Step Verification enforcement via Admin console
- **SSO Platforms:** Okta, Azure AD, Google Identity with MFA enforcement
- **Per-Application MFA:** Individual apps with built-in MFA if SSO not available

**Conditional Access Policies:**

- Require MFA for all users, all apps
- Exception: Trusted locations (on-premises network) may reduce MFA frequency
- Risk-based MFA: Higher risk sign-ins trigger MFA even from trusted locations

**Insurance Rationale (Universal):**

Cloud services store critical organizational data:

- **Education:** Student education records in Google Classroom, Microsoft Teams
- **Healthcare:** Patient health information in cloud EHR, telehealth platforms
- **Religious/Nonprofit:** Donor financial data in cloud accounting, donor management
- **General:** Customer data, financial records, intellectual property

**Email compromise** (no MFA) is top cause of business email compromise (BEC) attacks costing billions annually.

Coalition, Chubb, Corvus **require MFA for cloud email** specifically as mandatory control.

**Threat Landscape Justification:**

- **84% increase in phishing emails** delivering infostealers (IBM X-Force 2025)
- **BEC Attacks:** Attackers compromise cloud email accounts to impersonate executives for wire fraud
- **Cloud Account Takeover:** Compromised Microsoft 365/Google accounts used to access all connected services

**Sector-Specific Context:**

**Education:**

- **Microsoft 365 Education / Google Workspace for Education:** Primary platforms for student/staff collaboration
- **Student Data Access:** Teachers access student records via cloud SIS (Infinite Campus, PowerSchool cloud)
- **FERPA:** Cloud services with education records require strong authentication

**Healthcare:**

- **Cloud EHR:** Epic MyChart, Cerner cloud, athenahealth
- **Telemedicine:** Zoom Healthcare, Doxy.me, Microsoft Teams for Healthcare
- **HIPAA:** Business Associate Agreements require MFA for cloud services with PHI

**Religious/Nonprofit:**

- **Cloud Accounting:** QuickBooks Online, Xero with financial data
- **Donor Management:** Blackbaud, Planning Center Online with donor PII
- **Microsoft 365/Google Workspace:** Ministry communications, donor emails

**Citations:**

- **The Trust (Education Insurance):** Requirement #2 - MFA for cloud services
- **Coalition:** MFA for cloud email specifically required
- CIS Controls v8: Control 6.3 (Require MFA for Externally-Exposed Applications)
- NIST CSF 2.0: PR.AC-7 (Users are authenticated)
- **Microsoft 365 Security Baseline:** MFA required for all users
- **Google Workspace Security Checklist:** 2-Step Verification enforcement

---

### Question 2.5: MFA for Administrative Accounts 🔑 FOUNDATIONAL

**Question Text:**
Does the organization require multi-factor authentication (MFA) for all administrative and privileged accounts?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #2 for Education)

**Control Description:**

Administrative accounts require MFA:

- **Domain Administrators:** Active Directory, Azure AD Global Administrators
- **Local Administrators:** Workstation/server local admin accounts
- **Application Administrators:** Database admins, application admins, security tool admins
- **Cloud Administrators:** AWS root/admin, Azure subscription owners, Google Workspace super admins
- **Network Administrators:** Firewall, switch, router administrative access

**Privileged Account MFA Methods:**

- **Hardware Tokens:** FIDO2 keys (Yubikey) for phishing-resistant MFA
- **Authenticator Apps:** Time-based codes or push notifications
- **Certificate-Based Authentication:** Smart cards for Windows admin access
- **Biometric + PIN:** Windows Hello for Business

**Break-Glass Accounts:**

- Emergency admin accounts with MFA bypass (for MFA system outages)
- Stored in physical safe with audit logging
- Tested quarterly to verify functionality

**Service Account MFA:**

- Managed service accounts with certificate-based authentication
- No interactive logon for service accounts (reduce MFA challenges)

**Insurance Rationale (Universal):**

Privileged accounts are **prime targets** for attackers:

- Enable lateral movement across entire organization
- Can disable security tools (EDR, SIEM, backup systems)
- Deploy ransomware across all systems simultaneously
- Exfiltrate all organizational data

**42% of organizations now required to have Privileged Access Management** (PAM) for insurance coverage (Securden 2024), which includes MFA for privileged accounts.

**Threat Landscape Justification:**

- **30% of incidents involve account abuse** (IBM X-Force 2025), with privileged accounts as primary targets
- **88% of breaches involve stolen credentials** (Verizon DBIR 2024); compromised admin credentials have maximum impact
- Privileged account compromise enables **ransomware deployment** across entire network

**Sector-Specific Context:**

**Education:**

- **IT Admin Accounts:** Access to student information systems, Active Directory, Google Workspace admin console
- **Small IT Teams:** Often 1-3 IT staff with shared admin knowledge; MFA reduces insider threat risk

**Healthcare:**

- **EHR Admin Accounts:** Epic, Cerner, athenahealth administrators with access to all patient records
- **HIPAA:** Administrative access to PHI requires strong authentication and audit logging
- **Medical Device Management:** Admin access to medical device management consoles

**Religious/Nonprofit:**

- **Finance Admin Accounts:** Access to accounting software, bank accounts, payroll
- **Donor Database Admins:** Access to all donor financial information, credit cards

**Citations:**

- **The Trust (Education Insurance):** Requirement #2 - MFA for administrative accounts
- **Securden (2024):** "42% of organizations required to have PAM for cyber insurance"
- CIS Controls v8: Control 5.4 (Restrict Administrator Privileges to Dedicated Accounts)
- CIS Controls v8: Control 6.3 (Require MFA for Externally-Exposed Applications)
- NIST CSF 2.0: PR.AC-4 (Access permissions are managed)
- HIPAA Security Rule: §164.312(a)(2)(i) - Unique user identification for admin access

---

### Question 2.6: MFA for All Users 🔑 FOUNDATIONAL

**Question Text:**
Does the organization require multi-factor authentication (MFA) for all users (not just admins) accessing sensitive systems or data?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #2 for Education)

**Control Description:**

Universal MFA deployment covers:

- **All Employees:** Full-time, part-time, contractors, temporary staff
- **All Access Methods:** VPN, cloud services, email, sensitive applications
- **All Devices:** Workstations, laptops, mobile devices, tablets
- **All Locations:** Office, remote work, public Wi-Fi

**Sensitive Systems Requiring MFA:**

- Systems with PII, PHI, financial data, student education records
- Email (primary target for BEC attacks)
- Cloud productivity suites (Microsoft 365, Google Workspace)
- Line-of-business applications (EHR, SIS, donor management, accounting)
- File shares with confidential data

**MFA Enrollment Process:**

- New user onboarding includes MFA setup
- Self-service MFA enrollment portals
- Help desk support for MFA issues
- Backup MFA methods (multiple devices, backup codes)

**User Training:**

- MFA usage training during onboarding
- Phishing awareness (don't approve unexpected MFA prompts)
- MFA fatigue mitigation (conditional access reduces prompts)

**Insurance Rationale (Universal):**

**Universal MFA is the #1 insurance requirement across all carriers:**

- **82% of cyber insurance claims** involved organizations lacking MFA (Coalition 2024)
- Coalition, Chubb, Corvus **require MFA attestation** for policy issuance
- Organizations without universal MFA face:

  - Coverage denial or policy cancellation
  - Significantly higher premiums (20-30% increase)
  - Exclusions for claims involving compromised user accounts

**Threat Landscape Justification:**

- **99.9% of automated credential attacks** blocked by MFA (Microsoft research)
- **Phishing:** Even successful phishing cannot compromise MFA-protected accounts (unless user approves malicious MFA prompt)
- **Credential Stuffing:** Breached passwords from other sites useless against MFA-protected systems

**Sector-Specific Context:**

**Education:**

- **All Staff:** Teachers, administrators, custodians, bus drivers accessing any school system
- **Students:** Secondary students accessing sensitive systems (some districts MFA for students 13+)
- **Challenge:** Training non-technical staff; smartphone ownership for low-wage employees

**Healthcare:**

- **Clinical Staff:** Nurses, physicians, therapists accessing EHR systems
- **Administrative Staff:** Billing, scheduling, HR staff accessing patient data
- **HIPAA:** All workforce members accessing PHI require strong authentication

**Religious/Nonprofit:**

- **All Staff and Key Volunteers:** Anyone accessing donor data, financial systems
- **Challenge:** Older volunteers without smartphones; use hardware tokens or landline phone codes

**General:**

- **All Employees:** Universal MFA is baseline expectation in 2025-2026

**Citations:**

- **The Trust (Education Insurance):** Requirement #2 - MFA for all users
- **Coalition (2024):** "82% of claims involved orgs lacking MFA"
- **Microsoft Research:** "MFA blocks 99.9% of automated attacks"
- CIS Controls v8: Control 6.3 (Require MFA for Externally-Exposed Applications)
- NIST CSF 2.0: PR.AC-7 (Users are authenticated)
- CISA: MFA listed in "Cross-Sector Cybersecurity Performance Goals" for critical infrastructure

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

### Question 4.3: Patch Management Process 🔑 FOUNDATIONAL

**Question Text:**
Does the organization have a documented patch management process for timely installation of security updates on all systems (servers, workstations, network devices, applications)?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #3 for Education)

**Control Description:**

Patch management process includes:

**Scope:**

- **Operating Systems:** Windows, macOS, Linux servers and workstations
- **Applications:** Microsoft Office, Adobe, Java, web browsers, line-of-business applications
- **Network Devices:** Firewalls, switches, routers, wireless access points
- **Security Tools:** Antivirus, EDR, VPN clients
- **Cloud Services:** Apply vendor updates for SaaS applications (Microsoft 365, Google Workspace updates automatically)

**Patch Cycle:**

- **Critical Patches:** Deploy within 7-14 days of release (actively exploited vulnerabilities)
- **Security Patches:** Deploy within 30 days of release (monthly Patch Tuesday for Microsoft)
- **Non-Security Patches:** Deploy on quarterly schedule or as needed

**Patch Process:**

1. **Identification:** Monitor vendor security advisories (Microsoft, Apple, Adobe, etc.)
2. **Testing:** Test patches in development/test environment before production deployment
3. **Deployment:** Automated patch deployment tools (WSUS, SCCM, Intune, Jamf, third-party RMM)
4. **Verification:** Confirm patches installed successfully, systems functioning normally
5. **Documentation:** Track patch status, exemptions, failures

**Automated Patching:**

- **Windows:** WSUS (Windows Server Update Services), SCCM (System Center Configuration Manager), Intune (cloud-based)
- **macOS:** Jamf Pro, Apple Business Manager
- **Linux:** apt, yum, automated update scripts
- **Third-Party Applications:** Ninite, Chocolatey, third-party patch management tools

**Exception Management:**

- **Legacy Systems:** Document why patches cannot be applied (compatibility, vendor restrictions)
- **Compensating Controls:** Network segmentation, additional monitoring for unpatched systems
- **Medical Devices:** Vendor-controlled firmware updates (healthcare specific)

**Insurance Rationale (Universal):**

Patch management is **critical insurance requirement:**

- **50% of perimeter vulnerabilities remain unpatched** (Verizon DBIR 2024)
- Unpatched systems are #1 exploited vulnerability
- Coalition, Chubb, Corvus assess patch management maturity during underwriting

**Threat Landscape Justification:**

- **Exploited Vulnerabilities:** WannaCry (2017), NotPetya (2017), EternalBlue, Log4Shell (2021) exploited unpatched systems
- **Zero-Day Race:** Attackers exploit vulnerabilities within days/hours of disclosure
- **Verizon DBIR 2024:** Only 50% of perimeter vulnerabilities fully remediated

**Sector-Specific Context:**

**Education:**

- **Summer Patching:** Major patches deployed during summer break to minimize disruption
- **Chromebooks:** Auto-update via Chrome OS; minimal patch management burden
- **Windows Workstations:** WSUS or cloud-based patch management (Intune, third-party RMM)
- **Challenge:** Limited IT staff; automated patching essential

**Healthcare:**

- **Medical Devices:** Vendor-controlled firmware; hospitals cannot patch independently
- **EHR Systems:** Patches must be tested with EHR vendor to prevent downtime
- **24/7 Operations:** Patch deployment during maintenance windows (2-6 AM)
- **Challenge:** Balancing patient care continuity with security updates

**Religious/Nonprofit:**

- **Limited IT Resources:** Cloud-based patch management (Microsoft Intune) reduces burden
- **Donated Equipment:** May run outdated operating systems; prioritize replacement over patching
- **Challenge:** Volunteer IT may lack patch management expertise

**General:**

- **Operational Technology (OT/ICS):** Long patch cycles due to uptime requirements
- **Critical Systems:** Extensive testing before patching (financial systems, manufacturing)

**Citations:**

- **The Trust (Education Insurance):** Requirement #3 - Patch management process
- **Verizon DBIR 2024:** "Only 50% of perimeter-device vulnerabilities fully remediated"
- CIS Controls v8: Control 7.2 (Establish and Maintain a Remediation Process)
- NIST CSF 2.0: PR.IP-12 (A vulnerability management plan is developed and implemented)
- **WannaCry / NotPetya Case Studies:** Unpatched systems resulted in billions in damages

---

### Question 4.7: External Vulnerability Scanning 🔑 FOUNDATIONAL

**Question Text:**
Does the organization conduct external vulnerability scans at least quarterly to identify internet-facing vulnerabilities?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #4 for Education)

**Control Description:**

External vulnerability scanning identifies internet-facing vulnerabilities:

**Scan Scope:**

- **Public-Facing Systems:** Web servers, email servers, VPN endpoints, remote desktop gateways
- **Network Perimeter:** Firewalls, routers, external-facing network devices
- **Cloud Services:** Public cloud infrastructure (AWS, Azure, GCP), SaaS applications (if applicable)

**Scan Frequency:**

- **Quarterly (Minimum):** Required by most cyber insurance carriers and PCI DSS
- **Monthly (Preferred):** More frequent scanning reduces window of exposure
- **After Major Changes:** Scan after new system deployment, firewall rule changes
- **Continuous Scanning (Advanced):** Cloud-based continuous vulnerability management

**Vulnerability Scanning Tools:**

- **Commercial:** Tenable Nessus, Qualys, Rapid7 InsightVM, Greenbone
- **Open Source:** OpenVAS (community version of Greenbone)
- **Cloud-Native:** AWS Inspector, Azure Security Center Vulnerability Assessment
- **Managed Services:** Outsourced scanning from MSPs, CyberPools vulnerability scanning service

**Scan Process:**

1. **Discovery:** Identify all internet-facing IP addresses and domains
2. **Scanning:** Automated scan checks for known vulnerabilities (CVEs)
3. **Reporting:** Generate vulnerability report with severity ratings (Critical/High/Medium/Low)
4. **Prioritization:** Risk-rank vulnerabilities based on exploitability, asset criticality
5. **Remediation:** Patch or mitigate vulnerabilities within defined timeframes
    - **Critical:** 7-14 days
    - **High:** 30 days
    - **Medium:** 90 days
6. **Verification:** Rescan to confirm vulnerabilities remediated

**Authenticated vs. Unauthenticated Scanning:**

- **External Scans:** Unauthenticated (attacker perspective - what can be exploited from internet)
- **Internal Scans:** Authenticated (identify vulnerabilities inside network perimeter)

**Insurance Rationale (Universal):**

External vulnerability scanning is **mandatory insurance requirement:**

- **PCI DSS:** Quarterly external scans required for payment card processing (Requirement 11.3)
- **Coalition, Chubb, Corvus:** All require quarterly external vulnerability scanning
- **Scan Reports:** Provide to insurer as evidence of vulnerability management

**Threat Landscape Justification:**

- **Verizon DBIR 2024:** 50% of perimeter vulnerabilities remain unpatched
- **Internet Scanning:** Attackers constantly scan internet for vulnerable systems (Shodan, Masscan)
- **Exploit Kits:** Automated tools exploit known vulnerabilities within days of disclosure

**Sector-Specific Context:**

**Education:**

- **Internet-Facing Systems:** Student information system web portals, school websites, remote access VPNs
- **Challenge:** Budget constraints; CyberPools vulnerability scanning service provides cost-effective solution
- **FERPA:** Vulnerability scanning protects internet-facing systems with student data

**Healthcare:**

- **Internet-Facing Systems:** Patient portals, telehealth platforms, VPN for remote physicians
- **HIPAA:** Vulnerability scanning supports risk analysis requirement (§164.308(a)(1)(ii)(A))
- **Challenge:** 24/7 operations; scans scheduled during maintenance windows

**Religious/Nonprofit:**

- **Internet-Facing Systems:** Church websites, donor portals, online giving platforms
- **PCI DSS:** Quarterly scans required if processing credit card donations
- **Challenge:** Volunteer IT; outsourced scanning services provide expertise

**General:**

- **Internet-Facing Systems:** Corporate websites, customer portals, e-commerce, remote access
- **Regulatory Requirements:** PCI DSS, SOX (indirectly), state data breach laws

**Citations:**

- **The Trust (Education Insurance):** Requirement #4 - External vulnerability scanning (quarterly minimum)
- **PCI DSS Requirement 11.3.2:** Perform quarterly external vulnerability scans
- **Verizon DBIR 2024:** "Only 50% of perimeter-device vulnerabilities fully remediated"
- CIS Controls v8: Control 7.5 (Perform Automated Vulnerability Scans of External-Facing Systems)
- NIST CSF 2.0: ID.RA-1 (Asset vulnerabilities are identified and documented)
- HIPAA Security Rule: §164.308(a)(1)(ii)(A) - Risk analysis includes vulnerability assessment

---


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

### Question 5.4: Endpoint Detection and Response (EDR) 🔑 FOUNDATIONAL

**Question Text:**
Does the organization deploy Endpoint Detection and Response (EDR) or managed detection and response (MDR) solutions on all workstations, laptops, and servers?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #5 for Education)

**Control Description:**

Endpoint Detection and Response (EDR) provides advanced threat detection beyond traditional antivirus:

**EDR Capabilities:**

- **Behavioral Monitoring:** Detect suspicious behaviors (file encryption = ransomware, mass data access = exfiltration)
- **Threat Hunting:** Security analysts proactively search endpoints for threats
- **Automated Response:** Isolate infected endpoints from network, kill malicious processes
- **Forensic Investigation:** Detailed endpoint activity logs for incident investigation
- **Threat Intelligence Integration:** Compare endpoint behaviors against known attack patterns

**EDR vs. Antivirus:**

- **Antivirus:** Signature-based detection of known malware
- **EDR:** Behavior-based detection of unknown/zero-day malware, provides context and forensics

**EDR Solutions:**

- **Enterprise:** CrowdStrike Falcon, SentinelOne, Carbon Black, Microsoft Defender for Endpoint
- **SMB:** Sophos Intercept X, Bitdefender GravityZone, Malwarebytes Endpoint Protection
- **Managed Detection and Response (MDR):** Huntress, Arctic Wolf, Red Canary (EDR + 24/7 monitoring by security experts)

**Deployment:**

- **Agent-Based:** Lightweight software agent installed on all endpoints
- **Cloud-Managed:** Centralized cloud console for visibility across all endpoints
- **Automatic Updates:** EDR agents auto-update without user intervention

**Managed Detection and Response (MDR):**

- **24/7 Monitoring:** Security Operations Center (SOC) analysts monitor EDR alerts
- **Threat Response:** SOC team investigates alerts, responds to incidents
- **Practical for Small IT Teams:** Outsourced expertise for organizations without dedicated security staff

**Insurance Rationale (Universal):**

**EDR is UNIVERSAL insurance requirement across all carriers:**

- **Coalition, Chubb, Corvus:** All require EDR or equivalent endpoint protection
- **82% of claims** involved organizations lacking proper endpoint security
- **Ransomware Protection:** EDR is most effective defense against ransomware (blocks encryption behavior)

**Threat Landscape Justification:**

**Verizon DBIR 2024:**

- **75% of breaches** included ransomware (significant increase from prior year)
- EDR detects and stops ransomware during execution phase

**IBM X-Force 2025:**

- **84% increase** in phishing emails delivering infostealers
- EDR detects infostealer malware stealing credentials from browsers

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Ransomware Target:** Schools frequently targeted with ransomware
- **EDR Solutions:** Microsoft Defender for Endpoint (included with Microsoft 365 A3/A5), Sophos Intercept X (EDU pricing)
- **Managed MDR:** Huntress, Arctic Wolf (K-12 specialized offerings)
- **Chromebooks:** Minimal EDR needed (Chrome OS architecture limits malware)

**Healthcare:**

- **Ransomware Impact:** Can halt patient care, delay treatments, divert ambulances
- **EDR Solutions:** CrowdStrike, SentinelOne, Microsoft Defender for Endpoint
- **HIPAA:** EDR demonstrates technical safeguards for ePHI protection
- **Medical Devices:** Often cannot install EDR (vendor restrictions); network segmentation compensates

**Religious/Nonprofit:**

- **Ransomware Risk:** Donor databases, financial records targeted
- **EDR Solutions:** Sophos, Bitdefender (affordable for nonprofits)
- **Managed MDR:** Huntress (cost-effective for small organizations)

**General Organizations:**

- **Critical Infrastructure:** EDR required for OT/ICS endpoints
- **Financial Services:** Advanced EDR required by regulators

**Citations:**

- **The Trust (Education Insurance):** Requirement #5 - EDR/antivirus deployment
- **Coalition:** "82% of claims involved orgs lacking proper endpoint security"
- **Verizon DBIR 2024:** "75% of breaches included ransomware"
- CIS Controls v8: Control 10.7 (Use Behavior-Based Anti-Malware Software)
- NIST CSF 2.0: DE.CM-4 (Malicious code is detected)

---

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

### Question 6.3: Air-Gapped or Offline Backups 🔑 FOUNDATIONAL

**Question Text:**
Does the organization maintain air-gapped or offline backups that are isolated from the network and cannot be accessed by ransomware?

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #6 for Education)

**Control Description:**

Air-gapped or offline backups are physically or logically isolated from the network:

**Air-Gapped Backup Methods:**

- **Tape Backups:** Physically remove tapes from library, store off-site
- **Disk Rotation:** External hard drives rotated weekly, stored off-site
- **Immutable Cloud Backups:** Write-once-read-many (WORM) cloud storage that cannot be deleted or encrypted by ransomware
- **Vaulting:** Physical vault storage for backup media

**Immutable Backups (Modern Approach):**

- **AWS S3 Object Lock:** Prevents deletion/modification for specified retention period
- **Azure Immutable Blob Storage:** WORM storage for compliance
- **Backblaze B2 Object Lock:** Immutable cloud backups
- **Veeam Immutability:** Backup files cannot be deleted even with admin credentials

**Offline vs. Air-Gapped:**

- **Offline:** Backup media physically disconnected from network (tapes ejected, drives removed)
- **Air-Gapped:** Network-connected but logically isolated (immutable cloud storage)

**3-2-1 Backup Rule:**

- **3 Copies:** Production data + 2 backups
- **2 Different Media Types:** Disk + cloud or disk + tape
- **1 Off-Site:** At least one backup off-site (different physical location)

**Backup Rotation:**

- **Daily/Weekly Rotation:** Fresh backup media stored off-site weekly
- **Monthly Archives:** Long-term retention for compliance
- **Test Restorations:** Periodic testing to verify backups recoverable

**Insurance Rationale (Universal):**

**Air-gapped backups are CRITICAL insurance requirement:**

- **Coalition, Chubb, Corvus:** All require **weekly offline backups**
- **Ransomware Recovery:** Only defense against ransomware that encrypts network-accessible backups
- **Untested Backups:** 25% of untested backups fail during restoration; testing required

**Modern Ransomware Tactics:**

- Attackers delete or encrypt online backups before deploying ransomware
- Air-gapped/immutable backups cannot be reached by ransomware

**Threat Landscape Justification:**

**Verizon DBIR 2024:**

- **75% of breaches** included ransomware
- Ransomware specifically targets backup systems to force ransom payment

**Insurance Claims:**

- Organizations without air-gapped backups often must pay ransom (not covered by insurance)
- With air-gapped backups, organizations can restore without paying

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Frequent Ransomware Target:** Schools attacked due to limited cybersecurity resources
- **Air-Gapped Options:** Veeam immutable cloud backups, tape rotation, external drive rotation
- **Practical Implementation:** Cloud immutable backups (AWS S3 Object Lock) more practical than tape for smaller districts

**Healthcare:**

- **Patient Care Impact:** Ransomware can halt patient care; air-gapped backups enable rapid recovery
- **HIPAA:** Contingency planning requires testable backup/recovery procedures
- **24/7 Operations:** Backup testing during maintenance windows

**Religious/Nonprofit:**

- **Donor Database Protection:** Ransomware encrypting donor data is existential threat
- **Practical Implementation:** Cloud immutable backups (Backblaze B2 Object Lock) cost-effective

**General Organizations:**

- **Business Continuity:** Air-gapped backups enable recovery from any disaster (ransomware, fire, flood)

**Citations:**

- **The Trust (Education Insurance):** Requirement #6 - Air-gapped or offline backups (weekly minimum)
- **Coalition:** "Weekly offline backups" required for coverage
- CIS Controls v8: Control 11.3 (Protect Recovery Data)
- NIST CSF 2.0: PR.IP-4 (Backups are performed), RC.RP-1 (Recovery plan is executed)
- **Verizon DBIR 2024:** "75% of breaches included ransomware"

---

### Question 6.4: Backup Testing Frequency 🔑 FOUNDATIONAL

**Question Text:**
How frequently does the organization test backup restoration to verify that backups can be successfully recovered?

**Response Options:**

- Monthly or more frequently
- Quarterly
- Semi-annually
- Annually
- Never or rarely tested

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #6 for Education)

**Control Description:**

Regular backup testing verifies that backup procedures work correctly and data can be successfully restored during an emergency. Effective backup testing includes:

**Testing Procedures:**

- **Full Restoration Testing:** Restore entire systems to verify complete recoverability
- **Sample File Testing:** Restore sample files from backups to verify data integrity
- **Documented Procedures:** Written restore procedures tested by multiple team members
- **Restoration Metrics:** Track restoration success rate, time to restore, data loss (RPO/RTO)

**What to Test:**

- **Critical Systems:** Test restoration of critical servers, databases, applications
- **User Data:** Test file restoration from various backup generations
- **Configuration Files:** Verify system configurations can be restored
- **Disaster Recovery Site:** Test restoration to alternate location/hardware

**Recovery Objectives:**

- **Recovery Time Objective (RTO):** Maximum acceptable downtime (hours/days)
- **Recovery Point Objective (RPO):** Maximum acceptable data loss (hours of data)

**Insurance Rationale (Universal):**

**Trust Requirement #6 for Education pools:**

- Requires **quarterly backup testing** at minimum
- Untested backups are considered non-existent for insurance purposes

**Untested Backup Failures (Insurance Industry Data):**

- **25% of untested backups fail** during actual restoration attempts
- Common failures: corrupted backups, incomplete backups, incompatible restore hardware, lost encryption keys

**Insurance Claims Impact:**

- Organizations with tested backups restore operations 3-5x faster
- Untested backups often discovered as non-functional during ransomware recovery (forcing ransom payment)

**Insurers require:**

- Documented testing schedule (monthly/quarterly preferred)
- Restoration success metrics tracked over time
- Multiple staff trained on restoration procedures

**Threat Landscape Justification:**

**Ransomware Recovery Readiness:**

- **75% of breaches include ransomware** (Verizon DBIR 2024)
- Untested backups discovered as corrupt/incomplete when most needed
- Testing identifies failures before emergency

**Real-World Backup Failures:**

- **Baltimore Ransomware (2019):** Untested backups incomplete; city paid $18M in recovery costs
- **Colonial Pipeline (2021):** Backup restoration too slow; paid $4.4M ransom
- Backup testing would have identified these issues

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Limited IT Staff:** Backup testing often postponed due to daily firefighting
- **Practical Testing:** Quarterly restore of sample student data, key applications (SIS, LMS)
- **Summer Testing:** Use summer break for full disaster recovery testing
- **Documentation:** Written restoration procedures tested by substitutes/new hires

**Healthcare:**

- **Patient Care Continuity:** Backup testing critical for 24/7 operations
- **HIPAA Requirement:** Contingency plan must include "testing and revision procedures"
- **EHR Restoration:** Test EHR database restoration regularly (patient care depends on it)
- **Testing During Maintenance:** Schedule testing during planned maintenance windows

**Religious/Nonprofit:**

- **Small IT Teams:** Often lack resources for regular testing; consider managed backup services (Datto, Veeam)
- **Donor Database:** Test restoration of donor management systems at minimum
- **Financial Systems:** Test accounting/payroll restoration before year-end

**General Organizations:**

- **Business Continuity:** Backup testing validates entire DR plan
- **Compliance Audits:** Many frameworks (SOC 2, ISO 27001) require documented backup testing
- **Cloud Backup Testing:** Test restoration from cloud providers (AWS, Azure, Google Cloud)

**Citations:**

- **The Trust (Education Insurance):** Requirement #6 - Quarterly backup testing
- **Industry Standard:** 25% of untested backups fail during restoration
- CIS Controls v8: Control 11.4 (Establish and Maintain an Isolated Instance of Recovery Data)
- NIST CSF 2.0: RC.RP-1 (Recovery plan is executed during or after a cybersecurity incident)
- **Verizon DBIR 2024:** "75% of breaches included ransomware"
- **HIPAA Security Rule:** 45 CFR § 164.308(a)(7)(ii)(B) - Testing and revision procedures

---

### Question 7.2: Phishing Simulation Testing 🔑 FOUNDATIONAL

**Question Text:**
Does the organization conduct regular phishing simulation tests to measure user susceptibility to phishing attacks?

**Response Options:**

- Monthly or more frequently
- Quarterly
- Semi-annually
- Annually
- Never conducted

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #7 for Education)

**Control Description:**

Phishing simulation testing sends simulated phishing emails to users to measure their ability to recognize and report phishing attempts. Effective programs include:

**Simulation Components:**

- **Realistic Scenarios:** Simulate current phishing tactics (credential harvesting, malicious attachments, AI-generated messages)
- **Varied Difficulty:** Range from obvious phishing to sophisticated spear-phishing
- **Immediate Feedback:** Users who click receive just-in-time training explaining the red flags
- **Tracking and Reporting:** Measure click rates, reporting rates, repeat clickers over time

**Simulation Best Practices:**

- **Regular Cadence:** Monthly or quarterly testing to maintain awareness
- **Non-Punitive Approach:** Focus on education, not punishment (encourages reporting)
- **Progressive Difficulty:** Increase sophistication as users improve
- **Executive Inclusion:** Simulate executive-targeted attacks (CEO fraud, BEC)

**Popular Phishing Simulation Platforms:**

- **KnowBe4, Proofpoint, Cofense, Mimecast:** Automated platforms with template libraries, reporting dashboards
- **Integration with Training:** Link simulation failures to targeted micro-training

**Insurance Rationale (Universal):**

**Trust Requirement #7 for Education pools:**

- Requires **quarterly phishing simulation testing** at minimum
- Testing demonstrates proactive risk reduction to insurers

**Insurance Industry Requirement:**

- **Coalition, Chubb, Corvus** increasingly require phishing simulation testing for coverage
- Organizations with >10% phishing click rates may face higher premiums or coverage restrictions
- Demonstrable improvement over time (declining click rates) valued by underwriters

**Risk Reduction Evidence:**

- Organizations conducting monthly simulations reduce click rates from 30%+ to <5% within 12 months (KnowBe4)
- Simulation testing + just-in-time training most effective combination

**Threat Landscape Justification:**

**Phishing Dominance:**

- **Phishing is initial access vector in 36% of breaches** (Verizon DBIR 2024)
- **67.4% of phishing now uses AI** (Zscaler 2024), making attacks more convincing
- Simulation testing prepares users for real-world AI-generated phishing

**Credential Theft:**

- Phishing primary method for stealing credentials (88% of breaches involve credentials - Verizon)
- Simulation teaches users to recognize credential harvesting pages

**Business Email Compromise (BEC):**

- Average BEC loss: $125,000 per incident
- Executive-targeted phishing simulations reduce BEC risk

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Target Audience:** All staff with email accounts (teachers, administrators, support staff)
- **Education-Specific Scenarios:** Fake IT help desk requests, fake professional development links, fake student/parent emails
- **Practical Implementation:** Use platforms like KnowBe4 Education (K-12 pricing), CyberPools phishing testing service
- **Results Tracking:** Track by department; provide targeted training to high-click departments
- **Student Simulation:** Some districts simulate phishing for older students (high school) as part of digital citizenship

**Healthcare:**

- **Target Audience:** All staff with email (clinical, administrative, physicians)
- **Healthcare-Specific Scenarios:** Fake patient records requests, fake insurance verification emails, fake medical supplier invoices
- **High-Risk Impact:** Phishing can lead to HIPAA breaches, ransomware affecting patient care
- **Compliance:** HIPAA does not explicitly require simulation, but demonstrates security awareness effectiveness

**Religious/Nonprofit:**

- **Target Audience:** Staff, volunteers with email access, board members
- **Nonprofit-Specific Scenarios:** Fake donation receipts, fake vendor invoices, CEO fraud targeting finance staff
- **Practical Implementation:** Monthly simulations for staff; quarterly for volunteers/board
- **BEC Focus:** Nonprofits increasingly targeted by BEC scams (fake wire transfer requests from "CEO" or "pastor")

**General Organizations:**

- **Target Audience:** All employees, contractors with email access
- **Industry-Specific Scenarios:** Tailor simulations to industry (fake customer inquiries for retail, fake vendor invoices for finance)
- **Executive Phishing:** Simulate targeted attacks on executives, finance staff (BEC scenarios)
- **Compliance:** PCI DSS requires security awareness testing; simulation satisfies requirement

**Citations:**

- **The Trust (Education Insurance):** Requirement #7 - Quarterly phishing simulation testing
- CIS Controls v8: Control 14.2 (Train Workforce Members to Recognize Social Engineering Attacks)
- NIST CSF 2.0: PR.AT-2 (Individuals in specialized roles are trained)
- **Verizon DBIR 2024:** "36% of breaches involved phishing"
- **KnowBe4 Phishing Report 2024:** Organizations reduce click rates from 30% to <5% with monthly simulations
- **Zscaler 2024:** 67.4% of phishing uses generative AI
- **Coalition, Chubb, Corvus:** Increasingly require phishing simulation testing for coverage

---

### Question 7.3: Security Awareness Training Frequency 🔑 FOUNDATIONAL

**Question Text:**
How frequently does the organization provide security awareness training to all users?

**Response Options:**

- Quarterly or more frequently
- Semi-annually
- Annually
- Every 2+ years
- No regular training

**Impact Rating:** High (5)

**Foundational:** 🔑 YES - Insurance Critical (Trust Requirement #7 for Education)

**Control Description:**

Regular security awareness training ensures all users receive ongoing education about current threats, security policies, and their responsibilities. Effective training programs include:

**Training Delivery:**

- **Annual Comprehensive Training:** Full security awareness curriculum (45-60 minutes) covering all major topics
- **Ongoing Reinforcement:** Monthly micro-training (5-10 minutes) on current threats (new phishing tactics, ransomware trends)
- **Just-in-Time Training:** Immediate training when user fails phishing simulation
- **New Hire Training:** Security awareness during onboarding (before granting system access)

**Training Topics:**

- **Core Security Awareness:** Password security, phishing recognition, physical security, data protection
- **Current Threats:** Ransomware, AI-powered phishing, deepfakes, social engineering
- **Policy Training:** Acceptable use policy, data classification, incident reporting procedures
- **Role-Specific Training:** Specialized training for administrators, finance, HR, developers

**Training Management:**

- **Completion Tracking:** Training management system (KnowBe4, Mimecast, custom LMS) tracks completion
- **Compliance Reporting:** Generate completion reports for audits, insurance applications
- **Remedial Training:** Require additional training for repeat phishing simulation failures

**Insurance Rationale (Universal):**

**Trust Requirement #7 for Education pools:**

- Requires **annual security awareness training** for all users (minimum)
- Training completion records may be requested during insurance application/renewal

**Universal Insurance Requirement:**

- **100% of cyber insurers require annual training** (Coalition, Chubb, Corvus, all carriers)
- Organizations without annual training may be denied coverage
- Training completion rates (target: >90%) factor into premium calculations

**Compliance Alignment:**

- **HIPAA:** Annual training required
- **PCI DSS:** Annual training required
- **State Privacy Laws:** Many require annual training (CCPA, NYDFS Cybersecurity Regulation)
- Security frameworks (SOC 2, ISO 27001) require ongoing training

**Threat Landscape Justification:**

**Human Element in Breaches:**

- **68% of breaches involve human element** (Verizon DBIR 2024)
- **Training Effectiveness:** Organizations with annual+ training experience 70% fewer successful phishing attacks (KnowBe4 2024)
- Regular training reinforces secure behaviors, builds security culture

**Evolving Threat Landscape:**

- **AI-Powered Threats:** Generative AI creates more convincing phishing (67.4% of phishing now uses AI)
- **Deepfakes:** Voice and video deepfakes used for social engineering; training must address emerging threats
- **Annual training insufficient** for rapidly evolving threats; quarterly or monthly updates recommended

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Training Schedule:** Annual comprehensive training at start of school year; monthly micro-training during school year
- **Target Audience:** All staff (teachers, administrators, IT, support staff, substitutes); age-appropriate training for students
- **Practical Implementation:** Back-to-school security training session (in-person or online); monthly security tips via email/newsletter
- **Compliance:** FERPA does not require training, but demonstrates compliance with data protection obligations
- **Turnover Challenge:** High substitute/part-time staff turnover requires ongoing onboarding training

**Healthcare:**

- **Training Schedule:** Annual comprehensive HIPAA training (compliance requirement); quarterly security updates
- **Target Audience:** All workforce members with access to PHI (Protected Health Information)
- **Practical Implementation:** Online HIPAA training modules (HealthStream, Relias); in-person training for high-risk roles
- **HIPAA Requirement:** 45 CFR § 164.308(a)(5) - Annual security awareness training mandatory
- **High-Risk Focus:** Additional training for EHR users, physicians, finance (targeted by phishing)

**Religious/Nonprofit:**

- **Training Schedule:** Annual comprehensive training for staff; semi-annual for volunteers/board
- **Target Audience:** Staff, volunteers with data access, board members, finance committee
- **Practical Implementation:** Online training modules (KnowBe4, free resources from NIST/CISA); in-person workshops for staff
- **Donor Data Focus:** Emphasize donor privacy, financial controls, email compromise targeting nonprofits
- **Budget-Conscious:** Free resources available (CISA training modules, SANS Security Awareness)

**General Organizations:**

- **Training Schedule:** Annual comprehensive training; quarterly updates on current threats
- **Compliance Drivers:** PCI DSS (annual), SOC 2 (ongoing), ISO 27001 (ongoing), industry regulations
- **Role-Based Training:** Specialized training for developers (secure coding), finance (BEC), executives (targeted attacks)
- **Remote Workforce:** Virtual training platforms essential for distributed teams

**Citations:**

- **The Trust (Education Insurance):** Requirement #7 - Annual security awareness training for all users
- CIS Controls v8: Control 14.1 (Establish and Maintain a Security Awareness Program)
- NIST CSF 2.0: PR.AT-1 (Users are informed and trained)
- **Verizon DBIR 2024:** "68% of breaches involve human element"
- **KnowBe4 2024:** Organizations with annual+ training experience 70% fewer phishing attacks
- **HIPAA Security Rule:** 45 CFR § 164.308(a)(5) - Annual training required
- **PCI DSS 4.0:** Requirement 12.6 - Annual security awareness training required
- **Coalition, Chubb, Corvus:** All require annual training for coverage

---

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


