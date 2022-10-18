"""
This module is part of the 'pelican-compressor' package,
which is released under GPL-3.0-only license.
"""

import logging
from pathlib import Path
from typing import List, Tuple, Union
import uuid

from web_compressor import WebCompressor

from pelican import Pelican, signals

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def worker(pelican: Pelican) -> None:
    """
    Wrapper for 'WebCompressor'

    :param pelican: pelican.Pelican Pelican object
    :return: None
    """

    # Report initialization
    LOGGER.info("PLUGIN pelican-compressor was loaded")

    # Define alias for 'pelican' settings
    config = pelican.settings

    # Party time!
    obj = WebCompressor(Path(config["OUTPUT_PATH"]))

    # Apply 'pre' hook
    pre_hook = config.get("WEBCOMPRESSOR_PRE_HOOK")

    if callable(pre_hook):
        obj.apply_hook(pre_hook)

    # Minify web assets
    if config.get("WEBCOMPRESSOR_ENABLE_MINIFY", True):
        obj.minify_assets(
            # For supported mediatypes,
            # see https://github.com/tdewolff/minify/tree/master/bindings/py#mediatypes
            mediatypes=config.get("WEBCOMPRESSOR_MINIFY_MEDIATYPES"),
            options=config.get("WEBCOMPRESSOR_MINIFY_OPTIONS"),
        )

    # Optimize images
    if config.get("WEBCOMPRESSOR_ENABLE_IMAGEOPTIM", False):
        obj.optimize_images(
            mediatypes=config.get("WEBCOMPRESSOR_IMAGEOPTIM_MEDIATYPES"),
            quality=config.get("WEBCOMPRESSOR_JPEG_QUALITY", 75),
            strip_meta=config.get("WEBCOMPRESSOR_STRIP_METADATA", True),
        )

    # Gotta hash 'em all
    if config.get("WEBCOMPRESSOR_ENABLE_HASHING", True):
        obj.hash_assets(
            mediatypes=config.get("WEBCOMPRESSOR_HASHING_MEDIATYPES"),
            hash_length=config.get("WEBCOMPRESSOR_HASH_LENGTH", 10),
            use_mtime=config.get("WEBCOMPRESSOR_HASH_MODIFIED", False),
        )

    # Convert images
    if config.get("WEBCOMPRESSOR_ENABLE_MODERN_FORMATS", False):
        obj.convert_images(
            avif=config.get("WEBCOMPRESSOR_AVIF_SETTINGS", {"quality": 90}),
            webp=config.get("WEBCOMPRESSOR_WEBP_SETTINGS", {"method": 6}),
        )

    # Minify HTML files (see comment below)
    if config.get("WEBCOMPRESSOR_ENABLE_MINIFY", True):
        obj.minify_html(options=config.get("WEBCOMPRESSOR_MINIFY_OPTIONS"))

    # Add subresource integrity values (SRI)
    if config.get("WEBCOMPRESSOR_ENABLE_SRI", True):
        obj.generate_sri(config.get("WEBCOMPRESSOR_SRI_DIGEST", "sha512"))

    # Generate content security policy (CSP)
    if config.get("WEBCOMPRESSOR_ENABLE_CSP", False):
        obj.generate_csp(
            digest=config.get("WEBCOMPRESSOR_CSP_DIGEST", "sha512"),
            nonce=config.get("WEBCOMPRESSOR_CSP_NONCE", f"nonce-{uuid.uuid4().hex}"),
            sets=config.get(
                "WEBCOMPRESSOR_CSP_DIRECTIVES",
                {
                    "script-src": "'strict-dynamic'",
                    "object-src": "none",
                    "base-uri": "none",
                },
            ),
        )

    # Minify HTML files .. again (see comment below)
    if config.get("WEBCOMPRESSOR_ENABLE_MINIFY", True):
        obj.minify_html(options=config.get("WEBCOMPRESSOR_MINIFY_OPTIONS"))

    # NOTE:
    # Minifying HTML files also compresses inline styles/scripts,
    # which interferes with generating hashes for them, and since
    # this leads to invalid hashes, we have twice - any solutions
    # or PRs are welcome!

    # Prettify HTML files
    if config.get("WEBCOMPRESSOR_PRETTIFY_HTML", False):
        obj.prettify_html()

    # Apply 'post' hook
    post_hook = config.get("WEBCOMPRESSOR_POST_HOOK")

    if callable(post_hook):
        obj.apply_hook(post_hook)


def register() -> None:
    """
    Registers 'WebCompressor' plugin

    For more information,
    see https://docs.getpelican.com/en/latest/plugins.html

    :return: None
    """

    signals.finalized.connect(worker)
