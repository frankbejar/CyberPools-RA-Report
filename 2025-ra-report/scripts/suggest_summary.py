#!/usr/bin/env python3
"""
CyberPools AI Executive Summary Generator

Analyzes risk assessment JSON data and generates executive summary suggestions
using OpenAI GPT-3.5 Turbo, with support for multiple tones and interactive review.

Usage:
    python3 scripts/suggest_summary.py --input input/CBS-CBS.json
    python3 scripts/suggest_summary.py --input input/CBS-CBS.json --tone executive
    python3 scripts/suggest_summary.py --batch
    python3 scripts/suggest_summary.py --input input/CBS-CBS.json --dry-run
"""

import json
import sys
import argparse
import os
import subprocess
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️  Warning: python-dotenv not installed. Using environment variables only.")

# OpenAI import
try:
    from openai import OpenAI
except ImportError:
    print("❌ Error: openai package not installed.")
    print("   Install with: pip install openai python-dotenv pyperclip")
    sys.exit(1)

# Clipboard support
try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False
    print("ℹ️  Note: pyperclip not installed. Clipboard features disabled.")
    print("   Install with: pip install pyperclip")


# =============================================================================
# TONE DEFINITIONS
# =============================================================================

TONES = {
    "professional": {
        "name": "Professional (Risk-Focused)",
        "description": "Professional cybersecurity risk partner tone - balanced, specific, actionable",
        "system_instructions": """You are a professional cybersecurity risk analyst for CyberPools,
writing executive summaries for cyber insurance and risk assessment partners. Your tone is:
- Professional and authoritative, not alarmist
- Risk-oriented but balanced and constructive
- Uplifting for strengths, transparent about gaps
- Specific and actionable, not generic
- Technical enough to be credible, accessible enough for executives"""
    },
    "executive": {
        "name": "Executive (Board-Level)",
        "description": "Higher-level, less technical, board-friendly",
        "system_instructions": """You are writing for C-suite executives and board members.
Your tone is:
- Strategic and business-focused
- Less technical jargon, more business impact
- Concise and high-level
- Focus on risk exposure and business continuity"""
    },
    "technical": {
        "name": "Technical (IT-Focused)",
        "description": "Detailed technical analysis for IT teams",
        "system_instructions": """You are writing for IT and security professionals.
Your tone is:
- Technically detailed and specific
- Include control frameworks, technologies, protocols
- Granular findings and remediation steps
- Use industry-standard terminology"""
    },
    "concise": {
        "name": "Concise (Brief Summary)",
        "description": "Short, bullet-focused summary",
        "system_instructions": """Provide a brief, high-impact summary.
Your tone is:
- Extremely concise, every word counts
- Bullet-point friendly structure
- Lead with the score and key takeaway
- Maximum 3 short paragraphs"""
    }
}

DEFAULT_TONE = "professional"


# =============================================================================
# EXAMPLE SUMMARIES (Few-Shot Learning)
# =============================================================================

EXAMPLE_SUMMARIES = """
EXAMPLE 1 (Score: 96%, Grade A):
**Christian Brothers Services** demonstrates an **exceptionally mature cybersecurity program** with an overall risk score of **96%** – among the highest scores recorded in CyberPools assessments.

The organization achieved perfect **100% scores** in six of nine control categories, including **Account Management**, **Data Protection**, **Security Awareness**, and **Incident Response Management**, with **zero high-risk findings** identified.

Notable strengths include **comprehensive multi-factor authentication** across all systems and privileged accounts, **robust patch management** using PDQ and Intune, **advanced endpoint protection** through **SentinelOne EDR/MDR** with **24/7 SOC support**, monthly phishing simulations and security awareness training, **encrypted and immutable backups** with off-site management, and a sophisticated **vendor management program** using OneTrust.

The organization has established a **well-documented Cyber Incident Response Plan** and conducts regular **tabletop exercises** for both staff and executives, demonstrating a proactive security culture.

Only **two moderate-risk findings** were identified, both representing minor enhancement opportunities rather than critical vulnerabilities: implementing dedicated DNS filtering to complement existing Cato firewall protections, and formalizing a bi-annual internal backup recovery testing schedule to supplement the vendor's monthly restoration testing.

Overall, the assessment reveals a **strategically architected, well-managed security program** with **enterprise-level controls** that significantly exceed baseline expectations, with focused areas for incremental enhancement.

---

EXAMPLE 2 (Score: 82%, Grade B):
**Santa Catalina School** achieved an overall cyber risk score of **82%**, reflecting a **strong cybersecurity foundation** with effective controls in **asset management**, **multi-factor authentication**, **vendor oversight**, and **staff awareness**.

The school demonstrates **mature practices** through **comprehensive MFA enforcement**, **air-gapped backups**, and **regular security training**, but key vulnerabilities remain in **Incident Response** and **Endpoint Security**.

Specifically, the absence of a formal **Cyber Incident Response Plan (CIRP)**, lack of **Endpoint Detection and Response (EDR)**, and limited **endpoint encryption** present elevated risks to timely detection and recovery.

Strengthening these areas by implementing a **CIRP**, deploying **EDR**, **encrypting devices** and establishing a **backup validation process** will significantly enhance the school's readiness and resilience against modern cyber threats.

---

EXAMPLE 3 (Score: 80%, Grade B):
**Rosary College Prep** demonstrates a **developing cybersecurity posture**, achieving an overall **risk score of 80** with **three high-risk findings**. These high-risk areas include the absence of encryption on endpoints, backups, and servers; lack of **multi-factor authentication (MFA)** for remote access; and no **endpoint detection and response (EDR)** solutions in place.

The assessment also identified **five moderate-risk findings** which present opportunities for continued improvement. These include implementing **802.1x network authentication**, formalizing a **vendor vetting process**, and developing a **comprehensive cyber incident response plan** (templates can be provided).

Notably, the organization performed exceptionally well in the **Secure Configuration of Enterprise Assets** and **Data Recovery** categories, reflecting mature processes in asset configuration management and reliable **backup and restoration practices**.

Overall, **Rosary College Prep** has established **foundational cybersecurity controls** but requires focused remediation of high-risk gaps — particularly **MFA**, **encryption**, and **EDR** — to achieve a mature security posture aligned with baseline best practices.
"""


# =============================================================================
# DATA ANALYSIS
# =============================================================================

def load_json(file_path):
    """Load assessment JSON file"""
    with open(file_path, 'r') as f:
        return json.load(f)


def load_mappings(project_root):
    """Load question and category mappings"""
    question_mapping_path = project_root / 'mappings' / 'question_mapping.json'
    category_mapping_path = project_root / 'mappings' / 'category_mapping.json'

    with open(question_mapping_path, 'r') as f:
        question_mapping = json.load(f)
    with open(category_mapping_path, 'r') as f:
        category_mapping = json.load(f)

    return question_mapping, category_mapping


def calculate_score(questions, question_mapping):
    """Calculate overall score using the same formula as report generator"""
    total_score = 0
    min_possible = 0
    max_possible = 0

    for q in questions:
        q_id = q['qID']
        response = q['qResponse']

        if q_id not in question_mapping:
            continue

        impact = question_mapping[q_id].get('impact_score', 1)

        # Risk score = response * impact
        risk_score = response * impact
        total_score += risk_score

        # Min/max calculations
        min_possible += 1 * impact  # Best case: response = 1
        max_possible += 5 * impact  # Worst case: response = 5

    # Convert to percentage (inverse - lower risk = higher score)
    if max_possible > min_possible:
        percentage = (1 - (total_score - min_possible) / (max_possible - min_possible)) * 100
    else:
        percentage = 100

    # Calculate grade
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'

    percentage = Decimal(percentage).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return int(percentage), grade


def analyze_assessment(json_data, question_mapping, category_mapping):
    """Extract comprehensive metrics from assessment data"""

    # Calculate overall score
    overall_score, grade = calculate_score(json_data, question_mapping)

    # Analyze findings by risk level
    findings = {'high': [], 'moderate': [], 'low': []}
    technologies = set()
    perfect_categories = []
    weak_categories = []
    category_scores = {}

    # Group by category
    by_category = {}
    for q in json_data:
        cat = q['qCat']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(q)

    # Analyze each category
    for cat_id, cat_questions in by_category.items():
        cat_name = category_mapping.get(str(cat_id), {}).get('name', f'Category {cat_id}')

        # Calculate category score
        cat_score, cat_grade = calculate_score(cat_questions, question_mapping)
        category_scores[cat_name] = {'score': cat_score, 'grade': cat_grade}

        if cat_score == 100:
            perfect_categories.append(cat_name)
        elif cat_score < 70:
            weak_categories.append(cat_name)

        # Analyze questions
        for q in cat_questions:
            q_id = q['qID']
            if q_id not in question_mapping:
                continue

            q_info = question_mapping[q_id]
            response = q['qResponse']
            impact = q_info.get('impact_score', 1)
            risk_score = response * impact

            # Categorize by risk level
            if risk_score >= 16:
                level = 'high'
            elif risk_score >= 10:
                level = 'moderate'
            else:
                level = 'low'

            finding = {
                'category': cat_name,
                'number': q_info.get('number', ''),
                'text': q_info.get('text', ''),
                'notes': q.get('qNotes', ''),
                'risk_score': risk_score,
                'response': response
            }

            findings[level].append(finding)

            # Extract technologies from notes
            notes = q.get('qNotes', '').lower()
            tech_keywords = ['edr', 'mdr', 'mfa', 'sentinel', 'crowdstrike', 'okta',
                            'duo', 'knowbe4', 'veeam', 'acronis', 'palo alto',
                            'meraki', 'cisco', 'fortinet', 'sophos', 'webroot',
                            'intune', 'pdq', 'onetrust', 'google', 'microsoft']
            for tech in tech_keywords:
                if tech in notes:
                    technologies.add(tech.title())

    # Extract key strengths and gaps
    strengths = []
    gaps = []

    # Identify strengths (fully implemented controls)
    for q in json_data:
        if q['qResponse'] == 1 and q['qID'] in question_mapping:  # Fully implemented
            q_info = question_mapping[q['qID']]
            if q_info.get('impact_score', 1) >= 3:  # High impact controls
                note = q.get('qNotes', '').strip()
                if note and len(note) > 10:
                    strengths.append(note)

    # Identify gaps (high and moderate risk)
    for finding in findings['high'] + findings['moderate'][:3]:  # Top moderate risks
        gaps.append(f"{finding['number']} - {finding['text']}")

    return {
        'overall_score': overall_score,
        'grade': grade,
        'high_risk_count': len(findings['high']),
        'moderate_risk_count': len(findings['moderate']),
        'low_risk_count': len(findings['low']),
        'findings': findings,
        'perfect_categories': perfect_categories,
        'weak_categories': weak_categories,
        'category_scores': category_scores,
        'technologies': sorted(list(technologies)),
        'strengths': strengths[:5],  # Top 5
        'gaps': gaps[:5],  # Top 5
        'total_questions': len(json_data)
    }


# =============================================================================
# OPENAI INTEGRATION
# =============================================================================

def build_prompt(member_name, analysis, tone="professional", include_key_points=True):
    """Build the OpenAI prompt with analysis data"""

    tone_config = TONES.get(tone, TONES[DEFAULT_TONE])

    # Build findings summary
    findings_text = f"""
HIGH-RISK FINDINGS ({analysis['high_risk_count']}):
{chr(10).join(['- ' + f"{f['number']}: {f['text']}" for f in analysis['findings']['high'][:5]])}

MODERATE-RISK FINDINGS ({analysis['moderate_risk_count']}):
{chr(10).join(['- ' + f"{f['number']}: {f['text']}" for f in analysis['findings']['moderate'][:5]])}
"""

    # Build strengths summary
    strengths_text = "\n".join(['- ' + s[:200] for s in analysis['strengths']]) if analysis['strengths'] else "See detailed assessment"

    output_format = """
OUTPUT FORMAT:
Provide two sections:

1. EXECUTIVE SUMMARY (prose):
   - 4-6 well-structured paragraphs
   - Use **bold markdown** for: member name, scores, grades, percentages, category names,
     technology names, control acronyms (MFA, EDR, CIRP, etc.)
   - Professional, risk-focused language
   - Specific and actionable

2. KEY POINTS (bullets):
   - 5-8 concise bullet points
   - Highlight the most critical takeaways
   - Mix of scores, strengths, and priority gaps
"""

    prompt = f"""
{tone_config['system_instructions']}

STYLE EXAMPLES (learn from these):
{EXAMPLE_SUMMARIES}

---

ASSESSMENT DATA FOR: {member_name}

OVERALL METRICS:
- Score: {analysis['overall_score']}% (Grade: {analysis['grade']})
- Total Questions: {analysis['total_questions']}
- High-risk findings: {analysis['high_risk_count']}
- Moderate-risk findings: {analysis['moderate_risk_count']}
- Low-risk findings: {analysis['low_risk_count']}

PERFECT SCORE CATEGORIES ({len(analysis['perfect_categories'])}):
{chr(10).join(['- ' + cat for cat in analysis['perfect_categories']])}

WEAK CATEGORIES:
{chr(10).join(['- ' + cat for cat in analysis['weak_categories']])}

{findings_text}

KEY STRENGTHS OBSERVED:
{strengths_text}

TECHNOLOGIES MENTIONED:
{', '.join(analysis['technologies'])}

---

{output_format}

Generate the executive summary and key points now.
"""

    return prompt


def call_openai(prompt, api_key, dry_run=False):
    """Call OpenAI API to generate summary"""

    if dry_run:
        return {
            'summary': '[DRY RUN MODE - No API call made]',
            'key_points': '[DRY RUN MODE - No API call made]',
            'cost': 0,
            'tokens': {'input': 0, 'output': 0}
        }

    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional cybersecurity risk analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )

        content = response.choices[0].message.content

        # Parse summary and key points
        if "KEY POINTS" in content:
            parts = content.split("KEY POINTS")
            summary = parts[0].replace("EXECUTIVE SUMMARY", "").replace(":", "").strip()
            key_points = parts[1].strip()
        else:
            summary = content.strip()
            key_points = ""

        # Calculate cost (GPT-3.5 Turbo pricing as of 2024)
        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens
        cost = (input_tokens / 1000 * 0.0005) + (output_tokens / 1000 * 0.0015)

        return {
            'summary': summary,
            'key_points': key_points,
            'cost': cost,
            'tokens': {'input': input_tokens, 'output': output_tokens}
        }

    except Exception as e:
        print(f"\n❌ Error calling OpenAI API: {e}")
        return None


# =============================================================================
# USER INTERFACE
# =============================================================================

def copy_to_clipboard(text):
    """Copy text to clipboard if available"""
    if CLIPBOARD_AVAILABLE:
        try:
            pyperclip.copy(text)
            return True
        except:
            return False
    return False


def save_to_file(text, output_path):
    """Save text to file"""
    try:
        with open(output_path, 'w') as f:
            f.write(text)
        return True
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False


def display_summary(member_name, analysis, result, tone):
    """Display the generated summary with formatting"""

    print("\n" + "="*80)
    print(f"AI-GENERATED EXECUTIVE SUMMARY - {member_name}")
    print(f"Tone: {TONES[tone]['name']}")
    print(f"Score: {analysis['overall_score']}% (Grade: {analysis['grade']})")
    print("="*80)
    print()
    print(result['summary'])

    if result['key_points']:
        print()
        print("="*80)
        print("KEY POINTS:")
        print("="*80)
        print(result['key_points'])

    print()
    print("="*80)
    print(f"API Cost: ${result['cost']:.4f} | Tokens: {result['tokens']['input']} in, {result['tokens']['output']} out")
    print("="*80)


def interactive_review(member_name, analysis, result, tone, project_root, input_file):
    """Interactive review interface"""

    while True:
        print("\n📋 Actions:")
        print("  [a] Accept and copy to clipboard")
        print("  [e] Edit in text editor (nano)")
        print("  [r] Regenerate with same tone")
        print("  [t] Try different tone")
        print("  [s] Save to file")
        print("  [q] Quit without saving")

        choice = input("\nYour choice: ").lower().strip()

        if choice == 'a':
            full_text = result['summary']
            if result['key_points']:
                full_text += "\n\n" + "="*80 + "\nKEY POINTS:\n" + "="*80 + "\n" + result['key_points']

            if copy_to_clipboard(full_text):
                print("✅ Copied to clipboard!")
            else:
                print("ℹ️  Clipboard not available. Summary displayed above.")
            return result

        elif choice == 'e':
            # Save to temp file and open in editor
            temp_file = project_root / 'summaries' / f'temp_{member_name.replace(" ", "_")}.md'
            full_text = result['summary']
            if result['key_points']:
                full_text += "\n\n" + "="*80 + "\nKEY POINTS:\n" + "="*80 + "\n" + result['key_points']

            save_to_file(full_text, temp_file)
            subprocess.call(['nano', str(temp_file)])

            # Read back edited version
            with open(temp_file, 'r') as f:
                edited = f.read()

            result['summary'] = edited
            result['key_points'] = ""
            print("✅ Edits saved!")
            display_summary(member_name, analysis, result, tone)

        elif choice == 'r':
            return None  # Signal to regenerate

        elif choice == 't':
            print("\n📝 Available tones:")
            for key, config in TONES.items():
                print(f"  [{key}] {config['name']} - {config['description']}")

            new_tone = input("\nSelect tone: ").lower().strip()
            if new_tone in TONES:
                return ('change_tone', new_tone)
            else:
                print("❌ Invalid tone. Please try again.")

        elif choice == 's':
            default_filename = f"{member_name.replace(' ', '_')}_summary.md"
            filename = input(f"Filename [{default_filename}]: ").strip() or default_filename

            output_path = project_root / 'summaries' / filename
            full_text = result['summary']
            if result['key_points']:
                full_text += "\n\n" + "="*80 + "\nKEY POINTS:\n" + "="*80 + "\n" + result['key_points']

            if save_to_file(full_text, output_path):
                print(f"✅ Saved to: {output_path}")

        elif choice == 'q':
            print("👋 Exiting without saving.")
            return 'quit'

        else:
            print("❌ Invalid choice. Please try again.")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def process_assessment(input_file, tone, api_key, dry_run, project_root):
    """Process a single assessment file"""

    # Extract member name from filename
    member_name = Path(input_file).stem.replace('CBS-', '').replace('_', ' ')

    print(f"\n🔍 Analyzing: {member_name}")

    # Load data
    json_data = load_json(input_file)
    question_mapping, category_mapping = load_mappings(project_root)

    # Analyze
    analysis = analyze_assessment(json_data, question_mapping, category_mapping)

    print(f"   Overall Score: {analysis['overall_score']}% (Grade: {analysis['grade']})")
    print(f"   High-risk findings: {analysis['high_risk_count']}")
    print(f"   Moderate-risk findings: {analysis['moderate_risk_count']}")

    if dry_run:
        print("\n📝 Prompt Preview (DRY RUN MODE):")
        print("="*80)
        prompt = build_prompt(member_name, analysis, tone)
        print(prompt[:1000] + "\n... [truncated]")
        print("="*80)
        print(f"\nPrompt length: {len(prompt)} characters")
        print("Estimated tokens: ~" + str(len(prompt) // 4))
        print("Estimated cost: ~$0.02 - $0.05")
        return

    # Generate summary
    print(f"\n🤖 Generating executive summary (tone: {TONES[tone]['name']})...")

    current_tone = tone
    while True:
        prompt = build_prompt(member_name, analysis, current_tone)
        result = call_openai(prompt, api_key, dry_run=dry_run)

        if not result:
            return

        display_summary(member_name, analysis, result, current_tone)

        action = interactive_review(member_name, analysis, result, current_tone, project_root, input_file)

        if action is None:
            # Regenerate with same tone
            print("\n🔄 Regenerating...")
            continue
        elif isinstance(action, tuple) and action[0] == 'change_tone':
            # Change tone and regenerate
            current_tone = action[1]
            print(f"\n🔄 Regenerating with tone: {TONES[current_tone]['name']}...")
            continue
        elif action == 'quit':
            break
        else:
            # Accepted
            break


def main():
    parser = argparse.ArgumentParser(description="Generate AI-powered executive summaries for risk assessments")
    parser.add_argument('--input', type=str, help='Path to input JSON file')
    parser.add_argument('--tone', type=str, default=DEFAULT_TONE, choices=TONES.keys(),
                       help=f'Summary tone (default: {DEFAULT_TONE})')
    parser.add_argument('--batch', action='store_true', help='Process all JSON files in input/')
    parser.add_argument('--dry-run', action='store_true', help='Show prompt without calling API')
    parser.add_argument('--output', type=str, help='Save directly to file (non-interactive)')

    args = parser.parse_args()

    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Get API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key and not args.dry_run:
        print("❌ Error: OPENAI_API_KEY not found in environment")
        print("   Set it in .env file or export OPENAI_API_KEY='your-key-here'")
        sys.exit(1)

    print("="*80)
    print("🤖 CyberPools AI Executive Summary Generator")
    print("="*80)

    if args.batch:
        # Process all JSON files
        input_dir = project_root / 'input'
        json_files = sorted(input_dir.glob('CBS-*.json'))

        if not json_files:
            print("❌ No CBS-*.json files found in input/")
            sys.exit(1)

        print(f"\nFound {len(json_files)} assessments:")
        for i, f in enumerate(json_files, 1):
            print(f"  {i}. {f.name}")

        confirm = input(f"\nGenerate summaries for all {len(json_files)} assessments? [y/n]: ")
        if confirm.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)

        for i, json_file in enumerate(json_files, 1):
            print(f"\n{'='*80}")
            print(f"[{i}/{len(json_files)}] Processing {json_file.name}")
            print(f"{'='*80}")
            process_assessment(json_file, args.tone, api_key, args.dry_run, project_root)

    elif args.input:
        # Process single file
        input_path = Path(args.input)
        if not input_path.exists():
            # Try relative to project root
            input_path = project_root / args.input

        if not input_path.exists():
            print(f"❌ Error: File not found: {args.input}")
            sys.exit(1)

        process_assessment(input_path, args.tone, api_key, args.dry_run, project_root)

    else:
        parser.print_help()
        sys.exit(1)

    print("\n✅ Done!")


if __name__ == '__main__':
    main()
