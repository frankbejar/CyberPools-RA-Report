# CyberPools Risk Assessment Documentation Site

This directory contains the MkDocs Material documentation site for the Comprehensive Risk Assessment Questionnaire.

## 🚀 Quick Start

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements-docs.txt
   ```

2. **Preview the site locally:**
   ```bash
   mkdocs serve
   ```

   Open http://127.0.0.1:8000 in your browser

3. **Build static site:**
   ```bash
   mkdocs build
   ```

   Output will be in `site/` directory

### Rebuild from Source

If you've updated the comprehensive questionnaire markdown file, rebuild the docs:

```bash
python3 scripts/build_docs_site.py
```

This will regenerate all documentation pages from the source questionnaire.

## 📁 Directory Structure

```
docs/
├── index.md                    # Home page
├── overview/                   # Overview pages
│   ├── introduction.md         # Introduction and methodology
│   ├── methodology.md          # Assessment methodology
│   └── essential-controls.md   # 17 foundational questions
├── categories/                 # Category pages
│   ├── category-1.md          # Category 1: Asset Inventory
│   ├── category-2.md          # Category 2: Account Management
│   └── ...                    # Categories 3-9
├── filtered/                   # Filtered views
│   ├── foundational.md        # 17 foundational questions
│   ├── new-questions.md       # 13 new questions for 2026
│   └── high-impact.md         # High impact (5) questions
├── sectors/                    # Sector-specific guidance
│   ├── education.md           # K-12/Higher Ed guidance
│   ├── healthcare.md          # Healthcare guidance
│   ├── nonprofit.md           # Religious/Nonprofit guidance
│   └── general.md             # General organizations
├── reference/                  # Reference materials
│   ├── citations.md           # Comprehensive citations
│   └── frameworks.md          # Framework mapping
├── stylesheets/                # Custom CSS
│   └── extra.css              # Custom styling
└── tags.md                    # Tags index
```

## 🎨 Features

- **Search**: Full-text search across all questions
- **Tags**: Filter by category, impact rating, foundational, new, sector
- **Navigation**: Hierarchical navigation with expandable sections
- **Mobile Responsive**: Works on all devices
- **Dark Mode**: Toggle between light and dark themes
- **Print-Friendly**: Export to PDF via browser print

## 🔄 Auto-Deployment

The site automatically deploys to GitHub Pages when:
- Changes are pushed to `main` branch
- Files in `docs/`, `mkdocs.yml`, or source questionnaire are modified
- GitHub Actions workflow completes successfully

View deployed site at: `https://frankbejar.github.io/CyberPools-RA-Report/`

## 🛠️ Customization

### Update Configuration

Edit `mkdocs.yml` in the repository root to:
- Change site theme colors
- Modify navigation structure
- Add/remove features
- Update site metadata

### Update Source Content

To update question content:
1. Edit `poc-research/docs/COMPREHENSIVE_RISK_ASSESSMENT_QUESTIONNAIRE.md`
2. Run `python3 scripts/build_docs_site.py` to rebuild docs
3. Commit and push changes
4. GitHub Actions will auto-deploy

### Markdown Formatting Requirements

**MkDocs Material has specific formatting requirements for proper list rendering:**

#### Nested Lists Under Numbered Items

For numbered lists with sub-bullets, use **4 spaces** (not 3) for indentation and add a **blank line** after the header:

✅ **Correct:**
```markdown
1. **Header:**

    - Bullet item (4 spaces)
    - Bullet item (4 spaces)
```

❌ **Incorrect:**
```markdown
1. **Header:**
   - Bullet item (3 spaces - will render as separate numbered items)
```

#### Bold Headers with Bullets

Add a **blank line** after bold headers before bullet lists:

✅ **Correct:**
```markdown
**Header:**

- Bullet item
- Bullet item
```

❌ **Incorrect:**
```markdown
**Header:**
- Bullet item (will render as plain text)
```

#### Fixing Formatting Issues

If lists aren't rendering properly:

1. Check indentation with `od -c filename.md` to verify exact spacing
2. Ensure 4 spaces for nested bullets under numbered lists
3. Add blank lines after headers before bullets
4. Run `python3 scripts/build_docs_site.py` to rebuild
5. Preview with `mkdocs serve` before committing

### Custom Styling

Edit `docs/stylesheets/extra.css` for custom CSS.

## 📦 Deployment

### Manual Deploy

```bash
mkdocs gh-deploy
```

### Automated Deploy

Push to `main` branch - GitHub Actions handles deployment automatically.

## 🔍 Search Optimization

The site uses MkDocs Material's built-in search with:
- Fuzzy matching
- Search suggestions
- Search highlighting
- Search result sharing

## 📄 License

This documentation is part of the CyberPools Risk Assessment project.

## 🆘 Support

For issues or questions:
1. Check MkDocs Material docs: https://squidfunk.github.io/mkdocs-material/
2. Review GitHub repository issues
3. Contact CyberPools team

---

**Last Updated:** October 30, 2025
**Documentation Version:** 2.0
**MkDocs Material Version:** 9.5.0+
