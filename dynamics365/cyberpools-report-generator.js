/**
 * CyberPools Risk Assessment Report Generator - Dynamics 365 Web Resource
 *
 * This JavaScript file generates PDF reports directly from Dynamics 365 using DocRaptor API.
 *
 * Setup Instructions:
 * 1. Upload this file as a Web Resource in Dynamics 365
 * 2. Upload category_mapping.json and question_mapping.json as Web Resources
 * 3. Add a ribbon button or form button that calls: CyberPoolsReport.generateReport(executionContext)
 * 4. Configure your DocRaptor API key in the configuration below
 *
 * @version 1.0.0
 */

var CyberPoolsReport = CyberPoolsReport || {};

(function() {
    'use strict';

    // ==================== CONFIGURATION ====================
    const CONFIG = {
        DOCRAPTOR_API_KEY: 'Uej3BuDjlcc3vx8z5lfK', // Replace with your production key
        TEST_MODE: false, // Set to false for production PDFs (no watermark)

        // Web Resource paths for mapping files
        QUESTION_MAPPING_URL: 'new_/mappings/question_mapping.json',
        CATEGORY_MAPPING_URL: 'new_/mappings/category_mapping.json',

        // Boilerplate text
        BOILERPLATE: {
            how_to_read: {
                title: "How to Read This Report",
                intro: "This report provides a comprehensive assessment of your organization's cybersecurity posture..."
            }
        }
    };

    // ==================== MAIN ENTRY POINT ====================

    /**
     * Main function called from Dynamics 365 button
     * @param {Object} executionContext - Dynamics 365 execution context
     */
    CyberPoolsReport.generateReport = async function(executionContext) {
        try {
            // Show loading indicator
            Xrm.Utility.showProgressIndicator("Generating PDF report...");

            // Get form context
            const formContext = executionContext.getFormContext();

            // Get Risk Assessment data
            const assessmentData = await getRiskAssessmentData(formContext);

            // Get Member information from parent Service record
            const memberData = await getMemberData(assessmentData.serviceId);

            // Get Executive Summary (if exists in a field)
            const executiveSummary = getExecutiveSummary(formContext);

            // Load mapping files
            const [questionMapping, categoryMapping] = await Promise.all([
                loadMappingFile(CONFIG.QUESTION_MAPPING_URL),
                loadMappingFile(CONFIG.CATEGORY_MAPPING_URL)
            ]);

            // Transform data (same logic as Python)
            const transformedData = transformData(
                assessmentData,
                memberData,
                executiveSummary,
                questionMapping,
                categoryMapping
            );

            // Generate HTML
            const htmlContent = generateHTML(transformedData);

            // Generate PDF via DocRaptor
            await generatePDFWithDocRaptor(htmlContent, transformedData.metadata);

            Xrm.Utility.closeProgressIndicator();

            // Show success message
            Xrm.Navigation.openAlertDialog({
                text: "PDF report generated successfully and downloaded to your browser!",
                title: "Success"
            });

        } catch (error) {
            Xrm.Utility.closeProgressIndicator();
            console.error('Report generation error:', error);

            Xrm.Navigation.openErrorDialog({
                message: "Failed to generate report: " + error.message,
                details: error.stack
            });
        }
    };

    // ==================== DATA RETRIEVAL ====================

    /**
     * Get Risk Assessment data from current form
     */
    async function getRiskAssessmentData(formContext) {
        const recordId = formContext.data.entity.getId().replace(/[{}]/g, '');

        // Get the JSON field that contains all questions
        const jsonField = formContext.getAttribute("new_json");
        const questionsJSON = jsonField ? jsonField.getValue() : null;

        if (!questionsJSON) {
            throw new Error("No assessment data found. Please complete the assessment first.");
        }

        // Parse JSON
        const questions = JSON.parse(questionsJSON);

        // Get other fields from form
        return {
            recordId: recordId,
            serviceId: formContext.getAttribute("new_service")?.getValue()?.[0]?.id,
            questions: questions,
            totalScore: formContext.getAttribute("new_totalscore")?.getValue() || 0,
            totalGrade: formContext.getAttribute("new_totalgrade")?.getValue() || 'N/A',
            createdOn: formContext.getAttribute("createdon")?.getValue() || new Date(),
            createdBy: formContext.getAttribute("createdby")?.getValue()?.[0]?.name || 'Unknown',
            template: formContext.getAttribute("new_template")?.getValue() || 'Version 4.0'
        };
    }

    /**
     * Get Member data from parent Service record
     */
    async function getMemberData(serviceId) {
        if (!serviceId) {
            return {
                memberName: 'Unknown Organization',
                poolName: 'Unknown Pool',
                pocName: 'Unknown',
                pocEmail: ''
            };
        }

        // Clean the GUID
        serviceId = serviceId.replace(/[{}]/g, '');

        // Retrieve Service record with Member lookup
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
    }

    /**
     * Get executive summary from form (if field exists)
     */
    function getExecutiveSummary(formContext) {
        // Check if executive summary field exists
        const summaryField = formContext.getAttribute("new_executivesummary");
        if (summaryField) {
            return summaryField.getValue() || '';
        }
        return '';
    }

    /**
     * Load mapping JSON file from Web Resources
     */
    async function loadMappingFile(webResourceName) {
        try {
            const response = await fetch(`/WebResources/${webResourceName}`);
            if (!response.ok) {
                throw new Error(`Failed to load ${webResourceName}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Error loading ${webResourceName}:`, error);
            // Return empty mapping if file not found
            return {};
        }
    }

    // ==================== DATA TRANSFORMATION ====================

    /**
     * Transform CRM data to report format (matches Python logic)
     */
    function transformData(assessmentData, memberData, executiveSummary, questionMapping, categoryMapping) {
        console.log('Transforming data...');

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
        const sectionScores = {};

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
                overview: catInfo.overview || `Overview for ${catInfo.name}`,
                importance: catInfo.importance || `Importance of ${catInfo.name}`,
                questions: questionsList
            });

            sectionScores[catInfo.number] = {
                name: catInfo.name,
                score: catScore
            };
        });

        // Sort categories by number
        categories.sort((a, b) => compareNumbers(a.number, b.number));

        // Extract cyber requirements
        const cyberRequirements = questions
            .filter(q => q.qReq && q.qID !== 'b032c58a-fc8f-f011-b4cb-0022480aaebb')
            .map(q => {
                const qInfo = questionMapping[q.qID] || { text: 'Unknown Requirement' };
                return {
                    question: qInfo.text,
                    compliance: q.qResponse === 1
                };
            });

        // Format date
        const assessmentDate = new Date(assessmentData.createdOn);
        const formattedDate = `${assessmentDate.getMonth() + 1}/${assessmentDate.getDate()}/${assessmentDate.getFullYear()}`;

        return {
            metadata: {
                member_name: memberData.memberName,
                assessment_date: formattedDate,
                conducted_by: assessmentData.createdBy,
                member_contact: memberData.pocName,
                version: assessmentData.template
            },
            executive_summary_raw: executiveSummary,
            executive_summary_html: executiveSummary, // Already HTML from rich text field
            scoring: {
                overall_score: Math.round(assessmentData.totalScore),
                overall_grade: assessmentData.totalGrade,
                risk_distribution: riskDist,
                section_scores: sectionScores
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

    // ==================== HTML GENERATION ====================
    // (Continued in next part due to length...)

