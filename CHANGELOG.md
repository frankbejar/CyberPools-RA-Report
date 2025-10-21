# Changelog

## 2025-10-21 - Key Findings Section Improvements & DocRaptor Integration

### Key Findings Section
- Fixed narrow width rendering in DocRaptor PDF output
- Resolved page spanning issues - cards now break intelligently
- Updated findings cards to match Control Assessment section format
  - Added Control Status with numeric value and color coding
  - Added Impact rating with proper HIGH/MODERATE/LOW display
  - Added Risk Score (already working)
  - All three fields now display on one line
- Added proper spacing between risk level descriptions and finding cards
- Fixed data mapping to include control_status and impact_score numeric values

### DocRaptor Integration
- Integrated DocRaptor (Prince XML) as recommended PDF rendering engine
- Created comprehensive DocRaptor documentation in docs/ folder
  - docs/DOCRAPTOR_QUICKSTART.md - 5-minute getting started guide
  - docs/DOCRAPTOR_SETUP.md - Complete setup instructions
  - docs/DOCRAPTOR_USAGE.md - Advanced usage and features
- Added print_docraptor.css with Prince XML-specific optimizations
  - Full-width layout enforcement for all findings elements
  - Smart page break rules (cards stay together, sections can flow)
  - Removed unsupported CSS properties (gap)
  - Added proper running headers/footers via @page rules

### Code Quality Improvements
- Removed all emojis from Python scripts for professional appearance
- Replaced emoji indicators with [SUCCESS], [ERROR], [INFO] prefixes
- Updated all console output for cleaner, more professional logging

### Documentation
- Created comprehensive README.md at project root
- Moved all DocRaptor documentation to docs/ folder
- Added CLI reference and troubleshooting sections
- Documented both DocRaptor and Playwright rendering options

### CSS Fixes
- Added explicit width: 100% and max-width: 100% to all findings elements
- Fixed display modes for Prince XML compatibility
- Added proper margin-based spacing (replacing flex gap)
- Enforced full-width rendering in print stylesheets

### Bug Fixes
- Fixed missing control_status and impact_score in findings data structure
- Fixed badge color coding based on numeric values (1/3/5)
- Fixed status label formatting to match question blocks
- Resolved Prince XML "unsupported properties: gap" warnings

### Files Modified
- scripts/transform_and_generate.py - Added control_status and impact_score to findings, removed emojis
- scripts/generate_pdf_docraptor.py - Removed emojis
- scripts/quick_docraptor_test.py - Removed emojis
- scripts/test_docraptor.py - Removed emojis
- templates/partials/findings.html - Updated to match question block format
- styles/main.css - Added width constraints and spacing for findings
- styles/print_docraptor.css - Added Prince XML-specific optimizations
- README.md - Created comprehensive project documentation

### New Files
- README.md - Main project documentation
- docs/DOCRAPTOR_QUICKSTART.md - Quick start guide
- docs/DOCRAPTOR_SETUP.md - Setup instructions
- docs/DOCRAPTOR_USAGE.md - Usage documentation
- styles/print_docraptor.css - DocRaptor-specific print styles
- scripts/generate_pdf_docraptor.py - DocRaptor renderer
- CHANGELOG.md - This file
