"""Core helpers for the Stereo Vision Agri Robotics package."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable

from .config import StereoVisionConfig
from .datasets import StereoDatasetRegistry
from .pipeline import CalibrationParameters, StereoCameraModel, compute_rectification_parameters


def info() -> Dict[str, str]:
    """Return package metadata useful for quick checks and CLI banners."""

    package = __import__("stereo_vision_agri_robotics")
    return {
        "name": "stereo-vision-agri-robotics",
        "version": package.__version__,
        "modules": "datasets,pipeline,utils",
    }


def build_default_config(workspace_root: str | Path) -> StereoVisionConfig:
    """Create a default configuration for a given workspace root."""

    return StereoVisionConfig.from_workspace(workspace_root)


def create_dataset_registry(workspace_root: str | Path, dataset_names: Iterable[str]) -> StereoDatasetRegistry:
    """Initialise a dataset registry from a list of dataset directory names."""

    root_path = Path(workspace_root).resolve()
    registry = StereoDatasetRegistry()
    for name in dataset_names:
        registry.register(name, root_path / "data" / name)
    return registry


def default_calibration(camera: StereoCameraModel | None = None) -> CalibrationParameters:
    """Return placeholder calibration parameters for the provided camera."""

    model = camera or StereoCameraModel(focal_length=35.0, baseline=0.12, principal_point=(0.0, 0.0))
    return compute_rectification_parameters(model)
