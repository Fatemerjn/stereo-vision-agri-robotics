"""Filesystem helpers used by scripts and pipeline components."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List


def resolve_path(path_like: str | Path) -> Path:
    """Resolve a path-like input into an absolute :class:`Path` object."""
    return Path(path_like).expanduser().resolve()


def list_images(root: str | Path, *, extensions: Iterable[str] | None = None) -> List[Path]:
    """List image files in a directory.

    Args:
        root: Directory to scan recursively.
        extensions: Optional iterable of lowercase file extensions to include.
            When ``None`` a sensible default is used.
    """

    path = resolve_path(root)
    if not path.exists():
        raise FileNotFoundError(f"Directory does not exist: {path}")
    if not path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {path}")

    normalized_extensions = {ext.lower() for ext in (extensions or {".png", ".jpg", ".jpeg", ".bmp"})}

    images: List[Path] = []
    for candidate in path.rglob("*"):
        if candidate.is_file() and candidate.suffix.lower() in normalized_extensions:
            images.append(candidate)
    return sorted(images)


def load_image_bytes(path: str | Path) -> bytes:
    """Return the raw bytes of an image file.

    Keeping the utility free of IOCV ensures it works in environments without
    native OpenCV bindings. Downstream code can convert the bytes into numpy
    arrays or PIL images as needed.
    """

    image_path = resolve_path(path)
    if not image_path.exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")
    return image_path.read_bytes()
