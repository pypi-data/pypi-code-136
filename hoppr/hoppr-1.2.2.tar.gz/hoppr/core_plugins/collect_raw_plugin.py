"""
Collector plugin for raw files
"""

import shutil

from pathlib import Path
from typing import Any
from urllib.parse import unquote, urljoin, urlparse

from packageurl import PackageURL  # type: ignore

from hoppr import __version__
from hoppr.base_plugins.collector import SerialCollectorPlugin
from hoppr.base_plugins.hoppr import hoppr_rerunner
from hoppr.hoppr_types.cred_object import CredObject
from hoppr.net import download_file
from hoppr.result import Result


class CollectRawPlugin(SerialCollectorPlugin):
    """
    Collector plugin for raw files
    """

    supported_purl_types = ["binary", "generic", "raw"]

    def get_version(self) -> str:
        return __version__

    @hoppr_rerunner
    def collect(self, comp: Any, repo_url: str, creds: CredObject = None):
        """
        Copy a component to the local collection directory structure
        """
        source_url = urlparse(repo_url)

        purl = PackageURL.from_string(comp.purl)
        subdir = None
        if purl.namespace is not None:
            source_url = urlparse(urljoin(source_url.geturl() + "/", purl.namespace))
            subdir = unquote(purl.namespace)

        target_dir = self.directory_for(purl.type, repo_url, subdir=subdir)

        file_name = unquote(purl.name)

        if source_url.scheme == "file":
            source_file = Path(source_url.path, file_name).expanduser()

            if not source_file.is_file():
                return Result.fail(f"Unable to locate file {source_file}")

            self.get_logger().info(
                f"Copying file from {source_file} to directory {target_dir}"
            )
            shutil.copy(source_file, target_dir)
            return Result.success()

        download_url = urljoin(source_url.geturl(), file_name)

        self.get_logger().info(
            f"Downloading from {download_url} to file {target_dir.joinpath(file_name)}"
        )

        response = download_file(download_url, target_dir.joinpath(file_name), creds)

        return Result.from_http_response(response)
