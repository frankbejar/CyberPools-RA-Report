# CyberPools Risk Assessment

This repository contains multiple components for the CyberPools Risk Assessment system.

## Repository Structure

### 📋 2026 RA/ - Current Assessment Initiative
**Status:** Production-ready (v6.2 FINAL)

2026 Risk Assessment documentation including:
- 57-question framework (10 TIER 1A / 7 TIER 1B / 40 Comprehensive)
- TIER Framework justifications with evidence-based research
- Grade Ceiling methodology documentation
- GitHub Pages rebuild plan

**Key documents:**
- `2026_RA_QUESTION_SET_v6.2_FINAL.md` - Master question set
- `2026_RA_TIER_FRAMEWORK_JUSTIFICATION.md` - TIER 1A/1B evidence
- `GRADING_METHODOLOGY_EXECUTIVE_R2.md` - Grade Ceiling approach
- `GRADING_METHODOLOGY_TECHNICAL_SUPPLEMENT.md` - Technical details

[See 2026 RA/README.md for full documentation](2026%20RA/README.md)

---

### 📄 2025-ra-report/ - PDF Report Generator
**Status:** Active production system

Python-based PDF report generation system that transforms CRM assessment data into branded reports using DocRaptor (Prince XML) or Playwright (Chromium) rendering.

**Quick start:**
```bash
cd 2025-ra-report
pip install -r documentation/requirements.txt
python3 scripts/transform_and_generate.py
```

**Key features:**
- Professional PDF output with running headers/footers
- Intelligent page breaks and styling
- Cyber requirements compliance table
- AI-powered executive summary generation

[See 2025-ra-report/README-PDF-GENERATOR.md for full documentation](2025-ra-report/README-PDF-GENERATOR.md)

---

### 🌐 docs-site/ - GitHub Pages Documentation
**Status:** Pending rebuild (currently outdated)

Public documentation site hosted at: https://frankbejar.github.io/CyberPools-RA-Report/

**Current status:** Site shows outdated content. Rebuild planned to align with 2026 RA v6.2 FINAL.

**Plans:**
- Automated content generation from master documents
- Material for MkDocs theme with CyberPools branding
- Complete question set with TIER classifications
- Framework mappings and grading methodology

[See 2026 RA/GITHUB_PAGES_REENGINEERING_PLAN.md for rebuild details](2026%20RA/GITHUB_PAGES_REENGINEERING_PLAN.md)

---

### 📦 archive/ - Historical Content
**Status:** Reference only

Contains:
- `poc-research/` - POC work, alternative methodologies, historical research
- Includes insurance alignment reviews and grading model explorations

**Note:** Not for active development. Retained for historical reference and research context.

---

## Current Focus: 2026 Risk Assessment

**Primary working directory:** `2026 RA/`

The 2026 Risk Assessment v6.2 FINAL represents a complete redesign featuring:
- Evidence-based TIER framework (insurance carrier requirements + threat intelligence)
- Grade Ceiling methodology to ensure critical gaps are visible
- Sector-neutral approach applicable across K-12, healthcare, and nonprofit sectors
- 86% CIS Controls v8.1 IG1 coverage (48 of 56 safeguards)

---

## Development Guidelines

See [CLAUDE.md](CLAUDE.md) for:
- Project context and architecture
- Development standards and workflows
- Documentation requirements
- NO EMOJIS POLICY (strict prohibition)
- Production vs. POC separation guidelines

---

## Quick Navigation

**Working on 2026 Assessment?**
→ Start in `2026 RA/` - all production documents are here

**Generating PDF reports?**
→ Use `2025-ra-report/` - complete production system

**Building documentation site?**
→ See `2026 RA/GITHUB_PAGES_REENGINEERING_PLAN.md` first, then work in `docs-site/`

**Looking for research/POC work?**
→ Check `archive/poc-research/` - historical reference only

---

## Contact

For questions about CyberPools Risk Assessment:
- Email: cyber@cyberpools.org
- Repository: https://github.com/frankbejar/CyberPools-RA-Report

---

**Last Updated:** November 20, 2025
**Current Version:** 2026 RA v6.2 FINAL
