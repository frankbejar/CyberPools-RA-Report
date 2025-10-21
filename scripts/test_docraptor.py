#!/usr/bin/env python3
"""
Test script to generate a CyberPools report using DocRaptor.

This script:
1. Loads your existing transformed JSON data
2. Renders HTML using your existing Jinja templates
3. Converts to PDF using DocRaptor (Prince XML engine)
4. Compares with Playwright output

Usage:
    # First, install DocRaptor SDK:
    pip install docraptor

    # Get a free API key from: https://docraptor.com/signup

    # Run test with your API key:
    export DOCRAPTOR_API_KEY="your_key_here"
    python3 scripts/test_docraptor.py

    # Or pass key directly:
    python3 scripts/test_docraptor.py --api-key YOUR_KEY

    # For production (non-watermarked) PDF:
    python3 scripts/test_docraptor.py --production
"""

import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime

# Add scripts directory to path
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from jinja2 import Environment, FileSystemLoader, select_autoescape

try:
    from generate_pdf_docraptor import DocRaptorPDF
except ImportError:
    print("Error: DocRaptor SDK not installed.")
    print("Install with: pip install docraptor")
    sys.exit(1)


def load_json_file(filepath: Path):
    """Load JSON data from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def render_html_with_docraptor_css(template_name: str, context: dict) -> str:
    """Render Jinja template with DocRaptor-optimized CSS."""
    env = Environment(
        loader=FileSystemLoader(PROJECT_ROOT / 'templates'),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )
    env.filters['round'] = round

    template = env.get_template(template_name)
    html = template.render(context)

    # Replace print.css with print_docraptor.css for better Prince XML support
    html = html.replace(
        '<link rel="stylesheet" href="styles/print.css" media="print" />',
        '<link rel="stylesheet" href="styles/print_docraptor.css" media="print" />'
    )

    return html


def inline_css_in_html(html: str, assets_dir: Path) -> str:
    """
    Inline CSS files into HTML for DocRaptor.

    DocRaptor doesn't have access to local files, so we need to inline CSS.
    """
    import re

    # Find all <link rel="stylesheet"> tags
    link_pattern = re.compile(r'<link\s+rel="stylesheet"\s+href="([^"]+)"[^>]*/?>', re.IGNORECASE)

    def replace_link(match):
        css_path = match.group(1)
        full_path = assets_dir / css_path

        if full_path.exists():
            try:
                css_content = full_path.read_text(encoding='utf-8')
                return f'<style>\n{css_content}\n</style>'
            except Exception as e:
                print(f"Warning: Could not read {css_path}: {e}")
                return match.group(0)
        else:
            print(f"Warning: CSS file not found: {full_path}")
            return match.group(0)

    return link_pattern.sub(replace_link, html)


def inline_images_as_data_uri(html: str, assets_dir: Path) -> str:
    """
    Convert local image paths to data URIs.

    DocRaptor doesn't have access to local files, so we convert images to base64.
    """
    import re
    import base64
    import mimetypes

    # Find all <img src="..."> tags
    img_pattern = re.compile(r'<img\s+[^>]*src="([^"]+)"[^>]*>', re.IGNORECASE)

    def replace_img(match):
        img_path = match.group(1)

        # Skip if already a data URI or external URL
        if img_path.startswith('data:') or img_path.startswith('http'):
            return match.group(0)

        full_path = assets_dir / img_path

        if full_path.exists():
            try:
                # Determine MIME type
                mime_type, _ = mimetypes.guess_type(str(full_path))
                if not mime_type:
                    mime_type = 'image/png'

                # Read and encode image
                img_data = full_path.read_bytes()
                encoded = base64.b64encode(img_data).decode('ascii')
                data_uri = f'data:{mime_type};base64,{encoded}'

                # Replace src attribute
                return match.group(0).replace(img_path, data_uri)
            except Exception as e:
                print(f"Warning: Could not encode image {img_path}: {e}")
                return match.group(0)
        else:
            print(f"Warning: Image file not found: {full_path}")
            return match.group(0)

    return img_pattern.sub(replace_img, html)


def main():
    parser = argparse.ArgumentParser(description='Test DocRaptor PDF generation')
    parser.add_argument(
        '--api-key',
        help='DocRaptor API key',
        default='Uej3BuDjlcc3vx8z5lfK'  # Your API key
    )
    parser.add_argument(
        '--input',
        help='Path to transformed JSON file',
        default='output/transformed_report_data.json'
    )
    parser.add_argument(
        '--output',
        help='Output PDF path',
        default='output/docraptor_test.pdf'
    )
    parser.add_argument(
        '--production',
        action='store_true',
        help='Generate production PDF (no watermark, counts against quota)'
    )
    args = parser.parse_args()

    # API key is set by default now
    if not args.api_key:
        print("Error: DocRaptor API key required.")
        sys.exit(1)

    # Check if we have transformed data
    input_path = PROJECT_ROOT / args.input

    if not input_path.exists():
        print(f"Transformed JSON not found: {input_path}")
        print("\nGenerating transformed data first...")

        # Use the interactive script to generate transformed JSON
        import subprocess
        result = subprocess.run([
            'python3',
            str(PROJECT_ROOT / 'scripts/transform_and_generate.py'),
            '--input', 'input/cb-ra.json',
            '--auto',
            '--engine', 'playwright'  # Just to generate the transformed data
        ], cwd=PROJECT_ROOT)

        if result.returncode != 0:
            print("Error: Could not generate transformed data")
            sys.exit(1)

    # Load transformed data
    print(f"\n📄 Loading data from: {input_path}")
    data = load_json_file(input_path)

    # Load boilerplate
    boilerplate_path = PROJECT_ROOT / 'content/boilerplate.json'
    boilerplate = load_json_file(boilerplate_path) if boilerplate_path.exists() else {}

    # Merge boilerplate with categories
    if boilerplate.get('categories'):
        for category in data.get('categories', []):
            cat_num = category.get('number')
            if cat_num and cat_num in boilerplate['categories']:
                bp_cat = boilerplate['categories'][cat_num]
                category['overview'] = bp_cat.get('overview', category.get('overview', ''))
                category['importance'] = bp_cat.get('importance', category.get('importance', ''))

    # Check for high risk
    has_high_risk = any(
        q.get('risk_score', 0) >= 16
        for cat in data.get('categories', [])
        for q in cat.get('questions', [])
    )

    # Prepare context
    context = {
        **data,
        'boilerplate': boilerplate,
        'has_high_risk': has_high_risk,
        'report_date': datetime.now().strftime('%m/%d/%Y')
    }

    # Render HTML
    print("🎨 Rendering HTML template...")
    html = render_html_with_docraptor_css('main_template.html', context)

    # Inline CSS and images for DocRaptor
    print("📦 Inlining CSS and images for DocRaptor...")
    html = inline_css_in_html(html, PROJECT_ROOT)
    html = inline_images_as_data_uri(html, PROJECT_ROOT)

    # Save HTML for debugging (optional)
    html_debug_path = PROJECT_ROOT / 'output/docraptor_debug.html'
    html_debug_path.write_text(html, encoding='utf-8')
    print(f"💾 Debug HTML saved to: {html_debug_path}")

    # Generate PDF with DocRaptor
    output_pdf = PROJECT_ROOT / args.output

    print(f"\n🚀 Generating PDF with DocRaptor...")
    print(f"   Mode: {'PRODUCTION' if not args.production else 'TEST (watermarked)'}")
    print(f"   Output: {output_pdf}")

    try:
        renderer = DocRaptorPDF(api_key=args.api_key)
        renderer.render_html_to_pdf(
            html,
            output_pdf,
            test_mode=not args.production,
            assets_dir=PROJECT_ROOT
        )

        print(f"\n[SUCCESS] PDF generated: {output_pdf}")

        if not args.production:
            print("\nNote: This is a TEST PDF (watermarked)")
            print("   Use --production flag for production PDF (counts against quota)")

        print("\nCompare with Playwright version:")
        print(f"   DocRaptor:   {output_pdf}")
        print(f"   Playwright:  output/Sample_Organization_Risk_Assessment_*.pdf")

        print("\nKey improvements to look for:")
        print("   - Footer anchored to bottom of each page with page numbers")
        print("   - Better page break handling (content flows naturally)")
        print("   - No orphaned headers or awkward breaks")
        print("   - Consistent spacing and layout")

    except Exception as e:
        print(f"\n[ERROR] Error generating PDF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
