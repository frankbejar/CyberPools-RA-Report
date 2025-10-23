#!/usr/bin/env python3
"""
Update all JSON files to set qReq=true only for the 7 core CyberPools requirements.
All other questions will have qReq=false.
"""

import json
from pathlib import Path

# Define the 12 required question IDs (7 core requirements, some have multiple related questions)
REQUIRED_QUESTIONS = {
    # Requirement 1: MFA Implementation (4 questions)
    "ba646c09-9478-f011-b4cb-000d3a34656f",  # 2.3 - MFA for cloud resources
    "4c466f03-9478-f011-b4cb-000d3a34656f",  # 2.4 - MFA for remote access
    "43fce405-9478-f011-b4cb-0022480aaebb",  # 2.5 - MFA for admin/privileged
    "b049e21b-9478-f011-b4cb-000d3a34656f",  # 2.6 - MFA for critical systems

    # Requirement 2: Immutable Backups & Bi-annual Validation (2 questions)
    "0b323c15-9478-f011-b4cc-6045bd020f75",  # 6.3 - Air gap/immutable backups
    "3301bc17-9478-f011-b4cc-00224804279b",  # 6.4 - Bi-annual backup testing

    # Requirement 3: Quarterly Vulnerability Scanning (1 question)
    "0198eb0b-9478-f011-b4cb-0022480aaebb",  # 4.7 - External vulnerability scans

    # Requirement 4: Quarterly Security Awareness & Training (2 questions)
    "14323c15-9478-f011-b4cc-6045bd020f75",  # 7.1 - Security awareness program
    "0c1bd215-9478-f011-b4cb-000d3a34656f",  # 7.2 - Quarterly phishing simulations

    # Requirement 5: EDR Implementation (1 question)
    "051bd215-9478-f011-b4cb-000d3a34656f",  # 5.4 - EDR software services

    # Requirement 6: EOL Software Retirement/Segmentation (1 question)
    "f80f521b-9478-f011-b4cc-6045bd020f75",  # 1.4 - EOL software protection

    # Requirement 7: Patch Management (1 question)
    "c697eb0b-9478-f011-b4cb-0022480aaebb",  # 4.3 - Patch management process
}

def update_json_file(file_path):
    """Update a single JSON file with correct qReq values."""
    print(f"Processing {file_path.name}...")

    # Load the JSON
    with open(file_path, 'r') as f:
        questions = json.load(f)

    # Track changes
    updated_count = 0

    # Update each question
    for question in questions:
        qid = question.get('qID')
        current_req = question.get('qReq', False)
        should_be_req = qid in REQUIRED_QUESTIONS

        if current_req != should_be_req:
            question['qReq'] = should_be_req
            updated_count += 1

    # Save back to file
    with open(file_path, 'w') as f:
        json.dump(questions, f, separators=(',', ':'))

    print(f"  ✅ Updated {updated_count} questions in {file_path.name}")
    return updated_count

def main():
    input_dir = Path(__file__).parent.parent / 'input'

    print("=" * 60)
    print("Updating CyberPools Cyber Requirements")
    print("=" * 60)
    print(f"\nSetting qReq=true for {len(REQUIRED_QUESTIONS)} core requirement questions")
    print("All other questions will have qReq=false\n")

    # Process all CBS JSON files
    json_files = sorted(input_dir.glob('CBS-*.json'))
    total_updated = 0

    for json_file in json_files:
        updated = update_json_file(json_file)
        total_updated += updated

    print(f"\n{'=' * 60}")
    print(f"✅ Complete! Updated {total_updated} total question flags across {len(json_files)} files")
    print(f"{'=' * 60}\n")

    print("Core Requirements Summary:")
    print("1️⃣ MFA Implementation (4 questions)")
    print("2️⃣ Immutable Backups & Bi-annual Validation (2 questions)")
    print("3️⃣ Quarterly Vulnerability Scanning (1 question)")
    print("4️⃣ Quarterly Security Awareness & Training (2 questions)")
    print("5️⃣ EDR Implementation (1 question)")
    print("6️⃣ EOL Software Retirement/Segmentation (1 question)")
    print("7️⃣ Patch Management 30/7 days (1 question)")
    print(f"\nTotal: {len(REQUIRED_QUESTIONS)} required questions")

if __name__ == '__main__':
    main()
