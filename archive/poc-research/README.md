# POC Research & Concept Development

This folder contains proof-of-concept work, research materials, and experimental grading model concepts that are **not currently deployed in production**.

## Purpose

This directory serves as a workspace for:
- Testing new grading methodologies
- Exploring alternative assessment models
- Documenting research and concept development
- Preserving historical POC work for future reference

## Important Note

**⚠️ Nothing in this folder is currently in production.**

The production risk assessment system uses:
- Single overall score (0-100%)
- 51 questions across 9 categories
- Risk-based scoring: Control Rating × Impact Rating
- 12 "Cyber Requirements" compliance table
- Standard letter grades (A-F)

## Folder Structure

```
poc-research/
├── README.md                           # This file
├── POC_DUAL_SCORE_README.md           # Two-tier model concept overview
├── docs/                              # Research documentation
│   ├── ACTUAL_GRADING_OPTIONS.md      # 4 grading model options for 2026
│   ├── INSURANCE_STRATEGIC_ASSESSMENT_EXECUTIVE_SUMMARY.md  # Insurance research
│   ├── 80_20_MODEL_FINAL_RESULTS.md   # 80/20 weighting analysis
│   ├── TIER_MODEL_FINAL_SUMMARY.md    # Tier I/II model summary
│   ├── GRADING_SIMULATION_RESULTS.md  # Simulation results
│   ├── POC_TEAM_PRESENTATION_GUIDE.md # Team presentation materials
│   ├── POC_VISUAL_ENHANCEMENTS.md     # Visual design concepts
│   ├── ASSESSMENT_GAP_ANALYSIS.md     # Gap analysis research
│   ├── GRADING_MODEL_APPROACHES.md    # Comprehensive grading options
│   ├── CyberPools Company Profile.md  # Company background
│   └── QUICK_REFERENCE.md             # Quick reference guide
├── scripts/                           # POC scripts
│   ├── transform_and_generate_POC.py  # Two-tier report generator
│   ├── compare_weighting_options.py   # Weighting comparison tool
│   └── run_grading_simulation.py      # Simulation runner
├── templates/                         # POC templates
│   └── (Two-tier model templates)
├── styles/                            # POC stylesheets
│   └── dual_score_POC.css            # Two-tier styling
└── output/                            # POC generated reports
    └── POC_Dual_Score_*.pdf          # Sample two-tier reports

```

## Key POC Concepts Explored

### 1. Two-Tier Grading Model (80/20 Weighted)
**Status:** Concept only, not deployed

**Concept:**
- Tier I Score: Foundation (12 Cyber Requirements)
- Tier II Score: 80% × Tier I + 20% × Comprehensive
- Emphasizes critical insurance controls

**Files:**
- `POC_DUAL_SCORE_README.md`
- `docs/TIER_MODEL_FINAL_SUMMARY.md`
- `scripts/transform_and_generate_POC.py`

### 2. Alternative Weighting Models
**Status:** Research phase

**Concepts Explored:**
- Equal weighting (50/50)
- Moderate weighting (70/30)
- Category-based weighting
- Threshold-based grading

**Files:**
- `docs/80_20_MODEL_FINAL_RESULTS.md`
- `scripts/compare_weighting_options.py`

### 3. Enhanced Gap Analysis
**Status:** Research complete, recommendations documented

**Analysis:**
- Standards alignment (NIST, CIS, ISO 27001)
- Question coverage gaps
- Category balance issues
- Framework mapping

**Files:**
- `docs/ASSESSMENT_GAP_ANALYSIS.md`

## Using POC Materials

### To Run POC Two-Tier Reports

```bash
cd /Users/frankbejar/Documents/GitHub/cyberpools-RA-Report

python3 poc-research/scripts/transform_and_generate_POC.py \
  --input input/CBS-School.json \
  --auto \
  --engine docraptor \
  --output poc-research/output/test-report.pdf
```

### To Compare Weighting Options

```bash
python3 poc-research/scripts/compare_weighting_options.py \
  --input input/CBS-School.json
```

### To Run Grading Simulations

```bash
python3 poc-research/scripts/run_grading_simulation.py
```

## Decision Status

As of **October 30, 2025**, the team has **not decided** to implement any POC concepts.

Current considerations:
1. **Weighted Category Scoring** - Most likely short-term option
2. **Dual-Score Model** - Under evaluation for medium-term (6-12 months)
3. **80/20 Weighted Model** - Not recommended due to complexity
4. **Threshold-Based Grading** - Not recommended due to fairness concerns

See `../ACTUAL_GRADING_OPTIONS.md` for detailed recommendations based on production analysis.

## History

**October 2025:**
- Two-tier model POC developed
- Simulation testing with CBS schools
- Gap analysis completed
- Team review pending decision

**Next Steps:**
- Team review of options
- Insurance pool administrator feedback
- Test preferred model with 5-10 assessments
- Decision on implementation timeline

---

## Questions?

Contact: cyber@cyberpools.org

**Remember:** All materials in this folder are research/concept work. Always refer to production code in the main directory for actual deployed functionality.
