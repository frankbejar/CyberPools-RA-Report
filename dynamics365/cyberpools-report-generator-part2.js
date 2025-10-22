/**
 * CyberPools Report Generator - Part 2: HTML Generation & DocRaptor
 *
 * This file contains the HTML generation and DocRaptor integration.
 * Append this to the main file or keep separate and combine during deployment.
 */

// ==================== HTML GENERATION ====================

function generateHTML(data) {
    console.log('Generating HTML...');

    const css = getInlineCSS();

    return `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Risk Assessment Report - ${escapeHtml(data.metadata.member_name)}</title>
    <style>${css}</style>
</head>
<body>
    ${generateCoverPage(data)}
    ${generateExecutiveSummary(data)}
    ${generateResultsSummary(data)}
    ${generateHowToReadPage()}
    ${data.has_high_risk ? generateHighRiskFindings(data) : ''}
    ${generateCategories(data)}
    ${generateCyberRequirements(data)}
</body>
</html>
    `.trim();
}

// ==================== PAGE GENERATORS ====================

function generateCoverPage(data) {
    return `
<div class="page cover-page">
    <div class="cover-logo">CYBERPOOLS</div>
    <div class="cover-title">Risk Assessment Report</div>
    <div class="cover-subtitle">${escapeHtml(data.metadata.member_name)}</div>

    <div class="cover-metadata">
        <div class="cover-metadata-item">
            <span class="cover-metadata-label">Assessment Date:</span>
            <span class="cover-metadata-value">${escapeHtml(data.metadata.assessment_date)}</span>
        </div>
        <div class="cover-metadata-item">
            <span class="cover-metadata-label">Conducted By:</span>
            <span class="cover-metadata-value">${escapeHtml(data.metadata.conducted_by)}</span>
        </div>
        <div class="cover-metadata-item">
            <span class="cover-metadata-label">Member Contact:</span>
            <span class="cover-metadata-value">${escapeHtml(data.metadata.member_contact)}</span>
        </div>
        <div class="cover-metadata-item">
            <span class="cover-metadata-label">Template Version:</span>
            <span class="cover-metadata-value">${escapeHtml(data.metadata.version)}</span>
        </div>
    </div>
</div>
    `;
}

function generateExecutiveSummary(data) {
    const hasContent = data.executive_summary_raw && data.executive_summary_raw.length > 10;

    return `
<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <h1>Executive Summary</h1>

    ${hasContent ? `
    <div class="executive-summary-content">
        ${data.executive_summary_html}
    </div>
    ` : `
    <div class="executive-summary-placeholder">
        <h3 style="color: #6c757d; margin-top: 0;">[EXECUTIVE SUMMARY - CUSTOMIZED BY ACCOUNT MANAGER]</h3>

        <p>This section provides a high-level strategic overview of the assessment findings. The Account Manager reviews the detailed results and synthesizes key strengths and priority opportunities for improvement.</p>

        <p><strong>Sample Executive Summary:</strong></p>

        <p>"The organization demonstrates strong cybersecurity fundamentals with excellent performance in access management and incident response capabilities. A mature backup strategy and comprehensive security awareness program reflect the organization's commitment to operational resilience. Primary opportunity exists in implementing DNS filtering to strengthen malware defense posture. Overall, the assessment reveals a well-managed security program with focused areas for enhancement."</p>

        <p style="margin-top: 20px;"><em>Note: This placeholder text will be replaced with custom content entered by the Account Manager in the CRM system.</em></p>
    </div>
    `}
</div>
    `;
}

function generateResultsSummary(data) {
    const scoring = data.scoring;

    return `
<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <h1>Results Summary</h1>

    <div class="overall-score-box">
        <div class="score-label">Overall Security Score</div>
        <div class="overall-score">${scoring.overall_score}</div>
        <div class="overall-progress">
            <div class="overall-progress-track">
                <div class="overall-progress-fill" style="width: ${scoring.overall_score}%"></div>
            </div>
        </div>
    </div>

    <div class="risk-distribution-grid">
        <div class="risk-box high-risk">
            <div class="risk-number">${scoring.risk_distribution.high}</div>
            <div class="risk-label">High Risk</div>
        </div>
        <div class="risk-box moderate-risk">
            <div class="risk-number">${scoring.risk_distribution.moderate}</div>
            <div class="risk-label">Moderate Risk</div>
        </div>
        <div class="risk-box low-risk">
            <div class="risk-number">${scoring.risk_distribution.low}</div>
            <div class="risk-label">Low Risk</div>
        </div>
    </div>

    <h2>Category Scores</h2>
    ${generateCategoryScoresTable(data.categories)}
</div>
    `;
}

function generateCategoryScoresTable(categories) {
    const rows = categories.map(cat => `
        <tr>
            <td><strong>${escapeHtml(cat.number)}. ${escapeHtml(cat.name)}</strong></td>
            <td style="text-align: center;">
                <div class="score-bar">
                    <span>${cat.score}%</span>
                    <div class="score-bar-visual">
                        <div class="score-bar-fill ${getScoreFillClass(cat.score)}" style="width: ${cat.score}%"></div>
                    </div>
                </div>
            </td>
        </tr>
    `).join('');

    return `
<table class="legend-table">
    <thead>
        <tr>
            <th>Category</th>
            <th style="text-align: center; width: 40%;">Score</th>
        </tr>
    </thead>
    <tbody>
        ${rows}
    </tbody>
</table>
    `;
}

function generateHowToReadPage() {
    return `
<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <h1>How to Read This Report</h1>

    <div class="guide-grid">
        <div class="guide-item">
            <div class="guide-number">1</div>
            <div class="guide-content">
                <h4>Overall Score</h4>
                <p>The overall score reflects your organization's cybersecurity maturity on a scale of 0-100. Higher scores indicate stronger security controls.</p>
            </div>
        </div>

        <div class="guide-item">
            <div class="guide-number">2</div>
            <div class="guide-content">
                <h4>Risk Levels</h4>
                <p><strong>High Risk:</strong> Critical gaps requiring immediate attention. <strong>Moderate Risk:</strong> Important areas for improvement. <strong>Low Risk:</strong> Minor enhancements or best practices.</p>
            </div>
        </div>

        <div class="guide-item">
            <div class="guide-number">3</div>
            <div class="guide-content">
                <h4>Control Status</h4>
                <p><strong>Fully Implemented:</strong> Control is in place and effective. <strong>Partially Implemented:</strong> Some elements exist. <strong>Not Implemented:</strong> Control is missing.</p>
            </div>
        </div>

        <div class="guide-item">
            <div class="guide-number">4</div>
            <div class="guide-content">
                <h4>Categories</h4>
                <p>The assessment is organized into security domains (Access Control, Data Protection, etc.), each with specific questions and scores.</p>
            </div>
        </div>
    </div>
</div>
    `;
}

function generateHighRiskFindings(data) {
    const highRiskQuestions = [];

    data.categories.forEach(cat => {
        cat.questions.forEach(q => {
            if (q.risk_score >= 16) {
                highRiskQuestions.push({
                    category: cat.name,
                    question: q
                });
            }
        });
    });

    if (highRiskQuestions.length === 0) return '';

    const items = highRiskQuestions.map(item => `
        <div class="high-risk-item">
            <strong>${escapeHtml(item.category)} - ${escapeHtml(item.question.number)}</strong>
            <p>${escapeHtml(item.question.text)}</p>
            ${item.question.comments ? `<p><em>Notes: ${escapeHtml(item.question.comments)}</em></p>` : ''}
        </div>
    `).join('');

    return `
<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <h1>⚠️ High Risk Findings</h1>

    <div class="high-risk-section">
        <div class="high-risk-header">
            Critical Items Requiring Immediate Attention
        </div>
        ${items}
    </div>
</div>
    `;
}

function generateCategories(data) {
    return data.categories.map(cat => {
        const questions = cat.questions.map(q => generateQuestion(q)).join('');

        return `
<div class="page category-page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <div class="category-header">
        <div>
            <div class="category-number">${escapeHtml(cat.number)}</div>
            <div class="category-name">${escapeHtml(cat.name)}</div>
        </div>
        <div class="category-score">${cat.score}%</div>
    </div>

    ${cat.overview ? `
    <div class="category-overview">
        <h3>Overview</h3>
        <p>${escapeHtml(cat.overview)}</p>
    </div>
    ` : ''}

    ${questions}
</div>
        `;
    }).join('');
}

function generateQuestion(q) {
    const statusBadgeClass = {
        1: 'badge-success',
        3: 'badge-warning',
        5: 'badge-danger',
        0: 'badge-secondary'
    }[q.control_status] || 'badge-secondary';

    const riskBadgeClass = {
        'high': 'badge-danger',
        'moderate': 'badge-warning',
        'low': 'badge-success'
    }[q.risk_level] || 'badge-secondary';

    return `
<div class="question-block">
    <div class="question-core">
        <div class="question-text">
            <span class="question-number">${escapeHtml(q.number)}.</span>
            ${escapeHtml(q.text)}
        </div>

        ${q.control_description ? `
        <div class="control-description">
            ${escapeHtml(q.control_description)}
        </div>
        ` : ''}

        <div class="question-status">
            <div class="status-item">
                <span class="status-label">Status:</span>
                <span class="badge ${statusBadgeClass}">${escapeHtml(q.control_status_text)}</span>
            </div>
            <div class="status-item">
                <span class="status-label">Risk Level:</span>
                <span class="badge ${riskBadgeClass}">${q.risk_level}</span>
            </div>
            <div class="status-item">
                <span class="status-label">Risk Score:</span>
                <span>${q.risk_score}</span>
            </div>
        </div>

        ${q.comments ? `
        <div class="comments-section">
            <span class="comments-label">Assessment Notes:</span>
            <div class="comments-text">${escapeHtml(q.comments)}</div>
        </div>
        ` : ''}
    </div>
</div>
    `;
}

function generateCyberRequirements(data) {
    if (data.cyber_requirements.length === 0) return '';

    const rows = data.cyber_requirements.map(req => `
        <tr>
            <td>${escapeHtml(req.question)}</td>
            <td class="text-center">
                ${req.compliance ?
                    '<span class="compliance-yes">✓ Yes</span>' :
                    '<span class="compliance-no">✗ No</span>'
                }
            </td>
        </tr>
    `).join('');

    return `
<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <h1>Cyber Requirements Compliance</h1>

    <p>The following controls are mandatory requirements for cyber insurance coverage:</p>

    <table class="compliance-table">
        <thead>
            <tr>
                <th>Requirement</th>
                <th style="width: 150px; text-align: center;">Compliant</th>
            </tr>
        </thead>
        <tbody>
            ${rows}
        </tbody>
    </table>
</div>
    `;
}

// ==================== Continue in Part 3 for CSS and DocRaptor... ====================
