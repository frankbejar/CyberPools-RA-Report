---
title: Category 2 - Account Management and Access Control
tags:
  - Category 2
  - Foundational
  - High Impact
  - Moderate Impact
---

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
