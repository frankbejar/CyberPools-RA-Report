# CyberPools Report Generator - Dynamics 365 Deployment Guide

## Overview
This guide explains how to deploy the JavaScript-based PDF report generator directly into Dynamics 365.

## Prerequisites
- Dynamics 365 instance with System Administrator or Customizer role
- DocRaptor API key
- Risk Assessment entity with JSON field containing assessment data

## Architecture

```
Dynamics 365 Form
    ↓ (Button Click)
JavaScript Web Resource
    ↓ (Reads Data)
Member Record + Risk Assessment JSON
    ↓ (Transforms Data)
HTML Generation
    ↓ (API Call)
DocRaptor
    ↓ (Returns)
PDF Downloaded to Browser
```

## Files to Deploy

### 1. Main JavaScript File
**File:** `cyberpools-report-generator-complete.js`
- Contains all logic for data transformation and HTML generation
- Upload as Web Resource with name: `new_/scripts/cyberpools_report_generator.js`

### 2. Mapping Files
**Files:**
- `question_mapping.json` → Upload as `new_/mappings/question_mapping.json`
- `category_mapping.json` → Upload as `new_/mappings/category_mapping.json`

### 3. CSS Stylesheet (Optional)
**File:** `report-styles.css`
- Can be inlined in JavaScript or loaded as separate Web Resource
- Upload as `new_/styles/report_styles.css`

## Step-by-Step Deployment

### Step 1: Upload Web Resources

1. Navigate to **Settings** → **Customizations** → **Customize the System**
2. Go to **Web Resources** → **New**
3. For each file:
   - **Name:** `new_/scripts/cyberpools_report_generator.js`
   - **Display Name:** CyberPools Report Generator
   - **Type:** Script (JScript)
   - **Upload File:** Select the combined JavaScript file
   - Click **Save** then **Publish**

4. Repeat for mapping JSON files:
   - **Type:** Data (JSON)

### Step 2: Configure DocRaptor API Key

Edit the configuration section in the JavaScript file (Line 20-25):

```javascript
const CONFIG = {
    DOCRAPTOR_API_KEY: 'YOUR_PRODUCTION_API_KEY_HERE', // ← Change this!
    TEST_MODE: false, // Set to true for testing (watermarked PDFs)

    // Adjust these paths if your Web Resource names differ
    QUESTION_MAPPING_URL: 'new_/mappings/question_mapping.json',
    CATEGORY_MAPPING_URL: 'new_/mappings/category_mapping.json'
};
```

### Step 3: Add to Risk Assessment Form

#### Option A: Ribbon Button (Recommended)

1. Open the Risk Assessment form in Form Editor
2. Click **Form Properties**
3. Under **Form Libraries**, click **Add**
4. Select `new_/scripts/cyberpools_report_generator.js`
5. Add DocRaptor library:
   - Name: `DocRaptor`
   - Library: `https://docraptor.com/docraptor-1.0.0.js`
6. Click **OK** and **Publish**

7. **Add Ribbon Button:**
   - Use Ribbon Workbench or Command Bar:
   - **Button Label:** "Generate PDF Report"
   - **Command:** JavaScript Function
   - **Function Name:** `CyberPoolsReport.generateReport`
   - **Pass Execution Context:** Yes

#### Option B: Form Button (Simpler)

1. Add a Web Resource control to the form
2. **Web Resource:** `new_/scripts/report_button.html`
3. Create `report_button.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://docraptor.com/docraptor-1.0.0.js"></script>
    <script src="../scripts/cyberpools_report_generator.js"></script>
    <style>
        body { margin: 0; padding: 10px; }
        button {
            background: #2C5F7C;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            border-radius: 4px;
            width: 100%;
        }
        button:hover { background: #4A9FB8; }
    </style>
</head>
<body>
    <button onclick="generateReportClick()">Generate PDF Report</button>
    <script>
        function generateReportClick() {
            var formContext = window.parent.Xrm.Page;
            var execContext = {
                getFormContext: function() { return formContext; }
            };
            CyberPoolsReport.generateReport(execContext);
        }
    </script>
</body>
</html>
```

### Step 4: Configure Field Mappings

Ensure your Risk Assessment entity has these fields (or update the code to match your schema):

| Dynamics 365 Field | Schema Name | Type |
|-------------------|-------------|------|
| Service (Lookup) | `new_service` | Lookup to Service |
| JSON Data | `new_json` | Multiple Lines of Text |
| Total Score | `new_totalscore` | Whole Number |
| Total Grade | `new_totalgrade` | Single Line of Text |
| Template | `new_template` | Single Line of Text |
| Executive Summary (Optional) | `new_executivesummary` | Multiple Lines of Text (Rich Text) |

**To add Executive Summary field:**
1. Go to Risk Assessment entity → Fields → New
2. **Display Name:** Executive Summary
3. **Name:** new_executivesummary
4. **Data Type:** Multiple Lines of Text
5. **Format:** Rich Text
6. **Max Length:** 10000
7. Save and add to form

### Step 5: Upload Mapping Files

Create Web Resources for your mapping JSON files:

**question_mapping.json** - Upload from `/mappings/question_mapping.json`
**category_mapping.json** - Upload from `/mappings/category_mapping.json`

### Step 6: Test

1. Open a Risk Assessment record with data
2. Click "Generate PDF Report" button
3. You should see:
   - Progress indicator: "Generating PDF report..."
   - Browser download prompt for PDF file
   - Success message

## Troubleshooting

### Error: "No assessment data found"
- **Cause:** JSON field is empty
- **Fix:** Ensure risk assessment questions are saved to the JSON field

### Error: "Failed to load mapping file"
- **Cause:** Web Resource URL is incorrect
- **Fix:** Verify Web Resource names match CONFIG paths
- Check browser console for 404 errors

### Error: "DocRaptor API error"
- **Cause:** Invalid API key or quota exceeded
- **Fix:**
  - Verify API key in CONFIG
  - Check DocRaptor dashboard for quota/errors
  - Set `TEST_MODE: true` for unlimited testing

### PDF Generated but Looks Wrong
- **Cause:** CSS not loading or HTML structure issues
- **Fix:**
  - Check browser console for CSS errors
  - Compare HTML in browser DevTools
  - Test with `TEST_MODE: true` to get watermarked PDF quickly

### Button Not Appearing
- **Cause:** Web Resource not added to form
- **Fix:**
  - Verify form libraries include the script
  - Check form customization is published
  - Clear browser cache

## Security Considerations

### ⚠️ API Key Exposure
Your DocRaptor API key is visible in the JavaScript code. This means:
- Anyone with access to the Web Resource can see it
- Users can make DocRaptor API calls using your key

**Mitigation options:**
1. **User-level security:** Only give access to trusted users
2. **Monitor usage:** Watch DocRaptor dashboard for unusual activity
3. **Rotate keys:** Change API key periodically
4. **Production alternative:** Use Azure Function to hide key (see main docs)

### Permissions
Grant these security roles access to the Web Resources:
- System Administrator
- Risk Assessment Manager (custom role)
- Anyone who needs to generate reports

## Advanced Configuration

### Custom Branding
To add your logo to the cover page:

1. Upload logo as Web Resource: `new_/images/logo.png`
2. Modify `generateCoverPage()` function:

```javascript
function generateCoverPage(data) {
    return `
<div class="page cover-page">
    <img src="/WebResources/new_/images/logo.png" alt="Logo" style="max-width: 300px; margin-bottom: 30px;">
    <div class="cover-title">Risk Assessment Report</div>
    ...
    `;
}
```

### Multiple Report Templates
To support different report templates:

1. Add template field to Risk Assessment entity
2. Modify HTML generation to check template value
3. Generate different layouts based on template

### Email Integration
To automatically email the PDF instead of downloading:

1. Use `DocRaptor.createDoc()` instead of `createAndDownloadDoc()`
2. Get PDF as base64
3. Use Xrm.WebApi to create Email with attachment
4. Send via Dynamics 365 email

## Cost Considerations

### DocRaptor Pricing (as of 2024)
- **Test Mode:** Unlimited free (watermarked PDFs)
- **Production:**
  - 5 free documents/month
  - $15/month for 125 documents (~$0.12 per PDF)
  - Volume discounts available

### Recommendations
- Use Test Mode during development
- Switch to Production for client reports
- Monitor usage in DocRaptor dashboard
- Consider Azure Function for high volume (cheaper)

## Support

### Documentation
- [DocRaptor API Docs](https://docraptor.com/documentation)
- [Dynamics 365 Web Resources](https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/web-resources)

### Troubleshooting Resources
- Check browser console (F12) for JavaScript errors
- Review Dynamics 365 Web Resource console
- Test mapping files directly in browser
- Use DocRaptor test endpoint for debugging

## Next Steps

After successful deployment:

1. ✅ Test with multiple assessment records
2. ✅ Train users on the Generate PDF button
3. ✅ Set up Executive Summary field workflow
4. ✅ Monitor DocRaptor usage and costs
5. ✅ Consider Azure Function migration for production scale

## Migration Path to Azure Function

Once you've validated the JavaScript POC, you can migrate to a more secure Azure Function architecture while keeping the same user experience:

1. Deploy Python code to Azure Function (reuse existing code!)
2. Update JavaScript to call Azure Function instead of DocRaptor directly
3. API key stays secure on server
4. Same button, same user experience, better security

See `API_DEPLOYMENT_GUIDE.md` for Azure Function setup.

---

## Quick Start Checklist

- [ ] Upload main JavaScript file as Web Resource
- [ ] Upload mapping JSON files as Web Resources
- [ ] Configure DocRaptor API key in code
- [ ] Add script to Risk Assessment form
- [ ] Add "Generate PDF Report" button
- [ ] Add Executive Summary field (optional)
- [ ] Test with sample assessment
- [ ] Publish all customizations
- [ ] Train users

**Questions?** Check the troubleshooting section or review browser console for errors.
