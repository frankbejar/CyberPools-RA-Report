#!/usr/bin/env python3
"""
Debug script to diagnose compliance table issue.
Tests the compliance logic with different data scenarios.
"""

import json
from pathlib import Path

# Test data scenarios
test_scenarios = [
    {
        "name": "Integer qResponse",
        "data": [
            {"qID": "test-1", "qResponse": 1, "qReq": True},  # Should be Yes
            {"qID": "test-2", "qResponse": 3, "qReq": True},  # Should be No
            {"qID": "test-3", "qResponse": 5, "qReq": True},  # Should be No
        ]
    },
    {
        "name": "String qResponse",
        "data": [
            {"qID": "test-1", "qResponse": "1", "qReq": True},  # String "1"
            {"qID": "test-2", "qResponse": "3", "qReq": True},  # String "3"
            {"qID": "test-3", "qResponse": "5", "qReq": True},  # String "5"
        ]
    },
    {
        "name": "Float qResponse",
        "data": [
            {"qID": "test-1", "qResponse": 1.0, "qReq": True},  # Float 1.0
            {"qID": "test-2", "qResponse": 3.0, "qReq": True},  # Float 3.0
            {"qID": "test-3", "qResponse": 5.0, "qReq": True},  # Float 5.0
        ]
    },
    {
        "name": "Boolean qResponse (potential D365 bug)",
        "data": [
            {"qID": "test-1", "qResponse": True, "qReq": True},   # True
            {"qID": "test-2", "qResponse": False, "qReq": True},  # False
            {"qID": "test-3", "qResponse": True, "qReq": True},   # True
        ]
    }
]

def test_compliance_logic(questions):
    """Test the compliance determination logic"""
    results = []
    for q in questions:
        # This is the EXACT logic from transform_and_generate.py line 373
        compliance = q['qResponse'] == 1

        results.append({
            'qID': q['qID'],
            'qResponse': q['qResponse'],
            'qResponse_type': type(q['qResponse']).__name__,
            'compliance_result': compliance,
            'display': "✓ Yes" if compliance else "✗ No"
        })
    return results

def test_loose_compliance_logic(questions):
    """Test with loose equality (type coercion)"""
    results = []
    for q in questions:
        # Using == with type coercion
        compliance = q['qResponse'] == 1

        # Also test what would happen with truthy check
        truthy_compliance = bool(q['qResponse'])

        results.append({
            'qID': q['qID'],
            'qResponse': q['qResponse'],
            'strict_equality': compliance,
            'truthy_check': truthy_compliance,
            'display_strict': "✓ Yes" if compliance else "✗ No",
            'display_truthy': "✓ Yes" if truthy_compliance else "✗ No"
        })
    return results

def main():
    print("=" * 80)
    print("COMPLIANCE LOGIC DIAGNOSTIC TEST")
    print("=" * 80)
    print()

    for scenario in test_scenarios:
        print(f"\n{'='*80}")
        print(f"Scenario: {scenario['name']}")
        print(f"{'='*80}")

        results = test_compliance_logic(scenario['data'])

        print("\nResults with current logic (q['qResponse'] == 1):")
        print("-" * 80)
        for r in results:
            print(f"  qID: {r['qID']}")
            print(f"    qResponse: {r['qResponse']!r} (type: {r['qResponse_type']})")
            print(f"    Compliance: {r['compliance_result']} → {r['display']}")
            print()

        # Test truthy behavior
        print("\nComparison with truthy check:")
        print("-" * 80)
        truthy_results = test_loose_compliance_logic(scenario['data'])
        for r in truthy_results:
            print(f"  qResponse: {r['qResponse']!r}")
            print(f"    Strict (== 1): {r['display_strict']}")
            print(f"    Truthy (bool): {r['display_truthy']}")
            if r['display_strict'] != r['display_truthy']:
                print(f"    ⚠️  MISMATCH DETECTED!")
            print()

    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print("""
If you're seeing all "Yes" in D365, likely causes:

1. DATA TYPE ISSUE (String "1"):
   - D365 might be returning qResponse as string "1" instead of integer 1
   - String "1" == 1 evaluates to False in Python
   - BUT: All values would show "No", not "Yes" (doesn't match symptom)

2. INVERTED LOGIC BUG:
   - Template or JavaScript might have inverted if/else
   - Check if {% if req.compliance %} should be {% if not req.compliance %}

3. ALL VALUES ARE 1:
   - D365 query might be filtering only implemented controls (qResponse=1)
   - Check the OData query: $filter=(cp_response eq 1)

4. JAVASCRIPT OVERRIDE:
   - If using D365 JavaScript version, check for hardcoded compliance: true

5. WRONG FIELD MAPPING:
   - D365 might be mapping wrong field to qResponse
   - Check if pulling from boolean field instead of optionset

NEXT STEPS:
1. Export a sample JSON from D365 and check qResponse values
2. Add console.log or print statements to see actual values
3. Check D365 OData query for any filters
    """)

if __name__ == "__main__":
    main()
