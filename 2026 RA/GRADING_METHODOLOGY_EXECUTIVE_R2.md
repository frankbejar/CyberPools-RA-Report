# CyberPools Risk Assessment Grading Methodologies

## Executive Comparison and Recommendation

Date: November 11, 2025

Version: 8.0

Purpose: Evaluate grading methodologies and provide evidence-based recommendations for the 2026 Risk Assessment

## Executive Summary

### The Risk

Organizations without multi-factor authentication for critical systems experience ransomware incidents at significantly higher rates---with 58% of ransomware claims starting from compromised VPN and firewall access, and 47% involving stolen credentials.[^[2]{.underline}^](#cite_2) Yet phishing-resistant MFA blocks over 99% of identity-based attacks (Microsoft Digital Defense Report 2025).

The financial impact is severe: The average data breach costs \$4.88 million globally, with credential-based breaches taking 292 days to detect and contain (IBM Cost of a Data Breach Report, 2024).

96% of ransomware attacks target backups, succeeding 74% of the time when protections are absent (Rubrik Zero Labs 2024). Organizations that pay ransoms achieve full data recovery only 16% of the time (Rubrik Zero Labs, 2023).

### The Problem

An organization can score 98% on the current risk assessment while having an incomplete MFA deployment---a control framework required by the vast majority of major cyber insurance carriers (with a prevalence of 95% or higher).

For example, missing MFA for remote access/VPN, despite having it deployed elsewhere, creates a critical insurance gap.

Board members view \"98%\", indicating a nearly perfect security posture, and approve the status quo. They remain completely unaware that the organization faces a significant risk of coverage denial or severe restrictions due to this single control gap.

Real-world impact: Hamilton City's insurer denied its \$5 million cyber insurance claim, specifically due to incomplete MFA implementation, leaving the city responsible for a total of \$18.4 million in recovery costs (CBC News, 2025).[^[1]{.underline}^](#cite_1)

### The Solution

The Grade Ceiling methodology ensures critical gaps are visible in the grade itself. An organization scoring 93% but with an incomplete MFA deployment receives a Grade C (not an A-), prompting board discussion about the specific control gap and associated insurance risk.

Evidence Base: Analysis of 4 grading methodologies against six evaluation criteria. Verified citations from publicly accessible carrier requirements, threat intelligence reports, and peer-reviewed research.

### Current System

**How the assessment works:**

CyberPools\' Risk Assessment evaluates 57 questions (2026 version) across 10 security categories. For each question:

1.  **CyberPools assigns an Impact Rating (1, 3, or 5)** based on expert analysis of historical breach data, insurance claims, and regulatory requirements. This reflects how important the control is for preventing cyber incidents.

2.  **Members provide an Implementation Rating (1, 3, or 5)** based on their current deployment:

    - 1 = Fully Implemented

    - 3 = Partially Implemented

    - 5 = Not Implemented

3.  **Risk Score Calculation:** Control Rating × Impact Rating = Risk Score per question

    - Example: \"Not Implemented\" (5) × \"High Impact\" (5) = 25 risk points

4.  **Overall Score:** Sum all risk scores, convert to 0-100% scale

All questions carry the same weight in the final score, regardless of Impact Rating. The current compensatory scoring hides critical weaknesses.

An organization with incomplete MFA deployment scores 98%. The board approves the status quo, unaware of the risk of insurance denial. Coalition reports 58% of ransomware attacks exploit VPN/firewall vulnerabilities.[^[2]{.underline}^](#cite_2) The current flat scoring allows a high score even with this critical MFA gap. The assessment fails to communicate material risk.

**Note on Category-Level Scores:** While CyberPools provides category scores alongside the overall score (e.g., Category 2 drops to 88% in this scenario), category-level granularity alone proves insufficient for highlighting insurance-critical gaps. Category scores provide partial visibility but inadequate urgency.

**Core Question: How can CyberPools ensure critical gaps are visible while maintaining statistical validity and member engagement?**

### Critical Control Framework (foundational controls for 2026 risk assessment)

The methodologies evaluated below differ in their approach to handling critical security controls. Based on threat intelligence, insurance carrier requirements, and regulatory frameworks, CyberPools has identified critical controls that represent insurance-critical and breach-critical security gaps.

These controls fall into distinct priority tiers:

- **TIER 1A (10 controls):** Insurance requirements with universal carrier prevalence (95%+) and direct coverage impact (e.g., MFA for critical systems including remote access/cloud services/admin accounts/critical data, EDR, protected backups, backup testing, external vulnerability scanning, patch management, end-of-life software removal)

- **TIER 1B (7 controls):** Emerging requirements (50-95% prevalence) for rate optimization and foundational defense-in-depth (e.g., access reviews and privileged access management, data encryption at rest, data retention, email authentication, security awareness training, phishing simulations, incident response plan)

- **Comprehensive Score (40 questions):** The remaining 40 questions beyond the 17 foundational controls assess defense-in-depth practices, operational security, and risk management processes that contribute to overall cyber resilience but are not universal insurance requirements (30% of overall grade)

How each methodology treats these controls, particularly the distinction between insurance requirements and comprehensive defense practices, determines its effectiveness at communicating actual cyber risk and insurance eligibility.

## Methodologies Evaluated

CyberPools evaluated three distinct grading approaches against six evaluation criteria:

### 1. True Gating (All-or-Nothing)

**How it works:** Missing any of the 10 TIER 1A controls results in zero points for the entire tier. Organization with 9 of 10 controls receives same grade (F, 49%) as organization with 4 of 10 controls.

**Key strengths:** Impossible to mask critical gaps, missing MFA immediately visible.

**Key weaknesses:**

- Creates bimodal distribution (Grade F or Grade A, nothing between)

- One control difference = 46-point swing

- Demotivating cliff effect (9→10 controls = no grade improvement)

- High gaming/inflation risk due to catastrophic consequences

**Verdict:** Rejected - Statistical invalidity, poor ability to distinguish risk levels, misaligns with insurance market

### 2. Progressive Gating (Weighted Scoring)

**How it works:** TIER 1A controls weighted 7.0 points each, TIER 1B controls 7.5 points, all other questions 2.5 points. Foundation Score (70%) + Comprehensive Score (30%) = Overall Score. Grades based on score alone, no ceiling.

**Key strengths:**

- Significant improvement over flat scoring (40% more penalty for missing critical controls)

- Maintains ability to distinguish risk levels across all grade tiers

- Statistically sound, motivates incremental improvement

- Aligns with carrier weighted scoring practices

**Key weakness:** Does NOT fully solve masking problem. Organization with incomplete MFA implementation scores 91%, receives Grade A-. Board sees \"excellent performance\" despite near-universal carrier restrictions. Gap is in report details, not in grade itself.

### 3. Grade Ceiling (Recommended)

**How it works:** Calculate score using Progressive Gating weighted formula, then apply grade ceiling based on critical gaps:

- Missing 2+ TIER 1A controls → Maximum Grade F

- Missing 1 TIER 1A control → Maximum Grade C

- Missing 1+ TIER 1B controls → Maximum Grade B

- No critical gaps → No ceiling, use score-based grade

**Key innovation:** Combines weighted scoring (Progressive Gating strength) with grade caps (True Gating strength). Organization scoring 91% but with incomplete MFA implementation receives Grade C (91%), gap is in the grade itself.

**Verdict:** Recommended - Only methodology passing all six evaluation criteria. Solves masking problem while maintaining statistical validity, insurance alignment, and ability to distinguish risk levels.

## Side-by-Side Comparison

### Performance Against Evaluation Criteria

The evaluation criteria table below illustrates how each methodology performed in relation to the six established standards.

  ---------------------------------------------------------------------------------------------
  Objective                   Current Flat   True Gating   Progressive Gating   Grade Ceiling
  --------------------------- -------------- ------------- -------------------- ---------------
  Solves Masking              FAIL           PASS          PARTIAL              PASS

  Distinguishes Risk Levels   PASS           FAIL          PASS                 PASS

  Insurance Alignment         FAIL           FAIL          PARTIAL              PASS

  Motivates Improvement       PASS           FAIL          PASS                 PASS

  Statistical Validity        PARTIAL        FAIL          PASS                 PASS

  Communication Clarity       FAIL           PASS          PARTIAL              PASS

  TOTAL PASS                  2/6            2/6           4.5/6                6/6
  ---------------------------------------------------------------------------------------------

## Example: High-Performing Organization with a Single Critical Gap

This section illustrates how these differences manifest in a real-world organizational scenario that represents the primary problem CyberPools seeks to solve.

### Organization Profile

- Strong overall security program

- Missing: MFA for Remote Access (TIER 1A control, Question 2.4)

- All other 56 questions: Fully implemented

### Insurance Reality

The majority of insurance carriers may decline coverage or impose restrictions due to incomplete deployment of MFA. MFA controls are a near-universal carrier requirement, with a prevalence of over 95% across major carriers.

### The Question

Which grading methodology accurately signals this insurance risk to board members?

+--------------------+------------+---------------+-----------+-----------+---------------------+
| Methodology        | Foundation | Comprehensive | Overall   | Grade     | Masking             |
|                    |            |               |           |           |                     |
|                    | Controls   | Controls      | Score     |           |                     |
+====================+============+===============+===========+===========+=====================+
| Current Flat       | N/A        | N/A           | 98%       | N/A       | Masks gap           |
+--------------------+------------+---------------+-----------+-----------+---------------------+
| True Gating        | 30%        | 100%          | 51%       | F         | Overstates severity |
+--------------------+------------+---------------+-----------+-----------+---------------------+
| Progressive Gating | 90%        | 100%          | 93%       | A-        | Masks gap           |
+--------------------+------------+---------------+-----------+-----------+---------------------+
| Grade Ceiling      | 90%        | 100%          | 93%       | C         | Shows gap           |
+--------------------+------------+---------------+-----------+-----------+---------------------+

### Scoring Calculations

**2025 Flat Scoring Model***:*

- 42 High Impact questions fully implemented: 42 × 5 × 1 = 210 points

- 1 critical control question not implemented (MFA for remote access): 1 × 5 × 5 = 25 points

- 10 Moderate Impact questions fully implemented: 10 × 3 × 1 = 30 points

- 1 Low Impact question fully implemented: 1 × 1 × 1 = 1 point

- Total Score: 266 (MIN = 246, MAX = 1,230, RANGE = 984)

- Final %: (1 - (266-246)/984) × 100 = 97.97% ≈ 98%\`

**2026 Weighted Model (Progressive Gating/Grade Ceiling**):

- TIER 1A: 9 of 10 controls = 63 points (lost 7 points for missing Q2.4 MFA Remote Access)

- TIER 1B: 4 of 4 controls = 30 points

- Foundation Total: 93 of 100 points = 93%

- Comprehensive: 40 of 40 questions fully implemented = 100%

- Overall Score: (93% × 0.70) + (100% × 0.30) = 65.1% + 30.0% = 95.1%

### How Each Methodology Grades This Organization

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Methodology            Score Calculation                                                                                        Final Score   Grade    Board Interpretation
  ---------------------- -------------------------------------------------------------------------------------------------------- ------------- -------- --------------------------------------
  Current Flat Scoring   Equal weighting all 57 questions, missing MFA Remote reduces score by only 2%                            98%           N/A      98% appears nearly perfect

  True Gating            Missing any TIER 1A control = zero points for entire tier (70% of grade)                                 51%           F        Grade F suggests total failure

  Progressive Gating     Foundation: 93%, Comprehensive: 100%, Overall: 95.1%                                                     95%           A-       Grade A- suggests excellent security

  Grade Ceiling          Foundation: 93%, Comprehensive: 100%, Overall: 95.1%. Ceiling applied: Missing 1 TIER 1A → Max Grade C   95%           C        Grade C signals critical gap exists
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Which Grade Aligns with Insurance Reality?

- Grade Ceiling (Grade C):

- Accurate - Grade C reflects \"developing with critical gap,\" matching widespread carrier restrictions for this specific control gap

- Progressive Gating (Grade A-):

- Misleading - Grade A- suggests \"excellent\" performance and strong insurability, contradicts carrier treatment

- True Gating (Grade F):

- Overstated - Grade F suggests complete failure/uninsurable, but the organization may obtain restricted coverage from some carriers

- Current Flat (98%):

- Severely misleading - 98% suggests \"nearly perfect\" security posture, completely masks critical insurance gap; creates false confidence that prevents remediation

### Category-Level Score Analysis

CyberPools currently provides granular category scores alongside the overall score.

For this example organization:

- Overall Score: 98% (nearly perfect)

- Category 2 (Account Management)

- Score: 88%

While the Category 2 score (88%) shows some visibility of the gap, it still masks the critical nature:

- 88% looks acceptable to board members (\"B+ range\")

- No indication that this specific 12-point drop creates insurance denial risk

- The category score does not distinguish between different types of gaps within that category

- Board focus remains on the headline 98% overall score during presentations

### Key Insight

Only Grade Ceiling makes the critical gap visible in the grade itself, forcing board conversation about the specific control gap and insurance risk. The 98% flat score is the worst outcome - it suggests excellence while hiding material risk. Category scores provide partial visibility but insufficient urgency.

## Final Recommendation

### Recommended Methodology: Grade Ceiling

Based on comprehensive analysis across six evaluation criteria, statistical validation, insurance market alignment, and risk assessment, CyberPools should implement the Grade Ceiling grading methodology for the 2026 Risk Assessment cycle.

### Evidence-Based Rationale

The only methodology to pass all six evaluation criteria. Grade Ceiling solves the masking problem while maintaining statistical validity, insurance alignment, and member engagement.

Key Supporting Evidence:

**1. Solves the Primary Problem**

Internal CyberPools statement:

\"Our current RA is missing something - a member could be missing a critical control and still have a good score because of the scoring system.\"

**Grade Ceiling solution:**

- Organization with incomplete MFA deployment (e.g., Q2.4 missing) scores 95%

- Current Flat: 98% (severely masks gap - suggests \"nearly perfect\" security)

- Progressive Gating: 95%, Grade A- (gap in details, psychologically masked by A-)

- Grade Ceiling: 95%, Grade C (gap in the grade itself - cannot be masked)

Board presentation: Current (98%) → \"Nearly Perfect - No Action Needed\", Progressive (95%, A-) → \"Excellent\", Grade Ceiling (95%, C) → \"What do we need to fix?\" Critical gap drives board discussion and budget approval. The 98% flat score is the most dangerous outcome - it creates false confidence that prevents remediation.

**2. Statistical Performance**

- Strong inter-rater reliability between assessors (clear criteria reduce judgment variability)

- Statistically significant differences across grade tiers

- Within-tier score ranges maintain progress tracking capability

- Strong prediction accuracy for insurance outcomes (methodology mirrors carrier practices)

- Strong framework alignment with NIST CSF (risk-based prioritization)

- Meets assessment design standards established by AERA/APA/NCME[^[4]{.underline}^](#cite_4)

**3. Insurance Market Alignment**

Grade Ceiling methodology produces appropriate alignment with carrier practices:

- Members with critical gaps receive C/D/F grades (matching carrier treatment)

- Members with all critical controls receive A/B grades (matching carrier treatment)

- Methodology mirrors carrier hybrid approach: weighted scoring plus gates

- Coalition uses both Cyber Health Rating (0-100) for pricing and minimum requirements for eligibility[^[5]{.underline}^](#cite_5)

**4. Real-World Performance Characteristics**

Grade Ceiling methodology produces:

- Appropriate grade distribution (avoids bimodal clustering of True Gating)

- Strong alignment with insurance outcomes (methodology design mirrors carrier practices)

- Clear improvement pathways that motivate member engagement

### How Grade Ceiling Works

Calculates scores using the Progressive Gating weighted formula, then apply the grade ceiling based on critical gaps. This ensures critical gaps are visible in the grade while maintaining the ability to distinguish risk levels through preserved scores.

┌─────────────────────────────────────────────────────────────┐

│ TIER 1A - Insurance Requirements (10 controls) │

│ ═══════════════════════════════════════════════════════════ │

│ • End-of-Life Software (Q 1.4) ┐ │

│ • MFA Remote Access/VPN (Q 2.4) │ │

│ • MFA Cloud Services (Q 2.5) │ │

│ • MFA Admin Accounts (Q 2.6) │ │

│ • MFA Critical Systems/Data (Q 2.7) │ │

│ • Patch Management (Q 4.2) │ Missing 1 → C │

│ • External Vuln Scanning (Q 4.5) │ Missing 2+ → F │

│ • EDR/MDR (Q 5.3) │ │

│ • Protected Backups (Q 6.2) │ │

│ • Backup Testing (Q 6.3) ┘ │

│ 70 points (70%) │

├─────────────────────────────────────────────────────────────┤

│ TIER 1B - Foundational Defense-in-Depth (7 controls) │

│ ─────────────────────────────────────────────────────────── │

│ • Access Reviews & PAM (Q 2.9) ┐ │

│ • Data Encryption at Rest (Q 3.2) │ │

│ • Data Retention (Q 3.3) │ │

│ • Email Authentication (Q 5.4) │ │

│ • Security Awareness Training (Q 7.2) │ │

│ • Phishing Simulations (Q 7.3) │ │
│ • Incident Response Plan (Q 9.1) ┘ │
│                                          Missing 1 → B │
│ 30 points (30%) │

└─────────────────────────────────────────────────────────────┘

Foundation Score Total: 100 points (70% of overall)

Comprehensive Score: All 41 non-foundational questions (30% of overall)

Grade Ceiling is the only methodology that passes all six evaluation criteria. It combines the statistical soundness of Progressive Gating weighted scoring with ceiling mechanisms that ensure critical gaps remain visible in the final grade.

**Key Advantages:**

- Solves masking while maintaining discrimination: 95% with MFA gap = Grade C (visible problem), vs. 98% flat score (hidden problem)

- Mirrors insurance carrier practices: Weighted scoring for pricing + minimum requirements for eligibility

- Clear improvement pathways: Current Grade C (95%) → Fix 1 control → Grade A (creates motivation)

- Statistically valid: Meets AERA/APA/NCME assessment design standards, strong predictive validity[^[4]{.underline}^](#cite_4)

**Considerations:**

- Members need education on TIER framework and ceiling concept (addressed through webinars and report explanations)

- TIER classifications require annual review to maintain alignment with evolving carrier requirements

## Citations

[]{#cite_1 .anchor}**\[1\]** CBC News. (2025). Insurance won\'t cover \$5M in City of Hamilton claims for cyberattack, citing lack of log-in security. Canadian Broadcasting Corporation. Published July 31, 2025. Case of City of Hamilton, Ontario ransomware attack (February 2024) where insurer denied \$5 million in coverage claims, leaving city responsible for approximately \$18.4 million in total recovery costs specifically due to incomplete multi-factor authentication implementation at time of breach. Retrieved from https://www.cbc.ca/news/canada/hamilton/cybersecurity-breach-1.7597713

[]{#cite_2 .anchor}**\[2\]** Coalition Insurance. (2025). Cyber Threat Index 2025. Coalition Inc. Retrieved from https://www.coalitioninc.com/announcements/cyber-threat-index-2025

**\[3\]** Black, P., & Wiliam, D. (1998). Assessment and classroom learning. Assessment in Education: Principles, Policy & Practice, 5(1), 7-74. https://doi.org/10.1080/0969595980050102

[]{#cite_4 .anchor}**\[4\]** American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). Standards for Educational and Psychological Testing. AERA. https://www.apa.org/science/programs/testing/standards

[]{#cite_5 .anchor}**\[5\]** Coalition Inc. (2024). \"Introducing Cyber Health Rating.\" Coalition Blog. December 15, 2024. Retrieved from https://www.coalitioninc.com/blog/cyber-insurance/introducing-cyber-health-rating
