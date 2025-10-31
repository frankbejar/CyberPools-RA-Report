#!/usr/bin/env python3
"""
PROOF OF CONCEPT: Dual-Score Model
CyberPools Risk Assessment Report Generator with Foundation + Maturity Scoring

This POC adds:
- Foundation Score (based on 12 cyber requirement questions)
- Maturity Score (existing full assessment score)
- Dual score display in reports

To test:
    python3 scripts/transform_and_generate_POC.py --input input/CBS-CBS.json --auto --engine docraptor
"""

from __future__ import annotations

import base64
import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from html import escape
from decimal import Decimal, ROUND_HALF_UP

from jinja2 import Environment, FileSystemLoader, select_autoescape

try:
    from markdown import markdown
    MARKDOWN_AVAILABLE = True
except ModuleNotFoundError:
    markdown = None
    MARKDOWN_AVAILABLE = False


COMPLIANCE_QUESTION_NUMBERS = {
    "1.4",
    "2.3",
    "2.4",
    "2.5",
    "2.6",
    "4.3",
    "4.7",
    "5.4",
    "6.3",
    "6.4",
    "7.2",
    "7.3",
}

# ---------- Robust path setup (root-insensitive) ----------
THIS_FILE = Path(__file__).resolve()
SCRIPTS_DIR = THIS_FILE.parent
PROJECT_ROOT = SCRIPTS_DIR.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

def p(*parts: str | Path) -> Path:
    """Path under project root."""
    return PROJECT_ROOT.joinpath(*map(str, parts))
# -----------------------------------------------------------

# Lazy import WeasyPrint only when used (optional dependency)
def _import_weasyprint():
    from weasyprint import HTML, CSS
    return HTML, CSS

# Playwright renderer (sibling import with fallback)
try:
    from generate_pdf_playwright import PlaywrightPDF
except ModuleNotFoundError:
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    from scripts.generate_pdf_playwright import PlaywrightPDF  # type: ignore

# DocRaptor renderer (sibling import with fallback)
try:
    from generate_pdf_docraptor import DocRaptorPDF
except ModuleNotFoundError:
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    from scripts.generate_pdf_docraptor import DocRaptorPDF  # type: ignore

# DocRaptor API key
import os
DOCRAPTOR_API_KEY = os.getenv('DOCRAPTOR_API_KEY', 'Uej3BuDjlcc3vx8z5lfK')


# ---------- Pretty console colors ----------
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header():
    print("\n" + "="*70)
    print(f"{Colors.BOLD}CyberPools Risk Assessment - DUAL SCORE POC{Colors.END}")
    print("="*70 + "\n")

def print_success(message): print(f"{Colors.GREEN}[SUCCESS] {message}{Colors.END}")
def print_error(message):   print(f"{Colors.RED}[ERROR] {message}{Colors.END}")
def print_info(message):    print(f"{Colors.BLUE}[INFO] {message}{Colors.END}")


# ---------- File helpers ----------
def load_json_file(filepath: Path | str):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print_error(f"File not found: {filepath}")
        return None
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON in {filepath}: {e}")
        return None

def convert_freeform_text(raw_text: str, use_markdown: bool) -> str:
    if not raw_text:
        return ""
    if use_markdown and MARKDOWN_AVAILABLE:
        return markdown(raw_text, extensions=["extra"])
    if use_markdown and not MARKDOWN_AVAILABLE:
        print_error("Markdown support requested but the 'markdown' package is not installed. Rendering as plain text.")
    escaped = escape(raw_text)
    return escaped.replace("\r\n", "\n").replace("\n\n", "<br><br>").replace("\n", "<br>")

def get_logo_data_uri() -> str:
    logo_path = p('logo', 'cp-white-logo.png')
    if not logo_path.exists():
        print_error(f"Logo not found at {logo_path}. Cover will fall back to text branding.")
        return ""
    try:
        data = logo_path.read_bytes()
        encoded = base64.b64encode(data).decode('ascii')
        return f"data:image/png;base64,{encoded}"
    except Exception as exc:
        print_error(f"Failed to embed logo: {exc}")
        return ""


# ---------- Scoring helpers ----------
def get_status_text(response_value):
    return {1: "Fully Implemented", 3: "Partially Implemented", 5: "Not Implemented", 0: "Not Applicable"}.get(response_value, "Unknown")

def get_risk_level(risk_score):
    if risk_score <= 9:   return "low"
    if risk_score <= 15:  return "moderate"
    return "high"

def calculate_overall_score(questions, question_mapping):
    applicable = [q for q in questions if q['qResponse'] != 0]
    if not applicable: return 100
    actual = sum(q['qScore'] for q in applicable)
    min_score = sum((question_mapping.get(q['qID'], {}).get('impact_score', 3) * 1) for q in applicable)
    max_score = sum((question_mapping.get(q['qID'], {}).get('impact_score', 3) * 5) for q in applicable)
    if max_score == min_score: return 100
    final = (1 - (actual - min_score) / (max_score - min_score)) * 100
    return int(Decimal(final).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

def calculate_category_score(questions, question_mapping):
    applicable = [q for q in questions if q['qResponse'] != 0]
    if not applicable: return 100
    actual = sum(q['qScore'] for q in applicable)
    min_score = sum((question_mapping.get(q['qID'], {}).get('impact_score', 3) * 1) for q in applicable)
    max_score = sum((question_mapping.get(q['qID'], {}).get('impact_score', 3) * 5) for q in applicable)
    if max_score == min_score: return 100
    category_final = (1 - (actual - min_score) / (max_score - min_score)) * 100
    return int(Decimal(category_final).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

def get_grade(score):
    """Convert numeric score to letter grade."""
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

# ========== POC: NEW DUAL SCORING FUNCTIONS ==========

def calculate_foundation_score(questions, question_mapping):
    """
    POC: Calculate score based ONLY on cyber requirement questions.
    Uses same logic as cyber_requirements: qReq=true OR question number in COMPLIANCE_QUESTION_NUMBERS.
    Returns: (score, status, foundation_questions_list)
    """
    # Filter foundation questions using same logic as cyber_requirements
    foundation_qs = []
    for q in questions:
        if q['qID'] in EXCLUDED_CYBER_REQUIREMENTS:
            continue
        q_info = question_mapping.get(q['qID'], {})
        q_number = q_info.get('number', '0.0')
        include_requirement = q.get('qReq', False) or q_number in COMPLIANCE_QUESTION_NUMBERS
        if include_requirement:
            foundation_qs.append(q)

    # Separate applicable from N/A
    applicable = [q for q in foundation_qs if q['qResponse'] != 0]

    if not applicable:
        return 100, "CERTIFIED", []

    # Calculate score using same formula
    score = calculate_overall_score(applicable, question_mapping)

    # Determine foundation status
    if score >= 85:
        status = "CERTIFIED"
    elif score >= 70:
        status = "MEETS FOUNDATION"
    else:
        status = "BELOW FOUNDATION"

    # Build foundation questions detail for report
    foundation_details = []
    for q in foundation_qs:
        q_info = question_mapping.get(q['qID'], {})
        foundation_details.append({
            'number': q_info.get('number', '0.0'),
            'text': q_info.get('text', 'Unknown'),
            'control_status': q['qResponse'],
            'control_status_text': get_status_text(q['qResponse']),
            'risk_score': q['qScore'],
            'risk_level': get_risk_level(q['qScore']),
            'impact_score': q_info.get('impact_score', 3),
            'comments': q.get('qNotes', '')
        })

    # Sort by question number
    foundation_details.sort(key=lambda x: float(x['number'].split('.')[0]) * 100 + float(x['number'].split('.')[1]) if '.' in x['number'] else 0)

    return score, status, foundation_details

def get_foundation_status_description(status):
    """Get human-readable description for foundation status."""
    descriptions = {
        "CERTIFIED": "Organization meets all core cyber insurance requirements and foundation security controls",
        "MEETS FOUNDATION": "Organization meets minimum foundation requirements with some opportunities for improvement",
        "BELOW FOUNDATION": "Critical gaps identified in foundation security controls that require immediate attention"
    }
    return descriptions.get(status, "Status unknown")

def get_maturity_description(grade, score):
    """Get human-readable description for maturity grade."""
    descriptions = {
        'A': "Exceptional security posture with comprehensive controls across all assessment areas",
        'B': "Strong security posture with well-implemented controls and minor opportunities for improvement",
        'C': "Adequate security posture with room for improvement in multiple areas",
        'D': "Below average security posture requiring significant improvements",
        'F': "Poor security posture with critical deficiencies requiring immediate remediation"
    }
    return descriptions.get(grade, "Maturity level unknown")

# ======================================================


# ---------- Transform ----------
EXCLUDED_CYBER_REQUIREMENTS = {
    "b032c58a-fc8f-f011-b4cb-0022480aaebb",  # Cyber insurance participation (informational only)
}

def transform_crm_data(crm_questions, metadata_input, executive_summary, question_mapping, category_mapping, include_compliance=True):
    print_info("Transforming CRM data to template format...")
    print_info("POC: Calculating dual scores (Foundation + Maturity)...")

    risk_dist = {'high': 0, 'moderate': 0, 'low': 0}
    for q in crm_questions:
        if q['qResponse'] != 0:
            risk_dist[get_risk_level(q['qScore'])] += 1

    metadata = {
        "member_name": metadata_input['member_name'],
        "assessment_date": metadata_input['assessment_date'],
        "conducted_by": metadata_input['conducted_by'],
        "member_contact": metadata_input['member_contact'],
        "version": metadata_input.get('version', 'v1.0')
    }

    # POC: Calculate scores with 80/20 weighted blend
    foundation_score, foundation_status, foundation_questions = calculate_foundation_score(crm_questions, question_mapping)
    comprehensive_score = calculate_overall_score(crm_questions, question_mapping)

    # Blended Maturity Score: 80% Foundation + 20% Comprehensive
    maturity_score = int(foundation_score * 0.8 + comprehensive_score * 0.2)
    maturity_grade = get_grade(maturity_score)

    print_success(f"Tier I Score (Foundation): {foundation_score}%")
    print_success(f"Comprehensive Score: {comprehensive_score}%")
    print_success(f"Tier II Score (80/20 Weighted): {maturity_score}%")

    categories_dict = {}
    for q in crm_questions:
        categories_dict.setdefault(str(q['qCat']), []).append(q)

    categories = []
    section_scores = {}

    def sort_key(number_str: str) -> tuple[int, ...]:
        try:
            return tuple(int(part) for part in number_str.split('.'))
        except ValueError:
            return (999,)

    for cat_id, questions in sorted(
        categories_dict.items(),
        key=lambda item: sort_key(category_mapping.get(item[0], {}).get('number', '999.999'))
    ):
        cat_info = category_mapping.get(cat_id, {'number': '0.0', 'name': f'Unknown Category ({cat_id})'})
        cat_score = calculate_category_score(questions, question_mapping)

        q_list = []
        for q in sorted(questions, key=lambda item: sort_key(question_mapping.get(item['qID'], {}).get('number', '999.999'))):
            q_id = q['qID']
            q_info = question_mapping.get(q_id, {
                'number': '0.0',
                'text': f'Unknown Question (ID: {q_id[:8]}...)',
                'control_description': '',
                'impact_score': 3
            })
            # Check if this is a foundation question using same logic as calculate_foundation_score
            q_number = q_info.get('number', '0.0')
            is_foundation = (q.get('qReq', False) or q_number in COMPLIANCE_QUESTION_NUMBERS) and q_id not in EXCLUDED_CYBER_REQUIREMENTS

            q_list.append({
                'number': q_info['number'],
                'text': q_info['text'],
                'control_description': q_info.get('control_description', ''),
                'control_status': q['qResponse'],
                'control_status_text': get_status_text(q['qResponse']),
                'impact_score': q_info.get('impact_score', 0),
                'risk_score': q['qScore'],
                'risk_level': get_risk_level(q['qScore']),
                'comments': q.get('qNotes', ''),
                'is_foundation': is_foundation  # POC: Flag foundation questions
            })

        categories.append({
            'number': cat_info['number'],
            'name': cat_info['name'],
            'score': cat_score,
            'overview': f"Overview for {cat_info['name']}",
            'importance': f"Importance of {cat_info['name']}",
            'questions': q_list
        })
        section_scores[cat_info['number']] = {'name': cat_info['name'], 'score': cat_score}

    cyber_requirements = []
    if include_compliance:
        for q in crm_questions:
            if q['qID'] in EXCLUDED_CYBER_REQUIREMENTS:
                continue
            q_info = question_mapping.get(q['qID'], {'text': 'Unknown Requirement', 'number': '0.0'})
            q_number = q_info.get('number', '0.0')
            include_requirement = q.get('qReq', False) or q_number in COMPLIANCE_QUESTION_NUMBERS
            if include_requirement:
                cyber_requirements.append({
                    'question': q_info.get('text', 'Unknown Requirement'),
                    'number': q_number,
                    'compliance': q['qResponse'] == 1
                })

        cyber_requirements.sort(
            key=lambda x: float(x['number']) if x['number'] and x['number'] != '0.0' else 999
        )

    return {
        'metadata': metadata,
        'executive_summary': executive_summary,
        'scoring': {
            # POC: Dual scoring with weighted blend
            'foundation_score': int(foundation_score),
            'foundation_status': foundation_status,
            'foundation_status_description': get_foundation_status_description(foundation_status),
            'comprehensive_score': int(comprehensive_score),
            'maturity_score': int(maturity_score),  # 80/20 weighted blend
            'maturity_grade': maturity_grade,
            'maturity_description': get_maturity_description(maturity_grade, maturity_score),
            # Legacy fields for compatibility
            'overall_score': int(maturity_score),
            'overall_grade': maturity_grade,
            'section_scores': section_scores,
            'risk_distribution': risk_dist
        },
        'foundation_questions': foundation_questions,  # POC: Foundation questions detail
        'cyber_requirements': cyber_requirements,
        'categories': categories,
        'logo_data_uri': get_logo_data_uri()
    }


# ---------- Render + PDF ----------
def render_html(context: dict) -> str:
    # POC: Use POC templates directory
    template_dir = p('templates_POC') if (p('templates_POC')).exists() else p('templates')
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )
    tpl = env.get_template('main_template.html')
    return tpl.render(context)

def inline_css_for_docraptor(html_content: str) -> str:
    """Inline CSS files into HTML for DocRaptor."""
    main_css = p('styles', 'main.css').read_text(encoding='utf-8')
    print_css = p('styles', 'print_docraptor.css').read_text(encoding='utf-8')

    # POC: Add POC CSS if it exists
    poc_css_path = p('styles', 'dual_score_POC.css')
    poc_css = poc_css_path.read_text(encoding='utf-8') if poc_css_path.exists() else ""

    # Combine into ONE style block - print CSS comes LAST to override
    inline_styles = f"""<style>
{main_css}

/* ========================================
   DOCRAPTOR PRINT OVERRIDES
   ======================================== */
{print_css}

/* ========================================
   POC: DUAL SCORE STYLES
   ======================================== */
{poc_css}
</style>"""

    import re
    html_content = re.sub(r'<link rel="stylesheet"[^>]*href="styles/main\.css"[^>]*/?>', '', html_content)
    html_content = re.sub(r'<link rel="stylesheet"[^>]*href="styles/print\.css"[^>]*/?>', '', html_content)
    html_content = re.sub(r'<link rel="stylesheet"[^>]*href="styles/print_docraptor\.css"[^>]*/?>', '', html_content)
    html_content = re.sub(r'<link rel="stylesheet"[^>]*href="styles/dual_score_POC\.css"[^>]*/?>', '', html_content)
    html_content = html_content.replace('</head>', f'{inline_styles}\n</head>')
    return html_content

def generate_pdf_docraptor(html_content: str, output_filename: Path, test_mode: bool = True) -> None:
    """Generate PDF using DocRaptor API."""
    html_with_inline_css = inline_css_for_docraptor(html_content)
    renderer = DocRaptorPDF(api_key=DOCRAPTOR_API_KEY)
    renderer.render_html_to_pdf(html_with_inline_css, output_filename, test_mode=test_mode)


def main():
    print_header()

    parser = argparse.ArgumentParser(description='POC: Dual Score Risk Assessment Report Generator')
    parser.add_argument('--input', required=True, help='Input JSON file path')
    parser.add_argument('--auto', action='store_true', help='Use defaults (no interactive prompts)')
    parser.add_argument('--engine', default='docraptor', choices=['docraptor', 'playwright', 'weasyprint'], help='PDF engine')
    parser.add_argument('--output', help='Custom output filename')
    parser.add_argument('--production', action='store_true', help='Generate production PDF (no watermark)')

    args = parser.parse_args()

    # Resolve input path
    input_file = Path(args.input)
    if not input_file.is_absolute():
        input_file = p(args.input)

    if not input_file.exists():
        print_error(f"Input file not found: {input_file}")
        return 1

    # Load data
    print_info(f"Loading {input_file.name}...")
    crm_data = load_json_file(input_file)
    if not crm_data:
        print_error("Failed to load CRM data")
        return 1

    print_success(f"Loaded {len(crm_data)} questions")

    # Load mappings
    question_mapping = load_json_file(p('mappings', 'question_mapping.json'))
    category_mapping = load_json_file(p('mappings', 'category_mapping.json'))

    # Assessment metadata
    metadata = {
        'member_name': 'Sample Organization - POC',
        'assessment_date': datetime.now().strftime('%m/%d/%Y'),
        'conducted_by': 'CyberPools Assessment Team',
        'member_contact': 'Contact Person',
        'version': input_file.stem
    }

    # Executive summary
    executive_summary = "This is a Proof of Concept report demonstrating the new **dual-score model** for CyberPools Risk Assessments. The report now shows both a **Foundation Score** (based on core cyber insurance requirements) and a **Security Maturity Score** (based on comprehensive assessment)."
    executive_summary = convert_freeform_text(executive_summary, use_markdown=True)

    # Transform data
    template_data = transform_crm_data(
        crm_data,
        metadata,
        executive_summary,
        question_mapping,
        category_mapping
    )

    # Load boilerplate
    print_info("Loading boilerplate content...")
    boilerplate = load_json_file(p('content', 'boilerplate.json'))
    if not boilerplate:
        print_error("Could not load content/boilerplate.json")
        return 1

    # Update category descriptions from boilerplate
    for category in template_data['categories']:
        cat_num = category['number']
        if cat_num in (boilerplate.get('categories') or {}):
            category['overview'] = boilerplate['categories'][cat_num]['overview']
            category['importance'] = boilerplate['categories'][cat_num]['importance']

    # Build complete context for template
    context = {
        **template_data,
        'boilerplate': boilerplate,
        'has_high_risk': True,  # Include findings for POC
        'has_moderate_risk': True,
        'selected_risk_levels': ['high', 'moderate'],
        'findings': {'high': [], 'moderate': [], 'low': []},  # Empty for POC
        'executive_summary_raw': executive_summary,
        'executive_summary_html': executive_summary,
        'executive_summary_is_markdown': True,
        'report_date': datetime.now().strftime('%m/%d/%Y')
    }

    # Render HTML
    print_info("Rendering HTML template...")
    html_content = render_html(context)

    # Generate output filename
    if args.output:
        output_filename = Path(args.output)
        if not output_filename.is_absolute():
            output_filename = p(args.output)
    else:
        output_filename = p('output', f'POC_Dual_Score_{input_file.stem}.pdf')

    # Ensure output directory exists
    output_filename.parent.mkdir(parents=True, exist_ok=True)

    # Generate PDF
    print_info(f"Generating PDF using {args.engine}...")

    if args.engine == 'docraptor':
        test_mode = not args.production
        generate_pdf_docraptor(html_content, output_filename, test_mode=test_mode)
    else:
        print_error(f"For POC, only docraptor engine is configured. Please use --engine docraptor")
        return 1

    print_success(f"POC Report generated: {output_filename}")
    print_info("\nPOC Features Demonstrated:")
    print_info("  - Foundation Score (Cyber Requirements)")
    print_info("  - Security Maturity Score (Full Assessment)")
    print_info("  - Dual score display in executive summary")
    print_info("  - Foundation requirements breakdown")

    return 0


if __name__ == '__main__':
    sys.exit(main())
