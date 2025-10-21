# CyberPools Risk Assessment Report Generator

Modern Playwright/Jinja2 pipeline for producing the CyberPools branded Risk Assessment PDF from CRM exports.

---

## 1. What This Project Does

1. **Inputs** raw CRM question data (`input/*.json`) and CyberPools mapping files (`mappings/*.json`).
2. **Transforms** the raw records into the report data model (`metadata`, scoring, categories, cyber requirements).
3. **Renders** Jinja2 HTML templates (`templates/`) into a complete multi-page report.
4. **Prints to PDF** via headless Chromium (Playwright). WeasyPrint remains an optional fallback.

Result: a polished PDF in `output/` ready to share with members or carriers.

---

## 2. Repository Layout (Current)

```
cyberpools-report/
├── content/                 # Boilerplate descriptive text (JSON)
│   └── boilerplate.json
├── docs/                    # User + maintainer documentation (this folder)
│   ├── readme_setup.md                # This file - main setup guide
│   ├── file_organization_master.txt   # Repository map
│   ├── template_guide.txt             # Template variable reference
│   ├── mac_readme_stepbystep.txt      # Step-by-step setup for new engineers
│   ├── mac_auto_setup.sh              # Automated setup script
│   └── requirements.txt               # Python dependencies
├── example /                # Design reference files
│   └── CyberPools-Style Guide.html    # Official style guide (colors, typography, components)
├── input/                   # Raw CRM JSON exports (source data)
│   └── cb-ra.json           # Example/actual assessment data
├── logo/                    # Brand assets (currently unused - text branding on cover)
│   └── cp-white-logo.png
├── mappings/                # Question + category metadata lookup tables
│   ├── category_mapping.json         # Category IDs to section numbers/names
│   └── question_mapping.json         # Question GUIDs to text/impact
├── output/                  # Generated PDF reports (gitignored)
│   ├── Sample_Organization_Risk_Assessment_[date].pdf
│   └── example-reference.pdf
├── scripts/                 # Python utilities and CLIs
│   ├── transform_and_generate.py   # PRIMARY CLI (transform raw CRM → PDF)
│   ├── generate_pdf_playwright.py  # Playwright renderer wrapper
│   ├── generate_report.py          # Render from pre-transformed JSON
│   └── run.sh                      # macOS/Linux convenience wrapper
├── styles/                  # Shared styling (CSS design system)
│   ├── main.css             # Core design tokens, components, layout
│   └── print.css            # PDF/print overrides for Chromium
└── templates/               # Jinja2 HTML templates
    ├── main_template.html   # Master composition template
    └── partials/            # Modular sections (9 files)
        ├── cover.html                # Cover page with CYBERPOOLS branding
        ├── introduction.html         # Assessment overview
        ├── executive_summary.html    # Executive summary (optional)
        ├── results_summary.html      # Overall score + risk distribution grid
        ├── rating_legends.html       # Risk level definitions
        ├── high_risk_findings.html   # Critical findings (conditional)
        ├── cyber_requirements.html   # Mandatory controls table
        ├── category.html             # Category page layout
        └── question.html             # Individual control/question block
```

---

## 3. Requirements & Installation

### 3.1 Prerequisites
* macOS or Windows with Python 3.9+
* `pip` available on PATH
* Chromium downloaded by Playwright (see below)

### 3.2 Install Python Packages
From the repository root:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r docs/requirements.txt
```
The requirements file includes:
* `Jinja2`, `MarkupSafe` – template rendering
* `playwright` – default PDF engine
* `WeasyPrint` and supporting packages – optional fallback

### 3.3 Install the Playwright Chromium Bundle
```bash
python3 -m playwright install chromium
```
This only has to be done once per machine/user.

> **Tip:** If corporate policies block downloads, coordinate with IT to pre-install the browser bundle.

---

## 4. Quick Start – Generate a Report

### 4.1 Auto Mode (No Prompts)
1. **Place input data**
   * Raw CRM export JSON inside `input/` (e.g., `input/cb-ra.json`).
   * Ensure `mappings/question_mapping.json` and `mappings/category_mapping.json` are current.
2. **Optional:** update `content/boilerplate.json` with any revised copy.
3. **Run the generator** from the project root:
   ```bash
   python3 scripts/transform_and_generate.py --input input/cb-ra.json --auto
   ```
   * `--auto` populates metadata placeholders with defaults and skips all interactive prompts
   * Defaults: High + Moderate risk findings included in report
   * Use `--engine weasyprint` to switch to the WeasyPrint backend (Playwright is default)
   * When prompted for the executive summary you can enter Markdown (bold, lists, headings); the CLI converts it to HTML in the PDF.
4. **Find the PDF** in `output/`. File name pattern:
   `Sample_Organization_Risk_Assessment_10-20-2025.pdf`

### 4.2 Interactive Mode (With Prompts)
For more control, **omit the `--auto` flag**:
```bash
python3 scripts/transform_and_generate.py --input input/cb-ra.json
```

**Interactive prompts will ask you to:**
1. Enter assessment metadata (member name, date, conducted by, contact)
2. Optionally provide an executive summary
3. **Choose which risk levels to display in Findings section:**
   - Option 1: High risk only
   - Option 2: High + Moderate risk (default)
   - Option 3: All findings (High + Moderate + Low)
   - Option 4: Preview all findings before deciding
4. **Review findings preview** - see exactly what will be included
5. **Confirm PDF generation** before rendering

This mode lets you review findings and approve before generating the final PDF.

---

## 5. Input Data & Mapping Expectations

* **Raw CRM export (`input/*.json`)** – array of question responses from the CRM. Each record should include:
  * `qID` (CRM GUID), `qCat` (category ID), `qResponse`, `qScore`, `qNotes`, etc.
  * `qReq` flag identifies mandatory controls for the compliance table.

* **Mappings (`mappings/question_mapping.json`)** – defines number, text, impact, description for each `qID`. Must cover every GUID present in the CRM export.

* **Category mapping (`mappings/category_mapping.json`)** – maps CRM category IDs to the branded numbering (1.0–9.0) and labels.

* **Boilerplate (`content/boilerplate.json`)** – reusable copy for introduction, category overviews, importance messaging, etc.

Scripts will warn (but continue) if mappings are missing and will fall back to "Unknown Question/Category" placeholders.

---

## 6. Templating & Styling Highlights

* **Templates** (`templates/partials/*.html`) drive the report layout. Jinja2 context keys are detailed in `docs/template_guide.txt`.
* **styles/main.css** sets the design system – color tokens, progress bars, risk badges, grid layouts, etc.
  * Recent update: Summary of Results uses a 4-column horizontal grid (overall score + 3 risk distribution boxes) for compact layout
* **styles/print.css** enforces page breaks, ensures background colors print, and keeps question blocks intact when possible.
* **Cover page branding**: Uses "CYBERPOOLS" text (56px, bold, white, 4px letter-spacing) instead of logo image
* The default design shows a progress bar on the Summary page and omits on-page footers to reduce clutter.

To adjust layout, edit the partial and rerun the generator. No rebuild step is required.

---

## 7. Utility Scripts

| Script | Purpose |
| --- | --- |
| `scripts/transform_and_generate.py` | **PRIMARY CLI** - Transform raw CRM JSON to PDF. Supports `--input`, `--auto`, `--engine`, and `--ci` flags. |
| `scripts/generate_report.py` | Render straight from a pre-transformed JSON object (skips CRM transform step). |
| `scripts/generate_pdf_playwright.py` | Playwright PDF renderer wrapper class. Used by the above scripts. |
| `scripts/run.sh` | macOS/Linux convenience wrapper; checks Python version and installs dependencies if missing. |

---

## 8. Troubleshooting

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'playwright'` | Python env missing dependencies | Re-run `pip install -r docs/requirements.txt`. |
| `Error: Failed to launch browser` | Chromium not installed / blocked | Run `python3 -m playwright install chromium`. If blocked, request IT to download the bundle. |
| Questions show “Unknown Question” | Mapping file missing GUID | Update `mappings/question_mapping.json` with the new question metadata. |
| Bad page breaks | Print CSS conflict | Tweak `styles/print.css` rules (`page-break-inside`, `page-break-after`) or adjust content flow. |
| Need custom text | Edit `content/boilerplate.json` and re-run the generator. |

---

## 9. Next Steps & Support
* For template variables: see `docs/template_guide.txt`.
* For new engineers: use `docs/mac_readme_stepbystep.txt` for a guided setup.
* Questions? Email the CyberPools tooling team at **cyber@cyberpools.org**.

---

## 10. Recent Updates (October 2025)

* **NEW: Interactive findings selection** - Choose which risk levels (High, Moderate, Low) to include in the Findings section with preview before PDF generation
* **Removed deprecated scripts**: `split_example_html.py`, `export_example_pdf.py` (legacy utilities no longer needed)
* **Removed legacy example files**: `example/split/` folder, `CBS-RA-V1.html` (templates are now the canonical source)
* **Cover page update**: Switched from logo image to "CYBERPOOLS" text branding for consistent rendering
* **Summary page redesign**: Implemented 4-column horizontal grid layout for overall score + risk distribution (more compact, fits on one page)
* **Kept for reference**: `example/CyberPools-Style Guide.html` (active design system documentation)

This README reflects the project state as of **October 20, 2025**. Update it whenever scripts, dependencies, or templates change.
