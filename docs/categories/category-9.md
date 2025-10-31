---
title: Category 9 - Incident Response and Recovery
tags:
  - Category 9
  - New
  - High Impact
  - Moderate Impact
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

### Question 9.1: Incident Response Plan

**Question Text:**
Does the organization have a documented Incident Response Plan (IRP) that defines procedures for detecting, responding to, and recovering from cybersecurity incidents?

**Response Options:**

- Fully implemented - documented IRP, incident types defined, response procedures detailed, regularly updated
- Partially implemented - informal IRP or outdated documentation
- Not implemented - no incident response plan

**Impact Rating:** High (5)

**Foundational:** No (but critical control)

**Control Description:**

An Incident Response Plan (IRP) provides structured procedures for responding to cybersecurity incidents, minimizing damage and recovery time. Effective IRPs include:

**IRP Components:**

- **Incident Types:** Define incident categories (ransomware, phishing, data breach, DDoS, insider threat)
- **Incident Severity Levels:** High/Medium/Low severity criteria
- **Response Procedures:** Step-by-step procedures for each incident type (detect, contain, eradicate, recover, lessons learned)
- **Roles and Responsibilities:** Who does what during incident response (IR team roles - Question 9.2)
- **Communication Protocols:** Internal escalation, external notifications (law enforcement, insurers, regulators)
- **Evidence Preservation:** Forensic procedures for preserving evidence
- **Recovery Procedures:** System restoration, business continuity integration (Question 6.5-6.6)

**NIST Incident Response Lifecycle:**

1. **Preparation:** Tools, training, IR plan maintenance
2. **Detection and Analysis:** Identify and analyze incidents
3. **Containment, Eradication, and Recovery:** Stop incident, remove threat, restore operations
4. **Post-Incident Activity:** Lessons learned, plan updates

**Insurance Rationale (Universal):**

**IR Plan Requirement:**

- **100% of cyber insurers require documented IR plans** for coverage
- IR plan documentation may be requested during policy application/renewal
- Organizations with IR plans receive lower premiums (demonstrate preparedness)

**Faster Recovery = Lower Costs:**

- Organizations with IR plans recover 3-5x faster than those without
- **Average ransomware recovery:** 21 days without plan, 5-7 days with tested plan (Veeam 2024)
- Insurers pay lower claims for organizations with rapid IR

**Breach Notification Compliance:**

- IR plans ensure compliance with breach notification deadlines:

  - **HIPAA:** 60 days for breach notification
  - **State Laws:** 30-90 days (varies by state)
  - **GDPR:** 72 hours for breach notification
- Without IR plan, organizations miss deadlines → regulatory fines

**Threat Landscape Justification:**

**Incident Inevitability:**

- **68% of organizations experience material incidents** annually (Verizon DBIR 2024)
- **Average detection time: 212 days** without incident detection capabilities
- IR plan defines detection, response, recovery procedures

**Ransomware Recovery:**

- **75% of breaches include ransomware** (Verizon DBIR 2024)
- IR plan defines ransomware response: isolate systems, engage law enforcement, restore from backups, notify insurers
- Without IR plan, organizations make reactive decisions (pay ransom, lose data)

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Incident Scenarios:** Ransomware, phishing targeting staff/students, data breaches (student data), website defacement
- **Practical Implementation:** Adapt NIST IR framework, use Department of Education IR resources
- **FERPA Compliance:** IR plan includes procedures for student data breaches (notification to families, Department of Education)
- **Limited IT Resources:** IR plan defines when to engage external IR services (CyberPools, managed SOC, FBI)

**Healthcare:**

- **Incident Scenarios:** Ransomware affecting patient care, PHI breaches, medical device compromises
- **HIPAA Requirement:** Contingency plan must include incident response procedures
- **60-Day Notification:** IR plan ensures HIPAA breach notification met (HHS Office for Civil Rights)
- **Patient Safety:** IR plan addresses incidents affecting life-safety systems (patient monitoring, EHR downtime)

**Religious/Nonprofit:**

- **Incident Scenarios:** Ransomware, business email compromise, donor data breaches, website hacks
- **Donor Confidence:** IR plan demonstrates responsible data stewardship
- **Limited Resources:** IR plan defines when to engage external help (law enforcement, cyber insurance IR hotline)
- **Practical Implementation:** Simple IR plan template from CISA, SANS

**General Organizations:**

- **Compliance Drivers:** PCI DSS, SOC 2, ISO 27001 require incident response plans
- **Industry-Specific Scenarios:** Tailor IR plan to industry threats (financial fraud, IP theft, supply chain attacks)
- **Enterprise IR:** Dedicated IR teams, SIEM integration, forensic retainers

**Citations:**

- CIS Controls v8: Control 17 (Incident Response Management)
- NIST CSF 2.0: RS.MA-1 (Incident response plan is executed)
- **NIST SP 800-61 Rev. 2:** Computer Security Incident Handling Guide
- **Verizon DBIR 2024:** 68% of organizations experience material incidents
- **IBM Cost of Data Breach 2024:** Average detection time 212 days
- **Veeam 2024:** Average ransomware recovery 21 days without plan, 5-7 days with plan
- **HIPAA:** 45 CFR § 164.308(a)(6) - Security incident procedures required
- **PCI DSS 4.0:** Requirement 12.10 - Incident response plan required

---

### Question 9.2: Incident Response Team

**Question Text:**
Has the organization established an Incident Response Team (IRT) with defined roles, responsibilities, and contact information?

**Response Options:**

- Fully implemented - dedicated IRT, roles documented, 24/7 contact information
- Partially implemented - informal IR roles, limited documentation
- Not implemented - no IR team designated

**Impact Rating:** Moderate (3)

**Foundational:** No

**Control Description:**

An Incident Response Team (IRT) provides personnel structure for executing the IR plan (Question 9.1). Effective IRTs include:

**IR Team Roles:**

- **IR Manager/Coordinator:** Leads incident response, coordinates team activities
- **Technical Responders:** IT staff who contain/eradicate threats, preserve evidence
- **Legal Counsel:** Advises on legal obligations, breach notification requirements
- **Communications:** Handles internal/external communications (staff, media, customers)
- **Executive Sponsor:** Provides authority, resources, executive decisions
- **External Partners:** Law enforcement (FBI, Secret Service), cyber insurer, forensic vendors, legal counsel

**Team Responsibilities:**

- **Detection:** Monitor alerts, investigate suspicious activity
- **Containment:** Isolate affected systems, prevent lateral movement
- **Eradication:** Remove threat actors, malware from environment
- **Recovery:** Restore systems, verify threat removed
- **Communication:** Internal stakeholder updates, external notifications
- **Documentation:** Incident timeline, actions taken, evidence preservation

**Contact Information:**

- **IR Hotline:** 24/7 contact information for IR team members
- **Escalation Procedures:** When to escalate to executives, law enforcement, insurers
- **External Contacts:** Cyber insurance IR hotline, FBI cyber division, forensic vendors

**Insurance Rationale (Universal):**

**IR Team Demonstrates Preparedness:**

- Cyber insurers value designated IR teams
- IR team contact information may be requested during policy application

**Faster Incident Response:**

- Organizations with IR teams respond faster than those assembling ad-hoc teams during incidents
- Faster response = lower breach costs = lower insurance claims

**Cyber Insurance IR Services:**

- Many cyber insurance policies provide **incident response services** (forensics, legal counsel, public relations)
- IR team knows how to activate insurer IR services during incidents

**Threat Landscape Justification:**

**24/7 Incident Response:**

- Cyber incidents occur 24/7; weekends, holidays, nights
- IR team provides 24/7 response capability (or defines after-hours escalation)

**Coordinated Response:**

- Incidents require coordination across IT, legal, communications, executives
- IR team provides structure for coordinated response (vs. chaotic ad-hoc response)

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **IR Team Composition:** IT Director (IR Manager), network admin (technical responder), superintendent/president (executive sponsor), legal counsel
- **Limited Staff:** Small districts may have 1-2 person "IR team"; define when to engage external help (CyberPools, FBI, cyber insurer)
- **After-Hours Coverage:** Define after-hours escalation (IT staff may not be 24/7; define who to call nights/weekends)

**Healthcare:**

- **IR Team Composition:** CISO/IT Director (IR Manager), IT staff, HIPAA Privacy Officer (legal), communications, CEO (executive sponsor)
- **24/7 Operations:** Healthcare requires 24/7 IR capability; define on-call rotations
- **Patient Safety Integration:** IR team coordinates with patient safety/clinical engineering for incidents affecting patient care

**Religious/Nonprofit:**

- **IR Team Composition:** IT lead or external IT provider (IR Manager), executive director (executive sponsor), legal counsel
- **Volunteer IT:** Many nonprofits rely on volunteer/part-time IT; IR team defines when to engage professional IR help
- **Board Notification:** IR team includes procedures for notifying board of directors for significant incidents

**General Organizations:**

- **Enterprise IR Teams:** Dedicated IR teams with 24/7 SOC, forensic capabilities
- **CSIRT/CERT:** Some organizations establish formal Computer Security Incident Response Teams (CSIRTs)
- **Compliance:** SOC 2, ISO 27001 require defined IR roles

**Citations:**

- CIS Controls v8: Control 17.2 (Establish and Maintain Contact Information for Reporting Security Incidents)
- NIST CSF 2.0: RS.MA-2 (Incidents are reported)
- **NIST SP 800-61 Rev. 2:** Recommends IR team structure
- **SANS Incident Response Plan:** Template includes IR team roles

---

### Question 9.3: Incident Response Testing

**Question Text:**
Does the organization test its incident response plan at least annually through exercises, simulations, or actual incident response?

**Response Options:**

- Annually or more frequently tested
- Every 2-3 years
- Rarely or never tested

**Impact Rating:** High (5)

**Foundational:** No (but increasingly required by insurers)

**Control Description:**

Incident response testing validates that the IR plan works and the IR team can execute it under pressure. Testing methods include:

**Testing Methods:**

- **Tabletop Exercises:** Discussion-based scenarios where IR team talks through incident response (Question 9.4)
- **Functional Exercises:** Hands-on simulations where IR team performs IR actions (disconnect systems, activate backups)
- **Full-Scale Exercises:** Realistic simulations involving entire organization (rarely conducted due to disruption)
- **Post-Incident Review:** After actual incidents, conduct lessons learned sessions; update IR plan

**Testing Scenarios:**

- **Ransomware:** Simulate ransomware attack; test system isolation, backup restoration, law enforcement engagement
- **Phishing/Credential Theft:** Simulate compromised credentials; test account lockout, password resets, MFA enforcement
- **Data Breach:** Simulate data exfiltration; test breach notification procedures, legal engagement, regulatory reporting

**Testing Outcomes:**

- **Identify Gaps:** Testing reveals IR plan gaps, outdated procedures, missing contact information
- **Build Muscle Memory:** Regular testing builds IR team confidence, improves execution speed
- **Update IR Plan:** Test findings drive IR plan updates (at least annually)

**Insurance Rationale (Universal):**

**IR Testing Requirement:**

- Many cyber insurers **increasingly require annual IR testing** (tabletop exercises minimum)
- Testing documentation may be requested during policy application/renewal
- Demonstrates IR plan is current, IR team is prepared

**Untested IR Plans Fail:**

- **40% of untested IR plans fail** during actual incidents (outdated contacts, missing procedures)
- Testing identifies failures before real incidents

**Faster Recovery:**

- Organizations with tested IR plans recover 3-5x faster than those with untested plans
- Faster recovery = lower breach costs = lower insurance claims

**Threat Landscape Justification:**

**IR Plan Staleness:**

- IR plans become outdated quickly (staff turnover, new systems, updated regulations)
- Annual testing ensures IR plan remains current

**High-Pressure Execution:**

- Incidents are high-pressure, chaotic environments
- Testing builds IR team confidence for executing under pressure

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Testing Schedule:** Annual tabletop exercise (summer preferred for K-12; less disruptive)
- **Scenario:** Ransomware attack during school year; test notification to families, backup restoration, continuity of learning
- **Participants:** IT staff, superintendent/president, communications, legal

**Healthcare:**

- **Testing Schedule:** Annual tabletop exercise minimum; some hospitals conduct quarterly
- **HIPAA Alignment:** Testing validates HIPAA breach notification procedures (60-day deadline)
- **Scenario:** Ransomware affecting EHR; test patient care continuity, breach notification, regulatory reporting (HHS)
- **Life-Safety Focus:** Include patient safety team in exercises affecting clinical systems

**Religious/Nonprofit:**

- **Testing Schedule:** Annual tabletop exercise
- **Scenario:** Donor database breach; test breach notification to donors, regulatory reporting (state privacy laws), communications
- **Limited Resources:** Simple tabletop exercises sufficient (discussion-based, 1-2 hours)

**General Organizations:**

- **Compliance Drivers:** SOC 2, ISO 27001, PCI DSS require IR testing
- **Enterprise Testing:** Quarterly tabletop exercises, annual functional tests, red team exercises
- **Industry-Specific Scenarios:** Financial fraud for finance, IP theft for technology, supply chain attacks for manufacturing

**Citations:**

- CIS Controls v8: Control 17.4 (Establish and Maintain an Incident Response Process)
- NIST CSF 2.0: RS.MA-1 (Incident response plan is executed)
- **NIST SP 800-61 Rev. 2:** Recommends IR testing
- **PCI DSS 4.0:** Requirement 12.10.6 - Test IR plan annually
- **SOC 2:** IR testing required for Trust Services Criteria

---

### Question 9.4: Tabletop Exercises

**Question Text:**
Does the organization conduct annual tabletop exercises to simulate incident response scenarios and validate team readiness?

**Response Options:**

- Annually or more frequently
- Every 2-3 years
- Rarely or never conducted

**Impact Rating:** Moderate (3)

**Foundational:** No (but subset of Question 9.3)

**Control Description:**

Tabletop exercises are discussion-based IR simulations where the IR team walks through incident scenarios. Effective tabletop exercises include:

**Tabletop Exercise Structure:**

- **Scenario:** Realistic incident scenario (ransomware, data breach, phishing)
- **Facilitator:** Moderator guides discussion, asks probing questions
- **Participants:** IR team members, key stakeholders (legal, communications, executives)
- **Discussion:** Team discusses: How would we detect this? How would we contain it? Who would we notify? What would we communicate?
- **Duration:** 1-3 hours typically

**Exercise Benefits:**

- **Low-Cost Testing:** Tabletop exercises are inexpensive (vs. functional tests requiring system disruption)
- **Identify Gaps:** Reveals missing procedures, outdated contacts, unclear roles
- **Build Relationships:** IR team members meet, understand each other's roles before actual incidents
- **Update IR Plan:** Exercise findings drive IR plan updates

**Common Scenarios:**

- **Ransomware:** Systems encrypted, backups tested, ransom demand received
- **Data Breach:** Customer/student/patient data exfiltrated; breach notification required
- **Business Email Compromise:** CFO's email compromised, wire transfer requested
- **Insider Threat:** Employee downloading sensitive data before departure

**Insurance Rationale (Universal):**

**Tabletop Exercise Requirement:**

- Many cyber insurers **require annual tabletop exercises**
- Exercise documentation (sign-in sheets, scenario, findings) may be requested during policy application/renewal

**Most Cost-Effective IR Testing:**

- Tabletop exercises are most accessible form of IR testing (low cost, low disruption)
- Demonstrates IR readiness without functional testing expense

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Schedule:** Annual tabletop (summer for K-12)
- **Scenario Example:** Ransomware encrypts SIS during finals week; test backup restoration, parent notification, grade recovery
- **Participants:** IT, superintendent/president, communications, legal, teaching staff lead

**Healthcare:**

- **Schedule:** Annual minimum
- **Scenario Example:** Ransomware encrypts EHR; test downtime procedures (paper charts), patient safety protocols, HIPAA breach notification
- **Participants:** IT, CISO, HIPAA Privacy Officer, patient safety, CEO, communications

**Religious/Nonprofit:**

- **Schedule:** Annual
- **Scenario Example:** Donor database breach; test donor notification, state attorney general notification, PR response
- **Participants:** IT or external IT provider, executive director, communications, legal

**General Organizations:**

- **Compliance:** PCI DSS, SOC 2 require IR testing; tabletop exercises satisfy requirement
- **Enterprise:** Quarterly tabletop exercises for different scenarios
- **External Facilitation:** Some organizations hire external facilitators (SANS, cyber insurance providers offer tabletop facilitation services)

**Citations:**

- CIS Controls v8: Control 17.4 (Establish and Maintain an Incident Response Process)
- **NIST SP 800-61 Rev. 2:** Recommends IR exercises
- **CISA Tabletop Exercise Packages:** Free scenarios for various sectors
- **PCI DSS 4.0:** Requirement 12.10.6 allows tabletop exercises for IR testing

---

### Question 9.5: Cyber Insurance Coverage

**Question Text:**
Does the organization maintain cyber liability insurance coverage?

**Response Options:**

- Yes - comprehensive cyber liability coverage with data breach, ransomware, business interruption
- Yes - limited cyber liability coverage
- No - no cyber insurance coverage

**Impact Rating:** Moderate (3)

**Foundational:** No (but increasingly recommended)

**Control Description:**

Cyber liability insurance provides financial protection against cyber incidents, covering breach response costs, ransomware payments (policy-dependent), business interruption, and legal defense. Cyber insurance policies typically include:

**Coverage Types:**

- **Data Breach Response:** Forensic investigation, breach notification costs, credit monitoring for affected individuals, legal counsel, public relations
- **Ransomware:** Ransom payment (policy-dependent), system restoration costs, business interruption
- **Business Interruption:** Lost revenue during downtime
- **Cyber Extortion:** Payments for ransomware, DDoS extortion
- **Legal Defense:** Defense costs for lawsuits, regulatory fines (coverage varies)
- **Third-Party Liability:** Lawsuits from customers, partners affected by breach

**Cyber Insurance Providers:**

- **Coalition, Chubb, AIG, Beazley, Corvus, Travelers, CNA:** Major cyber insurance carriers
- **Cyber Insurance Pools:** Some insurance pools (like CyberPools for education) offer cyber insurance to members

**Policy Requirements:**

- Cyber insurers require security controls for coverage (MFA, EDR, backups, training - see foundational questions)
- Annual security attestations, questionnaires required for renewal
- Failure to maintain required controls may void coverage

**Insurance Rationale (Universal):**

**Cyber Insurance is Risk Transfer:**

- Organizations cannot eliminate all cyber risk; cyber insurance transfers financial risk to insurers
- **Average breach cost:** $4.45M globally, $9.48M in healthcare (IBM Cost of Data Breach 2024)
- Cyber insurance covers costs beyond organizational budgets

**Incident Response Services:**

- Cyber insurance policies include **IR hotlines** (24/7 access to forensic experts, legal counsel)
- Insurers have pre-negotiated rates with top IR vendors
- Immediate access to IR services during incidents

**Board/Executive Governance:**

- Board of directors expect cyber risk management; cyber insurance demonstrates due diligence
- Fiduciary duty to protect organizational assets includes cyber insurance consideration

**Threat Landscape Justification:**

**Rising Breach Costs:**

- **Average breach cost increasing** annually ($4.45M globally in 2024, up from $4.24M in 2023)
- Cyber insurance protects against catastrophic financial losses

**Ransomware Financial Impact:**

- **Average ransom payment:** $1.54M (Sophos 2024)
- **Average ransomware recovery cost:** $2.73M including downtime (Sophos 2024)
- Cyber insurance covers ransom (policy-dependent) and recovery costs

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Cyber Insurance Pools:** Some education insurance pools (CyberPools, The Trust) offer cyber insurance to K-12 members
- **Commercial Policies:** Higher ed institutions often purchase standalone cyber insurance (Coalition, Chubb)
- **Coverage Needs:** Data breach notification (FERPA breaches), ransomware recovery, business interruption (learning disruption)
- **Affordability:** Cyber insurance increasingly affordable for education (pool pricing, education-specific policies)

**Healthcare:**

- **HIPAA Breach Costs:** Average healthcare breach cost $9.48M (IBM 2024) - highest of any sector
- **Regulatory Fines:** HHS Office for Civil Rights HIPAA fines can reach millions; some cyber policies cover regulatory defense
- **Patient Care Interruption:** Business interruption coverage critical for 24/7 healthcare operations
- **Required Coverage:** Some healthcare systems require cyber insurance for risk management

**Religious/Nonprofit:**

- **Donor Confidence:** Cyber insurance demonstrates responsible risk management to donors
- **Limited Budgets:** Nonprofits may prioritize cyber insurance over hiring additional IT security staff
- **Practical Implementation:** Affordable cyber insurance options available for small nonprofits ($1-5K annual premiums)

**General Organizations:**

- **Industry Requirements:** Some industries, contracts require cyber insurance (financial services, government contractors)
- **Investor/Lender Requirements:** Private equity investors, lenders may require cyber insurance
- **Coverage Limits:** Enterprise organizations carry $10M-$100M+ cyber insurance limits

**Citations:**

- **IBM Cost of Data Breach 2024:** Average breach cost $4.45M globally, $9.48M healthcare
- **Sophos State of Ransomware 2024:** Average ransom $1.54M, recovery cost $2.73M
- **Coalition, Chubb, AIG, Beazley, Corvus:** Major cyber insurance providers
- **National Association of Insurance Commissioners (NAIC):** Cyber insurance market data

---

### Question 9.6: Breach Notification Procedures

**Question Text:**
Does the organization have documented procedures for notifying affected individuals, regulators, and other stakeholders in the event of a data breach?

**Response Options:**

- Fully implemented - documented breach notification procedures, templates, legal review process
- Partially implemented - informal procedures, no templates
- Not implemented - no breach notification procedures

**Impact Rating:** High (5)

**Foundational:** No (but critical for compliance)

**Control Description:**

Breach notification procedures ensure the organization complies with legal requirements to notify affected individuals and regulators following data breaches. Effective procedures include:

**Notification Requirements:**

- **Affected Individuals:** Notify individuals whose personal data was compromised
- **Regulators:**

  - **HIPAA:** HHS Office for Civil Rights (60 days for breaches affecting 500+ individuals)
  - **State Privacy Laws:** State attorneys general (timelines vary: 30-90 days)
  - **FERPA:** Department of Education (for student data breaches)
  - **GDPR:** EU Data Protection Authorities (72 hours)

- **Other Stakeholders:** Law enforcement (FBI, Secret Service), credit bureaus (for large breaches), media (for large breaches), cyber insurer, legal counsel

**Notification Timeline:**

- **Immediate:** Engage IR team, cyber insurer, legal counsel
- **24-72 Hours:** Assess breach scope, determine notification requirements
- **30-90 Days:** Notify affected individuals, regulators (per legal requirements)

**Notification Content:**

- **What Happened:** Description of breach, how it occurred
- **What Data Was Compromised:** Types of personal data exposed
- **What Organization Is Doing:** Steps taken to contain breach, prevent future breaches
- **What Individuals Should Do:** Credit monitoring, password changes, fraud monitoring
- **Contact Information:** Where individuals can get more information

**Notification Methods:**

- **Individual Notification:** Email, postal mail, substitute notice (if contact information unavailable)
- **Regulatory Notification:** Online portals (HHS, state AG), formal letters
- **Public Notice:** Website posting, media notice for large breaches

**Insurance Rationale (Universal):**

**Breach Notification Legal Requirements:**

- All 50 US states have breach notification laws (timelines: 30-90 days)
- **HIPAA:** 60-day notification requirement for healthcare
- **GDPR:** 72-hour notification to EU Data Protection Authorities
- **Failure to notify = fines, lawsuits**

**Cyber Insurance Breach Response:**

- Cyber insurance policies cover breach notification costs:

  - **Legal counsel:** Review notification requirements, draft notifications
  - **Notification services:** Vendors that mail breach notifications, set up call centers
  - **Credit monitoring:** 1-2 years credit monitoring for affected individuals
- Cyber insurers provide breach notification templates, vendor recommendations

**Timely Notification Reduces Liability:**

- Timely, transparent breach notifications reduce regulatory fines, class action lawsuit damages
- Demonstrates good faith compliance effort

**Threat Landscape Justification:**

**Breach Notification Deadlines:**

- **HIPAA:** 60 days (HHS Office for Civil Rights enforcement)
- **GDPR:** 72 hours (€20M fines for non-compliance)
- **State Laws:** 30-90 days (state attorney general enforcement)
- Without documented procedures, organizations miss deadlines → fines, lawsuits

**Breach Notification Complexity:**

- Multi-state breaches require navigating 50 different state laws
- International breaches require GDPR compliance (72-hour deadline)
- Legal counsel essential for breach notification compliance

**Sector-Specific Context:**

**Education (K-12/Higher Ed):**

- **Notification Requirements:**

  - **FERPA:** Notify Department of Education of student data breaches
  - **State Privacy Laws:** Notify state attorney general (varies by state)
  - **Affected Families:** Notify families of students whose data was compromised
  - **COPPA (K-12):** Additional notification requirements for children under 13

- **Practical Implementation:**

  - Breach notification procedure in IR plan (Question 9.1)
  - Notification templates reviewed by legal counsel
  - Engage cyber insurer for breach notification services

- **Communication Challenges:** Communicating data breaches to parents requires clear, non-technical language

**Healthcare:**

- **Notification Requirements:**

  - **HIPAA Breach Notification Rule:** 60 days to notify HHS for breaches affecting 500+ individuals
  - **State Privacy Laws:** Notify state AG
  - **Affected Patients:** Notify patients whose PHI was compromised
  - **Media Notice:** Required for breaches affecting 500+ individuals

- **HIPAA Deadlines:**

  - **500+ Individuals:** Notify HHS, media within 60 days
  - **<500 Individuals:** Notify HHS annually
  - **Patients:** Notify without unreasonable delay (60 days)

- **Practical Implementation:**

  - HIPAA breach notification templates
  - HHS breach notification portal access
  - Vendor notification (if Business Associate causes breach)

**Religious/Nonprofit:**

- **Notification Requirements:**

  - **State Privacy Laws:** Notify state AG, affected individuals (30-90 day timelines)
  - **Donor Notification:** Notify donors whose data was compromised
  - **No Federal Religious Data Privacy Law:** State laws apply

- **Practical Implementation:**

  - State-by-state breach notification law review (legal counsel)
  - Donor notification templates emphasizing transparency, stewardship
  - Cyber insurance breach notification services

**General Organizations:**

- **Notification Requirements:**

  - **State Privacy Laws:** All 50 states (varying timelines)
  - **GDPR:** 72 hours to EU DPAs for EU data breaches
  - **CCPA (California):** California Attorney General notification
  - **Industry-Specific:** PCI DSS (payment card breaches), SOX (public companies)

- **Compliance Complexity:** Multi-state, international breaches require legal counsel
- **Cyber Insurance:** Breach notification services standard in cyber insurance policies

**Citations:**

- **HIPAA Breach Notification Rule:** 45 CFR § 164.404-164.408 (60-day notification)
- **GDPR Article 33:** 72-hour breach notification to Data Protection Authorities
- **All 50 US States:** Data breach notification laws (varying timelines)
- **FERPA:** Student data breach notification to Department of Education
- **CCPA (California):** Cal. Civ. Code § 1798.82 - Breach notification requirements
- **National Conference of State Legislatures (NCSL):** State breach notification law tracker

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

