#!/usr/bin/env python3
"""Reproduce KNN diagnostics and priority-weight sensitivity from the pushed notebook."""

from __future__ import annotations

import argparse
import io
import json
import math
import re
from pathlib import Path

import numpy as np
import pandas as pd


ACADEMIC_QUESTIONS = {"gpa", "sat", "credits", "courses", "experience"}
SUPPORT_LOGISTICS_QUESTIONS = {"scholarship", "income", "distance", "work"}


def source_text(cell: dict) -> str:
    source = cell.get("source", [])
    return "".join(source) if isinstance(source, list) else str(source)


def output_text(cell: dict) -> str:
    chunks: list[str] = []
    for output in cell.get("outputs", []):
        text = output.get("text", "")
        chunks.append("".join(text) if isinstance(text, list) else str(text))
    return "".join(chunks)


def output_html(cell: dict) -> str:
    for output in cell.get("outputs", []):
        html = output.get("data", {}).get("text/html")
        if html:
            return "".join(html) if isinstance(html, list) else str(html)
    raise ValueError("Expected an HTML table in the selected notebook cell.")


def parse_notebook(notebook_path: Path) -> tuple[pd.DataFrame, np.ndarray, pd.DataFrame]:
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    cells = notebook["cells"]

    encoded_cell = next(
        cell for cell in cells if "Encoded training DataFrame" in source_text(cell)
    )
    features = pd.read_html(io.StringIO(output_html(encoded_cell)))[0]
    features = features.loc[
        :, ~features.columns.astype(str).str.startswith("Unnamed")
    ].astype(float)

    labels_match = re.search(r"Labels:\s*(\[[^\]]+\])", output_text(encoded_cell))
    if not labels_match:
        raise ValueError("Could not locate the label vector in notebook output.")
    labels = np.asarray(json.loads(labels_match.group(1)), dtype=float)

    schema_cell = next(
        cell for cell in cells if "Schema summary table" in source_text(cell)
    )
    schema = pd.read_html(io.StringIO(output_html(schema_cell)))[0]
    schema = schema.loc[:, ~schema.columns.astype(str).str.startswith("Unnamed")]

    if len(features) != len(labels):
        raise ValueError("Feature and label counts do not match.")
    return features, labels, schema


def standardize(training: np.ndarray, test: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    mean = training.mean(axis=0)
    standard_deviation = training.std(axis=0, ddof=0)
    standard_deviation = np.where(standard_deviation == 0, 1.0, standard_deviation)
    return (
        (training - mean) / standard_deviation,
        (test - mean) / standard_deviation,
    )


def distance_weighted_knn(
    training: np.ndarray, labels: np.ndarray, test: np.ndarray, k: int
) -> float:
    distances = np.sqrt(np.square(training - test).sum(axis=1))
    neighbor_indices = np.argsort(distances, kind="stable")[:k]
    neighbor_distances = distances[neighbor_indices]
    neighbor_labels = labels[neighbor_indices]
    exact_matches = neighbor_distances == 0
    if exact_matches.any():
        return float(neighbor_labels[exact_matches].mean())
    weights = 1.0 / neighbor_distances
    return float(np.average(neighbor_labels, weights=weights))


def regression_metrics(actual: np.ndarray, predicted: np.ndarray) -> dict:
    errors = actual - predicted
    mean_actual = actual.mean()
    total_sum_squares = np.square(actual - mean_actual).sum()
    residual_sum_squares = np.square(errors).sum()
    return {
        "mae": float(np.abs(errors).mean()),
        "rmse": float(np.sqrt(np.square(errors).mean())),
        "max_error": float(np.abs(errors).max()),
        "r2": float(1 - residual_sum_squares / total_sum_squares),
    }


def leakage_safe_loocv(features: pd.DataFrame, labels: np.ndarray, k: int = 3) -> dict:
    matrix = features.to_numpy(dtype=float)
    predictions = []
    baselines = []
    for test_index in range(len(labels)):
        train_mask = np.arange(len(labels)) != test_index
        training_scaled, test_scaled = standardize(
            matrix[train_mask], matrix[[test_index]]
        )
        predictions.append(
            distance_weighted_knn(
                training_scaled,
                labels[train_mask],
                test_scaled[0],
                min(k, int(train_mask.sum())),
            )
        )
        baselines.append(float(labels[train_mask].mean()))

    return {
        "knn": regression_metrics(labels, np.asarray(predictions)),
        "leave_one_out_mean_baseline": regression_metrics(
            labels, np.asarray(baselines)
        ),
    }


def normalized_response_scores(features: pd.DataFrame) -> pd.DataFrame:
    """Recover question-level normalized PWRS inputs from encoded notebook features."""
    scores = pd.DataFrame(index=features.index)
    maximum_weights = {
        "gpa": 9,
        "sat": 9,
        "credits": 9,
        "courses": 9,
        "distance": 9,
        "work": 9,
        "interested": 9,
        "experience": 9,
    }
    for question, maximum in maximum_weights.items():
        scores[question] = features[question] / maximum

    scores["scholarship"] = np.where(features["scholarship_yes"] == 1, 1.0, 0.1)
    scores["income"] = np.where(features["income_yes"] == 1, 1.0, 0.1)
    scores["career"] = 1.0
    return scores


def logistic_score(base_score: np.ndarray, steepness: float = 6.0) -> np.ndarray:
    return 100.0 / (1.0 + np.exp(-steepness * (base_score - 0.5)))


def calculate_readiness(scores: pd.DataFrame, priorities: pd.Series) -> np.ndarray:
    aligned_priorities = priorities.reindex(scores.columns).astype(float)
    base_score = scores.mul(aligned_priorities, axis=1).sum(axis=1) / aligned_priorities.sum()
    return logistic_score(base_score.to_numpy(dtype=float))


def rank_correlation(left: np.ndarray, right: np.ndarray) -> float:
    return float(pd.Series(left).rank().corr(pd.Series(right).rank()))


def scenario_summary(baseline: np.ndarray, scenario: np.ndarray) -> dict:
    absolute_delta = np.abs(scenario - baseline)
    return {
        "mean": float(scenario.mean()),
        "range": [float(scenario.min()), float(scenario.max())],
        "mean_absolute_delta": float(absolute_delta.mean()),
        "maximum_absolute_delta": float(absolute_delta.max()),
        "rank_correlation_with_baseline": rank_correlation(baseline, scenario),
    }


def priority_sensitivity(features: pd.DataFrame, schema: pd.DataFrame) -> dict:
    scores = normalized_response_scores(features)
    priorities = schema.set_index("Question")["Priority Score"].astype(float)
    priorities = priorities.reindex(scores.columns)
    baseline = calculate_readiness(scores, priorities)

    equal_priorities = pd.Series(1.0, index=priorities.index)
    academic_priorities = priorities.copy()
    academic_priorities.loc[list(ACADEMIC_QUESTIONS)] *= 2
    support_priorities = priorities.copy()
    support_priorities.loc[list(SUPPORT_LOGISTICS_QUESTIONS)] *= 2

    perturbation_deltas = []
    perturbation_correlations = []
    for question in priorities.index:
        for multiplier in (0.8, 1.2):
            perturbed = priorities.copy()
            perturbed.loc[question] *= multiplier
            scenario = calculate_readiness(scores, perturbed)
            perturbation_deltas.extend(np.abs(scenario - baseline).tolist())
            perturbation_correlations.append(rank_correlation(baseline, scenario))

    return {
        "baseline": {
            "mean": float(baseline.mean()),
            "range": [float(baseline.min()), float(baseline.max())],
        },
        "equal_weights": scenario_summary(
            baseline, calculate_readiness(scores, equal_priorities)
        ),
        "double_academic_priorities": scenario_summary(
            baseline, calculate_readiness(scores, academic_priorities)
        ),
        "double_support_logistics_priorities": scenario_summary(
            baseline, calculate_readiness(scores, support_priorities)
        ),
        "one_at_a_time_plus_minus_20_percent": {
            "mean_absolute_delta": float(np.mean(perturbation_deltas)),
            "maximum_absolute_delta": float(np.max(perturbation_deltas)),
            "minimum_rank_correlation": float(np.min(perturbation_correlations)),
            "scenario_count": int(len(priorities) * 2),
        },
    }


def rounded(value):
    if isinstance(value, dict):
        return {key: rounded(item) for key, item in value.items()}
    if isinstance(value, list):
        return [rounded(item) for item in value]
    if isinstance(value, float):
        return round(value, 3)
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook", type=Path, help="Path to knn_pipeline_analysis.ipynb.")
    args = parser.parse_args()

    features, labels, schema = parse_notebook(args.notebook)
    result = {
        "source": str(args.notebook),
        "sample_count": int(len(labels)),
        "feature_count": int(features.shape[1]),
        "model_configuration": {
            "algorithm": "distance-weighted KNN regression",
            "k": 3,
            "metric": "Euclidean distance",
            "preprocessing": "StandardScaler refitted within each leave-one-out fold",
        },
        "label_summary": {
            "minimum": float(labels.min()),
            "maximum": float(labels.max()),
            "mean": float(labels.mean()),
            "population_standard_deviation": float(labels.std(ddof=0)),
        },
        "leakage_safe_leave_one_out": leakage_safe_loocv(features, labels),
        "priority_sensitivity": priority_sensitivity(features, schema),
    }
    print(json.dumps(rounded(result), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
