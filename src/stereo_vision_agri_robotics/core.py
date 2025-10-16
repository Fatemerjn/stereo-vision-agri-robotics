"""Core helpers for the package."""

from typing import Dict


def info() -> Dict[str, str]:
    """Return basic package info for tests and quick checks.

    Returns:
        A dict with name and version.
    """
    return {"name": "stereo-vision-agri-robotics", "version": __import__("stereo_vision_agri_robotics").__version__}
