# Stereo Vision for Agricultural Robotics

A research-friendly Python starter kit for designing and evaluating stereo-vision
pipelines in agricultural robotics. The repository couples a lightweight
processing library with notebooks, utility scripts, and documentation that
encourage reproducible experiments.

## Highlights
- Modular pipeline components for calibration, disparity estimation, and post-processing.
- Dataset discovery helpers and filesystem utilities tailored to stereo image pairs.
- Reproducible development workflow with linting, type checking, and tests.
- Jupyter notebooks and scripts for data exploration and quick experimentation.

## Project Structure

```
stereo-vision-agri-robotics/
├── docs/                     # Long-form documentation and design notes
├── notebooks/                # Jupyter notebooks for experiments and reports
├── scripts/                  # Reusable CLI utilities (e.g., dataset downloads)
├── src/stereo_vision_agri_robotics/
│   ├── config.py             # Workspace configuration helpers
│   ├── core.py               # Package orchestration utilities
│   ├── datasets/             # Dataset registry and discovery helpers
│   ├── pipeline/             # Calibration, disparity, post-processing modules
│   └── utils/                # Filesystem helpers and general utilities
├── tests/                    # Pytest test suite
├── requirements.txt          # Runtime dependencies
├── requirements-dev.txt      # Development and QA dependencies
├── pyproject.toml            # Packaging metadata and tool configuration
└── Makefile                  # Common developer tasks
```

## Getting Started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
```

Smoke-test the installation:

```bash
make test
```

## Development Workflow

- `make lint` — run Ruff for static analysis and style checks.
- `make format` — apply Black to the source and test suites.
- `make typecheck` — enforce typing guarantees with MyPy.
- `make test` — execute the full Pytest suite.

All targets create and use the local `.venv` virtual environment automatically.

## Working with Data

1. Download a sample stereo pair:

   ```bash
   scripts/download_sample_dataset.py data/sample
   ```

2. Register datasets in code using `create_dataset_registry` and discover pairs
   with `discover_dataset`.

Notebooks in `notebooks/` demonstrate how to inspect raw imagery, perform
low-light analysis, and iterate on processing strategies.

## Documentation

- `docs/architecture.md` captures the intended system design and component
  responsibilities.
- Inline docstrings describe module-level responsibilities and expected inputs.
