# === Stage 20: Аномальные значения ===
# Project: RepairCafe
"""repair_anomaly_simple: simple statistical outlier detection for numeric claim fields.

This module provides a small, self-contained utility to flag anomalous values
in a numeric field of repair claims using basic statistics (z-score based).
It depends only on the Python standard library and does not import project code.
"""

import math
from typing import Iterable, List, Optional, Tuple


def _mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean of numeric values, or 0.0 for empty input."""
    total = sum(values)
    return total / len(values) if values else 0.0


def _standard_deviation(values: Iterable[float]) -> float:
    """Return the population standard deviation, or 0.0 for fewer than 2 values."""
    values = list(values)
    if len(values) < 2:
        return 0.0
    average = _mean(values)
    variance = sum((item - average) ** 2 for item in values) / len(values)
    return math.sqrt(variance)


def z_scores(values: Iterable[float], threshold: float = 3.0) -> List[float]:
    """Compute the z-score for each numeric value.

    The z-score measures how many standard deviations an observation is from
    the mean. When the standard deviation is zero (constant field) all scores
    are defined as zero, meaning no value stands out.
    """
    values = list(values)
    if len(values) < 2:
        return [0.0] * len(values)
    average = _mean(values)
    spread = _standard_deviation(values)
    if spread == 0.0:
        return [0.0] * len(values)
    return [(value - average) / spread for value in values]


def find_anomalies(values: Iterable[float], threshold: float = 3.0) -> List[Tuple[float, float]]:
    """Return pairs of (value, z_score) for values considered anomalous.

    A value is anomalous when its absolute z-score exceeds the given threshold.
    The threshold defaults to 3.0, a common choice known as the "three-sigma rule".
    """
    anomalies = []
    for value, score in zip(values, z_scores(values, threshold)):
        if abs(score) > threshold:
            anomalies.append((value, score))
    return anomalies


def is_anomalous(value: float, values: Iterable[float], threshold: float = 3.0) -> bool:
    """Return True when a single value is an outlier relative to a reference list."""
    return any(
        abs(score) > threshold
        for score in z_scores([value, *values], threshold)
    )


def detect_anomalies_in_claim_field(
    field_name: str,
    records: Iterable[dict],
    threshold: float = 3.0,
) -> List[Tuple[dict, float, float]]:
    """Scan a collection of claim records and flag anomalous field values.

    Each record is expected to be a mapping that contains the numeric field.
    The function returns a list of tuples: (record, value, z_score) for every
    anomalous entry found in the specified field.
    """
    results = []
    collected = [record[field_name] for record in records if field_name in record]
    for record in records:
        if field_name not in record:
            continue
        value = record[field_name]
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            continue
        scores = z_scores([value, *collected], threshold)
        for score in scores:
            if abs(score) > threshold:
                results.append((record, value, score))
                break
    return results
