"""Post-processing utilities for stereo disparity results."""

from __future__ import annotations

from typing import Iterable, List, Sequence


def apply_confidence_mask(
    disparity_map: Sequence[Sequence[float]],
    confidence_map: Sequence[Sequence[float]] | None = None,
    *,
    threshold: float = 0.5,
    invalid_value: float = 0.0,
) -> List[List[float]]:
    """Mask a disparity map based on a confidence estimate.

    Args:
        disparity_map: Nested sequence representation of the disparity map.
        confidence_map: Confidence scores aligned with the disparity map. If
            ``None``, a copy of the disparity map is returned.
        threshold: Minimum confidence required to keep a disparity value.
        invalid_value: Value written where the confidence is below the threshold.

    Returns:
        A masked disparity map. The function always returns a deep copy to avoid
        mutating the caller's data structures.
    """

    if confidence_map is None:
        return [list(row) for row in disparity_map]

    if len(disparity_map) != len(confidence_map):
        raise ValueError("Disparity map and confidence map must have the same number of rows.")

    masked: List[List[float]] = []
    for row_idx, (disparity_row, confidence_row) in enumerate(zip(disparity_map, confidence_map)):
        if len(disparity_row) != len(confidence_row):
            raise ValueError(
                f"Row {row_idx} has mismatched lengths: disparity={len(disparity_row)}, "
                f"confidence={len(confidence_row)}"
            )

        masked_row = [
            value if confidence >= threshold else invalid_value
            for value, confidence in zip(disparity_row, confidence_row)
        ]
        masked.append(masked_row)
    return masked
