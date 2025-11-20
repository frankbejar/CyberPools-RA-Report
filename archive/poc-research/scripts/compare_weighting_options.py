#!/usr/bin/env python3
"""
Compare different weighting approaches to see impact on grades
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
    "b032c58a-fc8f-f011-b4cb-0022480aaebb",
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

def calculate_overall_score_with_weighted_foundation(questions, question_mapping, foundation_multiplier):
    """Calculate overall score with foundation questions weighted more heavily."""
    applicable = [q for q in questions if q['qResponse'] != 0]
    if not applicable:
        return 100

    actual = 0
    min_score = 0
    max_score = 0

    for q in applicable:
        q_info = question_mapping.get(q['qID'], {})
        q_number = q_info.get('number', '0.0')
        is_foundation = (q.get('qReq', False) or q_number in COMPLIANCE_QUESTION_NUMBERS) and q['qID'] not in EXCLUDED_CYBER_REQUIREMENTS

        base_impact = q_info.get('impact_score', 3)
        # Apply multiplier to foundation questions
        impact = base_impact * foundation_multiplier if is_foundation else base_impact

        actual += q['qScore'] * (foundation_multiplier if is_foundation else 1)
        min_score += impact * 1
        max_score += impact * 5

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

def simulate_all_methods(json_file, question_mapping):
    """Simulate all weighting methods."""
    with open(json_file) as f:
        questions = json.load(f)

    member_name = json_file.stem.replace('CBS-', '')

    # Get base scores
    foundation_score = calculate_foundation_score(questions, question_mapping)
    comprehensive_score = calculate_overall_score(questions, question_mapping)

    # Method 1: Current (60/40 blend)
    method1_score = int(foundation_score * 0.6 + comprehensive_score * 0.4)
    method1_grade = get_grade(method1_score)

    # Method 2: 70/30 blend
    method2_score = int(foundation_score * 0.7 + comprehensive_score * 0.3)
    method2_grade = get_grade(method2_score)

    # Method 3: 80/20 blend
    method3_score = int(foundation_score * 0.8 + comprehensive_score * 0.2)
    method3_grade = get_grade(method3_score)

    # Method 4: 2x Impact Weight for foundation questions
    method4_score = calculate_overall_score_with_weighted_foundation(questions, question_mapping, 2.0)
    method4_grade = get_grade(method4_score)

    # Method 5: 1.5x Impact Weight for foundation questions
    method5_score = calculate_overall_score_with_weighted_foundation(questions, question_mapping, 1.5)
    method5_grade = get_grade(method5_score)

    # Old method for comparison
    old_score = comprehensive_score
    old_grade = get_grade(old_score)

    return {
        'member': member_name,
        'foundation': foundation_score,
        'comprehensive': comprehensive_score,
        'old_score': old_score,
        'old_grade': old_grade,
        'method1_score': method1_score,
        'method1_grade': method1_grade,
        'method2_score': method2_score,
        'method2_grade': method2_grade,
        'method3_score': method3_score,
        'method3_grade': method3_grade,
        'method4_score': method4_score,
        'method4_grade': method4_grade,
        'method5_score': method5_score,
        'method5_grade': method5_grade,
    }

def main():
    # Load question mapping
    mapping_file = PROJECT_ROOT / 'mappings' / 'question_mapping.json'
    with open(mapping_file) as f:
        question_mapping = json.load(f)

    # Find all JSON files
    input_dir = PROJECT_ROOT / 'input'
    json_files = sorted(input_dir.glob('CBS-*.json'))

    print("=" * 120)
    print("WEIGHTING METHOD COMPARISON")
    print("=" * 120)
    print()

    results = []
    for json_file in json_files:
        result = simulate_all_methods(json_file, question_mapping)
        results.append(result)

    # Print header
    print(f"{'Member':<25} {'Found':<6} {'Comp':<6} {'Old':<8} {'60/40':<9} {'70/30':<9} {'80/20':<9} {'2x Wgt':<9} {'1.5x Wgt':<9}")
    print(f"{'':<25} {'%':<6} {'%':<6} {'(Now)':<8} {'Blend':<9} {'Blend':<9} {'Blend':<9} {'Impact':<9} {'Impact':<9}")
    print("-" * 120)

    for r in results:
        old = f"{r['old_score']}% {r['old_grade']}"
        m1 = f"{r['method1_score']}% {r['method1_grade']}"
        m2 = f"{r['method2_score']}% {r['method2_grade']}"
        m3 = f"{r['method3_score']}% {r['method3_grade']}"
        m4 = f"{r['method4_score']}% {r['method4_grade']}"
        m5 = f"{r['method5_score']}% {r['method5_grade']}"

        print(f"{r['member']:<25} {r['foundation']:<6} {r['comprehensive']:<6} {old:<8} {m1:<9} {m2:<9} {m3:<9} {m4:<9} {m5:<9}")

    print()
    print("Method Descriptions:")
    print("  • Old (Now):     Current production model - equal weight all questions")
    print("  • 60/40 Blend:   60% Foundation + 40% Comprehensive")
    print("  • 70/30 Blend:   70% Foundation + 30% Comprehensive")
    print("  • 80/20 Blend:   80% Foundation + 20% Comprehensive")
    print("  • 2x Wgt Impact: Foundation questions count 2x their impact score in overall calculation")
    print("  • 1.5x Wgt:      Foundation questions count 1.5x their impact score in overall calculation")
    print()
    print("Recommendation:")
    print("  For MAXIMUM impact where missing one foundation question substantially affects grade:")
    print("  → Use 80/20 Blend or 2x Impact Weight")
    print()

if __name__ == '__main__':
    main()
