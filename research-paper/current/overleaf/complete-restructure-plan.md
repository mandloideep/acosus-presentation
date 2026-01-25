# ACOSUS Paper Restructuring Plan

## Overview

This document outlines the comprehensive plan to restructure the ACOSUS research paper by consolidating Sections 3 (System Design and Methodology) and 4 (System Implementation) into a single unified section.

### Goal
Provide readers with a **top-down, general-to-specific** understanding of the system—starting with the big picture and progressively drilling into details.

### Files Involved
- `main.tex` — Original paper (unchanged, serves as reference)
- `main-v2.tex` — Restructured version (all changes applied here)

---

## Current vs. New Structure

### Paper-Level Structure

| Current | New |
|---------|-----|
| Section 1: Introduction | Section 1: Introduction *(updated)* |
| Section 2: Literature Review | Section 2: Literature Review *(updated ending)* |
| Section 3: System Design and Methodology | **Merged into Section 3** |
| Section 4: System Implementation | **Merged into Section 3** |
| Section 5: Evaluation | Section 4: Evaluation |
| Section 6: Conclusion | Section 5: Conclusion |

### New Section 3: Methodology and Implementation

**Recommended Structure (Option A - Flat Subsections):**

```
3. Methodology and Implementation
   3.1 System Architecture
   3.2 Dual-Survey Architecture
   3.3 Survey Data Processing
   3.4 Progressive Learning Framework
   3.5 Configuration Flexibility
```

**Alternative Structure (Option B - Grouped Subsections):**

```
3. Methodology and Implementation
   3.1 System Design
       3.1.1 System Architecture (4-layer overview)
       3.1.2 Dual-Survey Architecture (conceptual design)
   3.2 Implementation
       3.2.1 Survey Data Processing
       3.2.2 Progressive Learning Framework
       3.2.3 Configuration Flexibility
```

> **Note:** Option A is recommended for a paper of this length. Option B preserves a clear "Design vs Implementation" distinction if reviewers expect that separation.

---

## Section Title Alternatives

The recommended title is **"Methodology and Implementation"**. Other options considered:

| Option | Pros | Cons |
|--------|------|------|
| **Methodology and Implementation** | Clear, emphasizes both aspects | Slightly generic |
| System Design and Implementation | Standard, familiar | Doesn't emphasize methodology |
| ACOSUS Architecture and Implementation | Emphasizes system name | May feel redundant with paper title |
| Platform Design and Implementation | Specific | Less common phrasing |
| Methodology | Common in research papers | Undersells implementation depth |

---

## Figure Renumbering

Figures will be renumbered based on their new order of appearance:

| Current | New | Content | Location (New) |
|---------|-----|---------|----------------|
| Fig 4 | **Fig 1** | System Architecture (4-layer diagram) | Section 3.1 |
| Fig 1 | **Fig 2** | Dual-Survey Architecture | Section 3.2 |
| Fig 3 | **Fig 3** | Survey Data Processing Pipeline | Section 3.3 |
| Fig 2 | **Fig 4** | Three-Stage Progressive Pipeline | Section 3.4 |
| Fig 5 | **Fig 5** | Dual-Survey with Linkage | Section 3.5 |

---

## Phase 0: Setup

### Objective
Create the working file and establish a clean baseline commit.

### Tasks

#### Task 0.1: Copy main.tex to main-v2.tex

**Action:** Create a copy of `main.tex` named `main-v2.tex`

```bash
cp main.tex main-v2.tex
```

#### Task 0.2: Initial Commit

**Action:** Commit main-v2.tex to establish baseline

```bash
git add main-v2.tex
git commit -m "Add main-v2.tex as baseline for paper restructuring"
```

> **Note:** This commit ensures main-v2.tex starts identical to main.tex, making all restructuring changes trackable from this point.

---

## Phase 1: Preparation

### Objective
Update section labels and figure references to prepare for content reorganization.

### Tasks

#### Task 1.1: Update Main Section Labels

**File:** `main-v2.tex`

**Before (lines 145-147):**
```latex
\section{System Design and Methodology}\label{sec:design}
```

**After:**
```latex
\section{Methodology and Implementation}\label{sec:methodology}
```

**Rationale:** New unified section replaces both `sec:design` and `sec:implementation`.

---

**Before (lines 303-304):**
```latex
\section{System Implementation}\label{sec:implementation}
```

**After:**
```latex
% REMOVED - Content moved to Section 3 subsections
```

**Rationale:** Section 4 is eliminated; content moves into Section 3 subsections.

---

#### Task 1.2: Update Evaluation Section Number

**Before (line 604):**
```latex
\section{Evaluation}\label{sec:evaluation}
```

**After:**
```latex
\section{Evaluation}\label{sec:evaluation}
```

**Note:** Label stays the same; LaTeX will auto-number as Section 4.

---

#### Task 1.3: Update Conclusion Section Number

**Before (line 712):**
```latex
\section{Conclusion and Future Work}\label{sec:conclusion}
```

**After:**
```latex
\section{Conclusion and Future Work}\label{sec:conclusion}
```

**Note:** Label stays the same; LaTeX will auto-number as Section 5.

---

#### Task 1.4: Prepare Figure Label Updates

Create a reference mapping for figure labels:

| Old Label | New Label | Update Required |
|-----------|-----------|-----------------|
| `fig:architecture` | `fig:architecture` | No (stays Fig 1 position) |
| `fig:dualsurvey` | `fig:dualsurvey` | No (stays same label) |
| `fig:processing` | `fig:processing` | No (stays same label) |
| `fig:pipeline` | `fig:pipeline` | No (stays same label) |
| `fig:linkage` | `fig:linkage` | No (stays same label) |

> **Note:** Figure labels don't need to change—only their order in the document changes, which LaTeX handles automatically.

---

## Phase 2: Content Restructuring

### Objective
Reorder subsections and move content blocks to achieve the new structure.

### Tasks

#### Task 2.1: Create New Section 3 Header

**Location:** After Literature Review section ends (after line 141)

**New Content:**
```latex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SECTION 3: METHODOLOGY AND IMPLEMENTATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Methodology and Implementation}\label{sec:methodology}

This section presents the ACOSUS platform's design and implementation. We begin with the overall system architecture (\S\ref{subsec:sysarch}), then describe the dual-survey data collection approach (\S\ref{subsec:dualsurvey}), detail how survey responses are processed (\S\ref{subsec:dataprocessing}), explain the progressive learning framework designed for small-data contexts (\S\ref{subsec:progressive}), and conclude with the configuration flexibility that enables institutional adaptation (\S\ref{subsec:config}).
```

**Rationale:** Introductory paragraph provides roadmap for the unified section.

---

#### Task 2.2: Move System Architecture to 3.1

**Current Location:** Lines 427-517 (Section 4.2)
**New Location:** First subsection of Section 3

**Before (subsection header):**
```latex
\subsection{System Architecture}\label{subsec:sysarch}
```

**After:**
```latex
\subsection{System Architecture}\label{subsec:sysarch}
```

**Note:** Header stays the same; content block (lines 427-517) moves to become first subsection.

**Cross-references affected:**
- `\ref{subsec:sysarch}` — No change needed (label preserved)
- Figure~\ref{fig:architecture} — Will auto-renumber to Fig 1

---

#### Task 2.3: Move Dual-Survey Architecture to 3.2

**Current Location:** Lines 149-197 (Section 3.1)
**New Location:** Second subsection of Section 3

**Content to move includes:**
- Terminology definitions (lines 151-157)
- Dual-survey explanation (lines 159-167)
- Figure 1 (Dual-Survey Architecture diagram, lines 169-197)

**Before (subsection header):**
```latex
\subsection{The Dual-Survey Architecture}\label{subsec:dualsurvey}
```

**After:**
```latex
\subsection{Dual-Survey Architecture}\label{subsec:dualsurvey}
```

**Change:** Remove "The" from title for consistency.

**Terminology Preamble:** Keep at the beginning of this subsection (before main content).

**Cross-references affected:**
- `\ref{subsec:dualsurvey}` — No change needed
- Figure~\ref{fig:dualsurvey} — Will auto-renumber to Fig 2

---

#### Task 2.4: Move Survey Data Processing to 3.3

**Current Location:** Lines 307-425 (Section 4.1)
**New Location:** Third subsection of Section 3

**Before (subsection header):**
```latex
\subsection{Survey Data Processing}\label{subsec:dataprocessing}
```

**After:**
```latex
\subsection{Survey Data Processing}\label{subsec:dataprocessing}
```

**Note:** Header stays the same.

**Cross-references affected:**
- `\ref{subsec:dataprocessing}` — No change needed
- Figure~\ref{fig:processing} — Will auto-renumber to Fig 3
- Table~\ref{tab:priority} — No change needed
- Table~\ref{tab:normalization} — No change needed

---

#### Task 2.5: Move Progressive Learning Framework to 3.4

**Current Location:** Lines 199-298 (Section 3.2)
**New Location:** Fourth subsection of Section 3

**Before (subsection header):**
```latex
\subsection{Architectural Philosophy: Small Data by Design}\label{subsec:progressive}
```

**After:**
```latex
\subsection{Progressive Learning Framework}\label{subsec:progressive}
```

**Change:** Renamed from "Architectural Philosophy: Small Data by Design" to "Progressive Learning Framework" for clarity and consistency.

**Sub-subsection update:**

**Before:**
```latex
\subsubsection{The Three-Stage Progressive Pipeline}
```

**After:**
```latex
\subsubsection{Three-Stage Pipeline}
```

**Change:** Simplified title (removed "The" and "Progressive" since parent section now contains "Progressive").

**Cross-references affected:**
- `\ref{subsec:progressive}` — No change needed
- Figure~\ref{fig:pipeline} — Will auto-renumber to Fig 4

---

#### Task 2.6: Move Configuration Flexibility to 3.5

**Current Location:** Lines 519-599 (Section 4.3)
**New Location:** Fifth (final) subsection of Section 3

**Before (subsection header):**
```latex
\subsection{Model Configuration Flexibility}\label{subsec:config}
```

**After:**
```latex
\subsection{Configuration Flexibility}\label{subsec:config}
```

**Change:** Shortened title (removed "Model" for brevity).

**Cross-references affected:**
- `\ref{subsec:config}` — No change needed
- Figure~\ref{fig:linkage} — Will auto-renumber to Fig 5

---

#### Task 2.7: Remove Old Section Headers

**Action:** Delete the following lines after content has been moved:

1. Old Section 3 header and intro (lines 142-147):
```latex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SECTION 3: SYSTEM DESIGN AND METHODOLOGY
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{System Design and Methodology}\label{sec:design}

To address the data constraints...
```

2. Old Section 4 header and intro (lines 300-305):
```latex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SECTION 4: SYSTEM IMPLEMENTATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{System Implementation}\label{sec:implementation}

The ACOSUS platform translates...
```

**Rationale:** These headers are replaced by the new unified Section 3.

---

## Phase 3: Reference Updates

### Objective
Update all cross-references in Introduction, Literature Review, and other sections.

### Tasks

#### Task 3.1: Update Introduction - Paper Organization Paragraph

**Location:** Line 121

**Before:**
```latex
The remainder of the paper is organized as follows. Section~\ref{sec:literature} reviews related work on transfer-student success and intelligent advising. Section~\ref{sec:design} describes our system design and methodology. Section~\ref{sec:implementation} presents implementation details. Section~\ref{sec:evaluation} reports empirical findings from our pilot study. Section~\ref{sec:conclusion} concludes and outlines directions for future research.
```

**After:**
```latex
The remainder of the paper is organized as follows. Section~\ref{sec:literature} reviews related work on transfer-student success and intelligent advising. Section~\ref{sec:methodology} presents our methodology and implementation, covering system architecture, the dual-survey data collection approach, survey processing, the progressive learning framework, and configuration flexibility. Section~\ref{sec:evaluation} reports empirical findings from our pilot study. Section~\ref{sec:conclusion} concludes and outlines directions for future research.
```

**Rationale:** Combines the two separate section references into one, with a brief enumeration of subsection topics.

---

#### Task 3.2: Update Introduction - Contributions List

**Location:** Lines 114-119

**Before:**
```latex
\begin{enumerate}
    \item We introduced an intelligent advising platform designed specifically for transfer students, integrating standard academic records with student-provided background to build a unified longitudinal profile.
    \item We developed a dual-survey architecture that separates outcome measurement (Target Surveys) from feature collection (Factor Surveys), enabling systematic capture of transfer-specific variables---academic background, financial circumstances, and logistical constraints---while providing advisors with unified, structured student profiles through a centralized dashboard.
    \item We implemented a modular prediction architecture with extensive configuration support that enables adaptation to diverse institutional contexts and emerging methodological advances. The system's algorithm-agnostic design—where any compatible method can serve each pipeline stage—allows researchers to empirically evaluate alternative approaches on their specific transfer student populations, while configuration options for survey linkage, phase transitions, and hyperparameters support customization without code modification.
    \item We validated the platform through a pilot deployment with transfer students, who provided feedback on their experience using it, showing that it streamlines self-advising workflows and is perceived as trustworthy, actionable, and equity-enhancing.
\end{enumerate}
```

**After:**
```latex
\begin{enumerate}
    \item We present an intelligent advising platform designed specifically for transfer students, built on a four-layer architecture that integrates standard academic records with student-provided background to build unified longitudinal profiles (\S\ref{subsec:sysarch}).
    \item We introduce a dual-survey architecture that separates outcome measurement (Target Surveys) from feature collection (Factor Surveys), enabling systematic capture of transfer-specific variables while providing advisors with structured student profiles through a centralized dashboard (\S\ref{subsec:dualsurvey}, \S\ref{subsec:dataprocessing}).
    \item We develop a progressive learning framework with algorithm-agnostic design, treating data scarcity as a fundamental design constraint. Configuration options for survey linkage, phase transitions, and hyperparameters support adaptation to diverse institutional contexts without code modification (\S\ref{subsec:progressive}, \S\ref{subsec:config}).
    \item We validate the platform through a pilot deployment with transfer students, demonstrating that the data collection workflow is perceived as easy to use, useful, and trustworthy (\S\ref{sec:evaluation}).
\end{enumerate}
```

**Rationale:**
- Adds section references to each contribution for easier navigation
- Slightly tightens language
- Maps contributions to the new subsection structure
- Changes verb tense for consistency ("introduced" → "present", "developed" → "introduce", etc.)

---

#### Task 3.3: Update Literature Review - Transition Paragraph

**Location:** Line 140

**Before:**
```latex
The present work answers these gaps from a systems perspective. Drawing on prior quantitative and qualitative insights, we engineer an integrated advising platform that fuses standard academic records (e.g., transfer-credit counts, GPA history, enrollment status) with student-supplied experience data and applies a lightweight, interpretable classifier to generate individualized success forecasts. An intuitive dashboard delivers these forecasts directly to students. Initial user feedback from the pilot indicates that the system fills a critical void in current transfer-student support practices and offers a scalable template for institutions seeking to improve equity and retention.
```

**After:**
```latex
The present work addresses these gaps through an integrated systems approach. We present ACOSUS, a platform that fuses standard academic records (e.g., transfer-credit counts, GPA history, enrollment status) with student-supplied data collected through a structured dual-survey architecture. A progressive learning framework enables the system to deliver value immediately through standardized data collection, while building toward predictive capabilities as observations accumulate. Initial user feedback from a pilot deployment indicates that the system fills a critical void in current transfer-student support practices and offers a scalable template for institutions seeking to improve equity and retention.
```

**Rationale:**
- Introduces ACOSUS by name (consistent with Section 3 intro)
- Mentions "dual-survey architecture" and "progressive learning framework" to foreshadow Section 3 content
- Removes "lightweight, interpretable classifier" (too specific for lit review transition)
- Better aligns with the new section's emphasis on immediate value + progressive capability

---

#### Task 3.4: Update Section 3 Internal References

**Location:** New Section 3 introductory paragraph (from Task 2.1)

The following cross-references appear in the new section intro and subsections. Verify each resolves correctly:

| Reference | Target | Status |
|-----------|--------|--------|
| `\ref{subsec:sysarch}` | 3.1 System Architecture | ✓ |
| `\ref{subsec:dualsurvey}` | 3.2 Dual-Survey Architecture | ✓ |
| `\ref{subsec:dataprocessing}` | 3.3 Survey Data Processing | ✓ |
| `\ref{subsec:progressive}` | 3.4 Progressive Learning Framework | ✓ |
| `\ref{subsec:config}` | 3.5 Configuration Flexibility | ✓ |

---

#### Task 3.5: Update References Within Moved Subsections

Several subsections contain internal references that need verification:

**In 3.1 System Architecture (moved from 4.2):**
- Line 429: `Section~\ref{sec:design}` → Change to `Section~\ref{sec:methodology}`

**Before:**
```latex
The ACOSUS platform translates the architectural principles described in Section~\ref{sec:design} into a functional system.
```

**After:**
```latex
The ACOSUS platform implements a four-layer architecture that separates concerns across presentation, business logic, data persistence, and predictive modeling (Figure~\ref{fig:architecture}).
```

**Rationale:** Since System Architecture now comes first, it can't reference "principles described earlier." Rewrite to be self-contained.

---

**In 3.2 Dual-Survey Architecture (moved from 3.1):**
- Line 159: `Section~\ref{sec:introduction}` — No change needed

---

**In 3.3 Survey Data Processing (moved from 4.1):**
- Line 309: `Section~\ref{subsec:dualsurvey}` — No change needed (still valid reference)

---

**In 3.4 Progressive Learning Framework (moved from 3.2):**
- Line 201: Reference to earlier design discussion

**Before:**
```latex
ACOSUS addresses data scarcity constraints through a framework that treats them not as limitations to overcome but as fundamental design constraints to embrace.
```

**After:**
```latex
ACOSUS addresses data scarcity constraints through a progressive learning framework that treats limited data not as a limitation to overcome but as a fundamental design constraint to embrace.
```

**Rationale:** Minor rewording for clarity since "framework" is now in the section title.

---

**In 3.5 Configuration Flexibility (moved from 4.3):**
- Line 521: `Section~\ref{subsec:progressive}` — No change needed (still valid)
- Line 523: `Section~\ref{subsec:dualsurvey}` — No change needed (still valid)

---

#### Task 3.6: Update Evaluation Section References

**Location:** Section 4 (Evaluation), line 606

**Before:**
```latex
This section describes the study design (\S\ref{subsec:studydesign}), evaluation instruments (\S\ref{subsec:instruments}), quantitative results (\S\ref{subsec:quantresults}), and qualitative findings (\S\ref{subsec:qualfindings}).
```

**After:** No change needed — internal references within Evaluation section remain valid.

---

**Location:** Line 612

**Before:**
```latex
This evaluation was conducted during the foundation phase of the progressive learning pipeline (Section~\ref{subsec:progressive})
```

**After:** No change needed — reference to `\ref{subsec:progressive}` still valid.

---

#### Task 3.7: Update Conclusion Section References

**Location:** Line 716

**Before:**
```latex
Our work makes three contributions: (1) a Dual-Survey Architecture that separates outcome measurement from feature collection while providing advisors with structured, standardized student profiles through a unified dashboard; (2) a modular prediction architecture with an algorithm-agnostic design that enables researchers to empirically evaluate alternative approaches on their specific transfer student populations, with configuration options for survey linkage, phase transitions, and hyperparameters supporting adaptation to diverse institutional contexts; and (3) pilot validation with transfer students ($N=4$) demonstrating strong usability---Perceived Ease of Use achieved a perfect score, indicating the survey workflow balances comprehensiveness with accessibility.
```

**After:**
```latex
Our work makes three contributions: (1) a dual-survey architecture that separates outcome measurement from feature collection while providing advisors with structured, standardized student profiles through a unified dashboard (\S\ref{subsec:dualsurvey}); (2) a progressive learning framework with algorithm-agnostic design that enables researchers to empirically evaluate alternative approaches on their specific transfer student populations, with configuration options supporting adaptation to diverse institutional contexts (\S\ref{subsec:progressive}, \S\ref{subsec:config}); and (3) pilot validation with transfer students ($N=4$) demonstrating strong usability---Perceived Ease of Use achieved a perfect score, indicating the survey workflow balances comprehensiveness with accessibility (\S\ref{sec:evaluation}).
```

**Rationale:** Added section references for navigation; changed "modular prediction architecture" to "progressive learning framework" to match new terminology.

---

#### Task 3.8: Remove Obsolete Label

**Action:** Search for and remove any references to `\label{sec:design}` and `\label{sec:implementation}` after content has been reorganized.

**Verification:** Compile document and check for "undefined reference" warnings.

---

## Phase 4: Validation

### Objective
Verify all changes are correct and the document compiles without errors.

### Tasks

#### Task 4.1: Compile and Check for Errors

**Action:** Run LaTeX compilation on main-v2.tex

```bash
pdflatex main-v2.tex
biber main-v2
pdflatex main-v2.tex
pdflatex main-v2.tex
```

**Check for:**
- [ ] No "undefined reference" warnings
- [ ] No "multiply defined label" warnings
- [ ] All figures appear in correct order (1, 2, 3, 4, 5)
- [ ] All tables appear correctly
- [ ] Bibliography renders correctly

---

#### Task 4.2: Verify Section Numbering

**Expected output:**

| Section | Title |
|---------|-------|
| 1 | Introduction |
| 2 | Literature Review |
| 3 | Methodology and Implementation |
| 3.1 | System Architecture |
| 3.2 | Dual-Survey Architecture |
| 3.3 | Survey Data Processing |
| 3.4 | Progressive Learning Framework |
| 3.5 | Configuration Flexibility |
| 4 | Evaluation |
| 4.1 | Study Design |
| 4.2 | Evaluation Instruments |
| 4.3 | Quantitative Results |
| 4.4 | Qualitative Findings |
| 5 | Conclusion and Future Work |

---

#### Task 4.3: Verify Figure Ordering

**Expected figure sequence in document:**

1. **Figure 1:** System Architecture (4-layer diagram) — appears in Section 3.1
2. **Figure 2:** Dual-Survey Architecture — appears in Section 3.2
3. **Figure 3:** Survey Data Processing Pipeline — appears in Section 3.3
4. **Figure 4:** Three-Stage Progressive Pipeline — appears in Section 3.4
5. **Figure 5:** Dual-Survey with Linkage — appears in Section 3.5
6. **Figure 6:** TAM construct scores — appears in Section 4.3
7. **Figure 7:** Behavioral intention — appears in Section 4.3
8. **Figure 8:** Qualitative theme distribution — appears in Section 4.4

---

#### Task 4.4: Read-Through for Flow

**Checklist:**
- [ ] Section 3 intro paragraph accurately describes subsection contents
- [ ] Terminology appears before first use in Section 3.2
- [ ] Transitions between subsections feel natural
- [ ] No orphaned references to old section structure
- [ ] Introduction contributions map clearly to section content
- [ ] Literature review ending flows into Section 3

---

#### Task 4.5: Final Commit

**Action:** Commit all restructuring changes

```bash
git add main-v2.tex
git commit -m "Restructure paper: consolidate Sections 3-4 into unified Methodology and Implementation"
```

---

## Appendix: Complete Cross-Reference Inventory

### Section References

| Reference | Old Target | New Target | Update Required |
|-----------|------------|------------|-----------------|
| `\ref{sec:introduction}` | Section 1 | Section 1 | No |
| `\ref{sec:literature}` | Section 2 | Section 2 | No |
| `\ref{sec:design}` | Section 3 | **REMOVED** | Yes — change to `\ref{sec:methodology}` |
| `\ref{sec:implementation}` | Section 4 | **REMOVED** | Yes — change to `\ref{sec:methodology}` |
| `\ref{sec:methodology}` | — | Section 3 | New |
| `\ref{sec:evaluation}` | Section 5 | Section 4 | No (auto-renumbered) |
| `\ref{sec:conclusion}` | Section 6 | Section 5 | No (auto-renumbered) |

### Subsection References

| Reference | Old Location | New Location | Update Required |
|-----------|--------------|--------------|-----------------|
| `\ref{subsec:dualsurvey}` | 3.1 | 3.2 | No (label preserved) |
| `\ref{subsec:progressive}` | 3.2 | 3.4 | No (label preserved) |
| `\ref{subsec:dataprocessing}` | 4.1 | 3.3 | No (label preserved) |
| `\ref{subsec:sysarch}` | 4.2 | 3.1 | No (label preserved) |
| `\ref{subsec:config}` | 4.3 | 3.5 | No (label preserved) |

### Figure References

| Reference | Old Figure # | New Figure # | Update Required |
|-----------|--------------|--------------|-----------------|
| `\ref{fig:dualsurvey}` | Fig 1 | Fig 2 | No (auto-renumbered) |
| `\ref{fig:pipeline}` | Fig 2 | Fig 4 | No (auto-renumbered) |
| `\ref{fig:processing}` | Fig 3 | Fig 3 | No |
| `\ref{fig:architecture}` | Fig 4 | Fig 1 | No (auto-renumbered) |
| `\ref{fig:linkage}` | Fig 5 | Fig 5 | No |

### Table References

| Reference | Table # | Update Required |
|-----------|---------|-----------------|
| `\ref{tab:priority}` | Table 1 | No |
| `\ref{tab:normalization}` | Table 2 | No |
| `\ref{tab:constructs}` | Table 3 | No |
| `\ref{tab:results}` | Table 4 | No |
| `\ref{tab:themes}` | Table 5 | No |

---

## Checklist Summary

### Phase 0: Setup
- [ ] Copy main.tex to main-v2.tex
- [ ] Commit baseline

### Phase 1: Preparation
- [ ] Update main section labels
- [ ] Verify figure labels (no changes needed)

### Phase 2: Content Restructuring
- [ ] Create new Section 3 header with intro paragraph
- [ ] Move System Architecture to 3.1
- [ ] Move Dual-Survey Architecture to 3.2 (with terminology)
- [ ] Move Survey Data Processing to 3.3
- [ ] Move Progressive Learning Framework to 3.4
- [ ] Move Configuration Flexibility to 3.5
- [ ] Remove old section headers

### Phase 3: Reference Updates
- [ ] Update Introduction - paper organization paragraph
- [ ] Update Introduction - contributions list
- [ ] Update Literature Review - transition paragraph
- [ ] Update internal references in moved subsections
- [ ] Verify Evaluation section references
- [ ] Update Conclusion section references
- [ ] Remove obsolete labels

### Phase 4: Validation
- [ ] Compile without errors
- [ ] Verify section numbering
- [ ] Verify figure ordering
- [ ] Read-through for flow
- [ ] Final commit
