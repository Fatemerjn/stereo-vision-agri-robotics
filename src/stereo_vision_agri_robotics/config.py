"""Configuration helpers for reproducible experiments."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .pipeline.calibration import StereoCameraModel


@dataclass(frozen=True)
class StereoVisionConfig:
    """Top-level configuration object."""

    project_name: str
    workspace_root: Path
    default_dataset: Optional[str] = None
    camera: Optional[StereoCameraModel] = None

    @staticmethod
    def from_workspace(
        workspace_root: str | Path,
        project_name: str = "Stereo Vision for Agricultural Robotics",
    ) -> "StereoVisionConfig":
        """Create a configuration anchored at a workspace root."""
        root = Path(workspace_root).resolve()
        camera = StereoCameraModel(focal_length=35.0, baseline=0.12, principal_point=(0.0, 0.0))
        return StereoVisionConfig(project_name=project_name, workspace_root=root, camera=camera)
