# Dual-Score Assessment Structure with Insurance Rationale

## Overview

This document outlines the complete assessment structure for the **recommended Dual-Score Model**, showing all 52 questions across 9 categories and identifying the 12 foundational questions that map to The Trust's 7 simplified cyber requirements.

### Assessment Components

- **Total Questions:** 52 questions
- **Categories:** 9 security control categories
- **Foundational Questions:** 12 questions (marked with 🔑) that map to The Trust's 7 requirements

### Scoring Structure (Recommended Approach)

1. **Foundation Score (Tier I)** - Based on 12 foundational questions
   - Insurance-critical controls (core requirements for 2024-2025 cyber insurance)
   - Binary compliance focus: Fully Implemented vs. Not Met
   - Determines insurance eligibility and premium tier

2. **Comprehensive Score (Tier II)** - Based on all 52 questions
   - Full security maturity assessment
   - Risk-based scoring: Control Rating × Impact Rating
   - Demonstrates overall cybersecurity posture

---

## Assessment Questions by Category

### Category 1: Inventory and Control of Assets

**Purpose:** Establish visibility and control over hardware and software assets to reduce attack surface and ensure proper lifecycle management.

**Questions (4 total):**

#### 1.1 - Does the organization inventory all company-owned devices?

- **Impact:** Moderate (3)
- **Control Description:** Establish and maintain an inventory of all end-user assets with the potential to store, transmit, or change data. This often includes devices such as desktops, laptops, and mobile devices (tablets and cellphones).

**Insurance Rationale:**
Asset inventory is foundational to cyber risk assessment. Insurers require organizations to demonstrate visibility into their IT environment. Cyber insurance applications commonly request network diagrams and asset inventories as part of underwriting documentation. Without asset visibility, organizations cannot effectively apply security controls, patch systems, or detect unauthorized devices—all of which increase breach likelihood and insurance claims.

**Citations:**
- CIS Controls v8 (Control 1: Inventory and Control of Enterprise Assets)
- Cyber insurance applications require evidence of asset management capabilities
- MoneyGeek Cyber Insurance Guide (2025): "Insurers are scrutinizing security postures more rigorously, demanding evidence of strong cyber hygiene"

---

#### 1.2 - Does the organization have a way to identify and address any unauthorized assets from the network (wired and wireless)?

- **Impact:** Moderate (3)
- **Control Description:** Ensure a process exists to identify and address unauthorized assets frequently. This includes wireless access and wired network ports. The enterprise may choose to remove the asset from the network, deny the asset from connecting remotely to the network, or quarantine the asset.

**Insurance Rationale:**
Rogue devices represent significant security blind spots and are common entry points for breaches. K-12 schools with BYOD environments and guest networks face heightened risk. Insurance carriers view unauthorized asset detection as essential to preventing lateral movement during attacks. Many ransomware incidents begin with unmanaged devices lacking security controls.

**Citations:**
- NIST Cybersecurity Framework 2.0 (ID.AM-1: Inventories of hardware are maintained)
- CIS Controls v8 (Control 1.5: Use asset inventory to address unauthorized assets)
- K-12 cybersecurity compliance requirements emphasize network access control (Duo Security, 2024)

---

#### 1.3 - Does the organization maintain an inventory of all licensed software installed across the organization?

- **Impact:** Moderate (3)
- **Control Description:** Establish and maintain a detailed inventory of all licensed software installed on enterprise assets. The software inventory should document important attributes such as the title, publisher, initial install/use date, and business purpose for each entry; where appropriate, include the Uniform Resource Locator (URL), app store(s), version(s), deployment mechanism, and decommission date. Review and update the software inventory bi-annually, or more frequently.

**Insurance Rationale:**
Software inventory directly impacts patch management capabilities and license compliance. Insurers assess whether organizations know what software is running and can update it promptly. Unlicensed software introduces legal liability and often lacks security updates. Shadow IT applications may lack security controls, creating data breach exposure.

**Citations:**
- CIS Controls v8 (Control 2: Inventory and Control of Software Assets)
- Cyber insurance applications require evidence of software asset management
- Woodruff Sawyer (2024): "Insurers require evidence of vulnerability management programs"

---

#### 🔑 1.4 - FOUNDATIONAL - Has the organization adopted and implemented plans to retire or protect and segregate end-of-life software?

- **Impact:** High (5)
- **Control Description:** Ensure that only currently supported software is designated as authorized in the software inventory for enterprise assets. Any end-of-life (EOL) software, which is unsupported, yet necessary for the fulfillment of the enterprise's mission, should be segmented, with proper controls and regular audits to ensure that the software is free of any compromises.
- **Trust Requirement:** End-of-life software management

**Insurance Rationale (FOUNDATIONAL):**
End-of-life software is a critical underwriting factor. Unsupported operating systems (Windows 7, Server 2008) and applications lack security patches, making them primary ransomware targets. Many insurers will decline coverage or exclude EOL systems from policies. The 2023 MOVEit vulnerability affected legacy systems, resulting in massive insurance claims. Insurers require attestation that critical systems are supported with vendor patches.

**Citations:**
- **Coalition Cyber Threat Index (2024-2025):** Organizations running EOL systems face significantly higher breach risk
  - URL: https://www.coalitioninc.com/announcements/cyber-threat-index-2025
- **Cyber Insurance Academy (2025):** "End-of-life systems represent uninsurable risk for many carriers"
- **CIS Controls v8 (Control 2.4):** Remove unsupported software
- **K-12 Context:** Many schools run legacy student information systems on EOL platforms (CDT K-12 Cybersecurity Report)

---

### Category 2: Account Management

**Purpose:** Control access to systems and data through proper identity management, authentication, and account lifecycle processes.

**Questions (9 total, 4 foundational):**

#### 2.1 - Does the organization have an inventory of all user accounts including users/admins/service accounts?

- **Impact:** Moderate (3)
- **Control Description:** Establish and maintain an inventory of all user, administrator, and service accounts, including names, usernames, start/stop dates, and departments. Validate account authorization at least quarterly. Service accounts should follow the principle of least privilege, use long complex passwords or key-based authentication, and undergo regular monitoring for abnormal activity. Password changes should occur only when compromise is suspected, not on arbitrary schedules (per NIST SP 800-63B).

**Insurance Rationale:**
Account inventory is essential for access control audits and detecting compromised credentials. Service account mismanagement is a common attack vector, as these accounts often have elevated privileges and weak oversight. Insurers assess whether organizations can quickly disable accounts during security incidents or employee terminations. Dormant accounts are frequently exploited in breaches.

**Citations:**
- NIST Cybersecurity Framework 2.0 (PR.AC-1: Identities and credentials are issued, managed, and verified)
- CIS Controls v8 (Control 5: Account Management)
- Cyber insurance applications require evidence of identity and access management practices

---

#### 2.2 - Does the organization enforce a password policy that adheres to industry best practices?

- **Impact:** High (5)
- **Control Description:** Ensure the organization has implemented and enforces a password policy that aligns with current best practices as outlined by leading authorities such as NIST, CISA, Microsoft, and other cybersecurity experts.

**Insurance Rationale:**
Password policies directly impact credential compromise risk. Modern guidance emphasizes length over complexity, elimination of forced rotations, and use of password managers. Weak passwords remain the primary initial access vector in cyber insurance claims. Many 2024-2025 policies require minimum 12-14 character passwords.

**Citations:**
- **MoneyGeek Cyber Insurance Guide (2025):** "Most cyber insurance policies require 12+ character passwords"
- **NIST Special Publication 800-63B:** Password guidelines for federal systems (adopted by insurers)
- **Centre Technologies (2025):** "Insurance carriers expect alignment with NIST password guidance"

---

#### 🔑 2.3 - FOUNDATIONAL - Is MFA enabled and enforced for all cloud resources, including email, document repositories, messaging or meeting platforms, and identity and access management tools?

- **Impact:** High (5)
- **Control Description:** MFA is essential for safeguarding critical assets, ensuring that unauthorized individuals cannot access sensitive systems or data even if one factor is compromised. It should be implemented for all user accounts interacting with organizational data or systems, prioritizing high-risk assets and accounts.
- **Trust Requirement:** Multi-Factor Authentication (1 of 4 MFA questions)

**Insurance Rationale (FOUNDATIONAL):**
MFA is the single most critical underwriting factor for 2024-2025 cyber insurance. According to Coalition's 2025 Cyber Threat Index, **most ransomware attacks start with compromised VPNs and remote access credentials**, highlighting the critical importance of MFA. Cloud resources are prime targets as they contain organizational email, documents, and identity systems. MFA prevents account takeover even when credentials are phished or breached. Nearly all 2025 policies mandate MFA for cloud access, with some carriers declining coverage without it.

**Citations:**
- **Coalition Cyber Threat Index (2025):** Most ransomware attacks start with compromised VPNs and remote access credentials
  - URL: https://www.coalitioninc.com/announcements/cyber-threat-index-2025
- **Aldridge (2025):** "Multi-factor authentication is mandatory for nearly all policies in 2025"
  - URL: https://aldridge.com/5-requirements-to-get-cyber-insurance/
- **Woodruff Sawyer (2024):** "MFA is non-negotiable for cyber insurance qualification"
  - URL: https://woodruffsawyer.com/insights/cyber-insurance-requirements-next-frontier
- **Microsoft Security (2019):** MFA blocks 99.9% of automated credential attacks
  - URL: https://www.microsoft.com/en-us/security/blog/2019/08/20/one-simple-action-you-can-take-to-prevent-99-9-percent-of-account-attacks/
- **K-12 Context:** FERPA compliance best practices recommend MFA for systems containing student PII to ensure reasonable security measures (Kiteworks FERPA Compliance Guide)

---

#### 🔑 2.4 - FOUNDATIONAL - Is MFA implemented for remote access to on-premises or hub networks?

- **Impact:** High (5)
- **Control Description:** MFA is essential for safeguarding critical assets, ensuring that unauthorized individuals cannot access sensitive systems or data even if one factor is compromised.
- **Trust Requirement:** Multi-Factor Authentication (2 of 4 MFA questions)

**Insurance Rationale (FOUNDATIONAL):**
Remote access via VPN is the #1 initial access vector for ransomware attacks. During COVID-19, schools expanded remote access, creating persistent attack surface. Attackers routinely scan for VPN endpoints and attempt credential stuffing. MFA for VPN access is universally required by cyber insurers and is specifically highlighted in insurance applications.

**Citations:**
- **MoneyGeek (2025):** "Insurers expect MFA for remote network access"
  - URL: https://www.moneygeek.com/insurance/business/cyber-insurance/requirements/
- **CybelAngel (2025):** "MFA on VPN/remote access is a universal baseline requirement"
  - URL: https://cybelangel.com/cyber-insurance-requirements/
- **Verizon DBIR (2024):** Remote access exploitation is top attack path
- **K-12 Context:** Remote access to student information systems requires MFA (CDT K-12 Report)

---

#### 🔑 2.5 - FOUNDATIONAL - Is MFA in place for all admin or privileged user accounts to ensure enhanced protection against unauthorized access?

- **Impact:** High (5)
- **Control Description:** MFA is essential for safeguarding critical assets, ensuring that unauthorized individuals cannot access sensitive systems or data even if one factor is compromised.
- **Trust Requirement:** Multi-Factor Authentication (3 of 4 MFA questions)

**Insurance Rationale (FOUNDATIONAL):**
Privileged accounts have elevated permissions to modify systems, access sensitive data, and disable security controls. Compromised admin credentials enable lateral movement and data exfiltration. Attackers specifically target administrative accounts for maximum impact. Insurers view privileged access management (PAM) as critical, with MFA on admin accounts being a minimum requirement.

**Citations:**
- **Upward Technology (2024):** "Insurers universally require MFA on privileged accounts"
  - URL: https://www.upward-technology.com/10-security-controls-recommended-by-cyber-insurers/
- **Centre Technologies (2025):** "Admin account MFA is mandatory for 2025 policies"
  - URL: https://blog.centretechnologies.com/how-to-meet-cyber-insurance-requirements-in-2025
- **CIS Controls v8 (Control 5.4):** Restrict administrator privileges and require MFA
- **CISA CPGs:** Account security includes MFA for privileged users

---

#### 🔑 2.6 - FOUNDATIONAL - Does the organization enforce MFA for access to all critical systems and data?

- **Impact:** High (5)
- **Control Description:** MFA is essential for safeguarding critical assets, ensuring that unauthorized individuals cannot access sensitive systems or data even if one factor is compromised.
- **Trust Requirement:** Multi-Factor Authentication (4 of 4 MFA questions)

**Insurance Rationale (FOUNDATIONAL):**
Beyond cloud and VPN, organizations have on-premises critical systems (student information systems, financial systems, databases) that require MFA protection. Comprehensive MFA coverage prevents attackers from pivoting to unprotected systems after initial compromise. Insurers assess MFA deployment breadth, not just presence. Partial MFA implementation leaves exploitable gaps.

**Citations:**
- **Aldridge (2025):** "MFA must extend beyond email to all critical systems"
  - URL: https://aldridge.com/5-requirements-to-get-cyber-insurance/
- **Cyber Insurance Academy (2025):** Insurers verify MFA scope during underwriting
  - URL: https://www.cyberinsuranceacademy.com/blog/guides/cyber-insurance-minimum-requirements/
- **K-12 Context:** Best practices for FERPA-regulated systems recommend MFA to ensure reasonable security measures protecting student records

---

#### 2.7 - Does the organization have a process to identify and disable dormant accounts after a defined period of inactivity?

- **Impact:** High (5)
- **Control Description:** The organization should implement a process to regularly monitor and identify dormant or inactive accounts. Disable or remove such accounts after 45 days of inactivity (or a timeframe aligned with organizational policy) to minimize security risks from unused credentials.

**Insurance Rationale:**
Dormant accounts are frequently exploited by attackers as they often have weak monitoring and unchanged passwords. Former employee accounts and unused service accounts provide covert access. Insurers view dormant account management as a hygiene indicator of overall identity governance maturity.

**Citations:**
- CIS Controls v8 (Control 5.3): Disable dormant accounts
- NIST Cybersecurity Framework 2.0 (PR.AC-1): Account management includes deactivation
- Cyber insurance applications commonly ask about account lifecycle processes

---

#### 2.8 - Does the organization have a policy and standard operating procedures outlined for onboarding or change in position?

- **Impact:** High (5)
- **Control Description:** Implement and maintain a policy with clear, documented procedures for granting access to enterprise assets during onboarding or role changes. This process should include automated workflows where possible to ensure timely, consistent, and secure access provisioning.

**Insurance Rationale:**
Onboarding procedures ensure new employees receive appropriate access without over-provisioning. Role changes often result in privilege creep (accumulating permissions from previous roles). Insurers assess whether organizations follow least-privilege principles and have documented access control processes.

**Citations:**
- CIS Controls v8 (Control 5): Account management includes provisioning processes
- SOC 2 Type II audits (common for vendors) require documented onboarding procedures
- K-12 Context: Teacher/staff turnover requires robust onboarding (Duo Security K-12 Report)

---

#### 2.9 - Does the organization have a policy and standard operating procedures outlined for off-boarding?

- **Impact:** High (5)
- **Control Description:** Establish and maintain a policy with clear procedures for promptly revoking access to enterprise assets during off-boarding. Utilize automated processes where possible to disable accounts immediately upon termination while preserving audit trails.

**Insurance Rationale:**
Delayed off-boarding creates insider threat risk and enables former employees to access data post-termination. Many data breaches involve terminated employees retaining access. Insurers specifically assess off-boarding speed and completeness during underwriting. K-12 schools with high staff turnover face elevated risk if off-boarding is manual.

**Citations:**
- CIS Controls v8 (Control 5): Account management includes deprovisioning
- Verizon DBIR (2024): Insider threats include terminated employees with lingering access
- FERPA compliance best practices recommend immediate revocation of access to student records upon termination to maintain reasonable security measures

---

### Category 3: Data Protection

**Purpose:** Protect sensitive data through proper identification, access controls, encryption, and lifecycle management.

**Questions (4 total):**

#### 3.1 - Does the organization have an inventory of critical data?

- **Impact:** Low (1)
- **Control Description:** Establish and maintain a data inventory, based on the enterprise's data management process. Inventory sensitive data, at a minimum. Review and update inventory annually, at a minimum, with a priority on sensitive data.

**Insurance Rationale:**
Data inventory enables targeted protection and reduces breach notification costs. Organizations must know where sensitive data resides to apply encryption, access controls, and monitoring. Insurers assess data classification maturity, as organizations without data inventories cannot demonstrate adequate protection. Breach notification costs scale with untracked data exposure.

**Citations:**
- NIST Cybersecurity Framework 2.0 (ID.AM-5: Resources are prioritized based on classification)
- CIS Controls v8 (Control 3.1): Establish and maintain data inventory
- FERPA compliance best practices emphasize knowing where student education records are stored for proper access control and breach notification (Protecting Student Privacy, 2024)

---

#### 3.2 - Do administrators have separate dedicated admin accounts for conducting high-privilege tasks?

- **Impact:** Moderate (3)
- **Control Description:** Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Conduct general computing activities, such as internet browsing, email, and productivity suite use, from the user's primary, non-privileged account.

**Insurance Rationale:**
Admin account separation prevents malware from standard user activities (email phishing, web browsing) from gaining elevated privileges. Attackers exploit this by phishing administrators who use privileged accounts for daily tasks. Separate admin accounts with PAM tools reduce lateral movement risk after initial compromise.

**Citations:**
- CIS Controls v8 (Control 5.4): Restrict administrator privileges
- Microsoft Security: Admin account separation is fundamental privileged access management
- Cyber insurance underwriting assesses privileged access management controls

---

#### 3.3 - Does the organization encrypt hard drives on endpoints, servers, and on-premises backups?

- **Impact:** High (5)
- **Control Description:** Encrypt data on end-user devices containing sensitive data. Example implementations can include Windows BitLocker, Apple FileVault, Linux dm-crypt.

**Insurance Rationale:**
Full-disk encryption protects data at rest from theft, loss, or unauthorized physical access. Lost/stolen laptops with student data trigger breach notifications unless encrypted. Many state breach notification laws exempt encrypted data. Insurers assess encryption as a baseline control for mobile devices and backups. Encrypted backups prevent ransomware actors from exfiltrating backup data.

**Citations:**
- FERPA compliance best practices strongly recommend encryption for student records in transit and at rest to ensure reasonable security measures (Kiteworks FERPA Guide, 2024)
- CIS Controls v8 (Control 3.6): Encrypt data on end-user devices
- Cyber insurance applications routinely ask about endpoint encryption deployment
- K-12 Context: Lost teacher laptops with unencrypted student data trigger costly breach notifications

---

#### 3.4 - Does the organization have a data retention policy that specifies how long organizational data is retained and when it should be securely deleted?

- **Impact:** Moderate (3)
- **Control Description:** Establish and maintain a documented data retention policy that defines retention schedules for different data types (student records, financial data, operational data, backups) based on legal requirements, business needs, and privacy principles. The policy should include procedures for secure deletion when retention periods expire, ensuring data minimization and reducing exposure in the event of a breach.

**Insurance Rationale:**
Data retention policies directly reduce breach liability and regulatory penalties. Organizations holding unnecessary data face larger breach notification costs, regulatory fines, and potential lawsuits. Data minimization is a core privacy principle in FERPA, COPPA, and state privacy laws. Cyber insurers assess data retention as risk mitigation—less stored data means smaller breach impact and lower potential claims. Schools accumulating years of student data without deletion face amplified breach consequences.

**Citations:**
- **FERPA Compliance (Kiteworks, 2024):** "Clear data retention policies outline specific duration for student records, balancing legal requirements with data minimization"
- **Protecting Student Privacy (ED.gov):** "Some student data must be retained and others deleted as part of faithful data management practices"
- **K-12 Cybersecurity (CDT, 2024):** Data minimization reduces breach impact in ed-tech environments
- **Cyber Insurance:** Data retention policies demonstrate privacy governance maturity to underwriters
- **State Privacy Laws:** Many states require reasonable data retention policies (CCPA, VCDPA, etc.)

---

### Category 4: Secure Configuration of Enterprise Assets

**Purpose:** Harden systems and networks through secure configuration, patch management, and vulnerability management.

**Questions (13 total, 2 foundational):**

#### 4.1 - Does the organization have physical security measures in place to protect on-premises network and system infrastructure?

- **Impact:** Moderate (3)
- **Control Description:** Implement and maintain physical security measures to protect on-premises network and system infrastructure. This includes securing server rooms, network closets, and other critical infrastructure locations against unauthorized access, environmental threats, and physical tampering.

**Insurance Rationale:**
Physical security prevents direct access to network infrastructure, servers, and backup systems. Unlocked server rooms enable malicious insiders or intruders to bypass network controls, steal data, or install rogue devices. K-12 schools with distributed campuses and multi-tenant buildings face heightened physical security challenges. Insurers assess physical controls as part of holistic security posture.

**Citations:**
- CIS Controls v8 (Control 1.4): Physical devices are secured
- NIST Cybersecurity Framework 2.0 (PR.PT-2: Removable media is protected and usage is restricted)
- K-12 Context: Schools must secure network closets and server rooms from students/visitors

---

#### 4.2 - Does the organization have a secure configuration process for endpoint devices?

- **Impact:** Moderate (3)
- **Control Description:** Establish and maintain a secure configuration process for all enterprise assets, including end-user devices, IoT devices, servers, and software. This process should include creating a standardized "golden image" for endpoint deployment that incorporates the latest OS patches, removal or hardening of default accounts, and restrictions on software installations to approved applications only.

**Insurance Rationale:**
Secure baseline configurations reduce attack surface by disabling unnecessary services, removing default credentials, and enforcing security settings. Consistent configurations enable rapid patching and reduce vulnerabilities. Insurers assess configuration management maturity, as ad-hoc device provisioning creates security gaps and complicates incident response.

**Citations:**
- CIS Controls v8 (Control 4: Secure Configuration of Enterprise Assets and Software)
- NIST Cybersecurity Framework 2.0 (PR.IP-1: Baseline configurations are created and maintained)
- Cyber insurance applications ask about configuration management processes

---

#### 🔑 4.3 - FOUNDATIONAL - Does the organization have a Patch Management Process to install all software patches within 30 or fewer days and critical and high-severity patches within 7 days?

- **Impact:** High (5)
- **Control Description:** Perform operating system updates on enterprise assets on a monthly, or more frequent, basis (preferably automated).
- **Trust Requirement:** Patch management

**Insurance Rationale (FOUNDATIONAL):**
Patch management is a universal cyber insurance requirement and a critical underwriting factor. **Cyber insurers expect timely deployment of critical and zero-day patches, with routine patches within 30 days**. Unpatched vulnerabilities are the #2 initial access vector (after phishing) in ransomware attacks. Many high-profile breaches exploit known vulnerabilities with available patches. Automated patch management demonstrates mature security operations. Manual patching in K-12 with limited IT staff creates dangerous delays.

**Citations:**
- **MoneyGeek (2025):** Cyber insurance requires "quarterly software updates" and timely critical patch deployment
  - URL: https://www.moneygeek.com/insurance/business/cyber-insurance/requirements/
- **Woodruff Sawyer (2024):** "Insurers review patch management to assess if assets are low-hanging fruit"
  - URL: https://woodruffsawyer.com/insights/cyber-insurance-requirements-next-frontier
- **Upward Technology (2024):** Patch management is top 10 control recommended by cyber insurers
  - URL: https://www.upward-technology.com/10-security-controls-recommended-by-cyber-insurers/
- **Verizon DBIR (2024):** Exploitation of known vulnerabilities is leading breach vector
- **CIS Controls v8 (Control 7):** Continuous vulnerability management

---

#### 4.4 - Does the organization's Patch Management Process address both operating systems and installed applications?

- **Impact:** High (5)
- **Control Description:** Perform operating system updates on enterprise assets on a monthly, or more frequent, basis (preferably automated).

**Insurance Rationale:**
Application vulnerabilities are as exploitable as OS vulnerabilities. Attackers target unpatched browsers, PDF readers, Java, and other common applications. Comprehensive patch management covering both OS and applications is essential. Many organizations patch OS but neglect third-party applications, creating exploitable gaps. Insurers assess patch scope, not just OS patching.

**Citations:**
- CIS Controls v8 (Control 7.2): Perform automated application patching
- Verizon DBIR (2024): Application vulnerabilities are frequently exploited
- Cyber insurance underwriting includes questions about application patch management

---

#### 4.5 - Does the organization have a secure configuration process for networking devices?

- **Impact:** High (5)
- **Control Description:** Establish and maintain a secure configuration process for network devices. This includes management of default accounts on enterprise assets and software, such as root, administrator, and other pre-configured vendor accounts.

**Insurance Rationale:**
Network devices (firewalls, switches, routers) with default credentials or weak configurations are common initial access points. Attackers routinely scan for default vendor passwords. Misconfigurations in firewalls create unintended exposure. Secure network device configuration is fundamental to perimeter defense and network segmentation.

**Citations:**
- CIS Controls v8 (Control 4.1): Establish secure configurations for network infrastructure
- NIST Cybersecurity Framework 2.0 (PR.IP-1): Baseline configurations for network devices
- K-12 Context: Legacy network equipment often retains default credentials

---

#### 4.6 - Does the organization have a process to ensure that network infrastructure (e.g., routers, switches, firewalls, network appliances) remain updated and supported with the latest security patches and firmware updates?

- **Impact:** High (5)
- **Control Description:** Establish and maintain a secure configuration process for network devices to ensure they remain updated and supported with the latest security patches and firmware updates.

**Insurance Rationale:**
Network infrastructure vulnerabilities enable perimeter bypass and internal lateral movement. Firewall and VPN vulnerabilities are high-value targets for sophisticated attackers. Many organizations patch servers and workstations but neglect network device firmware, creating persistent vulnerabilities. Insurers assess whether network infrastructure receives timely updates.

**Citations:**
- CIS Controls v8 (Control 7): Continuous vulnerability management includes network devices
- CISA Known Exploited Vulnerabilities (KEV) catalog includes numerous network device CVEs
- Cyber insurance applications ask about network infrastructure patch management

---

#### 🔑 4.7 - FOUNDATIONAL - Does the organization conduct regular external vulnerability scans?

- **Impact:** Moderate (3)
- **Control Description:** Regular external-facing vulnerability scans help identify and address potential system weaknesses and reduce security risks. It is recommended to conduct vulnerability scans at least quarterly to maintain a strong security posture.
- **Trust Requirement:** External vulnerability scanning

**Insurance Rationale (FOUNDATIONAL):**
External vulnerability scanning is a standard cyber insurance requirement and underwriting verification point. **Insurers commonly require quarterly scans as part of policy conditions.** Scans identify internet-facing vulnerabilities before attackers exploit them. Many insurers partner with or recommend specific scanning vendors. Scan results provide objective evidence of patch management effectiveness. Schools with public-facing web applications and remote access need continuous scanning.

**Citations:**
- **MoneyGeek (2025):** "Vulnerability scanning should be conducted quarterly at minimum"
  - URL: https://www.moneygeek.com/insurance/business/cyber-insurance/requirements/
- **CybelAngel (2025):** "Requirements include automated vulnerability scanning"
  - URL: https://cybelangel.com/cyber-insurance-requirements/
- **Upward Technology (2024):** Vulnerability scanning is top 10 control recommended by insurers
  - URL: https://www.upward-technology.com/10-security-controls-recommended-by-cyber-insurers/
- **CIS Controls v8 (Control 7.5):** Perform automated external vulnerability scans quarterly
- **CISA CPGs:** Device security includes vulnerability scanning

---

#### 4.8 - Has the organization configured session lockout times for endpoints?

- **Impact:** Moderate (3)
- **Control Description:** Configure automatic session locking on enterprise assets after a defined period of inactivity. For general-purpose operating systems, the period should not exceed 15 minutes. For mobile end-user devices, the period should not exceed 2 minutes.

**Insurance Rationale:**
Session lockouts prevent unauthorized physical access to unlocked workstations. In K-12 environments, students may access teacher workstations if left unlocked. Automatic lockouts enforce access control even with user error. While not a primary insurance factor, session management demonstrates security awareness and policy enforcement.

**Citations:**
- CIS Controls v8 (Control 4.3): Configure automatic session locking
- FERPA compliance: Student record access control best practices include authentication and session management to ensure reasonable security measures
- NIST Cybersecurity Framework 2.0 (PR.AC-7): Session management is enforced

---

#### 4.9 - Does the organization have different networks or subnets for employees and non-employees?

- **Impact:** Moderate (3)
- **Control Description:** Deploy and maintain a secure network architecture to ensure networks are configured based on the purpose of the workload in the respective network. Each network or subnet in an organization should be segmented to prevent unauthorized access.

**Insurance Rationale:**
Network segmentation limits lateral movement after initial compromise. Guest networks should be isolated from internal resources. K-12 schools with student devices, staff devices, IoT (cameras, door systems), and guest WiFi require segmentation. Flat networks allow ransomware to spread rapidly across all systems. Insurers assess network architecture as risk mitigation.

**Citations:**
- CIS Controls v8 (Control 12.2): Establish network segmentation
- NIST Cybersecurity Framework 2.0 (PR.AC-5): Network integrity is protected
- K-12 Context: Schools need segmentation between student, staff, and IoT networks (Duo Security)

---

#### 4.10 - Are the wireless networks segmented from each other?

- **Impact:** Moderate (3)
- **Control Description:** Deploy and maintain a secure wireless network architecture to ensure networks are configured based on the purpose of the workload in the respective network.

**Insurance Rationale:**
Wireless network segmentation prevents guest or student WiFi from accessing internal resources. Many K-12 schools provide open guest WiFi, creating attack surface if not isolated. Segmented wireless prevents compromised student devices from pivoting to staff systems or servers.

**Citations:**
- CIS Controls v8 (Control 12): Network infrastructure management includes wireless segmentation
- K-12 Context: Student wireless should be isolated from administrative systems

---

#### 4.11 - Does the organization use WPA2 or better for its wireless network(s)?

- **Impact:** Moderate (3)
- **Control Description:** The wireless network access controls should be deployed with the latest accepted encryption standards (WPA2 or better).

**Insurance Rationale:**
WPA2 (or WPA3) encryption protects wireless traffic from eavesdropping. Older WEP/WPA encryption is easily cracked. Unencrypted or weakly encrypted wireless enables attackers to intercept credentials and data. Modern encryption standards are baseline expectations for network security.

**Citations:**
- CIS Controls v8 (Control 12.5): Centrally manage wireless encryption
- NIST guidance recommends WPA2 or WPA3 for wireless security

---

#### 4.12 - Does the organization protect access via 802.1X or similar?

- **Impact:** Moderate (3)
- **Control Description:** Wireless access should be deployed so that each user is given access with their enterprise credentials.

**Insurance Rationale:**
802.1X authentication ensures each user has individual credentials for wireless access, enabling accountability and access control. Pre-shared keys (PSK) create shared passwords that can't be traced to individuals. Enterprise authentication integrates with Active Directory/identity systems for centralized management. While not a primary insurance factor, enterprise WiFi authentication demonstrates mature access control.

**Citations:**
- CIS Controls v8 (Control 12): Network access control
- K-12 Context: Individual student/staff credentials for wireless enable accountability

---

#### 4.13 - Does the organization change any wireless PSKs annually?

- **Impact:** Moderate (3)
- **Control Description:** PSK should only be used for guest wireless access. PSK should be changed annually to prevent any unwanted or unauthorized access from intruders.

**Insurance Rationale:**
Guest WiFi with static PSK passwords allows former students, visitors, or terminated staff to retain access. Annual PSK rotation limits exposure from shared passwords. While guest networks should be isolated, credential rotation is a hygiene practice for shared accounts.

**Citations:**
- CIS Controls v8 (Control 12): Wireless credential management
- K-12 Context: Guest WiFi PSK should rotate annually

---

### Category 5: Malware Defense

**Purpose:** Protect against malicious software through layered defensive technologies.

**Questions (4 total, 1 foundational):**

#### 5.1 - Does the organization use a DNS filtering service?

- **Impact:** High (5)
- **Control Description:** Implement and maintain DNS filtering services across the organization to protect against cyber threats. DNS filtering services should actively block access to known malicious domains, phishing sites, and other harmful web content.

**Insurance Rationale:**
DNS filtering provides first-line defense against phishing, malware downloads, and command-and-control (C2) communications. It prevents users from accessing malicious sites even if they click phishing links. DNS filtering also enforces acceptable use policies and blocks inappropriate content in K-12 environments (CIPA compliance). Insurers view DNS filtering as cost-effective preventative control.

**Citations:**
- CIS Controls v8 (Control 9.2): Use DNS filtering services
- CISA CPGs: Protective DNS services block malicious domains
- K-12 Context: DNS filtering supports CIPA compliance for internet filtering

---

#### 5.2 - Does the organization utilize an Email filtering service?

- **Impact:** High (5)
- **Control Description:** Email filtering services should detect and filter spam, phishing attempts, and emails containing malicious attachments or links, safeguarding the organization from email-based threats.

**Insurance Rationale:**
Email remains the #1 attack vector. Phishing emails deliver ransomware, credential theft, and business email compromise (BEC). Email filtering blocks malicious attachments, malicious links, and impersonation attempts. Many K-12 schools use Google Workspace or Microsoft 365 with built-in filtering, but enhanced third-party filtering (Proofpoint, Mimecast) provides additional protection. Insurers assess email filtering as critical preventative control.

**Citations:**
- CIS Controls v8 (Control 9.6): Block unnecessary email file types
- Verizon DBIR (2024): Phishing is leading initial access vector
- Cyber insurance applications ask about email security controls

---

#### 5.3 - Does the organization utilize an Anti-Malware service?

- **Impact:** High (5)
- **Control Description:** Deploy and maintain robust anti-malware solutions on all enterprise assets to protect against viruses, ransomware, spyware, and other malicious software. This can include traditional antivirus software like McAfee or Windows Defender, as well as more advanced Endpoint Protection Platforms (EPP).

**Insurance Rationale:**
Anti-malware is a baseline security control, though traditional antivirus is insufficient for modern threats. Signature-based AV detects known malware but misses zero-day threats and sophisticated attacks. Insurers require anti-malware deployment but increasingly expect next-generation EPP or EDR (see 5.4). Anti-malware demonstrates basic security hygiene.

**Citations:**
- CIS Controls v8 (Control 10.1): Deploy anti-malware software
- Cyber insurance baseline requirements include anti-malware deployment
- K-12 Context: Anti-malware on all student and staff devices

---

#### 🔑 5.4 - FOUNDATIONAL - Has the organization adopted and implemented endpoint detection and response (EDR) software services?

- **Impact:** High (5)
- **Control Description:** Implement an Endpoint Detection and Response (EDR) solution across all enterprise assets to detect, investigate, and respond to advanced threats in real time. EDR tools provide capabilities like threat detection, behavioral analysis, and automated remediation.
- **Trust Requirement:** Endpoint Detection and Response (EDR)

**Insurance Rationale (FOUNDATIONAL):**
EDR is now a universal cyber insurance requirement for 2024-2025 policies. **Traditional antivirus no longer qualifies**—insurers require EDR tools like CrowdStrike, SentinelOne, or Microsoft Defender for Endpoint. EDR provides real-time threat detection, behavioral analysis, and automated response that signature-based AV cannot match. EDR detects ransomware execution, fileless malware, and sophisticated attacks. Many insurers will decline coverage without EDR, and others charge premium increases. EDR is a core insurance requirement for 2024-2025 policies.

**Citations:**
- **Aldridge (2025):** "Traditional antivirus doesn't qualify—insurers require EDR like CrowdStrike, SentinelOne, Microsoft Defender"
  - URL: https://aldridge.com/5-requirements-to-get-cyber-insurance/
- **MoneyGeek (2025):** "EDR is mandatory for 2025 cyber insurance policies"
  - URL: https://www.moneygeek.com/insurance/business/cyber-insurance/requirements/
- **Upward Technology (2024):** "EDR/XDR is top security control recommended by cyber insurers"
  - URL: https://www.upward-technology.com/10-security-controls-recommended-by-cyber-insurers/
- **Atlantic Digital (2024):** "EDR is non-negotiable for cyber insurance in 2024"
  - URL: https://www.adiit.com/cyber-insurance-key-requirements-and-industry-insights/
- **CIS Controls v8 (Control 10.7):** Enable EDR capabilities

---

### Category 6: Data Recovery

**Purpose:** Ensure business continuity through comprehensive backup and recovery capabilities.

**Questions (4 total, 2 foundational):**

#### 6.1 - Does the organization perform backups of critical data/systems?

- **Impact:** High (5)
- **Control Description:** Organizations should implement and maintain a comprehensive data backup strategy to ensure critical data and systems are protected and recoverable in case of cyber incidents, hardware failures, or other disruptions.

**Insurance Rationale:**
Data backups are essential for ransomware recovery and business continuity. Organizations without backups are forced to pay ransoms or face permanent data loss. Insurers assess backup strategy comprehensiveness, including what is backed up, frequency, retention, and testing. Backups reduce claim severity by enabling recovery without ransom payment. However, backups must be protected (see 6.3) as attackers increasingly target backup systems.

**Citations:**
- CIS Controls v8 (Control 11.1): Establish and maintain data recovery capability
- NIST Cybersecurity Framework 2.0 (RC.CO-3: Recovery activities are communicated)
- Cyber insurance policies often require evidence of backup capability

---

#### 6.2 - How often does the organization perform backups?

- **Impact:** Moderate (3)
- **Control Description:** Perform regular backups of critical data/systems to minimize potential data loss, aligning the frequency with the importance and usage of the data.

**Insurance Rationale:**
Backup frequency determines recovery point objective (RPO) and acceptable data loss. Daily backups are standard for critical systems, with hourly or continuous replication for high-value data. Infrequent backups increase data loss in ransomware incidents. K-12 schools with student information systems need daily backups during school year. Insurers may ask about backup schedules during underwriting.

**Citations:**
- CIS Controls v8 (Control 11.2): Perform automated backups
- NIST guidelines recommend backup frequency aligned with data criticality
- K-12 Context: Student data systems require daily backup during school year

---

#### 🔑 6.3 - FOUNDATIONAL - Does the organization have an air gap or immutable backup of critical data/systems?

- **Impact:** High (5)
- **Control Description:** Maintain air-gapped and/or immutable backups to safeguard against ransomware attacks and unauthorized access. Air-gapped backups are physically isolated from the network, while immutable backups are designed to prevent alteration or deletion.
- **Trust Requirement:** Air-gapped/immutable backups

**Insurance Rationale (FOUNDATIONAL):**
Air-gapped or immutable backups are now a universal cyber insurance requirement and a core control for 2024-2025 policies. **Insurers require backups to be encrypted and stored in isolated environments** to prevent ransomware encryption or deletion. Modern ransomware specifically targets backup systems before encrypting production data. Network-attached backups without air-gapping or immutability are insufficient. Many 2024-2025 policies mandate offline/immutable backups with regular testing. This is a critical underwriting factor.

**Citations:**
- **MoneyGeek (2025):** "Backups need to be encrypted and stored in air-gapped environments"
  - URL: https://www.moneygeek.com/insurance/business/cyber-insurance/requirements/
- **Aldridge (2025):** "Air-gapped or immutable backups are mandatory for cyber insurance"
  - URL: https://aldridge.com/5-requirements-to-get-cyber-insurance/
- **Cyber Insurance Academy (2025):** "Isolated, tamper-proof backup systems tested regularly are required"
  - URL: https://www.cyberinsuranceacademy.com/blog/guides/cyber-insurance-minimum-requirements/
- **Upward Technology (2024):** Encrypted offline backups are top 10 control for insurers
  - URL: https://www.upward-technology.com/10-security-controls-recommended-by-cyber-insurers/
- **CIS Controls v8 (Control 11.3):** Protect recovery data
- **K-12 Context:** Schools need air-gapped backups for student information systems

---

#### 🔑 6.4 - FOUNDATIONAL - Does the organization perform bi-annual checks of the backups including testing and validation of recoverability capability?

- **Impact:** High (5)
- **Control Description:** Conduct bi-annual testing and validation of backups to ensure recoverability.
- **Trust Requirement:** Backup testing frequency

**Insurance Rationale (FOUNDATIONAL):**
Backup testing is a critical insurance requirement—untested backups are worthless if corrupted or incomplete. Many organizations discover backup failures during ransomware incidents, forcing ransom payment. **Insurers require at least annual backup testing, with bi-annual or quarterly testing preferred.** Testing validates that backup systems work and recovery procedures are documented. K-12 schools should test backups during summer when student systems are less critical.

**Citations:**
- **Cyber Insurance Academy (2025):** "Backups must be tested regularly for recovery"
  - URL: https://www.cyberinsuranceacademy.com/blog/guides/cyber-insurance-minimum-requirements/
- **Centre Technologies (2025):** Insurance carriers require backup testing verification
  - URL: https://blog.centretechnologies.com/how-to-meet-cyber-insurance-requirements-in-2025
- **CIS Controls v8 (Control 11.5):** Test data recovery
- **NIST Cybersecurity Framework 2.0 (RC.CO-4):** Recovery capability is tested
- **K-12 Context:** Test student information system backups during summer break

---

### Category 7: Security Awareness

**Purpose:** Build human firewall through education and training to recognize and respond to threats.

**Questions (3 total, 2 foundational):**

#### 7.1 - Does the organization have a security awareness program?

- **Impact:** Moderate (3)
- **Control Description:** Establish and maintain a comprehensive security awareness program to educate the workforce on recognizing, preventing, and responding to cybersecurity threats.

**Insurance Rationale:**
Security awareness training addresses the human element, which is the weakest link in cybersecurity. Training reduces phishing click rates, improves password hygiene, and promotes security culture. Insurers view security awareness as preventative control. Many policies require annual training for all employees. Training effectiveness is measured through phishing simulations (see 7.2).

**Citations:**
- CIS Controls v8 (Control 14.1): Establish security awareness program
- FERPA and CISA guidance emphasize training personnel on security practices
- Cyber insurance applications ask about security awareness programs

---

#### 🔑 7.2 - FOUNDATIONAL - Does the organization conduct phishing simulation tests and training at least quarterly?

- **Impact:** Moderate (3)
- **Control Description:** This program should include regular phishing simulation tests conducted at least quarterly, and follow-up training sessions to address identified gaps or emerging risks.
- **Trust Requirement:** Phishing testing

**Insurance Rationale (FOUNDATIONAL):**
Phishing simulations are now a common cyber insurance requirement for 2024-2025 policies. **Insurers require quarterly phishing tests with follow-up training.** Simulations measure training effectiveness and identify high-risk users for targeted training. Phishing remains the #1 initial access vector, making simulation testing a high-value control. Insurers view regular testing as evidence of security culture maturity. K-12 staff (teachers, administrators, support staff) need ongoing phishing training due to volume of email threats.

**Citations:**
- **MoneyGeek (2025):** "Most policies require security awareness training and phishing testing"
  - URL: https://www.moneygeek.com/insurance/business/cyber-insurance/requirements/
- **CybelAngel (2025):** "Implement security awareness training and testing program"
  - URL: https://cybelangel.com/cyber-insurance-requirements/
- **Atlantic Digital (2024):** "Training employees on phishing and cyber risks is required"
  - URL: https://www.adiit.com/cyber-insurance-key-requirements-and-industry-insights/
- **CIS Controls v8 (Control 14.2):** Train workforce on recognizing social engineering
- **K-12 Context:** Teachers are high-value phishing targets with access to student data

---

#### 🔑 7.3 - FOUNDATIONAL - Does the organization offer follow-up security training?

- **Impact:** Low (1)
- **Control Description:** Security Awareness Training should be conducted during onboarding and reinforced through ongoing or event-driven sessions to ensure sustained awareness and readiness.
- **Trust Requirement:** Security awareness training

**Insurance Rationale (FOUNDATIONAL):**
Ongoing security training ensures sustained awareness beyond annual compliance training. Event-driven training (after incidents, new threat campaigns, policy changes) keeps security top-of-mind. **Insurers increasingly require continuous training programs**, not just annual checkbox exercises. Follow-up training for phishing simulation failures provides targeted remediation. K-12 schools with high staff turnover need robust onboarding and ongoing training.

**Citations:**
- **CybelAngel (2025):** "Security awareness training must be ongoing, not one-time"
  - URL: https://cybelangel.com/cyber-insurance-requirements/
- **CIS Controls v8 (Control 14):** Continuous security awareness training
- **K-12 Context:** Teacher onboarding should include security training (CDT Report)
- **FERPA compliance best practices:** Staff accessing student records should receive ongoing privacy and security training to ensure reasonable safeguards

---

### Category 8: Vendor Management

**Purpose:** Manage third-party risk through vendor vetting, monitoring, and financial controls.

**Questions (5 total):**

#### 8.1 - Does the organization have a process for vetting their vendors?

- **Impact:** Moderate (3)
- **Control Description:** Establish a vendor management process that includes vetting vendors through certifications like SOC 2 or ISO 27001, reviewing security policies, assessing data sharing practices, and aligning service level agreements with organizational needs.

**Insurance Rationale:**
Third-party vendors with access to systems or data create supply chain risk. Vendor breaches can expose organizational data (e.g., through ed-tech platforms with student data). Insurers assess vendor risk management, as many breaches originate from vendor compromises. K-12 schools use hundreds of ed-tech vendors, amplifying third-party risk. Vendor security assessments (SOC 2, security questionnaires) demonstrate due diligence.

**Citations:**
- CIS Controls v8 (Control 15): Service provider management
- FERPA: Schools must ensure vendors protect student data through written agreements
- K-12 Context: Schools use hundreds of ed-tech tools requiring vendor vetting (CDT Report)

---

#### 8.2 - Does the organization keep an inventory of their vendors?

- **Impact:** Low (1)
- **Control Description:** Establish and maintain an inventory of vendors who hold sensitive data or are responsible for critical IT platforms or processes.

**Insurance Rationale:**
Vendor inventory enables risk assessment and incident response. Organizations must know which vendors have data access to assess breach notification obligations. Vendor inventories support contract management and security review scheduling. Insurers may ask about vendor inventory during underwriting.

**Citations:**
- CIS Controls v8 (Control 15.1): Establish vendor inventory
- FERPA: Schools must know which vendors process student data
- Cyber insurance applications ask about third-party risk management

---

#### 8.3 - Does the organization verify vendor/supplier bank accounts before adding their accounts to payable systems?

- **Impact:** Moderate (3)
- **Control Description:** Verify bank accounts, authenticate transfer requests, and prevent unauthorized wire transfers, ensuring compliance with industry regulations.

**Insurance Rationale:**
Business email compromise (BEC) attacks frequently target accounts payable processes. Attackers impersonate vendors and provide fraudulent bank account changes. Verifying bank accounts through out-of-band communication (phone call to known number) prevents wire fraud. Cyber insurance policies often exclude or limit BEC coverage, making prevention critical.

**Citations:**
- FBI IC3 Report: BEC remains top cybercrime by financial loss
- Cyber insurance policies may have sub-limits for funds transfer fraud
- K-12 Context: Schools face BEC attacks targeting finance departments

---

#### 8.4 - Does the organization authenticate funds transfer requests (e.g., by calling vendor/customer to verify request at a predetermined phone number)?

- **Impact:** Moderate (3)
- **Control Description:** Authenticate funds transfer requests to prevent unauthorized wire transfers and ensure compliance with industry regulations.

**Insurance Rationale:**
Out-of-band verification (phone call to known number) prevents BEC fraud where attackers impersonate executives or vendors via email. Dual authorization and verification procedures are best practices for wire transfers. Many cyber insurance policies require attestation of funds transfer controls during underwriting.

**Citations:**
- FBI guidance: Verify payment requests through secondary communication channel
- Cyber insurance applications ask about wire transfer controls
- K-12 Context: Schools are targeted by superintendent impersonation emails requesting wire transfers

---

#### 8.5 - Does the organization prevent unauthorized employees from initiating wire transfers?

- **Impact:** Moderate (3)
- **Control Description:** Prevent unauthorized employees from initiating wire transfers, ensuring compliance with industry regulations and protecting against fraud.

**Insurance Rationale:**
Dual authorization and segregation of duties prevent insider fraud and BEC attacks. Limiting wire transfer initiation to specific roles reduces attack surface. Many BEC attacks succeed due to lack of authorization controls in finance departments.

**Citations:**
- CIS Controls v8 (Control 5): Account management includes restricting critical functions
- Cyber insurance policies assess financial controls during underwriting
- K-12 Context: School finance departments need dual authorization for wire transfers

---

### Category 9: Incident Response Management

**Purpose:** Prepare for and respond to security incidents through planning, coordination, and testing.

**Questions (6 total):**

#### 9.1 - Does the organization have a Cyber Incident Response Plan (CIRP)?

- **Impact:** Moderate (3)
- **Control Description:** Establish and maintain an enterprise process for the workforce to report security incidents. The process includes reporting timeframe, personnel to report to, mechanism for reporting, and the minimum information to be reported.

**Insurance Rationale:**
Incident Response Plans (IRPs) are a universal cyber insurance requirement and a core control for 2024-2025 policies. **All cyber insurance policies require documented incident response plans.** IRPs reduce breach impact by ensuring coordinated response, evidence preservation, and timely notification. Insurers provide breach response resources (forensics, legal counsel) but require organizations to have plans. K-12 schools need IRPs covering data breaches, ransomware, and student data compromise.

**Citations:**
- **Aldridge (2025):** "Incident response plan is one of four essential requirements"
  - URL: https://aldridge.com/5-requirements-to-get-cyber-insurance/
- **MoneyGeek (2025):** "Incident response plan is required for cyber insurance"
  - URL: https://www.moneygeek.com/insurance/business/cyber-insurance/requirements/
- **CIS Controls v8 (Control 17):** Establish incident response program
- **NIST Cybersecurity Framework 2.0 (RS.CO):** Communication during response
- **FERPA:** Schools must notify parents of improper disclosure or access to student education records (34 CFR § 99.31-99.34)

---

#### 9.2 - Does the organization outline clear responsibilities in the CIRP?

- **Impact:** Moderate (3)
- **Control Description:** Ensure the incident response plan includes clear responsibilities for all team members.

**Insurance Rationale:**
Clear roles and responsibilities prevent confusion during incidents. IRPs should designate incident commander, technical responders, legal counsel contact, communications lead, and management notification chain. Insurers assess whether organizations have defined response teams. K-12 schools need to define roles for IT staff, superintendent, board notification, and parent communication.

**Citations:**
- CIS Controls v8 (Control 17.3): Establish incident response team
- NIST SP 800-61r2: Incident response roles and responsibilities
- K-12 Context: Schools need defined roles for student data breach response

---

#### 9.3 - Has the organization identified a CISO or a cybersecurity contact?

- **Impact:** Low (1)
- **Control Description:** Identify a Chief Information Security Officer (CISO) or cybersecurity contact responsible for coordinating incident response activities.

**Insurance Rationale:**
Designated security leadership ensures accountability and coordination. While K-12 schools may lack dedicated CISOs, they should designate a security coordinator (IT director, technology coordinator). Insurers need a primary contact for security incidents and policy administration.

**Citations:**
- CIS Controls v8 (Control 17): Designate incident response leadership
- Cyber insurance policies require designated security contact

---

#### 9.4 - Does the organization have a communication plan and contact information in the CIRP?

- **Impact:** Low (1)
- **Control Description:** Include a communication plan and contact information in the Cyber Incident Response Plan to ensure effective coordination during incidents.

**Insurance Rationale:**
Communication plans ensure timely notifications to insurers, law enforcement, regulators, and affected individuals. FERPA compliance requires schools to notify parents when student education records are improperly disclosed or accessed. IRPs should include contact information for cyber insurance carrier, breach coach attorney, forensics provider, and crisis communications. Timely insurer notification is required by policy terms.

**Citations:**
- NIST SP 800-61r2: Incident communication procedures
- FERPA: Schools must notify parents of improper disclosure or access to student education records (34 CFR § 99.31-99.34)
- Cyber insurance policies require timely incident notification (24-48 hours)

---

#### 9.5 - Does the organization perform periodic exercises such as tabletops to test the plan with the CIRP team members?

- **Impact:** Moderate (3)
- **Control Description:** Perform periodic exercises such as tabletops to test the Cyber Incident Response Plan with team members and ensure readiness.

**Insurance Rationale:**
IRP testing validates that plans work and responders understand their roles. Tabletop exercises identify gaps in procedures, communication channels, and decision-making. Insurers increasingly ask about IRP testing during underwriting. Annual tabletop exercises are best practice. K-12 schools should include superintendent, IT, legal counsel, and communications in tabletops.

**Citations:**
- CIS Controls v8 (Control 17.7): Conduct routine incident response exercises
- NIST SP 800-61r2: Test incident response procedures
- Cyber insurance underwriting assesses IRP testing practices

---

#### 9.6 - Outside of the CBS Pool, does the organization purchase cyber insurance?

- **Impact:** Low (1)
- **Control Description:** Consider purchasing cyber insurance to provide financial protection and support in the event of a cybersecurity incident.
- **Note:** Not included in foundational questions

**Insurance Rationale:**
Cyber insurance provides financial protection for breach costs (forensics, legal counsel, notification, credit monitoring, regulatory fines, lawsuits, business interruption). **K-12 schools are strongly encouraged to enroll in cyber liability insurance** due to ransomware attacks targeting education. CBS Pool members benefit from group cyber insurance, but schools should verify coverage limits and exclusions. Standalone cyber policies may provide higher limits or broader coverage.

**Citations:**
- **CDT K-12 Report:** "K-12 schools are strongly encouraged to enroll in cyber liability insurance"
  - URL: https://cdt.org/insights/policies-people-and-protective-measures-legal-requirements-for-k-12-cybersecurity/
- **Route Fifty (2024):** State and local entities adjusting to shifting cyber insurance requirements
  - URL: https://www.route-fifty.com/cybersecurity/2024/11/state-and-local-security-adjusting-shifting-cyber-threats-insurance-requirements/400829/
- Insurance Information Institute: Cyber insurance adoption growing in education sector
- K-12 Context: Schools face ransomware attacks, requiring cyber insurance coverage

---

## The 12 Foundational Questions (Tier I Assessment)

These questions map to The Trust's 7 simplified cyber requirements and form the basis of the Foundation Score. All 12 questions are **mandatory for cyber insurance qualification** and represent the core insurance requirements for 2024-2025 policies.

### The Trust's 7 Requirements → 12 CyberPools Questions

| Trust Requirement | CyberPools Questions | Category | Insurance Criticality |
|-------------------|---------------------|----------|----------------------|
| **1. End-of-Life Software** | 1.4 - EOL software management | Inventory & Assets | **CRITICAL** - Insurers decline coverage for EOL systems |
| **2. Multi-Factor Authentication** | 2.3 - MFA for cloud resources<br>2.4 - MFA for remote access<br>2.5 - MFA for admin accounts<br>2.6 - MFA for critical systems | Account Management | **CRITICAL** - Most ransomware starts with compromised VPNs/credentials; mandatory for 2025 policies |
| **3. Patch Management** | 4.3 - Patch management process (30/7 days) | Secure Configuration | **CRITICAL** - Timely critical/zero-day patching; routine patches within 30 days |
| **4. Vulnerability Scanning** | 4.7 - External vulnerability scans (quarterly) | Secure Configuration | **HIGH** - Quarterly scans required by most policies |
| **5. Endpoint Detection & Response** | 5.4 - EDR implementation | Malware Defense | **CRITICAL** - Traditional AV insufficient; EDR mandatory |
| **6. Air-Gapped Backups** | 6.3 - Air-gapped/immutable backups | Data Recovery | **CRITICAL** - Core requirement; ransomware protection |
| **7. Backup Testing** | 6.4 - Bi-annual backup testing | Data Recovery | **HIGH** - Untested backups = worthless insurance |
| *(Additional Trust Requirements)* | 7.2 - Phishing testing (quarterly)<br>7.3 - Security awareness training | Security Awareness | **HIGH** - Required by most 2025 policies |

### Core Insurance Requirements (2024-2025)

The cyber insurance industry universally requires these foundational controls for 2024-2025 policies:

1. **Multi-Factor Authentication (MFA)** - Questions 2.3-2.6
2. **Endpoint Detection and Response (EDR)** - Question 5.4
3. **Encrypted/Air-Gapped Backups** - Question 6.3
4. **Incident Response Plan** - Question 9.1
5. **Patch Management** - Question 4.3
6. **Vulnerability Scanning** - Question 4.7
7. **Security Awareness Training** - Questions 7.2-7.3
8. **End-of-Life Software Management** - Question 1.4

**All 12 foundational questions address these core insurance requirements—the minimum set of controls expected for 2025 cyber insurance qualification.**

**Note:** While The Trust has 7 requirements, CyberPools tracks 12 questions because some requirements (especially MFA) require multiple questions to assess comprehensively across different systems and use cases.

---

## Scoring Methodology

### Foundation Score (Tier I)
- **Questions:** 12 foundational questions only
- **Formula:** Risk-based scoring (Control Rating × Impact Rating)
- **Output:** Percentage (0-100%) with letter grade (A-F)
- **Purpose:** Insurance qualification and premium tier determination
- **Insurance Context:** Foundation Score predicts insurance eligibility—scores below 70% may face coverage denial or significant premium increases

### Comprehensive Score (Tier II)
- **Questions:** All 52 questions
- **Formula:** Risk-based scoring (Control Rating × Impact Rating)
- **Output:** Percentage (0-100%) with letter grade (A-F)
- **Purpose:** Full security maturity assessment
- **Insurance Context:** Comprehensive Score provides overall risk context but does not replace Foundation Score for underwriting decisions

### Risk Scoring Formula (Both Tiers)

```
Risk Score per Question = Control Rating × Impact Rating

Control Rating:
- Fully Implemented = 1 (lowest risk)
- Partially Implemented = 3 (moderate risk)
- Not Implemented = 5 (highest risk)
- Not Applicable = 0 (excluded from scoring)

Impact Rating (per question):
- Low Impact = 1
- Moderate Impact = 3
- High Impact = 5

Risk Levels:
- Low Risk: 0-9
- Moderate Risk: 10-15
- High Risk: 16-25

Overall Score:
Score = (Total Possible Risk - Actual Risk) / Total Possible Risk × 100%
```

---

## Framework Alignment

### NIST Cybersecurity Framework 2.0 (February 2024)
- **Govern:** Categories 8, 9 (Vendor Management, Incident Response)
- **Identify:** Categories 1, 3 (Asset Inventory, Data Protection)
- **Protect:** Categories 2, 4, 7 (Account Management, Secure Configuration, Security Awareness)
- **Detect:** Categories 4, 5 (Vulnerability Scanning, Malware Defense)
- **Respond:** Category 9 (Incident Response Management)
- **Recover:** Category 6 (Data Recovery)

**Insurance Context:** 74% of organizations using security frameworks use NIST CSF. Insurers recognize NIST CSF alignment as evidence of mature security program.

### CIS Controls v8 (May 2021)
- **IG1 (Basic):** Questions 1.1-1.3, 2.1-2.2, 4.2, 5.3, 6.1-6.2, 7.1
- **IG2 (Foundational):** All 12 foundational questions align with IG2 requirements
- **IG3 (Advanced):** Questions 4.5-4.6, 4.9-4.13, 8.1-8.2, 9.3-9.5

**Insurance Context:** CIS Controls v8 is widely adopted by K-12 schools and recognized by insurers. Implementation Group 2 (IG2) aligns with baseline insurance requirements.

### CISA Cybersecurity Performance Goals (CPGs)
- **Account Security:** Questions 2.1-2.9 (especially 2.3-2.6 for MFA, per CPG 2.H - Phishing-Resistant MFA)
- **Device & System Security:** Questions 4.3 (patch management per CPG 1.E), 4.7 (vulnerability management per CPG 1.E)
- **Incident Response:** Questions 9.1-9.5 (per CPG 2.S - Incident Response Plans)
- **Data Security:** Questions 3.3 (encryption per CPG 2.K), 3.4 (data management), 6.3-6.4 (backups per CPG 2.R)

**Insurance Context:** CISA CPGs target organizations with limited resources (including K-12 schools), emphasizing cost-effective high-impact controls.

### FERPA (Family Educational Rights and Privacy Act)

**Important Note:** FERPA (34 CFR Part 99) does not prescribe specific technical security controls. However, FERPA requires schools to use "reasonable methods" to protect student education records. The controls listed below represent industry best practices recommended by the U.S. Department of Education, FTC guidance, and FERPA compliance experts to ensure schools meet their "reasonable security" obligations.

- **Data Inventory:** Question 3.1
- **Data Retention:** Question 3.4 (NEW)
- **Encryption:** Question 3.3
- **Access Controls:** Questions 2.1-2.9 (especially MFA)
- **Security Training:** Questions 7.1-7.3
- **Vendor Management:** Questions 8.1-8.2
- **Breach Notification:** Question 9.4

**Insurance Context:** FERPA compliance reduces regulatory penalties in K-12 data breaches. Cyber insurers assess FERPA compliance as part of education sector underwriting.

---

## Cyber Insurance Market Context (2024-2025)

### Underwriting Tightening
Cyber insurance underwriting has significantly tightened since 2020-2021 due to ransomware losses:
- **Coalition (2025):** Most ransomware attacks start with compromised VPNs and remote access credentials; organizations without MFA face significantly higher claims risk
- **Premium increases:** Organizations without core insurance controls face 30-50% premium increases or coverage denial
- **Coverage restrictions:** Insurers may exclude EOL systems, unprotected backups, or systems without EDR
- **K-12 specific:** Education sector faces heightened scrutiny due to limited IT resources and high ransomware targeting

### Required Application Documentation
Cyber insurance applications now commonly require:
- Network diagrams and asset inventories
- Evidence of MFA deployment across all systems
- EDR tool documentation and deployment metrics
- Vulnerability scan reports (quarterly)
- Backup testing logs
- Incident response plan documentation
- Security awareness training records
- Patch management policies and procedures

### Policy Conditions and Sub-Limits
Modern cyber insurance policies include:
- **Mandatory controls:** MFA, EDR, air-gapped backups, incident response plan
- **Notification requirements:** Report incidents within 24-48 hours
- **Sub-limits:** BEC/funds transfer fraud often has lower limits
- **Exclusions:** EOL systems, acts of war, known vulnerabilities
- **Retroactive coverage:** Pre-existing conditions excluded

---

## Implementation Notes

### For Insurance Underwriters
- **Foundation Score** provides clear view of insurance-critical controls
- **12 foundational questions** align with core insurance requirements for 2024-2025 policies
- **Simple compliance table** shows yes/no status per Trust requirement
- **Comprehensive Score** provides context for overall security maturity
- **Citations support underwriting:** Each question includes insurance rationale with industry data

### For Member Organizations
- **Two-tier reporting** shows both insurance requirements and full security posture
- **Clear prioritization** helps focus remediation on insurance-critical gaps first (Foundation Score)
- **Framework alignment** supports grant applications and compliance requirements (NIST, CIS, CISA, FERPA)
- **Detailed findings** provide actionable remediation guidance with insurance justification
- **Insurance renewal support:** Assessment provides documentation for insurance applications

### For CyberPools Team
- **Maintains single assessment** (no duplicate work)
- **Same 52 questions** as current process (added data retention question)
- **Automated scoring** via existing transform scripts
- **Flexible reporting** can show Foundation only, Comprehensive only, or both
- **Insurance market alignment:** Assessment directly addresses 2024-2025 cyber insurance requirements

---

## Related Documents

- **CEO Executive Brief:** `CEO_EXECUTIVE_BRIEF_2026_ASSESSMENT_STRATEGY.md`
- **Grading Model Options:** `ACTUAL_GRADING_OPTIONS.md`
- **Insurance Research:** `INSURANCE_STRATEGIC_ASSESSMENT_EXECUTIVE_SUMMARY.md`
- **POC Implementation:** `../POC_DUAL_SCORE_README.md`

---

## Citations and References

### Cyber Insurance Industry Reports

- **Coalition Cyber Threat Index (2024 & 2025)**
  - 2024 Report: https://info.coalitioninc.com/download-cyber-threat-index-2024-b.html
  - 2025 Report: https://www.coalitioninc.com/announcements/cyber-threat-index-2025
  - Claims Report 2025: https://www.coalitioninc.com/announcements/2025-cyber-claims-report
  - Key Finding: Most ransomware attacks start with compromised VPNs and remote access credentials

- **Aldridge (2025): "5 Requirements to Get Cyber Insurance in 2025"**
  - URL: https://aldridge.com/5-requirements-to-get-cyber-insurance/
  - Key Topics: MFA, EDR, backups, vulnerability management, security training

- **MoneyGeek (2025): "Cyber Insurance Requirements (2025 Guide)"**
  - URL: https://www.moneygeek.com/insurance/business/cyber-insurance/requirements/
  - Key Topics: Password requirements, patch management, vulnerability scanning, MFA

- **Woodruff Sawyer (2024): "Cyber Insurance Requirements: The Next Frontier"**
  - URL: https://woodruffsawyer.com/insights/cyber-insurance-requirements-next-frontier
  - Additional: "2024 Guide to Cyber Liability Insurance"
  - URL: https://woodruffsawyer.com/insights/cyber-liability-insurance-buying-guide
  - Additional: "Cyber Insurance in 2025: What to Expect"
  - URL: https://woodruffsawyer.com/insights/cyber-looking-ahead-guide

- **Cyber Insurance Academy (2025): "Minimum Requirements in Cyber Insurance"**
  - URL: https://www.cyberinsuranceacademy.com/blog/guides/cyber-insurance-minimum-requirements/
  - Key Topics: EOL systems, backup testing, MFA scope verification

- **Upward Technology (2024): "10 Security Controls Recommended By Cyber Insurers"**
  - URL: https://www.upward-technology.com/10-security-controls-recommended-by-cyber-insurers/
  - Updated: November 2024
  - Key Topics: EDR, patch management, EOL systems, vulnerability scanning

- **Centre Technologies (2025): "How to Meet Cyber Insurance Requirements in 2025"**
  - URL: https://blog.centretechnologies.com/how-to-meet-cyber-insurance-requirements-in-2025
  - Free Resource: Cyber Insurance Coverage Requirements Matrix
  - URL: https://info.centretechnologies.com/cyber-insurance-coverage-requirements-matrix

- **CybelAngel (2025): "Navigating Cyber Insurance Requirements [2025 Guide]"**
  - URL: https://cybelangel.com/cyber-insurance-requirements/
  - Key Topics: MFA for VPN, vulnerability scanning, security training

- **Atlantic Digital (2024): "Cyber Insurance in 2024—Key Requirements and Industry Insights"**
  - URL: https://www.adiit.com/cyber-insurance-key-requirements-and-industry-insights/
  - Key Topics: EDR/XDR requirements, employee training, phishing protections

### Cybersecurity Frameworks

- **NIST Cybersecurity Framework 2.0 (February 2024)**
  - Official Page: https://www.nist.gov/cyberframework
  - Full Document: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1300.pdf
  - Announcement: https://www.nist.gov/news-events/news/2024/02/nist-releases-version-20-landmark-cybersecurity-framework
  - Release Date: February 26, 2024
  - Key Update: Added "Govern" as sixth core function

- **CIS Controls v8 (May 2021)**
  - Navigator: https://www.cisecurity.org/controls/cis-controls-navigator
  - Assessment Specification: https://cas.docs.cisecurity.org/en/latest/
  - Current Version: v8.1
  - Implementation Groups: IG1 (Basic), IG2 (Foundational), IG3 (Advanced)

- **CISA Cybersecurity Performance Goals (CPGs)**
  - Official Page: https://www.cisa.gov/cybersecurity-performance-goals-cpgs
  - Full Report v1.0.1 (March 2023): https://www.cisa.gov/sites/default/files/2023-03/CISA_CPG_REPORT_v1.0.1_FINAL.pdf
  - Controls List: https://www.cisa.gov/sites/default/files/publications/Common_Baseline_v2_Controls_List_508c.pdf
  - Initial Release: October 2022

- **NIST Special Publication 800-63B: "Digital Identity Guidelines"**
  - URL: https://pages.nist.gov/800-63-3/sp800-63b.html
  - Topic: Password and authentication guidelines

- **NIST Special Publication 800-61r2: "Computer Security Incident Handling Guide"**
  - URL: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf
  - Revision 2: August 2012
  - Topic: Incident response procedures

### K-12 Cybersecurity and FERPA

- **Protecting Student Privacy (ED.gov, U.S. Department of Education)**
  - Main Portal: https://studentprivacy.ed.gov/
  - FERPA Information: https://studentprivacy.ed.gov/ferpa
  - Data Retention Training: https://studentprivacy.ed.gov/training/data-retention-and-data-destruction
  - Best Practices for Data Destruction (2019): https://studentprivacy.ed.gov/sites/default/files/resource_document/file/Best%20Practices%20for%20Data%20Destruction%20(2019-3-26).pdf

- **Kiteworks FERPA Compliance Guides (2024)**
  - Main Guide: https://www.kiteworks.com/regulatory-compliance/ferpa-compliance/
  - Best Practices: https://www.kiteworks.com/regulatory-compliance/ferpa-compliance-best-practices/
  - In-Depth Guide: https://www.kiteworks.com/regulatory-compliance/mastering-ferpa-compliance-an-in-depth-guide-for-enterprises/
  - MFT for FERPA: https://www.kiteworks.com/managed-file-transfer/mft-for-ferpa-compliance/
  - Last Updated: August 2024

- **Center for Democracy and Technology (CDT)**
  - K-12 Cybersecurity Legal Requirements: https://cdt.org/insights/policies-people-and-protective-measures-legal-requirements-for-k-12-cybersecurity/
  - Student Privacy Research: https://cdt.org/insights/cdt-original-research-examines-privacy-implications-of-school-issued-devices-and-student-activity-monitoring-software/
  - FTC COPPA Enforcement: https://cdt.org/insights/ftc-to-prioritize-cybersecurity-and-data-minimization-enforcement-under-coppa-to-bolster-student-privacy/

- **Duo Security (2024)**
  - K-12 Solutions: https://duo.com/solutions/k-12
  - K-12 Cybersecurity Compliance Blog: https://duo.com/blog/breaking-down-learning-curve-in-k-12-cybersecurity-compliance
  - 2024 Trusted Access Report: https://duo.com/resources/ebooks/2024-duo-trusted-access-report

### Threat Intelligence

- **Verizon Data Breach Investigations Report (DBIR) 2024**
  - Main Report: https://www.verizon.com/business/resources/reports/dbir/
  - Executive Summary: https://www.verizon.com/business/resources/reports/2024-dbir-executive-summary.pdf
  - Full Report PDF: https://www.verizon.com/business/resources/Te3/reports/2024-dbir-data-breach-investigations-report.pdf
  - Scope: 10,626 confirmed breaches analyzed

- **Microsoft Security Reports**
  - MFA Effectiveness (2019): https://www.microsoft.com/en-us/security/blog/2019/08/20/one-simple-action-you-can-take-to-prevent-99-9-percent-of-account-attacks/
  - Mandatory MFA Planning (2024): https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication
  - Key Stat: MFA blocks 99.9% of automated attacks (2019) | 99.2% (2024 update)

- **FBI Internet Crime Complaint Center (IC3)**
  - Main Site: https://www.ic3.gov/
  - BEC Information: https://www.ic3.gov/CrimeInfo/BEC
  - BEC: The $55 Billion Scam (2024): https://www.ic3.gov/PSA/2024/PSA240911
  - 2023 Data: 21,442 BEC complaints, $2.8 billion in losses

- **CISA Known Exploited Vulnerabilities (KEV) Catalog**
  - URL: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  - Purpose: Authoritative list of actively exploited CVEs

### Additional Resources

- **Route Fifty (2024): "State and local security adjusting to shifting cyber threats, insurance requirements"**
  - URL: https://www.route-fifty.com/cybersecurity/2024/11/state-and-local-security-adjusting-shifting-cyber-threats-insurance-requirements/400829/
  - Published: November 2024

- **Insurance Information Institute**
  - Website: https://www.iii.org/
  - Topic: Cyber insurance market trends and adoption statistics

---

**Last Updated:** October 30, 2025
**Last Citation Verification:** October 30, 2025
**Status:** Recommended approach for January 1, 2026 launch
**Total Questions:** 52 (added data retention question to Category 3)
**Foundational Questions:** 12 (unchanged—map to The Trust's 7 requirements)

**Citation Verification Note:** All citations have been verified and updated with hyperlinks. See `/poc-research/docs/CITATION_VERIFICATION_REPORT.md` for detailed verification report. Key corrections made:
- Coalition 82% MFA statistic replaced with verified finding: most ransomware starts with compromised VPNs/remote access
- CyberAngel corrected to CybelAngel
- Microsoft MFA statistic date corrected from 2024 to 2019
- All major sources now include direct URLs for verification
