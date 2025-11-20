/**
 * CyberPools Report Generator - Local POC
 * Generates PDF reports using either Paged.js or DocRaptor
 */

// Configuration
const CONFIG = {
    DOCRAPTOR_API_KEY: 'Uej3BuDjlcc3vx8z5lfK',
    TEST_MODE: true, // Use test mode for POC
    DATA_PATH: './input/cb-ra.json',
    QUESTION_MAPPING_PATH: './mappings/question_mapping.json',
    CATEGORY_MAPPING_PATH: './mappings/category_mapping.json'
};

// Global data storage
let assessmentData = null;
let questionMapping = null;
let categoryMapping = null;

// Preload styles for inline rendering (fallback when <style id="report-styles"> is absent)
async function preloadStyles() {
    try {
        const response = await fetch('styles/main.css');
        if (!response.ok) throw new Error('Failed to load styles/main.css');
        const css = await response.text();

        let styleEl = document.getElementById('report-styles');
        if (!styleEl) {
            styleEl = document.createElement('style');
            styleEl.id = 'report-styles';
            document.head.appendChild(styleEl);
        }
        styleEl.textContent = css;
    } catch (error) {
        console.error('Style preload error:', error);
        updateStatus(`❌ Error loading styles: ${error.message}`);
    }
}

// Status updates
function updateStatus(message, isLoading = false) {
    const statusEl = document.getElementById('status');
    statusEl.innerHTML = isLoading
        ? `<span class="spinner"></span> ${message}`
        : message;
}

// Show comparison table
function showComparison() {
    const comparisonEl = document.getElementById('comparison');
    comparisonEl.style.display = comparisonEl.style.display === 'none' ? 'block' : 'none';
}

// Load test data from input folder
async function loadTestData() {
    updateStatus('Loading test data from input/ folder...', true);

    try {
        // Load all required files
        const [raResponse, qmResponse, cmResponse] = await Promise.all([
            fetch(CONFIG.DATA_PATH),
            fetch(CONFIG.QUESTION_MAPPING_PATH),
            fetch(CONFIG.CATEGORY_MAPPING_PATH)
        ]);

        if (!raResponse.ok) throw new Error('Failed to load cb-ra.json');
        if (!qmResponse.ok) throw new Error('Failed to load question_mapping.json');
        if (!cmResponse.ok) throw new Error('Failed to load category_mapping.json');

        assessmentData = await raResponse.json();
        questionMapping = await qmResponse.json();
        categoryMapping = await cmResponse.json();

        updateStatus(`✅ Loaded successfully: ${assessmentData.length} questions from Christian Brothers Services assessment`);
        console.log('Data loaded:', { assessmentData, questionMapping, categoryMapping });

    } catch (error) {
        updateStatus(`❌ Error loading data: ${error.message}`);
        console.error('Load error:', error);
    }
}

// Transform raw assessment data to report structure
function transformData() {
    if (!assessmentData || !questionMapping || !categoryMapping) {
        throw new Error('Data not loaded. Click "Reload Test Data" first.');
    }

    // Member/Service metadata (from CBS)
    const metadata = {
        memberName: 'Christian Brothers Services',
        assessmentDate: '2025-10-16',
        reportDate: new Date().toISOString().split('T')[0],
        overallScore: 96,
        overallGrade: 'A',
        executiveSummary: `Christian Brothers Services demonstrates strong cybersecurity practices with an overall score of 96/100. The organization has implemented comprehensive security controls across all categories, including multi-factor authentication, robust backup procedures, and regular security training. Key strengths include mature identity and access management, encrypted data protection, and well-documented incident response procedures.`
    };

    // Transform questions
    const questions = assessmentData.map(q => {
        const qInfo = questionMapping[q.qID] || {};
        const category = categoryMapping[q.qCat] || {};

        return {
            id: q.qID,
            questionNumber: qInfo.question_number || 'Unknown',
            questionText: qInfo.question_text || 'Question text not found',
            description: qInfo.description || '',
            category: category.category_name || 'Unknown Category',
            categoryNumber: category.category_number || 0,
            categoryId: q.qCat,
            response: q.qResponse,
            score: q.qScore,
            notes: q.qNotes || '',
            impactScore: qInfo.impact_score || 1,
            isRequired: q.qReq,
            isVerified: q.qVerified
        };
    });

    // Group by category
    const categoriesMap = {};
    questions.forEach(q => {
        if (!categoriesMap[q.categoryId]) {
            categoriesMap[q.categoryId] = {
                id: q.categoryId,
                name: q.category,
                number: q.categoryNumber,
                questions: [],
                totalScore: 0,
                maxScore: 0,
                percentScore: 0
            };
        }
        categoriesMap[q.categoryId].questions.push(q);
        categoriesMap[q.categoryId].totalScore += q.score;
        categoriesMap[q.categoryId].maxScore += (q.impactScore * 5); // Max control score is 5
    });

    // Calculate category percentages
    const categories = Object.values(categoriesMap).map(cat => {
        cat.percentScore = cat.maxScore > 0 ? Math.round((cat.totalScore / cat.maxScore) * 100) : 0;
        cat.questions.sort((a, b) => a.questionNumber - b.questionNumber);
        return cat;
    }).sort((a, b) => a.number - b.number);

    // Calculate risk distribution
    const riskCounts = { high: 0, moderate: 0, low: 0, na: 0 };
    questions.forEach(q => {
        if (q.score === 0) riskCounts.na++;
        else if (q.score >= 16) riskCounts.high++;
        else if (q.score >= 10) riskCounts.moderate++;
        else riskCounts.low++;
    });

    return {
        metadata,
        categories,
        questions,
        riskCounts
    };
}

// Generate HTML content matching the Python template structure
function generateHTML(data) {
    const { metadata, categories, questions, riskCounts } = data;
    const styles = document.getElementById('report-styles')?.textContent || '';

    let html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CyberPools Risk Assessment — ${metadata.memberName}</title>
    <style>
        ${styles}
    </style>
</head>
<body>

<!-- Cover Page -->
<div class="page cover-page">
    <div class="cover-logo">CYBERPOOLS</div>
    <div class="cover-title">Cyber Risk<br>Assessment Report</div>
    <div class="cover-subtitle">Comprehensive Security Analysis</div>

    <div class="cover-metadata">
        <div class="cover-metadata-item">
            <span class="cover-metadata-label">Member Organization:</span>
            <span class="cover-metadata-value">${metadata.memberName}</span>
        </div>
        <div class="cover-metadata-item">
            <span class="cover-metadata-label">Assessment Date:</span>
            <span class="cover-metadata-value">${metadata.assessmentDate}</span>
        </div>
        <div class="cover-metadata-item">
            <span class="cover-metadata-label">Report Date:</span>
            <span class="cover-metadata-value">${metadata.reportDate}</span>
        </div>
        <div class="cover-metadata-item">
            <span class="cover-metadata-label">Overall Score:</span>
            <span class="cover-metadata-value">${metadata.overallScore}% (Grade ${metadata.overallGrade})</span>
        </div>
    </div>
</div>

<!-- Executive Summary -->
<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <h1>Executive Summary</h1>

    <div class="executive-summary-content">
        <p>${metadata.executiveSummary}</p>
    </div>
</div>

<!-- Summary of Results -->
<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <h1>Summary of Results</h1>

    <!-- Overall Score Box - Full Width -->
    <div class="overall-score-box">
        <div class="overall-score">${metadata.overallScore}%</div>
        <div class="score-label">Overall Risk Score</div>
        <div class="overall-progress">
            <div class="overall-progress-track">
                <div class="overall-progress-fill" style="width: ${metadata.overallScore}%;"></div>
            </div>
        </div>
    </div>

    <!-- Risk Distribution Grid - 3 columns below -->
    <div class="risk-distribution-grid">
        <!-- High Risk -->
        <div class="risk-box high-risk">
            <div class="risk-number">${riskCounts.high}</div>
            <div class="risk-label">High Risk</div>
        </div>

        <!-- Moderate Risk -->
        <div class="risk-box moderate-risk">
            <div class="risk-number">${riskCounts.moderate}</div>
            <div class="risk-label">Moderate Risk</div>
        </div>

        <!-- Low Risk -->
        <div class="risk-box low-risk">
            <div class="risk-number">${riskCounts.low}</div>
            <div class="risk-label">Low Risk</div>
        </div>
    </div>

    <h2>Category Breakdown</h2>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>Category</th>
                    <th>Score</th>
                    <th>Questions</th>
                </tr>
            </thead>
            <tbody>
                ${categories.map(cat => `
                <tr>
                    <td>${cat.name}</td>
                    <td>${cat.percentScore}%</td>
                    <td>${cat.questions.length}</td>
                </tr>
                `).join('')}
            </tbody>
        </table>
    </div>
</div>

<!-- High Risk Findings -->
<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <h1>High Risk Findings</h1>

    ${questions.filter(q => q.score >= 16).length > 0 ? `
        <div class="findings-section">
            ${questions.filter(q => q.score >= 16).map(q => `
            <div class="finding-card finding-card--high">
                <div class="finding-card-title">${q.questionText}</div>
                <div class="finding-card-meta">Category: ${q.category} | Question ${q.questionNumber}</div>
                <div class="finding-card-status">
                    <div class="status-item">
                        <span class="status-label">Risk Score:</span>
                        <span class="badge badge-danger">${q.score}</span>
                    </div>
                </div>
                ${q.notes ? `<div class="finding-card-notes">${q.notes}</div>` : ''}
            </div>
            `).join('')}
        </div>
    ` : `
        <div class="info-box">
            <p>No high risk findings identified. Excellent work!</p>
        </div>
    `}
</div>

<!-- Categories (one per page) -->
${categories.map(cat => `
<div class="page">
    <div class="page-header">
        <div class="logo-text">CYBERPOOLS</div>
    </div>

    <div class="category-header">
        <div>
            <div class="category-number">Category ${cat.number}</div>
            <div class="category-name">${cat.name}</div>
        </div>
        <div class="category-score">${cat.percentScore}%</div>
    </div>

    ${cat.questions.map(q => {
        let riskClass = 'badge-success';
        let riskLabel = 'Low Risk';
        if (q.score === 0) {
            riskClass = 'badge-secondary';
            riskLabel = 'N/A';
        } else if (q.score >= 16) {
            riskClass = 'badge-danger';
            riskLabel = 'High Risk';
        } else if (q.score >= 10) {
            riskClass = 'badge-warning';
            riskLabel = 'Moderate Risk';
        }

        return `
        <div class="question-block">
            <div class="question-core">
                <div class="question-text">
                    <span class="question-number">Q${q.questionNumber}.</span>
                    ${q.questionText}
                    ${q.isRequired ? ' <span class="badge badge-secondary">Required</span>' : ''}
                </div>
                ${q.description ? `<div class="control-description">${q.description}</div>` : ''}

                <div class="question-status">
                    <div class="status-item">
                        <span class="status-label">Risk:</span>
                        <span class="badge ${riskClass}">${riskLabel}${q.score > 0 ? ` (${q.score})` : ''}</span>
                    </div>
                </div>

                ${q.notes ? `
                <div class="comments-section">
                    <span class="comments-label">Assessment Notes:</span>
                    <div class="comments-text">${q.notes}</div>
                </div>
                ` : ''}
            </div>
        </div>
        `;
    }).join('')}
</div>
`).join('')}

</body>
</html>`;

    return html;
}

// Generate PDF with Paged.js
async function generateWithPagedJS() {
    updateStatus('Generating PDF with Paged.js...', true);

    try {
        // Transform data
        const transformedData = transformData();

        // Generate HTML
        const htmlContent = generateHTML(transformedData);

        // Create a new window with the content
        const printWindow = window.open('', '_blank');
        printWindow.document.write(htmlContent);
        printWindow.document.close();

        // Wait for Paged.js to process
        setTimeout(() => {
            printWindow.print();
            updateStatus('✅ PDF preview opened! Use browser print dialog to save as PDF.');
        }, 2000);

    } catch (error) {
        updateStatus(`❌ Error: ${error.message}`);
        console.error('Paged.js error:', error);
    }
}

// Generate PDF with DocRaptor
async function generateWithDocRaptor() {
    updateStatus('Generating PDF with DocRaptor...', true);

    try {
        // Transform data
        const transformedData = transformData();

        // Generate HTML
        const htmlContent = generateHTML(transformedData);

        // Create DocRaptor request
        DocRaptor.createAndDownloadDoc(CONFIG.DOCRAPTOR_API_KEY, {
            test: CONFIG.TEST_MODE,
            type: "pdf",
            document_content: htmlContent,
            name: `CyberPools_Report_${transformedData.metadata.memberName.replace(/\s+/g, '_')}_${transformedData.metadata.reportDate}.pdf`,
            prince_options: {
                media: "print",
                baseurl: window.location.href
            }
        });

        updateStatus('✅ PDF generation started with DocRaptor! Check your downloads folder.');

    } catch (error) {
        updateStatus(`❌ Error: ${error.message}`);
        console.error('DocRaptor error:', error);
    }
}

// Auto-load data on page load
window.addEventListener('DOMContentLoaded', async () => {
    await preloadStyles();
    loadTestData();
});
