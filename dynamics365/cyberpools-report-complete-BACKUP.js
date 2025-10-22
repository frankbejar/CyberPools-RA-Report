/**
 * ========================================================================
 * CyberPools Risk Assessment Report Generator for Dynamics 365
 * ========================================================================
 *
 * Complete standalone version - ready to deploy as single Web Resource
 *
 * Version: 1.0.0
 * Date: 2025-10-21
 * Author: CyberPools Development Team
 *
 * QUICK START:
 * 1. Upload this file as Web Resource in Dynamics 365
 * 2. Update DOCRAPTOR_API_KEY below (line 27)
 * 3. Upload mapping JSON files as Web Resources (or use embedded option)
 * 4. Add button to Risk Assessment form
 * 5. Button calls: CyberPoolsReport.generateReport(executionContext)
 *
 * See DEPLOYMENT_GUIDE.md for detailed instructions
 * ========================================================================
 */

var CyberPoolsReport = CyberPoolsReport || {};

(function() {
    'use strict';

    // ==================== CONFIGURATION ====================
    const CONFIG = {
        // IMPORTANT: Replace with your production DocRaptor API key!
        DOCRAPTOR_API_KEY: 'Uej3BuDjlcc3vx8z5lfK',

        // TEST_MODE: true = watermarked PDFs (unlimited free)
        // TEST_MODE: false = production PDFs (uses quota, no watermark)
        TEST_MODE: false,

        // Web Resource URLs for mapping files
        // If you uploaded mappings as Web Resources, use these paths:
        QUESTION_MAPPING_URL: '/WebResources/new_/mappings/question_mapping.json',
        CATEGORY_MAPPING_URL: '/WebResources/new_/mappings/category_mapping.json',

        // Alternative: Use embedded mappings (see bottom of file)
        // Set to true if you didn't upload mapping files separately
        USE_EMBEDDED_MAPPINGS: false,

        // Dynamics 365 field schema names (update if yours are different)
        FIELD_NAMES: {
            json: 'new_json',
            service: 'new_service',
            totalScore: 'new_totalscore',
            totalGrade: 'new_totalgrade',
            template: 'new_template',
            executiveSummary: 'new_executivesummary'
        }
    };

    // ==================== MAIN ENTRY POINT ====================

    /**
     * Main function - call this from Dynamics 365 button
     * @param {Object} executionContext - Dynamics 365 execution context
     */
    CyberPoolsReport.generateReport = async function(executionContext) {
        console.log('CyberPools Report Generator starting...');

        try {
            // Show progress indicator
            Xrm.Utility.showProgressIndicator("Generating PDF report...");

            // Get form context
            const formContext = executionContext.getFormContext();

            // Step 1: Get Risk Assessment data from current record
            console.log('Step 1: Getting assessment data...');
            const assessmentData = await getRiskAssessmentData(formContext);

            // Step 2: Get Member information from parent Service record
            console.log('Step 2: Getting member data...');
            const memberData = await getMemberData(assessmentData.serviceId);

            // Step 3: Get Executive Summary (if field exists)
            console.log('Step 3: Getting executive summary...');
            const executiveSummary = getExecutiveSummary(formContext);

            // Step 4: Load mapping files
            console.log('Step 4: Loading mappings...');
            let questionMapping, categoryMapping;

            if (CONFIG.USE_EMBEDDED_MAPPINGS) {
                questionMapping = EMBEDDED_QUESTION_MAPPING || {};
                categoryMapping = EMBEDDED_CATEGORY_MAPPING || {};
            } else {
                [questionMapping, categoryMapping] = await Promise.all([
                    loadMappingFile(CONFIG.QUESTION_MAPPING_URL),
                    loadMappingFile(CONFIG.CATEGORY_MAPPING_URL)
                ]);
            }

            // Step 5: Transform data
            console.log('Step 5: Transforming data...');
            const transformedData = transformData(
                assessmentData,
                memberData,
                executiveSummary,
                questionMapping,
                categoryMapping
            );

            // Step 6: Generate HTML
            console.log('Step 6: Generating HTML...');
            const htmlContent = generateHTML(transformedData);

            // Step 7: Generate PDF via DocRaptor
            console.log('Step 7: Generating PDF...');
            await generatePDFWithDocRaptor(htmlContent, transformedData.metadata);

            // Success!
            Xrm.Utility.closeProgressIndicator();

            Xrm.Navigation.openAlertDialog({
                text: "PDF report generated successfully and downloaded to your browser!",
                title: "Success"
            });

            console.log('Report generation complete!');

        } catch (error) {
            Xrm.Utility.closeProgressIndicator();
            console.error('Report generation error:', error);

            Xrm.Navigation.openErrorDialog({
                message: "Failed to generate report: " + error.message,
                details: error.stack || error.toString()
            });
        }
    };

    // ==================== DATA RETRIEVAL FUNCTIONS ====================

    /**
     * Get Risk Assessment data from current form
     */
    async function getRiskAssessmentData(formContext) {
        const recordId = formContext.data.entity.getId().replace(/[{}]/g, '');

        // Get the JSON field that contains all questions
        const jsonField = formContext.getAttribute(CONFIG.FIELD_NAMES.json);
        const questionsJSON = jsonField ? jsonField.getValue() : null;

        if (!questionsJSON) {
            throw new Error("No assessment data found. Please complete the assessment first.");
        }

        // Parse JSON
        let questions;
        try {
            questions = JSON.parse(questionsJSON);
        } catch (e) {
            throw new Error("Invalid JSON data in assessment: " + e.message);
        }

        // Get other fields from form
        return {
            recordId: recordId,
            serviceId: formContext.getAttribute(CONFIG.FIELD_NAMES.service)?.getValue()?.[0]?.id,
            questions: questions,
            totalScore: formContext.getAttribute(CONFIG.FIELD_NAMES.totalScore)?.getValue() || 0,
            totalGrade: formContext.getAttribute(CONFIG.FIELD_NAMES.totalGrade)?.getValue() || 'N/A',
            createdOn: formContext.getAttribute("createdon")?.getValue() || new Date(),
            createdBy: formContext.getAttribute("createdby")?.getValue()?.[0]?.name || 'Unknown',
            template: formContext.getAttribute(CONFIG.FIELD_NAMES.template)?.getValue() || 'Version 4.0'
        };
    }

    /**
     * Get Member data from parent Service record
     */
    async function getMemberData(serviceId) {
        if (!serviceId) {
            console.warn('No service ID found, using defaults');
            return {
                memberName: 'Unknown Organization',
                poolName: 'Unknown Pool',
                pocName: 'Unknown',
                pocEmail: ''
            };
        }

        // Clean the GUID
        serviceId = serviceId.replace(/[{}]/g, '');

        try {
            // Retrieve Service record with Member and Pool lookups
            const result = await Xrm.WebApi.retrieveRecord(
                "new_service",
                serviceId,
                "?$select=new_name&$expand=new_Member($select=new_name,new_poc,emailaddress1),new_Pool($select=new_name)"
            );

            return {
                memberName: result.new_Member?.new_name || 'Unknown Organization',
                poolName: result.new_Pool?.new_name || 'Unknown Pool',
                pocName: result.new_Member?.new_poc?.[0]?.name || 'Unknown',
                pocEmail: result.new_Member?.emailaddress1 || ''
            };
        } catch (error) {
            console.error('Error retrieving member data:', error);
            return {
                memberName: 'Unknown Organization',
                poolName: 'Unknown Pool',
                pocName: 'Unknown',
                pocEmail: ''
            };
        }
    }

    /**
     * Get executive summary from form (if field exists)
     */
    function getExecutiveSummary(formContext) {
        const summaryField = formContext.getAttribute(CONFIG.FIELD_NAMES.executiveSummary);
        if (summaryField) {
            return summaryField.getValue() || '';
        }
        return '';
    }

    /**
     * Load mapping JSON file from Web Resources
     */
    async function loadMappingFile(webResourceUrl) {
        try {
            const response = await fetch(webResourceUrl);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Error loading mapping file from ${webResourceUrl}:`, error);
            console.warn('Falling back to empty mapping. Report may have incomplete data.');
            return {};
        }
    }

    // ==================== DATA TRANSFORMATION ====================

    /**
     * Transform CRM data to report format (matches Python logic)
     */
    function transformData(assessmentData, memberData, executiveSummary, questionMapping, categoryMapping) {
        console.log('Transforming data for', assessmentData.questions.length, 'questions');

        const questions = assessmentData.questions;

        // Calculate risk distribution
        const riskDist = { high: 0, moderate: 0, low: 0 };
        questions.forEach(q => {
            if (q.qResponse !== 0) {
                const riskLevel = getRiskLevel(q.qScore);
                riskDist[riskLevel]++;
            }
        });

        // Group questions by category
        const categoriesDict = {};
        questions.forEach(q => {
            const catId = String(q.qCat);
            if (!categoriesDict[catId]) {
                categoriesDict[catId] = [];
            }
            categoriesDict[catId].push(q);
        });

        // Build categories array
        const categories = [];

        Object.entries(categoriesDict).forEach(([catId, catQuestions]) => {
            const catInfo = categoryMapping[catId] || {
                number: '0.0',
                name: `Unknown Category (${catId})`
            };

            const catScore = calculateCategoryScore(catQuestions, questionMapping);

            // Transform questions
            const questionsList = catQuestions.map(q => {
                const qInfo = questionMapping[q.qID] || {
                    number: '0.0',
                    text: `Unknown Question (${q.qID.substring(0, 8)}...)`,
                    control_description: '',
                    impact_score: 3
                };

                return {
                    number: qInfo.number,
                    text: qInfo.text,
                    control_description: qInfo.control_description || '',
                    control_status: q.qResponse,
                    control_status_text: getStatusText(q.qResponse),
                    impact_score: qInfo.impact_score || 0,
                    risk_score: q.qScore,
                    risk_level: getRiskLevel(q.qScore),
                    comments: q.qNotes || ''
                };
            });

            // Sort questions by number
            questionsList.sort((a, b) => compareNumbers(a.number, b.number));

            categories.push({
                number: catInfo.number,
                name: catInfo.name,
                score: catScore,
                overview: catInfo.overview || ``,
                importance: catInfo.importance || ``,
                questions: questionsList
            });
        });

        // Sort categories by number
        categories.sort((a, b) => compareNumbers(a.number, b.number));

        // Extract cyber requirements (exclude insurance question)
        const EXCLUDED_CYBER_REQUIREMENTS = new Set(['b032c58a-fc8f-f011-b4cb-0022480aaebb']);
        const cyberRequirements = questions
            .filter(q => q.qReq && !EXCLUDED_CYBER_REQUIREMENTS.has(q.qID))
            .map(q => {
                const qInfo = questionMapping[q.qID] || { text: 'Unknown Requirement' };
                return {
                    question: qInfo.text,
                    compliance: q.qResponse === 1
                };
            });

        // Format date
        const assessmentDate = new Date(assessmentData.createdOn);
        const month = assessmentDate.getMonth() + 1;
        const day = assessmentDate.getDate();
        const year = assessmentDate.getFullYear();
        const formattedDate = month + '/' + day + '/' + year;

        return {
            metadata: {
                member_name: memberData.memberName,
                assessment_date: formattedDate,
                conducted_by: assessmentData.createdBy,
                member_contact: memberData.pocName,
                version: assessmentData.template,
                pool_name: memberData.poolName
            },
            executive_summary_raw: executiveSummary,
            executive_summary_html: executiveSummary,
            scoring: {
                overall_score: Math.round(assessmentData.totalScore),
                overall_grade: assessmentData.totalGrade,
                risk_distribution: riskDist
            },
            categories: categories,
            cyber_requirements: cyberRequirements,
            has_high_risk: questions.some(q => q.qScore >= 16)
        };
    }

    // ==================== HELPER FUNCTIONS ====================

    function getStatusText(responseValue) {
        const statusMap = {
            1: "Fully Implemented",
            3: "Partially Implemented",
            5: "Not Implemented",
            0: "Not Applicable"
        };
        return statusMap[responseValue] || "Unknown";
    }

    function getRiskLevel(riskScore) {
        if (riskScore <= 9) return "low";
        if (riskScore <= 15) return "moderate";
        return "high";
    }

    function calculateCategoryScore(questions, questionMapping) {
        const applicable = questions.filter(q => q.qResponse !== 0);
        if (applicable.length === 0) return 100;

        const actualScore = applicable.reduce((sum, q) => sum + q.qScore, 0);
        const minScore = applicable.reduce((sum, q) => {
            const impact = questionMapping[q.qID]?.impact_score || 3;
            return sum + (impact * 1);
        }, 0);
        const maxScore = applicable.reduce((sum, q) => {
            const impact = questionMapping[q.qID]?.impact_score || 3;
            return sum + (impact * 5);
        }, 0);

        if (maxScore === minScore) return 100;
        return Math.round((1 - (actualScore - minScore) / (maxScore - minScore)) * 100);
    }

    function compareNumbers(a, b) {
        const aParts = a.split('.').map(n => parseInt(n) || 0);
        const bParts = b.split('.').map(n => parseInt(n) || 0);

        for (let i = 0; i < Math.max(aParts.length, bParts.length); i++) {
            const aVal = aParts[i] || 0;
            const bVal = bParts[i] || 0;
            if (aVal !== bVal) return aVal - bVal;
        }
        return 0;
    }

    function escapeHtml(text) {
        if (!text) return '';
        return String(text)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    // ==================== HTML GENERATION ====================

    function generateHTML(data) {
        console.log('Generating complete HTML document...');

        return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Risk Assessment Report - ${escapeHtml(data.metadata.member_name)}</title>
    <style>${getInlineCSS()}</style>
</head>
<body>
${generateCoverPage(data)}
${generateExecutiveSummary(data)}
${generateResultsSummary(data)}
${generateHowToReadPage()}
${data.has_high_risk ? generateHighRiskFindings(data) : ''}
${data.categories.map(cat => generateCategoryPage(cat)).join('\n')}
${generateCyberRequirements(data)}
</body>
</html>`;
    }

    // PAGE GENERATORS

    function generateCoverPage(data) {
        return `<div class="page cover-page">
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

        return `<div class="page">
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

        return `<div class="page">
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
</div>
`;
    }

    function generateHowToReadPage() {
        return `<div class="page">
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
        const highRiskItems = [];

        data.categories.forEach(cat => {
            cat.questions.forEach(q => {
                if (q.risk_score >= 16) {
                    highRiskItems.push({
                        category: cat.name,
                        question: q
                    });
                }
            });
        });

        if (highRiskItems.length === 0) return '';

        const items = highRiskItems.map(item => `
        <div class="high-risk-item">
            <strong>${escapeHtml(item.category)} - ${escapeHtml(item.question.number)}</strong>
            <p>${escapeHtml(item.question.text)}</p>
            ${item.question.comments ? `<p><em>Notes: ${escapeHtml(item.question.comments)}</em></p>` : ''}
        </div>
    `).join('');

        return `<div class="page">
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

    function generateCategoryPage(cat) {
        const questions = cat.questions.map(q => generateQuestion(q)).join('');

        return `<div class="page category-page">
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

        return `<div class="page">
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

    // ==================== DOCRAPTOR PDF GENERATION ====================

    /**
     * Generate PDF using DocRaptor API
     */
    async function generatePDFWithDocRaptor(htmlContent, metadata) {
        console.log('Calling DocRaptor API...');

        const fileName = metadata.member_name.replace(/[^a-z0-9]/gi, '_') +
                        '_Risk_Assessment_' +
                        metadata.assessment_date.replace(/\//g, '-') +
                        '.pdf';

        // Use DocRaptor JavaScript library
        if (typeof DocRaptor === 'undefined') {
            throw new Error('DocRaptor library not loaded. Please include: https://docraptor.com/docraptor-1.0.0.js');
        }

        try {
            await DocRaptor.createAndDownloadDoc(CONFIG.DOCRAPTOR_API_KEY, {
                name: fileName,
                test: CONFIG.TEST_MODE,
                document_type: "pdf",
                document_content: htmlContent,
                javascript: false, // We don't need JS execution for static content
                prince_options: {
                    media: "print",
                    baseurl: window.location.origin
                }
            });

            console.log('PDF generated successfully:', fileName);
        } catch (error) {
            console.error('DocRaptor API error:', error);
            throw new Error('DocRaptor failed to generate PDF. Check API key and quota.');
        }
    }

    // ==================== CSS STYLES (MINIFIED) ====================

    function getInlineCSS() {
        // Minified CSS based on your main.css and print_docraptor.css
        return `:root{--primary-navy:#2C5F7C;--primary-teal:#4A9FB8;--accent-cyan:#6BC4D9;--risk-high:#C10000;--risk-moderate:#F39C12;--risk-low:#4CAF50;--gray-dark:#333;--gray-medium:#666;--gray-light:#CCC;--gray-bg:#F5F7FA;--white:#FFF}*{margin:0;padding:0;box-sizing:border-box}body{font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:13px;line-height:1.5;color:var(--gray-dark);background:#fff;padding:0}@page{size:letter;margin:0.5in}@page{@top-left{content:"CYBERPOOLS"}@bottom-right{content:counter(page)}}.page{width:8.5in;min-height:11in;padding:0.35in 0.45in;background:#fff;page-break-after:always;position:relative}.page:last-child{page-break-after:auto}.page-header{display:flex;justify-content:space-between;align-items:center;padding-bottom:12px;border-bottom:2px solid var(--primary-teal);margin-bottom:25px}.logo-text{font-size:22px;font-weight:700;color:var(--primary-navy);letter-spacing:1px}.cover-page{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:linear-gradient(135deg,var(--primary-navy),var(--primary-teal));color:#fff;padding:60px 40px}.cover-logo{font-size:56px;font-weight:700;letter-spacing:4px;margin-bottom:40px}.cover-title{font-size:48px;font-weight:300;margin-bottom:20px;line-height:1.2}.cover-subtitle{font-size:22px;font-weight:400;opacity:0.9;margin-bottom:50px}.cover-metadata{background:rgba(255,255,255,0.1);padding:20px 25px;border-radius:6px;margin-top:40px;text-align:left;width:100%;max-width:500px}.cover-metadata-item{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.2)}.cover-metadata-item:last-child{border-bottom:none}.cover-metadata-label{font-weight:600;opacity:0.9}.cover-metadata-value{opacity:0.95;text-align:right}h1{font-size:28px;font-weight:700;color:var(--primary-navy);margin-bottom:18px;padding-left:12px;border-left:5px solid var(--primary-teal);line-height:1.2}h2{font-size:18px;font-weight:600;color:var(--primary-navy);margin:15px 0 10px}h3{font-size:16px;font-weight:600;color:var(--primary-navy);margin:15px 0 8px}h4{font-size:14px;font-weight:600;color:var(--primary-navy);margin:12px 0 8px}p{margin-bottom:10px;text-align:justify}.executive-summary-content{background:#fff;border-left:4px solid var(--primary-teal);padding:18px;margin:18px 0;font-size:14px;line-height:1.7}.executive-summary-content p{margin-bottom:16px}.executive-summary-content strong,.executive-summary-content b{font-weight:700;color:var(--primary-navy)}.executive-summary-content em,.executive-summary-content i{font-style:italic}.executive-summary-placeholder{background:var(--gray-bg);border:2px dashed var(--gray-light);border-radius:6px;padding:18px;margin:18px 0;font-style:italic;color:var(--gray-medium)}.overall-score-box{background:var(--gray-bg);border:2px solid var(--gray-light);border-left:4px solid var(--primary-teal);border-radius:6px;padding:28px 24px;text-align:center;margin-bottom:24px}.overall-score{font-size:36pt;font-weight:700;color:var(--primary-navy);line-height:1;margin-bottom:5px}.score-label{font-size:9px;color:var(--gray-medium);font-weight:600;text-transform:uppercase;letter-spacing:0.6px;margin-bottom:10px}.overall-progress-track{position:relative;height:12px;border-radius:6px;background:var(--gray-bg);border:1px solid var(--gray-light);width:100%;overflow:hidden}.overall-progress-fill{height:100%;background:linear-gradient(90deg,var(--primary-teal),var(--primary-navy));border-radius:6px}.risk-distribution-grid{display:flex;gap:12px;margin:0 0 24px 0}.risk-box{background:var(--gray-bg);border:2px solid var(--gray-light);border-radius:6px;padding:28px 24px;text-align:center;flex:1}.risk-box.high-risk{border-left:4px solid var(--risk-high)}.risk-box.moderate-risk{border-left:4px solid var(--risk-moderate)}.risk-box.low-risk{border-left:4px solid var(--risk-low)}.risk-number{font-size:32pt;font-weight:700;color:var(--primary-navy);line-height:1;margin-bottom:5px}.risk-label{font-size:9px;color:var(--gray-medium);font-weight:600;text-transform:uppercase;letter-spacing:0.5px}.guide-grid{display:grid;grid-template-columns:1fr;gap:16px;margin:20px 0}.guide-item{display:flex;align-items:flex-start;padding:16px;background:#fff;border:1px solid var(--gray-light);border-radius:6px}.guide-number{width:36px;height:36px;background:var(--primary-teal);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;flex-shrink:0;margin-right:16px}.guide-content h4{margin:0 0 6px;color:var(--primary-navy);font-size:14px}.guide-content p{margin:0;font-size:13px;color:var(--gray-medium)}.high-risk-section{background:#fdeaea;border:2px solid var(--risk-high);border-radius:6px;padding:24px;margin:24px 0}.high-risk-header{font-size:16pt;font-weight:700;color:var(--risk-high);margin-bottom:20px}.high-risk-item{background:#fff;border-radius:5px;padding:16px 20px;margin-bottom:16px;border-left:4px solid var(--risk-high)}.high-risk-item:last-child{margin-bottom:0}.category-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;padding:24px;background:linear-gradient(135deg,var(--primary-navy),var(--primary-teal));color:#fff;border-radius:6px}.category-number{font-size:13pt;font-weight:700;opacity:0.9;margin-bottom:4px}.category-name{font-size:18pt;font-weight:700;line-height:1.2}.category-score{font-size:32pt;font-weight:700;line-height:1}.category-overview{background:var(--gray-bg);padding:18px 20px;border-radius:5px;margin:18px 0;border-left:4px solid var(--primary-teal)}.question-block{margin-bottom:24px;padding-bottom:20px;border-bottom:1px solid var(--gray-light);page-break-inside:avoid}.question-block:last-child{border-bottom:none}.question-text{font-weight:600;color:var(--gray-dark);margin-bottom:10px;font-size:14px;line-height:1.4}.question-number{font-weight:700;color:var(--primary-navy);margin-right:5px}.control-description{background:var(--gray-bg);padding:10px 12px;border-radius:4px;margin-bottom:10px;font-size:11px;color:var(--gray-medium);font-style:italic}.question-status{display:flex;gap:24px;margin:20px 0;flex-wrap:wrap}.status-item{display:flex;align-items:center;gap:8px}.status-label{font-weight:600;color:var(--gray-medium);font-size:11px}.badge{display:inline-block;padding:3px 10px;border-radius:10px;font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px;white-space:nowrap}.badge-success{background:rgba(76,175,80,0.1);color:var(--risk-low);border:1px solid var(--risk-low)}.badge-warning{background:rgba(243,156,18,0.1);color:#c87f0a;border:1px solid var(--risk-moderate)}.badge-danger{background:rgba(193,0,0,0.1);color:var(--risk-high);border:1px solid var(--risk-high)}.badge-secondary{background:rgba(204,204,204,0.2);color:var(--gray-medium);border:1px solid var(--gray-light)}.comments-section{margin-top:12px}.comments-label{font-weight:600;color:var(--gray-dark);margin-bottom:6px;display:block;font-size:12px}.comments-text{background:var(--gray-bg);padding:10px 12px;border-radius:4px;border-left:3px solid var(--primary-teal);color:var(--gray-dark);line-height:1.5;font-size:12px}table{width:100%;border-collapse:collapse;margin:15px 0;font-size:12px}thead{background-color:var(--primary-navy);color:#fff}th{padding:10px 12px;text-align:left;font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:0.5px;border:1px solid var(--primary-navy)}td{padding:14px 16px;border:1px solid var(--gray-light)}tbody tr:nth-child(even){background-color:var(--gray-bg)}.compliance-yes{color:var(--risk-low);font-weight:700;font-size:14px}.compliance-no{color:var(--risk-high);font-weight:700;font-size:14px}.text-center{text-align:center}`;
    }

    // ==================== EMBEDDED MAPPINGS (OPTIONAL) ====================

    // If you set USE_EMBEDDED_MAPPINGS = true, define these objects:
    // Copy from your mapping JSON files

    var EMBEDDED_QUESTION_MAPPING = {};
    var EMBEDDED_CATEGORY_MAPPING = {};

    // Example structure (replace with your actual data):
    /*
    EMBEDDED_QUESTION_MAPPING = {
        "4c466f03-9478-f011-b4cb-000d3a34656f": {
            "number": "1.1",
            "text": "Does the organization enforce multi-factor authentication?",
            "control_description": "MFA adds an extra layer of security...",
            "impact_score": 5
        },
        // ... more questions
    };

    EMBEDDED_CATEGORY_MAPPING = {
        "772120001": {
            "number": "1.0",
            "name": "Access Control",
            "overview": "This category evaluates...",
            "importance": "Access control is critical because..."
        },
        // ... more categories
    };
    */

})();

// ========================================================================
// END OF CYBERPOOLS REPORT GENERATOR
// ========================================================================

console.log('CyberPools Report Generator loaded successfully. Version 1.0.0');
console.log('Usage: CyberPoolsReport.generateReport(executionContext)');
