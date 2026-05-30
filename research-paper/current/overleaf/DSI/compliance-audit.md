# DSI Format Compliance Audit — `main-v3.tex`

Checked against `format-matrix.md`. Status legend:

- ✅ **PASS** — compliant, leave as is.
- ⚠️ **REVIEW** — judgment call / ambiguous in the template; decide before submit.
- ❌ **FIX** — clear deviation, needs a change.
- ✅ **FIXED (this pass)** — was a FIX item, now compliant.

Line numbers refer to `main-v3.tex` as of this re-audit (2026-05-30).

---

## Summary of FIX items (the must-do list — re-audited 2026-05-30)

1. ✅ **FIXED — Citations.** All `\cite` converted to `\parencite` (parenthetical) or
   `\textcite` (narrative for Ty/Deng/Thiry). No bare `\cite` remains; no manual `(\cite{})`
   wrappers remain. F1–F4 now satisfied.
2. ✅ **FIXED — Section cross-references.** All 6 `Section~\ref{...}` calls replaced
   using Option A from the J1 table (lines 324, 358, 579, 581, 687 ×2). Sentences
   now flow without the blank-rendering signpost. Figure/Table refs (lines 217, 691)
   kept as-is.
3. ❌ **Text is justified, not left-aligned** (A6) — `\RaggedRight` still commented (line 98).
4. ❌ **Paragraphs are indented** in the active (justified) mode — same root cause as #3.
5. ❌ **Running header missing entirely** (B1–B4) — `\pagestyle{empty}` (line 19) removes it.
6. ✅ **FIXED — "DECISION SCIENCES INSTITUTE" now bold** (C1, line 116).
7. ❌ **Author block missing** (C5–C7) — paper still jumps from title to abstract.
8. ✅ **FIXED — Abstract trimmed to ~100 words** (D2, line 161).
9. ❌ **L2 / L3 headings use Title Case, not sentence case** (E2/E3).
10. ⚠️ **Figure captions still below figures** (H3) — example shows captions above.
11. ⚠️ **A3 Arial:** still `\usepackage{helvet}` (line 87). Helvetica ≠ Arial; see the
    "Arial in Overleaf" note below for the three options (Helvetica substitute, `uarial`,
    or switch to XeLaTeX + `fontspec` for true Arial).
12. ⚠️ **D3 KEYWORDS label** still `\textbf{}` (line 165); template shows `\underline{}`.

---

## A. Page Setup

| ID | Status | Finding / Flag |
|----|--------|----------------|
| A1 Margins 1in | ✅ | `\usepackage[margin=1in]{geometry}` (line 18). |
| A3 Arial 11 | ⚠️ | `\documentclass[...,11pt]` (line 17) + `helvet`/`\sfdefault` (lines 87–88). Arial is unavailable in standard pdfLaTeX; **Helvetica is the accepted substitute**. See "Arial in Overleaf" note at the bottom for true-Arial options. |
| A4 Line spacing 1.0 | ✅ | `\linespread{1.0}` (line 99). |
| A5 No para spacing / A6 left-align | ❌ | **(a)** `\setlength{\parskip}{5pt}` (line 100) adds space between paragraphs — technically A5 says "none", but the template separates paragraphs with a blank line (A9), so a small skip is the LaTeX equivalent. **Decide:** keep 5pt (looks like the example) or set to a full `\baselineskip` to mirror "1 hard return". **(b) `\RaggedRight` is commented out (line 98) → the whole document is FULL-JUSTIFIED, violating A6.** Uncomment `\RaggedRight` (or apply `\RaggedRight` after `\begin{document}`). |
| A6 No indent | ❌ | `\RaggedRightParindent` is set to 0 (line 97) **but only takes effect under `\RaggedRight`, which is off**. In the current justified mode paragraphs carry the default indent. Fixing A6(b) above also fixes this; otherwise add `\setlength{\parindent}{0pt}`. |
| A7 No page numbers | ✅ | `\pagestyle{empty}` (line 19) suppresses them — but see B (it also kills the required header). |
| A10/A11 PDF ≤1MB, figs ≤500KB | ⚠️ | **Cannot verify from source — check after compiling.** Several PNG infographics + heavy TikZ. Measure the output PDF and the figure assets. |
| A12 ≤35 pages | ✅ | Short paper, well under. |
| A13 Language | ✅ | English only. |

## B. Running Header

| ID | Status | Finding / Flag |
|----|--------|----------------|
| B1–B4 | ❌ | **No running header at all** — `\pagestyle{empty}` (line 19) removes it. Template requires: left = author last names ("Mandloi et al." or the two names), right = short title ≤8 words (right-aligned), with a horizontal rule beneath, and still no page number. **Fix:** use `fancyhdr` — set L-head/R-head, `\renewcommand{\headrulewidth}{0.4pt}`, empty footer, `\pagestyle{fancy}`. Pick a ≤8-word short title (e.g. "An AI-driven Advising System for Transfer Students" = 7 words). |

## C. Title Block

| ID | Status | Finding / Flag |
|----|--------|----------------|
| C1 DSI line bold | ✅ FIXED 2026-05-30 | Line 116 now `\textbf{DECISION SCIENCES INSTITUTE}\\[6pt]`. |
| C2 Title centered | ✅ | Inside `\begin{center}` (lines 115–118). |
| C3 Title not bold | ✅ | Title is not bold. |
| C4 Title caps | ⚠️ | Current title is Title Case: "An AI-driven Transfer Student Advising System: Design, Implementation, and Evaluation". p.1 bullet literally says sentence case ("capitalize only the first Letter"), but the worked example p.5 uses Title Case. **Recommend keeping Title Case** (matches the example), but be aware of the p.1 wording. Your call. |
| C5–C7 Author block | ❌ | **Missing.** After the title (line 118) the paper goes straight to `\bigskip` then ABSTRACT. DSI full-paper template wants, centered & single-spaced under the title: each author's Full Name / Affiliation / complete address / email / telephone, with **no Dr./Prof. titles**. Add it (unless you are deliberately submitting blinded — confirm the track's review policy). |

## D. Abstract & Keywords

| ID | Status | Finding / Flag |
|----|--------|----------------|
| D1 "ABSTRACT" caps/bold/center | ✅ | Lines 157–159: `\begin{center}\textbf{ABSTRACT}\end{center}`. |
| D2 ≤100 words | ✅ FIXED 2026-05-30 | Current abstract (line 161) is **100 words** (verified by `wc -w`). |
| D3 KEYWORDS | ⚠️ | Line 165: label is **bold** (`\textbf{KEYWORDS:}`) but the template shows it **underlined**. 5 keywords present ✅. Decide: change to `\underline{KEYWORDS:}` to match, or keep bold. |
| D4 DSJ/DSJIE keywords | ⚠️ | Current: transfer students, intelligent advising, machine learning, higher education, student success prediction. Cross-check against the DSJ/DSJIE keyword list if you have it; otherwise fine. |

## E. Section Headings

| ID | Status | Finding / Flag |
|----|--------|----------------|
| E1 L1 ALL CAPS bold left | ✅ | `\titleformat{\section}{\normalfont\bfseries\MakeUppercase}{}{0pt}{}` (line 104) + no numbers. |
| E2 L2 bold sentence case | ⚠️→❌ | Format is correct (bold, no number, line 106) but **titles are Title Case**, e.g. "System Architecture", "Dual-Survey Architecture", "Survey Data Processing", "Progressive Learning Framework", "Configuration Flexibility", "Study Design", "Evaluation Instruments", "Quantitative Results", "Qualitative Findings". Template wants first-letter-only: "System architecture", etc. **Fix the title text** (or accept Title Case as a deliberate deviation). |
| E3 L3 underlined sentence case | ⚠️→❌ | Format correct (underlined, not bold, line 108). Titles are Title Case: "Priority Weighting", "Data Type Handling", "Three-Stage Pipeline", "TAM Construct Scores", "Behavioral Intention". Should be "Priority weighting", etc. |
| E4 Unnumbered | ✅ | `titlesec` formats emit no numbers. (This is exactly why J1 below matters.) |

## F. In-text Citations  ← FIXED 2026-05-30

**Setup:** `biblatex` apa style (line 90).

| Pattern | Status | Result |
|---------|--------|--------|
| `(\cite{...})` hand-wrapped | ✅ FIXED | All converted to `\parencite{...}` (manual parens removed). |
| Bare `\cite{...}` (no parens) | ✅ FIXED | Lines 358, 362, 691 (and table rows 381/383/385) converted to `\parencite{...}`. |
| Narrative (name in prose) | ✅ FIXED | Line 196 "Ty et al.'s use..." → `\textcite{computingtransfer2024}'s use...`; line 202 "Deng et al.\ applied... / Thiry et al.\ used..." → `\textcite{deng2021} applied... / \textcite{thiry2023} used...`. |

**No `\cite` commands remain in the document.** Sanity check after rebuild: confirm
all in-text citations render with "(Author, Year)" or "Author (Year)" as expected.

## G. Footnotes / Equations / Appendices

| ID | Status | Finding / Flag |
|----|--------|----------------|
| G1 No footnotes | ✅ | No `\footnote` used. |
| G2 Equations numbered, parens, right | ✅ | `\begin{equation}` `eq:priority` (lines 366–369) — auto right-aligned "(1)". |
| G3 Appendix | ✅ (N/A) | No appendix. If one is added, use L1 "APPENDIX" before REFERENCES. |

## H. Tables & Figures

| ID | Status | Finding / Flag |
|----|--------|----------------|
| H1 Numbered | ✅ | LaTeX auto-numbers all `table`/`figure` floats. |
| H2 "Table N:"/"Figure N:" centered | ✅ | Default `\caption` gives "Table 1: ..." / "Figure 1: ..."; floats are `\centering`. |
| H3 Caption ABOVE | ⚠️ | **Tables: caption is above ✅** (`\caption` precedes `tabular` in tab:priority, tab:normalization, tab:constructs, tab:results, tab:themes). **Figures: caption is BELOW** (`\caption` after the graphic in every figure). The worked example shows figure captions **above**. Decide whether to move figure `\caption` above the image to match exactly — many venues accept below, but the template example is above. |
| H4 Near first citation | ✅ | Floats use `[htbp]` and sit next to their references. |
| H5 Renders after PDF | ⚠️ | Verify TikZ + PNG render correctly in the final PDF (build-time check). |

## I. References

| ID | Status | Finding / Flag |
|----|--------|----------------|
| I1 Heading "REFERENCES" | ⚠️ | `\printbibliography[title={REFERENCES}]` (line 867). Title text ✅, but biblatex's default bib heading may render in a **larger font** than the L1 body headings. Confirm it matches E1 (Arial/Helvetica 11, bold, ALL CAPS, left); if not, add a custom `\defbibheading` (see "References styling check" note below). |
| I2 Only cited | ✅ | biblatex prints only cited entries. |
| I3 Alphabetical | ⚠️ | `sorting=nyt` (line 90) sorts by name→year→title — alphabetical by author ✅. Good. |
| I4 APA entries | ✅ | `style=apa` (line 90). APA italicizes container titles (journals/books) but not article titles — `style=apa` does this correctly. |
| I5 "available upon request" | ✅ (N/A) | Full reference list is included. |

## J. Cross-references  ← FIXED 2026-05-30

| ID | Status | Finding / Flag |
|----|--------|----------------|
| J1 Section refs by name, not number | ✅ FIXED 2026-05-30 | All 6 `Section~\ref{...}` calls (lines 324, 358, 579, 581, 687 ×2) replaced using Option A from the table below — five drop the signpost (the surrounding prose already names the concept), one rewrites the forward pointer using "configuration flexibility later in the paper". |
| J2 Figure/Table refs keep numbers | ✅ | `Figure~\ref{fig:architecture}` (line 217) and `Table~\ref{tab:constructs}` (line 691) preserved. |

### J1 per-line replacement table (revised after tone re-read 2026-05-30)

**Tone & style observations.** The paper is restrained, declarative, and avoids
redundancy. The Introduction already uses the only correct heavy-signposting
pattern (naming sections in ALL CAPS in prose: "LITERATURE REVIEW discusses…",
"METHODOLOGY AND IMPLEMENTATION describes…"). Inside the body, the prose
already does soft signposting in normal voice ("The next subsection explains
how that pipeline is designed for settings…"). Both styles work; what does NOT
work is `Section~\ref{...}` because the sections are unnumbered and the ref
renders blank.

**Key insight from re-reading the surrounding paragraphs.** Five of the six
remaining `\ref` calls point at a concept the prose has already named in the
same sentence — "dual-survey architecture", "progressive learning pipeline",
"survey instruments" — so the previous table's "described in the
Dual-Survey Architecture section" reads as a stutter ("the dual-survey
architecture described in the Dual-Survey Architecture section"). The cleaner
move for those five is to **drop the signpost** (or use "described earlier" /
"above") rather than re-state the heading name.

The one remaining case (line 324) is a *forward* pointer to a section the
reader has not seen yet, so naming the destination is genuinely helpful there.

Two options are given per row. **Option A** is the recommended, most natural
rewrite; **Option B** preserves an explicit name-by-name signpost in case you
want the cross-reference to remain visible.

| Line | Before | After (Option A — applied 2026-05-30) |
|------|--------|---------------------------------------|
| 324 | `…the next step is to transform raw responses into model-ready inputs. Section~\ref{subsec:config} returns to the linkage mechanism from an implementation perspective.` | `…the next step is to transform raw responses into model-ready inputs. We return to the linkage mechanism from an implementation perspective when discussing configuration flexibility later in the paper.` |
| 358 | `The survey instruments described in Section~\ref{subsec:dualsurvey} convert student responses into feature vectors…` | `The Target and Factor Survey instruments convert student responses into feature vectors…` |
| 579 | `The modular design described in Section~\ref{subsec:progressive} is implemented through a configuration system…` | `The modular pipeline design described above is implemented through a configuration system…` |
| 581 | `\textbf{Survey Linkage:} The dual-survey architecture described in Section~\ref{subsec:dualsurvey} uses explicit linkage settings.` | `\textbf{Survey Linkage:} The dual-survey architecture uses explicit linkage settings.` |
| 687 (a) | `during the foundation phase of the progressive learning pipeline (Section~\ref{subsec:progressive}), when the system was still collecting labeled observations…` | `during the foundation phase of the progressive learning pipeline, when the system was still collecting labeled observations…` |
| 687 (b) | `Participants completed the Factor and Target Survey instruments described in Sections~\ref{subsec:dualsurvey} and~\ref{subsec:dataprocessing}, then completed a feedback survey through Qualtrics.` | `Participants completed the Factor and Target Survey instruments, then completed a feedback survey through Qualtrics.` |

**Why the asymmetry?** Line 324 is the only *forward* reference (Methodology
pointing to Configuration Flexibility, which hasn't appeared yet). All five
others are *backward* references to sections that ended within the last page
or two and that the surrounding prose already names by concept. For a
reviewer reading linearly, naming the section a second time adds nothing; for
a reader skimming, the soft pointer ("above", "earlier", "later in the
paper") is enough to land them in the right area without the rendered-blank
`Section~\ref{}`.

If the previous table's pattern is preferred for the visual symmetry of
"the X section" in every spot, the Option B column delivers that without the
stutter. But Option A is what most published papers do.

The label → name mapping is kept below for reference (handy if more refs are
added later):

| Label | Section name to use in prose (if signposting) |
|-------|-----------------------------------------------|
| `sec:introduction`     | the Introduction |
| `sec:literature`       | the Literature Review |
| `sec:methodology`      | the Methodology and Implementation section |
| `sec:evaluation`       | the Evaluation section |
| `sec:conclusion`       | the Conclusion and Future Work section |
| `subsec:sysarch`       | the System Architecture section |
| `subsec:dualsurvey`    | the Dual-Survey Architecture section |
| `subsec:dataprocessing`| the Survey Data Processing section |
| `subsec:progressive`   | the Progressive Learning Framework section |
| `subsec:config`        | the Configuration Flexibility section |
| `subsec:studydesign`   | the Study Design section |
| `subsec:instruments`   | the Evaluation Instruments section |
| `subsec:quantresults`  | the Quantitative Results section |
| `subsec:qualfindings`  | the Qualitative Findings section |

All `Figure~\ref{fig:...}` and `Table~\ref{tab:...}` references stay as-is.

---

## Notes on the user's open questions (2026-05-30)

### Arial in Overleaf — what actually renders

Standard pdfLaTeX **cannot ship Arial** (proprietary TrueType). The current setup
(`\usepackage{helvet}` + `\renewcommand{\familydefault}{\sfdefault}`) renders
**Helvetica**, which is the universally accepted free substitute for Arial in
academic LaTeX submissions. Visually they are very close but not identical
(letter widths/kerning differ slightly).

Three real options in Overleaf:

1. **Keep Helvetica (current).** Zero risk. If a reviewer asks, note it as the
   standard LaTeX substitute for Arial — DSI has not historically rejected this.
2. **`uarial` package.** Maps the document font to URW's Arial-clone metrics.
   Requires no compiler change but the rendering is still not pixel-true Arial.
3. **Switch compiler to XeLaTeX or LuaLaTeX and use `fontspec`** to load the
   actual Arial system font. This gives **true Arial** in the output PDF. To do
   it on Overleaf:
   - Menu → Settings → Compiler → **XeLaTeX** (or LuaLaTeX).
   - Replace `\usepackage[T1]{fontenc}`, `\usepackage[utf8]{inputenc}`,
     `\usepackage{helvet}`, and `\renewcommand{\familydefault}{\sfdefault}` with:

     ```latex
     \usepackage{fontspec}
     \setmainfont{Arial}
     ```
   - Overleaf's TeXLive image includes Arial in its font cache, so this resolves
     without manual font uploads. `biblatex`, `titlesec`, `tikz`, etc. all
     continue to work under XeLaTeX with no other changes needed.

   Recommended if "Arial" wording in the DSI guidelines is being read strictly.

### References (REFERENCES section) styling check

- **Heading.** `\printbibliography[title={REFERENCES}]` emits a `\section*{REFERENCES}`,
  which under our `titlesec` config inherits `\bfseries\MakeUppercase` — should match
  L1 body headings (Arial/Helvetica 11pt, bold, all-caps, left-aligned). Visually
  confirm after compile; if biblatex uses a larger font for the bib heading,
  override with:

  ```latex
  \defbibheading{dsiheading}[REFERENCES]{%
    \section*{#1}}
  \printbibliography[heading=dsiheading]
  ```

- **Entry style.** `style=apa` (line 90) renders APA-style entries: author surname
  first, year in parentheses, article titles in plain (not italic) text, journal
  and book titles in italics, volume in italics, issue in parens, page range
  plain. This matches the worked example on p.7 of the template. **No styling
  change needed** for entries themselves — the earlier audit's wording "title in
  italics" was a misread of the I4 row; APA italicizes container titles, not
  article titles, and `style=apa` does exactly that.

- **One thing worth eyeballing in the compiled PDF.** APA bibliographies under
  biblatex use a **hanging indent** (first line flush, continuation lines
  indented). Confirm that renders; if Overleaf shows the entries with a flush
  block instead, add `\setlength{\bibhang}{0.5in}` (or similar) before
  `\printbibliography`.

---

## Suggested fix order (re-audited 2026-05-30)

Completed:

- ✅ **F. Citations** — all `\cite` converted to `\parencite`/`\textcite`.
- ✅ **C1.** "DECISION SCIENCES INSTITUTE" now bold.
- ✅ **D2.** Abstract trimmed to 100 words.
- ✅ **J1. Section cross-references** — all 6 `Section~\ref{...}` replaced (Option A).

Remaining (in priority order):

1. **Layout switches** — (a) A6: uncomment `\RaggedRight` on line 98; (b) B1–B4:
   add `fancyhdr` header with `\pagestyle{fancy}` (replacing `\pagestyle{empty}`
   on line 19); (c) C5–C7: add the centered author block under the title.
2. **A3 Arial** — decide between keeping Helvetica (zero-risk) or switching
   Overleaf to XeLaTeX + `fontspec{Arial}` for true Arial. See the "Arial in
   Overleaf" note below.
3. **D3 KEYWORDS** — change `\textbf{KEYWORDS:}` to `\underline{KEYWORDS:}` if
   you want to match the template exactly.
4. **Heading case (E2/E3)** — Title Case → sentence case (only if going for
   strict compliance).
5. **Figure caption placement (H3)** and **REFERENCES heading font (I1)** —
   final polish; re-confirm after rebuild.
6. **Build-time checks** — PDF ≤1 MB, figures ≤500 KB, all floats render
   (A10/A11/H5).
