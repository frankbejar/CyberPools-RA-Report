# CyberPools Risk Assessment Report Generator

Professional PDF report generation system for CyberPools Risk Assessments, powered by Jinja2 templates and DocRaptor/Playwright rendering engines.

---

## Overview

This project transforms raw CRM assessment data into polished, branded PDF reports with:
- **Professional layout** with running headers/footers and page numbers
- **Intelligent page breaks** that keep content logically grouped
- **Full-color output** with gradients, charts, and visual elements
- **Flexible rendering** via DocRaptor (Prince XML) or Playwright (Chromium)

### What It Does

1. **Inputs** raw CRM question data (`input/*.json`) and mapping files (`mappings/*.json`)
2. **Transforms** records into structured report data (metadata, scoring, categories)
3. **Renders** Jinja2 HTML templates into a complete multi-page report
4. **Generates PDF** via DocRaptor API or local Playwright

**Result:** A production-ready PDF in `output/` with proper pagination, headers, and styling.

---

## Quick Start

### Prerequisites
- Python 3.9+
- DocRaptor API key (recommended) OR Playwright installed

### Installation

```bash
# Install Python dependencies
pip install -r docs/requirements.txt

# For Playwright (optional)
playwright install chromium

# For DocRaptor (recommended)
pip install docraptor
export DOCRAPTOR_API_KEY="your_api_key_here"
```

### Generate a Report

**Using DocRaptor (Recommended):**
```bash
python3 scripts/transform_and_generate.py \
  --input input/cb-ra.json \
  --auto \
  --engine docraptor \
  --output output/report.pdf
```

**Using Playwright:**
```bash
python3 scripts/transform_and_generate.py \
  --input input/cb-ra.json \
  --auto \
  --engine playwright
```

---

## PDF Rendering Engines

### DocRaptor (Prince XML) - Recommended

**Advantages:**
- Superior CSS paged media support (@page with margin boxes)
- Running headers/footers with automatic page numbers
- Better page break control and widow/orphan handling
- Excellent gradient and modern CSS support
- No local dependencies required

**Setup:** See [docs/DOCRAPTOR_SETUP.md](docs/DOCRAPTOR_SETUP.md)

**Pricing:**
- Test mode: Unlimited watermarked PDFs (free)
- Production: 5 free PDFs/month, then $15/month for 125 documents

### Playwright (Chromium) - Alternative

**Advantages:**
- Free and open source
- No external API dependencies
- Works offline

**Limitations:**
- Limited CSS paged media support
- Manual header/footer implementation required
- Less sophisticated page break handling

---

## Project Structure

```
cyberpools-RA-Report-1/
├── content/                    # Boilerplate content (JSON)
│   └── boilerplate.json
├── docs/                       # Documentation
│   ├── DOCRAPTOR_QUICKSTART.md
│   ├── DOCRAPTOR_SETUP.md
│   ├── DOCRAPTOR_USAGE.md
│   ├── readme_setup.md
│   └── requirements.txt
├── example/                    # Style guide reference
│   └── CyberPools-Style Guide.html
├── input/                      # Raw CRM data (JSON)
│   └── cb-ra.json
├── mappings/                   # Question/category mappings
│   ├── category_mapping.json
│   └── question_mapping.json
├── output/                     # Generated PDFs
├── scripts/                    # Python generators
│   ├── transform_and_generate.py      # Main CLI
│   ├── generate_pdf_docraptor.py      # DocRaptor renderer
│   ├── generate_pdf_playwright.py     # Playwright renderer
│   └── generate_report.py             # Template renderer
├── styles/                     # CSS stylesheets
│   ├── main.css                       # Core styles
│   ├── print.css                      # Playwright print styles
│   └── print_docraptor.css            # DocRaptor/Prince XML styles
└── templates/                  # Jinja2 templates
    ├── main_template.html
    └── partials/
        ├── cover.html
        ├── introduction.html
        ├── executive_summary.html
        ├── results_summary.html
        ├── rating_legends.html
        ├── findings.html                # Key findings section
        ├── cyber_requirements.html
        ├── category.html
        └── question.html
```

---

## Key Features

### Intelligent Page Breaks
- Categories start on new pages
- Questions stay together (no mid-question breaks)
- Finding cards never split across pages
- Headers kept with their content

### Professional Styling
- CyberPools brand colors and typography
- Color-coded risk levels (High/Moderate/Low)
- Visual grade badges and progress bars
- Consistent spacing and alignment

### Flexible Output
- Executive summary (optional, supports Markdown)
- Key findings section (auto-generated based on risk scores)
- Full control assessment with all questions
- Cyber requirements reference table

---

## Documentation

- **[Setup Guide](docs/readme_setup.md)** - Detailed installation and configuration
- **[DocRaptor Quickstart](docs/DOCRAPTOR_QUICKSTART.md)** - Get started with DocRaptor in 5 minutes
- **[DocRaptor Setup](docs/DOCRAPTOR_SETUP.md)** - Complete DocRaptor configuration
- **[DocRaptor Usage](docs/DOCRAPTOR_USAGE.md)** - Advanced DocRaptor features
- **[Template Guide](docs/template_guide.txt)** - Template variable reference

---

## Common Tasks

### Update Assessment Data
1. Export latest data from CRM as JSON
2. Place in `input/` directory
3. Run generation script with `--input` flag

### Customize Styling
- Edit `styles/main.css` for base styles
- Edit `styles/print_docraptor.css` for DocRaptor-specific print styles
- Edit `styles/print.css` for Playwright-specific print styles

### Modify Report Content
- Edit templates in `templates/partials/`
- Update boilerplate text in `content/boilerplate.json`
- Adjust mappings in `mappings/` directory

---

## CLI Reference

### Main Script: `transform_and_generate.py`

```bash
python3 scripts/transform_and_generate.py [OPTIONS]

Options:
  --input PATH          Input JSON file (default: interactive selection)
  --auto                Skip interactive prompts (use defaults)
  --engine ENGINE       PDF engine: docraptor, playwright, weasyprint
  --output PATH         Output PDF path
  --ci                  CI mode (adds Chromium flags for containers)
```

### Examples

**Interactive mode:**
```bash
python3 scripts/transform_and_generate.py
```

**Full automation:**
```bash
python3 scripts/transform_and_generate.py \
  --input input/cb-ra.json \
  --auto \
  --engine docraptor \
  --output output/Q4_Assessment.pdf
```

---

## Troubleshooting

### DocRaptor Issues
- **"API key required"**: Set `DOCRAPTOR_API_KEY` environment variable
- **"Watermarked PDF"**: Using test mode (free). Add `test_mode=False` for production
- **"unsupported properties"**: Some CSS properties not supported by Prince XML (see logs)

### Playwright Issues
- **"Browser not found"**: Run `playwright install chromium`
- **Page breaks wrong**: Adjust CSS in `styles/print.css`
- **Headers/footers missing**: Check template page-header elements

### General Issues
- **Missing data**: Verify input JSON structure and mappings
- **Styling issues**: Check browser console for CSS errors
- **Template errors**: Review Jinja2 syntax in templates

---

## License

Copyright © 2025 CyberPools. All rights reserved.

---

## Support

For issues or questions:
1. Check documentation in `docs/`
2. Review example output in `output/`
3. Consult style guide in `example/CyberPools-Style Guide.html`
