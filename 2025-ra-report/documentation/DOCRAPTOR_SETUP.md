# DocRaptor Setup Guide

DocRaptor is a cloud-based HTML-to-PDF API built on **Prince XML**, offering superior paged media support compared to Playwright or WeasyPrint.

## Why DocRaptor?

### Advantages over Playwright:
✅ **Better page break control** - Natural content flow without rigid `.page` divs
✅ **Native footer support** - CSS `@page` margin boxes for running headers/footers
✅ **Page numbers** - Built-in `counter(page)` and `counter(pages)` support
✅ **Superior typography** - Better widow/orphan control and hyphenation
✅ **No infrastructure** - Cloud API, no need to manage headless browsers

### Advantages over WeasyPrint:
✅ **Full CSS3 support** - Gradients, transforms, modern layouts work perfectly
✅ **Better rendering quality** - Prince XML is commercial-grade PDF engine
✅ **Excellent documentation** - Comprehensive Prince XML docs + DocRaptor API docs

## Pricing

- **Test Mode**: Unlimited watermarked PDFs (FREE)
- **Production**:
  - 5 documents/month FREE
  - $15/month for 125 documents
  - Pay-per-document options available

Get started: https://docraptor.com/signup

## Installation

```bash
# Install DocRaptor Python SDK
pip install docraptor
```

## Getting Your API Key

1. Sign up at https://docraptor.com/signup
2. Verify your email
3. Get your API key from the dashboard
4. Set it as an environment variable:

```bash
export DOCRAPTOR_API_KEY="your_key_here"
```

Or add to your `.bashrc` / `.zshrc`:
```bash
echo 'export DOCRAPTOR_API_KEY="your_key_here"' >> ~/.zshrc
source ~/.zshrc
```

## Quick Test

Generate a test PDF (watermarked, unlimited free):

```bash
python3 scripts/test_docraptor.py
```

This will:
1. Load your existing report data
2. Render HTML with DocRaptor-optimized CSS
3. Generate a watermarked PDF at `output/docraptor_test.pdf`
4. Create debug HTML at `output/docraptor_debug.html`

## Production PDF

Generate a production PDF (no watermark, counts against quota):

```bash
python3 scripts/test_docraptor.py --production
```

## Custom Input/Output

```bash
# Use different transformed JSON file
python3 scripts/test_docraptor.py --input output/my_data.json

# Custom output location
python3 scripts/test_docraptor.py --output reports/my_report.pdf

# Pass API key directly (instead of env var)
python3 scripts/test_docraptor.py --api-key YOUR_KEY_HERE
```

## Integration with Existing Workflow

### Option 1: Add to generate_report.py

Update `scripts/generate_report.py` to support DocRaptor engine:

```python
def generate_pdf_docraptor(html_content: str, output_path: Path, api_key: str, test_mode: bool):
    from scripts.generate_pdf_docraptor import DocRaptorPDF
    renderer = DocRaptorPDF(api_key=api_key)
    renderer.render_html_to_pdf(html_content, output_path, test_mode=test_mode)

# In main():
parser.add_argument("--engine", choices=["playwright", "weasyprint", "docraptor"], default="playwright")
parser.add_argument("--docraptor-key", default=os.environ.get("DOCRAPTOR_API_KEY"))
parser.add_argument("--docraptor-test", action="store_true", help="Use DocRaptor test mode")

# Then:
if engine == "docraptor":
    generate_pdf_docraptor(html_content, output_path, args.docraptor_key, args.docraptor_test)
```

### Option 2: Use transform_and_generate.py

Similar modifications to `transform_and_generate.py` for end-to-end workflow.

## Key Features to Check

After generating your first PDF, verify these improvements:

### 1. Footer Positioning ✅
- Footer should be anchored at bottom of EVERY page
- Shows "Page X of Y" page numbers
- Left footer: "CyberPools Risk Assessment"
- Right footer: Report date

### 2. Page Breaks ✅
- Content flows naturally (no forced page breaks every section)
- Questions keep together (no split questions)
- Category headers don't orphan (stay with content)
- Tables don't break mid-row

### 3. Styling ✅
- Gradients render perfectly
- Colors are vibrant (not washed out)
- Typography is crisp
- Backgrounds print correctly

## CSS Changes for DocRaptor

The test script automatically uses `print_docraptor.css` which includes:

```css
@page {
  size: letter portrait;
  margin: 0.6in 0.7in 0.9in 0.7in;

  @bottom-center {
    content: "Page " counter(page) " of " counter(pages);
  }

  @bottom-left {
    content: "CyberPools Risk Assessment";
  }

  @bottom-right {
    content: string(report-date);
  }
}
```

This provides **running footers** that appear on every page automatically.

## Troubleshooting

### "DocRaptor API key required"
- Make sure you set `DOCRAPTOR_API_KEY` environment variable
- Or pass `--api-key` argument

### "pip: docraptor not found"
```bash
pip install docraptor
# or
pip3 install docraptor
```

### Images not showing
- The test script auto-converts images to data URIs
- Make sure image files exist in the `logo/` directory

### CSS not applying
- CSS is inlined automatically by the test script
- Check `output/docraptor_debug.html` to verify CSS is present

### API errors
- Check your API key is valid
- Verify you haven't exceeded quota (if in production mode)
- Test mode should always work (unlimited)

## Next Steps

1. **Test the output**: Compare `output/docraptor_test.pdf` with your current Playwright PDFs
2. **Evaluate quality**: Check page breaks, footer positioning, overall layout
3. **Decide on integration**: Add DocRaptor as another engine option or replace Playwright
4. **Optimize CSS**: Fine-tune `print_docraptor.css` for your specific needs

## Resources

- DocRaptor Documentation: https://docraptor.com/documentation
- Prince XML CSS Reference: https://www.princexml.com/doc/css-refs/
- Paged Media Guide: https://www.princexml.com/doc/paged/

## Support

DocRaptor has excellent customer support. If you have questions:
- Email: support@docraptor.com
- Documentation: https://docraptor.com/documentation
- Prince XML Forum: https://www.princexml.com/forum/

---

**Ready to test?**

```bash
# Set your API key
export DOCRAPTOR_API_KEY="your_key_from_docraptor_dashboard"

# Run test
python3 scripts/test_docraptor.py

# Check output
open output/docraptor_test.pdf
```
