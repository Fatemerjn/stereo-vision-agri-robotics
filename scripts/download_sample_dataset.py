#!/usr/bin/env python3
"""Download a tiny sample dataset for smoke-testing the pipeline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.request import urlretrieve

SAMPLE_URL = "https://raw.githubusercontent.com/opencv/opencv/4.x/samples/data/aloeL.jpg"
RIGHT_URL = "https://raw.githubusercontent.com/opencv/opencv/4.x/samples/data/aloeR.jpg"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Directory where the image pairs are stored")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir: Path = args.output
    output_dir.mkdir(parents=True, exist_ok=True)

    left_path = output_dir / "aloe_L.jpg"
    right_path = output_dir / "aloe_R.jpg"

    print(f"Downloading sample images to {output_dir}")
    urlretrieve(SAMPLE_URL, left_path)
    urlretrieve(RIGHT_URL, right_path)

    manifest = {
        "left": left_path.name,
        "right": right_path.name,
        "description": "Sample aloe stereo pair from OpenCV",
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print("Done.")


if __name__ == "__main__":
    main()
