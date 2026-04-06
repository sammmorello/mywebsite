#!/usr/bin/env python3
"""
Background Removal Script
Uses rembg library to remove backgrounds from images, creating sticker-like cutouts.
"""

import sys
from pathlib import Path

try:
    from rembg import remove
    from PIL import Image
except ImportError:
    print("Required packages not found. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rembg", "pillow"])
    from rembg import remove
    from PIL import Image


def remove_background(input_path: str, output_path: str = None) -> str:
    """
    Remove the background from an image.

    Args:
        input_path: Path to the input image
        output_path: Path for the output image (optional, defaults to input_name_nobg.png)

    Returns:
        Path to the output image
    """
    input_file = Path(input_path)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Generate output path if not provided
    if output_path is None:
        output_path = input_file.parent / f"{input_file.stem}_nobg.png"

    # Read the input image
    with open(input_path, "rb") as f:
        input_data = f.read()

    # Remove background
    print(f"Processing: {input_path}")
    output_data = remove(input_data)

    # Save the result as PNG (to preserve transparency)
    with open(output_path, "wb") as f:
        f.write(output_data)

    print(f"Saved: {output_path}")
    return str(output_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_background.py <input_image> [output_image]")
        sys.exit(1)

    input_image = sys.argv[1]
    output_image = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        result = remove_background(input_image, output_image)
        print(f"Background removed successfully!")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
