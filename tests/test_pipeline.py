from pathlib import Path

import pytest

from stereo_vision_agri_robotics import (
    apply_confidence_mask,
    compute_disparity_map,
    create_dataset_registry,
    default_calibration,
    discover_dataset,
)


def test_compute_disparity_map_simple():
    left = [[10, 20], [30, 40]]
    right = [[1, 2], [3, 4]]
    disparity = compute_disparity_map(left, right)
    assert disparity == [[9.0, 18.0], [27.0, 36.0]]


def test_apply_confidence_mask_thresholding():
    disparity = [[0.5, 1.5], [2.5, 3.5]]
    confidence = [[0.9, 0.1], [0.8, 0.4]]
    masked = apply_confidence_mask(disparity, confidence, threshold=0.5, invalid_value=-1.0)
    assert masked == [[0.5, -1.0], [2.5, -1.0]]


def test_discover_dataset_pairs(tmp_path: Path):
    dataset_root = tmp_path / "low_light"
    dataset_root.mkdir()
    (dataset_root / "frame001_L.png").write_bytes(b"left")
    (dataset_root / "frame001_R.png").write_bytes(b"right")
    (dataset_root / "readme.txt").write_text("ignore me")

    pairs = list(discover_dataset(dataset_root))
    assert len(pairs) == 1
    pair = pairs[0]
    assert pair.metadata["pair_id"] == "frame001"
    assert pair.exists()


def test_create_dataset_registry(tmp_path: Path):
    data_dir = tmp_path / "data"
    (data_dir / "set_a").mkdir(parents=True)
    (data_dir / "set_b").mkdir()

    registry = create_dataset_registry(tmp_path, ["set_a", "set_b"])
    assert registry.get("set_a") == (tmp_path / "data" / "set_a").resolve()
    assert registry.get("set_b") == (tmp_path / "data" / "set_b").resolve()
    with pytest.raises(KeyError):
        registry.get("set_c")


def test_default_calibration_returns_identity():
    calibration = default_calibration()
    assert calibration.rotation == [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    assert calibration.translation[0] > 0
