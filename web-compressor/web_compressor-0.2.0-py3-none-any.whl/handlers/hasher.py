"""
This module is part of the 'web-compressor' package,
which is released under GPL-3.0-only license.
"""

import base64
import hashlib
from pathlib import Path
import re
from typing import List, Union

from ..utils import append2file, read_file
from .handler import Handler


class Hasher(Handler):
    """
    Handles file hashing
    """

    # Validation rules
    ruleset: Union[re.Pattern, List[str]] = re.compile(
        r"""
            # CSS
            (?:text\/css)|
            # Fonts
            (?:font\/.*)|
            # JS
            (?:(?:application|text)/(x-)?(?:java|ecma)script)|
            # JSON
            (?:(?:application|text)\/(?:ld+)?json)|
            # Images
            (?:image\/.*)|
            # XML
            (?:.*\/(?:.*\+)?xml)
        """,
        re.VERBOSE,
    )

    def is_ready(self) -> bool:
        """
        Checks if dependencies are up & running

        :return: bool
        """

        return True

    def hash_file(
        self, file: Path, hash_length: int = 10, use_mtime: bool = False
    ) -> Path:
        """
        Hashes file

        :param file: pathlib.Path Path to file
        :param hash_length: int Length of added file hash
        :param use_mtime: bool Whether to hash 'modified' time or file contents
        :return: pathlib.Path Hashed file
        """

        # Define file hash
        file_hash: Union[str, None] = None

        # Determine whether to build file hash over ..
        if use_mtime:
            # (1) .. modified time
            file_hash = hashlib.blake2b(str(file.stat().st_mtime).encode()).hexdigest()

        # .. or ..
        else:
            # (2) .. file contents
            file_hash = self.get_file_hash(file)

        # NOTE:
        # While 'last modified' quickly indicates changes, this could be
        # misleading, since assets might be generated each time the page
        # changes which makes hashes over its contents the only reliable
        # way to prevent caching the same file twice

        # If hash generation failed ..
        if file_hash is None:
            # .. keep original
            return file

        # If hash length is ..
        # (1) .. greater than zero (= positive)
        # (2) .. lesser than length of actual hash
        if 0 < hash_length < len(file_hash):
            # .. shorten hash
            file_hash = file_hash[:hash_length]

        # If already hashed ..
        if file_hash in file.name:
            # .. keep original
            return file

        # Rename file
        return file.rename(append2file(file, file_hash))

    def get_file_hash(self, file: Path) -> str:
        """
        Computes file hash (using 'blake2b' digest)

        :param file: pathlib.Path Path to file
        :return: str File hash
        """

        # Create file hash
        return hashlib.blake2b(read_file(file)).hexdigest()

    def get_sri_value(self, file: Path, digest: str = "sha512") -> str:
        """
        Computes subresource integrity value (= SRI hash)

        :param file: pathlib.Path Path to file
        :param digest: str Cryptographic digest
        :return: str SRI hash
        """

        # If digest is invalid ..
        if digest.lower() not in ["sha256", "sha384", "sha512"]:
            # .. fall back to 'SHA512'
            digest = "sha512"

        # Create cryptographic digest
        sri_hash: bytes = hashlib.new(digest, read_file(file)).digest()

        # Convert digest into subresource integrity value
        # (1) Decode into string
        # (2) Base64-encode it
        # (3) Prepend digest function name
        return f"{digest}-{base64.b64encode(sri_hash).decode()}"

    def get_hashed_nonce(self, contents: str, digest: str = "sha512") -> str:
        """
        Computes hashed nonce value

        :param contents: str String to be hashed
        :param digest: str Cryptographic digest
        :return: str Hashed nonce
        """

        # If digest is invalid ..
        if digest.lower() not in ["sha256", "sha384", "sha512"]:
            # .. fall back to 'SHA512'
            digest = "sha512"

        # Create cryptographic digest
        nonce: bytes = hashlib.new(digest, contents.encode()).digest()

        # Convert digest into subresource integrity value
        # (1) Decode into string
        # (2) Base64-encode it
        # (3) Prepend digest function name
        return f"{digest}-{base64.b64encode(nonce).decode()}"
