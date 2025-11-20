#!/usr/bin/env python3
"""
CyberPools Risk Assessment Report Generator - Interactive Version

- Preserves original CLI:
    python3 scripts/transform_and_generate.py --input input/cb-ra.json --auto
- Flags:
    --input <path>        Raw CRM JSON (relative to project root unless absolute)
    --auto                 Use defaults (no interactive prompts)
    --engine               playwright | weasyprint  (default: playwright)
    --ci                   Add Chromium --no-sandbox/--disable-dev-shm-usage

- Robust path handling: works from project root OR inside scripts/.
- Leaves data model, mappings, and scoring formula unchanged.
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
    print(f"{Colors.BOLD}CyberPools Risk Assessment Report Generator{Colors.END}")
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

def get_input_files():
    input_dir = p('input')
    if not input_dir.exists():
        print_error("Input directory not found. Creating it...")
        input_dir.mkdir(parents=True)
        return []
    return list(input_dir.glob('*.json'))

def select_input_file():
    files = get_input_files()
    if not files:
        print_error("No JSON files found in input/ directory")
        print_info("Please place your CRM export JSON file in the input/ folder")
        sys.exit(1)

    print(f"{Colors.BOLD}Available input files:{Colors.END}")
    for i, file in enumerate(files, 1):
        print(f"  {i}. {file.name}")

    while True:
        try:
            choice = input(f"\nSelect input file (1-{len(files)}): ").strip()
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                return files[idx]
            print_error(f"Please enter a number between 1 and {len(files)}")
        except ValueError:
            print_error("Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\nCancelled by user")
            sys.exit(0)


# ---------- Prompts ----------
def get_multiline_input(prompt):
    print(f"\n{Colors.BOLD}{prompt}{Colors.END}")
    print("Enter text (press Enter twice when done, or Enter once to skip):\n")

    lines, empty = [], 0
    try:
        while True:
            line = input("> ")
            if not line:
                empty += 1
                if empty >= 2:
                    break
                if not lines:
                    # First blank line with no content means skip
                    break
                # Preserve intentional blank lines between paragraphs
                lines.append('')
            else:
                empty = 0
                lines.append(line)
        return '\n'.join(lines).strip()
    except KeyboardInterrupt:
        print("\n\nCancelled by user")
        sys.exit(0)

def prompt_yes_no(prompt_text: str, default: bool = True) -> bool:
    default_label = "Y/n" if default else "y/N"
    while True:
        try:
            resp = input(f"{prompt_text} ({default_label}): ").strip().lower()
        except KeyboardInterrupt:
            print("\n\nCancelled by user")
            sys.exit(0)

        if not resp:
            return default
        if resp in {'y', 'yes'}:
            return True
        if resp in {'n', 'no'}:
            return False
        print_error("Please enter Y or N.")

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

def get_assessment_metadata(auto_mode=False):
    print(f"\n{Colors.BOLD}Assessment Information{Colors.END}\n")
    if auto_mode:
        return {
            'member_name': 'Sample Organization',
            'assessment_date': datetime.now().strftime('%m/%d/%Y'),
            'conducted_by': 'Assessment Team',
            'member_contact': 'Contact Person'
        }
    try:
        member_name = input("Member Name: ").strip() or "Unknown Organization"
        assessment_date = input(f"Assessment Date [{datetime.now().strftime('%m/%d/%Y')}]: ").strip() or datetime.now().strftime('%m/%d/%Y')
        conducted_by = input("Conducted By: ").strip() or "Unknown"
        member_contact = input("Member Contact: ").strip() or "Unknown"
        return {
            'member_name': member_name,
            'assessment_date': assessment_date,
            'conducted_by': conducted_by,
            'member_contact': member_contact
        }
    except KeyboardInterrupt:
        print("\n\nCancelled by user")
        sys.exit(0)

def get_executive_summary(auto_mode=False):
    if auto_mode:
        return "", False
    use_markdown = prompt_yes_no("Format executive summary using Markdown?", default=True)
    summary = get_multiline_input("📝 Executive Summary")
    if summary and len(summary) < 100:
        print_info("Note: Executive summary is quite short (< 100 characters)")
        print_info("Consider adding more detail for a better report")
    return summary, use_markdown


# ---------- Scoring helpers (unchanged logic) ----------
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


# ---------- Transform (unchanged layout) ----------
EXCLUDED_CYBER_REQUIREMENTS = {
    "b032c58a-fc8f-f011-b4cb-0022480aaebb",  # Cyber insurance participation (informational only)
}
def transform_crm_data(crm_questions, metadata_input, executive_summary, question_mapping, category_mapping, include_compliance=True):
    print_info("Transforming CRM data to template format...")

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

    overall_score = calculate_overall_score(crm_questions, question_mapping)
    grade = 'A' if overall_score >= 90 else 'B' if overall_score >= 80 else 'C' if overall_score >= 70 else 'D' if overall_score >= 60 else 'F'

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
            'overall_score': int(overall_score),
            'overall_grade': grade,
            'section_scores': section_scores,
            'risk_distribution': risk_dist
        },
        'cyber_requirements': cyber_requirements,
        'categories': categories
    }


# ---------- Render + PDF ----------
def render_html(context: dict) -> str:
    env = Environment(
        loader=FileSystemLoader(p('templates')),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )
    tpl = env.get_template('main_template.html')
    return tpl.render(context)

def generate_pdf_weasyprint(html_content: str, output_filename: Path) -> None:
    HTML, CSS = _import_weasyprint()
    css_files = [CSS(filename=str(p('styles', 'main.css'))), CSS(filename=str(p('styles', 'print.css')))]
    HTML(string=html_content, base_url=str(PROJECT_ROOT)).write_pdf(str(output_filename), stylesheets=css_files)

def generate_pdf_playwright(html_content: str, output_filename: Path, ci_mode: bool) -> None:
    renderer = PlaywrightPDF(
        page_format="Letter",
        prefer_css_page_size=True,
        print_background=True,
        no_sandbox=ci_mode,
        chromium_args=["--font-render-hinting=none"],
        display_header_footer=False,
    )
    renderer.render_html_to_pdf(html_content, output_filename, assets_dir=PROJECT_ROOT)

def inline_css_for_docraptor(html_content: str) -> str:
    """Inline CSS files into HTML for DocRaptor."""
    main_css = p('styles', 'main.css').read_text(encoding='utf-8')
    print_css = p('styles', 'print_docraptor.css').read_text(encoding='utf-8')

    # Combine into ONE style block - print CSS comes LAST to override
    inline_styles = f"""<style>
{main_css}

/* ========================================
   DOCRAPTOR PRINT OVERRIDES
   ======================================== */
{print_css}
</style>"""

    import re
    html_content = re.sub(r'<link rel="stylesheet"[^>]*href="styles/main\.css"[^>]*/?>', '', html_content)
    html_content = re.sub(r'<link rel="stylesheet"[^>]*href="styles/print\.css"[^>]*/?>', '', html_content)
    html_content = re.sub(r'<link rel="stylesheet"[^>]*href="styles/print_docraptor\.css"[^>]*/?>', '', html_content)
    html_content = html_content.replace('</head>', f'{inline_styles}\n</head>')
    return html_content

def generate_pdf_docraptor(html_content: str, output_filename: Path, test_mode: bool = True) -> None:
    """Generate PDF using DocRaptor API."""
    html_with_inline_css = inline_css_for_docraptor(html_content)
    renderer = DocRaptorPDF(api_key=DOCRAPTOR_API_KEY)
    renderer.render_html_to_pdf(html_with_inline_css, output_filename, test_mode=test_mode)

def collect_findings_by_risk(template_data: dict) -> dict:
    """Collect all findings grouped by risk level."""
    findings = {'high': [], 'moderate': [], 'low': []}

    for cat in template_data['categories']:
        for q in cat['questions']:
            finding = {
                'category': cat['name'],
                'question_number': q['number'],
                'question_text': q['text'],
                'risk_score': q['risk_score'],
                'risk_level': q['risk_level'],
                'control_status': q['control_status'],
                'control_status_text': q['control_status_text'],
                'impact_score': q['impact_score'],
                'comments': q['comments']
            }
            findings[q['risk_level']].append(finding)

    return findings

def display_findings_preview(findings: dict, risk_levels: list):
    """Display findings for user review."""
    print(f"\n{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}Findings Preview{Colors.END}")
    print(f"{Colors.BOLD}{'='*70}{Colors.END}\n")

    for level in risk_levels:
        if level == 'high':
            color = Colors.RED
            label = "HIGH RISK"
        elif level == 'moderate':
            color = Colors.YELLOW
            label = "MODERATE RISK"
        else:
            color = Colors.GREEN
            label = "LOW RISK"

        findings_list = findings.get(level, [])
        if findings_list:
            print(f"{color}{Colors.BOLD}{label} FINDINGS ({len(findings_list)}){Colors.END}")
            print("-" * 70)
            for i, f in enumerate(findings_list, 1):
                print(f"{i}. {Colors.BOLD}{f['question_number']}{Colors.END} - {f['question_text']}")
                print(f"   Category: {f['category']}")
                print(f"   Status: {f['control_status_text']} | Risk Score: {f['risk_score']}")
                if f['comments']:
                    print(f"   Comments: {f['comments']}")
                print()
        else:
            print(f"{color}{Colors.BOLD}{label} FINDINGS (0){Colors.END}")
            print(f"✓ No {level} risk findings\n")

def get_findings_display_preference(findings: dict, auto_mode: bool):
    """Ask user which risk levels to include in findings section."""
    if auto_mode:
        # In auto mode, include high and moderate by default
        return ['high', 'moderate']

    high_count = len(findings.get('high', []))
    moderate_count = len(findings.get('moderate', []))
    low_count = len(findings.get('low', []))

    print(f"\n{Colors.BOLD}📊 Findings Summary:{Colors.END}")
    print(f"  {Colors.RED}• High Risk:{Colors.END} {high_count}")
    print(f"  {Colors.YELLOW}• Moderate Risk:{Colors.END} {moderate_count}")
    print(f"  {Colors.GREEN}• Low Risk:{Colors.END} {low_count}\n")

    print(f"{Colors.BOLD}Which risk levels would you like to display in the Findings section?{Colors.END}")
    print("1. High risk only")
    print("2. High + Moderate risk")
    print("3. All findings (High + Moderate + Low)")
    print("4. Preview findings before deciding")

    while True:
        choice = input(f"\n{Colors.BOLD}Enter choice (1-4) [default: 2]:{Colors.END} ").strip()
        if not choice:
            choice = '2'

        if choice == '1':
            return ['high']
        elif choice == '2':
            return ['high', 'moderate']
        elif choice == '3':
            return ['high', 'moderate', 'low']
        elif choice == '4':
            display_findings_preview(findings, ['high', 'moderate', 'low'])
            continue
        else:
            print(f"{Colors.RED}Invalid choice. Please enter 1, 2, 3, or 4{Colors.END}")

def generate_pdf_report(template_data: dict, output_filename: Path, engine: str, ci_mode: bool, auto_mode: bool, exec_use_markdown: bool, docraptor_test_mode: bool = True) -> bool:
    print_info("Loading boilerplate content...")
    boilerplate = load_json_file(p('content', 'boilerplate.json'))
    if not boilerplate:
        print_error("Could not load content/boilerplate.json")
        return False

    for category in template_data['categories']:
        cat_num = category['number']
        if cat_num in (boilerplate.get('categories') or {}):
            category['overview'] = boilerplate['categories'][cat_num]['overview']
            category['importance'] = boilerplate['categories'][cat_num]['importance']

    # Collect all findings by risk level
    findings = collect_findings_by_risk(template_data)

    # Get user preference for which findings to display
    selected_risk_levels = get_findings_display_preference(findings, auto_mode)
    # Normalize + preserve order
    risk_level_order = ['high', 'moderate', 'low']
    selected_risk_levels = [level for level in risk_level_order if level in selected_risk_levels]

    # Filter findings down to selected levels while keeping predictable keys
    filtered_findings = {
        level: findings.get(level, []) if level in selected_risk_levels else []
        for level in risk_level_order
    }

    executive_summary_raw = template_data.get('executive_summary', '')
    executive_summary_html = convert_freeform_text(executive_summary_raw, exec_use_markdown)
    cover_logo_data_uri = get_logo_data_uri()

    # Display preview of selected findings
    if not auto_mode:
        print(f"\n{Colors.GREEN}✓ Selected risk levels: {', '.join(level.upper() for level in selected_risk_levels)}{Colors.END}")
        display_findings_preview(filtered_findings, selected_risk_levels)

        confirm = input(f"\n{Colors.BOLD}Proceed with PDF generation? (Y/n):{Colors.END} ").strip().lower()
        if confirm and confirm != 'y':
            print_info("PDF generation cancelled")
            return False

    # Determine has_high_risk flag for template
    has_high_risk = 'high' in selected_risk_levels and len(filtered_findings.get('high', [])) > 0
    has_moderate_risk = 'moderate' in selected_risk_levels and len(filtered_findings.get('moderate', [])) > 0

    context = {
        **template_data,
        'boilerplate': boilerplate,
        'has_high_risk': has_high_risk,
        'has_moderate_risk': has_moderate_risk,
        'selected_risk_levels': selected_risk_levels,
        'findings': filtered_findings,
        'executive_summary_raw': executive_summary_raw,
        'executive_summary_html': executive_summary_html,
        'executive_summary_is_markdown': exec_use_markdown and MARKDOWN_AVAILABLE,
        'report_date': datetime.now().strftime('%m/%d/%Y'),
        'cover_logo_data_uri': cover_logo_data_uri
    }

    print_info("Rendering HTML template...")
    html_content = render_html(context)

    print_info(f"Converting to PDF via {engine}...")
    if engine == "weasyprint":
        generate_pdf_weasyprint(html_content, output_filename)
    elif engine == "docraptor":
        mode_msg = "production (no watermark)" if not docraptor_test_mode else "test (watermarked, free)"
        print_info(f"DocRaptor mode: {mode_msg}")
        generate_pdf_docraptor(html_content, output_filename, test_mode=docraptor_test_mode)
    else:
        generate_pdf_playwright(html_content, output_filename, ci_mode)
    return True


# ---------- Main ----------
def parse_args():
    parser = argparse.ArgumentParser(description='Generate Risk Assessment Reports')
    parser.add_argument('--input', help='Input JSON file path (raw CRM export)')
    parser.add_argument('--auto', action='store_true', help='Auto mode with defaults')
    parser.add_argument('--engine', choices=['playwright', 'weasyprint', 'docraptor'], default='playwright', help='PDF engine')
    parser.add_argument('--ci', action='store_true', help='Chromium no-sandbox (CI/Docker)')
    parser.add_argument('--production', action='store_true', help='DocRaptor production mode (no watermark, counts against quota)')
    parser.add_argument('--no-compliance', action='store_true', help='Skip Cyber Requirements compliance table')
    parser.add_argument('--output', help='Output PDF path (overrides default)')
    return parser.parse_args()

def main():
    print_header()
    args = parse_args()

    # Resolve input path under project root if relative
    if args.input:
        input_file = Path(args.input)
        if not input_file.is_absolute():
            input_file = p(args.input)
    else:
        input_file = select_input_file()

    if not input_file.exists():
        print_error(f"Input file not found: {input_file}")
        sys.exit(1)

    crm_data = load_json_file(input_file)
    if not crm_data:
        sys.exit(1)

    print_success(f"Loaded {len(crm_data)} questions from CRM data")

    print_info("Loading mapping files...")
    question_mapping = load_json_file(p('mappings', 'question_mapping.json')) or {}
    category_mapping = load_json_file(p('mappings', 'category_mapping.json')) or {}

    if not question_mapping or len(question_mapping) <= 1:
        print_error("Warning: question_mapping.json is empty or incomplete")
        print_info("Questions may show as 'Unknown Question' and scoring may be inaccurate")

    if not category_mapping:
        print_error("Warning: category_mapping.json is empty or missing")
        print_info("Categories will show as 'Unknown Category'")

    metadata = get_assessment_metadata(args.auto)
    metadata['version'] = input_file.stem

    executive_summary_raw, exec_use_markdown = get_executive_summary(args.auto)
    if not executive_summary_raw:
        print_info("No executive summary provided - placeholder will be used in report")
    else:
        print_success(f"Executive summary: {len(executive_summary_raw)} characters")

    try:
        include_compliance = not args.no_compliance
        template_data = transform_crm_data(
            crm_data,
            metadata,
            executive_summary_raw,
            question_mapping,
            category_mapping,
            include_compliance=include_compliance,
        )
        print_success("Data transformation complete")
        print_info(f"Overall Score: {template_data['scoring']['overall_score']}% (Grade: {template_data['scoring']['overall_grade']})")
    except Exception as e:
        print_error(f"Transformation failed: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)

    output_dir = p('output'); output_dir.mkdir(exist_ok=True)
    safe_name = metadata['member_name'].replace(' ', '_').replace('/', '_')
    date_str = metadata['assessment_date'].replace('/', '-')

    # Allow custom output path via --output flag
    if args.output:
        output_filename = Path(args.output)
        if not output_filename.is_absolute():
            output_filename = p(args.output)
    else:
        output_filename = output_dir / f"{safe_name}_Risk_Assessment_{date_str}.pdf"

    # DocRaptor test mode is the inverse of production flag
    docraptor_test_mode = not args.production

    print_info(f"Generating PDF: {output_filename}")
    try:
        if generate_pdf_report(template_data, output_filename, args.engine, args.ci, args.auto, exec_use_markdown, docraptor_test_mode):
            print_success(f"Report saved to: {output_filename}")
            print(f"\n{Colors.BOLD}✨ Done! Open the PDF to review.{Colors.END}\n")
        else:
            print_error("PDF generation failed")
            sys.exit(1)
    except Exception as e:
        print_error(f"PDF generation failed: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
