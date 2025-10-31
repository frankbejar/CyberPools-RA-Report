---
title: Category 7 - Security Awareness Training and Education
tags:
  - Category 7
  - Foundational
  - New
  - High Impact
  - Moderate Impact
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

