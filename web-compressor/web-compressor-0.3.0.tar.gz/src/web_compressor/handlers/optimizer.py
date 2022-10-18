"""
This module is part of the 'web-compressor' package,
which is released under GPL-3.0-only license.
"""

from pathlib import Path
import re
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import PIL as Pillow
    import pillow_avif  # pylint: disable=unused-import

except ModuleNotFoundError:
    pass

from ..utils import append2file, get_mime, is_loaded
from .handler import Handler


class Optimizer(Handler):
    """
    Handles image optimization
    """

    # Validation rules
    ruleset: Union[re.Pattern, List[str]] = re.compile(
        r"""
            # JPEG & PNG images
            (?:image\/(?:jpeg|png))
        """,
        re.VERBOSE,
    )

    def __init__(self) -> None:
        """
        Constructor

        :return: None
        :raises: ModuleNotFoundError Missing dependencies
        """

        # If dependencies are missing ..
        if not self.is_ready():
            # .. raise exception
            raise ModuleNotFoundError(
                "Aborting optimization due to missing dependencies. "
                + "Please install 'web-compressor[images]' package "
                + "which depends on 'Pillow'."
            )

    def is_ready(self) -> bool:
        """
        Checks if dependencies are up & running

        :return: bool
        """

        return is_loaded(["PIL", "pillow_avif"])

    def optimize_image(
        self,
        file: Path,
        mime_type: Optional[str] = None,
        quality: Union[int, str] = "keep",
        strip_meta: bool = True,
    ) -> Path:
        """
        Optimizes single image

        :param file: pathlib.Path Path to Image
        :param mime_type: str | None Mediatype
        :param quality: int | str Image quality (JPEG only)
        :param strip_meta: bool Whether to strip EXIF metadata (experimental)
        :return: pathlib.Path Image
        """

        # Skip files if they
        # (1) .. do not exist ..
        # (2) .. were optimized before ..
        if not file.exists() or ".min." in file.name:
            return file

        # Define temporary file
        optimized = append2file(file, "min")

        # Load image
        image = Pillow.Image.open(file)
        # If specified ..
        if strip_meta:
            # .. strip metadata by ..
            # (1) .. extracting image data
            data, img_format = list(image.getdata()), image.format
            # (2) .. creating blank canvas
            image = Pillow.Image.new(image.mode, image.size)
            # (3) .. inserting image data (w/o EXIF)
            image.putdata(data)
            # (4) .. reapplying original format
            image.format = img_format

        # If mediatype unknown ..
        if mime_type is None:
            # .. detect it
            mime_type = get_mime(file.name)

        # If mediatype is
        # (1) .. PNG ..
        if mime_type == "image/png":
            # .. make it as small as possible
            image.save(optimized, format="PNG", optimize=True)

        # (2) .. JPEG ..
        if mime_type == "image/jpeg":
            # If not RGB mode ..
            if image.mode != "RGB":
                # .. convert it
                image = image.convert("RGB")
                # .. apply JPEG format
                image.format = "JPEG"

            # .. optimize it
            # (a) .. making it progressive
            # (b) .. at maximum quality
            # (c) .. stripping metadata
            # (d) .. setting chroma subsampling mode to '420'
            image.save(
                optimized,
                format="JPEG",
                quality=quality,
                progressive=True,
                optimize=True,
                subsampling=2,
            )

        # Close file pointer
        image.close()

        # Remove original file
        file.unlink()

        return optimized

    def convert_image(
        self, file: Path, avif: Dict[str, Any] = None, webp: Dict[str, Any] = None
    ) -> Tuple[Path]:
        """
        Converts single image to AVIF & WebP

        Valid arguments are:
            - avif
            - webp

        :param file: pathlib.Path Path to Image
        :param kwargs: dict Config options
        :return: tuple
        """

        # Load image data
        with Pillow.Image.open(file) as image:
            # Create optimized AVIF image
            # See https://pypi.org/project/pillow-avif-plugin
            avif_file = file.with_suffix(".avif")

            # Apply image quality & save file
            image.save(avif_file, format="AVIF", avif=avif or {"quality": 90})

            # Create optimized WebP image
            webp_file = file.with_suffix(".webp")

            # Apply compression level & save file
            image.save(webp_file, format="WebP", webp=webp or {"method": 6})

        return avif_file, webp_file
