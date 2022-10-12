from __future__ import annotations

import base64
from io import BytesIO as _BytesIO
from typing import Any

import numpy as np
from PIL import Image


def colorize(img: np.ndarray) -> np.ndarray:
    """Convert a grayscale image to RGB."""
    if not img.shape[-1] == 3:
        if img.shape[-1] == 4:
            pass
        if img.shape[-1] == 1:
            img = np.repeat(img, 3, axis=-1)
        else:
            img = np.repeat(np.expand_dims(img, axis=-1), 3, axis=-1)

    return img


# Image utility functions
def pil_to_b64(im: Image, enc_format: str = "png", **kwargs: Any) -> str:
    """Converts a PIL Image into base64 string for HTML displaying.

    Args:
        im: PIL Image object
        enc_format: image format for displaying. If saved the image will have that extension.
        **kwargs: additional arguments for PIL.Image.save().

    Returns:
        image string with base64 encoding
    """
    buff = _BytesIO()
    im.save(buff, format=enc_format, **kwargs)
    encoded = base64.b64encode(buff.getvalue()).decode("utf-8")

    return encoded


def numpy_to_b64(array: np.ndarray, enc_format: str = "png", normalized=False, **kwargs):
    """Converts a numpy image into base 64 string for HTML displaying.

    Args:
        array: numpy array.
        enc_format: image format for displaying. If saved the image will have that extension.
        normalized: if True, the image will be denormalized to [0, 255].
        **kwargs: additional arguments for PIL.Image.save().

    Returns:
        image string with base64 encoding
    """
    if normalized:
        array *= 255

    im_pil = Image.fromarray(np.uint8(array))

    return pil_to_b64(im_pil, enc_format, **kwargs)
