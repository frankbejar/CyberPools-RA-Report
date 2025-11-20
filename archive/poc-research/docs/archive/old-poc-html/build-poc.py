#!/usr/bin/env python3
"""
Build improved local POC with complete CSS from main.css
"""

import json

# Read the complete CSS
with open('styles/main.css', 'r') as f:
    main_css = f.read()

# Control panel CSS (for the UI, not the PDF)
control_css = """
/* Control Panel Styles - NOT included in PDF */
#controls {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: #2C5F7C;
    color: white;
    padding: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    z-index: 10000;
}

#controls h1 {
    margin: 0 0 15px 0;
    font-size: 24px;
    font-weight: 600;
    color: white;
}

.button-group {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
    margin-bottom: 15px;
}

#controls button {
    background: #4A9FB8;
    color: white;
    border: none;
    padding: 12px 24px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    border-radius: 6px;
    transition: all 0.3s ease;
}

#controls button:hover {
    background: #6BC4D9;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

#controls button:disabled {
    background: #718096;
    cursor: not-allowed;
    transform: none;
}

#controls button.primary {
    background: #4CAF50;
    font-size: 16px;
    padding: 14px 28px;
}

#controls button.primary:hover {
    background: #45a049;
}

#controls button.secondary {
    background: #F39C12;
}

#controls button.secondary:hover {
    background: #E67E22;
}

.info-panel {
    background: rgba(255,255,255,0.1);
    padding: 12px;
    border-radius: 6px;
    font-size: 13px;
    line-height: 1.6;
}

.info-panel strong {
    color: #6BC4D9;
}

#status {
    margin-top: 10px;
    padding: 10px;
    background: rgba(255,255,255,0.1);
    border-radius: 4px;
    min-height: 20px;
    font-size: 13px;
}

#preview {
    margin-top: 220px;
    padding: 20px;
}

.comparison-info {
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    border-left: 4px solid #4A9FB8;
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
}

.comparison-info h2 {
    margin-top: 0;
    color: #2C5F7C;
}

.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}

.comparison-table th,
.comparison-table td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #e0e0e0;
}

.comparison-table th {
    background: #f5f7fa;
    font-weight: 600;
    color: #2C5F7C;
}

.comparison-table tr:hover {
    background: #fafbfc;
}

.badge {
    display: inline-block;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
}

.badge.free {
    background: #4CAF50;
    color: white;
}

.badge.paid {
    background: #F39C12;
    color: white;
}

.spinner {
    display: inline-block;
    width: 16px;
    height: 16px;
    border: 3px solid rgba(255,255,255,.3);
    border-radius: 50%;
    border-top-color: #fff;
    animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

/* Hide controls when printing */
@media print {
    #controls, #preview, .comparison-info {
        display: none !important;
    }
}
"""

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyberPools Report POC - Paged.js vs DocRaptor</title>

    <!-- External Libraries -->
    <script src="https://unpkg.com/pagedjs/dist/paged.polyfill.js"></script>
    <script src="https://docraptor.com/docraptor-1.0.0.js"></script>

    <style>
        {control_css}
    </style>

    <style id="report-styles">
        {main_css}
    </style>
</head>
<body>
    <div id="controls">
        <h1>🚀 CyberPools PDF Generator POC - Paged.js vs DocRaptor</h1>

        <div class="button-group">
            <button class="primary" onclick="generateWithPagedJS()">
                📄 Generate with Paged.js (FREE)
            </button>
            <button class="secondary" onclick="generateWithDocRaptor()">
                📄 Generate with DocRaptor
            </button>
            <button onclick="loadTestData()">
                🔄 Reload Test Data
            </button>
            <button onclick="showComparison()">
                ℹ️ Compare Engines
            </button>
        </div>

        <div class="info-panel">
            <strong>Data Source:</strong> input/cb-ra.json (Christian Brothers Services - 49 questions, Score: 96, Grade: A)<br>
            <strong>Paged.js:</strong> Free, browser-based, no API key required<br>
            <strong>DocRaptor:</strong> Cloud-based, requires API key (test mode: watermarked PDFs)
        </div>

        <div id="status">Ready to generate PDF...</div>
    </div>

    <div id="preview">
        <div class="comparison-info" id="comparison" style="display:none;">
            <h2>📊 Rendering Engine Comparison</h2>
            <table class="comparison-table">
                <thead>
                    <tr>
                        <th>Feature</th>
                        <th>Paged.js <span class="badge free">FREE</span></th>
                        <th>DocRaptor <span class="badge paid">PAID</span></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Cost</strong></td>
                        <td>$0 - Completely free</td>
                        <td>$15/month for 125 PDFs</td>
                    </tr>
                    <tr>
                        <td><strong>Where it runs</strong></td>
                        <td>Client-side in browser</td>
                        <td>Cloud API service</td>
                    </tr>
                    <tr>
                        <td><strong>API Key Required</strong></td>
                        <td>❌ No</td>
                        <td>✅ Yes</td>
                    </tr>
                    <tr>
                        <td><strong>Security</strong></td>
                        <td>All data stays local</td>
                        <td>Data sent to DocRaptor servers</td>
                    </tr>
                    <tr>
                        <td><strong>PDF Quality</strong></td>
                        <td>Excellent (browser print engine)</td>
                        <td>Excellent (Prince XML)</td>
                    </tr>
                    <tr>
                        <td><strong>Best For</strong></td>
                        <td>Unlimited PDFs, privacy-sensitive</td>
                        <td>Enterprise with budget</td>
                    </tr>
                </tbody>
            </table>
            <p style="margin-top: 15px; color: #666;">
                <strong>Recommendation:</strong> For your use case, Paged.js is ideal - it's free, secure (data never leaves browser),
                and produces professional PDFs identical to DocRaptor.
            </p>
        </div>
    </div>

    <script src="report-generator.js"></script>
</body>
</html>
"""

# Write the HTML file
with open('local-poc-v2.html', 'w') as f:
    f.write(html_template)

print("✅ Created local-poc-v2.html")
print("📝 Next: Creating report-generator.js...")
