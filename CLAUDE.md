# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains **TWO major systems**:

1. **PDF Report Generator** - Production system that generates branded PDF reports from CRM assessment data
2. **MkDocs Documentation Site** - Public-facing documentation site for the 65-question comprehensive risk assessment questionnaire

Both systems share the same assessment content but serve different purposes and audiences.

---

## ⚠️ CRITICAL: Production vs. POC Separation Policy

**ALWAYS maintain strict separation between production and proof-of-concept work:**

### Production Files (Main Directory)
- `scripts/` - Production report generation
- `templates/` - Production report templates
- `styles/` - Production CSS
- `content/boilerplate.json` - Production text
- `mappings/` - Production question/category mappings
- `input/` - Production assessment data
- `output/` - Production generated reports

### POC/Research Files (`poc-research/` Directory)
- Research documents and analysis
- Alternative grading model concepts
- Experimental scripts and templates
- Strategic planning documents
- Insurance market research
- Gap analysis and recommendations

**🚨 RULE: When doing research, exploring ideas, or analyzing alternatives, ALWAYS place documents in `poc-research/docs/`**

**Examples:**
- ✅ Grading model options → `poc-research/docs/`
- ✅ Insurance market research → `poc-research/docs/`
- ✅ Alternative assessment approaches → `poc-research/docs/`
- ✅ Strategic recommendations → `poc-research/docs/`
- ❌ NEVER put POC concepts in `content/boilerplate.json`
- ❌ NEVER mix experimental code with production scripts

**Why this matters:** The production system serves live members. Mixing POC concepts with production files creates confusion about what's deployed vs. what's being explored.

---

## Project Overview

CyberPools Risk Assessment Report Generator - A professional PDF report generation system that transforms raw CRM assessment data into polished, branded PDF reports for cybersecurity risk assessments.

**Technology Stack:**
- Python 3.9+ with Jinja2 templating
- DocRaptor (Prince XML) or Playwright for PDF rendering
- Microsoft Dynamics 365 CRM data integration

## Common Commands

### MkDocs Documentation Site

**Preview site locally:**
```bash
pip install -r requirements-docs.txt
mkdocs serve  # Opens at http://127.0.0.1:8000
```

**Build static site:**
```bash
mkdocs build  # Output in site/ directory
```

**Rebuild from source questionnaire:**
```bash
# After updating poc-research/docs/COMPREHENSIVE_RISK_ASSESSMENT_QUESTIONNAIRE.md
python3 scripts/build_docs_site.py
git add docs/
git commit -m "Update questionnaire content"
git push  # Auto-deploys to GitHub Pages
```

**Deploy to GitHub Pages:**
```bash
mkdocs gh-deploy  # Manual deployment (usually automatic via GitHub Actions)
```

**Live site:** https://frankbejar.github.io/CyberPools-RA-Report/

### Generate Production Reports

**Using Metadata Script (Recommended for custom reports):**
```bash
python3 scripts/generate_report_with_metadata.py \
  --input "input/CBS-School.json" \
  --member-name "School Name" \
  --assessment-date "10/15/2025" \
  --conducted-by "Assessor Name" \
  --member-contact "Contact Name" \
  --executive-summary "Summary text with **markdown** support..." \
  --outro-page \
  --production
```

**Using Transform Script (Original workflow):**
```bash
# Interactive mode (prompts for all options)
python3 scripts/transform_and_generate.py

# Automated mode (no prompts)
python3 scripts/transform_and_generate.py \
  --input input/CBS-School.json \
  --auto \
  --engine docraptor \
  --output output/report.pdf
```

**Batch Generate All CBS Reports:**
```bash
./scripts/generate_all_cbs_reports.sh
```

### Generate AI Executive Summaries

```bash
# Requires OPENAI_API_KEY in .env file
python3 scripts/suggest_summary.py --input input/CBS-CBS.json --tone professional
```

### Update Cyber Requirements Flags

```bash
# Run this whenever the "Cyber Requirements" list changes
# Updates qReq flags in all CBS-*.json files to match compliance table
python3 scripts/update_cyber_requirements.py
```

## Architecture Overview

### System 1: MkDocs Documentation Site

**Purpose:** Public-facing, searchable documentation for the 65-question comprehensive risk assessment questionnaire.

**Architecture:**
1. **Source of Truth:** `poc-research/docs/COMPREHENSIVE_RISK_ASSESSMENT_QUESTIONNAIRE.md` (6,450 lines, 65 questions)
2. **Build Script:** `scripts/build_docs_site.py` parses source and generates organized pages
3. **Generated Pages:** Split into `docs/` directory structure:
   - 9 category pages (`docs/categories/category-*.md`)
   - 3 filtered views (`docs/filtered/foundational.md`, `new-questions.md`, `high-impact.md`)
   - 4 sector pages (`docs/sectors/education.md`, etc.)
   - Reference materials (`docs/reference/`)
4. **Configuration:** `mkdocs.yml` defines site structure, theme, navigation
5. **Deployment:** GitHub Actions (`.github/workflows/docs.yml`) auto-deploys to GitHub Pages on push

**Key Features:**
- Full-text search across all questions
- Tag-based filtering (category, impact, foundational, new, sector)
- Mobile-responsive Material Design theme
- Dark/light mode toggle
- Automatic deployment on content changes

**Update Workflow:**
```
Edit COMPREHENSIVE_RISK_ASSESSMENT_QUESTIONNAIRE.md
  → Run build_docs_site.py
  → Commit changes
  → GitHub Actions deploys to https://frankbejar.github.io/CyberPools-RA-Report/
```

---

### System 2: PDF Report Generator

**Purpose:** Generate branded PDF reports for individual member assessments from CRM data.

### Data Flow Pipeline

1. **Input Data** → CRM exports raw assessment data as JSON (`input/*.json`)
2. **Transformation** → Python scripts transform and score the data using mappings
3. **Template Rendering** → Jinja2 renders HTML from templates with transformed data
4. **PDF Generation** → DocRaptor or Playwright converts HTML to PDF
5. **Output** → Final branded PDF saved to `output/` directory

### Core Data Model

**CRM Question Record Structure:**
```json
{
  "qID": "unique-guid",
  "qCat": 772120001,           // Category ID (maps via category_mapping.json)
  "qResponse": 1,              // Control Rating: 1=Fully, 3=Partial, 5=Not Implemented
  "qScore": 5,                 // Impact Rating: 1=Low, 3=Moderate, 5=High
  "qNotes": "Assessment notes",
  "qReq": true                 // Is this a "Cyber Requirement"? (12 questions map to 7 Trust requirements)
}
```

**Risk Scoring Formula:**
```
Risk Score = Control Rating (1/3/5) × Impact Rating (1/3/5)
- Low Risk: 0-9
- Moderate Risk: 10-15
- High Risk: 16-25
```

### The Trust Requirements Integration

**Important Context:**
- The Trust (insurance pool) has **7 simplified cyber requirements**
- CyberPools maps **12 questions** from the 51-question assessment to these 7 requirements
- Questions with `qReq: true` appear in the "Cyber Requirements" compliance table
- The 12 question numbers are hardcoded in `COMPLIANCE_QUESTION_NUMBERS` set in `transform_and_generate.py`

**The 12 Questions mapping to 7 Trust Requirements:**
- 1.4: End-of-life software management
- 2.3-2.6: MFA (4 questions covering different systems)
- 4.3: Patch management
- 4.7: External vulnerability scanning
- 5.4: EDR implementation
- 6.3: Air-gapped backups
- 6.4: Backup testing frequency
- 7.2: Phishing testing
- 7.3: Security awareness training

### Key Python Scripts

**`scripts/transform_and_generate.py`** (Main CLI)
- Entry point for report generation
- Transforms raw CRM JSON into scored assessment data
- Handles interactive prompts or automated mode
- Orchestrates the entire pipeline

**`scripts/generate_report_with_metadata.py`** (Metadata CLI)
- Newer interface for custom reports with explicit metadata
- Supports markdown in executive summaries (`**bold**` syntax)
- Optional outro page with services/contact info

**`scripts/generate_report.py`** (Template Renderer)
- Non-interactive renderer
- Takes pre-transformed data structure
- Renders Jinja2 templates to HTML

**`scripts/generate_pdf_docraptor.py`** (DocRaptor Renderer)
- Inlines CSS for DocRaptor API
- Converts HTML to PDF via Prince XML engine
- Supports running headers/footers via @page rules

**`scripts/generate_pdf_playwright.py`** (Playwright Renderer)
- Alternative free/offline PDF renderer
- Uses Chromium print-to-PDF
- Less sophisticated page break handling

**`scripts/suggest_summary.py`** (AI Summary Generator)
- Uses GPT-3.5 Turbo to generate risk-focused executive summaries
- Interactive CLI with regenerate/edit/tone options

### Mapping Files

**`mappings/category_mapping.json`**
- Maps CRM category IDs (e.g., `772120001`) to category numbers/names
- 9 categories: Inventory, Account Management, Data Protection, Secure Configuration, Malware Defense, Data Recovery, Security Awareness, Vendor Management, Incident Response

**`mappings/question_mapping.json`**
- Maps question GUIDs to question numbers (e.g., "2.3", "4.7")
- Contains full question text and metadata

**`content/boilerplate.json`**
- Production boilerplate text for report sections
- Category overviews and importance statements
- Rating legends and methodology descriptions
- **Production file - DO NOT mix with POC concepts**

### Template Structure

**`templates/main_template.html`**
- Master template that includes all partials
- Handles CSS/styling injection

**`templates/partials/`**
- `cover.html` - Cover page with member name/date
- `introduction.html` - Assessment methodology
- `executive_summary.html` - Optional custom summary (supports markdown)
- `results_summary.html` - Overall score and category breakdown
- `rating_legends.html` - Scoring formula explanation
- `findings.html` - Key findings (auto-generated high/moderate risks)
- `cyber_requirements.html` - The Trust's 7 requirements compliance table
- `category.html` - Category details with questions
- `question.html` - Individual question block

### Styling System

**`styles/main.css`** - Base styles for all renderers

**`styles/print_docraptor.css`** - DocRaptor/Prince XML specific
- @page rules for headers/footers/page numbers
- Page break control (avoid-break-inside, page-break-before)
- Prince XML-specific CSS extensions

**`styles/print.css`** - Playwright specific
- Chromium print media queries
- Manual header/footer implementation

**Grade Color System:**
- A: Dark Green (#2F5233)
- B: Light Green (#4D8B31)
- C: Orange (#EC7A08)
- D: Dark Orange (#C46100)
- F: Red (#C9190B)

## POC Research Folder

**`poc-research/`** directory contains:
- Proof-of-concept grading models (two-tier, weighted scoring)
- Research documentation on alternative assessment approaches
- POC scripts and templates
- Strategic planning and insurance market research
- **⚠️ NOTHING in this folder is production code or deployed**

**Important:** The production system uses a **single overall score (0-100%)** with 51 questions across 9 categories. POC work explores dual-score models and alternative weightings but these are NOT deployed.

**Key POC Documents:**
- `poc-research/README.md` - POC overview and status
- `poc-research/docs/ACTUAL_GRADING_OPTIONS.md` - Analysis of 4 grading model options for 2026
- `poc-research/docs/INSURANCE_STRATEGIC_ASSESSMENT_EXECUTIVE_SUMMARY.md` - Insurance industry research and recommendations
- `poc-research/docs/GRADING_MODEL_APPROACHES.md` - Comprehensive grading model documentation

**🚨 REMINDER: When Claude generates research, ideas, or strategic analysis, it must be saved to `poc-research/docs/`, NOT the main directory.**

## Key Workflows

### MkDocs Site: Updating Documentation Content

**When to rebuild docs:**
- Added/modified questions in comprehensive questionnaire
- Changed question metadata (foundational status, impact ratings, sector guidance)
- Updated framework mappings or citations

**Process:**
1. Edit `poc-research/docs/COMPREHENSIVE_RISK_ASSESSMENT_QUESTIONNAIRE.md`
2. Run `python3 scripts/build_docs_site.py` to regenerate all pages
3. Review changes: `mkdocs serve` to preview locally
4. Commit: `git add docs/ && git commit -m "Update questionnaire"`
5. Push: `git push` → GitHub Actions auto-deploys in ~30 seconds

**Common link issues:**
- Use relative links without `../` prefix in MkDocs (e.g., `filtered/foundational.md` not `../filtered/foundational.md`)
- Check build warnings: `mkdocs build` shows broken links
- Test navigation after changes

### MkDocs Site: Modifying Layout/Navigation

1. Edit `mkdocs.yml` to change navigation structure
2. Edit `docs/stylesheets/extra.css` for custom styling
3. Edit `scripts/build_docs_site.py` if changing page generation logic
4. Test build: `mkdocs build` (check for warnings)
5. Preview: `mkdocs serve`
6. Commit and push for auto-deployment

### PDF Reports: Adding a New Question

1. Add question to CRM (Dynamics 365)
2. Update `mappings/question_mapping.json` with new question GUID and metadata
3. Update `mappings/category_mapping.json` if new category added
4. If it's a Cyber Requirement question, add to `COMPLIANCE_QUESTION_NUMBERS` set in `transform_and_generate.py`
5. Run `scripts/update_cyber_requirements.py` to update all input JSON files
6. Update `content/boilerplate.json` if new category added

### PDF Reports: Modifying Report Layout

1. Edit templates in `templates/partials/` for content structure
2. Edit `styles/main.css` for base styling
3. Edit `styles/print_docraptor.css` for DocRaptor-specific print rules
4. Edit `styles/print.css` for Playwright-specific print rules
5. Test with both renderers: `--engine docraptor` and `--engine playwright`

### Updating Boilerplate Text

1. Edit `content/boilerplate.json`
2. Regenerate reports - text updates automatically via templates
3. **Never put POC/experimental text in this file** - use `poc-research/` for concept work

## PDF Rendering Engines

**DocRaptor (Recommended):**
- Superior CSS paged media support
- Running headers/footers with page numbers
- Better page break control
- Requires API key: `export DOCRAPTOR_API_KEY="your_key"`
- Free tier: unlimited test (watermarked) PDFs
- Production: `test_mode=False` in DocRaptorPDF constructor

**Playwright (Alternative):**
- Free and open source
- Works offline
- Limited paged media support
- Requires: `playwright install chromium`

## Testing

**Quick DocRaptor Test:**
```bash
python3 scripts/quick_docraptor_test.py
```

**Full DocRaptor Test:**
```bash
python3 scripts/test_docraptor.py
```

## Important Notes

### Cyber Requirements vs. All Questions
- The assessment has **51 total questions** across 9 categories
- **12 of these questions** are marked as "Cyber Requirements" (`qReq: true`)
- These 12 questions map to **7 simplified requirements** from The Trust insurance pool
- The compliance table shows these 12 questions separately for insurance reporting
- Do not confuse "12 questions" with "7 requirements" - both numbers are correct in different contexts

### Grade Rounding
- Overall and category percentages use standard half-up rounding
- Example: 80.5 → 81% (mirrors CRM dashboard behavior)
- Implemented via `Decimal.quantize(ROUND_HALF_UP)`

### Markdown Support
- Executive summaries support `**bold**` markdown syntax
- Converted via `markdown` library if available
- Falls back to plain text if library not installed

### Production vs. POC Code Separation

**STRICT SEPARATION POLICY:**

**Production (Main Directory):**
- Deployed code serving live members
- All files in main directory are production
- `content/boilerplate.json` = production text only
- Never mix POC concepts here

**POC/Research (`poc-research/`):**
- Research documents and analysis
- Alternative grading models (dual-score, weighted, threshold-based)
- Strategic planning and market research
- Experimental scripts and templates
- Nothing here is deployed

**When Claude does research or creates strategic documents:**
- ✅ Save to `poc-research/docs/`
- ✅ Use `poc-research/scripts/` for experimental code
- ✅ Use `poc-research/templates/` for POC templates
- ❌ Never save to main directory
- ❌ Never edit `content/boilerplate.json` with POC text

**This separation is critical** - production system serves live members and must not contain undeployed concepts.

## Environment Variables

```bash
# DocRaptor API key (optional, has default test key)
export DOCRAPTOR_API_KEY="your_api_key_here"

# OpenAI API key (for AI summary generation)
export OPENAI_API_KEY="your_openai_key"
```

## Dependencies

**PDF Report Generator:**
- jinja2 - Template rendering
- docraptor - DocRaptor API client
- playwright (optional) - Chromium PDF renderer
- markdown (optional) - Markdown to HTML conversion for summaries
- openai (optional) - AI summary generation

Install: `pip install -r docs/requirements.txt`

**MkDocs Documentation Site:**
- mkdocs >= 1.5.0
- mkdocs-material >= 9.5.0
- pymdown-extensions >= 10.0

Install: `pip install -r requirements-docs.txt`

## Repository File Structure

```
cyberpools-RA-Report/
├── .github/workflows/docs.yml    # GitHub Actions for auto-deployment
├── mkdocs.yml                     # MkDocs site configuration
├── requirements-docs.txt          # MkDocs dependencies
│
├── docs/                          # MkDocs site (generated, committed to git)
│   ├── index.md                   # Home page
│   ├── categories/                # 9 category pages
│   ├── filtered/                  # Filtered views (foundational, new, high-impact)
│   ├── sectors/                   # 4 sector-specific pages
│   ├── reference/                 # Citations, framework mapping
│   ├── stylesheets/extra.css      # Custom CSS
│   └── README.md                  # Docs build instructions
│
├── poc-research/                  # POC/Research (non-production)
│   └── docs/
│       └── COMPREHENSIVE_RISK_ASSESSMENT_QUESTIONNAIRE.md  # SOURCE OF TRUTH
│
├── scripts/
│   ├── build_docs_site.py         # Generates MkDocs pages from source
│   ├── transform_and_generate.py  # Main PDF report CLI
│   ├── generate_report_with_metadata.py  # Metadata-based PDF CLI
│   └── suggest_summary.py         # AI summary generator
│
├── templates/                     # Jinja2 templates for PDF reports
├── styles/                        # CSS for PDF reports
├── content/boilerplate.json       # Production boilerplate text
├── mappings/                      # Question/category mappings for CRM
├── input/                         # CRM assessment data (JSON)
└── output/                        # Generated PDF reports
```
