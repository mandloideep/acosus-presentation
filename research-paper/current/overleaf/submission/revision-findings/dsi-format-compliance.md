# DSI final-format compliance

Revision ID: `REV-FORMAT-001`.

The official DSI 2026 submission page links the initial and final full-paper templates.

Source: https://decisionsciences.org/conference/annual-2025/2026-submission-process/

Both templates limit abstract text to 100 words.

The final template requires author information and a running header containing author surnames and a short title of no more than eight words.

## Applied requirements

- US Letter with one-inch margins.
- Arial at 11 points.
- Single-spaced, left-aligned body text with no paragraph indentation or paragraph spacing.
- Centered bold `DECISION SCIENCES INSTITUTE` line.
- Centered sentence-case title without bold styling.
- Centered final-paper author block without professional titles.
- `Mandloi et al.` and `ACOSUS design and feasibility evaluation` in the running header.
- No page numbers or footer content.
- Bold uppercase level-one headings.
- Bold sentence-case level-two headings.
- Underlined sentence-case level-three headings.
- Bold centered `ABSTRACT` heading and abstract text no longer than 100 words.
- Bold uppercase `KEYWORDS:` label.
- APA author-year citations and alphabetized references.
- No footnotes.
- Numbered displayed equations.
- Figures and tables placed near first mention, with captions above to match the template examples.
- PDF length between 6 and 35 pages and file size no greater than 1 MB.

## Author placeholders

The author order is Deep Mandloi, Lizi Zhu, and Xiwei Wang.

Each author has explicit placeholders for affiliation, complete address, email, and telephone number.

The placeholders must be replaced before proceedings upload.

## Font handling

The source uses XeLaTeX and selects Arial when the font is available.

An Arial-compatible fallback keeps editing environments functional but is not sufficient for final verification.

The submitted PDF must be compiled in an environment that provides Arial and must pass an embedded-font inspection.

## Verification results

The active abstract contains 95 words by both a plain-text count and the LaTeX-aware verification script.

XeLaTeX and Biber completed without unresolved citations, unresolved references, duplicate labels, overfull boxes, or output-affecting warnings.

The verification PDF contains 17 US Letter pages and is approximately 604 KB.

Poppler reports embedded Arial regular, bold, and italic fonts.

All extracted page text remains within the one-inch left and right margins.

No page number or footer content appears in the rendered pages.

Every page contains the required running header and rule.

The PDF was rendered page by page and inspected for title placement, author placeholders, heading hierarchy, captions, table fit, figure legibility, missing glyphs, and clipping.
