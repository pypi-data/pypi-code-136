"""
This module is part of the 'web-compressor' package,
which is released under GPL-3.0-only license.
"""

from pathlib import Path
import re
from typing import Dict, List, Optional, Union

try:
    import minify

except ModuleNotFoundError:
    pass

from ..utils import append2file, get_mime, is_loaded
from .handler import Handler


class Minifier(Handler):
    """
    Handles file minification
    """

    # Validation rules
    ruleset: Union[re.Pattern, List[str]] = re.compile(
        r"""
            # CSS
            (?:text\/css)|
            # HTML
            (?:text\/html)|
            # JS
            # NOTE: "application/x-ecmascript" & "application/x-javascript"
            # are deprecated (but supported). Also "text/javascript" is valid
            # while "text/ecmascript" is not
            (?:(?:application|text)/(x-)?(?:java|ecma)script)|
            # JSON
            # NOTE: "text/json" is deprecated (but supported)
            (?:(?:application|text)\/(?:ld\+)?json)|
            # SVG
            (?:image\/svg\+xml)|
            # XML
            (?:.*\/(?:.*\+)?xml)
        """,
        re.VERBOSE,
    )

    def __init__(self, options: Optional[Dict[str, Union[bool, int]]] = None) -> None:
        """
        Constructor

        :param options: Optional[Dict[str, Union[bool, int]]] Minification settings
        :return: None
        :raises: ModuleNotFoundError Missing dependencies
        """

        # If dependencies are missing ..
        if not self.is_ready():
            # .. raise exception
            raise ModuleNotFoundError(
                "Aborting minification due to missing dependencies. "
                + "Please install 'web-compressor[minify]' package "
                + "which depends on 'minify-html' (requires 'Go')."
            )

        # Configure 'minify' module
        minify.config(
            options
            or {
                "css-precision": 0,
                "html-keep-comments": False,
                "html-keep-conditional-comments": False,
                "html-keep-default-attr-vals": False,
                "html-keep-document-tags": False,
                "html-keep-end-tags": False,
                "html-keep-whitespace": False,
                "html-keep-quotes": False,
                "js-precision": 0,
                "js-keep-var-names": False,
                "js-no-nullish-operator": False,
                "json-precision": 0,
                "json-keep-numbers": False,
                "svg-keep-comments": False,
                "svg-precision": 0,
                "xml-keep-whitespace": False,
            }
            # For more information,
            # see https://github.com/tdewolff/minify/tree/master/bindings/py
        )

    def is_ready(self) -> bool:
        """
        Checks if dependencies are up & running

        :return: bool
        """

        return is_loaded("minify")

    def minify_file(self, file: Path, mime_type: Optional[str] = None) -> Path:
        """
        Minifies single file

        :param file: pathlib.Path Path to file
        :param mime_type: str | None Mediatype
        :return: pathlib.Path File
        """

        # Skip files if they ..
        # (1) .. do not exist ..
        # (2) .. were minified before ..
        if ".min." in file.name:
            return file

        # Define temporary file
        minified = append2file(file, "min")

        # If mediatype unknown ..
        if mime_type is None:
            # .. detect it
            mime_type = get_mime(file.name)

        # Minify file contents & store in new file
        minify.file(mime_type, str(file), str(minified))

        # Replace source file with new file
        minified.replace(file)

        # Rename file
        return file.rename(minified)

    def minify_string(self, string: str, mime_type: str) -> str:
        """
        Minifies string

        :param string: str String to be minified
        :param mime_type: str Mediatype
        :return: str Minified string
        """

        # Minify string
        return minify.string(mime_type, string)
