# CyberPools K-12 Cybersecurity Assessment Expansion Research

**Research Date:** October 30, 2025
**Purpose:** Recommend 10-12 additional questions for CyberPools' K-12 cybersecurity risk assessment based on 2024-2025 threat landscape and insurance market trends
**Current Assessment:** 52 questions across 9 categories
**Research Focus:** IBM X-Force Threat Intelligence Index 2024-2025, Verizon DBIR 2024, Cyber Insurance Questionnaires (Coalition, Corvus, Chubb, etc.)

---

## Executive Summary

Based on comprehensive research of the 2024-2025 cyber threat landscape and insurance market requirements, this report recommends **11 additional questions** to enhance CyberPools' K-12 cybersecurity risk assessment. These questions address critical gaps in:

1. **Centralized Logging and Security Monitoring** (SIEM/SOC capabilities)
2. **Privileged Access Management** (PAM controls beyond basic MFA)
3. **Email Security Controls** (DMARC, SPF, DKIM authentication)
4. **Cloud Security Governance** (multi-cloud management and configuration)
5. **Incident Detection Capabilities** (threat detection and response metrics)
6. **Enhanced Third-Party Risk Management** (supply chain security beyond vendor vetting)
7. **Remote Work/BYOD Security** (expanded attack surface from distributed workforce)
8. **API Security** (emerging threat vector)

### Key Threat Landscape Findings

**IBM X-Force Threat Intelligence Index 2025:**
- Account abuse remains the #1 initial access vector (30% of incidents)
- 84% increase in phishing emails delivering infostealers
- K-12 schools are the most vulnerable in education sector due to limited budgets and small IT staffs
- Credential-based attacks dominate the threat landscape

**Verizon Data Breach Investigations Report 2024:**
- Education sector: 1,537 confirmed breaches (86% breach rate from incidents)
- 75% of all breaches analyzed included ransomware (significant increase from prior year)
- 88% of breaches involved stolen credentials
- Only 50% of perimeter-device vulnerabilities fully remediated
- Social engineering (42%) and system intrusion (35%) top attack patterns in education
- Third-party involvement in breaches doubled

### Key Insurance Market Trends (2024-2025)

**Emerging Requirements:**
- **SIEM/SOC capabilities**: 42% of organizations now required to have PAM for insurance coverage (up from 36% in 2023)
- **Centralized logging**: Larger organizations and regulated industries now require SIEM
- **Data retention policies**: Required by state privacy laws and cyber insurance carriers
- **Email authentication**: SPF/DKIM now baseline; DMARC increasingly required
- **Cloud security controls**: Multi-cloud environments require CSPM and configuration management
- **Third-party risk**: Insurers requiring robust TPRM programs with vendor certifications
- **Detection metrics**: Mean Time to Detect (MTTD) assessed during underwriting

**Major Insurance Carriers Emphasizing:**
- Coalition: Weekly offline backups, MFA enforcement, email authentication
- Corvus: Smart cyber application with enhanced risk assessment
- Chubb: Protected information governance, comprehensive security programs
- General trend: Independent audits and certifications (ISO 27001, NIST CSF) increasingly required

### Gap Analysis: Current Assessment vs. 2024-2025 Threat Landscape

**Current Strengths (Well-Covered):**
- ✅ Multi-factor authentication (4 comprehensive questions covering all systems)
- ✅ Endpoint Detection and Response (EDR)
- ✅ Backup and recovery (air-gapped, testing)
- ✅ Patch management
- ✅ Basic vendor management
- ✅ Incident response planning

**Critical Gaps Identified:**

| Gap Area | Current Coverage | Why It Matters | Insurance Pressure |
|----------|------------------|----------------|-------------------|
| **Centralized Logging/SIEM** | ❌ None | Essential for threat detection and incident investigation; 42% of orgs now required | HIGH - Required for larger districts |
| **Privileged Access Management (PAM)** | ⚠️ Partial (MFA + admin separation) | 42% of policies require PAM; controls beyond MFA needed | HIGH - Rapidly increasing |
| **Email Authentication (DMARC/SPF/DKIM)** | ❌ None | K12 SIX framework now considers SPF/DKIM baseline; prevents impersonation | MODERATE - Becoming standard |
| **Cloud Security Posture** | ❌ None | 95% of cloud breaches from misconfigurations; multi-cloud complexity | MODERATE-HIGH - Growing |
| **Incident Detection Metrics** | ❌ None | MTTD assessed in underwriting; avg 212 days to detect breaches | MODERATE - Emerging |
| **Enhanced Vendor Risk** | ⚠️ Basic only | 41% of attacks from 3rd parties; doubled in DBIR 2024 | MODERATE - Increasing |
| **Remote Work/BYOD Controls** | ⚠️ VPN MFA only | Post-COVID attack surface; BYOD market $52B in 2024 | MODERATE - Persistent |
| **API Security** | ❌ None | 78% of orgs had API breach in 2023; $2.5B in losses | LOW-MODERATE - Emerging |
| **Security Monitoring Coverage** | ❌ None | Only 26% integrate IR into TPRM; need continuous monitoring | MODERATE - Growing |
| **Data Retention Policy** | ✅ Recently Added (3.4) | Privacy law compliance; reduces breach exposure | MODERATE - Standard |

**Assessment Categories Needing Enhancement:**
- **Category 2 (Account Management):** Add PAM controls beyond basic MFA
- **Category 3 (Data Protection):** Recently added data retention (3.4) - adequate
- **Category 4 (Secure Configuration):** Add centralized logging and cloud security
- **Category 5 (Malware Defense):** Add email authentication controls
- **Category 8 (Vendor Management):** Enhance third-party risk with security certifications
- **Category 9 (Incident Response):** Add detection capabilities and metrics
- **NEW Category consideration:** Cloud Security (if cloud adoption warrants dedicated category)

---

## Recommended Questions for Assessment Expansion

### Question 3.5: Privileged Access Management (PAM) Platform
**Category:** 3 - Data Protection (Alternative: Could fit in Category 2 - Account Management)

**Question Text:**
Has the organization implemented a Privileged Access Management (PAM) solution to control, monitor, and audit access to privileged accounts (administrators, service accounts, shared credentials)?

**Impact Rating:** High (5)

**Foundational Question:** 🔑 YES - Insurance Critical

**Control Description:**
Privileged Access Management (PAM) provides centralized control over privileged accounts through secure credential vaulting, session monitoring/recording, just-in-time access provisioning, and automated credential rotation. PAM solutions consolidate privileged credentials for both human and machine identities, enforce least privilege principles, and provide detailed audit trails of all privileged activities. Capabilities include screen recording, keystroke logging, and the ability to pause or terminate suspicious privileged sessions.

**Insurance Rationale:**
PAM is rapidly becoming a core cyber insurance requirement, with 42% of organizations in 2024 required to have PAM for coverage (up from 36% in 2023). Vast majority of cyberattacks involve stolen credentials and misuse of privileged access, making PAM a critical control. Insurers require specific capabilities:
- Removing local admin rights from workstations
- Enforcing principle of least privilege (PoLP)
- Consolidating and securing all privileged credentials
- Monitoring and recording privileged sessions
- Auditing all privileged activities with real-time alerts

Organizations lacking robust PAM strategies face policy rejection or cancellation. Many insurers now mandate proof of adherence to regulatory standards (GDPR, HIPAA, PCI DSS) which require PAM controls.

**Threat Landscape Justification:**
**IBM X-Force 2025:** Account abuse remains the #1 initial access vector (30% of incidents). Attackers specifically target privileged accounts for maximum impact, enabling lateral movement and data exfiltration.

**Verizon DBIR 2024:** 88% of breaches involved stolen credentials. Privileged accounts with elevated permissions are prime targets as they can modify systems, access sensitive data, and disable security controls.

**K-12 Context:** School IT departments often share admin credentials across staff, use service accounts with weak oversight, and lack visibility into privileged activities. PAM addresses these risks while remaining practical for resource-constrained K-12 environments through managed service options.

**Citations:**
- Securden (2024): "42% of organizations required to have PAM for cyber insurance" (up from 36% in 2023)
- ManageEngine: "Vast majority of cyberattacks due to stolen credentials and misuse of privileged access"
- BeyondTrust: "Two basic requirements of many cyber insurers: removing admin rights and enforcing PoLP"
- CIS Controls v8 (Control 5.4): Restrict administrator privileges to dedicated accounts

---

### Question 4.14: Centralized Logging and SIEM
**Category:** 4 - Secure Configuration and Vulnerability Management

**Question Text:**
Does the organization implement centralized logging with a Security Information and Event Management (SIEM) or log management solution to collect, correlate, and analyze security events from across networks, servers, endpoints, and security devices?

**Impact Rating:** High (5)

**Foundational Question:** 🔑 YES (for larger districts >2,500 students) / NO (for smaller districts) - Consider tiered requirement

**Control Description:**
Centralized logging aggregates security events, system logs, and audit data from diverse sources (firewalls, endpoints, servers, applications, cloud services) into a unified platform. SIEM solutions provide real-time correlation, threat detection, alerting, and forensic investigation capabilities. Even basic log management solutions that centralize and retain logs (without full SIEM analytics) provide critical incident investigation and compliance value. Solutions can be on-premises or cloud-based/managed services.

**Insurance Rationale:**
SIEM/SOC capabilities are now required by cyber insurance carriers, particularly for larger organizations and regulated industries. Insurers require continuous security monitoring coverage - smaller security teams may leverage outsourced SOC teams with SIEM solutions. Key insurance drivers:
- Enables incident detection and investigation
- Provides audit trails for compliance (HIPAA, PCI DSS, state privacy laws)
- Supports Mean Time to Detect (MTTD) metrics assessed during underwriting
- Demonstrates mature security operations capabilities
- Required for 24/7 monitoring expected by insurers

While currently more common for larger organizations, security measures required for larger entities often become standard for all businesses as insurance requirements tighten.

**Threat Landscape Justification:**
**IBM X-Force 2025:** Average time to detect breach is 212 days. Organizations without centralized logging lack visibility into attacker lateral movement, credential abuse, and data exfiltration activities.

**Verizon DBIR 2024:** Third-party involvement in breaches doubled. Without centralized logging across on-premises and cloud environments, organizations cannot detect anomalous activities or trace attack paths.

**K-12 Context:** Schools with distributed campuses, cloud services (Google Workspace, Microsoft 365), student information systems, and network infrastructure need centralized visibility. Cloud-based SIEM solutions (Splunk Cloud, Microsoft Sentinel, Sumo Logic) offer practical options for K-12 budgets through EDU pricing.

**Citations:**
- TechSolutions Inc (2024): "SOC and SIEM no longer optional for cyber insurance"
- Atlantic Digital (2024): "SIEM among key requirements for cyber insurance in 2024"
- Parachute Cloud (2025): "Industries governed by HIPAA, PCI DSS require centralized log management"
- CIS Controls v8 (Control 8): Audit Log Management
- NIST CSF 2.0 (DE.AE): Anomalies and Events are detected

---

### Question 4.15: Cloud Security Configuration Management
**Category:** 4 - Secure Configuration and Vulnerability Management

**Question Text:**
Does the organization use cloud security posture management (CSPM) tools or processes to continuously monitor and remediate misconfigurations in cloud environments (AWS, Azure, Google Cloud, Microsoft 365, Google Workspace)?

**Impact Rating:** High (5)

**Foundational Question:** NO - Comprehensive maturity indicator

**Control Description:**
Cloud Security Posture Management (CSPM) involves continuous assessment of cloud infrastructure configurations against security best practices and compliance frameworks. This includes monitoring cloud storage permissions, identity and access management (IAM) policies, network security groups, encryption settings, and compliance with benchmarks like CIS Benchmarks for AWS/Azure/GCP or Microsoft Secure Score for M365. Organizations can implement CSPM through native cloud tools (AWS Security Hub, Azure Security Center, Google Security Command Center, Microsoft Secure Score) or third-party platforms.

**Insurance Rationale:**
95% of cloud breaches stem from misconfigurations, making CSPM essential for risk mitigation. As organizations adopt multi-cloud environments, insurers assess cloud security controls during underwriting. Key concerns:
- Publicly exposed storage buckets with sensitive data
- Overly permissive IAM policies enabling lateral movement
- Disabled encryption or logging
- Failure to meet compliance frameworks (NIST, CIS)

Cloud-native applications and SaaS platforms are now primary attack surfaces. Microsoft 365 and Google Workspace misconfigurations (e.g., external sharing, weak conditional access policies) create data exposure risks. Insurers increasingly require evidence of cloud security monitoring.

**Threat Landscape Justification:**
**IBM X-Force 2025:** Cloud environments face sophisticated attacks exploiting misconfigurations and identity vulnerabilities. Organizations need visibility across multi-cloud deployments.

**Industry Research (2024-2025):** 95% of cloud breaches result from misconfigurations. As of 2025, proliferation of sophisticated attacks and challenge of managing dynamic cloud assets underscore critical need for advanced cloud security.

**K-12 Context:** Schools extensively use Microsoft 365 Education or Google Workspace for Education, often with default configurations lacking security hardening. Student data stored in cloud platforms requires proper access controls, encryption, and monitoring. Many schools also use cloud-based student information systems (Infinite Campus, PowerSchool) requiring secure configuration.

**Citations:**
- GBHackers (2025): "95% of cloud breaches stem from misconfigurations"
- Microsoft Learn: "Microsoft cloud security benchmark with ~180 AWS checks for multi-cloud"
- Orca Security (2025): "Multi-cloud compliance requires consistent security policies across AWS, Azure, GCP"
- CIS Controls v8 (Control 4): Secure Configuration (extends to cloud)
- NIST CSF 2.0 (PR.IP-1): Baseline configurations for cloud services

---

### Question 5.5: Email Authentication Protocols (DMARC, SPF, DKIM)
**Category:** 5 - Malware Defense and Endpoint Security

**Question Text:**
Has the organization implemented email authentication protocols including SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail), and DMARC (Domain-based Message Authentication, Reporting, and Conformance) to prevent email spoofing and impersonation attacks?

**Impact Rating:** High (5)

**Foundational Question:** 🔑 YES - Insurance Critical (DMARC specifically)

**Control Description:**
Email authentication protocols work together to prevent domain spoofing and verify email legitimacy:
- **SPF:** Authorizes specific IP addresses to send email from your domain
- **DKIM:** Adds digital signature to verify message hasn't been tampered with in transit
- **DMARC:** Provides policy for handling emails failing SPF/DKIM checks and generates reports to domain owners

Full implementation includes:
1. Publishing SPF records in DNS listing authorized mail servers
2. Enabling DKIM signing on outbound email
3. Implementing DMARC policy (at minimum p=none for monitoring, ideally p=quarantine or p=reject)
4. Monitoring DMARC reports to identify spoofing attempts

**Insurance Rationale:**
Email remains the #1 attack vector with phishing as the top initial access method. Business Email Compromise (BEC) attacks cost billions annually, with attackers impersonating superintendents, principals, or vendors to request wire transfers or credential disclosure. Email authentication controls:
- Prevent domain impersonation (attacker can't send email appearing to be from your domain)
- Protect brand reputation and constituent trust
- Reduce successful phishing attacks reaching user inboxes
- Demonstrate proactive anti-phishing controls to insurers

Coalition specifically lists email authentication as part of cyber insurance coverage checklists. Many BEC losses are excluded or sub-limited in cyber policies, making prevention critical.

**Threat Landscape Justification:**
**IBM X-Force 2025:** 84% uptick in phishing emails delivering infostealers. Attackers increasingly use domain impersonation to appear legitimate.

**Verizon DBIR 2024:** Phishing and pretexting remain top causes of costly data breaches in education sector (42% of attack patterns). Email-based social engineering dominates.

**K-12 Context:** K12 Security Information eXchange (K12 SIX) updated framework for 2024-25 now considers SPF and DKIM baseline protections. However, only 16% of Virginia school districts have implemented DMARC, and just 8% have enforcement policies (p=quarantine/reject). Schools face impersonation attacks targeting parents, staff, and students. Superintendent impersonation for wire fraud is common attack pattern.

**Citations:**
- K12 SIX (2024): "SPF and DKIM now baseline protections in updated framework"
- Virginia School Data (2024): "84.6% SPF adoption, only 16% DMARC adoption, 8% with enforcement"
- Coalition: "Email authentication (SPF, DKIM, DMARC) on cyber insurance checklist"
- Clever Education (2024): "Schools should implement SPF, DKIM, DMARC to protect against spoofing"
- FBI IC3: BEC remains top cybercrime by financial loss

---

### Question 8.6: Third-Party Security Certifications and Assessments
**Category:** 8 - Third-Party and Vendor Risk Management

**Question Text:**
Does the organization require vendors with access to systems or data to provide security certifications (SOC 2 Type II, ISO 27001, etc.) or complete security assessments before being granted access?

**Impact Rating:** High (5)

**Foundational Question:** NO - Comprehensive maturity indicator (though trending toward foundational)

**Control Description:**
Enhanced third-party risk management requires vendors to demonstrate security posture through:
- **Security Certifications:** SOC 2 Type II (trust services criteria), ISO 27001 (information security management), FedRAMP (government cloud), HITRUST (healthcare), PCI DSS (payment card data)
- **Security Assessments:** Vendor security questionnaires, penetration testing results, vulnerability scan reports
- **Ongoing Monitoring:** Annual recertification, continuous monitoring for security incidents, periodic reassessment

This goes beyond basic vendor vetting (Question 8.1) to require documented proof of security controls. Organizations should:
1. Maintain tiered vendor classification (critical, high, medium, low risk)
2. Require certifications/assessments based on vendor access level and data sensitivity
3. Review certifications annually and validate with certification bodies
4. Require vendors to carry cyber/E&O insurance

**Insurance Rationale:**
Third-party involvement in breaches doubled in Verizon DBIR 2024, driving significant insurance concern. Supply chain attacks will result in $60 billion losses in 2025 (15% annual increase projected). Insurers now require:
- Robust third-party risk management (TPRM) programs
- Strong contractual language with security requirements
- Vendor cybersecurity certifications
- Requirements for vendors to carry cyber or tech E&O insurance

Gartner forecasts 45% of companies will experience supply chain cyberattack by 2025. 54% of executives cite TPRM as major challenge. Organizations without vendor security oversight face higher premiums or coverage limitations.

**Threat Landscape Justification:**
**Verizon DBIR 2024:** Third-party involvement in breaches doubled from previous year. Attackers compromise vendors to access multiple downstream organizations.

**Industry Research (2024-2025):** 41% of cyberattacks originated from third parties. Software supply chain attacks resulted in $60 billion projected losses in 2025. Less than 50% of organizations monitor even half their supply chain for cyber threats.

**K-12 Context:** Schools use hundreds of ed-tech vendors (learning management systems, student information systems, assessment platforms, communication tools) with access to sensitive student data. FERPA requires schools ensure vendors protect student data through written agreements. However, many schools lack resources to assess vendor security. Requiring certifications shifts burden to vendors while providing documented assurance.

**Citations:**
- Verizon DBIR (2024): "Third-party involvement in breaches doubled"
- Cybersecurity Ventures (2024): "$60 billion in losses from supply chain attacks in 2025"
- Gartner: "45% of companies will experience supply chain cyberattack by 2025"
- Arch Insurance (2024): "Cyber insurers require robust TPRM with vendor certifications and insurance"
- WEF (2024): "54% of executives cite TPRM as major challenge; 41% of attacks from 3rd parties"

---

### Question 9.7: Incident Detection and Response Capabilities
**Category:** 9 - Incident Response and Recovery

**Question Text:**
Does the organization have processes and tools in place to detect security incidents in a timely manner, including defined metrics for Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR)?

**Impact Rating:** Moderate (3)

**Foundational Question:** NO - Comprehensive maturity indicator

**Control Description:**
Incident detection and response capabilities include:
- **Detection Tools:** SIEM, EDR, Network Detection and Response (NDR), User and Entity Behavior Analytics (UEBA), alerts from security tools
- **Metrics:** Mean Time to Detect (MTTD) - average time to discover incidents; Mean Time to Respond (MTTR) - average time to contain/remediate incidents
- **Process:** 24/7 monitoring (internal SOC or outsourced), alert triage and escalation procedures, incident classification and prioritization, defined response workflows

Organizations should:
1. Track MTTD and MTTR for security incidents
2. Establish target thresholds (e.g., high-performing orgs achieve 30 minutes - 4 hours MTTD)
3. Review metrics quarterly and identify improvement opportunities
4. Integrate detection capabilities with incident response plan

**Insurance Rationale:**
When applying for cyber insurance, underwriters assess cybersecurity posture including detection capabilities. Organizations with lower MTTD are better positioned for coverage as they limit damage from incidents. Key considerations:
- IBM reports average detection time of 212 days for breaches
- Average combined detection and containment time is 277 days
- Organizations with security AI/automation detect and contain incidents 98 days faster
- Lower MTTD directly correlates to reduced breach costs and claim severity

Insurers increasingly assess whether organizations have continuous monitoring, defined detection metrics, and integrated response capabilities. This demonstrates security operations maturity.

**Threat Landscape Justification:**
**IBM X-Force 2025:** Organizations without timely detection capabilities allow attackers prolonged dwell time for reconnaissance, lateral movement, and data exfiltration. Account abuse and credential misuse require behavioral analytics to detect.

**Verizon DBIR 2024:** 75% of breaches involved ransomware. Early detection during reconnaissance or lateral movement phases prevents ransomware deployment. However, many organizations lack visibility and detection capabilities, allowing attacks to progress.

**K-12 Context:** School IT departments often lack 24/7 monitoring capabilities. Attacks during summer break, weekends, or holidays may go undetected for extended periods. Cloud-based EDR with managed detection and response (MDR) services provides practical detection capabilities. Tracking metrics helps resource-constrained IT teams demonstrate continuous improvement.

**Citations:**
- IBM (2024): "Average detection time 212 days; combined detection and containment 277 days"
- Wiz Academy: "High-performing orgs achieve 30 minutes - 4 hours MTTD"
- Lumifi Cybersecurity: "Organizations with lower MTTD better positioned for cyber insurance"
- Arctic Wolf: "MTTD and MTTR are critical incident response metrics"
- CIS Controls v8 (Control 8): Audit Log Management enables detection
- NIST CSF 2.0 (DE.CM): Security continuous monitoring

---

### Question 2.10: Privileged Account Session Monitoring
**Category:** 2 - Account Management and Access Control

**Question Text:**
Does the organization monitor and log privileged user sessions (administrators, service accounts) with the ability to review session recordings and detect suspicious privileged activities?

**Impact Rating:** High (5)

**Foundational Question:** NO - Comprehensive maturity indicator (PAM component)

**Control Description:**
Privileged session monitoring captures detailed records of activities performed by administrators and privileged service accounts, including:
- Session recording (screen capture/playback)
- Keystroke logging
- Command logging and audit trails
- Real-time suspicious activity alerts
- Ability to pause or terminate active suspicious sessions
- Searchable session archives for forensic investigation

This control typically requires PAM solutions but can be partially achieved through Windows Event Logging, Linux auditd, or privileged activity monitoring tools. Key capabilities:
1. All privileged sessions recorded and retained per data retention policy
2. Automated alerts for high-risk activities (credential access, security tool disablement, etc.)
3. Regular review of privileged activity logs
4. Integration with SIEM for correlation

**Insurance Rationale:**
Privileged account compromise is a critical insurance concern as it enables maximum attacker impact. Session monitoring:
- Provides forensic evidence during incident investigation (required for claim substantiation)
- Enables detection of insider threats or compromised admin accounts
- Demonstrates accountability and audit controls to insurers
- Meets compliance requirements (SOX, HIPAA, PCI DSS) that insurers assess

PAM solutions with session monitoring satisfy common auditor requirements. Organizations lacking privileged activity visibility face blind spots that increase claim severity.

**Threat Landscape Justification:**
**IBM X-Force 2025:** 30% of incidents involve account abuse, with privileged accounts as prime targets. Session monitoring detects anomalous admin activities (off-hours access, unusual commands, mass data access).

**Verizon DBIR 2024:** 88% of breaches involve stolen credentials. Compromised privileged accounts enable lateral movement and data exfiltration. Without session monitoring, organizations cannot detect attacker use of legitimate admin credentials.

**K-12 Context:** School IT staff often share admin credentials or use personal admin accounts for daily tasks. Service accounts for student information systems, payroll, and HR systems have broad permissions. Session monitoring provides accountability and detects compromised privileged accounts. Cloud-based PAM solutions offer practical implementation options.

**Citations:**
- ManageEngine: "Session recording, keystroke logging satisfy auditor requirements"
- BeyondTrust: "Monitoring and recording privileged sessions is core PAM capability for insurance"
- CIS Controls v8 (Control 5.4): Restrict and monitor administrator privileges
- NIST CSF 2.0 (PR.AC-4): Access permissions are monitored
- Securden: "Auditing privileged activities with real-time alerts required for cyber insurance"

---

### Question 4.16: Secure Remote Access Controls
**Category:** 4 - Secure Configuration and Vulnerability Management (Alternative: Category 2 - Account Management)

**Question Text:**
Beyond MFA, does the organization implement additional remote access security controls such as conditional access policies (device compliance, location-based access), network access control (NAC), or zero-trust network access (ZTNA)?

**Impact Rating:** Moderate (3)

**Foundational Question:** NO - Comprehensive maturity indicator

**Control Description:**
Enhanced remote access security goes beyond VPN+MFA to include:
- **Conditional Access:** Device health checks (OS version, encryption, EDR running), location-based policies, risk-based authentication (unusual location/time triggers additional verification)
- **Network Access Control (NAC):** Device posture assessment before network access, automated quarantine for non-compliant devices
- **Zero Trust Network Access (ZTNA):** Application-level access vs. network-level, least-privilege access per application, continuous verification
- **Split Tunneling Controls:** Policies for which traffic routes through VPN vs. direct internet
- **Remote Desktop Security:** Disabling RDP from internet, requiring VPN+MFA for RDP access, limiting RDP to specific IP ranges

**Insurance Rationale:**
Remote work expanded attack surface post-COVID, with Coalition reporting 82% of cyber insurance claims involved organizations lacking MFA. However, MFA alone is insufficient for remote access security. Insurers increasingly assess:
- Device compliance requirements (managed vs. unmanaged devices)
- Conditional access policies reducing risk-based access
- BYOD security controls
- VPN+MFA implementation quality (split tunneling risks, weak VPN protocols)

Organizations with "work from anywhere" policies face heightened risk if remote devices lack security controls. Remote work security requires VPN+MFA, EDR on all devices, encryption, DLP, and strict BYOD/Zero Trust policies.

**Threat Landscape Justification:**
**IBM X-Force 2025:** Most ransomware attacks start with compromised VPNs and remote access credentials. Advanced techniques exploit remote access technologies.

**Verizon DBIR 2024:** Remote access exploitation is a top attack path. Attackers scan for VPN endpoints and attempt credential stuffing.

**K-12 Context:** Post-COVID, many teachers and administrators work remotely or from multiple locations. BYOD (personal laptops, tablets) is common. Student remote learning platforms expanded attack surface. Schools need conditional access policies to ensure remote devices meet security baselines. Microsoft 365/Google Workspace conditional access features provide practical implementation paths.

**Citations:**
- Corvus Insurance (2024): "BYOD introduces security risks leaving companies vulnerable"
- DeepStrike (2025): "Remote work security requires VPN+MFA, EDR, encryption, DLP, BYOD/Zero Trust"
- Coalition (2024): "82% of claims involved orgs lacking MFA; remote access primary attack vector"
- Venn (2025): "BYOD market $52B in 2024, growing 15% CAGR to $150B by 2035"
- CIS Controls v8 (Control 12.6): Use secure network management and communication protocols

---

### Question 8.7: Vendor Continuous Monitoring and Incident Notification
**Category:** 8 - Third-Party and Vendor Risk Management

**Question Text:**
Does the organization continuously monitor vendors for security incidents or breaches and require contractual notification within defined timeframes (e.g., 24-48 hours) when vendors experience security events?

**Impact Rating:** Moderate (3)

**Foundational Question:** NO - Comprehensive maturity indicator

**Control Description:**
Vendor continuous monitoring and incident notification includes:
- **Continuous Monitoring:** Security rating services (SecurityScorecard, BitSight, UpGuard), breach notification monitoring, vendor security posture tracking
- **Contractual Requirements:** Vendor breach notification clauses, incident reporting timeframes (typically 24-48 hours), cooperation during incident response
- **Response Planning:** Procedures for vendor-originated incidents, assessment of exposure when vendor breached, coordination with vendor during containment

Organizations should:
1. Subscribe to threat intelligence or vendor monitoring services
2. Include breach notification language in vendor contracts
3. Define vendor notification expectations (timeframe, contact information, details required)
4. Maintain communication plan for vendor security incidents
5. Review vendor security quarterly or when significant changes occur

**Insurance Rationale:**
Third-party breaches increasingly impact downstream organizations. MOVEit vulnerability (2023-2024) affected hundreds of organizations through software vendor compromise. Insurers assess whether organizations:
- Have visibility into vendor security posture changes
- Will be notified promptly of vendor breaches
- Can assess exposure and respond to vendor incidents

Only 26% of organizations integrate incident response into TPRM programs. Less than 50% monitor even half their supply chain for threats. 54% of organizations don't sufficiently understand supply chain cyber exposure. Insurers recognize this gap and assess vendor monitoring maturity.

**Threat Landscape Justification:**
**Verizon DBIR 2024:** Third-party involvement in breaches doubled. MOVEit vulnerability was largest driver of cyberattacks first in education sector, then spreading to finance and insurance. Vendor-originated incidents require rapid response.

**Industry Research (2024-2025):** 41% of attacks originated from third parties. Without continuous monitoring, organizations learn of vendor breaches through media or breach notifications, delaying response. Average detection time compounds when vendor dwell time is added.

**K-12 Context:** Schools use numerous cloud-based ed-tech vendors. Vendor breaches exposing student data trigger FERPA notification requirements to parents. Schools need timely notification from vendors to meet statutory obligations. Many vendor contracts lack security breach notification clauses, creating blind spots.

**Citations:**
- SecurityScorecard (2025): "54% of orgs don't understand supply chain cyber exposure"
- WEF (2024): "Only 26% integrate incident response into TPRM programs"
- Centraleyes (2024): "Less than 50% monitor even half extended supply chain for threats"
- Verizon DBIR (2024): "Third-party involvement doubled; MOVEit affected education sector first"
- CIS Controls v8 (Control 15.2): Establish vendor communication channels

---

### Question 5.6: API Security Controls
**Category:** 5 - Malware Defense and Endpoint Security (Alternative: Category 4 - Secure Configuration)

**Question Text:**
For organizations using APIs (application programming interfaces) to integrate systems or provide services, are API security controls implemented including authentication (OAuth 2.0), authorization, rate limiting, and API activity monitoring?

**Impact Rating:** Moderate (3)

**Foundational Question:** NO - Comprehensive maturity indicator

**Control Description:**
API security controls protect application programming interfaces from abuse and exploitation:
- **Authentication:** OAuth 2.0, API keys, mutual TLS for API clients
- **Authorization:** Role-based access control (RBAC), attribute-based access control (ABAC), least-privilege API permissions
- **Rate Limiting:** Throttling to prevent abuse, DDoS protection
- **Input Validation:** Prevent injection attacks, sanitize user inputs
- **Monitoring:** API activity logging, anomaly detection (unusual access patterns), integration with SIEM
- **API Inventory:** Maintain catalog of all APIs (public, internal, partner), including version tracking

Organizations should:
1. Discover and inventory all APIs (including shadow APIs)
2. Implement authentication and authorization for all APIs
3. Monitor API traffic for anomalies
4. Conduct API security testing (penetration testing, vulnerability scanning)
5. Follow OWASP API Security Top 10 guidance

**Insurance Rationale:**
APIs represent emerging attack surface with significant financial impact. 78% of security professionals experienced API security breach in 2023. API vulnerabilities cost organizations $2.5 billion in 2024 in remediation, fines, and lost revenue. Insurers are beginning to assess API security as:
- Organizations adopt cloud-native architectures with extensive API usage
- Successful API compromises will grow through 2025
- Data breaches via API vulnerabilities trigger notification and remediation costs
- Regulatory requirements (PCI DSS v4, SEC disclosure rules) include API security

While not yet universal insurance requirement, API security is trending toward standard expectation for organizations with significant API usage.

**Threat Landscape Justification:**
**Industry Research (2024-2025):** 99% of surveyed organizations experienced API security issue in prior 12 months (Q1 2025). Only 10% had API posture governance strategy. Successful API-related compromises projected to grow through 2025 driven by expanding API usage, increasing complexity, growing data access, and improving attacker capabilities.

**K-12 Context:** Schools increasingly use APIs for system integrations - student information systems syncing with learning management systems, single sign-on integrations, rostering APIs for ed-tech platforms, assessment data sharing. Many schools lack visibility into API usage or security controls. Cloud-based APIs (Google Workspace, Microsoft Graph API) require proper authentication and permissions management.

**Citations:**
- CybelAngel (2025): "78% of security professionals experienced API breach in 2023"
- Imperva (2024): "API vulnerabilities cost $2.5 billion in 2024"
- APIsec (2025): "99% of orgs experienced API security issue in prior 12 months"
- SecurityWeek (2025): "Successful API compromises will grow through 2025"
- OWASP API Security Top 10 (2023): Industry-standard API security framework

---

### Question 3.6: Data Classification and Handling Procedures
**Category:** 3 - Data Protection and Privacy

**Question Text:**
Has the organization established a data classification system (e.g., public, internal, confidential, restricted) with documented handling procedures for each classification level?

**Impact Rating:** Moderate (3)

**Foundational Question:** NO - Comprehensive maturity indicator

**Control Description:**
Data classification systematically categorizes information based on sensitivity and impact of unauthorized disclosure:
- **Classification Levels:** Typical K-12 scheme:
  - Public: Information intended for public distribution (school website, newsletters)
  - Internal: Information for internal use (staff directories, policies)
  - Confidential: Student education records (FERPA), employee PII, financial data
  - Restricted: Highly sensitive data (SSNs, health records, investigation files)

- **Handling Procedures:** For each classification:
  - Storage requirements (encryption, access controls)
  - Transmission methods (encrypted email, secure file transfer)
  - Sharing/disclosure rules
  - Retention and destruction requirements
  - Labeling requirements (email subject tags, document headers)

Organizations should:
1. Define classification levels aligned with legal/regulatory requirements
2. Document handling procedures for each level
3. Train staff on classification and handling requirements
4. Implement technical controls enforcing handling procedures (DLP, encryption policies)
5. Review and update classification system annually

**Insurance Rationale:**
Data classification enables targeted protection and reduces breach impact. Insurers assess data classification maturity as indicator of:
- Organization's understanding of what data it holds
- Appropriate controls applied based on data sensitivity
- Breach notification scope (properly classified data enables rapid impact assessment)
- Compliance with privacy regulations (FERPA, state privacy laws)

Organizations without data classification struggle to answer insurer questions about sensitive data volumes, storage locations, and protection measures. Classification supports Question 3.1 (data inventory) and Question 3.4 (data retention) by providing framework for data governance.

**Threat Landscape Justification:**
**Verizon DBIR 2024:** Breaches increasingly target specific data types (credentials, personal information, payment data). Data classification enables organizations to focus protection on highest-value targets.

**Privacy Regulations (2024-2025):** Eight new state privacy laws in 2025 alone require data minimization and protection proportionate to sensitivity. Data classification is foundational to compliance.

**K-12 Context:** Schools handle diverse data sensitivity levels - public school calendars, internal staff communications, confidential student education records (FERPA), restricted special education records and investigation files. Many school staff lack clarity on what constitutes FERPA-protected data vs. directory information. Data classification with staff training reduces inadvertent disclosures.

**Citations:**
- NIST CSF 2.0 (ID.AM-5): "Resources are prioritized based on classification"
- CIS Controls v8 (Control 3.1): "Establish and maintain data management process"
- FERPA Compliance: Data classification helps distinguish education records from directory information
- State Privacy Laws (2025): "Data classification supports proportionate protection"

---

## Integration Guidance: How Questions Fit into Dual-Score Model

### Recommended Distribution Across Categories

**Category 2: Account Management (2 new questions)**
- 2.10: Privileged Account Session Monitoring

**Category 3: Data Protection (1 new question + 1 relocated)**
- 3.5: Privileged Access Management (PAM) Platform [FOUNDATIONAL]
- 3.6: Data Classification and Handling Procedures

**Category 4: Secure Configuration (3 new questions)**
- 4.14: Centralized Logging and SIEM [FOUNDATIONAL - Tiered by district size]
- 4.15: Cloud Security Configuration Management
- 4.16: Secure Remote Access Controls

**Category 5: Malware Defense (2 new questions)**
- 5.5: Email Authentication Protocols (DMARC, SPF, DKIM) [FOUNDATIONAL]
- 5.6: API Security Controls

**Category 8: Vendor Management (2 new questions)**
- 8.6: Third-Party Security Certifications and Assessments
- 8.7: Vendor Continuous Monitoring and Incident Notification

**Category 9: Incident Response (1 new question)**
- 9.7: Incident Detection and Response Capabilities

**TOTAL: 11 new questions (63 total questions in expanded assessment)**

### Foundational Questions Recommendation

**New Foundational Questions (4 questions):**
1. **3.5 - PAM Platform:** Critical insurance requirement; 42% of orgs required for coverage
2. **4.14 - Centralized Logging/SIEM:** Tiered requirement (foundational for districts >2,500 students; comprehensive for smaller districts)
3. **5.5 - Email Authentication (DMARC):** K12 SIX framework considers SPF/DKIM baseline; DMARC prevents impersonation

**Consideration for Foundational Status:**
- **8.6 - Vendor Security Certifications:** Trending toward foundational given third-party breach doubling, but recommend keeping as comprehensive maturity indicator for now

**Revised Foundational Count:**
- **Current:** 12 foundational questions
- **Recommended:** 15-16 foundational questions (depending on SIEM tiering approach)
- **The Trust Requirements:** May need expansion from 7 to 9-10 requirements to incorporate PAM, SIEM, and email authentication

### Dual-Score Model Impact

**Foundation Score (Tier I):**
- **Purpose:** Insurance eligibility and premium tier
- **Questions:** 15-16 foundational questions (was 12)
- **New Coverage:** PAM, centralized logging, email authentication
- **Rationale:** These controls directly align with 2024-2025 cyber insurance mandatory requirements

**Comprehensive Score (Tier II):**
- **Purpose:** Full security maturity assessment
- **Questions:** 63 total questions (was 52)
- **New Coverage:** Cloud security, API security, enhanced vendor risk, incident detection, remote access, data classification, privileged session monitoring
- **Rationale:** Demonstrates advanced security maturity and addresses emerging threat landscape

### Scoring Considerations

**Impact Ratings for New Questions:**
- **High (5):** 8 questions - PAM, SIEM, Cloud Security, Email Auth, Vendor Certifications, Privileged Sessions, Remote Access (borderline)
- **Moderate (3):** 3 questions - Incident Detection, Vendor Monitoring, API Security, Data Classification

**Risk Scoring Impact:**
- New questions follow existing formula: Control Rating (1/3/5) × Impact Rating (1/3/5)
- High-impact questions (5) create maximum risk differential between organizations
- Proper weighting aligns with insurance underwriting priorities

### Implementation Phasing Recommendation

**Phase 1 (January 2026 Launch):**
- Add 4 foundational questions: PAM, SIEM (tiered), Email Authentication
- Update Foundation Score calculation
- Communicate new insurance requirements to members

**Phase 2 (June 2026):**
- Add 7 comprehensive questions: Cloud Security, Vendor enhancements, Incident Detection, Remote Access, API Security, Data Classification, Privileged Sessions
- Update Comprehensive Score calculation
- Provide maturity roadmaps for advanced controls

**Rationale for Phasing:**
- Foundational questions align with immediate insurance renewal pressures
- Comprehensive questions require education and potentially longer implementation timelines
- Allows members to focus on insurance-critical gaps first

---

## Alternative Question Considerations (Not Recommended for Immediate Addition)

These questions were considered but NOT recommended for immediate addition due to lower priority, niche applicability, or overlap with existing questions:

### 1. Security Orchestration, Automation, and Response (SOAR)
**Why Not Recommended:** Too advanced for most K-12 environments; SIEM (Question 4.14) addresses core need. SOAR is typically for larger enterprises with dedicated SOC teams.

### 2. Data Loss Prevention (DLP)
**Why Not Recommended:** High implementation complexity for K-12; EDR and cloud security controls (Questions 5.4, 4.15) provide partial DLP capabilities. Consider for Phase 3 expansion.

### 3. Network Segmentation (Student vs. Staff vs. IoT)
**Why Not Recommended:** Partially covered by Questions 4.9-4.10 (network and wireless segmentation). Could enhance with IoT-specific language in future revision.

### 4. Mobile Device Management (MDM) for BYOD
**Why Not Recommended:** Overlaps with remote access controls (Question 4.16). K-12 schools increasingly use Chromebooks (managed by Chrome Admin) or Microsoft Intune. Consider adding specific MDM language to Question 4.16 in future.

### 5. Penetration Testing
**Why Not Recommended:** Vulnerability scanning (Question 4.7) addresses core insurance need. Penetration testing is valuable but not yet universal insurance requirement for K-12. Consider for larger districts or Phase 3.

### 6. Cyber Insurance Coverage Limits and Terms Review
**Why Not Recommended:** While important, this is policy/financial question vs. security control. Question 9.6 covers cyber insurance purchase.

### 7. Security Metrics Dashboard/Reporting to Board
**Why Not Recommended:** Governance question vs. technical control. Important for organizational maturity but not direct insurance/threat requirement.

### 8. Secure Software Development Lifecycle (SDLC)
**Why Not Recommended:** Most K-12 schools don't develop software. Vendor security (Category 8) addresses software acquisition security.

### 9. Quantum-Resistant Cryptography
**Why Not Recommended:** Emerging concern but not actionable for K-12 in 2025-2026 timeframe. Monitor for future years.

### 10. Insider Threat Program
**Why Not Recommended:** Partially addressed by privileged session monitoring (Question 2.10), user behavior analytics (implicit in SIEM Question 4.14), and off-boarding procedures (Question 2.9). Dedicated insider threat programs are advanced capability.

---

## Summary Table: Recommended Questions

| # | Question | Category | Impact | Foundational | Insurance Pressure | Primary Threat |
|---|----------|----------|--------|--------------|-------------------|----------------|
| 3.5 | Privileged Access Management (PAM) | Data Protection | High (5) | 🔑 YES | HIGH - 42% required | Credential Abuse |
| 4.14 | Centralized Logging/SIEM | Secure Config | High (5) | 🔑 YES (Tiered) | HIGH - Larger orgs | Detection Gap |
| 4.15 | Cloud Security Configuration | Secure Config | High (5) | NO | MODERATE-HIGH | Misconfiguration |
| 4.16 | Secure Remote Access Controls | Secure Config | Moderate (3) | NO | MODERATE | Remote Exploit |
| 5.5 | Email Authentication (DMARC/SPF/DKIM) | Malware Defense | High (5) | 🔑 YES | MODERATE | Phishing/BEC |
| 5.6 | API Security Controls | Malware Defense | Moderate (3) | NO | LOW-MODERATE | API Exploit |
| 8.6 | Vendor Security Certifications | Vendor Risk | High (5) | NO | MODERATE | Supply Chain |
| 8.7 | Vendor Continuous Monitoring | Vendor Risk | Moderate (3) | NO | MODERATE | Supply Chain |
| 9.7 | Incident Detection Capabilities (MTTD) | Incident Response | Moderate (3) | NO | MODERATE | Detection Gap |
| 2.10 | Privileged Session Monitoring | Account Mgmt | High (5) | NO | MODERATE | Insider/Abuse |
| 3.6 | Data Classification & Handling | Data Protection | Moderate (3) | NO | MODERATE | Privacy/Governance |

**Total: 11 questions**
**Foundational: 3-4 questions** (depending on SIEM tiering)
**Total Assessment: 63 questions** (was 52)

---

## Citations and References

### Threat Intelligence Reports

**IBM X-Force Threat Intelligence Index 2025**
- URL: https://www.ibm.com/reports/threat-intelligence
- Key Finding: "Account abuse remains primary entry point (30% of incidents); 84% uptick in phishing emails delivering infostealers"
- Education Sector: "K-12 schools most vulnerable within education industry with small staffs and budgets"

**Verizon Data Breach Investigations Report 2024**
- URL: https://www.verizon.com/business/resources/reports/dbir/
- Key Findings:
  - "75% of breaches included ransomware (notable rise from prior year)"
  - "88% of breaches involved stolen credentials"
  - "Education: 1,537 confirmed breaches; social engineering (42%) and system intrusion (35%) top patterns"
  - "Third-party involvement in breaches doubled"
  - "Only 50% of perimeter vulnerabilities fully remediated"

### Cyber Insurance Industry Reports

**Coalition Cyber Insurance**
- Cyber Threat Index 2024-2025: https://www.coalitioninc.com/announcements/cyber-threat-index-2025
- Coverage Checklist: https://www.coalitioninc.com/topics/cyber-liability-insurance-checklist
- Email Authentication: https://www.coalitioninc.com/topics/authenticating-email-using-SPF-DKIM-&-DMARC
- Finding: "Most ransomware attacks start with compromised VPNs and remote access credentials"
- Finding: "82% of claims involved organizations lacking MFA"

**Privileged Access Management (PAM) and Insurance**
- Securden (2024): "42% of organizations required to have PAM for coverage (up from 36% in 2023)"
  - URL: https://www.securden.com/privileged-account-manager/pam-for-cyberinsurance.html
- ManageEngine: "Vast majority of cyberattacks due to stolen credentials and misuse of privileged access"
  - URL: https://www.manageengine.com/privileged-access-management/pam-for-cyberinsurance.html
- BeyondTrust: "Two basic requirements: removing admin rights and enforcing PoLP"
  - URL: https://www.beyondtrust.com/solutions/cyber-insurance

**SIEM and Security Monitoring**
- TechSolutions Inc (2024): "SOC and SIEM no longer optional for cyber insurance"
  - URL: https://www.techsolutionsinc.com/blog/why-soc-and-siem-are-no-longer-optional-for-cyber-insurance/
- Atlantic Digital (2024): "SIEM among key requirements for cyber insurance in 2024"
  - URL: https://www.adiit.com/cyber-insurance-key-requirements-and-industry-insights/

**Third-Party Risk and Supply Chain**
- Arch Insurance (2024): "Insurers require robust TPRM with vendor certifications and insurance"
  - URL: https://insurance.archgroup.com/cyber-the-rise-in-third-party-risks-calls-for-greater-transparency/
- Cybersecurity Ventures (2024): "$60 billion in losses from supply chain attacks in 2025; 15% annual increase"
- Gartner: "45% of companies will experience supply chain cyberattack by 2025"
- WEF (2024): "54% of executives cite TPRM as major challenge; 41% of attacks from 3rd parties"
  - URL: https://www.weforum.org/stories/2025/04/three-key-directions-for-the-cyber-resiliency-crisis-in-global-supply-chains/

**Remote Work and BYOD**
- Corvus Insurance (2024): "BYOD introduces security risks leaving companies vulnerable"
  - URL: https://www.corvusinsurance.com/blog/byod-does-a-cyber-insurance-policy-cover-remote-workers
- DeepStrike (2025): "Remote work security requires VPN+MFA, EDR, encryption, DLP, BYOD/Zero Trust"
  - URL: https://deepstrike.io/blog/Remote-Work-Security-Risks-2025
- Venn (2025): "BYOD market $52B in 2024, growing 15% CAGR to $150B by 2035"
  - URL: https://www.venn.com/learn/byod/byod-security-best-practices/

### K-12 Cybersecurity Research

**K12 Security Information eXchange (K12 SIX)**
- GovTech (2024): "K12 SIX updated framework for 2024-25; SPF and DKIM now baseline protections"
  - URL: https://www.govtech.com/education/k-12/k12-six-releases-updated-framework-for-school-cybersecurity

**Email Security for Education**
- Clever Education (2024): "Schools should implement SPF, DKIM, DMARC to protect against spoofing"
  - URL: https://www.clever.com/blog/2024/06/email-security-for-education
- Virginia School Data (2024): "84.6% SPF adoption, only 16% DMARC adoption, 8% with enforcement policies"

### Cloud Security

**Cloud Security Statistics**
- GBHackers (2025): "95% of cloud breaches stem from misconfigurations"
  - URL: https://gbhackers.com/best-cloud-security-companies/
- Orca Security (2025): "Multi-cloud compliance requires consistent security policies across AWS, Azure, GCP"
  - URL: https://orca.security/resources/blog/what-is-multi-cloud-compliance/

### API Security

**API Security Research**
- CybelAngel (2025): "78% of security professionals experienced API breach in 2023"
  - URL: https://cybelangel.com/blog/the-api-threat-report-2025/
- Imperva (2024): "API vulnerabilities cost $2.5 billion in 2024"
  - URL: https://www.imperva.com/blog/state-of-api-security-in-2024/
- APIsec (2025): "99% of orgs experienced API security issue in prior 12 months"
  - URL: https://www.apisec.ai/blog/apisec-presents-the-2024-api-security-market-report

### Incident Detection Metrics

**MTTD Research**
- IBM (2024): "Average detection time 212 days; combined detection and containment 277 days"
- Wiz Academy: "High-performing orgs achieve 30 minutes - 4 hours MTTD"
  - URL: https://www.wiz.io/academy/mttd-and-mttr
- Lumifi Cybersecurity: "Organizations with lower MTTD better positioned for cyber insurance"
  - URL: https://www.lumificyber.com/fundamentals/what-is-mean-time-to-detect/

### Privacy and Compliance

**Data Privacy Regulations**
- State Privacy Laws (2025): "Eight new state privacy laws in 2025 alone; data retention and deletion required"
- FERPA Compliance: Data classification helps distinguish education records from directory information
  - URL: https://studentprivacy.ed.gov/

### Frameworks and Standards

**CIS Controls v8**
- URL: https://www.cisecurity.org/controls/cis-controls-navigator
- Referenced Controls: 1, 2, 3, 4, 5, 7, 8, 12, 14, 15, 17

**NIST Cybersecurity Framework 2.0**
- URL: https://www.nist.gov/cyberframework
- Referenced Functions: Identify (ID.AM), Protect (PR.AC, PR.IP), Detect (DE.AE, DE.CM), Respond (RS.CO), Recover (RC.CO)

**OWASP API Security Top 10**
- URL: https://owasp.org/API-Security/
- Industry-standard API security framework

---

## Appendices

### Appendix A: Insurance Application Question Mapping

This table maps recommended CyberPools questions to specific cyber insurance application requirements:

| Insurance Requirement | CyberPools Question | Carrier Examples |
|----------------------|---------------------|------------------|
| Privileged Access Management | 3.5 - PAM Platform | Coalition, Chubb, Corvus |
| Security Monitoring/SIEM | 4.14 - Centralized Logging | Chubb, Corvus |
| Email Authentication | 5.5 - DMARC/SPF/DKIM | Coalition |
| Cloud Security Controls | 4.15 - Cloud Security Config | Chubb, Coalition |
| Vendor Security Assessments | 8.6 - Vendor Certifications | Chubb, Corvus |
| Incident Detection Capabilities | 9.7 - MTTD/MTTR | Chubb |
| Remote Access Controls | 4.16 - Enhanced Remote Access | Coalition, Corvus |
| Data Classification | 3.6 - Data Classification | Chubb |

### Appendix B: Threat Landscape to Question Mapping

| Threat/Attack Vector | Verizon DBIR 2024 Finding | IBM X-Force 2025 Finding | CyberPools Question |
|---------------------|---------------------------|-------------------------|---------------------|
| Stolen Credentials | 88% of breaches | 30% of incidents (account abuse) | 3.5 (PAM), 2.10 (Session Monitoring) |
| Ransomware | 75% of breaches | Most start with compromised VPN | 4.16 (Remote Access), 4.14 (SIEM) |
| Phishing | 42% of education attacks | 84% uptick in infostealer phishing | 5.5 (Email Authentication) |
| Third-Party Compromise | Doubled from prior year | Supply chain attacks growing | 8.6 (Vendor Certs), 8.7 (Vendor Monitoring) |
| Cloud Misconfiguration | N/A | Identity-based attacks increasing | 4.15 (Cloud Security) |
| Unpatched Vulnerabilities | 50% perimeter vulns unresolved | 25%+ incidents exploit vulns | Existing 4.3 (Patch Mgmt) |
| Detection Gap | N/A | Avg 212 days to detect | 9.7 (MTTD), 4.14 (SIEM) |
| API Exploitation | N/A | Emerging threat | 5.6 (API Security) |

### Appendix C: Implementation Resources for K-12

**Privileged Access Management (PAM):**
- Cloud-based PAM for K-12: Delinea Secret Server Cloud, BeyondTrust Remote Support, ManageEngine PAM360 Cloud
- EDU pricing typically available
- Managed service options for schools without dedicated security staff

**Centralized Logging/SIEM:**
- K-12-friendly SIEM options: Microsoft Sentinel (M365 edu integration), Splunk Cloud (EDU pricing), Sumo Logic (cloud-native)
- Google Workspace Security Center (basic log management included)
- Managed SOC services: Arctic Wolf, Huntress, Red Canary (K-12 specialized offerings)

**Email Authentication:**
- Microsoft 365: Built-in SPF/DKIM; DMARC configuration via DNS
- Google Workspace: Built-in SPF/DKIM; DMARC configuration via DNS
- Free DMARC monitoring tools: DMARC Analyzer, MXToolbox, Postmark DMARC
- Implementation guide: Coalition's SPF/DKIM/DMARC documentation

**Cloud Security:**
- Microsoft 365: Microsoft Secure Score (built-in), Defender for Cloud Apps
- Google Workspace: Security Health page, Security Center investigations
- AWS/Azure: Native CSPM tools (Security Hub, Security Center)

**Vendor Risk Management:**
- Vendor assessment platforms: Whistic, SecurityScorecard, UpGuard (K-12 pricing)
- Template security questionnaires: CIS, NIST
- Contract language templates: CoSN (Consortium for School Networking)

### Appendix D: Question Development Methodology

This research followed a systematic methodology:

1. **Threat Intelligence Review:**
   - IBM X-Force Threat Intelligence Index 2024-2025
   - Verizon Data Breach Investigations Report 2024
   - Industry threat reports (Coalition, Corvus, etc.)

2. **Insurance Market Research:**
   - Cyber insurance application questionnaires (Coalition, Corvus, Chubb, At-Bay, Cowbell)
   - Insurance industry publications (Woodruff Sawyer, MoneyGeek, CybelAngel, etc.)
   - Insurance requirement trend analysis (2024-2025)

3. **Gap Analysis:**
   - Current CyberPools assessment structure (52 questions, 9 categories)
   - Mapping of current questions to threat landscape
   - Identification of coverage gaps

4. **Question Development:**
   - Practical applicability to K-12 environments
   - Alignment with insurance underwriting priorities
   - Measurable/assessable controls
   - Integration with existing assessment structure

5. **Validation:**
   - Cross-reference with CIS Controls v8, NIST CSF 2.0, CISA CPGs
   - K-12 context verification (K12 SIX, CoSN, ed-tech research)
   - Insurance rationale substantiation with citations

---

**Report Completed:** October 30, 2025
**Next Steps:**
1. Review recommended questions with CyberPools leadership
2. Validate with The Trust insurance pool requirements
3. Pilot test questions with 5-10 member districts
4. Update assessment templates and scoring algorithms
5. Develop member communication and training materials
6. Plan phased rollout (January 2026 foundational; June 2026 comprehensive)
