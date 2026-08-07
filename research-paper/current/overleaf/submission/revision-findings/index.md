# DSI paper revision findings index

Inspection date: 2026-08-05.

The line numbers below refer to the final revised `submission/main-v4-ai-edit.tex`.

## Revision map

| Revision ID | Reviewer | Issue | Active decision | Original line | Stable sentence anchor | Final line | Supporting file | Status |
| --- | --- | --- | --- | ---: | --- | ---: | --- | --- |
| `REV-TITLE-001` | 2817478 and 2817476 | Title overstates AI evaluation | Design-and-feasibility title active; two alternatives retained as comments | 106 | `ACOSUS: Design and feasibility evaluation` | 120 | [title-directions.md](title-directions.md) | Complete |
| `REV-ABSTRACT-001` | 2817476 and 2817831 | Abstract must match evaluated scope | 95-word feasibility abstract; predictive validity explicitly excluded | 152 | `Transfer students face fragmented records` | 149 | [dsi-format-compliance.md](dsi-format-compliance.md) | Complete |
| `REV-CONTRIB-001` | 2817476 and 2817831 | Prediction pipeline presented as a contribution | Structured data collection and advisor support made primary; model path treated as a diagnostic roadmap | 169 | `To address this gap, we designed ACOSUS` | 168 | [implementation-status.md](implementation-status.md) | Complete |
| `REV-COMP-001` | 2817478 | No comparison with existing transfer systems | Transfer-specific ASSIST and Transferology/TES comparison active; two alternative treatments retained | 191 | `Transfer-oriented technologies address distinct parts` | 192 | [comparison-transfer-specific.md](comparison-transfer-specific.md) | Complete |
| `REV-STATUS-001` | 2817831 | Implemented, evaluated, and aspirational claims are blended | Three-level status table based on pushed feature branches | 208 | `Table~\ref{tab:status} distinguishes` | 238 | [implementation-status.md](implementation-status.md) | Complete |
| `REV-SUCCESS-001` | 2817478 | Student success is undefined | Longitudinal success separated from proximal self-reported readiness | 299 | `In this paper, distal` | 338 | [student-success-definition.md](student-success-definition.md) | Complete |
| `REV-WEIGHT-001` | 2817476 | Priority weights lack validation | Aggregate sensitivity analysis active; interpreted as local stability only | 349 | `We examined how alternative priority assignments` | 426 | [priority-weight-sensitivity.md](priority-weight-sensitivity.md) | Complete |
| `REV-MODEL-001` | 2817831 | Central prediction claims lack performance evidence | Leakage-safe KNN and mean-baseline metrics active; two more conservative alternatives retained as comments | 467 | `We reproduced a leakage-safe leave-one-out diagnostic` | 547 | [model-performance-options.md](model-performance-options.md) | Complete |
| `REV-BIMODAL-001` | 2817476 | Bimodal behavioral intention needs exploration | Four aggregate groups reported without significance testing or participant-level disclosure | 769 | `For each respondent, we averaged` | 843 | [behavioral-intention-subgroups.md](behavioral-intention-subgroups.md) | Complete |
| `REV-LIMITS-001` | 2817831 and 2817476 | Evidence and generalizability are overstated | Small pilot, longitudinal, fairness, advisor-usability, and institutional limits explicit | 833 | `The pilot's small sample` | 927 | [implementation-status.md](implementation-status.md) | Complete |
| `REV-FORMAT-001` | Author request | DSI final-format compliance | XeLaTeX, embedded Arial, 11 point, US Letter, one-inch margins, running header, no footer or page numbers, captions above | 1 | `% !TeX program = xelatex` | 1 | [dsi-format-compliance.md](dsi-format-compliance.md) | Complete |
| `REV-REFS-001` | 2817478 | New comparison sources required | Complete AI-edit bibliography added without changing the original bibliography; provenance bibliography retained separately | 79 | `\addbibresource{submission/main-v4-ai-edit-references.bib}` | 87 | [main-v4-ai-edit-references.bib](../main-v4-ai-edit-references.bib) | Complete |

## Alternative documents

The active comparison is documented in [comparison-transfer-specific.md](comparison-transfer-specific.md).

The balanced alternative is documented in [comparison-balanced.md](comparison-balanced.md).

The academic-prototype alternative is documented in [comparison-academic-prototypes.md](comparison-academic-prototypes.md).

All three model treatments are documented in [model-performance-options.md](model-performance-options.md).

## Pushed implementation evidence

Fresh detached worktrees were created beneath `ai-workspace/worktrees/paper-revision/` after fetching the requested remote branches.

| Repository | Remote branch | Inspected commit |
| --- | --- | --- |
| frontend | `origin/feat-v2-target-factor-survey` | `615d76cdf1945316f5f4744d0d66a1b956219cd0` |
| backend | `origin/feat-survey-v2(target+factor)` | `b0fd2cd7954a1dfd3f6fbe32eec1cc8353fa2650` |
| model | `origin/feat-target-factors-with-success-rate` | `3a3a4c8bc6a39ebfaedbfeab184aa5d8cc3b6278` |

Local integration branches and their uncommitted changes were not used as implementation evidence.

## Reproduction

`analysis/behavioral_intention_analysis.py` reproduces aggregate behavioral-intention findings from the existing Qualtrics CSV.

`analysis/model_evidence_analysis.py` reproduces the KNN diagnostic and priority-weight sensitivity results from the pushed model notebook.

`analysis/verify_abstract.py` performs a LaTeX-aware count of the active abstract and fails above 100 words.
