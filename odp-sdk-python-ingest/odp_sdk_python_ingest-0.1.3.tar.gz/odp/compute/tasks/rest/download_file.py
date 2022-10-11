from datetime import datetime
from hashlib import md5
import json
import logging
from typing import Any, Callable, Optional, Tuple, Union
from urllib.parse import urlparse

from odp.types import FileInfo

import requests
from prefect.core.task import Task
from prefect.utilities.tasks import defaults_from_attrs

__all__ = ["RestDownloadFile"]

LOG = logging.getLogger(__name__)


class RestDownloadFile(Task):
    """Convenience Task for downloading a file"""

    def __init__(
        self,
        url: Optional[str] = None,
        download_timeout: Optional[float] = None,
        parse_cb: Optional[Callable[[str, bytes], Any]] = None,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        if url is not None and len(url) == 0:
            raise ValueError("URL cannot be emtpy")

        self.url = url
        self.download_timeout = download_timeout
        self.parse_cb = parse_cb

    @defaults_from_attrs("url", "download_timeout", "parse_cb")
    def run(
        self,
        url: Optional[str],
        download_timeout: Optional[float],
        parse_cb: Optional[Callable[[str, bytes], Any]],
    ) -> Union[FileInfo, Any]:

        if not url:
            raise ValueError("URL cannot be null or empty")

        fname, size = self._check_url_header(url, download_timeout)
        LOG.info("Downloading '%s', (%d bytes)", fname, size)

        res = requests.get(url, timeout=download_timeout)
        res.raise_for_status()

        if parse_cb:
            return parse_cb(fname, res.content)

        return FileInfo(
            name=fname,
            last_updated=datetime.now(),
            checksum="md5;" + md5(res.content).hexdigest(),
            mime_type=res.headers.get("Content-Type", "application/octet-stream"),
            ref="inline",
            contents=res.content,
        )

    @staticmethod
    def _check_url_header(url: str, timeout: Optional[float]) -> Tuple[str, int]:

        res = requests.head(url, timeout=timeout)
        res.raise_for_status()

        content, fname = RestDownloadFile._parse_content_header(res)
        if content.lower() != "attachment":
            raise RuntimeError("URL is not a file-download")
        if not fname:
            LOG.warning("Filename was not found in header. Using URL instead")

            p = urlparse(url)

            if p.path:
                fname = p.path.split("/")[-1]
            else:
                LOG.warning(
                    "Unable to infer filename from URL-path, generating name instead"
                )
                fname = md5(json.dumps(res.headers).encode("utf-8")).hexdigest()

        content_length = int(res.headers["Content-Length"])

        return fname, content_length

    @staticmethod
    def _parse_content_header(res: requests.Response) -> Tuple[str, Optional[str]]:
        content = res.headers["Content-Disposition"]
        content = [x.strip() for x in content.split(";")]

        if len(content) == 1:
            return content[0], None
        else:
            fname = content[1].split("=")[1]
            return content[0], fname
