---
title: Framework Mapping
tags:
  - Reference
  - Framework Alignment
---

# Framework Mapping

## NIST Cybersecurity Framework (CSF) 2.0

All questions in this assessment map to NIST CSF 2.0 functions:

### Govern (GV)
- Oversight and accountability for cybersecurity risk management
- Questions: 7.4 (AI AUP), 3.6 (Data Classification)

### Identify (ID)
- Asset management, risk assessment, supply chain
- Questions: Category 1 (Asset Inventory), Category 8 (Vendor Risk)

### Protect (PR)
- Safeguards to ensure delivery of services
- Questions: Category 2 (Access Control), Category 3 (Data Protection), Category 4 (Secure Configuration)

### Detect (DE)
- Timely discovery of cybersecurity events
- Questions: 4.14 (SIEM), 5.4 (EDR), 9.7 (MTTD/MTTR)

### Respond (RS)
- Action regarding detected cybersecurity incidents
- Questions: Category 9 (Incident Response)

### Recover (RC)
- Restoration of capabilities impaired by incidents
- Questions: Category 6 (Data Recovery, Business Continuity, DR)

---

## CIS Controls v8

All questions map to CIS Critical Security Controls:

### Implementation Group 1 (IG1) - Essential Cyber Hygiene
- Basic controls for all organizations
- Examples: Asset inventory (1.1-1.3), Access control basics (2.2), Backups (6.1-6.2)

### Implementation Group 2 (IG2) - Enterprise Security
- Controls for organizations with IT security staff
- Examples: MFA (2.3-2.6), Vulnerability scanning (4.7), Security awareness (7.2-7.3)

### Implementation Group 3 (IG3) - Advanced Security
- Controls for mature security programs
- Examples: PAM (3.5), SIEM (4.14), Vendor risk management (Category 8)

---

## NIST AI Risk Management Framework (AI RMF)

AI-related questions align with NIST AI RMF:

### Govern
- **7.4: AI Acceptable Use Policy** - AI governance and accountability

### Map
- **8.8: AI Tool Vetting** - Understanding AI system context and risks

### Measure
- AI tool security assessments, compliance verification

### Manage
- Implementing AI policies, technical controls (DLP, monitoring)

---

## Trust Requirements for Education

The 12 foundational questions (existing) map to 7 simplified requirements from The Trust insurance pool:

1. **End-of-Life Software** → Question 1.4
2. **Multi-Factor Authentication** → Questions 2.3, 2.4, 2.5, 2.6
3. **Patch Management** → Question 4.3
4. **Vulnerability Scanning** → Question 4.7
5. **EDR/Antivirus** → Question 5.4
6. **Backups + Testing** → Questions 6.3, 6.4
7. **Phishing + Training** → Questions 7.2, 7.3

---

## Regulatory Compliance Mapping

### HIPAA (Healthcare)
- Security Rule requirements: Training (7.3), IR procedures (9.1), Contingency plan (6.5-6.6), BAAs (8.3)
- Breach Notification Rule: Procedures (9.6), timelines (60 days)

### FERPA (Education)
- Student data privacy: Vendor agreements (8.3), AI tools (7.4, 8.8), breach notification (9.6)

### GDPR (International)
- Data protection: Encryption (3.2-3.3), DPAs (8.3), 72-hour breach notification (9.6)
- AI governance: AI Act compliance (7.4, 8.8)

### PCI DSS 4.0 (Payment Cards)
- Training (7.3), IR plan (9.1-9.3), Vendor management (8.1-8.5), MFA (2.3-2.6)

### State Privacy Laws (All)
- Breach notification (9.6), vendor contracts (8.3), security controls (all categories)
