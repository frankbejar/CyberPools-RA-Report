#!/usr/bin/env python3
"""
Generate Risk Assessment Report with custom metadata and executive summary.

Usage:
    python3 generate_report_with_metadata.py --input <json-file> \\
        --member-name "School Name" \\
        --assessment-date "MM/DD/YYYY" \\
        --conducted-by "Name" \\
        --member-contact "Contact Name" \\
        --executive-summary "Summary text..." \\
        [--production]
"""

import sys
import argparse
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / 'scripts'))

from transform_and_generate import (
    load_json_file,
    transform_crm_data,
    generate_pdf_report,
    p,
    print_success,
    print_error,
    print_info
)

def main():
    parser = argparse.ArgumentParser(description='Generate Risk Assessment Report with custom metadata')
    parser.add_argument('--input', required=True, help='Input JSON file path')
    parser.add_argument('--member-name', required=True, help='Member/School name')
    parser.add_argument('--assessment-date', required=True, help='Assessment date (MM/DD/YYYY)')
    parser.add_argument('--conducted-by', required=True, help='Name of person who conducted assessment')
    parser.add_argument('--member-contact', required=True, help='Member contact name')
    parser.add_argument('--executive-summary', default='', help='Executive summary text')
    parser.add_argument('--production', action='store_true', help='Generate production PDF (no watermark)')
    parser.add_argument('--outro-page', action='store_true', help='Include outro page with services and contact info')
    parser.add_argument('--output', help='Custom output filename (optional)')

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
        'member_name': args.member_name,
        'assessment_date': args.assessment_date,
        'conducted_by': args.conducted_by,
        'member_contact': args.member_contact,
        'version': input_file.stem
    }

    # Transform data
    print_info("Transforming CRM data...")
    template_data = transform_crm_data(
        crm_data,
        metadata,
        args.executive_summary,
        question_mapping,
        category_mapping
    )

    # Add outro page flag to template data
    template_data['include_outro'] = args.outro_page

    print_success(f"Overall Score: {template_data['scoring']['overall_score']}% (Grade: {template_data['scoring']['overall_grade']})")

    # Generate output filename
    if args.output:
        output_filename = Path(args.output)
        if not output_filename.is_absolute():
            output_filename = p(args.output)
    else:
        safe_name = args.member_name.replace(' ', '_').replace('/', '_')
        date_str = args.assessment_date.replace('/', '-')
        output_filename = p('output', f"{safe_name}_Risk_Assessment_{date_str}.pdf")

    # Generate PDF
    print_info(f"Generating PDF: {output_filename}")
    success = generate_pdf_report(
        template_data,
        output_filename,
        engine='docraptor',
        ci_mode=False,
        auto_mode=True,
        exec_use_markdown=True,
        docraptor_test_mode=not args.production
    )

    if success:
        print_success(f"Report generated successfully!")
        print_info(f"Location: {output_filename}")
        if not args.production:
            print_info("Note: Test mode - PDF will have watermark. Use --production for final version.")
        return 0
    else:
        print_error("Report generation failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
