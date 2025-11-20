# CyberPools Risk Assessment - Gap Analysis & Expansion Recommendations

## Executive Summary

This document analyzes the current 51-question assessment to identify coverage gaps and recommends 10 natural extensions that align with the existing framework. The recommendations focus on strengthening thin categories, addressing compliance requirements (FERPA), and filling critical security gaps without introducing overly complex technical controls.

**Current Assessment: 51 Questions across 9 Categories**

---

## Current Coverage Analysis

### Category Distribution

| Category | Current Questions | Coverage Assessment | Recommended Questions |
|----------|-------------------|---------------------|----------------------|
| **1.0 Inventory and Control of Assets** | 4 | ✅ Adequate | 4 (no change) |
| **2.0 Account Management** | 9 | ✅ Excellent | 9 (no change) |
| **3.0 Data Protection** | 3 | ⚠️ **Thin - Needs Expansion** | **7 (+4)** |
| **4.0 Secure Configuration** | 13 | ✅ Comprehensive | 13 (no change) |
| **5.0 Malware Defense** | 4 | ⚠️ Could be stronger | **6 (+2)** |
| **6.0 Data Recovery** | 4 | ⚠️ Missing DR plan | **5 (+1)** |
| **7.0 Security Awareness** | 3 | ⚠️ **Thin - Needs Expansion** | **6 (+3)** |
| **8.0 Vendor Management** | 5 | ✅ Adequate | 5 (no change) |
| **9.0 Incident Response** | 6 | ✅ Good | 6 (no change) |
| **TOTAL** | **51** | | **61 (+10)** |

---

## Detailed Gap Analysis

### Category 3.0 - Data Protection (CRITICAL GAP)

**Current State:** Only 3 questions
- 3.1: Data inventory
- 3.2: Separate admin accounts
- 3.3: Hard drive encryption

**Gaps Identified:**
1. ❌ No data classification framework
2. ❌ No data retention/disposal policies (FERPA compliance gap)
3. ❌ Encryption only covers "at rest" - missing "in transit"
4. ❌ No least privilege access controls
5. ❌ No questions about database encryption or application-level encryption

**Impact:** Schools hold massive amounts of sensitive data (student records, financial, health). Only 3 questions is insufficient.

---

### Category 7.0 - Security Awareness (CRITICAL GAP)

**Current State:** Only 3 questions
- 7.1: Security awareness program
- 7.2: Phishing simulation (quarterly)
- 7.3: Follow-up training

**Gaps Identified:**
1. ❌ No onboarding security training requirement
2. ❌ No role-specific training (IT, finance, executives)
3. ❌ No measurement of training effectiveness
4. ❌ Missing connection between account management procedures (2.8 onboarding) and security training

**Impact:** Human error is the #1 breach cause. Awareness program needs depth.

---

### Category 5.0 - Malware Defense (MODERATE GAP)

**Current State:** 4 questions covering DNS, email, anti-malware, EDR

**Gaps Identified:**
1. ❌ No shadow IT controls (unauthorized cloud storage)
2. ❌ No USB/removable media policies
3. ❌ Missing web content filtering beyond DNS

**Impact:** Shadow IT is rampant in education (teachers using personal Dropbox, Google Drive for student data).

---

### Category 6.0 - Data Recovery (MODERATE GAP)

**Current State:** 4 questions covering backups, frequency, air gap, testing

**Gaps Identified:**
1. ❌ No disaster recovery plan documentation
2. ❌ Testing backups (6.4) but no documented recovery procedures

**Impact:** Backups without documented recovery plans = incomplete resilience.

---

## Recommended 10 Questions for Expansion

### PRIORITY 1: Tier I Foundation Candidates (3 Questions)

These questions address critical gaps and should be considered for Tier I (foundation) status:

---

#### **Question 3.6 - Data Encryption (In Transit)**

**Category:** 3.0 Data Protection
**Question Number:** 3.6
**Impact Score:** 5 (High) - **Tier I Candidate**

**Question Text:**
"Are all systems that store or process sensitive data (student records, financial data, health information) encrypted both at rest and in transit?"

**Control Description:**
"Encryption protects sensitive data from unauthorized access during storage and transmission. At-rest encryption protects data on hard drives, databases, and backup systems. In-transit encryption (TLS/HTTPS) protects data as it moves across networks, including cloud applications, email, and web portals. Both are required to comply with data protection regulations and prevent data breaches."

**Why This Question:**
- Natural extension of question 3.3 (hard drive encryption)
- Addresses the full encryption lifecycle (at rest + in transit)
- Critical for schools transmitting student data to cloud SIS, learning platforms
- FERPA compliance requirement

**Example Implementations:**
- TLS 1.2+ for all web applications
- HTTPS enforcement for student/parent portals
- VPN or encrypted tunnels for data transmission
- Database encryption (SQL Server TDE, MySQL encryption)

---

#### **Question 6.5 - Disaster Recovery Plan**

**Category:** 6.0 Data Recovery
**Question Number:** 6.5
**Impact Score:** 5 (High) - **Tier I Candidate**

**Question Text:**
"Does the organization have a documented disaster recovery plan that includes recovery procedures, roles/responsibilities, and has been communicated to key stakeholders?"

**Control Description:**
"A disaster recovery plan (DRP) provides documented procedures to restore critical systems and data after a cyber incident, natural disaster, or system failure. The plan should define Recovery Time Objectives (RTO), Recovery Point Objectives (RPO), step-by-step recovery procedures, assigned responsibilities, and communication protocols. Regular testing and updates ensure the plan remains effective."

**Why This Question:**
- Natural follow-up to question 6.4 (backup testing)
- Testing backups without documented procedures = incomplete resilience
- Cyber insurance often requires documented DR plans
- Critical for business continuity

**Example Implementations:**
- Documented recovery procedures for critical systems
- Defined RTO/RPO for each system (e.g., SIS: 4 hours RTO)
- Assigned recovery team roles and responsibilities
- Annual DR plan review and tabletop exercise

---

#### **Question 3.5 - Data Retention and Disposal**

**Category:** 3.0 Data Protection
**Question Number:** 3.5
**Impact Score:** 5 (High) - **Tier I Candidate**

**Question Text:**
"Does the organization have documented data retention and disposal policies for sensitive information that comply with legal and regulatory requirements?"

**Control Description:**
"Data retention policies define how long different types of data must be kept (e.g., FERPA requires student records for 5 years, employment records for 7 years). Secure disposal procedures ensure data is properly destroyed when no longer needed using methods like secure deletion, degaussing, or physical destruction. Retaining data too long increases breach risk; disposing too early violates compliance."

**Why This Question:**
- Schools have specific FERPA retention requirements
- Missing from current assessment entirely
- Legal/compliance requirement for education sector
- Reduces data breach exposure by limiting data retention

**Example Implementations:**
- Written policy: Student records retained for 5 years post-graduation
- Secure disposal procedures (shredding, data wiping)
- Annual review of retention schedules
- Certificate of destruction for disposed storage media

---

### PRIORITY 2: Strengthen Weak Categories (4 Questions)

These questions fill critical gaps in thin categories:

---

#### **Question 3.7 - Least Privilege Access**

**Category:** 3.0 Data Protection
**Question Number:** 3.7
**Impact Score:** 5 (High)

**Question Text:**
"Does the organization restrict access to sensitive data based on job role and business need (principle of least privilege)?"

**Control Description:**
"The principle of least privilege ensures users only have access to the data and systems necessary for their job functions. This limits the impact of compromised accounts and prevents unauthorized data access. Role-based access control (RBAC) should be implemented for student information systems, financial systems, and other sensitive data repositories."

**Why This Question:**
- Natural follow-up to question 3.2 (separate admin accounts)
- Extends access control philosophy to data access
- Prevents over-privileged users (e.g., teachers accessing all student records)
- Common audit finding in education

**Example Implementations:**
- Teachers only access their own student rosters
- Finance staff cannot access student disciplinary records
- HR has separate access controls from IT
- Regular access reviews (quarterly)

---

#### **Question 7.5 - Onboarding Security Training**

**Category:** 7.0 Security Awareness
**Question Number:** 7.5
**Impact Score:** 3 (Moderate)

**Question Text:**
"Does the organization conduct security awareness training for new employees during onboarding?"

**Control Description:**
"New employees should receive security awareness training during their first week, covering topics like password requirements, phishing identification, data handling policies, acceptable use policies, and how to report security incidents. This establishes a security-first culture from day one and ensures all employees receive baseline security knowledge."

**Why This Question:**
- Complements question 2.8 (onboarding procedures) with security component
- First impressions matter - sets security culture expectations
- New employees are high-risk targets (unfamiliar with policies)
- Natural gap in current awareness questions

**Example Implementations:**
- Required security training module during first week
- Review of acceptable use policy
- Password creation and MFA enrollment
- "Who to call" for security incidents

---

#### **Question 5.5 - Shadow IT Controls**

**Category:** 5.0 Malware Defense
**Question Number:** 5.5
**Impact Score:** 3 (Moderate)

**Question Text:**
"Does the organization have policies and controls to prevent the use of unauthorized cloud storage or file-sharing services (e.g., blocking or monitoring personal Dropbox, Google Drive, OneDrive accounts)?"

**Control Description:**
"Shadow IT refers to unauthorized cloud services used by employees without IT approval. This creates data governance risks, compliance violations (FERPA), and security gaps. Organizations should maintain an approved list of cloud services, block high-risk personal cloud storage, and educate users on proper data handling. DLP or cloud access security broker (CASB) tools can detect and prevent unauthorized uploads."

**Why This Question:**
- HUGE issue in education - teachers using personal cloud accounts
- Student data ends up on personal Google Drive, Dropbox
- FERPA violation risk
- Missing from current assessment entirely

**Example Implementations:**
- Block personal Dropbox/Box/Google Drive at firewall
- Approved institutional cloud storage (Google Workspace for Education)
- Policy defining approved vs. prohibited services
- Education on FERPA requirements

---

#### **Question 3.4 - Data Classification**

**Category:** 3.0 Data Protection
**Question Number:** 3.4
**Impact Score:** 3 (Moderate)

**Question Text:**
"Does the organization classify data based on sensitivity levels (e.g., public, internal, confidential, restricted)?"

**Control Description:**
"Data classification organizes information into categories based on sensitivity and regulatory requirements. A typical framework includes: Public (can be shared freely), Internal (business use only), Confidential (sensitive business data), and Restricted (highly sensitive - student records, SSNs, health data). Classification drives security controls - restricted data requires encryption, access controls, and audit logging."

**Why This Question:**
- Foundation for all other data protection controls
- You ask about data inventory (3.1) but not classification
- Enables risk-based security (protect what matters most)
- Required for compliance frameworks

**Example Implementations:**
- Four-tier classification: Public, Internal, Confidential, Restricted
- Student records = Restricted
- Lesson plans = Internal
- Published newsletters = Public
- Classification labels on documents/systems

---

### PRIORITY 3: Nice to Have (3 Questions)

These questions add depth but are lower priority:

---

#### **Question 7.4 - Role-Specific Security Training**

**Category:** 7.0 Security Awareness
**Question Number:** 7.4
**Impact Score:** 3 (Moderate)

**Question Text:**
"Does the organization provide role-specific security training (e.g., additional training for IT staff, finance staff, executives)?"

**Control Description:**
"While all employees need baseline security awareness, certain roles require specialized training based on their elevated risk or privileged access. IT staff should receive training on secure configuration and vulnerability management. Finance staff need training on business email compromise and wire fraud. Executives need training on CEO fraud and social engineering targeting leadership."

**Why This Question:**
- Extends general awareness (7.1) to targeted training
- High-risk roles need specialized knowledge
- Reflects real-world attack patterns (BEC targets finance)

**Example Implementations:**
- IT staff: Advanced phishing, secure coding practices
- Finance: Wire fraud, invoice verification procedures
- Executives: CEO fraud, social engineering awareness
- Annual role-based training updates

---

#### **Question 5.6 - Removable Media Controls**

**Category:** 5.0 Malware Defense
**Question Number:** 5.6
**Impact Score:** 3 (Moderate)

**Question Text:**
"Does the organization block or restrict the use of removable media (USB drives, external hard drives) on endpoints that process sensitive data?"

**Control Description:**
"Removable media (USB drives) present two major risks: malware delivery and data exfiltration. USB-based malware can bypass network security controls. Users can copy sensitive data to USB drives and remove it from the organization. Controls include: disabling USB ports via group policy, using device control software to whitelist approved devices, or requiring encrypted USB drives for authorized use."

**Why This Question:**
- Complements malware defense stack (5.1-5.4)
- USB malware is still a threat vector
- Data exfiltration risk (employee copying student records)

**Example Implementations:**
- USB ports disabled via Group Policy
- Exception process for approved encrypted USB drives
- Device control software (Ivanti, Symantec)
- Policy prohibiting personal USB devices

---

#### **Question 8.6 - Vendor Access Management**

**Category:** 8.0 Vendor Management
**Question Number:** 8.6
**Impact Score:** 3 (Moderate)

**Question Text:**
"Does the organization review and approve vendor access to systems/data and promptly revoke access when vendor contracts end or services are no longer needed?"

**Control Description:**
"Third-party vendors often require temporary access to systems for support, implementation, or maintenance. This access should be: approved before granting, limited to minimum necessary privileges, time-bound with expiration dates, and revoked immediately when the vendor relationship ends. Regular vendor access reviews (quarterly) ensure no orphaned accounts remain active."

**Why This Question:**
- Current vendor questions (8.1-8.5) focus on payment fraud
- Missing vendor access management entirely
- Third-party access is a major breach vector
- Supply chain security consideration

**Example Implementations:**
- Vendor access request/approval process
- Separate vendor VPN or remote access portal
- 90-day access reviews
- Automatic access revocation on contract end
- Audit logging of vendor activity

---

## Implementation Priority Matrix

### Phase 1: Immediate (Next Assessment Cycle)
**Goal:** Fill critical gaps in Data Protection and add Tier I candidates

| Question | Category | Priority | Tier I? | Why Now |
|----------|----------|----------|---------|---------|
| **3.6** | Data Protection | Critical | YES | Encryption in transit = major gap |
| **6.5** | Data Recovery | Critical | YES | DR plan = insurance requirement |
| **3.5** | Data Protection | Critical | YES | FERPA compliance requirement |
| **7.5** | Security Awareness | High | NO | Links to existing onboarding (2.8) |

**Impact:** Adds 4 questions → Total: 55 questions (3 new Tier I questions)

---

### Phase 2: Near-Term (Within 6 Months)
**Goal:** Strengthen thin categories

| Question | Category | Priority | Tier I? | Why Phase 2 |
|----------|----------|----------|---------|-------------|
| **3.7** | Data Protection | High | NO | Least privilege access |
| **5.5** | Malware Defense | High | NO | Shadow IT = huge education issue |
| **3.4** | Data Protection | Medium | NO | Foundation for data security |

**Impact:** Adds 3 questions → Total: 58 questions

---

### Phase 3: Future Enhancement (12+ Months)
**Goal:** Round out assessment with specialized questions

| Question | Category | Priority | Tier I? | Why Phase 3 |
|----------|----------|----------|---------|-------------|
| **7.4** | Security Awareness | Medium | NO | Nice to have - role-specific training |
| **5.6** | Malware Defense | Medium | NO | USB controls - lower priority |
| **8.6** | Vendor Management | Medium | NO | Vendor access - can wait |

**Impact:** Adds 3 questions → Total: 61 questions

---

## Revised Tier I Foundation Questions

**Current Tier I:** 12 questions

**Proposed Additions (Phase 1):**
- 3.5 - Data retention and disposal (FERPA compliance)
- 3.6 - Data encryption at rest and in transit
- 6.5 - Documented disaster recovery plan

**New Tier I Total:** 15 questions (25% increase)

**Revised Tier II Formula:**
```
Tier II = (80% × Tier I Score) + (20% × Comprehensive Score)
```
Still maintains 80/20 weighting, but Tier I now includes 15 questions instead of 12.

---

## Category Coverage After Full Implementation

### Final Distribution (61 Questions)

| Category | Current | Phase 1 | Phase 2 | Phase 3 | Final |
|----------|---------|---------|---------|---------|-------|
| 1.0 Inventory | 4 | 4 | 4 | 4 | **4** |
| 2.0 Account Mgmt | 9 | 9 | 9 | 9 | **9** |
| 3.0 Data Protection | 3 | 6 | 8 | 8 | **8** ⬆️ |
| 4.0 Secure Config | 13 | 13 | 13 | 13 | **13** |
| 5.0 Malware Defense | 4 | 4 | 5 | 6 | **6** ⬆️ |
| 6.0 Data Recovery | 4 | 5 | 5 | 5 | **5** ⬆️ |
| 7.0 Security Awareness | 3 | 4 | 4 | 5 | **5** ⬆️ |
| 8.0 Vendor Mgmt | 5 | 5 | 5 | 6 | **6** ⬆️ |
| 9.0 Incident Response | 6 | 6 | 6 | 6 | **6** |
| **TOTAL** | **51** | **55** | **58** | **61** | **61** |

**Result:** More balanced coverage across all categories, no category below 4 questions.

---

## Benefits of These Additions

### 1. Compliance Alignment
✅ Addresses FERPA requirements (retention, disposal, encryption)
✅ Fills insurance requirement gaps (DR plan, encryption in transit)
✅ Regulatory best practices (data classification, least privilege)

### 2. Education Sector Relevance
✅ Shadow IT (teachers using personal cloud storage)
✅ Student data protection emphasis
✅ Role-based training (teachers vs. IT vs. admin)

### 3. Natural Extensions
✅ Extends existing questions rather than introducing new concepts
✅ Maintains consistent difficulty level
✅ Fits within existing 9-category framework

### 4. Maintains Simplicity
✅ No advanced technical tools required (SIEM, PAM, DLP)
✅ Policy and process focused
✅ Achievable for small to mid-sized organizations

---

## Implementation Considerations

### Question Development Checklist
For each new question:
- [ ] Assign impact score (1, 3, or 5)
- [ ] Write control description (how to implement)
- [ ] Determine Tier I eligibility
- [ ] Map to category (772120000-772120008)
- [ ] Add to question_mapping.json
- [ ] Create response options (0/1/3/5)
- [ ] Develop scoring formula
- [ ] Write guidance/examples

### Assessment Length Concerns
**Current:** 51 questions (~45 minutes)
**Phase 1:** 55 questions (~50 minutes) - acceptable increase
**Phase 3:** 61 questions (~55 minutes) - still reasonable

**Mitigation:** Consider retiring weak/outdated questions if length becomes an issue.

---

## Questions to Retire (Optional)

If assessment length is a concern after additions, consider retiring:

1. **9.6** - "Outside of CBS Pool, does organization purchase cyber insurance?"
   - Informational only, not actionable
   - Already excluded from Tier I

2. **4.13** - "Does organization change wireless PSKs annually?"
   - Very specific, low impact
   - Most orgs moving to 802.1X (4.12)

3. **8.3** - "Does organization verify vendor bank accounts?"
   - Payment fraud focus, not cybersecurity
   - Could consolidate with 8.4

**Potential:** Remove 2-3 low-value questions to offset additions.

---

## Next Steps

### Immediate Actions
1. **Review & Approve** Phase 1 questions (3.5, 3.6, 6.5, 7.5)
2. **Draft full question text** with control descriptions
3. **Determine Tier I status** for new questions
4. **Update question_mapping.json** with new questions
5. **Test with pilot members** before full rollout

### Documentation Updates
- Update boilerplate text to reflect expanded assessment
- Revise methodology section (55 questions, 15 Tier I questions)
- Update report templates for new category coverage
- Create member communication about assessment enhancements

### Timeline
- **Month 1:** Finalize Phase 1 questions, update mappings
- **Month 2:** Test with 2-3 pilot members, gather feedback
- **Month 3:** Roll out to all members with updated assessment
- **Month 6:** Evaluate Phase 2 additions based on Phase 1 results

---

## Conclusion

The recommended 10 questions address critical gaps in the current assessment, particularly in:
- **Data Protection** (3 questions → 8 questions)
- **Security Awareness** (3 questions → 5 questions)
- **Data Recovery** (4 questions → 5 questions)

All additions are natural extensions of existing questions, maintain the current framework's simplicity, and are highly relevant to the education sector. Phase 1 implementation adds 4 questions including 3 new Tier I foundation requirements, strengthening the assessment's alignment with cyber insurance requirements and FERPA compliance.

**Recommendation:** Implement Phase 1 immediately (4 questions), evaluate results, then proceed with Phase 2 and 3 based on member feedback and organizational capacity.
