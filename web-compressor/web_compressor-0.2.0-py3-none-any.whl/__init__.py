"""
This module is part of the 'web-compressor' package,
which is released under GPL-3.0-only license.
"""

from pathlib import Path
import re
from typing import Dict, List, Optional, Tuple
import uuid

import bs4

from .handlers.hasher import Hasher
from .handlers.minifier import Minifier
from .handlers.optimizer import Optimizer
from .logger import LOGGER
from .utils import get_mime


class WebCompressor:
    """
    Supercharges HTML files & web assets
    """

    def __init__(self, base_dir: Path, **kwargs) -> None:
        """
        Constructor

        :param base_dir: pathlib.Path Root directory
        :param kwargs: dict Config options
        :return: None
        """

        # Set root directory
        self.base_dir = base_dir

        # Apply configuration
        for key, value in kwargs.items():
            setattr(self, key, value)

        # Gotta collect 'em all
        self.html_files = self.collect_html()

    def validate(self, file: Path) -> bool:
        """
        Checks whether file may be collected

        Skips directories & hidden files

        :param file: pathlib.Path Path to file
        :return: bool
        """

        # Exclude ..
        # (1) .. directories
        # (2) .. hidden files
        return not (file.is_dir() or file.stem.startswith("."))

        # NOTE:
        # Although it might be preferable to exlude all files
        # below hidden directories, any one-fits-all approach
        # will (at some point or to some extent) fail

    def collect_html(self) -> List[Path]:
        """
        Collects HTM(L) files

        :return: list Collected HTM(L) files
        """

        def is_valid(file: Path) -> bool:
            """
            Checks whether file is valid & identifies as HTM(L)

            :param file: pathlib.Path Path to file
            :return: bool
            """

            return self.validate(file) and get_mime(file.name) == "text/html"

        return [file for file in self.base_dir.glob("**/*") if is_valid(file)]

    def collect_assets(self) -> List[Tuple[Path, str]]:
        """
        Collects web assets & their mediatypes

        :return: list Collected web assets & their mediatypes
        """

        # Create data array
        assets: List[Tuple[Path, str]] = []

        for file in self.base_dir.glob("**/*"):
            # Skip inapt files
            if not self.validate(file):
                continue

            # If mediatype indicates something other than HTM(L) file ..
            if (mime_type := get_mime(file.name)) != "text/html":
                # .. store file & MIME type
                assets.append((file, mime_type))

        return assets

    def update_html(self, references: List[Tuple[str, str]]) -> None:
        """
        Replaces asset references inside HTML files

        :param assets: list References of source & target files
        :return: None
        """

        for html_file in self.html_files:
            # Load original HTML contents
            with html_file.open("r", encoding="utf-8") as file:
                html = file.read()

            for reference in references:
                # Unpack reference pair
                old, new = reference

                # Gotta replace 'em all
                html = html.replace(old, new)

            # Write updated contents
            with html_file.open("w", encoding="utf-8") as file:
                file.write(html)

            LOGGER.info(f"Updated references in {html_file.relative_to(self.base_dir)}")

    def minify_assets(self, **kwargs) -> None:
        """
        Minifies web assets & updates their references

        Valid arguments are:
            - mediatypes
            - options

        :param kwargs: dict Keyword arguments
        :return: None
        """

        # Attempt to ..
        try:
            # .. initialize object
            obj = Minifier(kwargs.get("options"))

        # .. otherwise ..
        except ModuleNotFoundError as error:
            # .. report back
            LOGGER.warning(error)

            # .. abort process
            return

        # Create data array
        references: List[Tuple[str, str]] = []

        # Apply ruleset (if applicable)
        if ruleset := kwargs.get("mediatypes"):
            obj.ruleset = ruleset

        # Iterate over web assets
        for asset in self.collect_assets():
            # Unpack asset file & mediatype
            file, mime_type = asset

            # Skip inapt files
            if not obj.validate(mime_type):
                continue

            # Minify asset
            target = obj.minify_file(file, mime_type)

            # If something changed ..
            if reference := self.get_reference(file, target):
                # .. store them
                references.append(reference)

                # .. report back
                LOGGER.info(f"Minified {file.relative_to(self.base_dir)}")

        # If files changed ..
        if references:
            # .. update HTML files
            self.update_html(references)

    def minify_html(self, **kwargs) -> None:
        """
        Minifies HTML files

        Valid arguments are:
            - options

        :param kwargs: dict Keyword arguments
        :return: None
        """

        # Attempt to ..
        try:
            # .. initialize object
            obj = Minifier(kwargs.get("options"))

        # .. otherwise ..
        except ModuleNotFoundError as error:
            # .. report back
            LOGGER.warning(error)

            # .. abort process
            return

        for html_file in self.html_files:
            # Load original HTML contents
            with html_file.open("r", encoding="utf-8") as file:
                html = file.read()

            # Write minified contents
            with html_file.open("w", encoding="utf-8") as file:
                file.write(obj.minify_string(html, "text/html"))

            LOGGER.info(f"Minified {html_file.relative_to(self.base_dir)}")

    def prettify_html(self) -> None:
        """
        Prettifies HTML files

        :return: None
        """

        for html_file in self.html_files:
            # Load original HTML contents
            with html_file.open("r", encoding="utf-8") as file:
                html = file.read()

            # Write minified contents
            with html_file.open("w", encoding="utf-8") as file:
                file.write(str(html.prettify()))

            LOGGER.info(f"Prettified {html_file.relative_to(self.base_dir)}")

    def optimize_images(self, **kwargs) -> None:
        """
        Optimizes images & updates their references

        Valid arguments are:
            - mediatypes
            - quality

        :param kwargs: dict Keyword arguments
        :return: None
        """

        # Attempt to ..
        try:
            # .. initialize object
            obj = Optimizer()

        # .. otherwise ..
        except ModuleNotFoundError as error:
            # .. report back
            LOGGER.warning(error)

            # .. abort process
            return

        # Create data array
        references: List[Tuple[str, str]] = []

        # Apply ruleset (if applicable)
        if ruleset := kwargs.get("mediatypes"):
            obj.ruleset = ruleset

        # Iterate over web assets
        for asset in self.collect_assets():
            # Unpack asset file & mediatype
            file, mime_type = asset

            # Skip inapt files
            if not obj.validate(mime_type):
                continue

            # Optimize asset
            target = obj.optimize_image(file, kwargs.get("quality", 75))

            # If something changed ..
            if reference := self.get_reference(file, target):
                # .. store asset references
                references.append(reference)

                # .. report back
                LOGGER.info(f"Optimized {file.relative_to(self.base_dir)}")

        # If files changed ..
        if references:
            # .. update HTML files
            self.update_html(references)

    def restore_file(self, file: Path) -> Optional[Path]:
        """
        Restores original filename after minifying & hashing

        :param file: pathlib.Path Path to file
        :return: pathlib.Path | None Restored file
        """

        # If filename matched completely ..
        if restored := re.fullmatch(r"(.*)\.min\.\w*\.[a-z]{3,4}", file.name):
            # .. provide its base string
            return Path(file.parents[0], f"{restored.group(1)}{file.suffix}")

        return None

    def convert_images(self, **kwargs) -> Tuple[Path]:
        """
        Converts images to AVIF/WebP & updates their references

        Valid arguments are:
            - method
            - quality

        :param kwargs: dict Keyword arguments
        :return: Tuple[Path]
        """

        # Attempt to ..
        try:
            # .. initialize object
            obj = Optimizer()

        # .. otherwise ..
        except ModuleNotFoundError as error:
            # .. report back
            LOGGER.warning(error)

            # .. abort process
            return

        # Create data array
        references: List[Tuple[str, str]] = []

        # Iterate over web assets
        for asset in self.collect_assets():
            # Unpack asset file & mediatype
            file, mime_type = asset

            # Skip inapt files
            if not obj.validate(mime_type):
                continue

            # Convert image to AVIF/WebP
            obj.convert_image(file, **kwargs)

            # If original filename can be detected ..
            if restored := self.restore_file(file):
                # .. store references
                references.extend(
                    [
                        #  (1) AVIF
                        self.get_reference(
                            restored.with_suffix(".avif"), file.with_suffix(".avif")
                        ),
                        # (2) WebP
                        self.get_reference(
                            restored.with_suffix(".webp"), file.with_suffix(".webp")
                        ),
                    ]
                )

            # .. report back
            LOGGER.info(f"Created WebP & AVIF from {file.relative_to(self.base_dir)}")

        # If files changed ..
        if references:
            # .. update HTML files
            self.update_html(references)

    def hash_assets(self, **kwargs) -> None:
        """
        Hashes web assets & updates their references

        Valid arguments are
            - mediatypes
            - hash_length
            - use_mtime

        :param kwargs: dict Keyword arguments
        :return: None
        """

        # Create data array
        references: List[Tuple[str, str]] = []

        # Initialize object
        obj = Hasher()

        # Apply ruleset (if applicable)
        if ruleset := kwargs.get("mediatypes"):
            obj.ruleset = ruleset

        # Iterate over web assets
        for asset in self.collect_assets():
            # Unpack asset file & mediatype
            file, mime_type = asset

            # Skip inapt files
            if not obj.validate(mime_type):
                continue

            # Hash asset
            target = obj.hash_file(
                file, kwargs.get("hash_length", 10), kwargs.get("use_mtime", False)
            )

            # Store asset references (relative to root)
            references.append(self.get_reference(file, target))

            # Report back
            LOGGER.info(f"Hashed {file.relative_to(self.base_dir)}")

        # If files changed ..
        if references:
            # .. update HTML files
            self.update_html(references)

    def generate_sri(self, digest: str = "sha512") -> None:
        """
        Generates subresource integrity values ('link' & 'script' tags only)

        :param digest: str Cryptographic digest
        :return: None
        """

        # Retrieve web assets
        assets = self.collect_assets()

        # Initialize
        obj = Hasher()

        # Define eligible tags & their source attribute
        dtypes = {"link": "href", "script": "src"}

        for html_file in self.html_files:
            # Load original HTML contents
            with html_file.open("r", encoding="utf-8") as file:
                soup = bs4.BeautifulSoup(file, "html.parser")

            # Iterate over eligible tag types
            for dtype, attr in dtypes.items():
                # Find them in HTML contents
                for tag in soup.find_all(dtype):
                    # Skip tags ..
                    # (1) .. with 'integrity' attribute
                    # (2) .. not sourcing external file
                    if tag.has_attr("integrity") or not tag.has_attr(attr):
                        continue

                    # Skip 'link' tags not containing stylesheets
                    if dtype == "link" and get_mime(tag[attr]) != "text/css":
                        continue

                    # Iterate over web assets
                    for asset in assets:
                        # Unpack asset file & mediatype
                        file = asset[0]

                        # Get path relative to root directory
                        path = str(file.relative_to(self.base_dir))

                        # Skip inapt asset files
                        if path not in tag[attr]:
                            continue

                        # Apply SRI hash
                        tag["integrity"] = obj.get_sri_value(file, digest)

                        # Report back
                        LOGGER.info(f"Added SRI for {file.relative_to(self.base_dir)}")

                        # Quit loop
                        break

            # Write updated contents
            with html_file.open("w", encoding="utf-8") as file:
                file.write(str(soup))

    def _generate_csp(self, hashes: Dict[str, List[str]], sets: Dict[str, str]) -> str:
        """
        Generates CSP using (hashed) nonces

        This applies to ..
            - inline 'script' & 'style' tags
            - external 'link' & 'script' tags

        :param hashes: dict Hashed nonces
        :param sets: dict CSP directives
        :return: str CSP directives as string for use in 'meta' tag
        """

        csp: List[str] = []

        # Available directives (as per CSP specs)
        available = [
            # (1) Fetch directives
            # See https://www.w3.org/TR/CSP3/#directives-fetch
            "child-src",
            "connect-src",
            "default-src",
            "font-src",
            "frame-src",
            "img-src",
            "manifest-src",
            "media-src",
            "object-src",
            "prefetch-src",
            "script-src",
            "script-src-elem",
            "script-src-attr",
            "style-src",
            "style-src-elem",
            "style-src-attr",
            # (2) Other directives
            # See https://www.w3.org/TR/CSP3/#directives-other
            "webrtc",
            "worker-src",
            # (3) Document directives
            # See https://www.w3.org/TR/CSP3/#directives-document
            "base-uri",
            "sandbox",
            # (4) Navigation directives
            # See https://www.w3.org/TR/CSP3/#directives-navigation
            "form-action",
            "frame-ancestors",
            "form-action",
            # (5) Reporting directives
            # See https://www.w3.org/TR/CSP3/#directives-reporting
            "report-uri",
            "report-to",
        ]

        # Directives not supported by 'meta' tag
        # See https://www.w3.org/TR/CSP3/#meta-element
        unsupported = [
            "frame-ancestors",
            "report-uri",
            "sandbox",
        ]

        # Experimental directives
        # See https://mzl.la/3TgdSoJ (MDN on "other" directives)
        experimental = [
            "require-sri-for",
            "require-trusted-types-for",
            "trusted-types",
            "upgrade-insecure-requests",
        ]

        # Create data buffer
        csp = {}

        # Iterate over official & experimental directives
        for directive in available + experimental:
            # Skip directives which are ..
            # (1) .. not used
            # (2) .. supported
            if directive in unsupported or (
                directive not in sets and directive not in hashes
            ):
                continue

            # Create data array
            csp[directive] = []

            # If hashed nonces available ..
            if nonces := hashes.get(directive):
                # .. add them
                csp[directive].append(" ".join(map(lambda x: f"'{x}'", nonces)))

            # If user-defined directives available ..
            if value := sets.get(directive):
                # .. add them
                csp[directive].append(value)

        # Format CSP directives & combine them
        return " ".join([f"{key} {' '.join(value)};" for key, value in csp.items()])

    def _get_nonce(self, nonce: Optional[str]) -> str:
        """
        Validates CSP nonce (or creates one)

        :param nonce: str | None Nonce to be validated
        :return: str Valid CSP nonce
        """

        # Generate nonce (if applicable)
        if nonce is None:
            return f"nonce-{uuid.uuid4().hex}"

        # If keyword prepended ..
        if nonce.startswith("nonce-"):
            # .. return original nonce
            return nonce

        # .. otherwise catch up on it
        return f"nonce-{nonce}"

    def generate_csp(self, **kwargs) -> None:
        """
        Generates CSP using (hashed) nonces

        Valid arguments are
            - digest
            - nonce
            - sets

        For more information, see '_generate_csp()'

        :param kwargs: dict Keyword arguments
        :return: None
        """

        # Initialize
        obj = Hasher()

        for html_file in self.html_files:
            # Load original HTML contents
            with html_file.open("r", encoding="utf-8") as file:
                soup = bs4.BeautifulSoup(file, "html.parser")

            # Normalize nonce (if any)
            nonce = self._get_nonce(kwargs.get("nonce"))

            # Create data array
            hashes: Dict[str, List[str]] = {
                "script-src": [],
                "style-src": [],
            }

            # Define eligible tags & their source attribute (if applicable)
            dtypes = {"link": "href", "script": "src", "style": None}

            # Iterate over eligible tag types
            for dtype, attr in dtypes.items():
                # Find them in HTML contents
                for tag in soup.find_all(dtype):
                    # Skip tags already containing (hashed) nonce
                    if tag.has_attr("nonce"):
                        continue

                    # If tag references external file (scripts & links only) ..
                    if tag.has_attr(attr):
                        # .. skip 'link' tags not containing stylesheets
                        if dtype == "link" and get_mime(tag[attr]) != "text/css":
                            continue

                        # .. apply random nonce (without 'nonce-')
                        tag["nonce"] = nonce[6:]

                        # .. store it
                        if dtype == "script":
                            hashes["script-src"].append(nonce)

                        else:
                            hashes["style-src"].append(nonce)

                        # .. move on
                        continue

                    # Generate hashed nonce from tag contents
                    tag["nonce"] = obj.get_hashed_nonce(
                        tag.text, kwargs.get("digest", "sha512")
                    )

                    # Store it
                    if tag.name == "script":
                        hashes["script-src"].append(tag["nonce"])

                    else:
                        hashes["style-src"].append(tag["nonce"])

            # Create 'meta' tag
            meta_tag = soup.new_tag("meta")

            # Generate CSP directives & add them
            meta_tag["http-equiv"] = "content-security-policy"
            meta_tag["content"] = self._generate_csp(
                hashes,
                kwargs.get(
                    "sets",
                    {
                        "script-src": "'strict-dynamic'",
                        "object-src": "none",
                        "base-uri": "none",
                    },
                ),
            )

            # Add 'meta' tag containing CSP directives
            # (1) Determine earliest tag possible (either 'head' or 'body')
            insert_tag = soup.head if soup.select("head") else soup.html

            # Insert 'meta' tag before
            insert_tag.findChildren()[0].insert_before(meta_tag)

            # NOTE:
            # When minifying HTML contents, the 'head' tag is optional
            # as per the specs, thus we cannot rely on it being always
            # present, although this might break some websites.
            #
            # See https://github.com/tdewolff/minify/issues/90

            # Write updated contents
            with html_file.open("w", encoding="utf-8") as file:
                file.write(str(soup))

            LOGGER.info(f"Added CSP to {html_file.relative_to(self.base_dir)}")

    def get_reference(self, source: Path, target: Path) -> Optional[Tuple[str, str]]:
        """
        Turns two path objects into references relative to root directory

        :param source: pathlib.Path Source file
        :param target: pathlib.Path Target file
        :return: tuple | None Asset reference
        """

        # Get their relative paths
        old = str(source.relative_to(self.base_dir))
        new = str(target.relative_to(self.base_dir))

        # Provide changed files only
        if old != new:
            return old, new

        return None


__all__ = [
    # Main class
    "WebCompressor",
    # Subclasses
    "Hasher",
    "Minifier",
    "Optimizer",
]
