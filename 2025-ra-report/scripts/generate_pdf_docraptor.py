#!/usr/bin/env python3
"""
DocRaptor-based HTML → PDF renderer for CyberPools reports.

DocRaptor uses Prince XML engine which has excellent support for:
- CSS Paged Media (@page with margin boxes)
- Page breaks and orphan/widow control
- Running headers/footers with page numbers
- Print-specific CSS features

Setup:
    pip install docraptor

Usage:
    from scripts.generate_pdf_docraptor import DocRaptorPDF
    renderer = DocRaptorPDF(api_key="YOUR_API_KEY")
    renderer.render_html_to_pdf(html, Path("output.pdf"), test_mode=True)

Free tier:
    - Use test_mode=True for unlimited test documents (watermarked)
    - 5 free documents/month in production mode
    - Then $15/month for 125 documents or pay-per-document

Get API key:
    https://docraptor.com/signup
"""

from __future__ import annotations
from pathlib import Path
from typing import Optional
import docraptor
import logging

logger = logging.getLogger(__name__)


class DocRaptorPDF:
    """
    Renders HTML to PDF using DocRaptor API (Prince XML engine).

    Advantages over Playwright/WeasyPrint:
    - Better CSS paged media support (@page margin boxes for headers/footers)
    - Superior page break handling
    - Native support for running headers/footers with page numbers
    - Better widow/orphan control
    - Excellent gradient and modern CSS support
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        javascript: bool = False,
        prince_options: Optional[dict] = None,
    ) -> None:
        """
        Initialize DocRaptor renderer.

        Args:
            api_key: DocRaptor API key (or set DOCRAPTOR_API_KEY env var)
            javascript: Enable JavaScript rendering (default: False for security)
            prince_options: Additional Prince XML options
                Examples:
                - {'profile': 'PDF/A-1b'} for archival PDFs
                - {'pdf_title': 'My Report'} for PDF metadata
        """
        self.api_key = api_key
        self.javascript = javascript
        self.prince_options = prince_options or {}

        if not self.api_key:
            raise ValueError(
                "DocRaptor API key required. Get one at https://docraptor.com/signup\n"
                "Pass api_key parameter or set DOCRAPTOR_API_KEY environment variable"
            )

    def render_html_to_pdf(
        self,
        html: str,
        output_pdf: Path,
        test_mode: bool = True,
        assets_dir: Optional[Path] = None,
    ) -> None:
        """
        Convert HTML to PDF using DocRaptor API.

        Args:
            html: HTML content (must be complete document with <html>, <head>, <body>)
            output_pdf: Path where PDF will be saved
            test_mode: If True, generates watermarked test PDF (unlimited free)
                      If False, counts against your document quota
            assets_dir: Directory containing assets (images, CSS, fonts)
                       Note: For DocRaptor to access local files, you must either:
                       1. Inline all CSS/images (recommended)
                       2. Use absolute URLs to publicly accessible assets
                       3. Use data URIs for images
        """
        output_pdf.parent.mkdir(parents=True, exist_ok=True)

        # Ensure HTML has proper DOCTYPE and encoding
        if not html.strip().startswith('<!DOCTYPE'):
            html = '<!DOCTYPE html>\n' + html

        # Initialize DocRaptor client (following official docs pattern)
        doc_api = docraptor.DocApi()
        doc_api.api_client.configuration.username = self.api_key

        # Build Prince options
        prince_opts = {
            'media': 'print',  # Use print media queries
            **self.prince_options
        }

        try:
            logger.info(f"Sending PDF request to DocRaptor (test_mode={test_mode})...")

            # Create document using official API pattern
            response = doc_api.create_doc({
                'test': test_mode,
                'document_type': 'pdf',
                'document_content': html,
                'name': output_pdf.name,
                'javascript': self.javascript,
                'prince_options': prince_opts,
            })

            # Write PDF to file (response is bytes)
            with open(output_pdf, 'w+b') as f:
                f.write(bytearray(response))

            mode_msg = "test (watermarked)" if test_mode else "production"
            logger.info(f"[SUCCESS] PDF generated via DocRaptor ({mode_msg}): {output_pdf}")

            if test_mode:
                logger.info("Note: Test PDFs are watermarked. Set test_mode=False for production.")

        except docraptor.rest.ApiException as error:
            logger.error(f"DocRaptor API error: Status {error.status}")
            logger.error(f"Reason: {error.reason}")
            logger.error(f"Response body: {error.body}")
            raise RuntimeError(f"DocRaptor PDF generation failed: {error}") from error


def example_usage():
    """Example of how to use DocRaptorPDF renderer."""

    # Simple HTML example
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"/>
        <title>DocRaptor Test</title>
        <style>
            @page {
                size: letter;
                margin: 0.75in 0.75in 1in 0.75in;

                /* Running footer with page numbers - Prince XML feature */
                @bottom-center {
                    content: "Page " counter(page) " of " counter(pages);
                    font-size: 9pt;
                    color: #666;
                }

                @bottom-left {
                    content: "Generated with DocRaptor";
                    font-size: 8pt;
                    color: #999;
                }
            }

            body {
                font-family: sans-serif;
                line-height: 1.6;
            }

            h1 {
                color: #2C5F7C;
                page-break-after: avoid;
            }

            .section {
                page-break-inside: avoid;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <h1>DocRaptor PDF Test</h1>
        <p>This is a test document generated with DocRaptor (Prince XML).</p>

        <div class="section">
            <h2>Section 1</h2>
            <p>Content here...</p>
        </div>

        <div class="section">
            <h2>Section 2</h2>
            <p>More content...</p>
        </div>
    </body>
    </html>
    """

    # For testing, use the test API key (generates watermarked PDFs)
    # Get your real API key from: https://docraptor.com/signup
    renderer = DocRaptorPDF(api_key="YOUR_TEST_API_KEY_HERE")

    output_path = Path("output/docraptor_test.pdf")
    renderer.render_html_to_pdf(html, output_path, test_mode=True)

    print(f"[SUCCESS] Test PDF generated: {output_path}")
    print("  (watermarked - set test_mode=False for production)")


if __name__ == '__main__':
    example_usage()
