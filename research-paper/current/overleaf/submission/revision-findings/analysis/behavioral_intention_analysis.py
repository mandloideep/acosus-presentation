#!/usr/bin/env python3
"""Reproduce aggregate behavioral-intention subgroup results without PII output."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


LIKERT_MAP = {
    "Strongly disagree": 1,
    "Somewhat disagree": 2,
    "Neither agree nor disagree": 3,
    "Somewhat agree": 4,
    "Strongly agree": 5,
}

SCALE_MAPS = {
    "Q7": {
        "Not at all accurate": 1,
        "Slightly accurate": 2,
        "Moderately accurate": 3,
        "Very accurate": 4,
        "Extremely accurate": 5,
    },
    "Q8": {
        "Not at all aligned": 1,
        "Slightly aligned": 2,
        "Somewhat aligned": 3,
        "Very aligned": 4,
        "Perfectly aligned": 5,
    },
    "Q9": {
        "Not relevant at all": 1,
        "Not at all relevant": 1,
        "Slightly relevant": 2,
        "Moderately relevant": 3,
        "Very relevant": 4,
        "Extremely relevant": 5,
    },
    "Q10": {
        "Not actionable": 1,
        "Slightly actionable": 2,
        "Somewhat difficult to implement": 2,
        "Moderately actionable": 3,
        "Reasonably actionable": 4,
        "Easily actionable": 5,
    },
}


def build_cohort(csv_path: Path) -> pd.DataFrame:
    """Apply the submitted-paper cohort rules in memory."""
    data = pd.read_csv(csv_path, skiprows=[1, 2])

    email = data["student_email"].astype(str)
    data = data[~email.str.contains("test", case=False, na=False)].copy()

    data["_finished"] = (
        data["Finished"].astype(str).str.lower().eq("true").astype(int)
    )
    data["_progress"] = pd.to_numeric(
        data["Progress"], errors="coerce"
    ).fillna(0)
    data["_nonnull"] = data.notna().sum(axis=1)
    data = data.sort_values(
        ["_finished", "_progress", "_nonnull"], ascending=False
    )

    has_email = data["student_email"].notna() & data[
        "student_email"
    ].astype(str).str.strip().ne("")
    duplicate_indices = data[has_email].index[
        data[has_email].duplicated(subset="student_email", keep="first")
    ]
    data = data.drop(index=duplicate_indices)
    data = data.drop(columns=["_finished", "_progress", "_nonnull"])
    return data.sort_values("RecordedDate").reset_index(drop=True)


def prepare_scores(data: pd.DataFrame) -> pd.DataFrame:
    """Map survey responses to the published 1-to-5 scales."""
    scored = data.copy()
    usefulness_columns = [f"Q1_{index}" for index in range(1, 7)]
    ease_columns = [f"Q2_{index}" for index in range(1, 7)]

    usefulness = scored[usefulness_columns].apply(
        lambda column: column.map(LIKERT_MAP)
    )
    ease = scored[ease_columns].apply(lambda column: column.map(LIKERT_MAP))
    scored["Perceived usefulness"] = usefulness.mean(axis=1)
    scored["Perceived ease of use"] = ease.mean(axis=1)

    metric_names = {
        "Q7": "System accuracy",
        "Q8": "Probability alignment",
        "Q9": "Recommendation relevance",
        "Q10": "Actionability",
    }
    for column, scale_map in SCALE_MAPS.items():
        scored[metric_names[column]] = scored[column].map(scale_map)

    scored["Likelihood to continue"] = pd.to_numeric(
        scored["Q13_1"], errors="coerce"
    ).replace(0, np.nan)
    scored["Likelihood to recommend"] = pd.to_numeric(
        scored["Q13_2"], errors="coerce"
    ).replace(0, np.nan)
    scored["Behavioral intention composite"] = scored[
        ["Likelihood to continue", "Likelihood to recommend"]
    ].mean(axis=1)

    composite = scored["Behavioral intention composite"]
    scored["Subgroup"] = np.select(
        [composite.ge(4), composite.le(2), composite.notna()],
        ["enthusiastic", "skeptical", "intermediate"],
        default="missing both intention items",
    )
    return scored


def rounded_or_none(value: float) -> float | None:
    if pd.isna(value):
        return None
    return round(float(value), 2)


def summarize(scored: pd.DataFrame) -> dict:
    metric_columns = [
        "Perceived usefulness",
        "Perceived ease of use",
        "System accuracy",
        "Probability alignment",
        "Recommendation relevance",
        "Actionability",
    ]
    subgroup_order = [
        "enthusiastic",
        "skeptical",
        "intermediate",
        "missing both intention items",
    ]

    groups = {}
    for group in subgroup_order:
        subset = scored[scored["Subgroup"] == group]
        groups[group] = {
            "n": int(len(subset)),
            "means": {
                metric: rounded_or_none(subset[metric].mean())
                for metric in metric_columns
            },
        }

    complete_intention = scored.dropna(
        subset=["Likelihood to continue", "Likelihood to recommend"]
    )
    complete_case_groups = {
        str(group): int(count)
        for group, count in complete_intention["Subgroup"].value_counts().items()
    }
    return {
        "analysis_cohort_n": int(len(scored)),
        "missing_rule": "Zero is outside the 1-to-5 intention scale and is treated as missing.",
        "subgroup_rule": (
            "The respondent-level mean of available intention items defines "
            "enthusiastic (>=4), skeptical (<=2), intermediate (>2 and <4), "
            "or missing when both items are absent."
        ),
        "intention_items": {
            "likelihood_to_continue": {
                "n": int(scored["Likelihood to continue"].notna().sum()),
                "mean": rounded_or_none(scored["Likelihood to continue"].mean()),
            },
            "likelihood_to_recommend": {
                "n": int(scored["Likelihood to recommend"].notna().sum()),
                "mean": rounded_or_none(scored["Likelihood to recommend"].mean()),
            },
        },
        "groups": groups,
        "complete_case_intention_n": int(len(complete_intention)),
        "complete_case_groups": complete_case_groups,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=Path, help="Path to the raw Qualtrics CSV.")
    parser.add_argument(
        "--expected-n",
        type=int,
        default=10,
        help="Fail if cohort cleaning does not produce this sample size.",
    )
    args = parser.parse_args()

    cohort = build_cohort(args.csv)
    if len(cohort) != args.expected_n:
        raise SystemExit(
            f"Expected {args.expected_n} analysis responses, found {len(cohort)}."
        )

    result = summarize(prepare_scores(cohort))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
