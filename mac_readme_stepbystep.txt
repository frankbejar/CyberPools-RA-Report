# CyberPools Risk Assessment Report Generator  
## MacBook Setup & Usage (Zero-to-PDF)

**Last updated:** October 2025  
**Estimated time:** 20–30 minutes  

This playbook walks a new teammate through installing the tooling, preparing the inputs, and producing a CyberPools-branded PDF using Playwright.

---

## 1. Prerequisites Checklist

1. **Python 3.9 or newer**
   ```bash
   python3 --version
   ```
   If missing, install the official macOS package from [python.org](https://www.python.org/downloads/).

2. **Homebrew (optional but helpful)** – for system upgrades:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Text editor or IDE** – VS Code, PyCharm, or even TextEdit in plain-text mode.

4. **Admin rights / ability to install Chromium** – required by Playwright. Coordinate with IT if downloads are restricted.

---

## 2. Clone or Copy the Repository

```bash
cd ~/Documents
git clone <repo-url> cyberpools-report   # or copy the folder provided by the team
cd cyberpools-report
```

> If you receive the project via zipped archive, unzip it into `~/Documents/cyberpools-report` and run the remaining steps from that directory.

Directory sanity check:
```bash
ls
# Example  content  docs  input  logo  mappings  output  scripts  styles  templates
```

---

## 3. Install Python Dependencies

From the project root:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r docs/requirements.txt
```

Then install Chromium for Playwright (one-time):

```bash
python3 -m playwright install chromium
```

Verify Playwright can launch:

```bash
python3 - <<'PY'
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    print("✅ Chromium available:", p.chromium.name)
PY
```

---

## 4. Prepare Input Data

1. Copy the raw CRM export JSON file into `input/`. The script expects an array of question objects with keys like `qID`, `qCat`, `qResponse`, `qScore`, etc.
2. Confirm the GUIDs in the CRM file exist in `mappings/question_mapping.json`. Add new entries for any new questions.
3. Update `content/boilerplate.json` if CyberPools messaging changes (introduction, category overviews, etc.).
4. Ensure your mapping JSON is valid (use VS Code or `jq . file.json` to confirm).

---

## 5. Generate a PDF (Playwright Engine)

Run the primary script from the project root:

```bash
python3 scripts/transform_and_generate.py --input input/cb-ra.json --auto
```

What happens:
1. Loads the CRM questions.
2. Builds the report context (metadata, scoring, category groupings).
3. Renders the Jinja2 templates.
4. Launches headless Chromium via Playwright and prints the HTML to `output/<Org>_Risk_Assessment_<Date>.pdf`.

> **Note on rounding**: Overall and category percentages now use standard half-up rounding (e.g., 80.5 → 81) to match the CRM dashboards exactly.
> **Compliance table**: The Cyber Requirements section is included by default. Add `--no-compliance` if you need to omit it for a particular run.

During the prompts you’ll be asked whether to format the executive summary with Markdown. Choose **Y** if you want bold text, lists, headings, etc.—the script will convert the Markdown to HTML automatically.

**Common flags**
| Flag | Description |
| --- | --- |
| `--auto` | Skip interactive prompts (uses sensible defaults). |
| `--engine weasyprint` | Use WeasyPrint instead of Playwright. |
| `--ci` | Adds Chromium `--no-sandbox` flags for CI/docker. |

Inspect the PDF under `output/`.

---

## 6. Optional Utilities

| Command | Purpose |
| --- | --- |
| `python3 scripts/export_example_pdf.py` | Print the legacy static HTML example using the Playwright renderer. |
| `python3 scripts/split_example_html.py` | Split the HTML in `Example /` into per-page files for comparison. |
| `./scripts/run.sh` | Mac helper that checks Python, installs dependencies if missing, then proxies to `transform_and_generate.py`. Make executable with `chmod +x scripts/run.sh`. |

---

## 7. Customizing the Report

* **Templates (`templates/partials/…`)** – edit HTML structure, add/remove sections, tweak the summary progress bar, etc.
* **Brand variables (`styles/main.css`)** – adjust colors, typography, spacing. The summary now uses a progress bar instead of a letter grade and omits footers for a cleaner layout.
* **Print behaviour (`styles/print.css`)** – tune page breaks or how question blocks flow across pages.
* **Boilerplate copy (`content/boilerplate.json`)** – update introductions, category importance messaging, and methodology descriptions.

After making changes, simply rerun the generator—no build step is required.

---

## 8. Troubleshooting on macOS

| Issue | Fix |
| --- | --- |
| `ModuleNotFoundError: playwright` | Rerun `pip install -r docs/requirements.txt`. |
| `Error: Failed to launch browser` | Rerun `python3 -m playwright install chromium`. Check network restrictions. |
| Output PDF missing content | Confirm the CRM file GUIDs exist in `mappings/question_mapping.json`. |
| CSS not applying in PDF | Playwright inlines both `styles/main.css` and `styles/print.css`. Re-run the script after editing the stylesheets. |
| Need to roll back | Use git to revert your changes (`git checkout -- file`). |

---

## 9. What to Share with Teammates

1. The `output/*.pdf` report.
2. Any updated mappings (`mappings/question_mapping.json`) after new questions roll in.
3. Updated docs if you change process steps—keep everything in `docs/` synchronized so newcomers have a single source of truth.

---

### Need Help?
Reach out to the CyberPools tooling team – **cyber@cyberpools.org** – or check the top-level README (`docs/readme_setup.md`) for architecture and dependency context.

⚠️ **YOU MUST CREATE THIS FROM YOUR CRM**

For now, create a starter file:

1. Create new file in TextEdit
2. Paste this template:

```json
{
  "REPLACE-WITH-ACTUAL-GUID": {
    "number": "1.1",
    "text": "REPLACE WITH ACTUAL QUESTION TEXT",
    "control_description": "REPLACE WITH CONTROL DESCRIPTION",
    "impact_score": 3,
    "category": "772120000"
  }
}
```

3. Save as: `Documents/cyberpools-report/mappings/question_mapping.json`

📝 **TODO:** Export all questions from CRM and complete this file

✅ **Checkpoint:** 2 JSON files in `mappings/` folder

---

#### **3.4 - Download Templates (FOLDER: templates/)**

**Main Template:**
1. In artifacts, find **"4.1 - main_template.html"**
2. Copy content
3. Save as: `Documents/cyberpools-report/templates/main_template.html`

**Partial Templates (9 files):**

For each of these, repeat: Click artifact → Copy → Save

| Artifact Name | Save As |
|---------------|---------|
| 4.1.1 - cover.html | `templates/partials/cover.html` |
| 4.1.2 - introduction.html | `templates/partials/introduction.html` |
| 4.1.3 - executive_summary.html | `templates/partials/executive_summary.html` |
| 4.1.4 - results_summary.html | `templates/partials/results_summary.html` |
| 4.1.5 - rating_legends.html | `templates/partials/rating_legends.html` |
| 4.1.6 - high_risk_findings.html | `templates/partials/high_risk_findings.html` |
| 4.1.7 - cyber_requirements.html | `templates/partials/cyber_requirements.html` |
| 4.1.8 - category.html | `templates/partials/category.html` |
| 4.1.9 - question.html | `templates/partials/question.html` |

✅ **Checkpoint:** 10 HTML files (1 main + 9 partials)

---

#### **3.5 - Download Python Scripts (FOLDER: scripts/)**

**File 1: generate_report.py**
1. Find **"7.1 - Report Generation Script"** or **"generate_report.py"**
2. Copy content
3. Save as: `Documents/cyberpools-report/scripts/generate_report.py`

**File 2: transform_and_generate.py** (Main script!)
1. Find **"7.2 - Interactive Script"** or **"transform_and_generate.py"**
2. Copy content
3. Save as: `Documents/cyberpools-report/scripts/transform_and_generate.py`

**File 3: run.sh**
1. Find **"7.3 - Mac Quick Start"** or **"run.sh"**
2. Copy content
3. Save as: `Documents/cyberpools-report/scripts/run.sh`

**Make run.sh executable:**
```bash
cd ~/Documents/cyberpools-report
chmod +x scripts/run.sh
```

✅ **Checkpoint:** 3 Python/script files in `scripts/` folder

---

#### **3.6 - Download Documentation (FOLDER: docs/)**

**Create requirements.txt first (MOST IMPORTANT!):**

1. Open TextEdit
2. Paste this EXACT content:

```
Jinja2==3.1.2
WeasyPrint==59.0
MarkupSafe==2.1.3
cffi==1.15.1
pycparser==2.21
Pillow==10.0.0
cssselect2==0.7.0
tinycss2==1.2.1
fonttools==4.42.0
pydyf==0.7.0
pyphen==0.14.0
```

3. Save as: `Documents/cyberpools-report/docs/requirements.txt`

**Other Documentation (Optional but helpful):**

Download these from artifacts if you want:
- README.md → `docs/README.md`
- SETUP_GUIDE.md → `docs/SETUP_GUIDE.md`
- DATA_SCHEMA.md → `docs/DATA_SCHEMA.md`
- TEMPLATE_GUIDE.md → `docs/TEMPLATE_GUIDE.md`
- TESTING.md → `docs/TESTING.md`

✅ **Checkpoint:** `requirements.txt` exists in `docs/` folder

---

### **STEP 4: Add Your CRM Data (FOLDER: input/)**

**Get your CRM export:**

1. Open your Risk Assessment Excel file
2. Find the **JSON column** (Column P)
3. Copy the ENTIRE JSON array from the cell
4. Open TextEdit
5. Paste
6. Save as: `Documents/cyberpools-report/input/cbs_raw_data.json`

**Format should look like:**
```json
[
  {
    "qCat": 772120001,
    "qID": "guid-here",
    "qResponse": 1,
    "qScore": 5,
    "qNotes": "Comments here...",
    "qReq": true
  },
  ...more questions
]
```

✅ **Checkpoint:** At least 1 JSON file in `input/` folder

---

### **STEP 5: Install Python Dependencies**

**In Terminal:**

```bash
# Make sure you're in the project folder
cd ~/Documents/cyberpools-report

# Install all required packages
pip3 install -r docs/requirements.txt
```

**This will install:**
- Jinja2 (template engine)
- WeasyPrint (PDF generator)
- All dependencies

**Expected output:**
```
Successfully installed Jinja2-3.1.2 WeasyPrint-59.0 ...
```

⚠️ **If you get errors:**
```bash
# Try with --user flag
pip3 install --user -r docs/requirements.txt

# Or use python3 -m pip
python3 -m pip install -r docs/requirements.txt
```

✅ **Checkpoint:** All packages installed successfully

---

### **STEP 6: Verify Your Setup**

**Check folder structure:**

```bash
cd ~/Documents/cyberpools-report
find . -type f | grep -v .DS_Store | sort
```

**You should see approximately:**
```
./content/boilerplate.json
./docs/requirements.txt
./input/cbs_raw_data.json
./mappings/category_mapping.json
./mappings/question_mapping.json
./scripts/generate_report.py
./scripts/run.sh
./scripts/transform_and_generate.py
./styles/components.css
./styles/main.css
./styles/print.css
./templates/main_template.html
./templates/partials/category.html
./templates/partials/cover.html
./templates/partials/cyber_requirements.html
./templates/partials/executive_summary.html
./templates/partials/high_risk_findings.html
./templates/partials/introduction.html
./templates/partials/question.html
./templates/partials/rating_legends.html
./templates/partials/results_summary.html
```

**Count files:**
```bash
find . -type f | grep -v .DS_Store | wc -l
```

**Expected:** Around 20-25 files

✅ **Checkpoint:** All files in place

---

## 🎯 STEP 7: RUN YOUR FIRST REPORT!

### **Method 1: Interactive Script (Recommended)**

```bash
cd ~/Documents/cyberpools-report
python3 scripts/transform_and_generate.py
```

**What happens:**
1. Script shows available input files
2. You select one
3. You enter member name
4. You enter assessment date
5. You enter conducted by
6. You enter member contact
7. **You enter executive summary** (type your summary, press Enter twice)
8. Script transforms data
9. Script generates PDF
10. PDF appears in `output/` folder!

### **Method 2: Using run.sh**

```bash
cd ~/Documents/cyberpools-report
./scripts/run.sh
```

**This does the same but checks dependencies first**

### **Method 3: Quick/Auto Mode**

```bash
python3 scripts/transform_and_generate.py --auto
```

**Skips prompts, uses defaults - good for testing**

---

## 📊 EXPECTED OUTPUT

### **During Execution:**

```
===============================================================
  CyberPools Risk Assessment Report Generator
===============================================================

📂 Available input files:
  1. input/cbs_raw_data.json

Select input file (1-1): 1

✓ Loaded 51 questions from CRM data

📋 Assessment Information

Member Name: Christian Brothers Services
Assessment Date [01/18/2025]: 10/16/2025
Conducted By: Alex Robles
Member Contact: Ashu Ketkar

📝 Executive Summary
Enter text (press Enter twice when done):

> CBS demonstrates exceptional cybersecurity maturity...
> 

✓ Data transformation complete
✓ Generating PDF...
✓ Report saved to: output/Christian_Brothers_Services_Risk_Assessment_10-16-2025.pdf

✨ Done! Open the PDF to review.
```

### **Check Your Output:**

```bash
ls -lh output/
```

**You should see:** `[Member]_Risk_Assessment_[Date].pdf`

**Open the PDF:**
```bash
open output/*.pdf
```

✅ **SUCCESS!** Your first report is generated!

---

## ✅ VERIFICATION CHECKLIST

After completing all steps:

- [ ] Project folder created in Documents
- [ ] All 8 subfolders exist
- [ ] 3 CSS files in `styles/`
- [ ] 1 JSON file in `content/`
- [ ] 2 JSON files in `mappings/`
- [ ] 10 HTML files in `templates/` (1 + 9 partials)
- [ ] At least 1 JSON file in `input/`
- [ ] 3 files in `scripts/`
- [ ] `requirements.txt` in `docs/`
- [ ] Python dependencies installed
- [ ] Can run script without errors
- [ ] PDF generates in `output/`
- [ ] PDF opens and looks correct

---

## 🐛 TROUBLESHOOTING

### **"Command not found: python3"**
```bash
# Install Python 3 from python.org
# Or try:
python --version
# If that works, use 'python' instead of 'python3'
```

### **"No module named 'jinja2'"**
```bash
# Install dependencies
cd ~/Documents/cyberpools-report
pip3 install -r docs/requirements.txt
```

### **"File not found: templates/..."**
```bash
# Check you're in the right folder
pwd
# Should show: /Users/YourName/Documents/cyberpools-report

# Check files exist
ls -la templates/partials/
```

### **"Permission denied" when running run.sh**
```bash
# Make executable
chmod +x scripts/run.sh
```

### **PDF has wrong colors**
✅ Make sure you downloaded the UPDATED CSS files (1.1 and 1.2)

### **"Unknown Question" appears in PDF**
⚠️ You need to complete `question_mapping.json` with your CRM question data

### **Script crashes**
```bash
# Check Python version
python3 --version  # Should be 3.8+

# Reinstall dependencies
pip3 install --upgrade -r docs/requirements.txt

# Run with error details
python3 scripts/transform_and_generate.py
```

---

## 📁 QUICK REFERENCE

### **Project Location:**
```bash
cd ~/Documents/cyberpools-report
```

### **Run Report Generator:**
```bash
python3 scripts/transform_and_generate.py
```

### **View Generated PDFs:**
```bash
open output/
```

### **Add New Data:**
```bash
# Place JSON files in:
cp /path/to/new_data.json input/
```

### **Update CSS:**
```bash
# Edit:
open -a TextEdit styles/main.css
```

---

## 📞 NEED HELP?

### **Common Issues:**
1. **Can't find artifacts** → Look to right side of Claude chat
2. **Python errors** → Make sure Python 3.8+ installed
3. **Module not found** → Run `pip3 install -r docs/requirements.txt`
4. **PDF looks wrong** → Check CSS files are updated versions (1.1, 1.2)
5. **Missing questions** → Complete `question_mapping.json` from CRM

### **Resources:**
- **This Guide:** Keep it open for reference
- **Master Guide:** See `0.0 - MASTER FILE ORGANIZATION GUIDE` artifact
- **Data Schema:** See `8.3 - DATA_SCHEMA.md` for JSON format
- **Testing:** See `8.5 - TESTING.md` for full test checklist

### **Contact:**
- Email: cyber@cyberpools.org
- Reference: CyberPools Style Guide v1.0

---

## 🎉 YOU'RE DONE!

**What you can do now:**
1. ✅ Generate professional PDF reports
2. ✅ Customize executive summaries
3. ✅ Process CRM data automatically
4. ✅ Create brand-compliant reports

**Next Steps:**
1. Complete `question_mapping.json` from your CRM
2. Test with multiple assessments
3. Review generated PDFs
4. Customize as needed

---

**Congratulations!** You now have a fully functional Risk Assessment Report Generator on your MacBook Pro! 🎊

**Last Updated:** October 2025  
**Version:** 1.0 - Style Guide Compliant
