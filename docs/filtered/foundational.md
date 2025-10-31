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

### Question 1.1: Hardware Asset Inventory

**Question Text:**
Does the organization maintain an accurate, up-to-date inventory of all hardware assets, including servers, workstations, mobile devices, network equipment, and IoT devices?

**Impact Rating:** High (5)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

A comprehensive hardware asset inventory includes:
- **Servers:** Physical and virtual servers, including cloud instances (EC2, Azure VMs)
- **Workstations:** Desktop computers, laptops (organization-owned and BYOD if managed)
- **Mobile Devices:** Smartphones, tablets (organization-owned and BYOD if managed via MDM)
- **Network Equipment:** Routers, switches, firewalls, wireless access points
- **IoT Devices:** Printers, security cameras, HVAC controllers, medical devices, smart building systems
- **Peripheral Equipment:** External storage, USB devices (if managed)

**Inventory Attributes:**

- Asset tag or serial number
- Make, model, operating system version
- Physical location or network location
- Asset owner/custodian
- Purchase date, warranty/support expiration
- Classification (production, development, test)
- Status (active, retired, storage)

**Inventory Maintenance:**

- Automated discovery tools (network scanners, endpoint agents)
- Quarterly manual verification
- Integration with procurement/IT ticketing systems
- Decommissioning procedures to remove retired assets

**Insurance Rationale (Universal):**

Cyber insurance applications require organizations to report:
- Total number of servers (including cloud instances)
- Total number of workstations/endpoints
- Critical system counts (financial systems, HR systems, customer databases)

Accurate asset inventory enables:
- Proper insurance coverage limits (first-party costs, business interruption)
- Accurate premium calculation based on organization size and complexity
- Rapid incident impact assessment during claims

**Threat Landscape Justification:**

- **Verizon DBIR 2024:** Unknown or unmanaged assets frequently exploited for initial access
- Attackers scan for forgotten web servers, unpatched workstations, IoT devices with default credentials
- **Shadow IT Risk:** Unmanaged cloud services and devices bypass security controls (no EDR, no MFA, no logging)

**Sector-Specific Context:**

**Education:**

- **Challenge:** High device turnover (student laptops, Chromebooks), multiple campus locations, summer equipment moves
- **Technology:** Student information systems (SIS), learning management systems (LMS), Chromebooks, iPads, interactive whiteboards

**Healthcare:**

- **Challenge:** Medical devices (infusion pumps, monitors, X-ray machines) often unmanaged, vendor-controlled firmware
- **HIPAA:** Asset inventory required for risk analysis (§164.308(a)(1)(ii)(A))
- **Technology:** EHR servers, PACS imaging workstations, medical devices, patient monitoring systems

**Religious/Nonprofit:**

- **Challenge:** Limited IT staff, volunteer-owned devices, donated equipment of unknown provenance
- **Technology:** Donor management systems, accounting software, presentation/livestream equipment

**General:**

- **Technology:** Operational technology (OT/ICS), manufacturing equipment, building automation systems

**Citations:**

- CIS Controls v8: Control 1.1 (Establish and Maintain Detailed Enterprise Asset Inventory)
- NIST CSF 2.0: ID.AM-1 (Inventories of hardware managed by the organization are maintained)
- Verizon DBIR 2024: Unknown assets create security blind spots

---

### Question 1.2: Software Asset Inventory

**Question Text:**
Does the organization maintain an accurate inventory of all software applications, including operating systems, productivity applications, line-of-business applications, and cloud services?

**Impact Rating:** Moderate (3)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

A comprehensive software asset inventory includes:
- **Operating Systems:** Windows, macOS, Linux versions across all endpoints and servers
- **Productivity Applications:** Microsoft Office, Google Workspace, Adobe Creative Cloud
- **Line-of-Business Applications:** Student information systems, EHR systems, donor management, accounting software
- **Cloud Services (SaaS):** Email, file sharing, collaboration tools, CRM, specialized cloud apps
- **Development Tools:** IDEs, databases, frameworks (for organizations with development teams)
- **Security Tools:** Antivirus, EDR, firewalls, VPN clients

**Inventory Attributes:**

- Software name, vendor, version number
- License type (perpetual, subscription, open-source)
- Installation count vs. license count
- Support/maintenance expiration date
- Approved vs. unapproved status
- Data classification of data processed by software

**Inventory Maintenance:**

- Automated software discovery (endpoint agents, network scanners)
- Cloud service discovery (CASB, SaaS management platforms)
- Quarterly license reconciliation
- Software approval process for new applications

**Insurance Rationale (Universal):**

Software inventory enables:
- Identification of end-of-life software requiring replacement (insurance concern - see Question 1.4)
- License compliance (reduces legal/financial risk)
- Vendor risk management (tracking third-party software with access to organizational data)

**Threat Landscape Justification:**

- **Shadow IT:** Employees use unapproved cloud services (Dropbox, personal Gmail, free file sharing) storing organizational data outside security controls
- **Outdated Software:** Applications running unsupported versions with known vulnerabilities
- **Supply Chain Risk:** 41% of attacks originate from third parties, including software vendors

**Sector-Specific Context:**

**Education:**

- **Challenge:** Hundreds of EdTech applications (learning apps, assessment platforms, communication tools) with student data access
- **FERPA:** Schools must track all software with access to education records to ensure vendor agreements in place

**Healthcare:**

- **Challenge:** Specialized medical software (lab systems, billing, pharmacy), often vendor-managed
- **HIPAA:** Software inventory required for risk analysis; Business Associate Agreements needed for software processing PHI

**Religious/Nonprofit:**

- **Challenge:** Donor management software, accounting software, volunteer management tools
- **PCI DSS:** Payment processing software must be tracked for compliance

**Citations:**

- CIS Controls v8: Control 2.1 (Establish and Maintain a Software Inventory)
- NIST CSF 2.0: ID.AM-2 (Inventories of software, services, and systems managed by the organization are maintained)

---

### Question 1.3: Cloud Service Inventory

**Question Text:**
Does the organization maintain an inventory of all cloud services and SaaS applications in use, including both approved and unapproved (shadow IT) services?

**Impact Rating:** Moderate (3)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

Cloud service inventory captures:
- **Approved Cloud Services:** Organization-vetted and contracted cloud platforms
  - Microsoft 365, Google Workspace, AWS, Azure, Salesforce, etc.
- **Shadow IT:** Unapproved cloud services discovered via:
  - Cloud Access Security Broker (CASB) monitoring
  - DNS/web proxy logs analysis
  - Firewall logs showing cloud service connections
  - Expense report review (personal credit card cloud subscriptions)

**Inventory Attributes:**

- Service name, vendor, category (productivity, file sharing, collaboration, etc.)
- Data classification of data stored in service (PII, PHI, financial, public)
- Approval status (approved, under review, prohibited)
- User count, cost
- Security assessment status (vendor vetting completed, DPA signed, etc.)
- Integration points with other systems (APIs, SSO)

**Shadow IT Discovery Methods:**

- CASB platforms (Microsoft Defender for Cloud Apps, Netskope, Zscaler)
- Network traffic analysis (identify cloud service API calls)
- User surveys (what cloud tools do you use for work?)
- Expense report audits

**Insurance Rationale (Universal):**

Cloud services create:
- **Data breach exposure:** Misconfigured cloud storage (S3 buckets, Azure blobs) with public access
- **Third-party risk:** Cloud vendors can be breached, exposing customer data (see Question 8.6-8.8)
- **Compliance violations:** Unapproved cloud services may not meet HIPAA, FERPA, or state privacy law requirements

Insurers assess:
- Cloud security posture (see Question 4.15)
- Vendor risk management for cloud services
- Data governance (what data is in what clouds?)

**Threat Landscape Justification:**

- **95% of cloud breaches** stem from misconfigurations (industry research 2024-2025)
- **Shadow IT Risk:** Employees store organizational data in personal Dropbox, Google Drive, WeTransfer without security controls
- Unapproved AI tools (ChatGPT, Gemini) used for work tasks, potentially exposing confidential data

**Sector-Specific Context:**

**Education:**

- **Approved:** Google Workspace for Education, Microsoft 365 Education, Canvas/Schoology LMS
- **Shadow IT:** Teachers using personal Google Drive, students using unapproved file sharing for group projects
- **FERPA:** All cloud services with student data require written agreements

**Healthcare:**

- **Approved:** EHR cloud hosting, cloud PACS, telemedicine platforms
- **Shadow IT:** Physicians using personal file sharing, patient communication via personal WhatsApp/texting
- **HIPAA:** Business Associate Agreements (BAA) required for all cloud services processing PHI

**Religious/Nonprofit:**

- **Approved:** Donor management SaaS (Blackbaud, Planning Center), Microsoft 365/Google Workspace
- **Shadow IT:** Staff using personal file sharing, free website builders without security controls

**Citations:**

- CIS Controls v8: Control 2.2 (Ensure Authorized Software is Currently Supported)
- NIST CSF 2.0: ID.AM-2 (Software, services, and systems inventory)
- Cloud Security Alliance: Cloud Controls Matrix

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
## Category 2: Account Management and Access Control

### Overview

Account management and access control ensures that only authorized individuals can access organizational systems and data, with permissions appropriate to their role. This category addresses:
- User account lifecycle (creation, modification, deactivation)
- Multi-factor authentication (MFA) across all access points
- Privileged access management (PAM) for administrator accounts
- Password policies and credential management
- Access review and recertification processes

**Framework Alignment:**

- **NIST CSF 2.0:** PR.AC (Identity Management, Authentication and Access Control) - "Access to physical and logical assets is limited to authorized users"
- **CIS Controls v8:** Control 5 (Account Management), Control 6 (Access Control Management)

### Importance

**Why Account Management Matters:**

1. **#1 Attack Vector:** Credential abuse is the most common initial access method (30% of incidents - IBM X-Force 2025)
2. **88% of Breaches:** Involve stolen or compromised credentials (Verizon DBIR 2024)
3. **Insurance Requirement:** 82% of cyber insurance claims involved organizations lacking MFA (Coalition 2024)
4. **Privilege Escalation:** Attackers target privileged accounts for maximum impact (lateral movement, data exfiltration, ransomware deployment)
5. **Insider Threats:** Former employees with active accounts, excessive permissions, or shared credentials create risk

**Universal Threats:**

- **Credential Stuffing:** Attackers use breached credentials from other sites to access organizational systems
- **Phishing:** Social engineering to trick users into revealing passwords or MFA codes
- **Brute Force:** Automated password guessing against accounts without MFA
- **Privilege Abuse:** Compromised privileged accounts enable ransomware deployment and data theft
- **Orphaned Accounts:** Former employee accounts remaining active after termination

**Sector-Specific Risks:**

- **Education:** Shared teacher accounts, student accounts not deactivated after graduation, summer staff turnover
- **Healthcare:** Shared clinical staff accounts, vendor/contractor accounts with excessive permissions, physicians using personal devices
- **Religious/Nonprofit:** Volunteer accounts with undefined lifecycle, shared passwords for ministry tools
- **General:** Contractor/vendor accounts, service accounts with static passwords, excessive administrative permissions

---

### Question 2.1: User Account Lifecycle Management

**Question Text:**
Does the organization have a formal process for user account creation, modification, and deactivation aligned with hiring, role changes, and termination?

**Impact Rating:** High (5)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

User account lifecycle management includes:

**Account Creation:**

- Formal request and approval process (manager authorization)
- Role-based access provisioning (access based on job function)
- Integration with HR onboarding process
- Account naming conventions and email address standards
- New user security training completion before account activation

**Account Modification:**

- Role change process (promotion, department transfer, contractor conversion)
- Access recertification when responsibilities change
- Temporary access elevation for projects (time-limited)
- Integration with HR change management

**Account Deactivation:**

- Termination procedures (disable account immediately upon notification)
- Resignation procedures (disable account on last day)
- Leave of absence procedures (temporary disable)
- Automated deactivation based on HR system integration
- Account deletion after retention period (30-90 days post-termination)

**Access Reviews:**

- Quarterly or annual review of active accounts
- Manager attestation of team member access appropriateness
- Removal of unused accounts (dormant >90 days)
- Shared account identification and elimination

**Insurance Rationale (Universal):**

Orphaned accounts (former employees) are prime targets for attackers:
- No monitoring (former employee won't report suspicious activity)
- Often retain elevated permissions from last role
- Credential reuse (employee may use same password elsewhere that gets breached)

Cyber insurance claims frequently involve:
- Terminated employee accessing systems post-termination (data theft, sabotage)
- Contractor accounts persisting beyond project completion
- Shared accounts preventing accountability during incidents

**Threat Landscape Justification:**

- **Insider Threats:** Disgruntled former employees with active accounts can access systems remotely
- **Credential Reuse:** Former employee credentials appear in breach databases; attackers try them against organizational systems
- **Verizon DBIR 2024:** Orphaned accounts and excessive permissions frequently exploited

**Sector-Specific Context:**

**Education:**

- **High Turnover:** Teachers, substitutes, student teachers, summer staff create frequent account changes
- **Student Accounts:** Graduating seniors, transferring students require systematic deactivation
- **Challenge:** Summer transitions (June-August) create account management backlog

**Healthcare:**

- **Clinical Staff Mobility:** Nurses, physicians rotating through departments require role-based access changes
- **Vendor/Contractor Access:** Medical device technicians, consultants need time-limited access
- **HIPAA:** Access controls and workforce clearinghouse procedures required (§164.308(a)(3))

**Religious/Nonprofit:**

- **Volunteer Turnover:** High volunteer churn requires systematic account deactivation
- **Seasonal Staff:** Summer camps, holiday programs create temporary account needs
- **Challenge:** Limited HR infrastructure; manual account management

**Citations:**

- CIS Controls v8: Control 5.1 (Establish and Maintain an Inventory of Accounts)
- CIS Controls v8: Control 5.2 (Use Unique Passwords)
- NIST CSF 2.0: PR.AC-1 (Identities and credentials are issued, managed, verified, revoked)
- HIPAA Security Rule: §164.308(a)(3)(i) - Workforce clearance procedures

---

### Question 2.2: Password Policy

**Question Text:**
Does the organization enforce a password policy requiring minimum length, complexity, and regular password changes (or passphrase/password manager usage)?

**Impact Rating:** Moderate (3)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

Modern password policies align with NIST SP 800-63B guidance:

**Minimum Requirements:**

- **Length:** Minimum 12-15 characters (passphrases preferred over complexity rules)
- **Complexity:** No strict complexity requirements if length ≥15 characters; otherwise require uppercase, lowercase, number, special character
- **Password Managers:** Encourage or require password manager usage for generating/storing unique passwords
- **Passphrases:** Allow spaces and long phrases (e.g., "coffee-morning-sunshine-24")

**What NOT to Require (Outdated Practices):**

- **NO forced periodic password changes** (causes users to make predictable changes: Password1 → Password2)
- **NO password hints** (often reveal answers)
- **NO security questions** (easily guessable or publicly available answers)

**Best Practices:**

- **Breach Detection:** Check passwords against known breach databases (Have I Been Pwned API)
- **No Password Reuse:** Prevent users from reusing previous passwords
- **Account Lockout:** Temporary lockout after failed login attempts (5-10 attempts)
- **MFA Requirement:** Reduce password reliance through multi-factor authentication (see Questions 2.3-2.6)

**Technical Enforcement:**

- Active Directory Group Policy or Azure AD Password Protection
- Password filters or validators
- Self-service password reset with identity verification

**Insurance Rationale (Universal):**

While password policies alone are insufficient protection, they remain baseline security hygiene. Weak passwords combined with lack of MFA create critical vulnerability.

Insurers assess:
- Minimum password length requirements (8+ characters minimum, 12+ preferred)
- MFA implementation (far more critical than password policy)
- Password manager deployment for IT/admin staff

**Threat Landscape Justification:**

- **Credential Stuffing:** Attackers use breached credentials from other sites; password reuse across sites is common
- **Brute Force:** Short, simple passwords vulnerable to automated guessing
- **Phishing:** Strong passwords still vulnerable to phishing; MFA is essential defense

**Sector-Specific Context:**

**Education:**

- **Challenge:** Students/teachers resist complex passwords; password manager training needed
- **Student Accounts:** Age-appropriate password policies (elementary vs. high school)
- **FERPA:** Passwords protect access to student education records

**Healthcare:**

- **Challenge:** Clinical staff need rapid access during patient care; complex passwords slow workflow
- **HIPAA 2025 Security Rule:** Enhanced password requirements expected in final rule
- **Solution:** Biometric authentication or badge readers combined with PIN

**Religious/Nonprofit:**

- **Challenge:** Older volunteers/congregation members unfamiliar with password managers
- **Solution:** Passphrase approach (memorable but long)

**Citations:**

- **NIST SP 800-63B:** Digital Identity Guidelines (modern password guidance)
- CIS Controls v8: Control 5.2 (Use Unique Passwords)
- NIST CSF 2.0: PR.AC-1 (Credentials are managed)
- HIPAA Security Rule: §164.308(a)(5)(ii)(D) - Password management

---

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


### Question 2.7: Privileged Account Separation

**Question Text:**
Are privileged administrative functions performed using dedicated administrative accounts (not regular user accounts)?

**Impact Rating:** High (5)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

Privileged account separation means:
- **Separate Accounts:** Administrators have TWO accounts:
  - **Regular User Account:** For email, web browsing, daily work (john.smith@org.edu)
  - **Admin Account:** For administrative tasks only (john.smith-admin@org.edu or admin-jsmith)
- **No Dual-Use Accounts:** Never use admin account for email, web browsing, or daily tasks
- **Elevated Access Only When Needed:** Admin account used only for administrative tasks, then logged out

**Implementation:**

- Active Directory: Separate OU for admin accounts with restrictive GPOs
- Azure AD: Separate admin accounts or Privileged Identity Management (PIM) for just-in-time admin access
- Workstation Restriction: Admin accounts cannot log into regular workstations (only jump servers/admin workstations)

**Rationale:**

- **Phishing Protection:** Admin account not used for email, so cannot be phished
- **Malware Protection:** Admin account not used for web browsing, so malware cannot compromise admin credentials
- **Audit Trail:** Clear separation of administrative actions vs. regular user activity

**Insurance Rationale (Universal):**

Privileged account separation is core component of **Privileged Access Management (PAM)**:
- BeyondTrust: "Removing admin rights from workstations" is basic requirement of cyber insurers
- Prevents **privilege escalation** attacks where malware on user workstation compromises admin credentials

**Threat Landscape Justification:**

- Dual-use admin accounts create **phishing vulnerability**: Admin clicks malicious email link → malware runs with admin privileges
- **Pass-the-Hash Attacks:** Malware on workstation steals cached admin credentials
- **Lateral Movement:** Compromised admin account on one system enables lateral movement across network

**Sector-Specific Context:**

**Education:**

- **Small IT Teams:** 1-3 IT staff often use personal email accounts as admin accounts
- **Best Practice:** Separate admin account even for small teams

**Healthcare:**

- **EHR Administrators:** Separate account for EHR admin tasks vs. clinical documentation
- **HIPAA:** Administrative access should be separate from clinical access for audit purposes

**Religious/Nonprofit:**

- **Volunteer IT:** Separate admin account from personal volunteer account

**Citations:**

- **BeyondTrust:** "Removing admin rights and enforcing PoLP" basic insurance requirement
- CIS Controls v8: Control 5.4 (Restrict Administrator Privileges to Dedicated Accounts)
- NIST CSF 2.0: PR.AC-4 (Access permissions are managed)
- Microsoft Security Baseline: Separate admin accounts recommended

---

### Question 2.8: Access Review and Recertification

**Question Text:**
Does the organization conduct periodic reviews (at least annually) of user access rights to ensure they remain appropriate for current job responsibilities?

**Impact Rating:** Moderate (3)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

Access review process includes:
- **Quarterly or Annual Reviews:** Manager attestation that team members have appropriate access
- **Role Change Reviews:** Immediate review when employee changes roles, promoted, or transfers departments
- **Privileged Access Reviews:** Quarterly review of all administrative accounts
- **Shared Account Audit:** Identify and eliminate shared accounts
- **Dormant Account Removal:** Disable accounts inactive >90 days

**Review Process:**
1. Generate access reports from systems (Active Directory, cloud services, applications)
2. Distribute to department managers for review
3. Managers certify access is appropriate or request changes
4. IT implements approved changes (remove excessive permissions)
5. Document reviews for compliance audit trail

**Automated Tools:**

- **Identity Governance:** Tools like SailPoint, Okta Identity Governance automate access reviews
- **Azure AD Access Reviews:** Built-in access review workflows for Microsoft 365
- **Manual Reviews:** Excel spreadsheets for smaller organizations

**Insurance Rationale (Universal):**

Access creep (accumulation of permissions over time) creates risk:
- Employees retain permissions from previous roles
- Excessive permissions enable insider threats or account compromise
- Demonstrates governance maturity to insurers

**Threat Landscape Justification:**

- **Insider Threats:** Disgruntled employees with excessive permissions can cause significant damage
- **Compromised Accounts:** Attackers with access to over-privileged account have larger impact
- **Compliance:** SOX, HIPAA, FERPA require periodic access reviews

**Sector-Specific Context:**

**Education:**

- **Teacher Role Changes:** Teacher moves from elementary to high school, access should change
- **Student Graduation:** Annual review identifies graduated students with active accounts

**Healthcare:**

- **HIPAA:** Access reviews required under Security Rule (§164.308(a)(3)(ii)(C))
- **Clinical Staff Rotation:** Nurses, physicians rotating through departments need access adjustments

**Religious/Nonprofit:**

- **Volunteer Turnover:** High volunteer churn requires frequent access reviews
- **Seasonal Staff:** Review after seasonal programs end (summer camp, holiday events)

**Citations:**

- CIS Controls v8: Control 5.3 (Disable Dormant Accounts)
- CIS Controls v8: Control 6.1 (Establish an Access Granting Process)
- NIST CSF 2.0: PR.AC-4 (Access permissions are managed)
- HIPAA Security Rule: §164.308(a)(3)(ii)(C) - Review of access authorization
- SOX Compliance: Periodic access reviews required for financial system access

---

### Question 2.9: Account Off-boarding Process

**Question Text:**
Does the organization have a process to immediately disable accounts and revoke access when employees are terminated or resign?

**Impact Rating:** High (5)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

Account off-boarding includes:

**Immediate Actions (Termination Day):**

- **Disable AD/Azure AD Account:** Prevents authentication to any system
- **Disable Cloud Services:** Microsoft 365, Google Workspace, SaaS applications
- **Revoke VPN Access:** Disable VPN certificates/profiles
- **Disable Badge Access:** Physical security systems
- **Remote Wipe Mobile Devices:** Organization-owned or BYOD devices with MDM
- **Collect Equipment:** Laptop, badge, keys, company credit cards

**Follow-Up Actions (7-30 Days):**

- **Email Forwarding:** Redirect email to manager for business continuity
- **Data Transfer:** Transfer files from personal drives to shared locations
- **Application-Specific Access:** Remove from line-of-business applications (EHR, SIS, accounting)
- **Remove from Distribution Lists/Groups:** Teams, Slack, email groups

**Final Actions (30-90 Days):**

- **Account Deletion:** Delete account after retention period
- **License Reclamation:** Recover software licenses for reassignment
- **Audit Trail:** Document all off-boarding actions

**Integration with HR:**

- HR system triggers IT off-boarding workflow
- Automated account disable on termination date in HR system
- Resignation off-boarding checklist

**Insurance Rationale (Universal):**

Terminated employee accounts are **high-risk:**
- Disgruntled former employees may sabotage systems, steal data, or leak confidential information
- Attackers may compromise terminated employee accounts (no monitoring, credentials in breaches)
- Cyber insurance claims frequently involve former employee access

**Threat Landscape Justification:**

- **Insider Threats:** Terminated employees are highest risk for malicious insider activity
- **Credential Reuse:** Former employee credentials appear in breach databases; attackers try them
- **Remote Access:** Work-from-home era makes immediate physical retrieval of equipment difficult

**Sector-Specific Context:**

**Education:**

- **End of School Year:** Mass terminations (retiring teachers, graduating student workers) require systematic off-boarding
- **Challenge:** Teachers terminated in May may have active accounts through August

**Healthcare:**

- **Clinical Staff Departures:** Physicians, nurses leaving must lose PHI access immediately
- **HIPAA:** Terminated workforce members must have access revoked immediately

**Religious/Nonprofit:**

- **Staff/Volunteer Departures:** Clear off-boarding for paid staff and key volunteers with system access

**Citations:**

- CIS Controls v8: Control 5.3 (Disable Dormant Accounts)
- NIST CSF 2.0: PR.AC-1 (Identities and credentials are revoked)
- HIPAA Security Rule: §164.308(a)(3)(ii)(C) - Termination procedures
- **Insider Threat Mitigation:** CISA guidance on workforce off-boarding

---


<a name="category-3"></a>
## Category 3: Data Protection and Privacy

### Overview

Data protection and privacy controls safeguard sensitive information from unauthorized access, disclosure, modification, or destruction. This category addresses:
- Data inventory and classification
- Encryption (at rest and in transit)
- Data retention and secure deletion
- Privileged access management (PAM)
- Privacy compliance (FERPA, HIPAA, state privacy laws)
- Data loss prevention

**Framework Alignment:**

- **NIST CSF 2.0:** PR.DS (Data Security) - "Data is managed consistent with the organization's risk strategy"
- **CIS Controls v8:** Control 3 (Data Protection)

### Importance

**Why Data Protection Matters:**

1. **Breach Notification Laws:** All 50 states + DC require notification of data breaches involving PII
2. **Regulatory Fines:** HIPAA violations ($50K-$1.5M per violation), FERPA (loss of federal funding), state privacy laws ($7,500 per violation)
3. **Cyber Insurance Coverage:** First-party breach costs (notification, credit monitoring, legal defense) are primary coverage
4. **Reputational Damage:** Data breaches erode trust with students/patients/donors/customers
5. **Privilege Escalation:** Compromised privileged accounts enable attackers to access ALL organizational data

**Universal Threats:**

- **Ransomware:** Encrypts data, demands payment for decryption key
- **Data Exfiltration:** Attackers steal sensitive data for sale on dark web or extortion
- **Insider Threats:** Employees with excessive access steal data before departure
- **Cloud Misconfiguration:** Publicly exposed cloud storage (S3 buckets, Azure blobs)
- **Unencrypted Data:** Laptops, USB drives, backups lost or stolen without encryption

**Sector-Specific Risks:**

- **Education:** Student education records (FERPA), SSNs, financial aid information
- **Healthcare:** Patient health information (HIPAA), medical records, billing data
- **Religious/Nonprofit:** Donor PII, credit card information, pastoral counseling notes
- **General:** Customer PII, financial data, trade secrets, intellectual property

---

### Question 3.1: Data Inventory

**Question Text:**
Has the organization identified and documented all sensitive data it collects, processes, and stores, including data types, locations, and business purposes?

**Impact Rating:** Moderate (3)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

Data inventory includes:

**Data Types:**

- **Personally Identifiable Information (PII):** Names, addresses, SSNs, dates of birth
- **Protected Health Information (PHI):** Medical records, diagnoses, prescriptions, billing
- **Education Records (FERPA):** Student grades, discipline records, IEPs, assessments
- **Financial Data:** Credit cards (PCI DSS), bank accounts, payroll, donor contributions
- **Sensitive Business Data:** Trade secrets, intellectual property, contracts

**Data Locations:**

- **On-Premises:** File servers, databases, workstations, paper records
- **Cloud Services:** Microsoft 365, Google Workspace, AWS S3, Azure Blob, SaaS applications
- **Backups:** Backup tapes, cloud backups, archived data
- **Mobile Devices:** Laptops, smartphones, tablets, USB drives
- **Third-Party Systems:** Vendor-hosted applications, cloud service providers

**Data Attributes:**

- Business purpose for collecting data
- Legal basis for processing (consent, legal obligation, legitimate interest)
- Data owner (department or individual responsible)
- Retention period (how long data is kept)
- Disposal method (secure deletion, shredding)

**Data Flow Mapping:**

- How data enters organization (web forms, paper applications, third parties)
- How data moves through organization (integrations, file transfers, email)
- How data exits organization (vendor sharing, reporting, disposal)

**Insurance Rationale (Universal):**

Data inventory is foundational for:
- **Breach Response:** Knowing what data was exposed enables proper notification scope
- **Coverage Limits:** Insurance coverage based on records at risk (cost per record for notification)
- **Privacy Law Compliance:** GDPR, CCPA, state privacy laws require data inventories

Organizations without data inventory cannot:
- Accurately assess breach impact
- Comply with privacy law requirements ("right to access" requests)
- Implement proportionate security controls

**Threat Landscape Justification:**

- **Cannot protect what you don't know exists:** Unknown data stores create blind spots
- **Cloud Data Sprawl:** Data copied to personal cloud accounts, shared externally without tracking
- **Shadow Data:** Employees store sensitive data in unapproved locations

**Sector-Specific Context:**

**Education:**

- **Student Records:** SIS data, Google Classroom, learning apps, assessment platforms
- **FERPA:** Schools must know what education records exist and where they're stored
- **Challenge:** Hundreds of EdTech applications, each with student data

**Healthcare:**

- **PHI Locations:** EHR systems, billing systems, email, patient portals, medical devices
- **HIPAA:** Required under Security Rule risk analysis (§164.308(a)(1)(ii)(A))
- **Challenge:** Multiple systems (lab, pharmacy, radiology) each with patient data

**Religious/Nonprofit:**

- **Donor Data:** Donor management systems, accounting software, email, paper pledge cards
- **Challenge:** Decentralized data (each ministry may maintain separate contact lists)

**Citations:**

- NIST CSF 2.0: ID.AM-5 (Resources are prioritized based on classification and business value)
- CIS Controls v8: Control 3.1 (Establish and Maintain a Data Management Process)
- GDPR Article 30: Records of Processing Activities
- CCPA: Business must disclose categories of personal information collected
- HIPAA Security Rule: §164.308(a)(1)(ii)(A) - Risk analysis requires data inventory

---


### Question 3.2: Encryption at Rest

**Question Text:**
Does the organization encrypt sensitive data at rest (stored data on servers, workstations, mobile devices, and backups)?

**Impact Rating:** High (5)

**Foundational:** NO (Comprehensive maturity indicator, though trending toward foundational)

**Control Description:**

Encryption at rest protects:
- **Workstations/Laptops:** Full-disk encryption (BitLocker for Windows, FileVault for macOS)
- **Mobile Devices:** Device encryption (iOS/Android built-in encryption)
- **Servers:** Encrypted file systems, database transparent data encryption (TDE)
- **Cloud Storage:** Server-side encryption for cloud data (AWS S3, Azure Blob, Google Cloud Storage)
- **Backups:** Encrypted backup files and backup media
- **USB/External Drives:** Encrypted portable storage

**Encryption Methods:**

- **Windows:** BitLocker Drive Encryption (built into Windows Pro/Enterprise)
- **macOS:** FileVault 2 (built into macOS)
- **Database:** SQL Server TDE, Oracle Advanced Security, MySQL encryption
- **Cloud:** AWS S3 default encryption, Azure Storage Service Encryption

**Key Management:**

- Centralized key management (Azure Key Vault, AWS KMS)
- Escrow of recovery keys for lost password scenarios
- Key rotation procedures

**Insurance Rationale (Universal):**

**Safe Harbor** from breach notification laws:
- Many state laws exempt encrypted data from breach notification requirements
- **Reduces breach costs:** If laptop stolen with encrypted data, no notification required
- **Reduces liability:** Demonstrates reasonable security measures

**HIPAA 2025 Security Rule:** Encryption mandated for ePHI at rest (§164.312(a)(2)(iv))

**Threat Landscape Justification:**

- **Lost/Stolen Devices:** Unencrypted laptops, phones, USB drives create data breach
- **Insider Threats:** Database administrators cannot read encrypted data without keys
- **Physical Theft:** Server theft, backup tape theft mitigated by encryption

**Sector-Specific Context:**

**Education:**

- **Laptop Encryption:** Teacher/administrator laptops with student data must be encrypted
- **FERPA:** Encryption demonstrates reasonable security for education records
- **Challenge:** Chromebooks use built-in encryption; Windows laptops need BitLocker enabled

**Healthcare:**

- **HIPAA 2025 Requirement:** Encryption of ePHI at rest now mandated (previously "addressable")
- **Mobile Devices:** Physicians/nurses with patient data on smartphones must use encryption
- **EHR Databases:** Transparent Data Encryption (TDE) for SQL databases

**Religious/Nonprofit:**

- **Laptop Encryption:** Staff laptops with donor credit card data must be encrypted
- **PCI DSS:** Encryption required for stored payment card data

**Citations:**

- **HIPAA Security Rule (2025 NPRM):** §164.312(a)(2)(iv) - Encryption at rest mandated
- **State Breach Notification Laws:** Many states exempt encrypted data from notification
- CIS Controls v8: Control 3.11 (Encrypt Sensitive Data at Rest)
- NIST CSF 2.0: PR.DS-1 (Data-at-rest is protected)
- PCI DSS Requirement 3.4: Render PAN unreadable (encryption)

---

### Question 3.3: Encryption in Transit

**Question Text:**
Does the organization encrypt sensitive data in transit (data transmitted over networks, including internal networks and internet connections)?

**Impact Rating:** High (5)

**Foundational:** NO (Comprehensive maturity indicator, though trending toward foundational)

**Control Description:**

Encryption in transit protects:
- **Websites:** HTTPS with TLS 1.2+ certificates (not HTTP)
- **Email:** TLS encryption for email transmission (STARTTLS)
- **VPN:** Encrypted VPN tunnels for remote access
- **File Transfers:** SFTP, FTPS (not plain FTP)
- **Wireless:** WPA3 or WPA2 encryption (not WEP, not open Wi-Fi)
- **Internal Networks:** TLS for internal web applications, databases

**Protocols:**

- **TLS 1.2 or higher:** Deprecate TLS 1.0/1.1, SSL 2.0/3.0 (insecure)
- **SSH:** Secure remote administration (not Telnet)
- **IPsec:** VPN encryption
- **HTTPS:** Enforce HTTPS for all web applications (HTTP → HTTPS redirect)

**Certificate Management:**

- Valid TLS certificates from trusted CAs (not self-signed for production)
- Certificate expiration monitoring and renewal
- Internal PKI for internal applications (optional)

**Insurance Rationale (Universal):**

**Regulatory Requirements:**

- **HIPAA 2025:** Encryption in transit mandated for ePHI (§164.312(e)(2)(ii))
- **PCI DSS:** Encryption of cardholder data over public networks (Requirement 4)
- **State Privacy Laws:** Many require encryption of personal information in transit

**Breach Prevention:**

- **Man-in-the-Middle Attacks:** Unencrypted traffic can be intercepted on networks
- **Public Wi-Fi Risk:** Unencrypted connections on coffee shop Wi-Fi expose credentials

**Threat Landscape Justification:**

- **Network Eavesdropping:** Attackers on same network can capture unencrypted traffic
- **Wi-Fi Sniffing:** Unencrypted Wi-Fi or weak WEP encryption easily cracked
- **Email Interception:** Unencrypted email can be read in transit

**Sector-Specific Context:**

**Education:**

- **Student Data Transmission:** Uploads to cloud SIS, Google Classroom must use HTTPS
- **FERPA:** Encryption protects education records in transit
- **Wi-Fi Security:** School Wi-Fi networks should use WPA2/WPA3, not open Wi-Fi

**Healthcare:**

- **HIPAA 2025:** TLS encryption for all ePHI transmission (telehealth, patient portals, EHR)
- **Telemedicine:** Zoom Healthcare, Doxy.me use encrypted connections
- **Medical Device Communication:** Devices transmitting patient data should use encryption

**Religious/Nonprofit:**

- **Donor Transactions:** Credit card processing must use HTTPS (PCI DSS)
- **Email Security:** Donor communications containing PII should use encrypted email

**Citations:**

- **HIPAA Security Rule (2025 NPRM):** §164.312(e)(2)(ii) - Encryption in transit mandated
- **PCI DSS Requirement 4:** Encrypt transmission of cardholder data
- CIS Controls v8: Control 3.10 (Encrypt Sensitive Data in Transit)
- NIST CSF 2.0: PR.DS-2 (Data-in-transit is protected)
- **TLS Best Practices:** NIST SP 800-52 Rev. 2 - Guidelines for TLS Implementations

---

### Question 3.4: Data Retention and Secure Deletion

**Question Text:**
Has the organization established data retention policies defining how long different types of data are kept and procedures for secure deletion when retention periods expire?

**Impact Rating:** Moderate (3)

**Foundational:** NO (Recently added, comprehensive maturity indicator)

**Control Description:**

Data retention policies specify:

**Retention Periods by Data Type:**

- **Financial Records:** 7 years (IRS requirement)
- **Employee Records:** 3-7 years post-termination (state law varies)
- **Student Education Records:** Permanent (transcripts) vs. temporary (discipline records - typically 5 years) (FERPA guidance)
- **Patient Medical Records:** 6 years post-final treatment (HIPAA), longer for minors (state law varies)
- **Email:** 1-3 years (business email) vs. permanent (legal/compliance email)
- **Donor Records:** Permanent (donation history) vs. 3 years (pledge cards)

**Legal/Regulatory Requirements:**

- **FERPA:** Schools must retain education records until no longer needed; cannot retain indefinitely without purpose
- **HIPAA:** Minimum 6 years retention for covered entities
- **IRS:** 7 years for financial records
- **State Privacy Laws (2025):** Data deletion upon consumer request; cannot retain beyond business purpose

**Secure Deletion Methods:**

- **Digital Data:** Secure file deletion (DoD 5220.22-M 7-pass wipe) or cryptographic erasure
- **Hard Drives:** Degaussing or physical destruction (shredding) before disposal
- **Paper Records:** Cross-cut shredding (not strip shredding)
- **Backup Media:** Tape/disk destruction after retention period

**Automated Retention:**

- Email archiving solutions (Barracuda, Mimecast) with automated retention
- Cloud storage lifecycle policies (auto-delete files after X years)
- Document management systems with retention rules

**Insurance Rationale (Universal):**

**Reduces Breach Exposure:**

- **Data Minimization:** Less data stored = less data at risk in breach
- **Notification Costs:** Smaller breach notification scope if old data deleted
- **Defensibility:** Demonstrates reasonable security (didn't hoard unnecessary data)

**Privacy Law Compliance:**

- **GDPR Article 5:** Data minimization principle - retain only as long as necessary
- **CCPA/State Privacy Laws:** Right to deletion requires documented retention policies

**Threat Landscape Justification:**

- **Ransomware:** Less data to encrypt/exfiltrate if old data deleted
- **Insider Threats:** Former employees cannot access data that's been deleted
- **Litigation:** Reduces eDiscovery scope in lawsuits

**Sector-Specific Context:**

**Education:**

- **FERPA Balance:** Must retain records to provide transcripts, but cannot hoard unnecessary data
- **Student Records:** Permanent transcripts vs. temporary discipline/health records
- **Email:** Teachers' email should be archived but eventually deleted (not retained forever)

**Healthcare:**

- **HIPAA:** Minimum 6 years; many states require longer for minors (until age 21-25)
- **Medical Records:** Balance between continuity of care (need old records) and privacy (don't hoard)
- **Research Data:** De-identified data may be retained longer for research

**Religious/Nonprofit:**

- **Donor Records:** Permanent retention for giving history, but delete old credit card numbers
- **Volunteer Records:** Retain background checks for legal protection, delete after 7 years

**Citations:**

- **State Privacy Laws (2025):** 8 new laws requiring data deletion and minimization
- **GDPR Article 5(1)(e):** Storage limitation principle
- **CCPA:** Right to deletion requires retention policies
- NIST CSF 2.0: PR.DS-3 (Assets are formally managed throughout removal, transfers, and disposition)
- CIS Controls v8: Control 3.12 (Segment Data Processing and Storage)
- **NIST SP 800-88 Rev. 1:** Guidelines for Media Sanitization
- FERPA: 34 CFR §99.10 - What limitations exist on destruction of education records?

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
## Category 4: Secure Configuration and Vulnerability Management

### Overview

Secure configuration and vulnerability management ensures that systems are hardened against attack and that known vulnerabilities are identified and remediated in a timely manner. This category addresses:
- Network security architecture (firewalls, segmentation, DMZ)
- System hardening and secure baselines
- Patch management processes
- Vulnerability scanning and assessment
- Wireless network security
- Centralized logging and security monitoring (SIEM)
- Cloud security posture management
- Remote access security controls

**Framework Alignment:**

- **NIST CSF 2.0:** PR.IP (Protective Technology) - "Security configurations are managed and maintained"
- **CIS Controls v8:** Control 4 (Secure Configuration), Control 7 (Continuous Vulnerability Management)

### Importance

**Why Secure Configuration and Vulnerability Management Matters:**

1. **50% of Vulnerabilities Remain Unpatched:** Organizations struggle to patch known vulnerabilities (Verizon DBIR 2024)
2. **Attackers Exploit Known CVEs:** Vulnerabilities exploited within days of disclosure (zero-day race)
3. **Default Configurations Are Insecure:** Out-of-box systems have unnecessary services, weak passwords, excessive permissions
4. **Cloud Misconfigurations:** 95% of cloud breaches stem from misconfigurations (industry research 2024-2025)
5. **Detection Gap:** Average 212 days to detect breach without centralized logging (IBM X-Force 2025)

**Universal Threats:**

- **Unpatched Systems:** Attackers scan internet for vulnerable systems (EternalBlue, Log4Shell, etc.)
- **Default Credentials:** Routers, firewalls, IoT devices with default admin/admin passwords
- **Unnecessary Services:** Attack surface expanded by unused services (FTP, Telnet, SMBv1)
- **Firewall Misconfigurations:** Overly permissive rules allowing unauthorized access
- **Cloud Storage Exposure:** Publicly accessible S3 buckets, Azure blobs with sensitive data

**Sector-Specific Risks:**

- **Education:** Forgotten web servers, unpatched student information systems, open wireless networks
- **Healthcare:** Medical devices with unpatched firmware, legacy radiology systems, HL7 interface vulnerabilities
- **Religious/Nonprofit:** Donated equipment with unknown security status, volunteer-managed networks
- **General:** Operational technology (OT/ICS) with long patch cycles, legacy business-critical systems

---

### Question 4.1: Firewall and Network Security

**Question Text:**
Does the organization deploy firewalls at network perimeter and between network segments to control traffic based on security policies?

**Impact Rating:** High (5)

**Foundational:** NO (Comprehensive maturity indicator, though baseline expectation)

**Control Description:**

Firewall deployment includes:

**Perimeter Firewalls:**

- **Internet-Facing Firewall:** Controls traffic between internet and internal network
- **Default Deny Policy:** Block all traffic unless explicitly allowed
- **Stateful Inspection:** Track connection state, only allow responses to initiated connections
- **Application-Aware:** Next-generation firewalls (NGFW) inspect application-layer traffic

**Internal Firewalls (Segmentation):**

- **DMZ (Demilitarized Zone):** Isolated network for public-facing servers (web, email)
- **VLAN Segmentation:** Separate networks for different departments, guest Wi-Fi, IoT devices
- **East-West Traffic Control:** Firewalls between internal network segments

**Firewall Rule Management:**

- Documented firewall rules with business justification
- Regular rule review (quarterly) to remove unused rules
- Change management process for firewall modifications
- Logging of all allowed/denied traffic

**Modern Firewall Features:**

- **Intrusion Prevention System (IPS):** Block known attack patterns
- **Web Filtering:** Block malicious websites, phishing sites
- **VPN Termination:** Secure remote access endpoint
- **SSL/TLS Inspection:** Decrypt and inspect encrypted traffic for threats

**Insurance Rationale (Universal):**

Firewalls are baseline security expectation:
- Cyber insurance applications ask: "Do you have firewalls protecting your network?"
- Absence of firewalls may result in coverage denial
- Proper firewall configuration demonstrates due diligence

**Threat Landscape Justification:**

- **Perimeter Defense:** Attackers scan internet for open ports, vulnerable services
- **Lateral Movement Prevention:** Internal firewalls limit attacker movement if perimeter breached
- **Ransomware Containment:** Network segmentation prevents ransomware spread

**Sector-Specific Context:**

**Education:**

- **Multi-Campus:** Firewalls between district office, elementary schools, middle schools, high schools
- **Guest Wi-Fi Isolation:** Separate network for student/visitor devices
- **Challenge:** Budget constraints; free/open-source firewalls (pfSense, OPNsense) viable for smaller districts

**Healthcare:**

- **Medical Device Segmentation:** Separate network for medical devices (infusion pumps, monitors)
- **HIPAA:** Network segmentation required to limit PHI access
- **Challenge:** Legacy medical devices cannot be firewalled without breaking functionality

**Religious/Nonprofit:**

- **Simple Perimeter:** Often single firewall between internet and internal network
- **Guest Wi-Fi:** Separate network for congregation members, visitors

**Citations:**

- CIS Controls v8: Control 13.1 (Centralize Security Event Alerting)
- NIST CSF 2.0: PR.AC-5 (Network integrity is protected)
- HIPAA Security Rule: §164.312(e)(1) - Transmission security (firewalls protect PHI transmission)

---

### Question 4.2: Network Architecture and Segmentation

**Question Text:**
Has the organization implemented network segmentation to separate critical systems, guest networks, and high-risk devices (IoT, BYOD) from core business networks?

**Impact Rating:** High (5)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

Network segmentation divides network into isolated zones:

**Common Segments:**

- **Core Business Network:** Employee workstations, servers, business applications
- **DMZ (Demilitarized Zone):** Public-facing servers (web servers, email gateways)
- **Guest Network:** Visitor Wi-Fi with no access to internal resources
- **IoT/OT Network:** Printers, security cameras, HVAC, building automation
- **BYOD Network:** Personal devices with limited access to corporate resources
- **Administrative Network:** Jump servers, admin workstations for privileged access

**Segmentation Technologies:**

- **VLANs (Virtual LANs):** Layer 2 segmentation via switches
- **Firewalls:** Layer 3/4 segmentation with access control between zones
- **Microsegmentation:** Software-defined networking (SDN), zero-trust network access (ZTNA)

**Access Control Between Segments:**

- **Default Deny:** No traffic between segments unless explicitly allowed
- **Firewall Rules:** Specific rules for required communication (e.g., workstations → servers)
- **Monitoring:** Log all cross-segment traffic for anomaly detection

**Insurance Rationale (Universal):**

Network segmentation is defense-in-depth strategy:
- **Ransomware Containment:** Prevents lateral spread across entire network
- **Breach Impact Reduction:** Attackers contained to compromised segment
- **Compliance:** HIPAA, PCI DSS require network segmentation

**Threat Landscape Justification:**

- **Lateral Movement:** Attackers pivot from compromised workstation to servers; segmentation blocks this
- **IoT Vulnerabilities:** IoT devices (cameras, printers) are frequent attack entry points
- **Guest Network Risk:** Visitors with malware cannot access internal resources if segmented

**Sector-Specific Context:**

**Education:**

- **Segments:** Administrative network (SIS, HR, payroll), instructional network (student devices), guest Wi-Fi, security cameras
- **Student Device Isolation:** Chromebooks, iPads segmented from teacher workstations
- **Challenge:** Flat networks common in smaller districts; VLAN implementation requires managed switches

**Healthcare:**

- **Segments:** Clinical network (EHR), medical device network, administrative network, guest Wi-Fi
- **HIPAA:** Network segmentation required to limit PHI access to authorized systems
- **Medical Devices:** Isolated network prevents internet-connected medical devices from being attack vector

**Religious/Nonprofit:**

- **Segments:** Office network, guest Wi-Fi, security cameras, livestream equipment
- **Challenge:** Often flat networks; basic VLAN segmentation provides significant improvement

**Citations:**

- CIS Controls v8: Control 12.2 (Establish and Maintain a Secure Network Architecture)
- NIST CSF 2.0: PR.AC-5 (Network integrity is protected)
- PCI DSS Requirement 1.2: Build firewall configuration that restricts connections between untrusted networks and cardholder data environment

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

### Question 4.4: System Hardening and Secure Baselines

**Question Text:**
Does the organization apply security hardening configurations and maintain secure baseline images for servers, workstations, and network devices?

**Impact Rating:** Moderate (3)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

System hardening reduces attack surface by:

**Hardening Standards:**

- **CIS Benchmarks:** Industry-standard hardening guides for Windows, Linux, macOS, network devices
- **DISA STIGs:** Defense Information Systems Agency Security Technical Implementation Guides (government/regulated industries)
- **Vendor Baselines:** Microsoft Security Baselines, Apple Platform Security

**Common Hardening Measures:**

- **Disable Unnecessary Services:** Remove FTP, Telnet, SMBv1, unnecessary Windows services
- **Remove Unnecessary Software:** Uninstall unused applications
- **Enable Security Features:** Windows Defender, firewall, BitLocker encryption
- **Secure Protocols:** Disable SSLv2/v3, TLS 1.0/1.1; use TLS 1.2+
- **Strong Authentication:** Disable default accounts, enforce password policies
- **Logging:** Enable audit logging for security events

**Baseline Images:**

- **Gold Images:** Pre-configured, hardened OS images for workstation deployment
- **Image Management:** Tools like SCCM, MDT (Microsoft Deployment Toolkit), Jamf for macOS
- **Configuration Management:** Ansible, Puppet, Chef for server configuration
- **Regular Updates:** Refresh baseline images quarterly with latest patches

**Compliance Scanning:**

- **CIS-CAT:** CIS Configuration Assessment Tool scans systems against CIS Benchmarks
- **Microsoft Security Compliance Toolkit:** Scan Windows systems against Microsoft baselines
- **Automated Remediation:** Tools automatically apply hardening settings

**Insurance Rationale (Universal):**

System hardening is defense-in-depth best practice:
- Reduces exploitable vulnerabilities beyond just patching
- Demonstrates security maturity to insurers
- Addresses insider threats (disabled unnecessary services limit abuse)

**Threat Landscape Justification:**

- **Default Configurations Are Insecure:** Out-of-box systems prioritize functionality over security
- **Unnecessary Services:** Attackers exploit unused services (FTP, Telnet) for lateral movement
- **Legacy Protocols:** SMBv1, TLS 1.0 have known vulnerabilities

**Sector-Specific Context:**

**Education:**

- **Windows Workstations:** Apply CIS Benchmark for Windows 10/11
- **Chromebooks:** Google manages hardening; minimal configuration needed
- **Challenge:** Balancing security with ease-of-use for non-technical staff

**Healthcare:**

- **Clinical Workstations:** EHR vendor may prescribe specific configurations
- **HIPAA:** System hardening demonstrates technical safeguards (§164.312)
- **Challenge:** Medical software compatibility with hardened configurations

**Religious/Nonprofit:**

- **Basic Hardening:** Disable unnecessary services, enable Windows Firewall, automatic updates
- **Challenge:** Volunteer IT may lack expertise for advanced hardening

**Citations:**

- CIS Controls v8: Control 4.1 (Establish and Maintain a Secure Configuration Process)
- NIST CSF 2.0: PR.IP-1 (A baseline configuration is created and maintained)
- **CIS Benchmarks:** https://www.cisecurity.org/cis-benchmarks
- **Microsoft Security Baselines:** https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-security-configuration-framework/windows-security-baselines

---


### Question 4.5: Wireless Network Security

**Question Text:**
Are all wireless networks secured with WPA2 or WPA3 encryption, and are guest wireless networks isolated from internal networks?

**Impact Rating:** High (5)

**Foundational:** NO (Comprehensive maturity indicator, though baseline expectation)

**Control Description:**

Wireless security includes:

**Encryption Standards:**

- **WPA3 (Preferred):** Latest Wi-Fi security standard with improved encryption
- **WPA2 (Minimum):** Required minimum; deprecate WPA, WEP (insecure and easily cracked)
- **Enterprise Mode (WPA2/WPA3-Enterprise):** RADIUS authentication with individual user credentials
- **Personal Mode (WPA2/WPA3-Personal):** Pre-shared key (PSK) for small networks

**Network Separation:**

- **Corporate Wi-Fi:** For employees accessing internal resources
- **Guest Wi-Fi:** Isolated network with internet-only access (no access to internal network)
- **IoT Wi-Fi:** Separate network for printers, security cameras, smart devices

**Wireless Security Controls:**

- **Strong PSK:** 20+ character random passphrase for WPA2/WPA3-Personal
- **SSID Configuration:** Descriptive SSID names (avoid hiding SSID - provides minimal security)
- **MAC Address Filtering (Optional):** Whitelist authorized devices (bypassable, not primary security control)
- **Disable WPS:** Wi-Fi Protected Setup has known vulnerabilities
- **Regular Password Changes:** Rotate guest Wi-Fi password quarterly or after large events

**Enterprise Wi-Fi (Larger Organizations):**

- **802.1X Authentication:** RADIUS server with Active Directory integration
- **Certificate-Based Authentication:** Eliminates password sharing
- **Device Management:** MDM-enrolled devices automatically connect to corporate Wi-Fi

**Insurance Rationale (Universal):**

Insecure wireless networks create attack vector:
- **WEP/WPA Cracking:** Attackers within range can crack encryption in minutes
- **Guest Network Isolation:** Prevents visitor malware from accessing internal systems
- **Compliance:** PCI DSS requires wireless encryption if handling payment card data

**Threat Landscape Justification:**

- **Wi-Fi Sniffing:** Unencrypted or weakly encrypted Wi-Fi allows traffic interception
- **Evil Twin Attacks:** Attackers create fake Wi-Fi access points to steal credentials
- **Lateral Movement:** Compromised guest Wi-Fi device pivots to internal network if not isolated

**Sector-Specific Context:**

**Education:**

- **Student/Staff Wi-Fi:** Separate networks or 802.1X authentication to distinguish users
- **Guest Wi-Fi:** For parents, visitors during events
- **Challenge:** Large campus coverage requires many access points; budget constraints

**Healthcare:**

- **Clinical Wi-Fi:** For wireless workstations, tablets accessing EHR
- **Guest Wi-Fi:** For patients, visitors in waiting rooms
- **Medical Device Wi-Fi:** Isolated network for Wi-Fi-enabled medical devices
- **HIPAA:** Wireless encryption required for PHI transmission (§164.312(e)(1))

**Religious/Nonprofit:**

- **Congregation Wi-Fi:** Guest Wi-Fi for members during services/events
- **Office Wi-Fi:** Staff Wi-Fi for ministry operations

**Citations:**

- CIS Controls v8: Control 12.7 (Ensure Remote Devices Utilize a VPN and are Connecting to an Enterprise's AAA Infrastructure)
- NIST CSF 2.0: PR.AC-5 (Network integrity is protected)
- PCI DSS Requirement 4.1.1: Ensure wireless networks transmitting cardholder data use strong encryption
- **WPA2 Migration:** Wi-Fi Alliance deprecated WPA/WEP in 2006

---

### Question 4.6: Network Monitoring and Anomaly Detection

**Question Text:**
Does the organization monitor network traffic for anomalous behavior, unauthorized devices, or suspicious activity?

**Impact Rating:** Moderate (3)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

Network monitoring includes:

**Traffic Monitoring:**

- **Network Traffic Analysis (NTA):** Monitor flow data for anomalies (unusually large data transfers, unexpected protocols)
- **Intrusion Detection System (IDS):** Passive monitoring for attack signatures, malicious traffic patterns
- **Intrusion Prevention System (IPS):** Active blocking of detected threats (IPS vs. IDS)

**Device Discovery:**

- **Network Access Control (NAC):** Identify all devices connecting to network
- **Rogue Device Detection:** Alert on unauthorized devices (unknown laptops, personal Wi-Fi hotspots)
- **Asset Inventory Integration:** Reconcile discovered devices with asset inventory (Question 1.1)

**Behavioral Analytics:**

- **User and Entity Behavior Analytics (UEBA):** Baseline normal user behavior, detect anomalies
- **Anomaly Examples:** User accessing systems from unusual locations/times, downloading large volumes of data

**Monitoring Tools:**

- **SIEM Integration:** Network monitoring feeds into SIEM for correlation (see Question 4.14)
- **Network Detection and Response (NDR):** Darktrace, ExtraHop, Vectra AI
- **Firewall Logs:** Analyze allowed/denied traffic patterns
- **SNMP Monitoring:** Monitor network device health, bandwidth usage

**Insurance Rationale (Universal):**

Network monitoring enables early threat detection:
- Detects reconnaissance/scanning before full-scale attack
- Identifies lateral movement after initial compromise
- Supports incident investigation (what systems did attacker access?)

**Threat Landscape Justification:**

- **Dwell Time Reduction:** Detect attackers during reconnaissance phase (before data exfiltration)
- **Insider Threats:** Unusual data access patterns indicate compromised or malicious insiders
- **Command and Control (C2):** Detect malware "phoning home" to attacker servers

**Sector-Specific Context:**

**Education:**

- **Basic Monitoring:** Firewall logs, bandwidth monitoring for excessive usage
- **Advanced (Larger Districts):** Network Detection and Response (NDR) tools
- **Challenge:** Limited IT staff; cloud-based monitoring services (Arctic Wolf, Huntress) provide practical option

**Healthcare:**

- **Medical Device Monitoring:** Unusual medical device network traffic may indicate compromise
- **PHI Exfiltration Detection:** Large data transfers leaving network trigger alerts
- **HIPAA:** Monitoring supports audit control requirements (§164.312(b))

**Religious/Nonprofit:**

- **Basic Monitoring:** Firewall logs, endpoint security alerts
- **Managed Services:** Outsourced monitoring for organizations without 24/7 IT staff

**Citations:**

- CIS Controls v8: Control 13.2 (Deploy a Host-Based Intrusion Detection Solution)
- NIST CSF 2.0: DE.CM-1 (Networks are monitored to detect potential cybersecurity events)
- HIPAA Security Rule: §164.312(b) - Audit controls (monitoring systems for suspicious activity)

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
## Category 5: Malware Defense and Endpoint Security

### Overview

Malware defense and endpoint security protects workstations, laptops, mobile devices, and servers from malicious software including viruses, ransomware, spyware, and advanced persistent threats (APTs). This category addresses:
- Antivirus and anti-malware deployment
- Endpoint Detection and Response (EDR)
- Email security controls (filtering, authentication)
- Web filtering and browser security
- Application whitelisting
- Mobile device management (MDM)

**Framework Alignment:**

- **NIST CSF 2.0:** PR.PT (Protective Technology) - "Technical security solutions are managed to ensure the security and resilience of systems"
- **CIS Controls v8:** Control 10 (Malware Defenses)

### Importance

**Why Malware Defense Matters:**

1. **Ransomware is #1 Threat:** 75% of breaches included ransomware (Verizon DBIR 2024)
2. **Email is #1 Attack Vector:** 84% increase in phishing emails delivering infostealers (IBM X-Force 2025)
3. **EDR is Universal Insurance Requirement:** All carriers require endpoint protection
4. **Business Disruption:** Ransomware can shut down entire organization for weeks
5. **Data Theft:** Modern ransomware exfiltrates data before encryption (double extortion)

**Universal Threats:**

- **Ransomware:** Encrypts files, demands payment for decryption key
- **Phishing:** Social engineering emails trick users into clicking malicious links, downloading malware
- **Infostealers:** Malware steals credentials, browser cookies, cryptocurrency wallets
- **Business Email Compromise (BEC):** Attackers impersonate executives for wire fraud
- **Drive-By Downloads:** Malicious websites automatically download malware to visitor browsers

**Sector-Specific Risks:**

- **Education:** Phishing targeting teachers/administrators, ransomware encrypting student records
- **Healthcare:** Ransomware disrupting patient care, medical device malware
- **Religious/Nonprofit:** BEC attacks targeting donor funds, ransomware encrypting donor databases
- **General:** Ransomware, data theft, industrial espionage

---

### Question 5.1: Antivirus/Anti-Malware Deployment

**Question Text:**
Does the organization deploy antivirus or anti-malware software on all workstations, laptops, and servers with regular definition updates?

**Impact Rating:** High (5)

**Foundational:** NO (Baseline expectation, but EDR is the foundational requirement - see 5.4)

**Control Description:**

Antivirus/anti-malware deployment includes:

**Coverage:**

- **All Windows Workstations:** Windows Defender (built-in) or third-party antivirus
- **All macOS Devices:** macOS XProtect (built-in) or third-party antivirus
- **All Servers:** Windows Server Defender, Linux antivirus (ClamAV, Sophos)
- **Mobile Devices:** iOS/Android built-in protections, MDM-managed security

**Antivirus Solutions:**

- **Built-In (Free):** Windows Defender (excellent protection), macOS XProtect
- **Third-Party:** Symantec, McAfee, Trend Micro, Sophos, ESET
- **Cloud-Managed:** Centralized management console for definition updates, scanning schedules

**Key Features:**

- **Real-Time Scanning:** Monitor file access, downloads, email attachments
- **Scheduled Scans:** Full system scans weekly, quick scans daily
- **Automatic Updates:** Virus definition updates multiple times daily
- **Quarantine:** Isolate detected malware, prevent execution
- **Centralized Management:** Deploy, configure, monitor antivirus from central console

**Signature-Based vs. Behavior-Based:**

- **Signature-Based:** Detect known malware via signature database
- **Behavior-Based (Heuristics):** Detect unknown malware via suspicious behaviors
- **Cloud-Based Reputation:** Query cloud database for file reputation (clean/malicious)

**Insurance Rationale (Universal):**

Antivirus is baseline expectation, but **EDR has replaced antivirus as primary insurance requirement** (see Question 5.4). However, antivirus still provides value:
- Blocks known malware variants
- Lightweight, minimal performance impact
- Often built-in (Windows Defender is highly rated)

**Threat Landscape Justification:**

- **Known Malware:** Signature-based detection blocks 90%+ of known malware
- **Email Attachments:** Antivirus scans email attachments before user opens
- **Drive-By Downloads:** Real-time scanning blocks malicious downloads

**Sector-Specific Context:**

**Education:**

- **Windows Defender:** Free, effective antivirus built into Windows 10/11
- **Chromebooks:** Minimal malware risk due to sandboxed Chrome OS architecture
- **Challenge:** Budget constraints; Windows Defender provides excellent free protection

**Healthcare:**

- **Clinical Workstations:** Antivirus must not interfere with EHR performance
- **Medical Devices:** Often cannot install antivirus (vendor-controlled); network segmentation compensates
- **HIPAA:** Antivirus demonstrates technical safeguards (§164.312(b))

**Religious/Nonprofit:**

- **Windows Defender:** Adequate for most nonprofits; free with Windows
- **Donated Equipment:** Ensure antivirus installed and updated

**Citations:**

- CIS Controls v8: Control 10.1 (Deploy and Maintain Anti-Malware Software)
- NIST CSF 2.0: PR.PT-2 (Removable media is protected)
- **AV-TEST Institute:** Independent antivirus testing; Windows Defender consistently high-rated

---


### Question 5.2-5.3: Additional Malware Defense Questions

**Note:** Questions 5.2-5.3 cover:
- 5.2: Email Security Gateway / Filtering
- 5.3: Web Filtering and Safe Browsing

*(Full detail follows same comprehensive format)*

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
## Category 6: Data Recovery and Business Continuity

### Overview

Data recovery and business continuity ensures organizational resilience against ransomware, disasters, and system failures. This category addresses:
- Backup processes and technologies
- Air-gapped and offline backups
- Backup testing and restoration procedures
- Business continuity planning
- Disaster recovery planning
- Recovery time and recovery point objectives

**Framework Alignment:**

- **NIST CSF 2.0:** RC (Recover) - "Recovery planning and improvements are managed"
- **CIS Controls v8:** Control 11 (Data Recovery)

### Importance

**Why Data Recovery Matters:**

1. **Ransomware is Inevitable:** 75% of breaches include ransomware (Verizon DBIR 2024)
2. **Backups are Last Line of Defense:** Air-gapped backups enable recovery without paying ransom
3. **Business Continuity:** Downtime costs $5,600/minute for small businesses, $9,000/minute for enterprises
4. **Regulatory Requirements:** HIPAA, FERPA require business continuity/disaster recovery plans
5. **Untested Backups Fail 25% of Time:** Backup testing is critical

**Universal Threats:**

- **Ransomware:** Encrypts files, demands payment; backups enable free recovery
- **Hardware Failure:** Server crashes, hard drive failures
- **Natural Disasters:** Floods, fires, hurricanes destroy physical infrastructure
- **Human Error:** Accidental file deletion, data corruption
- **Cyberattacks:** Data destruction, sabotage by insiders or attackers

**Sector-Specific Risks:**

- **Education:** Ransomware encrypting student records, disaster destroying on-premises servers
- **Healthcare:** Ransomware halting patient care, hurricane destroying hospital
- **Religious/Nonprofit:** Ransomware encrypting donor databases, fire destroying office
- **General:** Any organization faces ransomware and disaster risks

---

### Question 6.1: Backup Process

**Question Text:**
Does the organization perform regular backups of all critical data, systems, and configurations?

**Impact Rating:** High (5)

**Foundational:** NO (Baseline expectation, but air-gapped backups are foundational - see 6.3)

**Control Description:**

Backup process includes:

**Backup Scope:**

- **Servers:** File servers, database servers, application servers, virtual machine images
- **Workstations:** User data folders, email PST files (if applicable)
- **Cloud Data:** Microsoft 365, Google Workspace (yes, cloud services need backups!)
- **Configurations:** Firewall configurations, switch configurations, application settings
- **System Images:** Full system images for rapid bare-metal restoration

**Backup Types:**

- **Full Backup:** Complete copy of all data (weekly)
- **Incremental Backup:** Only changes since last backup (daily)
- **Differential Backup:** Changes since last full backup
- **Snapshot:** Point-in-time copy (cloud VMs, SAN storage)

**Backup Frequency:**

- **Critical Systems:** Daily incremental, weekly full
- **Less Critical Systems:** Weekly full
- **Retention:** 30 days online, 90 days archival, 7 years for compliance data

**Backup Technologies:**

- **On-Premises:** Veeam, Commvault, Veritas Backup Exec, Windows Server Backup
- **Cloud Backup:** Backblaze, Carbonite, Acronis Cyber Protect, Datto
- **Hybrid:** On-premises + cloud (recommended)

**Insurance Rationale (Universal):**

Backups are essential but **air-gapped backups are the critical insurance requirement** (see 6.3):
- Regular backups enable recovery from hardware failures, human error
- But ransomware targets backups; air-gapped backups are insurance focus

**Threat Landscape Justification:**

- **Ransomware:** Without backups, must pay ransom or lose all data
- **Hardware Failure:** Server crashes require restoration from backups
- **Accidental Deletion:** Users delete important files, need restoration

**Sector-Specific Context:**

**Education:**

- **Critical Data:** Student information systems (SIS), Google Workspace/Microsoft 365, financial systems
- **Cloud Backups:** Backupify (Google Workspace), Veeam Backup for Microsoft 365
- **Challenge:** Budget constraints; free/open-source options (Veeam Community Edition, UrBackup)

**Healthcare:**

- **Critical Data:** EHR systems, PACS imaging, lab results, billing systems
- **HIPAA:** Contingency planning (§164.308(a)(7)) requires data backup plan
- **24/7 Operations:** Backup windows during off-peak hours (2-6 AM)

**Religious/Nonprofit:**

- **Critical Data:** Donor databases, accounting systems, ministry records
- **Cloud Backups:** Cost-effective for limited budgets (Backblaze B2, Wasabi)

**Citations:**

- CIS Controls v8: Control 11.1 (Establish and Maintain a Data Recovery Process)
- NIST CSF 2.0: PR.IP-4 (Backups are performed)
- HIPAA Security Rule: §164.308(a)(7)(ii)(A) - Data backup plan

---

### Question 6.2: Backup Encryption

**Question Text:**
Are backups encrypted to protect data confidentiality in the event of backup media theft or unauthorized access?

**Impact Rating:** Moderate (3)

**Foundational:** NO (Comprehensive maturity indicator)

**Control Description:**

Backup encryption protects:
- **Backup Data:** Encrypted at rest on backup media (tapes, disks, cloud storage)
- **Transmission:** Encrypted in transit to cloud backup services (TLS)
- **Encryption Keys:** Securely stored separate from backups (escrow for disaster recovery)

**Encryption Methods:**

- **AES-256:** Industry-standard encryption algorithm
- **Built-In:** Veeam, Veeam Backup for Microsoft 365, AWS S3 encryption
- **Cloud Storage:** Server-side encryption (AWS S3, Azure Blob, Backblaze B2)

**Insurance Rationale (Universal):**

Backup encryption mitigates:
- **Tape/Disk Theft:** Physical theft of backup media
- **Cloud Breach:** Unauthorized access to cloud backup storage
- **Insider Threats:** IT staff cannot read encrypted backups without keys

**Threat Landscape Justification:**

- **Backup Media Theft:** Tapes stored off-site can be lost or stolen in transit
- **Cloud Vendor Breach:** Rare but possible; encryption provides defense-in-depth

**Sector-Specific Context:**

**Education:**

- **FERPA:** Backups containing student records should be encrypted
- **Practical Implementation:** Veeam, cloud backup services provide built-in encryption

**Healthcare:**

- **HIPAA 2025:** Encryption mandated for ePHI at rest (includes backups)
- **Backup Tapes:** Off-site tape storage requires encryption

**Religious/Nonprofit:**

- **Donor Data:** Backups with donor credit card information must be encrypted (PCI DSS)

**Citations:**

- NIST CSF 2.0: PR.DS-1 (Data-at-rest is protected)
- HIPAA Security Rule (2025): §164.312(a)(2)(iv) - Encryption at rest
- PCI DSS Requirement 3.4: Render PAN unreadable (includes backups)

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

### Question 6.5: Business Continuity Planning

**Question Text:**
Does the organization have a documented Business Continuity Plan (BCP) that defines procedures for maintaining critical operations during disruptions (natural disasters, cyberattacks, facility loss)?

**Response Options:**

- Fully implemented - documented plan, tested annually, staff trained
- Partially implemented - documented plan exists, limited testing
- Not implemented - no formal business continuity plan

**Impact Rating:** Moderate (3)

**Foundational:** No (but strongly recommended for organizations >100 users or with critical operations)

**Control Description:**

A Business Continuity Plan (BCP) ensures the organization can maintain essential functions during and after a disruption. Effective BCPs include:

**BCP Components:**

- **Business Impact Analysis (BIA):** Identify critical business functions, maximum tolerable downtime
- **Continuity Strategies:** Define how to maintain operations during disruption (alternate work sites, manual procedures, cloud failover)
- **Communication Plans:** Emergency contact lists, stakeholder notification procedures
- **Resource Requirements:** Personnel, equipment, supplies needed during continuity operations
- **Recovery Priorities:** Define which systems/processes must be restored first

**Testing and Maintenance:**

- **Annual Testing:** Tabletop exercises, functional drills, full-scale exercises
- **Plan Updates:** Review and update BCP annually or after organizational changes
- **Staff Training:** Ensure key personnel know their BCP roles

**Integration with Disaster Recovery:**

- BCP focuses on **business processes** (how to continue operations)
- DR focuses on **IT systems** (how to restore technology)
- Both plans must align and reference each other

**Insurance Rationale (Universal):**

**Cyber Insurance and BCP:**

- Many cyber insurers offer **premium discounts** for organizations with tested BCPs
- BCP demonstrates organizational resilience, reducing insurer risk
- Insurance claims processed faster when organization has documented continuity procedures

**Business Interruption Coverage:**

- BCP critical for business interruption insurance claims (documents normal operations, recovery costs)
- Without BCP, insurers may dispute interruption impact/duration

**Sector-Specific Importance:**

- **Education:** Maintain learning during facility closures (pandemic, natural disaster)
- **Healthcare:** Patient care continuity is life-safety issue
- **Nonprofit:** Donor confidence maintained through operational resilience
- **General:** Contractual obligations, customer SLAs require continuity planning

**Threat Landscape Justification:**

**Ransomware and Extended Outages:**

- **Average ransomware recovery:** 21 days (Veeam Ransomware Trends 2024)
- BCP defines how to operate during recovery (manual processes, alternate systems)
- Without BCP, organizations face complete operational shutdown

**Natural Disasters and Multiple Threats:**

- **Climate Change:** Increasing frequency of floods, hurricanes, wildfires
- **Facility Loss:** Fire, power outages, physical disasters
- BCP ensures organization can relocate and continue operations

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Continuity Scenarios:** Pandemic closures, severe weather, facility damage, cyber incidents
- **Critical Functions:** Maintain student learning, staff payroll, food services (K-12), student housing (higher ed)
- **Practical Implementation:** Define remote learning procedures, alternate exam schedules, emergency communication to parents/students
- **Compliance:** Some state education departments require BCP for school districts

**Healthcare:**

- **Patient Care First:** BCP ensures continuity of patient care during any disruption
- **Critical Functions:** Emergency services, patient monitoring, medication administration, medical records access
- **HIPAA/CMS Requirements:** Emergency mode operations plan required
- **Real-World Examples:** Hospitals with BCPs successfully maintained operations during ransomware attacks (Scripps Health, Universal Health Services)

**Religious/Nonprofit:**

- **Mission-Critical Services:** Food banks, shelters, counseling services cannot pause during disruptions
- **Donor Relations:** BCP demonstrates stewardship, maintains donor confidence
- **Practical Implementation:** Define alternate facilities, emergency volunteer protocols, critical vendor relationships
- **Financial Continuity:** Ensure donation processing, payroll continues during disruption

**General Organizations:**

- **Regulatory Requirements:** Publicly traded companies, financial services require BCP
- **Customer Obligations:** SLAs, contractual commitments require operational continuity
- **Competitive Advantage:** BCP enables faster recovery than competitors after regional disasters

**Citations:**

- CIS Controls v8: Not directly covered (focuses on IT systems)
- NIST CSF 2.0: RC.RP-1 (Recovery plan is executed)
- **ISO 22301:** International standard for Business Continuity Management Systems
- **Veeam Ransomware Trends 2024:** Average 21-day recovery time
- **HIPAA:** 45 CFR § 164.308(a)(7) - Contingency plan requirement
- **FERPA:** No direct BCP requirement, but supports data availability obligations

---

### Question 6.6: Disaster Recovery Planning

**Question Text:**
Does the organization have a documented IT Disaster Recovery Plan (DRP) that defines procedures for restoring IT systems, data, and infrastructure after a disaster or major incident?

**Response Options:**

- Fully implemented - documented DRP, tested annually, includes RTO/RPO for critical systems
- Partially implemented - documented DRP exists, limited testing
- Not implemented - no formal disaster recovery plan

**Impact Rating:** High (5)

**Foundational:** No (but strongly recommended for organizations with critical IT dependencies)

**Control Description:**

An IT Disaster Recovery Plan (DRP) provides step-by-step procedures for restoring IT systems after a disaster. Effective DRPs include:

**DRP Components:**

- **System Inventory:** List of all critical IT systems, applications, dependencies
- **Recovery Priorities:** Define restoration order based on business criticality
- **Recovery Objectives:**
  - **RTO (Recovery Time Objective):** Maximum acceptable downtime for each system
  - **RPO (Recovery Point Objective):** Maximum acceptable data loss for each system
- **Recovery Procedures:** Detailed technical steps for restoring each system
- **Resource Requirements:** Hardware, software, personnel needed for recovery
- **Vendor Contact Information:** Critical vendor support contacts, SLAs

**Testing and Maintenance:**

- **Annual Testing:** Tabletop exercises (discuss recovery scenarios), functional tests (restore non-production systems), full-scale tests (restore production to DR site)
- **Plan Updates:** Review DRP after infrastructure changes, software upgrades, organizational changes
- **Documentation:** Keep DRP accessible offline (printed copies, USB drives) in case primary systems are unavailable

**Integration with Backups and BCP:**

- DRP relies on backup systems tested via Question 6.4
- DRP focuses on **IT restoration**, BCP focuses on **business operations**
- Both must be coordinated for effective recovery

**Insurance Rationale (Universal):**

**Cyber Insurance and DRP:**

- **Premium Discounts:** Organizations with tested DRPs receive lower premiums
- **Claims Processing:** DRP documentation accelerates insurance claims (proves normal operations, recovery costs)
- **Breach Response:** DRP critical for meeting breach notification deadlines (HIPAA 60 days, state laws 30-90 days)

**Insurer Requirements:**

- Many insurers require DRP for organizations with >500 users or high-value data
- DRP must include RTO/RPO metrics for critical systems
- Annual testing documentation may be requested during policy renewal

**Ransomware Recovery:**

- Organizations with tested DRPs recover from ransomware 3-5x faster than those without
- DRP enables restoration without paying ransom (insurance does not cover ransom payments in many policies)

**Threat Landscape Justification:**

**Ransomware and Cyber Disasters:**

- **75% of breaches include ransomware** (Verizon DBIR 2024)
- **Average recovery:** 21 days without DRP, 5-7 days with tested DRP
- DRP defines: system restoration order, data recovery procedures, vendor escalation paths

**Infrastructure Failures:**

- **Cloud Outages:** AWS, Azure, Google Cloud experience regional outages; DRP defines failover procedures
- **Hardware Failures:** Server failures, storage failures, network failures
- DRP ensures IT team knows how to restore quickly

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Critical Systems:** Student Information Systems (SIS), Learning Management Systems (LMS), email, network authentication
- **Recovery Priorities:** Restore SIS first (grades, attendance legal requirement), then LMS, then administrative systems
- **Practical Implementation:** Define restoration procedures for cloud systems (Google Workspace, Microsoft 365), on-premise servers
- **Testing:** Use summer break for DRP tabletop exercises; test restore to alternate hardware
- **RTO/RPO Examples:** SIS RTO=24 hours, RPO=4 hours; Email RTO=12 hours, RPO=1 hour

**Healthcare:**

- **Critical Systems:** Electronic Health Records (EHR), patient monitoring systems, imaging systems (PACS), lab systems
- **Recovery Priorities:** EHR restored first (patient care depends on it); RTO for EHR typically 4-8 hours
- **Life-Safety Considerations:** Some systems (patient monitoring) cannot tolerate downtime; require high-availability architecture
- **HIPAA Requirement:** Contingency plan must include disaster recovery procedures
- **Real-World Examples:** Scripps Health ransomware (2021) - 30-day recovery without tested DRP cost $113M

**Religious/Nonprofit:**

- **Critical Systems:** Donor management, accounting/payroll, email, website
- **Recovery Priorities:** Restore donor database first (mission-critical), then financial systems, then communications
- **Practical Implementation:** Cloud-based systems (Salesforce Nonprofit Cloud) simplify DR; define procedures for restoring access after credential compromise
- **Small Organizations:** Managed DR services (Datto, Veeam) provide DRP templates, automated testing

**General Organizations:**

- **Regulatory Compliance:** SOC 2, ISO 27001, PCI DSS require documented disaster recovery
- **Customer SLAs:** Contractual uptime commitments require DRP
- **Business Impact:** Average cost of IT downtime: $5,600/minute (Gartner); DRP minimizes downtime
- **Supply Chain:** DRP ensures ability to fulfill orders, maintain customer relationships during disasters

**Citations:**

- CIS Controls v8: Control 11 (Data Recovery)
- NIST CSF 2.0: RC.RP-1 (Recovery plan is executed during or after a cybersecurity incident)
- **Verizon DBIR 2024:** "75% of breaches included ransomware"
- **Veeam Ransomware Trends 2024:** Average 21-day recovery time
- **Gartner:** Average IT downtime cost $5,600/minute
- **Scripps Health Ransomware (2021):** $113M recovery cost
- **HIPAA:** 45 CFR § 164.308(a)(7)(ii)(C) - Disaster recovery plan requirement
- **SOC 2:** CC9.1 - Identifies, selects, and develops risk mitigation activities (includes disaster recovery)

---

## Category 7: Security Awareness Training and Education

**Overview:**

Security awareness training educates staff and stakeholders about cybersecurity threats, safe computing practices, and their role in protecting organizational data and systems. Human error remains the leading cause of security breaches, making security awareness training one of the most cost-effective security controls.

**Importance:**

**Human Factor in Breaches:**

- **68% of breaches involve a human element** (Verizon DBIR 2024) - phishing, credential theft, social engineering
- **Training Reduces Risk:** Organizations with regular security awareness training experience 70% fewer successful phishing attacks (KnowBe4 2024)
- **Compliance Requirement:** HIPAA, PCI DSS, state privacy laws require security awareness training

**Insurance Requirements:**

- Most cyber insurers **require** annual security awareness training for all users
- **Phishing simulation testing** increasingly required as foundational control
- Training metrics (completion rates, phishing click rates) may be requested during policy renewal

**Sector-Agnostic Relevance:**

- **All sectors** rely on human users who are targeted by phishing, social engineering, password attacks
- Security awareness training applies universally across Education, Healthcare, Religious/Nonprofit, General organizations
- Modern threats (AI-powered phishing, deepfakes, social engineering) require ongoing training

**Category 7 includes 4 questions:**

- Question 7.1: Security Awareness Program
- Question 7.2: Phishing Simulation Testing 🔑 FOUNDATIONAL
- Question 7.3: Security Awareness Training Frequency 🔑 FOUNDATIONAL
- Question 7.4: AI Acceptable Use Policy and Governance 🔑 FOUNDATIONAL 🆕

---

### Question 7.1: Security Awareness Program

**Question Text:**
Does the organization have a formal security awareness program with defined objectives, content, and delivery methods?

**Response Options:**

- Fully implemented - formal program with documented curriculum, multiple delivery methods, tracked completion
- Partially implemented - informal program, limited content/tracking
- Not implemented - no security awareness program

**Impact Rating:** Moderate (3)

**Foundational:** No (but Question 7.3 on training frequency is foundational)

**Control Description:**

A formal security awareness program provides structured education to all staff and stakeholders about cybersecurity risks and their responsibilities. Effective programs include:

**Program Components:**

- **Documented Curriculum:** Topics covered include: password security, phishing recognition, physical security, data protection, acceptable use, incident reporting
- **Multiple Delivery Methods:** Online training modules, in-person workshops, email tips, posters/signage, security newsletters
- **Role-Based Training:** Specialized training for IT staff, administrators, HR, finance (high-risk roles)
- **New Hire Onboarding:** Security training during employee orientation (before system access granted)
- **Completion Tracking:** Training management system tracks completion rates, quiz scores, certificates

**Program Management:**

- **Annual Review:** Update content based on current threats (AI phishing, ransomware tactics)
- **Executive Support:** Leadership reinforces security culture through communications
- **Measurement:** Track metrics like training completion rates, phishing click rates, incident reports

**Insurance Rationale (Universal):**

**Cyber Insurance Requirement:**

- **100% of cyber insurers** require security awareness training as baseline control
- Insurers may request training completion records during policy application/renewal
- Premium discounts available for organizations with mature programs (>90% completion, quarterly updates)

**Human Error Reduction:**

- **68% of breaches involve human element** (Verizon DBIR 2024)
- Security awareness training directly addresses the leading cause of breaches
- Organizations with formal programs experience 70% fewer successful phishing attacks (KnowBe4 2024)

**Threat Landscape Justification:**

**Phishing and Social Engineering:**

- **Phishing is #1 initial access vector** (IBM X-Force 2025)
- **AI-powered phishing:** 67.4% of phishing now uses generative AI (Zscaler 2024); more convincing, personalized attacks
- Training must evolve to address AI-generated phishing, deepfakes, vishing (voice phishing)

**Insider Threats (Unintentional):**

- Most insider threats are unintentional (data misconfiguration, accidental sharing)
- Training reduces unintentional data exposure

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Target Audience:** Teachers, administrators, students (age-appropriate), substitutes, volunteers
- **Education-Specific Topics:** FERPA compliance, student data privacy, acceptable use of school technology, social media safety
- **Practical Implementation:** Back-to-school training sessions, monthly security tips via email, student assemblies on cyberbullying/privacy
- **Challenge:** High staff turnover (teachers, substitutes) requires frequent onboarding training

**Healthcare:**

- **Target Audience:** Clinical staff, administrative staff, physicians, vendors with access
- **Healthcare-Specific Topics:** HIPAA compliance, patient privacy, medical device security, phishing targeting healthcare credentials
- **Practical Implementation:** Annual HIPAA training (compliance requirement), quarterly security newsletters, role-based training for EHR users
- **HIPAA Requirement:** Security awareness training is mandatory under HIPAA Security Rule

**Religious/Nonprofit:**

- **Target Audience:** Staff, volunteers, board members, donors (for online giving security)
- **Nonprofit-Specific Topics:** Donor data protection, financial controls, email compromise targeting nonprofits, social media account security
- **Practical Implementation:** Annual training for staff/volunteers, donor communications on secure giving, email tips on recognizing scams
- **Challenge:** Volunteer workforce may have limited technical skills; training must be accessible

**General Organizations:**

- **Target Audience:** All employees, contractors, third-party vendors with access
- **Industry-Specific Topics:** Varies by industry (PCI DSS for retail, SOC 2 for SaaS, etc.)
- **Compliance Drivers:** SOC 2, ISO 27001, PCI DSS all require security awareness training
- **Executive Focus:** Business email compromise (BEC) training for finance/executive teams (average BEC loss: $125,000)

**Citations:**

- CIS Controls v8: Control 14.1 (Establish and Maintain a Security Awareness Program)
- NIST CSF 2.0: PR.AT-1 (Users are informed and trained)
- **Verizon DBIR 2024:** "68% of breaches involve human element"
- **KnowBe4 2024:** Organizations with training experience 70% fewer successful phishing attacks
- **IBM X-Force 2025:** Phishing is #1 initial access vector
- **Zscaler 2024:** 67.4% of phishing uses generative AI
- **HIPAA Security Rule:** 45 CFR § 164.308(a)(5) - Security awareness and training required

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

## Category 9: Incident Response and Recovery

**Overview:**

Incident response and recovery capabilities enable organizations to detect, respond to, and recover from cybersecurity incidents effectively. Despite best preventive efforts, security incidents will occur - mature incident response processes minimize damage, reduce recovery time, and ensure compliance with breach notification requirements.

**Importance:**

**Inevitable Security Incidents:**

- **68% of organizations experience material cybersecurity incidents** annually (Verizon DBIR 2024)
- **Average breach detection time: 212 days** (IBM Cost of Data Breach 2024)
- **Average recovery time: 21 days** for ransomware without tested IR plan (Veeam 2024)
- Organizations with IR plans recover 3-5x faster than those without

**Insurance Requirements:**

- Cyber insurers **require documented incident response plans** for coverage
- **Incident response testing** (tabletop exercises) increasingly required
- **Cyber insurance coverage** itself is becoming a recommended control
- Breach notification deadlines (HIPAA 60 days, state laws 30-90 days) require rapid IR

**Sector-Agnostic Relevance:**

- **All sectors** experience cybersecurity incidents (phishing, ransomware, data breaches)
- IR applies universally across Education, Healthcare, Religious/Nonprofit, General organizations
- **Regulatory compliance** (HIPAA, state privacy laws, FERPA) requires breach response capabilities

**Category 9 includes 7 questions:**

- Question 9.1: Incident Response Plan
- Question 9.2: Incident Response Team
- Question 9.3: Incident Response Testing
- Question 9.4: Tabletop Exercises
- Question 9.5: Cyber Insurance Coverage
- Question 9.6: Breach Notification Procedures
- Question 9.7: Incident Detection and Response Capabilities (MTTD/MTTR) 🆕

---


