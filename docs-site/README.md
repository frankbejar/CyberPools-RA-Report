# CyberPools Risk Assessment - Documentation Site

**Status:** Pending rebuild - Currently outdated

**Live Site:** https://frankbejar.github.io/CyberPools-RA-Report/

## Current Status

The GitHub Pages documentation site is currently showing outdated content based on v5.0 (65 questions, 9 categories, sector-specific pages).

**Rebuild Required:** Site needs complete redesign to align with 2026 RA v6.2 FINAL (57 questions, 10 categories, TIER framework).

## Rebuild Plan

See **[../2026 RA/GITHUB_PAGES_REENGINEERING_PLAN.md](../2026%20RA/GITHUB_PAGES_REENGINEERING_PLAN.md)** for complete rebuild documentation including:

- Target site structure
- Content generation strategy (automated from master documents)
- Navigation design
- Implementation phases (10-day timeline)
- Material for MkDocs theme configuration

## Structure

```
docs-site/
├── .github/workflows/     # GitHub Actions for auto-deployment
├── docs/                  # MkDocs content (to be regenerated)
├── scripts/               # Build scripts (to be created)
├── mkdocs.yml            # MkDocs configuration (needs update)
├── requirements-docs.txt  # Python dependencies
└── README.md             # This file
```

## Next Steps

**Before starting rebuild:**
1. Review GITHUB_PAGES_REENGINEERING_PLAN.md
2. Create `scripts/build_mkdocs_site.py` to auto-generate content from master documents
3. Update `mkdocs.yml` for new structure
4. Test locally: `mkdocs serve`
5. Deploy: Push to main branch (GitHub Actions auto-deploys)

## Local Development

**Prerequisites:**
```bash
pip install -r requirements-docs.txt
```

**Preview site locally:**
```bash
cd docs-site
mkdocs serve
# Opens at http://127.0.0.1:8000
```

**Build static site:**
```bash
mkdocs build
```

**Deploy to GitHub Pages:**
```bash
mkdocs gh-deploy
```

## Source of Truth

All content should be auto-generated from master documents in:
- `../2026 RA/2026_RA_QUESTION_SET_v6.2_FINAL.md`
- `../2026 RA/2026_RA_TIER_FRAMEWORK_JUSTIFICATION.md`
- `../2026 RA/GRADING_METHODOLOGY_EXECUTIVE_R2.md`
- `../2026 RA/GRADING_METHODOLOGY_TECHNICAL_SUPPLEMENT.md`

**DO NOT manually edit content** - always regenerate from source documents using build script.

---

**Last Updated:** November 20, 2025
**Target:** Align with 2026 RA v6.2 FINAL
