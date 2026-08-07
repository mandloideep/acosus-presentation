# Behavioral-intention subgroups

Revision ID: `REV-BIMODAL-001`.

## Cohort and missing-data rules

The analysis skips the two Qualtrics metadata rows, excludes internal test accounts, and retains the most complete repeated submission for identified respondents.

Anonymous 2025 responses are retained.

This produces the submitted-paper cohort of ten respondents.

Behavioral-intention values of zero are outside the 1-to-5 response scale and are treated as missing.

The respondent-level mean of available intention items defines enthusiastic respondents at 4 or above, skeptical respondents at 2 or below, and intermediate respondents between those thresholds.

One respondent is missing both items.

## Results

| Group | N | PU | PEOU | Accuracy | Alignment | Relevance | Actionability |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Enthusiastic | 3 | 4.83 | 5.00 | 4.67 | 4.67 | 4.67 | 5.00 |
| Skeptical | 4 | 2.71 | 3.62 | 2.25 | 2.00 | 2.25 | 2.50 |
| Intermediate | 2 | 2.92 | 3.75 | 4.50 | 3.00 | 2.50 | 3.00 |
| Missing both intention items | 1 | 2.50 | 4.33 | 4.00 | Not reported | 3.00 | 2.00 |

The enthusiastic group rated both usability and perceived value highly.

The skeptical group still rated ease of use above the scale midpoint but gave substantially lower usefulness, accuracy, alignment, relevance, and actionability ratings.

Open-ended responses from enthusiastic respondents emphasized speed, ease, and a positive interface experience.

Skeptical responses emphasized missing prerequisite or course-planning analysis, requests for deeper career exploration, or a preference for human advising.

A complete-case check using only respondents with both intention items retained the same directional contrast, with three enthusiastic, two skeptical, and two intermediate respondents.

## Interpretation

The comparison is descriptive and exploratory.

The group sizes are too small for inferential tests or population-level conclusions.

The pattern suggests that interface usability alone did not determine willingness to continue or recommend the system.

Perceived advising value and desired functionality appear more important candidates for future study.

## Reproduction and insertion

Reproduction script: `analysis/behavioral_intention_analysis.py`.

Insert the brief comparison after the existing bimodality paragraph near submitted-paper line 769.

Link the interpretation to the qualitative themes without exposing participant-level records.
