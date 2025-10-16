"""Dataset loading and registry helpers."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Iterator


@dataclass(frozen=True)
class StereoImagePair:
    """Lightweight container for a single stereo pair."""

    left: Path
    right: Path
    metadata: Dict[str, str]

    def exists(self) -> bool:
        """Return True if both image files exist on disk."""
        return self.left.exists() and self.right.exists()


class StereoDatasetRegistry:
    """A small registry for dataset roots.

    This enables scripts and notebooks to reference datasets by name without
    hard-coding directory paths throughout the codebase.
    """

    def __init__(self) -> None:
        self._entries: Dict[str, Path] = {}

    def register(self, name: str, root: Path) -> None:
        """Register (or overwrite) the root directory for a dataset."""
        self._entries[name] = root.resolve()

    def get(self, name: str) -> Path:
        """Return the dataset root path or raise a KeyError if unknown."""
        if name not in self._entries:
            known = ", ".join(sorted(self._entries)) or "none"
            raise KeyError(f"Unknown dataset '{name}'. Known datasets: {known}")
        return self._entries[name]

    def items(self) -> Iterable[tuple[str, Path]]:
        """Yield (name, root_path) pairs."""
        return self._entries.items()


def discover_dataset(root: Path, left_suffix: str = "_L", right_suffix: str = "_R") -> Iterator[StereoImagePair]:
    """Yield stereo image pairs from a dataset root.

    Args:
        root: Directory to scan for stereo image pairs.
        left_suffix: Identifier appended to the left image stem (before the suffix).
        right_suffix: Identifier appended to the right image stem.

    Yields:
        :class:`StereoImagePair` objects for every matching pair discovered.

    Notes:
        The discovery strategy is intentionally simple: it looks for files with
        a common stem and the provided suffixes. Any additional metadata files
        (for example, timestamps) can be passed in by the caller via the returned
        object's ``metadata`` attribute.
    """

    root = root.resolve()
    if not root.exists():
        raise FileNotFoundError(f"Dataset root does not exist: {root}")

    by_stem: Dict[str, Dict[str, Path]] = {}
    for path in root.glob("**/*"):
        if not path.is_file():
            continue

        stem = path.stem
        if stem.endswith(left_suffix):
            base = stem[: -len(left_suffix)]
            by_stem.setdefault(base, {})["left"] = path
        elif stem.endswith(right_suffix):
            base = stem[: -len(right_suffix)]
            by_stem.setdefault(base, {})["right"] = path

    for base, matches in sorted(by_stem.items()):
        left = matches.get("left")
        right = matches.get("right")
        if left and right:
            metadata: Dict[str, str] = {"pair_id": base}
            yield StereoImagePair(left=left, right=right, metadata=metadata)
