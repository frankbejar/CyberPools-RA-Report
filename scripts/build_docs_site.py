#!/usr/bin/env python3
"""
Build MkDocs documentation site from comprehensive questionnaire.
Splits the large markdown file into organized category pages.
"""

import os
import re
from pathlib import Path

# Paths
QUESTIONNAIRE_PATH = Path(__file__).parent.parent / "poc-research/docs/COMPREHENSIVE_RISK_ASSESSMENT_QUESTIONNAIRE.md"
DOCS_DIR = Path(__file__).parent.parent / "docs"

def read_questionnaire():
    """Read the comprehensive questionnaire file."""
    with open(QUESTIONNAIRE_PATH, 'r') as f:
        return f.read()

def extract_section(content, start_pattern, end_pattern=None):
    """Extract a section from content between start and end patterns."""
    start_match = re.search(start_pattern, content, re.MULTILINE)
    if not start_match:
        return None

    start_pos = start_match.start()

    if end_pattern:
        end_match = re.search(end_pattern, content[start_pos:], re.MULTILINE)
        if end_match:
            end_pos = start_pos + end_match.start()
            return content[start_pos:end_pos]

    return content[start_pos:]

def create_overview_pages(content):
    """Create overview pages: introduction, methodology, essential controls."""

    # Introduction
    intro = extract_section(
        content,
        r"^# CyberPools Cyber Risk Assessment Questionnaire",
        r"^## Cyber Essential Controls"
    )
    if intro:
        intro_file = DOCS_DIR / "overview" / "introduction.md"
        intro_file.write_text(f"---\ntitle: Introduction\ntags:\n  - Overview\n---\n\n{intro}")
        print(f"✓ Created {intro_file}")

    # Essential Controls
    essential = extract_section(
        content,
        r"^## Cyber Essential Controls",
        r"^## Category 1:"
    )
    if essential:
        essential_file = DOCS_DIR / "overview" / "essential-controls.md"
        essential_file.write_text(f"---\ntitle: Cyber Essential Controls\ntags:\n  - Overview\n  - Foundational\n---\n\n{essential}")
        print(f"✓ Created {essential_file}")

    # Methodology is included in introduction page, no separate page needed

def create_category_pages(content):
    """Create individual category pages."""

    categories = [
        (1, "Asset Inventory and Management", "Category 1:"),
        (2, "Account Management and Access Control", "Category 2:"),
        (3, "Data Protection and Privacy", "Category 3:"),
        (4, "Secure Configuration and Vulnerability Management", "Category 4:"),
        (5, "Malware Defense and Endpoint Security", "Category 5:"),
        (6, "Data Recovery and Business Continuity", "Category 6:"),
        (7, "Security Awareness Training and Education", "Category 7:"),
        (8, "Third-Party and Vendor Risk Management", "Category 8:"),
        (9, "Incident Response and Recovery", "Category 9:"),
    ]

    for i, (num, name, pattern) in enumerate(categories):
        # Determine end pattern (next category or appendix)
        if i < len(categories) - 1:
            end_pattern = f"^## Category {num+1}:"
        else:
            end_pattern = r"^## APPENDIX:"

        category_content = extract_section(
            content,
            f"^## {pattern}",
            end_pattern
        )

        if category_content:
            # Add metadata
            tags = [f"Category {num}"]

            # Detect foundational and new questions
            if "🔑 FOUNDATIONAL" in category_content:
                tags.append("Foundational")
            if "🆕" in category_content:
                tags.append("New")

            # Detect impact levels
            if "Impact Rating:** High (5)" in category_content:
                tags.append("High Impact")
            if "Impact Rating:** Moderate (3)" in category_content:
                tags.append("Moderate Impact")
            if "Impact Rating:** Low (1)" in category_content:
                tags.append("Low Impact")

            tags_str = "\n  - ".join(tags)
            metadata = f"---\ntitle: Category {num} - {name}\ntags:\n  - {tags_str}\n---\n\n"

            category_file = DOCS_DIR / "categories" / f"category-{num}.md"
            category_file.write_text(metadata + category_content)
            print(f"✓ Created {category_file}")

def create_filtered_pages(content):
    """Create filtered view pages."""

    # Foundational questions - only match questions with 🔑 FOUNDATIONAL in the header
    # Stop at next question, category header, or end of file to avoid capturing category overviews
    foundational_questions = []
    for match in re.finditer(r"(###\s+Question\s+[\d.]+:[^\n]*🔑 FOUNDATIONAL[^\n]*\n.*?)(?=###\s+Question|##\s+Category|\Z)", content, re.DOTALL):
        foundational_questions.append(match.group(1))

    if foundational_questions:
        foundational_content = f"""---
title: Foundational Questions (14)
tags:
  - Foundational
  - Insurance Critical
---

# 🔑 Foundational Questions

These 14 questions are **insurance-critical** controls required by most cyber insurance carriers.

## 12 Existing Foundational

Trust Requirements for Education:

- 1.4: End-of-Life Software Management
- 2.3-2.6: Multi-Factor Authentication (4 questions)
- 4.3: Patch Management
- 4.7: External Vulnerability Scanning
- 5.4: EDR/Antivirus Deployment
- 6.3-6.4: Air-gapped Backups + Testing
- 7.2-7.3: Phishing Simulation + Training

## 2 NEW Foundational

2026 Additions:

- 3.5: Privileged Access Management (PAM) - Process-based approaches acceptable
- 5.5: Email Authentication (DMARC/SPF/DKIM)

---

{"".join(foundational_questions)}
"""
        foundational_file = DOCS_DIR / "filtered" / "foundational.md"
        foundational_file.write_text(foundational_content)
        print(f"✓ Created {foundational_file} ({len(foundational_questions)} questions)")

    # New questions - only match questions with 🆕 in the header
    # Stop at next question, category header, or end of file to avoid capturing category overviews
    new_questions = []
    for match in re.finditer(r"(###\s+Question\s+[\d.]+:[^\n]*🆕[^\n]*\n.*?)(?=###\s+Question|##\s+Category|\Z)", content, re.DOTALL):
        new_questions.append(match.group(1))

    if new_questions:
        new_content = f"""---
title: New Questions (12)
tags:
  - New
  - 2026 Expansion
---

# 🆕 New Questions for 2026

These 12 questions have been added based on 2024-2025 threat landscape analysis and insurance market requirements.

**5 New Foundational:**
- 3.5: PAM Platform
- 4.14: SIEM
- 5.5: Email Authentication
- 7.4: AI AUP
- 8.8: AI Vetting

**7 New Supporting:**
- 3.6: Data Classification
- 4.15: Cloud Security
- 4.16: Secure Remote Access
- 5.6: API Security
- 8.6: Vendor Certifications
- 8.7: Vendor Monitoring
- 9.7: MTTD/MTTR

---

{"".join(new_questions)}
"""
        new_file = DOCS_DIR / "filtered" / "new-questions.md"
        new_file.write_text(new_content)
        print(f"✓ Created {new_file} ({len(new_questions)} questions)")

    # High impact questions
    high_impact_questions = []
    for match in re.finditer(r"(###\s+Question\s+[\d.]+:.*?\*\*Impact Rating:\*\* High \(5\).*?)(?=###\s+Question|\Z)", content, re.DOTALL):
        high_impact_questions.append(match.group(1))

    if high_impact_questions:
        high_content = f"""---
title: High Impact Questions
tags:
  - High Impact
  - Critical Controls
---

# ⚠️ High Impact Questions

Questions with **High (5)** impact rating - these are critical security controls.

Impact Rating Scale:
- **High (5):** Critical control - significant impact if compromised
- Moderate (3): Important control - moderate impact if compromised
- Low (1): Basic control - limited impact if compromised

---

{"".join(high_impact_questions)}
"""
        high_file = DOCS_DIR / "filtered" / "high-impact.md"
        high_file.write_text(high_content)
        print(f"✓ Created {high_file} ({len(high_impact_questions)} questions)")

def create_citations_page(content):
    """Create citations/reference page."""

    citations = extract_section(
        content,
        r"^## APPENDIX: Comprehensive Citations and References",
        r"^---\s*$"
    )

    if citations:
        citations_file = DOCS_DIR / "reference" / "citations.md"
        citations_file.write_text(f"---\ntitle: Citations and References\ntags:\n  - Reference\n---\n\n{citations}")
        print(f"✓ Created {citations_file}")

def create_framework_mapping_page():
    """Create framework mapping reference page."""

    framework_content = """---
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
"""

    framework_file = DOCS_DIR / "reference" / "frameworks.md"
    framework_file.write_text(framework_content)
    print(f"✓ Created {framework_file}")

def create_tags_page():
    """Create tags index page."""

    tags_content = """---
title: Browse by Tags
---

# 🏷️ Browse by Tags

Use tags to filter questions across categories:

## Question Types

- [Foundational](../filtered/foundational.md) - 17 insurance-critical controls
- [New](../filtered/new-questions.md) - 12 questions added for 2026
- [High Impact](../filtered/high-impact.md) - Critical security controls (impact rating 5)

## Categories

- [Category 1](../categories/category-1.md) - Asset Inventory and Management
- [Category 2](../categories/category-2.md) - Account Management and Access Control
- [Category 3](../categories/category-3.md) - Data Protection and Privacy
- [Category 4](../categories/category-4.md) - Secure Configuration and Vulnerability Management
- [Category 5](../categories/category-5.md) - Malware Defense and Endpoint Security
- [Category 6](../categories/category-6.md) - Data Recovery and Business Continuity
- [Category 7](../categories/category-7.md) - Security Awareness Training and Education
- [Category 8](../categories/category-8.md) - Third-Party and Vendor Risk Management
- [Category 9](../categories/category-9.md) - Incident Response and Recovery

## Sectors

- [Education](../sectors/education.md) - K-12 and Higher Education
- [Healthcare](../sectors/healthcare.md) - HIPAA compliance and patient care
- [Religious/Nonprofit](../sectors/nonprofit.md) - Donor data protection
- [General](../sectors/general.md) - Enterprise and industry-agnostic

## Framework Alignment

- NIST CSF 2.0
- CIS Controls v8
- NIST AI RMF
"""

    tags_file = DOCS_DIR / "tags.md"
    tags_file.write_text(tags_content)
    print(f"✓ Created {tags_file}")

def create_sector_pages():
    """Create sector-specific guidance pages."""

    sectors = [
        ("education", "Education (K-12/Higher Ed)", "🎓",
         "Sector-specific guidance for K-12 and Higher Education organizations, including FERPA compliance, student data protection, and practical implementation for limited IT resources."),
        ("healthcare", "Healthcare", "🏥",
         "Healthcare-specific guidance including HIPAA compliance, patient care considerations, and life-safety systems integration."),
        ("nonprofit", "Religious/Nonprofit", "⛪",
         "Guidance for religious organizations and nonprofits, focusing on donor data protection, budget-conscious implementations, and stewardship."),
        ("general", "General Organizations", "🏢",
         "Enterprise and industry-agnostic guidance applicable across all sectors with various regulatory frameworks.")
    ]

    for filename, title, icon, description in sectors:
        content = f"""---
title: {title}
tags:
  - Sector Guidance
  - {title.split()[0]}
---

# {icon} {title}

{description}

---

!!! info "How to Use This Page"
    This page extracts the **{title}** sector-specific context from all 65 questions. Each question includes practical implementation guidance tailored to {title.lower()} organizations.

---

## Category 1: Asset Inventory and Management

*Sector-specific guidance for Asset Inventory questions will appear here*

[View full Category 1 →](../categories/category-1.md)

---

## Category 2: Account Management and Access Control

*Sector-specific guidance for Account Management questions will appear here*

[View full Category 2 →](../categories/category-2.md)

---

## Category 3: Data Protection and Privacy

*Sector-specific guidance for Data Protection questions will appear here*

[View full Category 3 →](../categories/category-3.md)

---

## Category 4: Secure Configuration and Vulnerability Management

*Sector-specific guidance for Secure Configuration questions will appear here*

[View full Category 4 →](../categories/category-4.md)

---

## Category 5: Malware Defense and Endpoint Security

*Sector-specific guidance for Malware Defense questions will appear here*

[View full Category 5 →](../categories/category-5.md)

---

## Category 6: Data Recovery and Business Continuity

*Sector-specific guidance for Data Recovery questions will appear here*

[View full Category 6 →](../categories/category-6.md)

---

## Category 7: Security Awareness Training and Education

*Sector-specific guidance for Security Awareness questions will appear here*

[View full Category 7 →](../categories/category-7.md)

---

## Category 8: Third-Party and Vendor Risk Management

*Sector-specific guidance for Vendor Risk questions will appear here*

[View full Category 8 →](../categories/category-8.md)

---

## Category 9: Incident Response and Recovery

*Sector-specific guidance for Incident Response questions will appear here*

[View full Category 9 →](../categories/category-9.md)

---

!!! tip "Next Steps"
    - [View all categories](../categories/category-1.md)
    - [See foundational questions](../filtered/foundational.md)
    - [Browse new questions](../filtered/new-questions.md)
"""
        sector_file = DOCS_DIR / "sectors" / f"{filename}.md"
        sector_file.write_text(content)
        print(f"✓ Created {sector_file}")

def create_custom_css():
    """Create custom CSS for enhanced styling."""

    css_content = """/* Custom styles for CyberPools Risk Assessment site */

/* Highlight foundational questions */
:root {
  --foundational-color: #2e7d32;
  --new-color: #1976d2;
  --high-impact-color: #d32f2f;
}

/* Foundational badge */
span:has-text("🔑 FOUNDATIONAL") {
  background-color: var(--foundational-color);
  color: white;
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 500;
}

/* New badge */
span:has-text("🆕") {
  background-color: var(--new-color);
  color: white;
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 500;
}

/* High impact highlight */
strong:has-text("High (5)") {
  color: var(--high-impact-color);
  font-weight: 700;
}

/* Question headers */
h3[id^="question-"] {
  border-left: 4px solid var(--md-primary-fg-color);
  padding-left: 1rem;
  margin-left: -1rem;
}

/* Grid cards enhancement */
.grid.cards {
  margin-top: 1rem;
}

/* Sector icons */
.sector-icon {
  font-size: 2rem;
  margin-right: 0.5rem;
}

/* Impact rating badges */
.impact-high {
  color: #d32f2f;
  font-weight: 700;
}

.impact-moderate {
  color: #f57c00;
  font-weight: 600;
}

.impact-low {
  color: #388e3c;
  font-weight: 500;
}
"""

    css_file = DOCS_DIR / "stylesheets" / "extra.css"
    css_file.write_text(css_content)
    print(f"✓ Created {css_file}")

def main():
    """Main build function."""
    print("🏗️  Building MkDocs site from comprehensive questionnaire...\n")

    # Read questionnaire
    content = read_questionnaire()
    print(f"✓ Read questionnaire ({len(content)} characters)\n")

    # Create pages
    print("Creating overview pages...")
    create_overview_pages(content)

    print("\nCreating category pages...")
    create_category_pages(content)

    print("\nCreating filtered view pages...")
    create_filtered_pages(content)

    print("\nCreating reference pages...")
    create_citations_page(content)
    create_framework_mapping_page()
    create_tags_page()

    print("\nCreating sector pages...")
    create_sector_pages()

    print("\nCreating custom CSS...")
    create_custom_css()

    print("\n✅ Site build complete!")
    print("\nNext steps:")
    print("1. Install MkDocs Material: pip install mkdocs-material")
    print("2. Preview locally: mkdocs serve")
    print("3. Build static site: mkdocs build")
    print("4. Deploy to GitHub Pages: See .github/workflows/docs.yml")

if __name__ == "__main__":
    main()
