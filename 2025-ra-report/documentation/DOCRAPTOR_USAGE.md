# How to Use DocRaptor with Your Real Data

DocRaptor has been integrated into your report generation workflow! You can now use it with your real CRM data.

## Quick Start

### Option 1: Use the All-in-One Script (Recommended)

This is the easiest way - it transforms your raw CRM JSON and generates the PDF in one command:

```bash
# Using DocRaptor (test mode - watermarked, unlimited free)
python3 scripts/transform_and_generate.py \
  --input input/cb-ra.json \
  --auto \
  --engine docraptor

# Using DocRaptor (production mode - no watermark, counts against quota)
python3 scripts/transform_and_generate.py \
  --input input/cb-ra.json \
  --auto \
  --engine docraptor \
  --production
```

### Option 2: Two-Step Process

If you want more control, you can transform the data first, then generate:

**Step 1: Transform your raw CRM JSON**
```bash
# This creates a transformed JSON file
python3 scripts/transform_crm_data.py input/cb-ra.json output/transformed.json
```

**Step 2: Generate PDF with DocRaptor**
```bash
# Test mode (watermarked)
python3 scripts/generate_report.py output/transformed.json \
  --engine docraptor \
  --output output/my_report.pdf

# Production mode (no watermark)
python3 scripts/generate_report.py output/transformed.json \
  --engine docraptor \
  --production \
  --output output/my_report.pdf
```

## Engine Options

You now have **3 PDF engines** to choose from:

| Engine | Command | Pros | Cons |
|--------|---------|------|------|
| **Playwright** | `--engine playwright` | Default, fast, free | Limited page break control, footer issues |
| **WeasyPrint** | `--engine weasyprint` | Free, open source | Limited CSS support |
| **DocRaptor** | `--engine docraptor` | Best page breaks, footers on every page, professional quality | Requires API key, test mode has watermark |

## DocRaptor Modes

### Test Mode (Default)
- **Watermark**: "TEST DOCUMENT" diagonal across pages
- **Cost**: Unlimited free
- **Use for**: Development, testing, previewing

### Production Mode
- **Watermark**: None
- **Cost**: 5 free PDFs/month, then $15/month for 125 PDFs
- **Use for**: Final client reports
- **Enable with**: `--production` flag

## Examples

### Drop JSON in Input, Generate with DocRaptor

```bash
# 1. Drop your JSON file into input/ directory
cp ~/Downloads/my-crm-export.json input/my-data.json

# 2. Generate PDF with DocRaptor (test mode)
python3 scripts/transform_and_generate.py \
  --input input/my-data.json \
  --auto \
  --engine docraptor

# Your PDF will be in output/ directory
```

### Custom Output Path

```bash
python3 scripts/transform_and_generate.py \
  --input input/cb-ra.json \
  --auto \
  --engine docraptor \
  --output output/ClientName_Assessment_2025-10-20.pdf
```

### Compare All Three Engines

```bash
# Generate with all three engines to compare
python3 scripts/transform_and_generate.py --input input/cb-ra.json --auto --engine playwright
python3 scripts/transform_and_generate.py --input input/cb-ra.json --auto --engine weasyprint
python3 scripts/transform_and_generate.py --input input/cb-ra.json --auto --engine docraptor

# Check output/ directory for the results
ls -lh output/
```

## What Makes DocRaptor Better?

DocRaptor uses **Prince XML** engine which provides:

✅ **Footers on every page** with page numbers ("Page X of Y")
✅ **Better page breaks** - sections start on new pages
✅ **No orphaned headers** - headings stay with their content
✅ **Professional quality** - commercial-grade PDF rendering
✅ **Full gradient support** - cover page looks perfect
✅ **Proper spacing** - content flows naturally

## API Key

The API key is already configured in the code:
- **Current key**: `Uej3BuDjlcc3vx8z5lfK`
- **Environment variable**: Set `DOCRAPTOR_API_KEY` to override

Get your own API key at: https://docraptor.com/signup

## Troubleshooting

### "Module not found" error
```bash
pip install docraptor
```

### API error
Check your API key is valid at: https://docraptor.com/

### Want to see the watermark?
Test mode adds "TEST DOCUMENT" watermark - this is normal and free!

### Remove watermark
Use `--production` flag (counts against your quota)

## File Locations

- **Input JSON**: `input/` directory (your raw CRM exports)
- **Output PDFs**: `output/` directory
- **Templates**: `templates/` directory
- **Styles**: `styles/` directory
  - `main.css` - Main stylesheet
  - `print_docraptor.css` - DocRaptor-specific print styles

## Need Help?

1. **View all options**: `python3 scripts/transform_and_generate.py --help`
2. **Check examples**: See this file
3. **Test with sample data**: `input/cb-ra.json` is your test file

---

**Ready to use!** Just drop your JSON in `input/` and run the command above.
