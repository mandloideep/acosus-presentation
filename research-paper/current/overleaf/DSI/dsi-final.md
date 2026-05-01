# Converting ACOSUS Paper from DSI Initial → Final Submission

When the paper is accepted, apply these changes to `main-v3.tex` to convert from the blind Initial submission format to the authored Final submission format.

All other formatting rules (page setup, fonts, headings, citations, references) remain identical — see `format-rules.md` "Common rules" section.

---

## 1. Add the author block

In `main-v3.tex`, find the title block at the top of the document body:

```latex
\begin{document}

\begin{center}
DECISION SCIENCES INSTITUTE\\[6pt]
An AI-driven transfer student advising system: Design, implementation, and evaluation
\end{center}

\bigskip

\begin{center}
\textbf{ABSTRACT}
\end{center}
```

Insert a new author `\begin{center}...\end{center}` block **between the title block and the ABSTRACT block** (replacing the `\bigskip` between them):

```latex
\begin{center}
DECISION SCIENCES INSTITUTE\\[6pt]
An AI-driven transfer student advising system: Design, implementation, and evaluation
\end{center}

\bigskip

\begin{center}
[Full Name 1]\\
[Affiliation 1]\\
[Complete Address 1]\\
[email1@institution.edu]\\
[Phone 1]\\[10pt]
[Full Name 2]\\
[Affiliation 2]\\
[Complete Address 2]\\
[email2@institution.edu]\\
[Phone 2]\\[10pt]
[Full Name 3]\\
[Affiliation 3]\\
[Complete Address 3]\\
[email3@institution.edu]\\
[Phone 3]
\end{center}

\bigskip

\begin{center}
\textbf{ABSTRACT}
\end{center}
```

### Author block rules
- **Single-spaced**, **centered**
- **No** titles (Dr., Professor, Prof., PhD, etc.)
- One author per line for name, affiliation, address, email, phone
- Separate co-authors with `\\[10pt]` to leave a blank line between author blocks
- Order matches the submission system's author display order

### Required vs optional per-author fields
- **Required**: Full name, Affiliation, Email
- **Recommended**: Complete address, Telephone number (the Final template explicitly lists these; include if available)

---

## 2. Remove any blind-review accommodations from the body

Search the prose for self-anonymizing phrasing introduced for the Initial submission and restore normal phrasing if necessary. Examples:
- `[redacted for blind review]` → real name/citation
- `our prior work [Author, Year]` → keep as is (this is fine in Final)

For the ACOSUS draft as of the Initial submission, no such substitutions are believed to exist — verify before submitting Final.

---

## 3. Length awareness

- Initial-submission norm: 6–35 pages
- Final-submission norm: ~35 pages inclusive of all figures, tables, and references
- Excessively long papers risk rejection or shallow review

---

## 4. Acknowledgments section (optional, Final only)

If the Acknowledgments section names funding sources or individuals, ensure it stays in the Final version. The current paper has:

```latex
\section{Acknowledgments}
\small
This material is based upon work supported by the National Science Foundation under Grant No. CNS-2219623.
```

This is acceptable in Final. The commented-out line about CISE-MSI award + ASEE CyBR-MSI mini-grant can be re-added if appropriate.

---

## 5. Everything else stays the same

- Same `\documentclass`, geometry, font (Arial via helvet), margins, line spacing
- Same `titlesec` heading formatting
- Same biblatex APA configuration and `\printbibliography[title={REFERENCES}]`
- Same figures, tables, equations, labels, and prose

After updating, recompile and run the verification checklist from the Initial reformat plan to confirm.
