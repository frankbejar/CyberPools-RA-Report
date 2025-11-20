#!/usr/bin/env python3
"""
Grading Simulation: Compare Old vs New (60/40 Weighted) Grading
"""
import json
import sys
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP

# Path setup
THIS_FILE = Path(__file__).resolve()
SCRIPTS_DIR = THIS_FILE.parent
PROJECT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

COMPLIANCE_QUESTION_NUMBERS = {
    '1.4', '2.3', '2.4', '2.5', '2.6', '4.3', '4.7', '5.4', '6.3', '6.4', '7.2', '7.3'
}

EXCLUDED_CYBER_REQUIREMENTS = {
    "b032c58a-fc8f-f011-b4cb-0022480aaebb",  # Cyber insurance participation
}

def calculate_overall_score(questions, question_mapping):
    """Calculate overall score using standard formula."""
    applicable = [q for q in questions if q['qResponse'] != 0]
    if not applicable:
        return 100

    actual = sum(q['qScore'] for q in applicable)
    min_score = sum((question_mapping.get(q['qID'], {}).get('impact_score', 3) * 1) for q in applicable)
    max_score = sum((question_mapping.get(q['qID'], {}).get('impact_score', 3) * 5) for q in applicable)

    if max_score == min_score:
        return 100

    final = (1 - (actual - min_score) / (max_score - min_score)) * 100
    return int(Decimal(final).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

def calculate_foundation_score(questions, question_mapping):
    """Calculate score based on foundation questions only."""
    foundation_qs = []
    for q in questions:
        if q['qID'] in EXCLUDED_CYBER_REQUIREMENTS:
            continue
        q_info = question_mapping.get(q['qID'], {})
        q_number = q_info.get('number', '0.0')
        include_requirement = q.get('qReq', False) or q_number in COMPLIANCE_QUESTION_NUMBERS
        if include_requirement:
            foundation_qs.append(q)

    applicable = [q for q in foundation_qs if q['qResponse'] != 0]

    if not applicable:
        return 100

    return calculate_overall_score(applicable, question_mapping)

def get_grade(score):
    """Convert numeric score to letter grade."""
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

def simulate_grading(json_file, question_mapping):
    """Simulate both old and new grading methods."""
    with open(json_file) as f:
        questions = json.load(f)

    # Old Method: Comprehensive score only
    old_score = calculate_overall_score(questions, question_mapping)
    old_grade = get_grade(old_score)

    # New Method: 60% Foundation + 40% Comprehensive
    foundation_score = calculate_foundation_score(questions, question_mapping)
    comprehensive_score = calculate_overall_score(questions, question_mapping)
    new_score = int(foundation_score * 0.6 + comprehensive_score * 0.4)
    new_grade = get_grade(new_score)

    member_name = json_file.stem.replace('CBS-', '')

    return {
        'member': member_name,
        'old_score': old_score,
        'old_grade': old_grade,
        'foundation_score': foundation_score,
        'comprehensive_score': comprehensive_score,
        'new_score': new_score,
        'new_grade': new_grade,
        'score_change': new_score - old_score,
        'grade_change': old_grade != new_grade
    }

def main():
    # Load question mapping
    mapping_file = PROJECT_ROOT / 'mappings' / 'question_mapping.json'
    with open(mapping_file) as f:
        question_mapping = json.load(f)

    # Find all JSON files
    input_dir = PROJECT_ROOT / 'input'
    json_files = sorted(input_dir.glob('CBS-*.json'))

    print("=" * 100)
    print("GRADING SIMULATION: Old Method vs New Method (60/40 Weighted)")
    print("=" * 100)
    print()

    results = []
    for json_file in json_files:
        result = simulate_grading(json_file, question_mapping)
        results.append(result)

    # Print table header
    print(f"{'Member':<30} {'Old':<15} {'Foundation':<12} {'Comprehensive':<15} {'New (60/40)':<15} {'Change':<10}")
    print(f"{'':<30} {'Score/Grade':<15} {'Score':<12} {'Score':<15} {'Score/Grade':<15} {'+/-':<10}")
    print("-" * 100)

    # Print results
    for r in results:
        old = f"{r['old_score']}% ({r['old_grade']})"
        new = f"{r['new_score']}% ({r['new_grade']})"
        change = f"{r['score_change']:+d}%"
        if r['grade_change']:
            change += " ⚠️"

        print(f"{r['member']:<30} {old:<15} {r['foundation_score']:>3}%{'':<8} {r['comprehensive_score']:>3}%{'':<11} {new:<15} {change:<10}")

    print()
    print("Summary:")
    print(f"  - Total members simulated: {len(results)}")
    print(f"  - Grade changes: {sum(1 for r in results if r['grade_change'])}")
    print(f"  - Average score change: {sum(r['score_change'] for r in results) / len(results):.1f}%")
    print()
    print("Notes:")
    print("  - Old Method: Score based on all 51 questions equally weighted")
    print("  - New Method: 60% Foundation (12 questions) + 40% Comprehensive (51 questions)")
    print("  - ⚠️  indicates a grade letter change")
    print()

if __name__ == '__main__':
    main()
