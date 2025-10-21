#!/bin/bash
# CyberPools Report Generator - Mac Auto Setup
# Creates complete folder structure with numbered organization
# Run: ./SETUP-MAC.sh

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  CyberPools Risk Assessment Report Generator              ║"
echo "║  Automatic Setup for Mac                                  ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Set the project root
PROJECT_ROOT="$HOME/Documents/cyberpools-report"

echo "📁 Creating project structure at:"
echo "   $PROJECT_ROOT"
echo ""

# Check if folder exists
if [ -d "$PROJECT_ROOT" ]; then
    echo "⚠️  WARNING: Folder already exists!"
    echo ""
    read -p "Do you want to continue? (y/n): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Setup cancelled"
        exit 1
    fi
fi

# Create main project folder
mkdir -p "$PROJECT_ROOT"
cd "$PROJECT_ROOT"

echo "✓ Creating folder structure..."
echo ""

# FOLDER 1: styles
mkdir -p styles
echo "  ✓ FOLDER 1: styles/"

# FOLDER 2: content
mkdir -p content
echo "  ✓ FOLDER 2: content/"

# FOLDER 3: mappings
mkdir -p mappings
echo "  ✓ FOLDER 3: mappings/"

# FOLDER 4: templates and partials
mkdir -p templates/partials
echo "  ✓ FOLDER 4: templates/"
echo "    ✓ FOLDER 4.1: templates/partials/"

# FOLDER 5: input
mkdir -p input
echo "  ✓ FOLDER 5: input/"

# FOLDER 6: output
mkdir -p output
echo "  ✓ FOLDER 6: output/"

# FOLDER 7: scripts
mkdir -p scripts
echo "  ✓ FOLDER 7: scripts/"

# FOLDER 8: docs
mkdir -p docs
echo "  ✓ FOLDER 8: docs/"

echo ""
echo "✅ Folder structure created successfully!"
echo ""

# Create placeholder files to show structure
echo "📝 Creating README files in each folder..."
echo ""

# FOLDER 1
cat > styles/README.txt << 'EOF'
FOLDER 1: styles/
CSS Stylesheets

Required Files:
- 1.1 - main.css (Core styles)
- 1.2 - print.css (PDF styles)
- 1.3 - components.css (Optional)

Copy the CSS files from the artifacts here.
EOF

# FOLDER 2
cat > content/README.txt << 'EOF'
FOLDER 2: content/
Boilerplate Text Content

Required Files:
- 2.1 - boilerplate.json

Copy the boilerplate.json file here.
This contains all extracted text from the CBS report.
EOF

# FOLDER 3
cat > mappings/README.txt << 'EOF'
FOLDER 3: mappings/
Data Mapping Files

Required Files:
- 3.1 - category_mapping.json (Category IDs to names)
- 3.2 - question_mapping.json (Question GUIDs to details)

⚠️ YOU MUST CREATE THESE FROM YOUR CRM!

See the setup guide for instructions.
EOF

# FOLDER 4
cat > templates/README.txt << 'EOF'
FOLDER 4: templates/
Jinja2 Templates

Required Files:
- 4.1 - main_template.html (Master template)

FOLDER 4.1: partials/ contains:
- 4.1.1 - cover.html
- 4.1.2 - introduction.html
- 4.1.3 - executive_summary.html
- 4.1.4 - results_summary.html
- 4.1.5 - rating_legends.html
- 4.1.6 - high_risk_findings.html
- 4.1.7 - cyber_requirements.html
- 4.1.8 - category.html
- 4.1.9 - question.html

Copy all template files from artifacts here.
EOF

cat > templates/partials/README.txt << 'EOF'
FOLDER 4.1: templates/partials/
Template Components

9 partial template files go here.
See FOLDER 4 README for complete list.
EOF

# FOLDER 5
cat > input/README.txt << 'EOF'
FOLDER 5: input/
Your CRM Data Files

Place your CRM export JSON files here.

Format: Array of question objects from Column P in Excel

Example files:
- 5.1 - cbs_raw_data.json (sample)
- 5.2 - your_data.json (your actual data)

The script will show available files when you run it.
EOF

# FOLDER 6
cat > output/README.txt << 'EOF'
FOLDER 6: output/
Generated PDF Reports

PDFs will be automatically created here when you run the script.

Naming format:
[Member]_Risk_Assessment_[Date].pdf

Example:
Christian_Brothers_Services_Risk_Assessment_10-16-2025.pdf

This folder starts empty - PDFs appear after generation.
EOF

# FOLDER 7
cat > scripts/README.txt << 'EOF'
FOLDER 7: scripts/
Python Scripts

Required Files:
- 7.1 - generate_report.py (PDF generator)
- 7.2 - transform_and_generate.py (Interactive script)
- 7.3 - run.sh (Mac launcher)

⭐ MAIN SCRIPT: 7.2 - transform_and_generate.py

Run: python3 scripts/transform_and_generate.py
Or:  ./scripts/run.sh

Copy all Python scripts from artifacts here.
Make run.sh executable: chmod +x scripts/run.sh
EOF

# FOLDER 8
cat > docs/README.txt << 'EOF'
FOLDER 8: docs/
Documentation

Required Files:
- 8.1 - README.md (Project overview)
- 8.2 - SETUP_GUIDE.md (Installation)
- 8.3 - DATA_SCHEMA.md (Data structure)
- 8.4 - TEMPLATE_GUIDE.md (Template variables)
- 8.5 - TESTING.md (Test checklist)
- 8.6 - requirements.txt (Python packages)

⚠️ IMPORTANT: Create requirements.txt with:
Jinja2==3.1.2
WeasyPrint==59.0
MarkupSafe==2.1.3

Then run: pip3 install -r docs/requirements.txt
EOF

echo "✓ README files created in each folder"
echo ""

# Create a master checklist
cat > SETUP-CHECKLIST.txt << 'EOF'
═══════════════════════════════════════════════════════════
  CYBERPOOLS REPORT GENERATOR - SETUP CHECKLIST
═══════════════════════════════════════════════════════════

📋 STEP-BY-STEP SETUP:

□ 1. Copy files to FOLDER 1 (styles/)
   □ 1.1 - main.css
   □ 1.2 - print.css
   □ 1.3 - components.css (optional)

□ 2. Copy files to FOLDER 2 (content/)
   □ 2.1 - boilerplate.json

□ 3. CREATE files in FOLDER 3 (mappings/)
   □ 3.1 - category_mapping.json (from CRM)
   □ 3.2 - question_mapping.json (from CRM)
   ⚠️ Must export from your CRM!

□ 4. Copy files to FOLDER 4 (templates/)
   □ 4.1 - main_template.html
   □ Copy 9 partials to templates/partials/

□ 5. Add data to FOLDER 5 (input/)
   □ Copy CRM JSON export(s)

□ 6. Copy files to FOLDER 7 (scripts/)
   □ 7.1 - generate_report.py
   □ 7.2 - transform_and_generate.py
   □ 7.3 - run.sh
   □ Make run.sh executable: chmod +x scripts/run.sh

□ 7. Setup FOLDER 8 (docs/)
   □ 8.6 - requirements.txt (create this!)
   □ Copy documentation files

□ 8. Install Python dependencies:
   $ cd ~/Documents/cyberpools-report
   $ pip3 install -r docs/requirements.txt

□ 9. Test the setup:
   $ python3 scripts/transform_and_generate.py

═══════════════════════════════════════════════════════════

📝 NOTES:
- Each folder has a README.txt explaining what goes there
- Numbered files (1.1, 7.2, etc.) help you organize
- See "0.0 - MASTER FILE ORGANIZATION GUIDE" for details

✅ When all boxes are checked, you're ready to generate reports!

═══════════════════════════════════════════════════════════
EOF

echo "📋 Setup checklist created: SETUP-CHECKLIST.txt"
echo ""

# Show folder tree
echo "📁 Your folder structure:"
echo ""
find . -maxdepth 2 -type d | sed 's|^\./||' | sort | sed 's|^|  |'
echo ""

# Final instructions
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  ✅ SETUP COMPLETE!                                        ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "📍 Location: $PROJECT_ROOT"
echo ""
echo "📋 NEXT STEPS:"
echo ""
echo "  1. Open SETUP-CHECKLIST.txt in this folder"
echo "  2. Follow the checklist to copy all files"
echo "  3. Install Python dependencies"
echo "  4. Run the generator!"
echo ""
echo "  Quick start:"
echo "    cd $PROJECT_ROOT"
echo "    cat SETUP-CHECKLIST.txt"
echo ""
echo "  Each folder has a README.txt explaining what to put there."
echo ""
echo "Need help? See '0.0 - MASTER FILE ORGANIZATION GUIDE'"
echo ""

# Open the folder in Finder (Mac)
if command -v open &> /dev/null; then
    read -p "Open project folder in Finder? (y/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        open "$PROJECT_ROOT"
    fi
fi

echo "Done! 🎉"
echo ""
