#!/usr/bin/env python3
"""Create searchable Markdown companions for the downloaded reference PDFs."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RETRIEVED = "2026-08-07"

SOURCES = {
    "mathieson1995transfer": {
        "title": "A Decision Support System for Student Transfer Advising",
        "authors": "Kieran Mathieson and Albert L. Lederer",
        "year": "1995",
        "url": "https://jise.org/Volume7/n3/JISEv7n3p96.pdf",
        "landing": "https://jise.org/Volume7/n3/JISEv7n3p96.html",
    },
    "nguyen2024optimal": {
        "title": "Optimal Academic Plan Derived from Articulation Agreements: A Preliminary Experiment on Human-Generated and Hypothetical Algorithm-Generated Academic Plans",
        "authors": "David V. Nguyen, Shayan Doroudi, and Daniel A. Epstein",
        "year": "2024",
        "url": "https://arxiv.org/pdf/2307.04500",
        "landing": "https://arxiv.org/abs/2307.04500",
    },
    "mattei2014advising": {
        "title": "Lessons Learned from Development of a Software Tool to Support Academic Advising",
        "authors": "Nicholas Mattei, Thomas Dodson, Joshua T. Guerin, Judy Goldsmith, and Joan M. Mazur",
        "year": "2014",
        "url": "https://arxiv.org/pdf/1312.4113",
        "landing": "https://arxiv.org/abs/1312.4113",
    },
    "mi2025smartcourse": {
        "title": "SmartCourse: A Contextual AI-Powered Course Advising System for Undergraduates",
        "authors": "Yixuan Mi, Yiduo Yu, and Yiyi Zhao",
        "year": "2025",
        "url": "https://arxiv.org/pdf/2507.22946",
        "landing": "https://arxiv.org/abs/2507.22946",
    },
}


def ascii_hyphens(text: str) -> str:
    replacements = {
        "\u00ad": "",
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": " - ",
        "\u2212": "-",
    }
    for source, replacement in replacements.items():
        text = text.replace(source, replacement)
    return text


def normalize_page(text: str) -> str:
    text = ascii_hyphens(text)
    text = text.replace("\x00", "")
    lines = [line.rstrip() for line in text.splitlines()]
    output: list[str] = []
    paragraph: list[str] = []

    def flush() -> None:
        if not paragraph:
            return
        joined = re.sub(r"\s+", " ", " ".join(paragraph)).strip()
        joined = re.sub(r"(?<=[.!?])\s+(?=[A-Z0-9])", "\n", joined)
        output.append(joined)
        paragraph.clear()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush()
            continue
        paragraph.append(stripped)
    flush()
    return "\n\n".join(output).strip()


def convert(key: str, metadata: dict[str, str]) -> None:
    pdf_path = ROOT / f"{key}.pdf"
    result = subprocess.run(
        ["pdftotext", "-enc", "UTF-8", str(pdf_path), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    pages = result.stdout.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()

    header = [
        "---",
        f"bibtex_key: {key}",
        f"title: \"{metadata['title']}\"",
        f"authors: \"{metadata['authors']}\"",
        f"year: {metadata['year']}",
        f"source_url: {metadata['url']}",
        f"landing_page: {metadata['landing']}",
        f"retrieved: {RETRIEVED}",
        f"original_pdf: {key}.pdf",
        "conversion: Automated text extraction with pdftotext; consult the PDF for figures, tables, equations, and OCR-sensitive wording.",
        "---",
        "",
        f"# {metadata['title']}",
        "",
        f"Authors: {metadata['authors']}.",
        "",
        "This Markdown file is a searchable extraction of the locally archived PDF.",
        "The PDF remains the authoritative local copy for page layout and exact wording.",
        "",
        "## Extracted text",
    ]
    body: list[str] = []
    for number, page in enumerate(pages, start=1):
        body.extend(["", f"### PDF page {number}", "", normalize_page(page)])

    output_path = ROOT / f"{key}.pdf.md"
    output_path.write_text("\n".join(header + body).rstrip() + "\n", encoding="utf-8")


for citation_key, source_metadata in SOURCES.items():
    convert(citation_key, source_metadata)
