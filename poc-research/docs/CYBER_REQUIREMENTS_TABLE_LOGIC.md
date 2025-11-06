# Cyber Requirements Compliance Table - Build Logic

## Executive Summary

The **Cyber Requirements Compliance Table** (also called "Critical Control Table") is built by filtering questions from the CRM assessment data using **TWO conditions** (OR logic). A question appears in this table if **EITHER** condition is true:

1. **qReq Flag**: The question has `qReq: true` in the JSON data
2. **Question Number Match**: The question's number is in the hardcoded `COMPLIANCE_QUESTION_NUMBERS` set

## CC USD Analysis Result

**For the CC USD JSON file you provided:**
- Total questions in assessment: 50
- Questions with `qReq: true`: 0
- Questions matching by number: 0
- **Cyber Requirements table entries: 0 (EMPTY)**

**Why is it empty?**
- All questions have `qReq: false`
- All question GUIDs are NOT in the `question_mapping.json` file
- Without mapping, question numbers default to '0.0'
- '0.0' is not in `COMPLIANCE_QUESTION_NUMBERS` set

## Code Location & Logic

### Primary Logic: `scripts/transform_and_generate.py`

**Lines 38-51: Hardcoded Question Numbers**
```python
COMPLIANCE_QUESTION_NUMBERS = {
    "1.4",  # End-of-life software
    "2.3",  # MFA for cloud resources
    "2.4",  # MFA for remote access
    "2.5",  # MFA for admin/privileged accounts
    "2.6",  # MFA for critical systems
    "4.3",  # Patch management
    "4.7",  # External vulnerability scanning
    "5.4",  # EDR implementation
    "6.3",  # Air-gapped/immutable backups
    "6.4",  # Bi-annual backup testing
    "7.2",  # Quarterly phishing simulations
    "7.3",  # Security awareness training
}
```

**Lines 288-290: Exclusions**
```python
EXCLUDED_CYBER_REQUIREMENTS = {
    "b032c58a-fc8f-f011-b4cb-0022480aaebb",  # Cyber insurance participation
}
```

**Lines 361-378: Table Building Logic**
```python
cyber_requirements = []
if include_compliance:
    for q in crm_questions:
        # CONDITION 1: Skip excluded questions
        if q['qID'] in EXCLUDED_CYBER_REQUIREMENTS:
            continue

        # Lookup question metadata by GUID
        q_info = question_mapping.get(q['qID'], {
            'text': 'Unknown Requirement',
            'number': '0.0'
        })
        q_number = q_info.get('number', '0.0')

        # CONDITION 2: Include if qReq flag OR number matches
        include_requirement = (
            q.get('qReq', False) or                    # Condition A: qReq flag
            q_number in COMPLIANCE_QUESTION_NUMBERS    # Condition B: number match
        )

        if include_requirement:
            cyber_requirements.append({
                'question': q_info.get('text', 'Unknown Requirement'),
                'number': q_number,
                'compliance': q['qResponse'] == 1  # 1 = Fully Implemented
            })

    # Sort by question number
    cyber_requirements.sort(
        key=lambda x: float(x['number']) if x['number'] != '0.0' else 999
    )
```

## Data Flow Diagram

```
1. Input: CRM JSON File
   ├─ qID: "guid-here"
   ├─ qReq: true/false
   └─ qResponse: 1/3/5

2. Lookup: question_mapping.json
   ├─ Maps qID → question number
   └─ If not found → defaults to '0.0'

3. Filter Logic (OR condition):
   ├─ Condition A: qReq == true
   └─ Condition B: question number in COMPLIANCE_QUESTION_NUMBERS

4. Output: cyber_requirements array
   ├─ question text
   ├─ question number
   └─ compliance (Yes if qResponse == 1, else No)

5. Template Rendering: templates/partials/cyber_requirements.html
   └─ Displays table with ✓ Yes or ✗ No

6. Final PDF: Cyber Requirements Compliance Table
```

## Condition Breakdown

### Condition A: qReq Flag
- **Source**: Set in CRM during assessment
- **Maintenance**: Updated via `scripts/update_cyber_requirements.py`
- **Purpose**: Marks questions as "required by The Trust"
- **Typical Count**: 12 questions across standard assessment

### Condition B: Question Number Match
- **Source**: Hardcoded in `COMPLIANCE_QUESTION_NUMBERS` set
- **Purpose**: Fallback/override mechanism
- **Use Case**: Ensures specific questions always appear even if qReq is false
- **Standard Questions**: 12 questions (1.4, 2.3-2.6, 4.3, 4.7, 5.4, 6.3-6.4, 7.2-7.3)

### Why Two Conditions?

This dual-condition design provides:

1. **Flexibility**: CRM can set `qReq: true` dynamically per assessment
2. **Consistency**: Hardcoded numbers ensure core requirements always appear
3. **Override**: Allows manual inclusion by question number regardless of qReq flag
4. **Redundancy**: If qReq flags aren't set, number matching catches them

## The 7 Trust Requirements → 12 Questions Mapping

The Trust insurance pool has **7 simplified cyber requirements** that map to **12 specific questions** in the 51-question assessment:

| Trust Requirement | Question Numbers | Description |
|------------------|------------------|-------------|
| 1. MFA Implementation | 2.3, 2.4, 2.5, 2.6 | Multi-factor authentication across systems |
| 2. Immutable Backups & Testing | 6.3, 6.4 | Air-gapped backups with bi-annual validation |
| 3. Vulnerability Scanning | 4.7 | Quarterly external vulnerability scans |
| 4. Security Awareness Training | 7.2, 7.3 | Phishing simulations and training |
| 5. EDR Implementation | 5.4 | Endpoint detection and response software |
| 6. EOL Software Management | 1.4 | End-of-life software retirement/segmentation |
| 7. Patch Management | 4.3 | 30/7 day patch management process |

## Template Rendering

### HTML Template: `templates/partials/cyber_requirements.html`

```html
<h1>Cyber Requirements Compliance</h1>

<table class="compliance-table">
    <thead>
        <tr>
            <th>No.</th>
            <th>Requirement</th>
            <th>Compliance</th>
        </tr>
    </thead>
    <tbody>
        {% for req in cyber_requirements %}
        <tr>
            <td><strong>{{ req.number }}</strong></td>
            <td>{{ req.question }}</td>
            <td class="text-center">
                {% if req.compliance %}
                    <span class="compliance-yes">✓ Yes</span>
                {% else %}
                    <span class="compliance-no">✗ No</span>
                {% endif %}
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

**Compliance Logic:**
- `req.compliance = true` if `qResponse == 1` (Fully Implemented) → Shows **✓ Yes**
- `req.compliance = false` if `qResponse == 3 or 5` (Partial/Not Implemented) → Shows **✗ No**

## Example Comparisons

### Example 1: CBS-CBS.json (Standard Assessment)

**Question Sample:**
```json
{
  "qID": "ba646c09-9478-f011-b4cb-000d3a34656f",
  "qReq": false,
  "qResponse": 1,
  "qScore": 5
}
```

**Processing:**
1. Lookup qID in question_mapping.json → Found: Question 2.3
2. Check `qReq: false` → Condition A: FALSE
3. Check `"2.3" in COMPLIANCE_QUESTION_NUMBERS` → Condition B: TRUE
4. **Result**: INCLUDED in table (shows as ✓ Yes)

### Example 2: CC USD JSON (Unmapped Questions)

**Question Sample:**
```json
{
  "qID": "ddc56966-ecac-ef11-b8e8-000d3a36cba8",
  "qReq": false,
  "qResponse": 1,
  "qScore": 5
}
```

**Processing:**
1. Lookup qID in question_mapping.json → NOT FOUND → defaults to '0.0'
2. Check `qReq: false` → Condition A: FALSE
3. Check `"0.0" in COMPLIANCE_QUESTION_NUMBERS` → Condition B: FALSE
4. **Result**: NOT INCLUDED in table

## Maintenance Scripts

### `scripts/update_cyber_requirements.py`

**Purpose**: Updates `qReq` flags in all CBS-*.json input files

**Usage:**
```bash
python3 scripts/update_cyber_requirements.py
```

**Logic:**
- Defines `REQUIRED_QUESTIONS` set with 12 question GUIDs
- Sets `qReq: true` for questions in set
- Sets `qReq: false` for all others
- Updates all CBS-*.json files in `input/` directory

**Lines 11-37: Required Question GUIDs**
```python
REQUIRED_QUESTIONS = {
    # MFA (4 questions)
    "ba646c09-9478-f011-b4cb-000d3a34656f",  # 2.3
    "4c466f03-9478-f011-b4cb-000d3a34656f",  # 2.4
    "43fce405-9478-f011-b4cb-0022480aaebb",  # 2.5
    "b049e21b-9478-f011-b4cb-000d3a34656f",  # 2.6
    # Backups (2 questions)
    "0b323c15-9478-f011-b4cc-6045bd020f75",  # 6.3
    "3301bc17-9478-f011-b4cc-00224804279b",  # 6.4
    # Vulnerability Scanning (1 question)
    "0198eb0b-9478-f011-b4cb-0022480aaebb",  # 4.7
    # Security Awareness (2 questions)
    "14323c15-9478-f011-b4cc-6045bd020f75",  # 7.1
    "0c1bd215-9478-f011-b4cb-000d3a34656f",  # 7.2
    # EDR (1 question)
    "051bd215-9478-f011-b4cb-000d3a34656f",  # 5.4
    # EOL Software (1 question)
    "f80f521b-9478-f011-b4cc-6045bd020f75",  # 1.4
    # Patch Management (1 question)
    "c697eb0b-9478-f011-b4cb-0022480aaebb",  # 4.3
}
```

## Troubleshooting

### Problem: Table is empty or missing expected questions

**Diagnosis Steps:**

1. **Check qReq flags:**
   ```bash
   python3 -c "
   import json
   data = json.load(open('input/CBS-YOURFILE.json'))
   print(f'Questions with qReq=true: {sum(1 for q in data if q.get(\"qReq\"))}')
   "
   ```

2. **Check question mapping:**
   ```bash
   python3 -c "
   import json
   data = json.load(open('input/CBS-YOURFILE.json'))
   mapping = json.load(open('mappings/question_mapping.json'))
   unmapped = [q['qID'][:20] for q in data if q['qID'] not in mapping]
   print(f'Unmapped question IDs: {len(unmapped)}')
   if unmapped: print(unmapped[:5])
   "
   ```

3. **Run update script:**
   ```bash
   python3 scripts/update_cyber_requirements.py
   ```

### Problem: New assessment version with different GUIDs

**Solution**: Update `mappings/question_mapping.json` with new GUIDs

**Example:**
```json
{
  "ddc56966-ecac-ef11-b8e8-000d3a36cba8": {
    "number": "2.4",
    "text": "Is MFA implemented for remote access?",
    "control_description": "...",
    "impact_score": 5,
    "category": "772120001"
  }
}
```

## Key Files Reference

| File | Purpose | Lines |
|------|---------|-------|
| `scripts/transform_and_generate.py` | Main table building logic | 361-378 |
| `scripts/update_cyber_requirements.py` | Sets qReq flags | 11-37 |
| `templates/partials/cyber_requirements.html` | Table HTML rendering | 19-35 |
| `mappings/question_mapping.json` | GUID → question number mapping | Full file |
| `COMPLIANCE_QUESTION_NUMBERS` | Hardcoded question numbers | Lines 38-51 |

## Summary

The Cyber Requirements Compliance table appears in the report when:

1. **Questions are marked**: Via `qReq: true` flag in JSON OR question number in hardcoded set
2. **Questions are mapped**: Question GUIDs exist in `question_mapping.json`
3. **Exclusions respected**: Question is not in `EXCLUDED_CYBER_REQUIREMENTS`
4. **Compliance shown**: ✓ Yes if `qResponse == 1`, ✗ No otherwise

**For CC USD:** The table is empty because question GUIDs are not in the mapping file, causing all questions to default to number '0.0', which doesn't match any criteria.
