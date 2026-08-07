# Model-performance treatment options

Revision ID: `REV-MODEL-001`.

The pilot did not evaluate a trained predictive model.

The pushed model branch contains a post-pilot distance-weighted KNN implementation and an executed notebook with ten readiness labels and seventeen encoded features.

The notebook’s reusable model utility scales the complete dataset before leave-one-out evaluation, so it is not used for the paper’s diagnostic.

The revision analysis instead refits the scaler inside every leave-one-out fold.

## Option A: Cautious numeric diagnostic

This is the active option.

The KNN uses three neighbors, distance weighting, Euclidean distance, and fold-specific standardization.

Leakage-safe leave-one-out evaluation produced MAE 4.63, RMSE 5.91, maximum absolute error 13.81, and (R^2=-0.26).

The leave-one-out mean baseline produced MAE 4.38, RMSE 5.85, and (R^2=-0.24).

The KNN did not outperform the simple baseline.

These readiness labels range from 56.8 to 75.6 and are deterministic survey composites rather than observed persistence, credit accumulation, or completion outcomes.

The result is a technical diagnostic that supports deferring predictive claims.

It is not evidence of predictive validity.

## Option B: Methods without numeric results

State that a post-pilot KNN implementation exists and that future evaluation will use leakage-safe resampling and comparison against simple baselines.

Do not include current error values because the ten labels are readiness composites and the model has not been evaluated against observed longitudinal outcomes.

If selected, remove the numeric diagnostic paragraph and retain the implementation-status table.

## Option C: Complete metric deferral

State only that no trained predictor was evaluated in the pilot and that predictive performance remains outside the evidence presented in the paper.

If selected, remove the post-pilot KNN paragraph, its commented numeric option, and KNN-specific language from the conclusion.

## Evidence and reproduction

Source notebook: `ai-workspace/worktrees/paper-revision/model/notebooks/knn_pipeline_analysis.ipynb` at commit `3a3a4c8bc6a39ebfaedbfeab184aa5d8cc3b6278`.

Reproduction script: `analysis/model_evidence_analysis.py`.

The script parses the deidentified encoded feature table and label vector from committed notebook outputs and emits aggregates only.

## Insertion and downstream edits

Insert Option A after the implementation-status table and before the proposed research roadmap.

The original pipeline discussion begins near submitted-paper line 467.

The stable anchor is the subsection originally titled `Progressive Learning Framework`.

Ensure the abstract, contributions, evaluation opening, limitations, and conclusion do not treat this diagnostic as pilot evidence.
