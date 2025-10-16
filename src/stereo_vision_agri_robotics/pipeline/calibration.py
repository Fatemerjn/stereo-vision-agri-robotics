"""Calibration utilities for stereo camera systems."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


def _identity_3x3() -> List[List[float]]:
    """Return a 3x3 identity matrix."""
    return [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]


@dataclass(frozen=True)
class StereoCameraModel:
    """Minimal stereo camera model used for documentation and tests."""

    focal_length: float
    baseline: float
    principal_point: Tuple[float, float]


@dataclass(frozen=True)
class CalibrationParameters:
    """Container for rectification parameters."""

    rotation: List[List[float]]
    translation: List[float]
    left_rectification: List[List[float]]
    right_rectification: List[List[float]]


def compute_rectification_parameters(camera: StereoCameraModel) -> CalibrationParameters:
    """Return deterministic placeholder rectification parameters for a camera.

    The function intentionally avoids third-party dependencies so that unit
    tests remain lightweight. It is not meant to be a physically correct
    calibration routine, but instead captures all required artefacts (rotation,
    translation, rectification transforms) in a predictable format.
    """

    rotation = _identity_3x3()
    translation = [camera.baseline, 0.0, 0.0]
    left_rectification = _identity_3x3()
    right_rectification = _identity_3x3()

    return CalibrationParameters(
        rotation=rotation,
        translation=translation,
        left_rectification=left_rectification,
        right_rectification=right_rectification,
    )
