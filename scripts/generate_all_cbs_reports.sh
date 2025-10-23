#!/bin/bash

# Generate all CBS Risk Assessment Reports
# This script generates PDFs for all three CBS schools with their specific metadata

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=========================================="
echo "Generating All CBS Risk Assessment Reports"
echo "=========================================="
echo ""

# Assessment #1: Rosary College Prep
echo "📄 Generating Rosary College Prep Report..."
python3 "$SCRIPT_DIR/generate_report_with_metadata.py" \
    --input "input/CBS-Rosary College Prep.json" \
    --member-name "Rosary College Prep" \
    --assessment-date "10/02/2025" \
    --conducted-by "Naweed Nabi" \
    --member-contact "Jovan Lazarevic" \
    --executive-summary "Rosary College Prep achieved an **overall cyber risk score of 80%**, reflecting a **solid cybersecurity foundation** with effective controls in several areas. The school demonstrates strong practices in **data recovery**, **secure network configuration**, **account management**, and **inventory management**. However, critical vulnerabilities remain in three key areas: **Incident Response**, **Data Protection**, and **Endpoint Security**. Specifically, the absence of a **formal Cyber Incident Response Plan (CIRP)**, lack of **Endpoint Detection and Response (EDR)**, and missing encryption on endpoints, servers, and backups present significant risks. Addressing these gaps by implementing a CIRP, deploying EDR, and encrypting all critical systems will substantially enhance the school's cyber resilience and incident response capabilities." \
    --outro-page

echo "✅ Rosary College Prep report complete"
echo ""

# Assessment #2: Salesian College Preparatory School
echo "📄 Generating Salesian College Preparatory School Report..."
python3 "$SCRIPT_DIR/generate_report_with_metadata.py" \
    --input "input/CBS-Salesian College Prep.json" \
    --member-name "Salesian College Preparatory School" \
    --assessment-date "10/09/2025" \
    --conducted-by "Naweed Nabi" \
    --member-contact "Kion Tubtim" \
    --executive-summary "Salesian College Preparatory School achieved an **overall cyber risk score of 76%**, reflecting a **developing cybersecurity posture** with solid foundational controls but significant gaps in critical areas. The school demonstrates strong practices in **data recovery**, **multi-factor authentication enforcement**, and **network segmentation**. However, major vulnerabilities exist in **Incident Response**, **Endpoint Security**, and **Security Awareness**. Specifically, the absence of a **formal Cyber Incident Response Plan (CIRP)**, lack of **Endpoint Detection and Response (EDR)**, missing endpoint encryption, inconsistent security awareness training, and gaps in backup testing present elevated risks to detection, response, and recovery capabilities. Strengthening these areas by implementing a CIRP, deploying EDR, encrypting devices, establishing regular security training, and validating backup recoverability will significantly improve the school's resilience against modern cyber threats." \
    --outro-page

echo "✅ Salesian College Preparatory School report complete"
echo ""

# Assessment #3: Santa Catalina School
echo "📄 Generating Santa Catalina School Report..."
python3 "$SCRIPT_DIR/generate_report_with_metadata.py" \
    --input "input/CBS-Santa Catalina School.json" \
    --member-name "Santa Catalina School" \
    --assessment-date "10/15/2025" \
    --conducted-by "Alex Robles" \
    --member-contact "Jodi Wiseley" \
    --executive-summary "Santa Catalina School achieved an **overall cyber risk score of 82%**, reflecting a **strong cybersecurity foundation** with effective controls in asset management, multi-factor authentication, vendor oversight, and staff awareness. The school demonstrates mature practices through **comprehensive MFA enforcement**, **air-gapped backups**, and **regular security training**, but key vulnerabilities remain in **Incident Response** and **Endpoint Security**. Specifically, the absence of a **formal Cyber Incident Response Plan (CIRP)**, lack of **Endpoint Detection and Response (EDR)**, and **limited endpoint encryption** present elevated risks to timely detection and recovery. Strengthening these areas by implementing a CIRP, deploying EDR, encrypting devices and establishing a backup validation process will significantly enhance the school's readiness and resilience against modern cyber threats." \
    --outro-page

echo "✅ Santa Catalina School report complete"
echo ""

echo "=========================================="
echo "✅ All Reports Generated Successfully!"
echo "=========================================="
echo ""
echo "Reports saved to: $PROJECT_ROOT/output/"
echo ""
echo "Generated files:"
ls -lh "$PROJECT_ROOT/output/"*Risk_Assessment*.pdf | tail -3
echo ""
echo "Note: Reports are in TEST mode (watermarked)."
echo "To generate production versions, add --production flag to each command."
