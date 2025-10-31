---
title: Category 6 - Data Recovery and Business Continuity
tags:
  - Category 6
  - Foundational
  - High Impact
  - Moderate Impact
---

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

