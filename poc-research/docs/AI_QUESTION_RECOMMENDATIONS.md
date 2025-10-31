# AI-Related Cybersecurity Questions for CyberPools K-12 Assessment

**Analysis Date:** October 30, 2025
**Purpose:** Identify questions from ASSESSMENT_EXPANSION_RESEARCH.md that can be traded for AI-related cybersecurity questions
**Methodology:** Combined GRC expert analysis and cybersecurity risk assessment perspectives

---

## Executive Summary

Based on comprehensive research of the 2024-2025 AI threat landscape, insurance market trends, and K-12 education sector AI adoption, this analysis recommends **trading 2-3 lower-priority questions** from the 11 proposed expansion questions for **2 AI-specific cybersecurity questions**.

### Key Findings

**AI Threat Landscape (2024-2025):**
- **67.4% of phishing attacks** now utilize AI technology
- **442% increase** in AI-powered voice phishing (vishing) attacks
- **84% increase** in infostealer delivery via phishing emails (IBM X-Force 2025)
- **Only 24%** of generative AI projects are properly secured
- AI-automated phishing achieves **54% click-through rate** vs. 12% for non-AI phishing

**K-12 AI Adoption Crisis:**
- **80% of K-12 districts** have generative AI initiatives underway
- **43% of districts** lack formal AI policies or guidance
- **FERPA limitations:** Does not cover AI-generated data (predictive analytics, behavioral insights)
- Teachers experimenting with free AI chatbots **without district approval** in many cases
- Students pasting essays into public AI tools, potentially violating COPPA/FERPA

**Insurance Market Reality Check:**
- **NO AI-specific requirements** from major carriers (Coalition, Chubb, Corvus) in 2025
- AI coverage exists for AI-related incidents, but **governance is not yet mandated**
- This is a **forward-looking** recommendation, not current insurance pressure
- NIST AI Risk Management Framework is **voluntary** (released 2023, updated 2024)

### Strategic Recommendation

**Trade these 3 questions for 2 AI questions:**
1. **Question 5.6: API Security Controls** (LOW-MODERATE insurance pressure, too technical for most K-12)
2. **Question 3.6: Data Classification and Handling** (NO immediate insurance pressure, governance maturity)
3. **Question 2.10: Privileged Session Monitoring** (Overlaps with 3.5 PAM Platform)

**Add these 2 AI questions:**
1. **Question 7.4: AI Acceptable Use Policy and Governance** (Category 7 - Security Awareness)
2. **Question 8.8: AI Tool Privacy and Security Assessment** (Category 8 - Vendor Management)

---

## Questions Recommended for Trading (Deprioritization)

### 1. Question 5.6: API Security Controls ❌ TRADE THIS

**Why Trade This Question:**

**Low Insurance Pressure:**
- Marked as "LOW-MODERATE" emerging threat in original research
- "Not yet universal insurance requirement for K-12"
- API security is more relevant for organizations with extensive API usage

**Limited K-12 Applicability:**
- Most K-12 schools **do not develop APIs** directly
- Schools consume APIs from vendors (SIS, LMS, Google/Microsoft) but don't control API security
- Too technical for typical K-12 IT staff (OAuth 2.0, RBAC, ABAC, rate limiting, OWASP API Top 10)
- Vendor API security is covered by enhanced vendor questions (8.6, 8.7)

**Risk Assessment:**
- While API vulnerabilities cost $2.5B in 2024, this is enterprise-wide data
- K-12 schools face API risks primarily through **vendor-provided APIs**, not self-developed APIs
- Question 8.6 (Vendor Security Certifications) addresses vendor API security more appropriately

**Verdict:** This question is valuable for enterprises but not practical or high-priority for K-12 environments in 2025-2026.

---

### 2. Question 3.6: Data Classification and Handling Procedures ⚠️ CONSIDER TRADING

**Why Consider Trading This Question:**

**No Immediate Insurance Pressure:**
- Marked as "MODERATE" insurance pressure (not HIGH)
- More of a governance maturity indicator than insurance requirement
- Not explicitly mentioned in Coalition, Chubb, or Corvus application requirements

**Implementation Complexity for K-12:**
- Requires significant policy development, staff training, and technical enforcement (DLP)
- Many K-12 schools lack dedicated compliance or privacy officers
- Smaller districts (under 2,500 students) unlikely to have resources for formal classification programs

**Overlapping Coverage:**
- **Question 3.1:** Data inventory (existing) asks what data the organization holds
- **Question 3.4:** Data retention policy (recently added) addresses retention/destruction
- Data classification is the "next level" maturity beyond these, but not immediately critical

**K-12 Context:**
- Schools already understand FERPA-protected data vs. directory information (basic classification)
- Formal classification schemes (Public/Internal/Confidential/Restricted) add administrative burden

**Counterargument for Keeping:**
- State privacy laws (8 new in 2025) increasingly require data protection proportionate to sensitivity
- Data classification supports Questions 3.1 and 3.4 by providing governance framework
- NIST CSF 2.0 (ID.AM-5) recommends resource prioritization based on classification

**Verdict:** This is a "nice-to-have" governance control but not critical for 2025-2026 insurance or threat landscape. Consider trading if AI questions are prioritized.

---

### 3. Question 2.10: Privileged Session Monitoring ⚠️ CONSIDER TRADING

**Why Consider Trading This Question:**

**Overlapping Coverage with Question 3.5 (PAM Platform):**
- Question 3.5 asks about PAM implementation including "session monitoring/recording"
- Question 3.5 control description explicitly includes: "screen recording, keystroke logging, ability to pause/terminate sessions"
- **This question feels redundant** if PAM is already covered comprehensively in 3.5

**Not Foundational (Lower Priority):**
- Marked as "NO - Comprehensive maturity indicator"
- PAM Platform (3.5) is marked as "Foundational - Insurance Critical"
- If resources are limited, **PAM platform implementation** is more critical than standalone session monitoring

**Moderate Insurance Pressure:**
- Insurance pressure rating is "MODERATE" (not HIGH)
- Primarily valuable as component of PAM solution, which is already covered

**K-12 Context:**
- Many PAM solutions for K-12 (Delinea, BeyondTrust, ManageEngine) include session monitoring
- Asking separate question may create confusion about PAM scope
- Better to ensure comprehensive PAM implementation (3.5) than separate session monitoring

**Counterargument for Keeping:**
- Session monitoring can be achieved without full PAM via Windows Event Logging, Linux auditd
- Provides granular forensic capabilities for insider threat detection
- 88% of breaches involve stolen credentials (Verizon DBIR), monitoring detects misuse

**Verdict:** If Question 3.5 (PAM Platform) is comprehensive enough, this question adds limited additional value. Consider trading for higher-priority AI risks.

---

## Proposed AI-Related Cybersecurity Questions

### Question 7.4: AI Acceptable Use Policy and Governance

**Category:** 7 - Security Awareness Training and Education
**Alternative Category:** 1 - Asset and Inventory Management (if treating AI as technology asset)

**Question Text:**

Has the organization established an Artificial Intelligence (AI) Acceptable Use Policy that defines approved AI tools, prohibited uses, data privacy requirements, and staff/student responsibilities when using AI technologies (ChatGPT, Google Gemini, Microsoft Copilot, AI-enabled EdTech platforms)?

**Impact Rating:** High (5)

**Foundational Question:** 🔑 YES - Critical governance gap

**Control Description:**

An AI Acceptable Use Policy (AUP) provides governance framework for generative AI and AI-enabled tools used by staff and students. The policy should address:

**Approved AI Tools:**
- District-vetted AI platforms with FERPA-compliant data handling (e.g., Microsoft Copilot for Education, Google Gemini for Education)
- EdTech platforms with embedded AI features (tutoring systems, grading assistants)
- Prohibition of unapproved public AI tools for sensitive data processing

**Prohibited Uses:**
- Inputting student PII, FERPA-protected education records, or confidential data into public AI chatbots
- Using AI for high-stakes decisions (student discipline, special education placement) without human oversight
- Bypassing content filters or using AI for academic dishonesty
- Generating deepfake content or impersonating individuals

**Data Privacy Requirements:**
- Training data restrictions (student work must not be used for AI model training)
- Data retention and deletion policies for AI tool vendors
- Consent requirements for AI processing of student data
- Integration with existing vendor management policies

**Staff and Student Responsibilities:**
- Training on approved AI tools and policy compliance
- Reporting requirements for unauthorized AI tool discovery
- Guidance on AI-assisted work (proper attribution, verification of AI outputs)
- Acceptable AI use in instruction, assessment, and administrative functions

**Governance Structure:**
- AI oversight committee or designated AI governance role
- Regular policy review aligned with NIST AI Risk Management Framework (Govern function)
- Incident response procedures for AI-related data breaches or misuse
- Integration with existing AUPs and technology usage policies

**Insurance Rationale:**

While **cyber insurers do not yet mandate AI governance policies in 2025**, this is a **forward-looking control** addressing rapidly emerging risks. Key insurance considerations:

**Emerging Coverage and Risk Assessment:**
- Coalition and other carriers now offer **"Affirmative AI Insurance"** for AI-related cybersecurity events
- Underwriters are beginning to ask about AI governance during application processes
- Organizations demonstrating AI risk management may receive favorable consideration as market matures

**FERPA and Privacy Law Compliance:**
- Student data exposure via AI tools creates **FERPA violation risk** and breach notification obligations
- State privacy laws increasingly require documented policies for automated decision-making and AI processing
- Breach notification costs and regulatory fines are covered expenses in cyber policies

**Liability Risk Reduction:**
- Shadow AI adoption (staff/students using unapproved tools) creates data exposure blind spots
- Insurers favor organizations with documented policies reducing likelihood of incidents
- AI-related incidents (student data training AI models, deepfake creation) may fall under cyber or E&O coverage

**Threat Landscape Justification:**

**IBM X-Force Threat Intelligence Index 2025:**
- Threat actors adopt generative AI "like an intern or assistant" to write phishing emails, clone websites, generate malicious code
- **84% increase** in infostealer-delivering phishing emails, with AI accelerating attack sophistication
- Traditional defenses (grammar checks, stylistic analysis) **no longer work** against AI-generated phishing
- "Only **24% of generative AI projects are secured**" - organizations adopt AI faster than security controls

**AI-Powered Phishing Statistics (2024-2025):**
- **67.4% of phishing attacks** utilized AI technology in 2024
- AI-automated phishing achieves **54% click-through rate** vs. 12% for non-AI lures
- **442% increase** in AI-powered voice phishing (vishing) between H1 and H2 2024
- **30% of organizations** fell victim to AI-enhanced voice scams in 2024
- Deepfake scams cost organizations average of **$25 million** in notable 2024 incidents

**K-12 Context:**

**Widespread AI Adoption Without Governance:**
- **80% of K-12 districts** have generative AI initiatives underway
- **43% of districts** lack formal AI policies or guidance
- Teachers experimenting with ChatGPT, Gemini, Copilot **without district approval** in many cases
- Students using AI for homework assistance, often pasting essays into public tools

**FERPA Compliance Gaps:**
- FERPA (signed 1974) **does not cover AI-generated data** such as:
  - Predictive performance insights from AI tutoring systems
  - Behavioral analytics generated by AI monitoring tools
  - Student profiles created by AI-powered EdTech platforms
- Many AI tools **not inherently FERPA-compliant** and don't disclose data storage/usage practices
- If teacher pastes student essay into ChatGPT, that data may enter commercial model training loop **without consent**

**Shadow AI Risks:**
- Free AI tools (ChatGPT, Google Gemini, Meta AI) used by staff for lesson planning, grading feedback
- Risk of student PII, IEP information, discipline records being inputted into unvetted tools
- District IT departments often unaware of AI tool proliferation across schools

**Threat Scenarios Specific to K-12:**
- **Superintendent Deepfake Impersonation:** AI voice cloning used for wire fraud (similar to existing BEC attacks)
- **Student Data Training:** Student essays, assessments used to train commercial AI models without consent
- **AI-Generated Misinformation:** Students or staff using AI to create fake communications appearing to be from school officials
- **Credential Harvesting:** AI-generated phishing targeting teachers via realistic parent/administrator impersonation

**Citations:**

**NIST AI Risk Management Framework:**
- NIST AI RMF 1.0 (January 2023): https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF 2.0 (February 2024) with enhanced governance guidance
- NIST Generative AI Profile (July 2024): Addresses unique risks from generative AI systems
- **Govern Function:** "Establishes organizational policies and accountability structures for AI risk management"

**K-12 AI Governance Frameworks:**
- **CoSN (Consortium for School Networking):** AI guidance for K-12 education leaders on ethical AI integration
  - URL: https://www.cosn.org/ai/
  - Partnership with AESA, SETDA, AASA on Building Capacity for Generative AI Project
- **TeachAI + Code.org + CoSN:** AI Guidance for Schools Toolkit with seven principles
  - URL: https://www.aiforeducation.io/ai-resources/state-ai-guidance
- **Council of Great City Schools + CoSN:** K-12 Generative AI Readiness Checklist

**K-12 AI Privacy Research:**
- Chalkbeat (2024): "AI tools used by teachers can put student privacy and data at risk"
  - URL: https://www.chalkbeat.org/2024/12/13/ai-tools-used-by-teachers-can-put-student-privacy-and-data-at-risk/
  - Finding: "43% of districts lack AI policies; 80% have AI initiatives"
- Safe AI for Children (2024): "AI Risks for K-12 Students: Lessons from U.S. to Protect Children Globally"
  - URL: https://www.safeaiforchildren.org/ai-risks-k12-ferpa-coppa/
  - Finding: "FERPA doesn't extend to AI-generated data like predictive analytics"
- Control Alt Achieve (2024): "AI Tools and Student Data Privacy"
  - URL: https://www.controlaltachieve.com/2024/03/ai-tools-and-student-data-privacy.html
  - Finding: "Many free AI tools continue learning from user prompts; student data may enter training loops"

**Threat Intelligence on AI-Enabled Attacks:**
- **IBM X-Force 2025 Threat Intelligence Index:**
  - URL: https://www.ibm.com/reports/threat-intelligence
  - "Threat actors adopt generative AI for phishing, website cloning, malware generation"
  - "84% increase in infostealer-delivering emails"
  - "Only 24% of generative AI projects secured"
- **CybelAngel (2025):** "The Rise of AI-Powered Phishing"
  - URL: https://cybelangel.com/blog/rise-ai-phishing/
  - "67.4% of phishing attacks use AI; 82.6% of phishing emails use AI technology"
  - "AI-automated phishing: 54% click-through rate vs. 12% for non-AI"
- **Tech Advisors (2025):** "AI Cyber Attack Statistics 2025"
  - URL: https://tech-adv.com/blog/ai-cyber-attack-statistics/
  - "442% increase in vishing attacks H1-H2 2024"
  - "30% of organizations fell victim to AI voice scams in 2024"
  - "Deepfake scam cost multinational firm $25 million in 2024"

**Insurance and Compliance:**
- **American Bar Association (2025):** "Cyber and Data Privacy Insurance in 2025"
  - URL: https://www.americanbar.org/groups/tort_trial_insurance_practice/resources/brief/2025-winter/cyber-data-privacy-insurance-2025/
  - "Model hallucinations and AI-driven fraud propel new coverage requirements"
  - Coalition includes "Affirmative AI Insurance" for AI-related cybersecurity events
- **State Privacy Laws:** Eight new state privacy laws in 2025 requiring data protection for AI processing
- **FERPA Limitations:** Student privacy regulations predate AI era (1974), lack coverage for AI-generated analytics

**Framework Alignment:**
- NIST Cybersecurity Framework 2.0: GV.PO (Governance - Policies) - "Organizational policies are established, communicated, and enforced"
- CIS Controls v8: Control 1.1 (Establish and Maintain Detailed Enterprise Asset Inventory) - extends to AI tools as technology assets
- ISO/IEC 42001 (AI Management System): International standard for AI governance (published 2023)

---

### Question 8.8: AI Tool Privacy and Security Vetting

**Category:** 8 - Third-Party and Vendor Risk Management
**Alternative Category:** 3 - Data Protection and Privacy

**Question Text:**

Does the organization assess privacy and security risks before deploying AI tools or EdTech platforms with AI features, including verification of FERPA/COPPA compliance, data usage restrictions (no student data for AI model training), and data processing agreements with AI vendors?

**Impact Rating:** High (5)

**Foundational Question:** 🔑 YES - Critical privacy compliance gap

**Control Description:**

AI tool privacy and security vetting extends third-party risk management (Category 8) to address unique AI risks. Organizations should implement assessment processes for:

**Pre-Deployment AI Risk Assessment:**
- Privacy impact assessment for AI tools processing student or staff data
- Security architecture review (data encryption, access controls, authentication)
- Vendor AI model transparency (training data sources, model capabilities, limitations)
- Identification of AI decision-making scope (informational vs. automated decisions)

**FERPA/COPPA Compliance Verification:**
- **FERPA (Family Educational Rights and Privacy Act):** Vendor agreement includes:
  - School official designation (vendor acting on behalf of school)
  - Limited use of education records to authorized purposes
  - Prohibition on re-disclosure without consent
  - Data deletion upon contract termination
- **COPPA (Children's Online Privacy Protection Act):** For tools used by children under 13:
  - Parental consent mechanisms
  - Data collection limitations (collect only what's needed)
  - Reasonable security measures
  - Prohibition on conditioning participation on excessive data collection

**Data Usage Restrictions (Model Training):**
- **Explicit prohibition:** Student inputs/outputs cannot be used for AI model training or improvement
- **Data retention:** Vendor must delete student data upon request or contract end
- **Data isolation:** Student data segregated from general training datasets
- **Audit rights:** School can verify compliance through audits or third-party assessments

**Data Processing Agreement (DPA) Requirements:**
- Vendor role as data processor (not data controller) for student data
- Sub-processor disclosure (cloud hosting, AI model providers)
- Data location and sovereignty (U.S.-based storage for some states)
- Breach notification obligations (24-48 hour notification)
- Liability and indemnification for data breaches or FERPA violations

**Technical Security Controls:**
- Encryption in transit (TLS 1.2+) and at rest (AES-256)
- Multi-factor authentication for administrative access
- Role-based access control (RBAC) limiting data access
- Audit logging of AI processing activities
- Data anonymization/de-identification techniques where possible

**Vendor Transparency and Documentation:**
- AI system documentation (NIST AI RMF "Map" function - identify risks)
- Model cards or AI fact sheets describing:
  - Intended use cases and limitations
  - Training data characteristics
  - Known biases or fairness concerns
  - Performance metrics and accuracy
- Regular vendor security assessments (SOC 2 Type II, ISO 27001)

**Ongoing Monitoring:**
- Annual DPA review and renewal
- Vendor security incident monitoring
- Student/parent complaints about AI tool usage
- Regulatory compliance updates (new state privacy laws, FERPA guidance)

**Insurance Rationale:**

**Current Insurance Landscape (2025):**
- **No explicit AI vetting requirements** from major carriers yet
- However, **general vendor risk management IS required** (see Question 8.6, 8.7)
- This question extends existing vendor vetting to AI-specific risks

**Why This Matters for Insurance:**

**Data Breach Liability:**
- Vendor AI tools processing student PII create **data breach exposure**
- If AI vendor suffers breach, school faces:
  - Breach notification costs (state laws require notification)
  - Credit monitoring services for affected students/families
  - Regulatory fines (state education departments, FTC for COPPA violations)
  - Legal defense costs (parent lawsuits, class actions)
- All of these are **covered expenses** under cyber insurance policies

**FERPA Violation Consequences:**
- Loss of federal education funding (ED can withhold funds)
- Reputational damage and enrollment impact
- While funding loss not insurable, defense costs and regulatory response ARE covered

**Third-Party Risk Transfer:**
- Strong DPAs shift liability to AI vendors (vendor must indemnify school)
- Cyber insurers favor organizations with robust vendor contracts
- Schools without DPAs bear full liability for vendor-caused breaches

**Regulatory Compliance Trend:**
- Eight new state privacy laws in 2025 alone
- Many require data processing agreements for third-party services
- Compliance violations trigger regulatory investigations (covered legal expenses)

**Threat Landscape Justification:**

**K-12 Vendor AI Tool Landscape (2024-2025):**
- EdTech platforms increasingly embed AI features (adaptive learning, auto-grading, chatbot tutors)
- Many vendors use public cloud AI services (OpenAI API, Google Gemini API) as sub-processors
- Schools often unaware of sub-processor relationships or data flows

**FERPA Compliance Failures:**
- **Fordham Institute (2024):** "AI is a serious threat to student privacy"
  - Many AI companies don't sufficiently protect student personal data
  - Services offered to teachers/students often lack FERPA protections
  - Data shared with AI companies may be used for model training without disclosure
- **Future of Privacy Forum (2024):** "Vetting Generative AI Tools for Use in Schools"
  - Schools need legal compliance framework for AI vendor assessment
  - Many free AI tools not appropriate for FERPA-protected data
  - Requires vendor transparency on data processing and model training

**Data Exposure Scenarios:**
- Teacher uses AI grading assistant, uploads student essays to cloud-based AI service
- AI vendor suffers breach, exposing student names, grades, written work
- AI chatbot tutor stores conversation history containing student learning disabilities discussions
- EdTech platform uses student interaction data to improve AI algorithms (training) without consent

**Regulatory Enforcement Risk:**
- FTC enforcement of COPPA violations (fines up to $50,120 per violation)
- State attorneys general pursuing EdTech companies for student privacy violations
- OCR (Office for Civil Rights) FERPA investigations of schools using non-compliant vendors

**Citations:**

**K-12 AI Privacy Guidance:**
- **Fordham Institute (2024):** "AI is a serious threat to student privacy"
  - URL: https://fordhaminstitute.org/national/commentary/ai-serious-threat-student-privacy
  - "AI companies proliferate with insufficient student data protection"
  - "FERPA protections don't extend to AI-generated data (predictive insights, behavioral analytics)"
- **Chalkbeat (2024):** "AI tools used by teachers can put student privacy and data at risk"
  - URL: https://www.chalkbeat.org/2024/12/13/ai-tools-used-by-teachers-can-put-student-privacy-and-data-at-risk/
  - "Many AI tools not inherently FERPA-compliant"
  - "Free chatbots may use student inputs for model training"
- **Future of Privacy Forum (2024):** "Vetting Generative AI Tools for Use in Schools"
  - URL: https://fpf.org/wp-content/uploads/2024/10/Ed_AI_legal_compliance.pdf_FInal_OCT24.pdf
  - Legal compliance framework for AI vendor assessment
  - Checklist for FERPA, COPPA, state privacy law compliance
- **eSchool News (2025):** "Data, privacy, and cybersecurity in schools: A 2025 wake-up call"
  - URL: https://www.eschoolnews.com/digital-learning/2025/07/30/data-privacy-and-cybersecurity-in-schools-a-2025-wake-up-call/
  - "Student data governance requires proactive AI vendor vetting"

**FERPA Regulatory Framework:**
- **U.S. Department of Education - Student Privacy:** https://studentprivacy.ed.gov/
  - FERPA applies to "education records" held by schools and authorized vendors
  - Schools must have written agreements with vendors (school official designation)
  - Data must be deleted when no longer needed for authorized purpose
- **FERPA Limitations with AI:**
  - Does not cover AI-generated analytics, predictions, or behavioral insights
  - Regulation predates AI era (1974, last major update 2011)

**COPPA Regulatory Framework:**
- **FTC COPPA Rule:** https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule
  - Applies to online services collecting data from children under 13
  - Requires parental consent, data minimization, reasonable security
  - Penalties: up to $50,120 per violation

**State Privacy Laws (2025):**
- Eight new comprehensive state privacy laws in 2025
- Many include specific protections for student data and AI processing
- Require data processing agreements for third-party vendors

**Vendor Risk Management Frameworks:**
- **CIS Controls v8:**
  - Control 15.1: "Establish and Maintain an Inventory of Service Providers"
  - Control 15.2: "Establish and Maintain a Service Provider Management Policy"
  - Control 15.7: "Securely Decommission Service Providers"
- **NIST Cybersecurity Framework 2.0:**
  - ID.SC (Supply Chain Risk Management): "Priorities, constraints, risk tolerances established and used to support risk decisions associated with managing supply chain risk"
  - GV.SC (Governance - Supply Chain): "Cyber supply chain risk management processes are identified, established, managed, monitored, and improved by organizational stakeholders"
- **NIST AI RMF:**
  - **Map Function:** Identify AI system risks and impacts on individuals
  - **Measure Function:** Assess AI system performance, safety, privacy metrics
  - Applicable to third-party AI systems, not just internally developed

**Insurance Carrier Vendor Requirements:**
- **Chubb (2024):** Preliminary questions include third-party access and data protection
- **Coalition (2025):** Requires robust third-party risk management programs
- **Arch Insurance (2024):** "Insurers require robust TPRM with vendor certifications"
  - URL: https://insurance.archgroup.com/cyber-the-rise-in-third-party-risks-calls-for-greater-transparency/

**Practical K-12 Implementation:**
- CoSN (Consortium for School Networking) provides vendor vetting checklists
- Student Privacy Pledge (pledged by 400+ EdTech companies) commits to data protection
- SETDA (State Educational Technology Directors Association) offers contract language templates
- Many state education departments publish approved vendor lists (pre-vetted for privacy compliance)

---

## Trade Analysis Summary

### Questions to Remove (Make Room for AI Questions)

| Question | Insurance Pressure | K-12 Applicability | Rationale for Trading |
|----------|-------------------|-------------------|----------------------|
| **5.6: API Security Controls** | LOW-MODERATE | Low (schools don't develop APIs) | Too technical; vendor API security covered by 8.6 |
| **3.6: Data Classification** | MODERATE | Moderate (resource-intensive) | Governance maturity indicator; overlaps with 3.1, 3.4 |
| **2.10: Privileged Session Monitoring** | MODERATE | Moderate (component of PAM) | Overlaps with 3.5 (PAM Platform includes session monitoring) |

**Net Impact:** Remove 3 questions (2 High impact, 1 Moderate) = 11 total expansion questions → 8 non-AI questions

### AI Questions to Add

| Question | Insurance Pressure | K-12 Applicability | Rationale for Adding |
|----------|-------------------|-------------------|---------------------|
| **7.4: AI Acceptable Use Policy** | FORWARD-LOOKING | HIGH (80% have AI initiatives; 43% lack policies) | Addresses governance gap; FERPA compliance; shadow AI risk |
| **8.8: AI Tool Privacy Vetting** | FORWARD-LOOKING | HIGH (EdTech AI proliferation) | Vendor risk extension; FERPA/COPPA compliance; breach liability |

**Net Impact:** Add 2 AI questions (both High impact, both Foundational) = 10 total expansion questions

### Revised Assessment Structure

**Original Expansion Plan:** 52 questions + 11 new questions = **63 questions**

**With AI Trade:** 52 questions + 8 non-AI questions + 2 AI questions = **62 questions**

**Foundational Questions:**
- Original plan: 12 existing + 4 new (PAM, SIEM, Email Auth) = 16 foundational
- With AI trade: 16 foundational - 0 removed + 2 AI = **18 foundational questions**

**Category Distribution:**
- Category 2 (Account Management): +1 question → 2.10 removed = **NO NET CHANGE** (keep current count)
- Category 3 (Data Protection): +2 questions → 3.6 removed = **+1 net** (3.5 PAM remains)
- Category 4 (Secure Configuration): +3 questions → No removals = **+3**
- Category 5 (Malware Defense): +2 questions → 5.6 removed = **+1 net** (5.5 Email Auth remains)
- Category 7 (Security Awareness): +1 question (AI AUP) = **+1**
- Category 8 (Vendor Management): +2 questions + 1 new AI question → No removals = **+3**
- Category 9 (Incident Response): +1 question → No removals = **+1**

---

## Critical Assessment: Is AI a True 2025-2026 Priority?

### Arguments FOR Adding AI Questions Now

**1. Threat Landscape is Real and Growing:**
- 67.4% of phishing attacks use AI (not theoretical, happening now)
- 442% increase in AI vishing attacks (H1-H2 2024)
- K-12 schools are targets for AI-enabled superintendent impersonation (BEC attacks)

**2. K-12 Adoption Outpaces Governance:**
- 80% of districts have AI initiatives BUT 43% lack policies
- This creates **unmanaged risk** (shadow AI, FERPA violations)
- Questions address existing gap, not future-looking scenario

**3. FERPA Compliance Crisis:**
- FERPA does not cover AI-generated data (legal gap)
- Many EdTech vendors use student data for AI training
- Schools face regulatory risk TODAY, not in future

**4. Insurance Trend Direction:**
- While not mandated in 2025, Coalition offers "Affirmative AI Insurance"
- Early adopters of AI governance will be better positioned when requirements tighten
- Similar to how MFA became universal requirement (early adopters had lower premiums)

**5. Framework Alignment:**
- NIST AI RMF released 2023, updated 2024 (mainstream framework)
- CoSN, TeachAI, Council of Great City Schools all provide K-12 AI guidance
- Questions align with existing governance standards

### Arguments AGAINST Adding AI Questions Now

**1. NO Current Insurance Mandates:**
- Coalition, Chubb, Corvus do not require AI governance in 2025 applications
- Adding questions increases assessment burden without insurance ROI
- May confuse members about what's actually required vs. aspirational

**2. Implementation Difficulty:**
- AI governance is emerging discipline; K-12 staff lack expertise
- Vetting AI tools requires understanding of model training, data processing, sub-processors
- Smaller districts cannot practically implement these controls in 2025-2026

**3. Opportunity Cost:**
- Trading proven insurance requirements (API security, data classification) for forward-looking AI
- PAM, SIEM, Email Auth are HIGH insurance pressure NOW
- Better to focus on immediate insurance compliance than emerging risks

**4. Assessment Scope Creep:**
- Original research identified 11 questions based on insurance + threat landscape
- AI questions are governance/policy focused, not technical security controls
- Risk of assessment becoming too broad, losing focus

**5. Framework Immaturity:**
- NIST AI RMF is voluntary, not regulatory requirement
- No enforcement mechanism for AI governance in K-12
- Unlike FERPA (mandatory), AI governance is "best practice"

### Recommendation: CONDITIONAL ADDITION

**Recommended Approach:**

**Option A: Add AI Questions as "Emerging Risk" Category (Comprehensive Maturity Only)**
- Mark both AI questions as **NON-foundational** (Comprehensive score only)
- Position as "forward-looking" controls for advanced organizations
- Do not penalize schools lacking AI governance in 2025-2026
- Allows CyberPools to collect baseline data on AI adoption

**Option B: Pilot AI Questions with 10-15 Volunteer Districts in 2025-2026**
- Test questions with larger, more resourced districts
- Gather feedback on clarity, applicability, implementation difficulty
- Refine questions based on pilot results
- Roll out broadly in 2026-2027 when insurance pressure materializes

**Option C: Add AI Questions as Foundational (Aggressive Approach)**
- Justify based on 80% AI adoption rate and 43% policy gap
- Position CyberPools as leader in AI governance for K-12
- Risk: May be too early for insurance alignment, creates compliance burden

**My Recommendation: Option A (Emerging Risk Category)**

**Rationale:**
1. Addresses real K-12 risk (shadow AI, FERPA gaps) without mandating compliance
2. Allows CyberPools to collect baseline AI governance data
3. Positions organization as forward-thinking without penalizing members
4. Provides pathway to Foundational status when insurance market catches up (2026-2027)
5. Avoids trading proven insurance requirements (API, data classification) if questions are non-foundational

**Implementation:**
- Add both AI questions to assessment (7.4, 8.8)
- Mark as "Comprehensive Maturity Indicators" (not Foundational)
- Include explanatory text: "Emerging risk area - forward-looking control"
- Do NOT trade away other questions (keep all 11 original + 2 AI = 13 total expansion)
- Monitor insurance market for AI governance requirements in 2025-2026

---

## Citations Master List

### Threat Intelligence and AI Attack Research

**IBM X-Force Threat Intelligence Index 2025:**
- URL: https://www.ibm.com/reports/threat-intelligence
- Key findings: 84% increase in infostealers; only 24% of AI projects secured; threat actors adopt AI for phishing/malware

**CybelAngel (2025) - AI-Powered Phishing:**
- URL: https://cybelangel.com/blog/rise-ai-phishing/
- Statistics: 67.4% of phishing uses AI; 82.6% of phishing emails use AI; 54% click-through rate for AI phishing

**Tech Advisors (2025) - AI Cyber Attack Statistics:**
- URL: https://tech-adv.com/blog/ai-cyber-attack-statistics/
- Findings: 442% increase in vishing; 30% of orgs fell victim to AI voice scams; $25M deepfake scam

**Verizon Data Breach Investigations Report 2024:**
- URL: https://www.verizon.com/business/resources/reports/dbir/
- Education sector: 88% of breaches involve stolen credentials; 75% include ransomware

### NIST AI Risk Management Framework

**NIST AI RMF:**
- URL: https://www.nist.gov/itl/ai-risk-management-framework
- Framework: Four functions (Govern, Map, Measure, Manage)
- Generative AI Profile: July 2024 update addressing GenAI risks

### K-12 AI Privacy and Governance

**CoSN (Consortium for School Networking):**
- URL: https://www.cosn.org/ai/
- K-12 AI guidance and readiness checklists

**TeachAI + Code.org + CoSN - AI Guidance for Schools Toolkit:**
- URL: https://www.aiforeducation.io/ai-resources/state-ai-guidance
- Seven principles for AI in education

**Fordham Institute (2024) - AI Threat to Student Privacy:**
- URL: https://fordhaminstitute.org/national/commentary/ai-serious-threat-student-privacy
- FERPA limitations with AI-generated data

**Chalkbeat (2024) - AI Tools Risk Student Privacy:**
- URL: https://www.chalkbeat.org/2024/12/13/ai-tools-used-by-teachers-can-put-student-privacy-and-data-at-risk/
- 43% of districts lack AI policies; 80% have AI initiatives

**Future of Privacy Forum (2024) - Vetting GenAI Tools:**
- URL: https://fpf.org/wp-content/uploads/2024/10/Ed_AI_legal_compliance.pdf_FInal_OCT24.pdf
- Legal compliance framework for K-12 AI vendor assessment

**eSchool News (2025) - Data Privacy Wake-Up Call:**
- URL: https://www.eschoolnews.com/digital-learning/2025/07/30/data-privacy-and-cybersecurity-in-schools-a-2025-wake-up-call/

### Regulatory Frameworks

**FERPA (Family Educational Rights and Privacy Act):**
- URL: https://studentprivacy.ed.gov/
- Student privacy regulations for education records

**COPPA (Children's Online Privacy Protection Act):**
- FTC COPPA Rule: https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule
- Penalties: up to $50,120 per violation

**State Privacy Laws (2025):**
- Eight new state comprehensive privacy laws

### Insurance Market Research

**American Bar Association (2025) - Cyber Insurance 2025:**
- URL: https://www.americanbar.org/groups/tort_trial_insurance_practice/resources/brief/2025-winter/cyber-data-privacy-insurance-2025/
- Coalition "Affirmative AI Insurance" for AI-related events

**Aldridge (2025) - 5 Cyber Insurance Requirements:**
- URL: https://aldridge.com/5-requirements-to-get-cyber-insurance/
- MFA, backups, EDR, vulnerability management, training

**Coalition - 5 Essential Requirements:**
- URL: https://www.coalitioninc.com/topics/5-essential-cyber-insurance-requirements

**Arch Insurance (2024) - Third-Party Cyber Risk:**
- URL: https://insurance.archgroup.com/cyber-the-rise-in-third-party-risks-calls-for-greater-transparency/
- Insurers require robust TPRM with vendor certifications

### Cybersecurity Frameworks

**CIS Controls v8:**
- URL: https://www.cisecurity.org/controls/cis-controls-navigator
- Controls 1, 3, 5, 8, 15 (asset inventory, data management, privileged access, audit logs, vendor management)

**NIST Cybersecurity Framework 2.0:**
- URL: https://www.nist.gov/cyberframework
- Functions: Govern (GV), Identify (ID), Protect (PR), Detect (DE), Respond (RS), Recover (RC)

**ISO/IEC 42001 - AI Management System:**
- International standard for AI governance (published 2023)

---

## Appendix: Question Text Comparison

### Removed Questions (Traded Away)

**5.6: API Security Controls**
> For organizations using APIs (application programming interfaces) to integrate systems or provide services, are API security controls implemented including authentication (OAuth 2.0), authorization, rate limiting, and API activity monitoring?

**3.6: Data Classification and Handling Procedures**
> Has the organization established a data classification system (e.g., public, internal, confidential, restricted) with documented handling procedures for each classification level?

**2.10: Privileged Account Session Monitoring**
> Does the organization monitor and log privileged user sessions (administrators, service accounts) with the ability to review session recordings and detect suspicious privileged activities?

### Added Questions (AI-Specific)

**7.4: AI Acceptable Use Policy and Governance**
> Has the organization established an Artificial Intelligence (AI) Acceptable Use Policy that defines approved AI tools, prohibited uses, data privacy requirements, and staff/student responsibilities when using AI technologies (ChatGPT, Google Gemini, Microsoft Copilot, AI-enabled EdTech platforms)?

**8.8: AI Tool Privacy and Security Vetting**
> Does the organization assess privacy and security risks before deploying AI tools or EdTech platforms with AI features, including verification of FERPA/COPPA compliance, data usage restrictions (no student data for AI model training), and data processing agreements with AI vendors?

---

## Next Steps for CyberPools Leadership

1. **Review and Decide on Trade-Off:**
   - Option A: Trade 3 questions for 2 AI questions (net 62 questions)
   - Option B: Keep all 11 + add 2 AI questions (net 65 questions)
   - Option C: Pilot AI questions separately before integration

2. **Determine Foundational Status for AI Questions:**
   - Foundational (insurance-critical) vs. Comprehensive (maturity indicator)
   - Recommendation: Start as Comprehensive, upgrade to Foundational in 2026-2027

3. **Validate with The Trust Insurance Pool:**
   - Do The Trust requirements need AI governance?
   - Are any insurers asking about AI policies in 2025 renewals?

4. **Pilot Test with 10-15 Member Districts:**
   - Gather feedback on AI question clarity and applicability
   - Assess implementation difficulty
   - Refine question wording based on pilot results

5. **Develop Member Resources:**
   - AI Acceptable Use Policy templates
   - AI vendor vetting checklist (FERPA/COPPA compliance)
   - AI governance training for IT directors
   - CoSN/TeachAI framework integration guidance

6. **Monitor Insurance Market Evolution:**
   - Track Coalition, Chubb, Corvus application updates in 2025-2026
   - Assess when AI governance becomes mandated requirement
   - Adjust Foundational classification accordingly

7. **Plan Phased Rollout:**
   - **Phase 1 (January 2026):** Add 4 foundational questions (PAM, SIEM, Email Auth, and possibly 1 AI question)
   - **Phase 2 (June 2026):** Add comprehensive questions including second AI question
   - **Phase 3 (2026-2027):** Upgrade AI questions to Foundational if insurance market requires

---

**Report Completed:** October 30, 2025
**Analysis Completed By:** Claude Code (GRC Expert + Cybersecurity Risk Assessment Perspectives)
**Next Review:** Monitor insurance market quarterly for AI governance requirement emergence
