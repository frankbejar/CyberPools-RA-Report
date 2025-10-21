#!/usr/bin/env python3
"""
Quick DocRaptor Test - All-in-one script

This script:
1. Loads your existing CRM data
2. Transforms it to report format
3. Renders HTML with DocRaptor-optimized CSS
4. Generates PDF using DocRaptor API

Usage:
    # Install DocRaptor first:
    pip install docraptor

    # Run the test:
    python3 scripts/quick_docraptor_test.py

    # Output will be at: output/docraptor_test.pdf
"""

import json
import sys
import base64
import re
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Setup paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

# Import DocRaptor
try:
    import docraptor
except ImportError:
    print("[ERROR] DocRaptor SDK not installed.")
    print("\nInstall with:")
    print("  pip install docraptor")
    sys.exit(1)

# Your API key
API_KEY = "Uej3BuDjlcc3vx8z5lfK"


def load_json_file(filepath):
    """Load JSON data from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_status_text(response_value):
    """Convert response value to status text."""
    return {
        1: "Fully Implemented",
        3: "Partially Implemented",
        5: "Not Implemented",
        0: "Not Applicable"
    }.get(response_value, "Unknown")


def get_risk_level(risk_score):
    """Calculate risk level from score."""
    if risk_score <= 9:
        return "low"
    if risk_score <= 15:
        return "moderate"
    return "high"


def calculate_overall_score(questions, question_mapping):
    """Calculate overall score."""
    applicable = [q for q in questions if q['qResponse'] != 0]
    if not applicable:
        return 100

    actual = sum(q['qScore'] for q in applicable)
    min_score = sum(
        (question_mapping.get(q['qID'], {}).get('impact_score', 3) * 1)
        for q in applicable
    )
    max_score = sum(
        (question_mapping.get(q['qID'], {}).get('impact_score', 3) * 5)
        for q in applicable
    )

    if max_score == min_score:
        return 100

    final = (1 - (actual - min_score) / (max_score - min_score)) * 100
    return round(final, 0)


def calculate_category_score(questions, question_mapping):
    """Calculate category score."""
    applicable = [q for q in questions if q['qResponse'] != 0]
    if not applicable:
        return 100

    actual = sum(q['qScore'] for q in applicable)
    min_score = sum(
        (question_mapping.get(q['qID'], {}).get('impact_score', 3) * 1)
        for q in applicable
    )
    max_score = sum(
        (question_mapping.get(q['qID'], {}).get('impact_score', 3) * 5)
        for q in applicable
    )

    if max_score == min_score:
        return 100

    return round((1 - (actual - min_score) / (max_score - min_score)) * 100, 0)


def transform_crm_data(crm_questions, question_mapping, category_mapping):
    """Transform CRM data to report format."""
    print("🔄 Transforming CRM data...")

    # Calculate risk distribution
    risk_dist = {'high': 0, 'moderate': 0, 'low': 0}
    for q in crm_questions:
        if q['qResponse'] != 0:
            risk_dist[get_risk_level(q['qScore'])] += 1

    # Metadata
    metadata = {
        "member_name": "Test Organization",
        "assessment_date": datetime.now().strftime('%m/%d/%Y'),
        "conducted_by": "CyberPools Assessment Team",
        "member_contact": "Contact Person",
        "version": "v1.0"
    }

    # Calculate overall score
    overall_score = calculate_overall_score(crm_questions, question_mapping)
    grade = (
        'A' if overall_score >= 90 else
        'B' if overall_score >= 80 else
        'C' if overall_score >= 70 else
        'D' if overall_score >= 60 else
        'F'
    )

    # Group by categories
    categories_dict = {}
    for q in crm_questions:
        categories_dict.setdefault(str(q['qCat']), []).append(q)

    categories = []
    section_scores = {}

    def sort_key(number_str):
        try:
            return tuple(int(part) for part in number_str.split('.'))
        except ValueError:
            return (999,)

    # Process each category
    for cat_id, questions in sorted(
        categories_dict.items(),
        key=lambda item: sort_key(
            category_mapping.get(item[0], {}).get('number', '999.999')
        )
    ):
        cat_info = category_mapping.get(
            cat_id,
            {'number': '0.0', 'name': f'Unknown Category ({cat_id})'}
        )
        cat_score = calculate_category_score(questions, question_mapping)

        q_list = []
        for q in sorted(
            questions,
            key=lambda item: sort_key(
                question_mapping.get(item['qID'], {}).get('number', '999.999')
            )
        ):
            q_id = q['qID']
            q_info = question_mapping.get(q_id, {
                'number': '0.0',
                'text': f'Unknown Question (ID: {q_id[:8]}...)',
                'control_description': '',
                'impact_score': 3
            })
            q_list.append({
                'number': q_info['number'],
                'text': q_info['text'],
                'control_description': q_info.get('control_description', ''),
                'control_status': q['qResponse'],
                'control_status_text': get_status_text(q['qResponse']),
                'impact_score': q_info.get('impact_score', 0),
                'risk_score': q['qScore'],
                'risk_level': get_risk_level(q['qScore']),
                'comments': q.get('qNotes', '')
            })

        categories.append({
            'number': cat_info['number'],
            'name': cat_info['name'],
            'score': cat_score,
            'overview': f"Overview for {cat_info['name']}",
            'importance': f"Importance of {cat_info['name']}",
            'questions': q_list
        })
        section_scores[cat_info['number']] = {
            'name': cat_info['name'],
            'score': cat_score
        }

    # Cyber requirements
    EXCLUDED = {"b032c58a-fc8f-f011-b4cb-0022480aaebb"}
    cyber_requirements = []
    for q in crm_questions:
        if q.get('qReq', False) and q['qID'] not in EXCLUDED:
            q_info = question_mapping.get(q['qID'], {'text': 'Unknown Requirement'})
            cyber_requirements.append({
                'question': q_info['text'],
                'compliance': q['qResponse'] == 1
            })

    return {
        'metadata': metadata,
        'executive_summary': '',
        'scoring': {
            'overall_score': int(overall_score),
            'overall_grade': grade,
            'section_scores': section_scores,
            'risk_distribution': risk_dist
        },
        'cyber_requirements': cyber_requirements,
        'categories': categories
    }


def inline_css_in_html(html, assets_dir):
    """Inline CSS files into HTML for DocRaptor."""
    link_pattern = re.compile(
        r'<link\s+rel="stylesheet"\s+href="([^"]+)"[^>]*/>',
        re.IGNORECASE
    )

    def replace_link(match):
        css_path = match.group(1)
        full_path = assets_dir / css_path

        if full_path.exists():
            try:
                css_content = full_path.read_text(encoding='utf-8')
                return f'<style>\n{css_content}\n</style>'
            except Exception as e:
                print(f"⚠️  Warning: Could not read {css_path}: {e}")
                return match.group(0)
        else:
            print(f"⚠️  Warning: CSS file not found: {full_path}")
            return match.group(0)

    return link_pattern.sub(replace_link, html)


def inline_images_as_data_uri(html, assets_dir):
    """Convert local image paths to data URIs."""
    import mimetypes

    img_pattern = re.compile(r'<img\s+[^>]*src="([^"]+)"[^>]*>', re.IGNORECASE)

    def replace_img(match):
        img_path = match.group(1)

        # Skip if already a data URI or external URL
        if img_path.startswith('data:') or img_path.startswith('http'):
            return match.group(0)

        full_path = assets_dir / img_path

        if full_path.exists():
            try:
                mime_type, _ = mimetypes.guess_type(str(full_path))
                if not mime_type:
                    mime_type = 'image/png'

                img_data = full_path.read_bytes()
                encoded = base64.b64encode(img_data).decode('ascii')
                data_uri = f'data:{mime_type};base64,{encoded}'

                return match.group(0).replace(img_path, data_uri)
            except Exception as e:
                print(f"⚠️  Warning: Could not encode image {img_path}: {e}")
                return match.group(0)

        return match.group(0)

    return img_pattern.sub(replace_img, html)


def main():
    print("\n" + "=" * 70)
    print("DocRaptor PDF Test - CyberPools Risk Assessment")
    print("=" * 70 + "\n")

    # Load CRM data
    print("Loading CRM data...")
    crm_data_path = PROJECT_ROOT / 'input/cb-ra.json'
    if not crm_data_path.exists():
        print(f"[ERROR] CRM data not found at {crm_data_path}")
        sys.exit(1)

    crm_data = load_json_file(crm_data_path)
    print(f"[SUCCESS] Loaded {len(crm_data)} questions")

    # Load mappings
    print("Loading mapping files...")
    question_mapping = load_json_file(PROJECT_ROOT / 'mappings/question_mapping.json')
    category_mapping = load_json_file(PROJECT_ROOT / 'mappings/category_mapping.json')
    print("[SUCCESS] Mappings loaded")

    # Transform data
    template_data = transform_crm_data(crm_data, question_mapping, category_mapping)
    print(f"[SUCCESS] Overall Score: {template_data['scoring']['overall_score']}% "
          f"(Grade: {template_data['scoring']['overall_grade']})")

    # Load boilerplate
    boilerplate_path = PROJECT_ROOT / 'content/boilerplate.json'
    boilerplate = load_json_file(boilerplate_path) if boilerplate_path.exists() else {}

    # Merge boilerplate with categories
    if boilerplate.get('categories'):
        for category in template_data.get('categories', []):
            cat_num = category.get('number')
            if cat_num and cat_num in boilerplate['categories']:
                bp_cat = boilerplate['categories'][cat_num]
                category['overview'] = bp_cat.get('overview', category.get('overview', ''))
                category['importance'] = bp_cat.get('importance', category.get('importance', ''))

    # Check for high risk
    has_high_risk = any(
        q.get('risk_score', 0) >= 16
        for cat in template_data.get('categories', [])
        for q in cat.get('questions', [])
    )

    # Prepare context
    context = {
        **template_data,
        'boilerplate': boilerplate,
        'has_high_risk': has_high_risk,
        'report_date': datetime.now().strftime('%m/%d/%Y')
    }

    # Render HTML with DocRaptor CSS
    print("🎨 Rendering HTML template...")
    env = Environment(
        loader=FileSystemLoader(PROJECT_ROOT / 'templates'),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )
    env.filters['round'] = round

    template = env.get_template('main_template.html')
    html = template.render(context)

    # Replace print.css with print_docraptor.css
    html = html.replace(
        '<link rel="stylesheet" href="styles/print.css" media="print" />',
        '<link rel="stylesheet" href="styles/print_docraptor.css" media="print" />'
    )

    # Inline CSS and images for DocRaptor
    print("📦 Inlining CSS and images for DocRaptor...")
    html = inline_css_in_html(html, PROJECT_ROOT)
    html = inline_images_as_data_uri(html, PROJECT_ROOT)

    # Save debug HTML
    html_debug_path = PROJECT_ROOT / 'output/docraptor_debug.html'
    html_debug_path.parent.mkdir(parents=True, exist_ok=True)
    html_debug_path.write_text(html, encoding='utf-8')
    print(f"💾 Debug HTML saved: {html_debug_path}")

    # Generate PDF with DocRaptor
    output_pdf = PROJECT_ROOT / 'output/docraptor_test.pdf'
    print(f"\n🚀 Generating PDF with DocRaptor...")
    print(f"   API Key: {API_KEY[:10]}...")
    print(f"   Mode: TEST (watermarked, unlimited free)")
    print(f"   Output: {output_pdf}")

    try:
        # Initialize DocRaptor client (following official docs)
        doc_api = docraptor.DocApi()
        doc_api.api_client.configuration.username = API_KEY

        # Create PDF
        print("   Sending request to DocRaptor API...")
        response = doc_api.create_doc({
            'test': True,  # Test mode = watermarked but free
            'document_type': 'pdf',
            'document_content': html,
            'name': 'cyberpools_risk_assessment.pdf',
            'javascript': False,
            'prince_options': {
                'media': 'print',
            },
        })

        # Write PDF to file
        with open(output_pdf, 'w+b') as f:
            f.write(bytearray(response))

        print(f"\n[SUCCESS] PDF generated: {output_pdf}")
        print("\nNote: This is a TEST PDF (watermarked)")
        print("   Watermark will not appear in production mode")

        print("\nCheck these improvements:")
        print("   - Footer on every page with page numbers")
        print("   - Better page breaks (no awkward splits)")
        print("   - Natural content flow")
        print("   - Consistent spacing")

        print("\nCompare with Playwright version:")
        print(f"   DocRaptor:   {output_pdf}")
        print(f"   Playwright:  output/Sample_Organization_Risk_Assessment_*.pdf")

    except docraptor.rest.ApiException as error:
        print(f"\n[ERROR] DocRaptor API Error:")
        print(f"   Status: {error.status}")
        print(f"   Reason: {error.reason}")
        if error.body:
            print(f"   Details: {error.body}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
