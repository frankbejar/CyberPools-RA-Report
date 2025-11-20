#!/usr/bin/env python3
"""
Playwright-based HTML → PDF renderer for CyberPools reports.

Fixes:
- Emulates print media so print.css is applied.
- Inlines CSS (styles/main.css, styles/print.css) to avoid file:// loading issues
  when using page.set_content().
- Still injects <base href="..."> so relative images/fonts resolve.

Usage:
    from scripts.generate_pdf_playwright import PlaywrightPDF
    PlaywrightPDF().render_html_to_pdf(html, Path("output.pdf"), assets_dir=Path("."))

"""

from __future__ import annotations
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime
import re

from playwright.sync_api import sync_playwright


class PlaywrightPDF:
    def __init__(
        self,
        page_format: str = "Letter",
        margins: Optional[Dict[str, str]] = None,
        print_background: bool = True,
        prefer_css_page_size: bool = True,
        scale: float = 1.0,
        display_header_footer: bool = False,
        header_template: Optional[str] = None,
        footer_template: Optional[str] = None,
        wait_until: str = "load",
        chromium_args: Optional[List[str]] = None,
        no_sandbox: bool = False,
        inline_css_paths: Optional[List[Path]] = None,
    ) -> None:
        self.page_format = page_format
        self.margins = margins or {
            "top": "0.6in", "right": "0.7in", "bottom": "0.6in", "left": "0.7in"
        }
        self.print_background = print_background
        self.prefer_css_page_size = prefer_css_page_size
        self.scale = scale
        self.display_header_footer = display_header_footer
        self.header_template = header_template
        self.footer_template = footer_template
        self.wait_until = wait_until

        self.chromium_args = list(chromium_args or [])
        if no_sandbox and "--no-sandbox" not in self.chromium_args:
            self.chromium_args.append("--no-sandbox")
        if "--disable-dev-shm-usage" not in self.chromium_args:
            self.chromium_args.append("--disable-dev-shm-usage")

        # Default CSS to inline
        self.inline_css_paths = inline_css_paths  # resolved later against assets_dir

    @staticmethod
    def _abs_file_url(path: Path) -> str:
        return path.resolve().as_uri()

    @staticmethod
    def _ensure_base_href(html: str, base_href: str) -> str:
        """Ensure a <base href="..."> inside <head> so relative URLs resolve."""
        head_rx = re.compile(r"(?i)<head([^>]*)>")
        if "<head" not in html.lower():
            return f'<head><base href="{base_href}"/></head>' + html
        return head_rx.sub(
            lambda m: f'<head{m.group(1)}><base href="{base_href}"/>', html, count=1
        )

    @staticmethod
    def _inline_css_into_html(html: str, css_text: str) -> str:
        """Append a <style> tag with provided CSS at the end of <head> (or create one)."""
        if "</head>" in html.lower():
            return re.sub(r"(?i)</head>", f"<style>{css_text}</style></head>", html, count=1)
        # No head tag? Prepend one.
        return f"<head><style>{css_text}</style></head>" + html

    def _read_css_bundle(self, assets_dir: Path, paths: List[Path]) -> str:
        buf = []
        for rel in paths:
            candidate = (assets_dir / rel).resolve()
            if candidate.exists():
                try:
                    buf.append(candidate.read_text(encoding="utf-8"))
                except Exception:
                    pass
        return "\n\n".join(buf)

    def render_html_to_pdf(
        self,
        html: str,
        output_pdf: Path,
        assets_dir: Optional[Path] = None,
    ) -> None:
        output_pdf.parent.mkdir(parents=True, exist_ok=True)
        assets_root = (assets_dir or Path.cwd()).resolve()

        # 1) Base href so relative images/fonts resolve
        base_href = self._abs_file_url(assets_root)
        html_final = self._ensure_base_href(html, base_href)

        # 2) Inline CSS to guarantee styles even if <link> fails under file://
        #    Default to styles/main.css + styles/print.css under assets_root
        inline_list = self.inline_css_paths
        if inline_list is None:
            inline_list = [Path("styles/main.css"), Path("styles/print.css")]
        css_bundle = self._read_css_bundle(assets_root, inline_list)
        if css_bundle.strip():
            html_final = self._inline_css_into_html(html_final, css_bundle)

        with sync_playwright() as p:
            browser = p.chromium.launch(args=self.chromium_args)
            page = browser.new_page()

            # 3) Ensure print media rules are used
            page.emulate_media(media="print")

            # 4) Load content and wait
            page.set_content(html_final, wait_until=self.wait_until)

            # 5) Build PDF
            pdf_options: Dict[str, Any] = {
                "path": str(output_pdf),
                "format": self.page_format,
                "margin": self.margins,
                "print_background": self.print_background,
                "prefer_css_page_size": self.prefer_css_page_size,
                "scale": self.scale,
            }

            if self.display_header_footer:
                pdf_options["display_header_footer"] = True
                pdf_options["header_template"] = self.header_template or (
                    "<div style='font-size:8px;text-align:center;color:#6b7280;'>"
                    "CyberPools Risk Assessment</div>"
                )
                gen_date = datetime.now().strftime("%Y-%m-%d")
                pdf_options["footer_template"] = self.footer_template or (
                    "<div style='font-size:8px;width:100%;display:flex;"
                    "justify-content:space-between;color:#6b7280;'>"
                    f"<span>Generated {gen_date}</span>"
                    "<span><span class='pageNumber'></span>/<span class='totalPages'></span></span>"
                    "</div>"
                )

            page.pdf(**pdf_options)
            browser.close()
