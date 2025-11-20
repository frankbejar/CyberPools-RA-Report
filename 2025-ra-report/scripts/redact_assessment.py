#!/usr/bin/env python3
"""
Redact confidential information from assessment JSON data.
Replaces sensitive details with ████ blocks.
"""

import json
import re
import sys
from pathlib import Path


def redact_text(text):
    """
    Redact confidential information from text using pattern matching.
    Returns redacted text with ████ blocks.
    """
    if not text or text.strip() == "":
        return text

    # Define redaction patterns
    redactions = [
        # People names
        (r'\bKT\b', '██'),
        (r'\bKeon\b', '████'),
        (r'\bKion\b', '████'),
        (r'HR Manager', '██ ███████'),

        # Vendor/Product names (security tools)
        (r'\bMosyle\b', '██████'),
        (r'\bBackupify\b', '█████████'),
        (r'\bMeraki\b', '██████'),
        (r'\bWebroot\b', '███████'),
        (r'\bKnowBe4\b', '███████'),
        (r'\bRaptor\b', '██████'),
        (r'\bCisco Catalyst\b', '█████ ████████'),
        (r'\bCisco\b', '█████'),
        (r'\bFileVault\b', '█████████'),
        (r'\bGoogle Workspace\b', '██████ █████████'),
        (r'\bGoogle\b', '██████'),
        (r'\bApple\b', '█████'),
        (r'\bActive Directory\b', '██████ █████████'),

        # Organizational details
        (r'catholic schools?', '████████ ███████'),
        (r'Catholic schools?', '████████ ███████'),
        (r"CFO's", "███'█"),
        (r'\bdistrict-issued\b', '████████-██████'),
        (r'\bdistrict\b', '████████'),

        # Specific technical details that could be exploited
        (r'\bWPA2-PSK\b', '████-███'),
        (r'\bWPA2\b', '████'),
        (r'\bVLAN\b', '████'),
        (r'Windows Server 2012', '███████ ██████ ████'),
        (r'\bASM\b', '███'),
        (r'\bCDN\b', '███'),

        # Specific infrastructure details
        (r'\bIDF\b', '███'),
        (r'\bMDF\b', '███'),
        (r'\bVMS\b', '███'),
        (r'\bVOIP\b', '████'),
        (r'\bW-9\b', '█-█'),
        (r'\bAHC\b', '███'),
        (r'\bACH\b', '███'),

        # Time periods that might be identifying
        (r'2-3 years old', '█-█ █████ ███'),
        (r'in the fall', 'in ███ ████'),
        (r'five years', '████ █████'),

        # Physical location details
        (r'in a basement', 'in █ ████████'),
        (r'in a lockbox', 'in █ ███████'),
        (r'front desk', '█████ ████'),
    ]

    redacted = text
    for pattern, replacement in redactions:
        redacted = re.sub(pattern, replacement, redacted, flags=re.IGNORECASE)

    return redacted


def redact_assessment_data(input_path, output_path):
    """
    Read assessment JSON, redact confidential information, and save.
    """
    # Read input JSON
    with open(input_path, 'r') as f:
        data = json.load(f)

    # Redact notes in each question
    redacted_count = 0
    for question in data:
        if 'qNotes' in question and question['qNotes']:
            original = question['qNotes']
            redacted = redact_text(original)
            if original != redacted:
                redacted_count += 1
            question['qNotes'] = redacted

    # Write output JSON
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✓ Redacted {redacted_count} question notes")
    print(f"✓ Saved redacted data to: {output_path}")

    return redacted_count


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 redact_assessment.py <input.json> <output.json>")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)

    redact_assessment_data(input_file, output_file)
