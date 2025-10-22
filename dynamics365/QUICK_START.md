# CyberPools Report Generator - Quick Start Guide

## 🎯 What You Have

A complete JavaScript solution that generates PDF reports directly from Dynamics 365 using DocRaptor!

## ✅ Prerequisites Checklist

- [ ] Dynamics 365 instance with System Administrator access
- [ ] DocRaptor API key (you have: `Uej3BuDjlcc3vx8z5lfK`)
- [ ] Risk Assessment entity with JSON field
- [ ] Mapping files: `question_mapping.json` and `category_mapping.json`

## 🚀 Quick Deploy (5 Steps - 15 Minutes)

### Step 1: Test Locally First (Optional but Recommended)

1. Open `test-local.html` in your browser
2. Click "Generate Test Report"
3. Verify PDF downloads successfully

**If test works** → proceed to Step 2
**If test fails** → check browser console for errors

---

### Step 2: Upload JavaScript to Dynamics 365

1. Go to **Settings** → **Customizations** → **Customize the System**
2. Click **Web Resources** → **New**
3. Fill in:
   - **Name:** `new_/scripts/cyberpools_report_generator`
   - **Display Name:** CyberPools Report Generator
   - **Type:** Script (JScript)
   - **Upload File:** Select `cyberpools-report-complete.js`
4. Click **Save** then **Publish**

---

### Step 3: Upload Mapping Files

**Option A: Upload as Web Resources (Recommended)**

Repeat for each file:

1. **Web Resources** → **New**
2. For `question_mapping.json`:
   - **Name:** `new_/mappings/question_mapping`
   - **Display Name:** Question Mapping
   - **Type:** Data (JSON)
   - **Upload:** `mappings/question_mapping.json`
3. For `category_mapping.json`:
   - **Name:** `new_/mappings/category_mapping`
   - **Display Name:** Category Mapping
   - **Type:** Data (JSON)
   - **Upload:** `mappings/category_mapping.json`
4. **Save** and **Publish** each

**Option B: Embed in JavaScript (Simpler, Larger File)**

1. Open `cyberpools-report-complete.js`
2. Find line ~25: `USE_EMBEDDED_MAPPINGS: false`
3. Change to: `USE_EMBEDDED_MAPPINGS: true`
4. Scroll to bottom (line ~900)
5. Copy contents of `question_mapping.json` into `EMBEDDED_QUESTION_MAPPING`
6. Copy contents of `category_mapping.json` into `EMBEDDED_CATEGORY_MAPPING`
7. Re-upload the modified JavaScript file

---

### Step 4: Add to Risk Assessment Form

#### Method A: Form Button (Easiest - 5 minutes)

1. Go to **Risk Assessment** entity → **Forms** → **Main Form**
2. Click **Insert** → **Section** (or use existing section)
3. Click **Insert** → **Web Resource**
4. Create a button HTML file:

**Upload this as new Web Resource** (`new_/html/generate_report_button`):

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://docraptor.com/docraptor-1.0.0.js"></script>
    <script src="../scripts/cyberpools_report_generator.js"></script>
    <style>
        body { margin: 0; padding: 10px; background: transparent; }
        button {
            background: #2C5F7C;
            color: white;
            border: none;
            padding: 14px 28px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            border-radius: 6px;
            width: 100%;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        button:hover { background: #4A9FB8; transform: translateY(-1px); }
        button:active { transform: translateY(0); }
    </style>
</head>
<body>
    <button onclick="generateReport()">📄 Generate PDF Report</button>
    <script>
        function generateReport() {
            try {
                var formContext = window.parent.Xrm.Page;
                var executionContext = {
                    getFormContext: function() { return formContext; }
                };
                CyberPoolsReport.generateReport(executionContext);
            } catch (error) {
                alert('Error: ' + error.message);
            }
        }
    </script>
</body>
</html>
```

5. In form editor, select the button Web Resource
6. Set properties:
   - **Height:** 60px
   - **Width:** 100%
   - **Border:** No
7. **Save** and **Publish** form

#### Method B: Ribbon Button (More Professional)

*Requires Ribbon Workbench - See DEPLOYMENT_GUIDE.md for details*

---

### Step 5: Add Executive Summary Field (Optional)

To allow account managers to write formatted summaries:

1. Go to **Risk Assessment** entity → **Fields**
2. Click **New**
3. Fill in:
   - **Display Name:** Executive Summary
   - **Name:** new_executivesummary
   - **Data Type:** Multiple Lines of Text
   - **Format:** **Rich Text** ← Important!
   - **Max Length:** 10000
   - **IME Mode:** Auto
4. **Save**
5. Add to form:
   - Open **Main Form**
   - **Insert** → **Field**
   - Select **Executive Summary**
   - Set height: 200px
6. **Save** and **Publish**

---

## 🧪 Testing Your Deployment

### Test 1: Button Appears

1. Open any Risk Assessment record
2. Verify button shows on form
3. Button should say "Generate PDF Report"

### Test 2: Generate Test PDF

1. Open a completed assessment (with JSON data)
2. Click "Generate PDF Report"
3. Wait for progress indicator
4. PDF should download to browser
5. Open PDF and verify:
   - ✅ Cover page shows member name
   - ✅ Assessment date is correct
   - ✅ Results summary shows score
   - ✅ Categories appear
   - ✅ Questions are listed

### Test 3: Executive Summary

1. Edit an assessment
2. Add text to Executive Summary field
3. Use formatting: **bold**, *italic*, bullets
4. Generate PDF
5. Verify formatted text appears on page 2

---

## ⚙️ Configuration Options

### Change API Key

Edit `cyberpools-report-complete.js` line 27:

```javascript
DOCRAPTOR_API_KEY: 'YOUR_NEW_KEY_HERE'
```

Re-upload Web Resource and publish.

### Enable Test Mode (Watermarked PDFs)

Line 32:
```javascript
TEST_MODE: true  // Free unlimited watermarked PDFs
```

### Update Field Names

If your Dynamics 365 fields have different names, update lines 42-49:

```javascript
FIELD_NAMES: {
    json: 'your_json_field',
    service: 'your_service_lookup',
    totalScore: 'your_score_field',
    // etc.
}
```

---

## 🐛 Troubleshooting

### "No assessment data found"

**Cause:** JSON field is empty
**Fix:**
1. Verify assessment questions are saved
2. Check field name matches CONFIG.FIELD_NAMES.json
3. View test data to see field contents

### "DocRaptor library not loaded"

**Cause:** Internet connection issue or button HTML incorrect
**Fix:**
1. Check internet connection
2. Verify button HTML includes: `<script src="https://docraptor.com/docraptor-1.0.0.js"></script>`
3. Try loading `https://docraptor.com/docraptor-1.0.0.js` directly in browser

### "Failed to load mapping file"

**Cause:** Web Resource URL incorrect or not published
**Fix:**
1. Verify Web Resources exist and are published
2. Check names match exactly:
   - `new_/mappings/question_mapping` (no .json extension in name)
   - `new_/mappings/category_mapping`
3. Or switch to embedded mappings (see Step 3, Option B)

### PDF Downloads But Looks Wrong

**Cause:** CSS or HTML generation issue
**Fix:**
1. Open browser DevTools (F12)
2. Check Console for errors
3. Verify test-local.html works correctly
4. Compare PDF with expected output from Python version

### "API key required" or DocRaptor Error

**Cause:** Invalid API key or quota exceeded
**Fix:**
1. Verify API key is correct in line 27
2. Check DocRaptor dashboard: https://docraptor.com/account
3. Ensure you have available quota
4. Try TEST_MODE: true for unlimited testing

---

## 📊 Usage Statistics

Monitor your DocRaptor usage:

1. Go to https://docraptor.com/account
2. View **Usage** tab
3. Check:
   - Documents this month
   - Test mode vs Production
   - Quota remaining

**Cost Estimate:**
- First 5 docs/month: Free
- Additional: ~$0.12 per PDF
- Unlimited test mode PDFs (watermarked)

---

## 🔒 Security Notes

### ⚠️ API Key Visibility

Your DocRaptor API key is in the JavaScript file, which means:
- Anyone with access to Web Resources can see it
- Users can theoretically make DocRaptor calls using your key

**Mitigation:**
1. **Access Control:** Only grant Web Resource access to trusted users
2. **Monitor Usage:** Watch DocRaptor dashboard for unusual activity
3. **Rotate Keys:** Change API key periodically
4. **Future:** Migrate to Azure Function to hide key server-side

### User Permissions

Required security roles for users:
- Read access to Risk Assessment entity
- Read access to Web Resources
- Execute access to report generator script

---

## 📈 Next Steps

### Phase 1: Validation (Current)
- ✅ Deploy JavaScript POC
- ✅ Test with real assessments
- ✅ Gather user feedback
- ✅ Verify DocRaptor costs

### Phase 2: Production Hardening (Optional)
- Migrate to Azure Function (hide API key)
- Add auto-attachment to assessment record
- Email PDF to member automatically
- Add template selection

### Phase 3: Scale (If Needed)
- Deploy to RackNerd server with FastAPI
- Add queue for bulk generation
- Implement caching
- Custom branding per pool

---

## 🆘 Getting Help

### Check These First:
1. Browser console (F12) for JavaScript errors
2. Network tab for failed requests
3. Dynamics 365 Web Resource console
4. DocRaptor API dashboard for errors

### Common Issues:

| Error | Solution |
|-------|----------|
| Button not appearing | Check form is published, clear browser cache |
| Progress bar stuck | Check browser console, may be API timeout |
| PDF has no data | Verify JSON field has data, check field names |
| Formatting wrong | CSS may be cached, hard refresh (Ctrl+F5) |

---

## 📞 Support Contacts

- **DocRaptor Support:** support@docraptor.com
- **Documentation:** https://docraptor.com/documentation
- **API Status:** https://status.docraptor.com

---

## ✨ Success Checklist

After deployment, you should be able to:

- [x] Click button on Risk Assessment form
- [x] See progress indicator
- [x] Download PDF to browser
- [x] PDF contains:
  - [x] Member name and date
  - [x] Overall score
  - [x] Risk distribution
  - [x] All categories and questions
  - [x] Assessment notes
  - [x] Cyber requirements compliance
- [x] Executive summary (if field populated)
- [x] Professional CyberPools branding

---

## 🎉 You're Done!

Your JavaScript POC is complete and ready to use!

**Total deployment time:** ~15-30 minutes
**Cost:** $0 in test mode, ~$0.12/PDF in production
**Maintenance:** Upload mapping files when questions change

For advanced features (Azure Function, server deployment, etc.), see:
- `DEPLOYMENT_GUIDE.md` - Full deployment details
- `../README.md` - Project overview
- API recommendation docs

**Questions?** Check the troubleshooting section or test locally first with `test-local.html`!
