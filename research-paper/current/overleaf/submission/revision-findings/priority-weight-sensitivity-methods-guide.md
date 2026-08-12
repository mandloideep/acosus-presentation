# Priority-Weight Sensitivity Methods Guide

## Purpose

This guide explains how the values in the paper's priority-weight sensitivity table were calculated.
It is intended to help the ACOSUS research team explain the analysis to reviewers and collaborators.
It does not establish that the baseline priorities are correct, and it does not validate the readiness score as a predictor of persistence, credit accumulation, or completion.

## Short explanation of the 5.24-point value

The 5.24-point value is the largest absolute difference between a profile's score under equal weighting and the same profile's score under the baseline priorities.
For the affected deidentified profile, the baseline-priority score was 78.11 and the equal-weight score was 72.87.
The signed difference was therefore -5.24 points, and its absolute value was 5.24 points.
This is a sensitivity difference produced by changing the priority configuration.
It is not a change observed in a student over time, a treatment effect, or a prediction error.

Across all ten profiles, the mean absolute difference under equal weighting was 1.77 points.
The maximum of those ten absolute differences was 5.24 points.

## Reproducible source snapshot

The analysis used ten deidentified Factor Survey profiles and the question schema stored in the executed model notebook below.

- Model notebook: `model/notebooks/knn_pipeline_analysis.ipynb`
- Verified worktree path: `ai-workspace/worktrees/paper-revision/model/notebooks/knn_pipeline_analysis.ipynb`
- Model commit: `3a3a4c8bc6a39ebfaedbfeab184aa5d8cc3b6278`
- Commit date: July 27, 2026
- Reproduction script: `revision-findings/analysis/model_evidence_analysis.py`
- Analysis sample: 10 deidentified profiles
- Questions used in the sensitivity calculation: 11 Factor Survey questions

The reproduction script parses the encoded feature table and question schema from the committed notebook outputs.
It then reconstructs normalized question-level responses, applies each priority scenario, and calculates the summary statistics reported in the paper.

## What baseline priorities mean

The baseline priorities are the numeric priority scores stored in the notebook's Factor Survey schema.
They describe the prototype's starting configuration for how much influence each question has in the weighted aggregation.
They are design values informed by the literature and the configured survey structure, not regression coefficients estimated from ACOSUS longitudinal outcomes.
A higher priority gives a question more influence in the weighted average, but it does not prove that the question has a larger causal or predictive effect.

The sum of the 11 baseline priorities is 74.

| Question ID | Question topic | Data type | Baseline priority | Option-weight range | Scenario group |
| --- | --- | --- | ---: | --- | --- |
| `gpa` | GPA | Ordinal | 9 | 2-9 | Academic |
| `sat` | SAT score | Ordinal | 8 | 2-9 | Academic |
| `credits` | Completed credits | Ordinal | 8 | 7-9 | Academic |
| `courses` | Number of courses selected | Ordinal | 7 | 6-9 | Academic |
| `scholarship` | Scholarship status | Cardinal | 4 | 1-10 | Support and logistics |
| `income` | Family income support | Cardinal | 4 | 1-10 | Support and logistics |
| `distance` | Distance from home to the university | Ordinal | 6 | 6-9 | Support and logistics |
| `work` | Employment status | Ordinal | 8 | 6-9 | Support and logistics |
| `career` | Career aspiration | Cardinal | 7 | 9-9 | Neither doubled group |
| `interested` | Interest in the courses | Ordinal | 4 | 4-9 | Neither doubled group |
| `experience` | Prior subject exposure, experience, and knowledge | Ordinal | 9 | 5-9 | Academic |

The exact question wording and option weightages are documented in `research-paper/02-surveys/survey-tables.md`.
The values used for this analysis come from the schema embedded in the model notebook at the commit listed above.

## Step 1: Normalize each selected response

For profile \(j\) and question \(i\), the selected option weight is divided by that question's maximum option weight:

\[
r_{ji} = \frac{w_{ji}^{\text{selected}}}{w_i^{\text{max}}}.
\]

This converts each response to a value between 0 and 1 before priorities are applied.
For example, a GPA option with weight 8 and maximum weight 9 becomes \(8/9 = 0.889\).
For the scholarship and income questions, a Yes response becomes \(10/10 = 1.0\), while a No response becomes \(1/10 = 0.1\).
Every career-aspiration option has weight 9, so that question normalizes to 1.0 for every profile in this schema.

## Step 2: Calculate the priority-weighted base score

For each profile, the normalized responses are multiplied by the scenario's priorities and divided by the sum of those priorities:

\[
b_j = \frac{\sum_i r_{ji}p_i}{\sum_i p_i}.
\]

Under the baseline scenario, \(p_i\) is the configured priority listed in the table above.
The resulting base score remains between 0 and 1.

## Step 3: Apply the bounded calibration

The reproduction applies the notebook's logistic calibration with steepness \(k=6\):

\[
s_j = \frac{100}{1 + \exp[-6(b_j - 0.5)]}.
\]

This maps the base score to the 0-100 readiness-score scale.
All four scenarios use the same normalization and calibration, so the only change between scenarios is the priority assignment.

## Step 4: Define the four scenarios

### Baseline priorities

Each question uses its configured priority from the notebook schema.
The priorities sum to 74.
This scenario is the reference used to calculate all differences.

### Equal weighting

Every question receives a priority of 1.
The priorities sum to 11.
This scenario tests what happens when no question is given more influence than another.

### Double academic priorities

The baseline priorities for `gpa`, `sat`, `credits`, `courses`, and `experience` are multiplied by 2.
All other priorities remain at their baseline values.
The priorities sum to 115.

### Double support and logistics priorities

The baseline priorities for `scholarship`, `income`, `distance`, and `work` are multiplied by 2.
All other priorities remain at their baseline values.
The priorities sum to 96.

## Step 5: Calculate the table columns

The calculations below are performed separately for each scenario.

### Mean

The mean is the arithmetic average of the ten recalculated profile scores:

\[
\text{Mean} = \frac{1}{10}\sum_{j=1}^{10}s_j^{\text{scenario}}.
\]

For equal weighting, the ten scenario scores average to 81.10.
This is different from the mean absolute difference of 1.77.

### Range

The range reports the minimum and maximum score among the ten profiles under that scenario.
For equal weighting, the minimum is 67.82 and the maximum is 91.16.

### Profile-level difference

Each scenario score is compared with the baseline score for the same profile:

\[
\Delta_j = s_j^{\text{scenario}} - s_j^{\text{baseline}}.
\]

A negative value means the alternative priority assignment produced a lower score for that profile.
A positive value means it produced a higher score.

### Mean absolute difference

The mean absolute difference averages the magnitudes of the ten profile-level differences:

\[
\text{Mean }|\Delta| = \frac{1}{10}\sum_{j=1}^{10}|\Delta_j|.
\]

Absolute values are used because upward and downward changes should not cancel each other.

### Maximum absolute difference

The maximum absolute difference is the largest magnitude among the ten profile-level differences:

\[
\text{Max }|\Delta| = \max_j |\Delta_j|.
\]

For equal weighting, this is the 5.24-point difference described at the beginning of this guide.

## Profile-level results

The profile labels below are analysis-row identifiers only.
They do not identify participants.
Values are rounded to two decimal places, as in the paper.

| Profile | Baseline | Equal weighting | Double academic | Double support and logistics |
| --- | ---: | ---: | ---: | ---: |
| P1 | 72.25 | 67.82 | 71.27 | 70.35 |
| P2 | 78.63 | 77.49 | 76.86 | 78.82 |
| P3 | 91.38 | 91.16 | 91.92 | 91.22 |
| P4 | 80.10 | 78.53 | 77.48 | 82.29 |
| P5 | 74.26 | 75.31 | 72.25 | 72.86 |
| P6 | 78.11 | 72.87 | 79.01 | 74.90 |
| P7 | 86.86 | 85.59 | 86.81 | 85.73 |
| P8 | 82.30 | 81.44 | 81.26 | 81.47 |
| P9 | 88.82 | 90.13 | 86.97 | 90.04 |
| P10 | 90.01 | 90.66 | 89.60 | 89.91 |

The unrounded P6 equal-weight difference is \(72.867 - 78.110 = -5.243\), which is reported as an absolute difference of 5.24 points after rounding.

## Summary values reported in the paper

| Scenario | Mean | Range | Mean absolute difference | Maximum absolute difference | Rank correlation with baseline |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline priorities | 82.27 | 72.25-91.38 | 0.00 | 0.00 | 1.000 |
| Equal weighting | 81.10 | 67.82-91.16 | 1.77 | 5.24 | 0.988 |
| Double academic priorities | 81.35 | 71.27-91.92 | 1.22 | 2.63 | 0.964 |
| Double support and logistics priorities | 81.76 | 70.35-91.22 | 1.23 | 3.21 | 0.976 |

The paper omits the rank-correlation column to keep the table compact.
The correlation values are included here because they help the research team understand whether the ordering of profiles changed under an alternative scenario.
They do not validate the score against an external outcome.

## How to interpret the results safely

The analysis answers a narrow question: how much do these ten calculated scores move when the priority configuration is changed in three specified ways?
The relatively small mean absolute differences indicate limited average movement within this set under the tested alternatives.
The 5.24-point maximum shows that an average can conceal a larger change for one profile.
Neither observation establishes that the baseline priorities are optimal.

The analysis should not be described as predictive validation because the scores are deterministic survey composites rather than observed longitudinal outcomes.
It should not be described as a fairness evaluation because the sample is too small and the analysis does not estimate group-level error or disparity.
It should not be described as evidence that equal weighting is better or worse because no external criterion is used to judge the scenarios.

## Reproduction command

From `research-paper/current/overleaf/submission`, run:

```bash
python3 revision-findings/analysis/model_evidence_analysis.py \
  /path/to/model/notebooks/knn_pipeline_analysis.ipynb
```

Use the model notebook at commit `3a3a4c8bc6a39ebfaedbfeab184aa5d8cc3b6278` to reproduce the values in this guide and the paper.
The script requires Python with NumPy, pandas, and an HTML-table parser available.

## Reviewer-ready explanation

The baseline priorities are prototype configuration values assigned to the 11 Factor Survey questions, not empirically estimated coefficients.
We tested sensitivity by recalculating the same ten deidentified profiles under equal weighting, doubled academic priorities, and doubled support and logistics priorities while holding response normalization and logistic calibration fixed.
For each scenario, we reported the mean and range of recalculated scores, the mean absolute difference from each profile's baseline score, and the largest such difference.
Under equal weighting, the average absolute difference was 1.77 points, and the largest absolute difference was 5.24 points for one profile, whose score decreased from 78.11 to 72.87.
These results describe local sensitivity to the tested priority assignments and do not establish optimal weights or predictive validity.
