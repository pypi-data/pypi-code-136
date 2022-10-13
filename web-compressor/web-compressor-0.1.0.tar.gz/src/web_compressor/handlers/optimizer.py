from pathlib import Path
import re
from typing import List, Union

try:
    import PIL as Pillow
    import pillow_avif  # pylint: disable=unused-import

except ModuleNotFoundError:
    pass

from ..utils import append2file, is_loaded
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
        Checks if everything checks out

        :return: bool Setup status
        """

        return is_loaded("PIL")

    def optimize_image(
        self, file: Path, mime_type: str, quality: Union[int, str] = "keep"
    ) -> Path:
        """
        Optimizes single image

        :param file: Path Path to Image
        :param mime_type: str Mediatype
        :param quality: Union[int, str] Image quality (JPEG only)
        :return: Path Image
        """

        # If file was optimized before ..
        if ".min." in file.name:
            # .. no action needed
            return file

        # Define temporary file
        optimized = append2file(file, "min")

        # Load image data
        image = Pillow.Image.open(file)

        # If mediatype is
        # (1) .. PNG ..
        if mime_type == "image/png":
            # .. make it as small as possible
            image.save(optimized, format="PNG", optimize=True)

        # (2) .. JPEG ..
        if mime_type == "image/jpeg":
            # .. determine quality setting ('CMYK' cannot 'keep' former quality)
            if quality == "keep" and image.mode == "CMYK":
                quality = 100

            # .. optimize it
            # (a) .. making it progressive
            # (b) .. at maximum quality
            # (c) .. stripping metadata
            # (d) .. setting chroma subsampling mode to '420'
            image.convert("RGB").save(
                optimized,
                format="JPEG",
                quality=quality,
                progressive=True,
                optimize=True,
                subsampling=2,
            )

        # Close file pointer
        image.close()

        # Rename file
        return file.rename(optimized)

    def convert_image(self, file: Path, mime_type: str, **kwargs) -> None:
        """
        Converts single image to AVIF & WebP

        Valid arguments are:
            - method
            - quality

        :param file: Path Path to Image
        :param mime_type: str Mediatype
        :param kwargs: Dict[str, Any] Config options
        :return: None
        """

        if mime_type in ["image/avif", "image/webp"]:
            return

        # Load image data
        image = Pillow.Image.open(file)

        # Create optimized WebP image
        webp_file = file.with_suffix(".webp")

        # Apply compression level & save file
        image.save(webp_file, format="WebP", method=kwargs.get("method", 6))

        # Create optimized AVIF image
        # See https://pypi.org/project/pillow-avif-plugin
        avif_file = file.with_suffix(".avif")

        # Apply image quality & save file
        image.save(avif_file, format="AVIF", quality=kwargs.get("quality", 90))

        # Close file pointer
        image.close()
