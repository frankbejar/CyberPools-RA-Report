/**
 * =================================================================
 * ADDITIONS FOR CYBERPOOLS-REPORT-COMPLETE V2
 * =================================================================
 *
 * Add these sections to cyberpools-report-complete.js to match
 * the Python PDF output exactly.
 *
 * Instructions:
 * 1. Add BOILERPLATE constant after line 60 (after CONFIG)
 * 2. Replace generateHTML() function (around line 540)
 * 3. Add new page generator functions before generateCoverPage()
 *
 * =================================================================
 */

// ==================== ADD AFTER CONFIG (Line 60) ====================

// Boilerplate content (from boilerplate.json)
const BOILERPLATE = {
    introduction: {
        what_is_assessment: "A cyber risk assessment is the process of identifying, evaluating, and prioritizing potential security threats to an organization's assets and infrastructure. This includes analyzing the likelihood and impact of these risks and determining the measures and controls to be put in place to mitigate them. The goal of a cyber risk assessment is to improve an organization's cybersecurity posture and prevent data breaches, unauthorized access, and other types of cyber-attacks.",
        methodology: "The following categories have been derived from previous version of the risk assessment which questions were influenced from previous cyber insurance claims, cybersecurity best practices, and common knowledge derived from the cybersecurity industry and as outlined by organizations such as NIST (National Institute of Standards and Technology), CISA (Cybersecurity and Infrastructure Security Agency) and CIS (Center for Internet Security).",
        recommendation: "It is recommended that organizations schedule a review meeting with appropriate district personnel to discuss identified risks and to define remediation actions.",
        grading_update: "As of September 2025, and in alignment with our continuous improvement practices across all Cyber Toolkit services, CyberPools has enhanced the grading formula used in this assessment. The updated methodology ensures that scores more accurately reflect implementation status across each control category and the overall assessment.",
        emphasis: "While the overall score provides a high-level benchmark, members should place greater emphasis on the control categories and the associated risk ratings (Low, Medium, High). These ratings highlight which areas carry greater weight in reducing organizational risk and therefore warrant more focused attention during remediation planning.",
        contact: "For any questions about our risk assessment or grading, please reach out to cyber@cyberpools.org"
    },
    rating_legends: {
        control_ratings: {
            fully_implemented: { value: 1, label: "Fully Implemented", description: "Control(s) are fully implemented and effective at mitigating risk." },
            partially_implemented: { value: 3, label: "Partially Implemented", description: "Controls are partially implemented and somewhat effective in mitigating risk." },
            not_implemented: { value: 5, label: "Not Implemented", description: "Control(s) are nonexistent." },
            not_applicable: { value: 0, label: "Not Applicable", description: "Control(s) are not necessary or applicable to the environment." }
        },
        impact_ratings: {
            low: { value: 1, label: "Low", description: "Minimal disruption of operations and no sensitive data compromised or exfiltrated." },
            moderate: { value: 3, label: "Moderate", description: "Operational disruptions of operations but no sensitive data compromised or exfiltrated." },
            high: { value: 5, label: "High", description: "Significant disruption of operations and sensitive data compromised or exfiltrated." },
            not_applicable: { value: 0, label: "Not Applicable", description: "No impact to your organization or environment as a result of the missing control." }
        },
        risk_ratings: {
            low: { range: "0-9", label: "Low", description: "Overall risk is low to organization" },
            moderate: { range: "10-15", label: "Moderate", description: "Overall risk is moderate to organization" },
            high: { range: "16-25", label: "High", description: "Overall risk is high to organization." },
            not_applicable: { range: "0", label: "Not Applicable", description: "No risk posed as a result of the missing control." }
        },
        example: {
            control: "Multi-factor Authentication",
            control_rating: "Partially Implemented (3)",
            impact_rating: "High (5)",
            calculation: "3 x 5 = 15",
            result: "15 scores as moderate risk based on risk rating legend above."
        }
    }
};

// ==================== REPLACE generateHTML() FUNCTION (around line 540) ====================

function generateHTML(data) {
    console.log('Generating complete HTML document...');

    // NEW: Match Python template page order exactly
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Risk Assessment Report - ${escapeHtml(data.metadata.member_name)}</title>
    <style>${getInlineCSS()}</style>
</head>
<body>
${generateCoverPage(data)}
${generateIntroductionPage()}
${generateExecutiveSummary(data)}
${generateResultsSummary(data)}
${generateRatingLegendsPage()}
${generateHowToReadPage()}
${generateFindingsPage(data)}
${generateCyberRequirements(data)}
${data.categories.map(cat => generateCategoryPage(cat)).join('\n')}
</body>
</html>`;
}

// ==================== ADD THESE NEW PAGE GENERATORS (before generateCoverPage) ====================

/**
 * Generate Introduction Page
 */
function generateIntroductionPage() {
    const intro = BOILERPLATE.introduction;

    return `<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <h1>Introduction</h1>

    <h2>What is a Cyber Risk Assessment?</h2>
    <p>${intro.what_is_assessment}</p>

    <h2>Methodology</h2>
    <p>${intro.methodology}</p>
    <p>${intro.recommendation}</p>

    <h2>Grading Methodology Update</h2>
    <p>${intro.grading_update}</p>
    <p>${intro.emphasis}</p>

    <div class="info-box" style="margin-top:20px;">
        <p><strong>Questions or Feedback:</strong> ${intro.contact}</p>
    </div>
</div>
`;
}

/**
 * Generate Rating Legends / Methodology Page
 */
function generateRatingLegendsPage() {
    const legends = BOILERPLATE.rating_legends;

    return `<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <h1>Assessment Methodology</h1>

    <h2>Rating Legend</h2>
    <div class="table-wrapper">
        <table class="legend-table">
            <thead>
                <tr>
                    <th>Control Rating</th>
                    <th>Impact Rating</th>
                    <th>Risk Rating</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>
                        <strong>${legends.control_ratings.fully_implemented.label}</strong><br>
                        ${legends.control_ratings.fully_implemented.description}
                    </td>
                    <td>
                        <strong>${legends.impact_ratings.low.label} (${legends.impact_ratings.low.value})</strong><br>
                        ${legends.impact_ratings.low.description}
                    </td>
                    <td>
                        <strong>${legends.risk_ratings.low.label} (${legends.risk_ratings.low.range})</strong><br>
                        ${legends.risk_ratings.low.description}
                    </td>
                </tr>
                <tr>
                    <td>
                        <strong>${legends.control_ratings.partially_implemented.label}</strong><br>
                        ${legends.control_ratings.partially_implemented.description}
                    </td>
                    <td>
                        <strong>${legends.impact_ratings.moderate.label} (${legends.impact_ratings.moderate.value})</strong><br>
                        ${legends.impact_ratings.moderate.description}
                    </td>
                    <td>
                        <strong>${legends.risk_ratings.moderate.label} (${legends.risk_ratings.moderate.range})</strong><br>
                        ${legends.risk_ratings.moderate.description}
                    </td>
                </tr>
                <tr>
                    <td>
                        <strong>${legends.control_ratings.not_implemented.label}</strong><br>
                        ${legends.control_ratings.not_implemented.description}
                    </td>
                    <td>
                        <strong>${legends.impact_ratings.high.label} (${legends.impact_ratings.high.value})</strong><br>
                        ${legends.impact_ratings.high.description}
                    </td>
                    <td>
                        <strong>${legends.risk_ratings.high.label} (${legends.risk_ratings.high.range})</strong><br>
                        ${legends.risk_ratings.high.description}
                    </td>
                </tr>
                <tr>
                    <td>
                        <strong>${legends.control_ratings.not_applicable.label}</strong><br>
                        ${legends.control_ratings.not_applicable.description}
                    </td>
                    <td>
                        <strong>${legends.impact_ratings.not_applicable.label} (${legends.impact_ratings.not_applicable.value})</strong><br>
                        ${legends.impact_ratings.not_applicable.description}
                    </td>
                    <td>
                        <strong>${legends.risk_ratings.not_applicable.label} (${legends.risk_ratings.not_applicable.range})</strong><br>
                        ${legends.risk_ratings.not_applicable.description}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <h2>Scoring Methodology</h2>

    <h3>Raw Score Calculation</h3>
    <p>Each control is evaluated using a two-factor calculation that multiplies the implementation status by the potential impact to the organization.</p>

    <div class="info-box legend-info" style="background:#e8f4f8;border-left:4px solid #4A9FB8;padding:15px;margin:15px 0;">
        <h4 style="margin-top:0;">Formula: Control Rating × Impact Rating</h4>
        <p><strong>Control Rating:</strong> Indicates control implementation status.</p>
        <ul>
            <li>1 = Fully Implemented</li>
            <li>3 = Partially Implemented</li>
            <li>5 = Not Implemented</li>
        </ul>
        <p><strong>Impact Rating:</strong> Reflects the level of organizational disruption if the control fails.</p>
        <ul>
            <li>1 = Low impact (minimal disruption, no data compromise)</li>
            <li>3 = Moderate impact (operational disruption, no sensitive data compromise)</li>
            <li>5 = High impact (significant disruption and/or data compromise)</li>
        </ul>
    </div>

    <h3>Score Normalization</h3>
    <p>Raw scores are normalized to a 0–100 scale to produce comparable category and overall scores across assessments.</p>
    <ul>
        <li>Ensures organizations can be measured consistently year over year.</li>
        <li>Maintains alignment with industry benchmarks and CyberPools grading standards.</li>
        <li>Keeps the model sensitive to partially implemented controls versus complete gaps.</li>
    </ul>

    <h2>Risk Calculation Example</h2>
    <div class="info-box legend-info" style="background:#e8f4f8;border-left:4px solid #4A9FB8;padding:15px;">
        <p><strong>Control:</strong> ${legends.example.control}</p>
        <p><strong>Control Rating:</strong> ${legends.example.control_rating}</p>
        <p><strong>Impact Rating:</strong> ${legends.example.impact_rating}</p>
        <p><strong>Raw Risk Score:</strong> ${legends.example.calculation}</p>
        <p><strong>Result:</strong> ${legends.example.result}</p>
    </div>
</div>
`;
}

/**
 * Generate Complete Findings Page (All Risk Levels)
 */
function generateFindingsPage(data) {
    // Group findings by risk level
    const findings = {
        high: [],
        moderate: [],
        low: []
    };

    data.categories.forEach(cat => {
        cat.questions.forEach(q => {
            if (q.risk_score > 0) { // Exclude N/A
                const finding = {
                    category: cat.name,
                    question_number: q.number,
                    question_text: q.text,
                    control_status: q.control_status,
                    control_status_text: q.control_status_text,
                    impact_score: q.impact_score,
                    risk_score: q.risk_score,
                    risk_level: q.risk_level,
                    comments: q.comments
                };

                findings[q.risk_level].push(finding);
            }
        });
    });

    // Check if we have any findings
    const hasFindings = findings.high.length > 0 || findings.moderate.length > 0 || findings.low.length > 0;

    if (!hasFindings) {
        return ''; // No findings page if no findings
    }

    const riskMeta = {
        high: {
            title: 'High Risk Findings',
            range: 'Risk Score 16-25 – requires immediate attention.',
            cardClass: 'finding-card finding-card--high'
        },
        moderate: {
            title: 'Moderate Risk Findings',
            range: 'Risk Score 11-15 – schedule remediation activities.',
            cardClass: 'finding-card finding-card--moderate'
        },
        low: {
            title: 'Low Risk Findings',
            range: 'Risk Score 1-10 – monitor as part of normal operations.',
            cardClass: 'finding-card finding-card--low'
        }
    };

    const generateFindingCards = (items, level) => {
        if (!items || items.length === 0) return '';

        return items.map(finding => `
        <div class="${riskMeta[level].cardClass}">
            <div class="finding-card-title">${escapeHtml(finding.question_number)} ${escapeHtml(finding.question_text)}</div>
            <div class="finding-card-meta">Category: ${escapeHtml(finding.category)}</div>
            <div class="finding-card-status">
                <div class="status-item">
                    <span class="status-label">Control Status:</span>
                    <span class="badge ${finding.control_status === 1 ? 'badge-success' : finding.control_status === 3 ? 'badge-warning' : 'badge-danger'}">${escapeHtml(finding.control_status_text)} (${finding.control_status})</span>
                </div>
                <div class="status-item">
                    <span class="status-label">Impact:</span>
                    <span class="badge ${finding.impact_score === 5 ? 'badge-danger' : finding.impact_score === 3 ? 'badge-warning' : 'badge-success'}">${finding.impact_score === 5 ? 'HIGH' : finding.impact_score === 3 ? 'MODERATE' : 'LOW'} (${finding.impact_score})</span>
                </div>
                <div class="status-item">
                    <span class="status-label">Risk Score:</span>
                    <span class="badge ${finding.risk_score >= 16 ? 'badge-danger' : finding.risk_score >= 10 ? 'badge-warning' : 'badge-success'}">${finding.risk_score} - ${finding.risk_score >= 16 ? 'HIGH' : finding.risk_score >= 10 ? 'MODERATE' : 'LOW'}</span>
                </div>
            </div>
            ${finding.comments ? `<div class="finding-card-notes">${escapeHtml(finding.comments)}</div>` : ''}
        </div>
        `).join('');
    };

    const generateRiskGroup = (level) => {
        const items = findings[level];
        if (!items || items.length === 0) return '';

        return `
            <div class="findings-risk-group">
                <div class="findings-risk-heading">
                    <span>${riskMeta[level].title} (${items.length})</span>
                </div>
                <p class="findings-intro">${riskMeta[level].range}</p>
                <div class="findings-grid">
                    ${generateFindingCards(items, level)}
                </div>
            </div>
        `;
    };

    return `<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <div class="findings-section">
        <div class="findings-header">
            <div class="findings-header-icon">⚠</div>
            <div class="findings-header-title">Key Findings</div>
        </div>
        <p class="findings-intro">The following controls were highlighted based on their risk scores and should be reviewed with the stakeholder team.</p>

        ${generateRiskGroup('high')}
        ${generateRiskGroup('moderate')}
        ${generateRiskGroup('low')}
    </div>
</div>
`;
}

// ==================== ADD THESE CSS CLASSES TO getInlineCSS() ====================

// Add to the CSS string in getInlineCSS() function (around line 880):

/*
.finding-card{background:#fff;border-radius:6px;border:1px solid #ccc;padding:20px 24px;margin-bottom:24px;box-shadow:0 6px 24px rgba(17,24,39,0.04)}
.finding-card-title{font-weight:700;color:#2C5F7C;margin-bottom:8px;font-size:14px}
.finding-card-meta{font-size:12px;color:#666;margin-bottom:8px}
.finding-card-status{display:flex;gap:24px;margin:12px 0;flex-wrap:wrap}
.finding-card-notes{background:#F5F7FA;border-radius:6px;padding:12px 14px;font-size:12px;color:#333;border-left:3px solid #4A9FB8;margin-top:12px}
.finding-card--high{border-left:4px solid #C10000}
.finding-card--moderate{border-left:4px solid #F39C12}
.finding-card--low{border-left:4px solid #4CAF50}
.findings-header{display:flex;align-items:center;margin-bottom:16px}
.findings-header-icon{margin-right:12px;font-size:24px;color:#F39C12}
.findings-header-title{font-size:20px;font-weight:700;text-transform:uppercase;letter-spacing:1.1px;color:#2C5F7C}
.findings-intro{color:#666;font-size:13px;margin:0 0 16px 0}
.findings-risk-group{margin-bottom:24px}
.findings-risk-heading{font-weight:700;font-size:16px;color:#2C5F7C;margin-bottom:8px}
.findings-grid{display:flex;flex-direction:column}
.legend-info{background:#e8f4f8;border-left:4px solid #4A9FB8;padding:15px;margin:15px 0}
.info-box{background:#F5F7FA;border-left:4px solid #4A9FB8;padding:15px;margin:12px 0;border-radius:0 6px 6px 0}
.info-box h4{color:#4A9FB8;margin-top:0;margin-bottom:8px}
.table-wrapper{margin:15px 0;background:#fff;border:1px solid #ccc;border-radius:6px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,0.08)}
.table-wrapper table{margin:0}
.legend-table td{vertical-align:top;line-height:1.6;padding:16px}
.legend-table strong{color:#2C5F7C}
*/

// ==================== END OF ADDITIONS ====================

console.log('✅ V2 additions loaded. These add:');
console.log('  - Introduction page');
console.log('  - Rating Legends / Methodology page');
console.log('  - Complete Findings page (all risk levels)');
console.log('  - Exact page order matching Python template');
