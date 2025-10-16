"""Stereo Vision Agri Robotics package."""

from .config import StereoVisionConfig
from .core import build_default_config, create_dataset_registry, default_calibration, info
from .datasets import StereoDatasetRegistry, StereoImagePair, discover_dataset
from .pipeline import (
    CalibrationParameters,
    StereoCameraModel,
    apply_confidence_mask,
    compute_disparity_map,
    compute_rectification_parameters,
)
from .utils import list_images, load_image_bytes, resolve_path

__all__ = [
    "__version__",
    "StereoVisionConfig",
    "StereoDatasetRegistry",
    "StereoImagePair",
    "StereoCameraModel",
    "CalibrationParameters",
    "info",
    "build_default_config",
    "create_dataset_registry",
    "default_calibration",
    "discover_dataset",
    "compute_rectification_parameters",
    "compute_disparity_map",
    "apply_confidence_mask",
    "list_images",
    "load_image_bytes",
    "resolve_path",
]

__version__ = "0.1.0"
