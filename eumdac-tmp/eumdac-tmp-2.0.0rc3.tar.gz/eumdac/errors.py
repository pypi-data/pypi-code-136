"""
This module defines errors and error handling functions for eumdac.
"""
import json
from typing import *
from urllib.parse import urlparse

import requests


def eumdac_raise_for_status(
    msg: str, response: requests.Response, exc_cls: Type[Exception]
) -> None:
    """take a message and a requests response to transform it into a eumdac error."""
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        url = urlparse(response.url)
        try:
            extra_info = json.loads(response.text)
        except json.decoder.JSONDecodeError:
            extra_info = {"text": response.text}
        extra_info.update({"url": url, "status": response.status_code})
        exception = exc_cls(msg, extra_info)
        raise exception from exc


class EumdacError(Exception):
    """All eumdac errors will inherit from a EumdacError"""

    def __init__(self, msg: str, extra_info: Optional[Dict[str, Any]] = None):
        self.extra_info = extra_info
        super().__init__(msg)
