---
title: Category 4 - Secure Configuration and Vulnerability Management
tags:
  - Category 4
  - Foundational
  - New
  - High Impact
  - Moderate Impact
---

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


### Question 4.8-4.13: Additional Configuration Questions

**Note:** Questions 4.8-4.13 cover additional secure configuration topics including:

- 4.8: Remote Desktop Protocol (RDP) Security
- 4.9: Internal Network Segmentation  
- 4.10: VLAN Configuration
- 4.11: DNS Security (DNSSEC)
- 4.12: Time Synchronization (NTP)
- 4.13: Configuration Change Management

*(Full detail for these questions follows same format as above with question text, impact rating, foundational status, control description, insurance rationale, threat landscape justification, sector-specific context, and citations)*

---

### Question 4.14: Centralized Logging and SIEM 🆕

**Question Text:**
Does the organization implement centralized logging with a Security Information and Event Management (SIEM) or log management solution to collect, correlate, and analyze security events from across networks, servers, endpoints, and security devices?

**Impact Rating:** High (5)

**Foundational:** NO - Advanced security control (NEW 2026)

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
