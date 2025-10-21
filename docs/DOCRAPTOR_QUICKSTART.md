# DocRaptor Quick Start Guide

✅ **DocRaptor is now set up and working!**

Your API key is already configured in the test scripts.

## What Just Happened?

I've successfully:
1. ✅ Installed DocRaptor SDK
2. ✅ Updated scripts to follow official DocRaptor documentation
3. ✅ Added your API key (`Uej3BuDjlcc3vx8z5lfK`)
4. ✅ Generated your first test PDF at `output/docraptor_test.pdf`

## Quick Test (Already Done!)

```bash
python3 scripts/quick_docraptor_test.py
```

**Output**: `output/docraptor_test.pdf` (✓ Successfully generated - 277KB)

## What to Check in the PDF

Open `output/docraptor_test.pdf` and look for these improvements:

### 1. ✅ Footer on Every Page
- Bottom center: "Page X of Y"
- Bottom left: "CyberPools Risk Assessment"
- Bottom right: Report date

**This is what you wanted!** No more footer headaches.

### 2. ✅ Better Page Breaks
- Content flows naturally
- No orphaned headers
- Questions stay together
- Categories don't split awkwardly

### 3. ✅ Professional Layout
- Consistent spacing
- Clean typography
- Proper gradients and colors
- High-quality rendering

## Test Mode vs Production Mode

### Test Mode (Current - FREE)
```bash
python3 scripts/quick_docraptor_test.py
```
- Watermarked "TEST DOCUMENT" diagonal across pages
- **Unlimited free PDFs**
- Perfect for development and testing

### Production Mode (No Watermark)
```bash
# Edit quick_docraptor_test.py line 309:
# Change 'test': True to 'test': False

# Or use the flag version:
python3 scripts/test_docraptor.py --production
```
- No watermark
- Counts against your quota (5 free/month, then $15/month for 125)

## Compare Results

You now have two PDFs to compare:

1. **Playwright version**: `output/Sample_Organization_Risk_Assessment_10-20-2025.pdf`
2. **DocRaptor version**: `output/docraptor_test.pdf`

**Key differences:**
- DocRaptor has **footers on every page** ✅
- DocRaptor has **better page breaks** ✅
- DocRaptor uses **Prince XML** (commercial-grade PDF engine)

## Integration Options

### Option 1: Replace Playwright with DocRaptor
Update `generate_report.py` to use DocRaptor instead of Playwright.

### Option 2: Add DocRaptor as Third Engine
Keep Playwright, WeasyPrint, and add DocRaptor as option:
```bash
python3 scripts/generate_report.py input.json --engine docraptor
```

### Option 3: Make DocRaptor the Default
Use DocRaptor for production, Playwright for development.

**Which do you prefer?** I can implement any of these.

## Pricing Summary

- **Test Mode**: Unlimited watermarked PDFs (FREE forever)
- **Production**: 5 PDFs/month free
- **Paid Plan**: $15/month for 125 PDFs (~$0.12 per PDF)
- **Higher Tiers**: Available for more volume

For occasional report generation, the free tier (5 production PDFs/month) might be enough!

## CSS Improvements for Prince XML

The `print_docraptor.css` file includes Prince-specific features:

```css
@page {
  @bottom-center {
    content: "Page " counter(page) " of " counter(pages);
  }
}
```

This is **not possible** in Playwright or WeasyPrint without hacks!

## Scripts Available

1. **`scripts/quick_docraptor_test.py`** - All-in-one test (what we just ran)
2. **`scripts/test_docraptor.py`** - More configurable version
3. **`scripts/generate_pdf_docraptor.py`** - Reusable DocRaptor class

## Next Steps

1. **Review the PDF** - Open `output/docraptor_test.pdf` and check the footer/page breaks
2. **Decide if you like it** - Compare with Playwright version
3. **Let me know** - I can integrate DocRaptor into your main workflow

## Troubleshooting

### API Error
If you get an API error, check:
- API key is correct: `Uej3BuDjlcc3vx8z5lfK`
- You have internet connection
- DocRaptor service is up: https://www.docraptorstatus.com/

### Module Not Found
```bash
pip install docraptor
```

### Watermark Removal
For production PDFs without watermark, change `'test': True` to `'test': False` in the script.
Note: This counts against your quota.

## Resources

- **DocRaptor Docs**: https://docraptor.com/documentation/python
- **Prince XML Reference**: https://www.princexml.com/doc/
- **Your Dashboard**: https://docraptor.com/

---

**Ready to integrate?** Let me know which option you prefer and I'll update your main report generation scripts!
