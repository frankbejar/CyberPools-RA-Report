# GitHub Pages Documentation Site Re-Engineering Plan

**Project:** CyberPools 2026 Risk Assessment Documentation Site
**URL:** https://frankbejar.github.io/CyberPools-RA-Report/
**Status:** Complete redesign planned
**Date Created:** November 19, 2025
**Current Status:** Planning phase - Ready for implementation

---

## Executive Summary

Complete re-engineering of the CyberPools Risk Assessment GitHub Pages documentation site to align with the 2026 v6.2 FINAL question set (57 questions, 10/7/40 TIER structure, sector-neutral approach). The redesign focuses on clear information architecture, automated content generation from master documents, and optimized user journeys for multiple stakeholder audiences.

---

## Current State vs. Target State

### Current State (OUTDATED)
- Site description: "65 questions across 9 categories"
- Based on old questionnaire structure
- Has sector-specific pages (Education, Healthcare, Religious/Nonprofit)
- Last updated: October 31, 2024
- Manual content management

### Target State (v6.2 ALIGNED)
- Site description: "57 questions across 10 categories"
- Based on 2026_RA_QUESTION_SET_v6.2_FINAL.md
- Sector-neutral approach
- 10 TIER 1A, 7 TIER 1B, 40 Comprehensive structure
- Automated content generation from master documents
- Comprehensive grading methodology documentation
- Full framework alignment (CIS v8.1 IG1, NIST CSF 2.0)

---

## Site Goals & Target Audiences

### Primary Goals
1. Provide public documentation of the 2026 Risk Assessment framework
2. Demonstrate CyberPools' evidence-based, insurance-aligned methodology
3. Enable self-service learning for assessors, risk managers, and members
4. Establish thought leadership in organizational cybersecurity assessment

### Target Audiences
1. **Insurance Carriers/Underwriters** - Understanding TIER structure and insurance alignment
2. **Risk Managers/CISOs** - Preparing for assessments, understanding requirements
3. **CyberPools Assessors** - Conducting assessments, understanding question intent
4. **Pool Administrators** - Understanding member risk profiles and improvement paths
5. **Executive Leadership** - High-level understanding of assessment approach

### Key User Journeys
- "What questions will I be asked?" → Question Set
- "Why do these questions matter for insurance?" → TIER Framework
- "How is my organization scored?" → Grading Methodology
- "What frameworks does this align with?" → Framework Mappings
- "I need to find question 2.4" → Search or TIER 1A page

---

## Proposed Site Structure

```
Home
├── Getting Started
│   ├── What is the 2026 Risk Assessment
│   ├── Who Should Use This Assessment
│   ├── How to Navigate This Site
│   └── Assessment Overview (57 questions, 10/7/40 structure)
│
├── Question Set
│   ├── All Questions (Full List - 57 questions)
│   ├── By TIER
│   │   ├── TIER 1A Questions (10) - Insurance Critical
│   │   ├── TIER 1B Questions (7) - Foundational Defense
│   │   └── Comprehensive Questions (40) - Defense-in-Depth
│   ├── By Category
│   │   ├── Category 1: Inventory and Control of Assets
│   │   ├── Category 2: Account Management
│   │   ├── Category 3: Data Protection
│   │   ├── Category 4: Secure Configuration
│   │   ├── Category 5: Malware Defense
│   │   ├── Category 6: Data Recovery
│   │   ├── Category 7: Security Awareness
│   │   ├── Category 8: Vendor Management
│   │   ├── Category 9: Incident Response
│   │   └── Category 10: Information Security Policies
│   └── By Framework
│       ├── CIS Controls v8.1 IG1 Mapping (86% coverage)
│       └── NIST CSF 2.0 Mapping
│
├── TIER Framework
│   ├── Understanding TIER Classifications
│   ├── TIER 1A: Insurance Requirements (Coverage-Impacting)
│   ├── TIER 1B: Foundational Defense-in-Depth
│   ├── Comprehensive: Maturity & Defense-in-Depth
│   └── Insurance Alignment Research
│
├── Grading Methodology
│   ├── Executive Summary (Grade Ceiling Approach)
│   ├── How Scoring Works (Foundation 70% + Comprehensive 30%)
│   ├── Grade Boundaries (A/B/C/D/F)
│   ├── Example Calculations
│   └── Technical Deep-Dive
│
├── Framework Alignment
│   ├── CIS Controls v8.1 Implementation Group 1
│   ├── NIST Cybersecurity Framework 2.0
│   ├── Coverage Analysis (48 of 56 IG1 safeguards)
│   └── Gap Analysis & Rationale
│
├── For Assessors
│   ├── Assessment Guidance
│   ├── Question Intent & Scoring
│   ├── Common Clarifications
│   └── Evidence Collection
│
├── Resources
│   ├── Citations & Sources
│   ├── Glossary
│   ├── FAQ
│   └── Version History
│
└── About
    ├── About CyberPools
    ├── Contact
    └── Feedback
```

---

## Core Pages Inventory

### Must-Have Pages (Priority 1)

**1. Home / Landing Page (`index.md`)**
- Welcome and orientation
- What this is, who it's for
- 57 questions overview
- TIER structure diagram
- Quick links to key sections

**2. TIER 1A Questions (`questions/tier-1a.md`)**
- All 10 insurance-critical questions
- Full justification for each
- Carrier requirements, threat validation
- Key evidence/statistics

**3. TIER 1B Questions (`questions/tier-1b.md`)**
- All 7 foundational defense questions
- Emerging requirements explanation
- Rate optimization vs. coverage

**4. Comprehensive Questions by Category (10 pages)**
- `questions/category-1.md` through `questions/category-10.md`
- Category introduction + all questions in that category

**5. All Questions (`questions/all-questions.md`)**
- Searchable, filterable master list
- All 57 questions in single table

**6. TIER Framework Explained (`tier-framework/overview.md`)**
- What is TIER 1A/1B/Comprehensive
- Insurance prevalence research
- Coverage vs. rate optimization

**7. Grading Methodology - Executive (`grading/executive-summary.md`)**
- Why Grade Ceiling was chosen
- How it works (Foundation 70% + Comprehensive 30%)
- Comparison with rejected alternatives
- Real organization examples

**8. Grading Methodology - Technical (`grading/technical-details.md`)**
- Point allocation formulas
- Grade boundaries
- Example calculations
- Statistical validation

**9. CIS Controls Mapping (`frameworks/cis-controls.md`)**
- 86% coverage (48 of 56 safeguards)
- Coverage table by CIS Control
- Gap analysis and rationale

**10. NIST CSF Mapping (`frameworks/nist-csf.md`)**
- Mapping by Function (GV, ID, PR, DE, RS, RC)
- Coverage by Category

**11. Citations & Sources (`resources/citations.md`)**
- All research sources organized by type
- Threat intelligence, frameworks, insurance carriers

**12. FAQ (`resources/faq.md`)**
- Common questions answered

---

## Navigation Design

### Primary Navigation (Top Bar)

```
[CyberPools Logo] | Home | Questions | TIER Framework | Grading | Frameworks | Resources
```

### Secondary Navigation (Left Sidebar - Context-Specific)

**When in "Questions" section:**
```
Questions
  ├─ All Questions
  ├─ By TIER
  │  ├─ TIER 1A (10)
  │  ├─ TIER 1B (7)
  │  └─ Comprehensive (40)
  ├─ By Category
  │  ├─ 1. Inventory
  │  ├─ 2. Account Management
  │  ├─ 3. Data Protection
  │  ├─ 4. Secure Configuration
  │  ├─ 5. Malware Defense
  │  ├─ 6. Data Recovery
  │  ├─ 7. Security Awareness
  │  ├─ 8. Vendor Management
  │  ├─ 9. Incident Response
  │  └─ 10. Policies
  └─ By Framework
     ├─ CIS v8.1 IG1
     └─ NIST CSF 2.0
```

---

## Content Generation Strategy

### Source Documents (Master Files)

Located in: `/Users/frankbejar/Documents/GitHub/cyberpools/risk-assessment/2026 RA/`

1. **`2026_RA_QUESTION_SET_v6.2_FINAL.md`** - Master question set
2. **`2026_RA_TIER_FRAMEWORK_JUSTIFICATION.md`** - TIER justifications
3. **`GRADING_METHODOLOGY_EXECUTIVE_R2.md`** - Executive grading explanation
4. **`GRADING_METHODOLOGY_TECHNICAL_SUPPLEMENT.md`** - Technical grading details

### Generation Method: Python Script (RECOMMENDED)

**Script Purpose:** Parse master documents and auto-generate MkDocs pages

**Script Location:** `scripts/build_mkdocs_site.py`

**Script Functionality:**
```python
def build_mkdocs_site():
    """
    Build MkDocs site from master documents
    """
    # 1. Parse master question set
    questions = parse_master_question_set()
    # Output: List of 57 questions with metadata (TIER, category, impact, frameworks)

    # 2. Generate question pages
    generate_tier_1a_page(questions)      # tier-1a.md
    generate_tier_1b_page(questions)      # tier-1b.md
    generate_category_pages(questions)    # category-1.md through category-10.md
    generate_all_questions_page(questions) # all-questions.md

    # 3. Generate framework mapping pages
    generate_cis_mapping_page(questions)  # cis-controls.md
    generate_nist_mapping_page(questions) # nist-csf.md

    # 4. Copy/format methodology pages
    convert_grading_executive()           # grading/executive-summary.md
    convert_grading_technical()           # grading/technical-details.md
    convert_tier_framework()              # tier-framework/overview.md

    # 5. Generate supporting pages
    generate_home_page()                  # index.md
    generate_faq()                        # faq.md
    generate_citations()                  # citations.md
    generate_glossary()                   # glossary.md

def parse_master_question_set():
    """
    Parse 2026_RA_QUESTION_SET_v6.2_FINAL.md

    Returns:
    [
        {
            'number': '1.4',
            'text': 'End-of-life software removed/isolated',
            'tier': 'T1A',
            'category': 1,
            'impact': 5,
            'cis': ['2.2', '4.1', '7.1'],
            'nist': ['ID.RA', 'PR.IP'],
            'why_matters': '...',
            'key_evidence': '...'
        },
        ...
    ]
    """
    pass
```

**Alternative: Manual Page Creation**
- Copy content from master documents
- Format for MkDocs
- More time-consuming, harder to maintain

**Recommendation:** Build Python script for automated generation

---

## Design & Branding

### Material for MkDocs Theme Configuration

**Color Scheme:**
```yaml
# mkdocs.yml
theme:
  name: material
  palette:
    - scheme: default
      primary: custom  # CyberPools Primary Navy: #003B5C
      accent: custom   # CyberPools Accent: #0066CC
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: custom
      accent: custom
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

### Custom CSS (`docs/stylesheets/extra.css`)

```css
/* CyberPools Brand Colors */
:root {
  --cp-navy: #003B5C;        /* CyberPools Primary */
  --cp-blue: #0066CC;        /* CyberPools Accent */
  --cp-light-blue: #4A90E2;  /* Lighter accent */

  /* TIER Badge Colors */
  --tier-1a: #C9190B;        /* Red - Critical */
  --tier-1b: #EC7A08;        /* Orange - Important */
  --tier-comp: #2F5233;      /* Green - Comprehensive */

  /* Grade Colors */
  --grade-a: #2F5233;        /* Dark Green */
  --grade-b: #4D8B31;        /* Light Green */
  --grade-c: #EC7A08;        /* Orange */
  --grade-d: #C46100;        /* Dark Orange */
  --grade-f: #C9190B;        /* Red */
}

/* TIER Badges */
.tier-1a-badge {
  background-color: var(--tier-1a);
  color: white;
  padding: 2px 8px;
  border-radius: 3px;
  font-weight: bold;
  font-size: 0.85em;
}

.tier-1b-badge {
  background-color: var(--tier-1b);
  color: white;
  padding: 2px 8px;
  border-radius: 3px;
  font-weight: bold;
  font-size: 0.85em;
}

.tier-comp-badge {
  background-color: var(--tier-comp);
  color: white;
  padding: 2px 8px;
  border-radius: 3px;
  font-weight: bold;
  font-size: 0.85em;
}

/* Impact Badges */
.impact-high {
  background-color: #C9190B;
  color: white;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 0.8em;
}

.impact-moderate {
  background-color: #EC7A08;
  color: white;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 0.8em;
}

.impact-low {
  background-color: #4D8B31;
  color: white;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 0.8em;
}

/* Question Cards */
.question-card {
  border-left: 4px solid var(--cp-blue);
  padding: 16px;
  margin: 16px 0;
  background-color: #f8f9fa;
  border-radius: 4px;
}

.question-card h3 {
  margin-top: 0;
  color: var(--cp-navy);
}

/* Framework Badges */
.framework-badge {
  display: inline-block;
  background-color: #e8eaed;
  color: #333;
  padding: 2px 8px;
  border-radius: 3px;
  font-size: 0.8em;
  margin-right: 4px;
}
```

### Visual Elements
- **Logo:** CyberPools logo in header (need logo file)
- **Badges:** Color-coded TIER badges on questions
- **Icons:** Material icons for navigation and features
- **Cards:** Material card design for questions (expandable)
- **Tables:** Sortable, filterable tables for question lists

---

## Question Display Format

### Individual Question Card Example

```markdown
## Q2.4: MFA for Remote Access/VPN

<span class="tier-1a-badge">TIER 1A</span> <span class="impact-high">Impact: 5</span> <span class="framework-badge">CIS 6.3, 6.4</span> <span class="framework-badge">NIST: PR.AA, PR.PT</span>

**Question:** Is MFA implemented for remote access to on-premises or hub networks?

### Why This Matters

Remote access compromise = 58% of ransomware claims (Coalition 2025). VPN/firewall credentials are the primary initial access vector in modern breaches. Multi-factor authentication blocks 99% of account compromise attacks.

### Insurance Impact

- **Carrier Prevalence:** 100% (universal requirement)
- **Coverage Impact:** Missing MFA for remote access can result in claim denial
- **Real Example:** Hamilton City $5M claim denial for incomplete MFA implementation

### Framework Alignment

- **CIS Controls v8.1:** Safeguards 6.3, 6.4 (IG1 - Implementation Group 1)
- **NIST CSF 2.0:** PR.AA (Authentication and Identity Management), PR.PT (Protective Technology)

### Related Questions

- [Q2.5: MFA for cloud services](./tier-1a.md#q25-mfa-for-cloud-services)
- [Q2.6: MFA for administrative accounts](./tier-1a.md#q26-mfa-for-administrative-accounts)
- [Q2.7: MFA for critical systems/data](./tier-1a.md#q27-mfa-for-critical-systemsdata)
```

---

## Deployment Strategy

### GitHub Pages Configuration

**Repository:** `frankbejar/CyberPools-RA-Report` (existing)
**Branch:** `gh-pages` (auto-generated by MkDocs)
**Build Method:** GitHub Actions (automated deployment)

### GitHub Actions Workflow

**File:** `.github/workflows/docs.yml`

```yaml
name: Deploy MkDocs to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements-docs.txt

      - name: Build and deploy MkDocs
        run: |
          mkdocs gh-deploy --force --clean
```

### Dependencies (`requirements-docs.txt`)

```
mkdocs>=1.5.0
mkdocs-material>=9.5.0
pymdown-extensions>=10.0
```

### Update Workflow

**When questions change:**
```bash
1. Update source documents in 2026 RA/
2. Run: python scripts/build_mkdocs_site.py
3. Review: mkdocs serve (preview at http://127.0.0.1:8000)
4. Commit: git add docs/ mkdocs.yml && git commit -m "Update documentation"
5. Deploy: git push (GitHub Actions auto-deploys in ~30 seconds)
```

---

## Implementation Phases

### Phase 1: Foundation (Days 1-2)
**Goal:** Set up new site structure and configuration

**Tasks:**
- [ ] Create new `mkdocs.yml` configuration
- [ ] Set up folder structure (`docs/questions/`, `docs/grading/`, etc.)
- [ ] Configure Material theme with CyberPools branding
- [ ] Create custom CSS with TIER badge styles
- [ ] Design home page layout
- [ ] Set up GitHub Actions workflow

**Deliverable:** Empty site structure with proper navigation and branding

---

### Phase 2: Question Pages (Days 3-5)
**Goal:** Generate all question-related pages

**Tasks:**
- [ ] Build Python script `scripts/build_mkdocs_site.py`
- [ ] Parse `2026_RA_QUESTION_SET_v6.2_FINAL.md`
- [ ] Generate TIER 1A page (10 questions with full justifications)
- [ ] Generate TIER 1B page (7 questions with full justifications)
- [ ] Generate 10 category pages (40 comprehensive questions)
- [ ] Generate "All Questions" searchable table
- [ ] Add question cross-references and links
- [ ] Test question search functionality

**Deliverable:** Complete question set with all 57 questions organized by TIER and category

---

### Phase 3: Framework & Grading Pages (Days 6-7)
**Goal:** Add methodology and framework documentation

**Tasks:**
- [ ] Create TIER Framework Explained page
- [ ] Convert `GRADING_METHODOLOGY_EXECUTIVE_R2.md` to MkDocs format
- [ ] Convert `GRADING_METHODOLOGY_TECHNICAL_SUPPLEMENT.md` to MkDocs format
- [ ] Build CIS Controls v8.1 IG1 mapping table
- [ ] Build NIST CSF 2.0 mapping table
- [ ] Add framework gap analysis content
- [ ] Create example calculation pages

**Deliverable:** Complete grading methodology and framework alignment documentation

---

### Phase 4: Resources & Supporting Pages (Day 8)
**Goal:** Add supporting content and polish

**Tasks:**
- [ ] Create FAQ page (10+ common questions)
- [ ] Create Citations & Sources page (organized by type)
- [ ] Create Glossary (key terms defined)
- [ ] Create Version History page
- [ ] Create About CyberPools page
- [ ] Add feedback form/contact information
- [ ] Test all internal links
- [ ] Mobile responsive testing

**Deliverable:** Complete supporting resources and polished site

---

### Phase 5: Testing & Launch (Days 9-10)
**Goal:** Final testing and production deployment

**Tasks:**
- [ ] Comprehensive link testing (all internal/external links)
- [ ] Mobile device testing (iOS, Android)
- [ ] Browser testing (Chrome, Safari, Firefox, Edge)
- [ ] Search functionality testing
- [ ] Load time optimization
- [ ] Accessibility testing (WCAG 2.1 AA compliance)
- [ ] Internal stakeholder review
- [ ] Fix any issues found
- [ ] Final deployment to production
- [ ] Update links in other CyberPools materials
- [ ] Announcement to stakeholders

**Deliverable:** Live production site at https://frankbejar.github.io/CyberPools-RA-Report/

---

## Key Decisions Needed

Before starting implementation, answer these questions:

### 1. Content Scope
**Question:** Do you want ALL documents public (including grading methodology technical details)?

**Options:**
- [ ] **Option A:** Everything public (full transparency)
- [ ] **Option B:** Hide technical grading details (keep high-level only)
- [ ] **Option C:** Create password-protected section for assessors

**Recommendation:** Option A - Full transparency builds credibility with carriers and risk managers

---

### 2. Branding Assets
**Question:** Do you have specific CyberPools brand assets?

**Needed:**
- [ ] CyberPools logo (PNG/SVG) for header
- [ ] Favicon (small logo for browser tab)
- [ ] Brand color codes (Primary Navy: #003B5C confirmed?)
- [ ] Any other brand guidelines

**Location for assets:** `docs/assets/images/`

---

### 3. Tone & Audience Level
**Question:** What level of technical detail?

**Options:**
- [ ] **Technical:** Deep technical detail for security professionals
- [ ] **Balanced:** Mix of technical and business context
- [ ] **Simplified:** High-level for executives and non-technical stakeholders

**Recommendation:** Balanced - Technical where needed (grading formulas) but accessible language for broader audience

---

### 4. Interactivity Level
**Question:** How interactive should the site be?

**Features to consider:**
- [ ] Filterable/sortable question tables
- [ ] Expandable question cards
- [ ] Framework mapping matrix (interactive table)
- [ ] Grading calculator (input scores, see grade)
- [ ] Question search with autocomplete

**Recommendation:** Start with basic filtering/sorting, add interactivity in future iterations

---

### 5. Assessor Guidance
**Question:** Should there be assessor-specific content?

**Options:**
- [ ] **Public:** Assessment guidance visible to all
- [ ] **Private:** Separate assessor portal (requires authentication)
- [ ] **None:** Exclude assessor-specific content

**Recommendation:** Public guidance helps organizations prepare, builds transparency

---

### 6. Timeline
**Question:** When do you need this live?

**Options:**
- [ ] **Aggressive:** 1 week (basic functionality)
- [ ] **Standard:** 2 weeks (full features)
- [ ] **Comprehensive:** 3-4 weeks (full features + polish + testing)

**Current estimate:** 10 days based on implementation phases above

---

### 7. Maintenance Approach
**Question:** How will you update this site?

**Options:**
- [ ] **Automated:** Python script regenerates all pages from master docs
- [ ] **Semi-automated:** Script for questions, manual for other pages
- [ ] **Manual:** Direct editing of markdown files

**Recommendation:** Automated for questions (most frequent updates), manual for other content

---

## File Structure (Proposed)

```
cyberpools/risk-assessment/
├── mkdocs.yml                           # MkDocs configuration
├── requirements-docs.txt                 # Python dependencies
├── scripts/
│   └── build_mkdocs_site.py             # Auto-generation script
├── docs/                                 # MkDocs content
│   ├── index.md                         # Home page
│   ├── stylesheets/
│   │   └── extra.css                    # Custom CSS
│   ├── assets/
│   │   └── images/
│   │       ├── cp-logo.png              # CyberPools logo
│   │       └── favicon.png              # Browser icon
│   ├── getting-started/
│   │   ├── overview.md
│   │   └── how-to-navigate.md
│   ├── questions/
│   │   ├── all-questions.md             # All 57 questions table
│   │   ├── tier-1a.md                   # 10 TIER 1A questions
│   │   ├── tier-1b.md                   # 7 TIER 1B questions
│   │   ├── category-1.md                # Inventory
│   │   ├── category-2.md                # Account Management
│   │   ├── category-3.md                # Data Protection
│   │   ├── category-4.md                # Secure Configuration
│   │   ├── category-5.md                # Malware Defense
│   │   ├── category-6.md                # Data Recovery
│   │   ├── category-7.md                # Security Awareness
│   │   ├── category-8.md                # Vendor Management
│   │   ├── category-9.md                # Incident Response
│   │   └── category-10.md               # Policies
│   ├── tier-framework/
│   │   ├── overview.md                  # TIER explained
│   │   ├── tier-1a-explained.md
│   │   ├── tier-1b-explained.md
│   │   └── insurance-research.md
│   ├── grading/
│   │   ├── executive-summary.md         # Grade Ceiling approach
│   │   ├── how-scoring-works.md
│   │   ├── grade-boundaries.md
│   │   ├── examples.md
│   │   └── technical-details.md
│   ├── frameworks/
│   │   ├── cis-controls.md              # CIS v8.1 IG1 mapping
│   │   ├── nist-csf.md                  # NIST CSF 2.0 mapping
│   │   └── gap-analysis.md
│   ├── assessors/
│   │   ├── guidance.md
│   │   ├── question-intent.md
│   │   └── evidence-collection.md
│   ├── resources/
│   │   ├── citations.md
│   │   ├── glossary.md
│   │   ├── faq.md
│   │   └── version-history.md
│   └── about/
│       ├── cyberpools.md
│       ├── contact.md
│       └── feedback.md
└── 2026 RA/                              # Source documents (unchanged)
    ├── 2026_RA_QUESTION_SET_v6.2_FINAL.md
    ├── 2026_RA_TIER_FRAMEWORK_JUSTIFICATION.md
    ├── GRADING_METHODOLOGY_EXECUTIVE_R2.md
    └── GRADING_METHODOLOGY_TECHNICAL_SUPPLEMENT.md
```

---

## Next Steps (To Start Tomorrow)

### Immediate Actions:

1. **Review & Decide:**
   - [ ] Review this plan
   - [ ] Answer the 7 key decisions above
   - [ ] Gather CyberPools logo/brand assets
   - [ ] Confirm timeline expectations

2. **Environment Setup:**
   - [ ] Install MkDocs: `pip install mkdocs mkdocs-material pymdown-extensions`
   - [ ] Test MkDocs works: `mkdocs --version`
   - [ ] Navigate to project: `cd /Users/frankbejar/Documents/GitHub/cyberpools/risk-assessment`

3. **Start Phase 1:**
   - [ ] Create new `mkdocs.yml` configuration
   - [ ] Set up folder structure
   - [ ] Test local preview: `mkdocs serve`

### Commands to Remember:

```bash
# Preview site locally
mkdocs serve
# Opens at http://127.0.0.1:8000

# Build site (generates site/ directory)
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy

# Build script (once created)
python scripts/build_mkdocs_site.py
```

---

## Resources & References

### Documentation:
- **MkDocs:** https://www.mkdocs.org/
- **Material for MkDocs:** https://squidfunk.github.io/mkdocs-material/
- **GitHub Pages:** https://docs.github.com/en/pages

### Source Documents:
- Located in: `/Users/frankbejar/Documents/GitHub/cyberpools/risk-assessment/2026 RA/`
- Master: `2026_RA_QUESTION_SET_v6.2_FINAL.md`
- TIER Justifications: `2026_RA_TIER_FRAMEWORK_JUSTIFICATION.md`
- Grading Executive: `GRADING_METHODOLOGY_EXECUTIVE_R2.md`
- Grading Technical: `GRADING_METHODOLOGY_TECHNICAL_SUPPLEMENT.md`

### Current Site:
- **URL:** https://frankbejar.github.io/CyberPools-RA-Report/
- **Repository:** https://github.com/frankbejar/CyberPools-RA-Report

---

## Success Criteria

### Site is considered successful when:

**Functionality:**
- [ ] All 57 questions are documented and accessible
- [ ] TIER classifications are clear and justified
- [ ] Grading methodology is explained (executive + technical levels)
- [ ] Framework mappings are complete and accurate
- [ ] Search works across all content
- [ ] All links are functional (no 404s)
- [ ] Mobile-responsive on all devices

**Content Quality:**
- [ ] Aligned with v6.2 FINAL master documents
- [ ] Sector-neutral language throughout
- [ ] Accurate citations and sources
- [ ] Clear, professional writing
- [ ] Consistent formatting and style

**User Experience:**
- [ ] Easy to find specific questions
- [ ] Clear navigation for different audiences
- [ ] Fast load times (<3 seconds)
- [ ] Professional appearance
- [ ] Accessible (WCAG 2.1 AA compliance)

**Maintainability:**
- [ ] Automated generation from master docs
- [ ] Clear update workflow documented
- [ ] Version control integrated
- [ ] Easy to regenerate when content changes

---

## Questions & Notes

**Questions for tomorrow's session:**
1. Brand assets available?
2. Timeline preference?
3. Content scope decisions?
4. Any specific requirements not covered?

**Notes:**
- Current site is outdated (65 questions, 9 categories) - complete rebuild needed
- All master documents verified and production-ready (November 19, 2025)
- GitHub Actions workflow will auto-deploy on push to main branch
- Material for MkDocs provides excellent built-in search and navigation

---

**Status:** Ready for implementation
**Next Session:** Start Phase 1 - Foundation setup
**Estimated Completion:** 10 days for full implementation
