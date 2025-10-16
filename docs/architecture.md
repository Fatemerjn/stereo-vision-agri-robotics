# Architecture Overview

This document captures the key components that make up the stereo-vision toolkit.
It is intentionally concise and focuses on how the modules interact so future
contributors can extend the system with confidence.

## Package Modules

- `config.py` defines `StereoVisionConfig`, a dataclass capturing the workspace
  layout, default datasets, and the reference stereo camera model.
- `core.py` hosts top-level helpers for constructing common objects (dataset
  registries and calibration parameters) used throughout scripts and notebooks.
- `datasets/` contains primitives for discovering and handling stereo image
  pairs on disk. The `StereoDatasetRegistry` centralises dataset paths to keep
  scripts portable.
- `pipeline/` groups the processing stages required for a stereo-vision stack:
  calibration, disparity estimation, and post-processing. Each module exposes
  a narrow surface area so implementations can be swapped without touching
  downstream code.
- `utils/` bundles cross-cutting concerns (filesystem helpers, path resolution,
  and light I/O wrappers).

## Data Flow

1. **Dataset registration**: Workspaces call `create_dataset_registry` to map
   dataset names to directories under `data/`.
2. **Pair discovery**: `discover_dataset` returns `StereoImagePair` objects for
   each left/right image pair in a dataset, abstracting naming conventions.
3. **Calibration**: `default_calibration` wraps `compute_rectification_parameters`
   so scripts start with a deterministic calibration baseline before plugging in
   real calibration data.
4. **Disparity estimation**: `compute_disparity_map` currently implements a
   lightweight difference-based algorithm, making it trivial to unit test while
   leaving room for production-grade implementations.
5. **Post-processing**: `apply_confidence_mask` demonstrates how to blend
   disparity maps with confidence scores to produce usable depth maps.

## Future Enhancements

- Replace placeholder disparity logic with OpenCV block matching algorithms or
  deep-learning based estimators.
- Persist calibration and configuration artefacts to YAML so they can be shared
  between notebooks, scripts, and autonomous vehicle deployments.
- Add benchmarking utilities that track runtime, memory usage, and accuracy
  across datasets.
