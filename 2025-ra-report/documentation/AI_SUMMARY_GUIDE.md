# AI Executive Summary Generator Guide

## Overview

The AI Executive Summary Generator uses OpenAI GPT-3.5 Turbo to automatically create professional executive summaries for CyberPools risk assessment reports. It analyzes your JSON assessment data and generates context-aware, risk-focused summaries with proper markdown formatting.

---

## Features

- ✅ **Intelligent Analysis**: Automatically extracts scores, findings, strengths, and gaps
- ✅ **Multiple Tones**: Professional, Executive, Technical, or Concise
- ✅ **Interactive Review**: Approve, edit, regenerate, or change tone
- ✅ **Key Points Extraction**: Bullet-point summary in addition to prose
- ✅ **Clipboard Integration**: Auto-copy accepted summaries
- ✅ **Batch Processing**: Generate summaries for all assessments at once
- ✅ **Dry Run Mode**: Preview prompts and costs without API calls
- ✅ **Cost Tracking**: Shows API usage and costs for each generation

---

## Installation

### 1. Install Required Packages

```bash
pip install openai python-dotenv pyperclip
```

### 2. Configure API Key

Your OpenAI API key is already configured in `.env`:

```bash
# Check that .env exists
cat .env

# Should show:
# OPENAI_API_KEY=sk-proj-...
```

**⚠️ Security Note**: Never commit `.env` to git (it's already in `.gitignore`)

---

## Usage

### Basic Usage (Single Assessment)

```bash
python3 scripts/suggest_summary.py --input input/CBS-CBS.json
```

**What happens:**
1. Analyzes the assessment JSON
2. Generates executive summary using AI
3. Shows you the result with scores and metrics
4. Prompts you to accept, edit, regenerate, or change tone
5. Optionally copies to clipboard or saves to file

### Different Tones

```bash
# Professional tone (default - risk-focused partner)
python3 scripts/suggest_summary.py --input input/CBS-CBS.json --tone professional

# Executive tone (board-level, less technical)
python3 scripts/suggest_summary.py --input input/CBS-CBS.json --tone executive

# Technical tone (IT-focused, detailed)
python3 scripts/suggest_summary.py --input input/CBS-CBS.json --tone technical

# Concise tone (brief, bullet-focused)
python3 scripts/suggest_summary.py --input input/CBS-CBS.json --tone concise
```

### Batch Processing

Generate summaries for all assessments:

```bash
python3 scripts/suggest_summary.py --batch
```

This will:
- Find all `CBS-*.json` files in `input/`
- Generate summary for each one
- Prompt for review after each
- Save approved summaries to `summaries/` directory

### Dry Run Mode

Preview the AI prompt without making API calls:

```bash
python3 scripts/suggest_summary.py --input input/CBS-CBS.json --dry-run
```

Useful for:
- Checking what data will be sent to OpenAI
- Estimating costs before running
- Debugging prompt formatting

---

## Interactive Options

After generating a summary, you'll see:

```
📋 Actions:
  [a] Accept and copy to clipboard
  [e] Edit in text editor (nano)
  [r] Regenerate with same tone
  [t] Try different tone
  [s] Save to file
  [q] Quit without saving
```

### Accept (a)
- Copies summary to clipboard (if pyperclip installed)
- Ready to paste into report command

### Edit (e)
- Opens summary in nano text editor
- Make manual edits
- Saves and displays edited version

### Regenerate (r)
- Calls API again with same parameters
- Useful if result wasn't quite right
- Each regeneration costs ~$0.02-0.05

### Change Tone (t)
- Shows available tone options
- Regenerates with different style
- Great for comparing approaches

### Save to File (s)
- Saves to `summaries/` directory
- Default filename: `{Member_Name}_summary.md`
- Can specify custom filename

---

## Output Format

The AI generates two sections:

### 1. Executive Summary (Prose)
4-6 well-structured paragraphs with:
- Overall score and risk posture
- Perfect scores and achievements
- Specific technologies and controls (e.g., SentinelOne EDR/MDR)
- High-risk and moderate-risk findings
- Actionable recommendations

**Bold formatting** applied to:
- Member names
- Scores and grades
- Category names
- Technology names
- Control acronyms (MFA, EDR, CIRP, etc.)

### 2. Key Points (Bullets)
5-8 concise bullet points highlighting:
- Overall score
- Notable achievements
- Critical gaps
- Priority actions

---

## Cost Estimates

Using GPT-3.5 Turbo (as of 2024):

| Operation | Input Tokens | Output Tokens | Cost |
|-----------|--------------|---------------|------|
| Single summary | ~3,500 | ~800 | ~$0.02-0.05 |
| Batch (4 reports) | ~14,000 | ~3,200 | ~$0.10-0.20 |
| Monthly (20 reports) | ~70,000 | ~16,000 | ~$0.50-1.00 |

**Very affordable!** The script shows exact costs after each generation.

---

## Integration with Report Generation

### Option 1: Copy-Paste

```bash
# 1. Generate summary
python3 scripts/suggest_summary.py --input input/CBS-CBS.json

# 2. Accept and copy to clipboard (press 'a')

# 3. Generate report with pasted summary
python3 scripts/generate_report_with_metadata.py \
  --input "input/CBS-CBS.json" \
  --member-name "Christian Brothers Services" \
  --assessment-date "10/16/2025" \
  --conducted-by "Alex Robles" \
  --member-contact "Ashu Ketkar" \
  --executive-summary "**Christian Brothers Services** demonstrates..." \
  --outro-page
```

### Option 2: Save to File, Then Reference

```bash
# 1. Generate and save summary
python3 scripts/suggest_summary.py --input input/CBS-CBS.json
# (press 's' to save to summaries/CBS_summary.md)

# 2. Use saved file in report generation
python3 scripts/generate_report_with_metadata.py \
  --input "input/CBS-CBS.json" \
  --member-name "Christian Brothers Services" \
  --assessment-date "10/16/2025" \
  --conducted-by "Alex Robles" \
  --member-contact "Ashu Ketkar" \
  --executive-summary "$(cat summaries/CBS_summary.md)" \
  --outro-page
```

### Option 3: Batch Workflow

```bash
# 1. Generate all summaries
python3 scripts/suggest_summary.py --batch
# Review and save each one

# 2. Create a batch report generation script
#!/bin/bash
python3 scripts/generate_report_with_metadata.py \
  --input "input/CBS-CBS.json" \
  --member-name "Christian Brothers Services" \
  --assessment-date "10/16/2025" \
  --conducted-by "Alex Robles" \
  --member-contact "Ashu Ketkar" \
  --executive-summary "$(cat summaries/CBS_summary.md)" \
  --outro-page

python3 scripts/generate_report_with_metadata.py \
  --input "input/CBS-Rosary College Prep.json" \
  --member-name "Rosary College Prep" \
  --assessment-date "10/02/2025" \
  --conducted-by "Naweed Nabi" \
  --member-contact "Jovan Lazarevic" \
  --executive-summary "$(cat summaries/Rosary_summary.md)" \
  --outro-page

# ... etc
```

---

## Tone Descriptions

### Professional (Default)
**Best for**: Most CyberPools reports

**Characteristics**:
- Risk-focused but balanced
- Professional and authoritative
- Specific technologies and controls mentioned
- Uplifting for strengths, transparent about gaps
- Actionable recommendations

**Example**:
> **Christian Brothers Services** demonstrates an **exceptionally mature cybersecurity program** with an overall risk score of **96%**...

---

### Executive
**Best for**: Board presentations, C-suite summaries

**Characteristics**:
- Higher-level, strategic focus
- Less technical jargon
- Business impact emphasis
- Concise and accessible

**Example**:
> Christian Brothers Services has established enterprise-grade cybersecurity controls that significantly exceed industry standards, achieving a 96% risk score...

---

### Technical
**Best for**: IT teams, detailed remediation plans

**Characteristics**:
- Technically detailed and specific
- Control frameworks and protocols mentioned
- Granular findings
- Industry-standard terminology

**Example**:
> Assessment of Christian Brothers Services revealed comprehensive implementation of defense-in-depth controls, including SentinelOne EDR/MDR with 24/7 SOC monitoring, immutable backup architecture...

---

### Concise
**Best for**: Quick summaries, dashboards

**Characteristics**:
- Extremely brief (3 short paragraphs max)
- Bullet-point friendly
- Every word counts

**Example**:
> **Score: 96% (A)** - Exceptional program. Perfect scores in 6/9 categories. Zero high-risk findings. Minor gaps: DNS filtering, backup testing schedule.

---

## Examples

### Example 1: Single Assessment

```bash
$ python3 scripts/suggest_summary.py --input input/CBS-CBS.json

🔍 Analyzing: Christian Brothers Services
   Overall Score: 96% (Grade: A)
   High-risk findings: 0
   Moderate-risk findings: 2

🤖 Generating executive summary (tone: Professional (Risk-Focused))...

================================================================================
AI-GENERATED EXECUTIVE SUMMARY - Christian Brothers Services
Tone: Professional (Risk-Focused)
Score: 96% (Grade: A)
================================================================================

**Christian Brothers Services** demonstrates an **exceptionally mature
cybersecurity program** with an overall risk score of **96%** – among the
highest scores recorded in CyberPools assessments.

[... full summary ...]

================================================================================
KEY POINTS:
================================================================================

- **Overall Score: 96% (Grade A)** - Among highest in CyberPools assessments
- Perfect **100% scores** in 6 of 9 categories (Account Management, Data Protection, etc.)
- **Zero high-risk findings** identified
- Advanced controls: **SentinelOne EDR/MDR**, **encrypted immutable backups**, **CIRP with tabletop exercises**
- Minor enhancements: Implement dedicated DNS filtering, formalize bi-annual backup testing

================================================================================
API Cost: $0.0234 | Tokens: 3,421 in, 782 out
================================================================================

📋 Actions:
  [a] Accept and copy to clipboard
  [e] Edit in text editor (nano)
  [r] Regenerate with same tone
  [t] Try different tone
  [s] Save to file
  [q] Quit without saving

Your choice: a
✅ Copied to clipboard!
```

### Example 2: Batch Processing

```bash
$ python3 scripts/suggest_summary.py --batch

================================================================================
🤖 CyberPools AI Executive Summary Generator
================================================================================

Found 4 assessments:
  1. CBS-CBS.json
  2. CBS-Rosary College Prep.json
  3. CBS-Salesian College Prep.json
  4. CBS-Santa Catalina School.json

Generate summaries for all 4 assessments? [y/n]: y

================================================================================
[1/4] Processing CBS-CBS.json
================================================================================

🔍 Analyzing: Christian Brothers Services
...

[Shows summary, you review and approve]

================================================================================
[2/4] Processing CBS-Rosary College Prep.json
================================================================================

...

✅ Done!
```

---

## Troubleshooting

### "OPENAI_API_KEY not found"

**Solution**: Check that `.env` file exists and contains your API key:

```bash
cat .env
# Should show: OPENAI_API_KEY=sk-proj-...
```

If missing, create `.env` from template:
```bash
cp .env.example .env
nano .env  # Add your API key
```

### "openai package not installed"

**Solution**: Install required packages:

```bash
pip install openai python-dotenv pyperclip
```

### "pyperclip not installed"

**Solution** (Optional - clipboard features only):

```bash
pip install pyperclip
```

The script works without pyperclip, just without clipboard auto-copy.

### API Rate Limits

If you hit rate limits (rare with GPT-3.5):
- Wait a few seconds between calls
- Use `--dry-run` to preview without calling API
- Consider upgrading OpenAI plan if processing large batches

### Unexpected Output Format

If the AI doesn't follow formatting:
- Try regenerating (press 'r')
- Try a different tone (press 't')
- Edit manually (press 'e')

---

## Best Practices

1. **Review Before Accepting**: AI is smart but not perfect - always review
2. **Try Multiple Tones**: Compare professional vs. executive for best fit
3. **Edit for Specifics**: Use AI as starting point, add specific details you know
4. **Save Good Examples**: Build a library of approved summaries in `summaries/`
5. **Batch First, Review Later**: Generate all summaries, then review as a batch
6. **Use Dry Run**: Test prompts before spending API credits

---

## Future Enhancements

Potential improvements:
- Direct integration into `generate_report_with_metadata.py`
- Custom tone definitions (JSON config)
- Template-based customization
- Multi-language support
- Comparison mode (show multiple tones side-by-side)

---

## Support

For issues or questions:
- Check this guide first
- Review the example summaries in the script
- Test with `--dry-run` to debug prompts
- Check OpenAI API status: https://status.openai.com

---

**Happy summarizing! 🤖**
