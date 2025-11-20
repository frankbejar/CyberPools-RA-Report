#!/usr/bin/env python3
"""
CyberPools Risk Assessment Report Generator (non-interactive)

- Loads a fully transformed data structure (already grouped, scored, etc.)
- Renders HTML + converts to PDF
- Engine switch: --engine playwright|weasyprint (default: playwright)

If you want the interactive transforms + prompts, use transform_and_generate.py instead.
"""

from __future__ import annotations

import json
import sys
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML, CSS
import logging

# Handle imports from both project root and scripts/ directory
try:
    from generate_pdf_playwright import PlaywrightPDF
    from generate_pdf_docraptor import DocRaptorPDF
except ModuleNotFoundError:
    from scripts.generate_pdf_playwright import PlaywrightPDF  # type: ignore
    from scripts.generate_pdf_docraptor import DocRaptorPDF  # type: ignore

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# DocRaptor API key - get from environment or use default test key
import os
DOCRAPTOR_API_KEY = os.getenv('DOCRAPTOR_API_KEY', 'Uej3BuDjlcc3vx8z5lfK')


def load_json_file(filepath: Path | str):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def setup_jinja_environment():
    template_dir = Path('templates')
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )
    env.filters['round'] = round
    return env


def render_html(template_name: str, context: dict) -> str:
    env = setup_jinja_environment()
    template = env.get_template(template_name)
    return template.render(context)


def generate_pdf_weasyprint(html_content: str, output_path: Path):
    css_files = [CSS(filename='styles/main.css'), CSS(filename='styles/print.css')]
    HTML(string=html_content, base_url='.').write_pdf(
        str(output_path),
        stylesheets=css_files,
        optimize_size=('fonts', 'images')
    )


def generate_pdf_playwright(html_content: str, output_path: Path, ci_mode: bool):
    renderer = PlaywrightPDF(
        page_format="Letter",
        prefer_css_page_size=True,
        print_background=True,
        no_sandbox=ci_mode,
        chromium_args=["--font-render-hinting=none"],
        display_header_footer=False,
    )
    renderer.render_html_to_pdf(html_content, output_path, assets_dir=Path("."))


def inline_css_for_docraptor(html_content: str) -> str:
    """
    Inline CSS files into HTML for DocRaptor.
    DocRaptor needs all assets inlined since it can't access local files.
    """
    # Read CSS files
    main_css = Path('styles/main.css').read_text(encoding='utf-8')
    print_css = Path('styles/print_docraptor.css').read_text(encoding='utf-8')

    # Combine into ONE style block - print CSS comes LAST to override
    inline_styles = f"""<style>
{main_css}

/* ========================================
   DOCRAPTOR PRINT OVERRIDES
   ======================================== */
{print_css}
</style>"""

    # Replace the <link> tags with inline styles
    # Remove existing link tags for styles
    import re
    html_content = re.sub(r'<link rel="stylesheet"[^>]*href="styles/main\.css"[^>]*/?>', '', html_content)
    html_content = re.sub(r'<link rel="stylesheet"[^>]*href="styles/print\.css"[^>]*/?>', '', html_content)
    html_content = re.sub(r'<link rel="stylesheet"[^>]*href="styles/print_docraptor\.css"[^>]*/?>', '', html_content)

    # Insert inline styles in head
    html_content = html_content.replace('</head>', f'{inline_styles}\n</head>')

    return html_content


def generate_pdf_docraptor(html_content: str, output_path: Path, test_mode: bool = True):
    """
    Generate PDF using DocRaptor API (Prince XML engine).

    Args:
        html_content: HTML to convert
        output_path: Where to save PDF
        test_mode: True = watermarked test PDF (unlimited free)
                   False = production PDF (counts against quota)
    """
    # Inline CSS since DocRaptor can't access local files
    html_with_inline_css = inline_css_for_docraptor(html_content)

    renderer = DocRaptorPDF(api_key=DOCRAPTOR_API_KEY)
    renderer.render_html_to_pdf(html_with_inline_css, output_path, test_mode=test_mode)


def generate_report_from_transformed_json(
    transformed_json_path: Path,
    output_pdf_path: Path,
    engine: str = "playwright",
    ci_mode: bool = False,
    docraptor_test_mode: bool = True,
) -> None:
    # transformed JSON should already contain: metadata, scoring, categories, cyber_requirements, etc.
    data = load_json_file(transformed_json_path)

    # Load boilerplate and merge category text if present
    boilerplate_path = Path('content/boilerplate.json')
    boilerplate = load_json_file(boilerplate_path) if boilerplate_path.exists() else {}

    if boilerplate.get('categories'):
        for category in data.get('categories', []):
            cat_num = category.get('number')
            if cat_num and cat_num in boilerplate['categories']:
                bp_cat = boilerplate['categories'][cat_num]
                category['overview'] = bp_cat.get('overview', category.get('overview', ''))
                category['importance'] = bp_cat.get('importance', category.get('importance', ''))

    # High-risk flag
    has_high_risk = any(
        q.get('risk_score', 0) >= 16
        for cat in data.get('categories', [])
        for q in cat.get('questions', [])
    )

    context = {**data, 'boilerplate': boilerplate, 'has_high_risk': has_high_risk}
    html_content = render_html('main_template.html', context)

    output_pdf_path.parent.mkdir(parents=True, exist_ok=True)
    if engine == "weasyprint":
        generate_pdf_weasyprint(html_content, output_pdf_path)
    elif engine == "docraptor":
        generate_pdf_docraptor(html_content, output_pdf_path, test_mode=docraptor_test_mode)
    else:
        generate_pdf_playwright(html_content, output_pdf_path, ci_mode)

    logger.info(f"✔ PDF generated: {output_pdf_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate PDF from a transformed JSON file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate with Playwright (default)
  python3 scripts/generate_report.py input/data.json

  # Generate with DocRaptor (test mode - watermarked, unlimited free)
  python3 scripts/generate_report.py input/data.json --engine docraptor

  # Generate with DocRaptor (production mode - no watermark, counts against quota)
  python3 scripts/generate_report.py input/data.json --engine docraptor --production

  # Custom output path
  python3 scripts/generate_report.py input/data.json --output output/my_report.pdf --engine docraptor
        """
    )
    parser.add_argument("input_json", help="Path to transformed JSON (not raw CRM export).")
    parser.add_argument("--output", help="Output PDF path (default: output/report.pdf)")
    parser.add_argument("--engine", choices=["playwright", "weasyprint", "docraptor"], default="playwright",
                        help="PDF engine: playwright (default), weasyprint, or docraptor")
    parser.add_argument("--ci", action="store_true", help="Chromium no-sandbox/CI mode (playwright only)")
    parser.add_argument("--production", action="store_true",
                        help="DocRaptor production mode (no watermark, counts against quota). Default is test mode (watermarked, unlimited free).")
    args = parser.parse_args()

    input_path = Path(args.input_json)
    if not input_path.exists():
        logger.error(f"File not found: {input_path}")
        sys.exit(1)

    out_path = Path(args.output) if args.output else Path("output/report.pdf")

    # DocRaptor test mode is the inverse of production flag
    docraptor_test_mode = not args.production

    try:
        generate_report_from_transformed_json(
            input_path,
            out_path,
            engine=args.engine,
            ci_mode=args.ci,
            docraptor_test_mode=docraptor_test_mode
        )
    except Exception as e:
        logger.error(f"Error generating report: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
