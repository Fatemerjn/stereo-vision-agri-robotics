"""Disparity estimation helpers."""

from __future__ import annotations

from typing import Iterable, List, Sequence


def compute_disparity_map(
    left: Sequence[Sequence[float]],
    right: Sequence[Sequence[float]],
    *,
    invalid_value: float = 0.0,
) -> List[List[float]]:
    """Compute a lightweight disparity map by subtracting pixel intensities.

    Args:
        left: Left rectified image represented as a nested sequence (e.g. list of rows).
        right: Right rectified image represented as a nested sequence.
        invalid_value: Value to use when inputs have mismatched lengths.

    Returns:
        A list-of-lists disparity "map". The implementation uses a simple
        difference to keep the dependency surface minimal; replace this with a
        proper block matching or deep network implementation for production.
    """

    if len(left) != len(right):
        raise ValueError("Left and right images must have the same number of rows.")

    disparity: List[List[float]] = []
    for row_index, (left_row, right_row) in enumerate(zip(left, right)):
        if len(left_row) != len(right_row):
            # We choose to pad the shorter row to keep the output rectangular.
            max_len = max(len(left_row), len(right_row))
            padded_left = list(left_row) + [0.0] * (max_len - len(left_row))
            padded_right = list(right_row) + [0.0] * (max_len - len(right_row))
            left_row = padded_left
            right_row = padded_right
        disparity.append([float(l) - float(r) for l, r in zip(left_row, right_row)])
    return disparity
