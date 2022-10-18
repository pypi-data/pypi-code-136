import mimetypes
import random
from typing import Mapping

from urllib3.util import parse_url, Url

RETRYABLE_STATUS_CODES = [408, 429, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 598, 599]

GCS_SCHEME = "gs"


def filter_none(js: dict) -> dict:
    if isinstance(js, Mapping):
        return {k: filter_none(v) for k, v in js.items() if v is not None}
    else:
        return js


def get_content_type(filename: str) -> str:
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types
    if filename.split(".")[-1] == "csv":
        content_type = "text/csv"
    else:
        content_type = mimetypes.guess_type(filename)[0]
        content_type = content_type if content_type is not None else 'application/octet-stream'

    return content_type


def get_resource_id(signed_url: str) -> str:
    url = parse_url(signed_url)
    resource_id = Url(scheme=GCS_SCHEME, path=url.path)
    return str(resource_id).replace("///", "//")


# https://cloud.google.com/iot/docs/how-tos/exponential-backoff
def get_wait_time(upload_attempt: int, max_retry_wait_time: int) -> float:
    """
    Calculates the wait time before attempting another file upload or download

    :param upload_attempt: How many attempts to upload that have been made
    :return: int: The time to wait before retrying upload
    """
    initial_wait_time_seconds: int = pow(2, upload_attempt - 1)
    wait_time_seconds: float = initial_wait_time_seconds + random.random()
    wait_time_seconds: float = wait_time_seconds if wait_time_seconds < max_retry_wait_time else max_retry_wait_time
    return wait_time_seconds
