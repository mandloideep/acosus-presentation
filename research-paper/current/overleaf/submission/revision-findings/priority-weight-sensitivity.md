# Priority-weight sensitivity

Revision ID: `REV-WEIGHT-001`.

## Purpose

The reviewer requested empirical validation or, at minimum, a sensitivity analysis.

The current sample cannot validate the weights against longitudinal outcomes.

The analysis therefore asks how alternative priority assignments change the ten available readiness profiles.

## Method

The reproduction script parses the committed notebook’s deidentified encoded profiles and question priorities.

It reconstructs normalized option scores, applies the paper’s weighted aggregation, and uses logistic calibration with steepness (k=6).

The academic scenario doubles GPA, SAT, credits, courses, and prior academic or research experience.

The support and logistics scenario doubles scholarship, income, distance, and work priorities.

The one-at-a-time analysis changes each priority by plus or minus 20 percent.

## Results

| Scenario | Mean readiness | Range | Mean absolute change | Maximum absolute change | Rank correlation with baseline |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline | 82.27 | 72.25-91.38 | 0.00 | 0.00 | 1.000 |
| Equal weights | 81.10 | 67.82-91.16 | 1.77 | 5.24 | 0.988 |
| Double academic priorities | 81.35 | 71.27-91.92 | 1.22 | 2.63 | 0.964 |
| Double support and logistics priorities | 81.76 | 70.35-91.22 | 1.23 | 3.21 | 0.976 |

Across the 22 one-at-a-time perturbations, the mean absolute score change was 0.34 points, the maximum change was 1.23 points, and the minimum rank correlation was 0.988.

## Interpretation

The observed rankings were locally stable under the tested alternatives, although equal weighting shifted one score by more than five points.

This does not establish that the baseline priorities are correct.

It does not validate readiness as a predictor of persistence or completion.

Future validation must estimate or revise weights using longitudinal outcomes and larger samples.

## Reproduction and insertion

Reproduction script: `analysis/model_evidence_analysis.py`.

Insert a compact table and cautious interpretation after the priority-weight equation and example priorities.

The original section begins near submitted-paper line 351.
