"""Request with built-in retry"""
from typing import Collection
from requests import Response, Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def get_with_retry(
    url: str,
    retries: int = 3,
    backoff_factor: float = 0.3,
    status_forcelist: Collection[int] = (
        500,
        502,
        504,
    ),  # pylint: disable=unsubscriptable-object
) -> Response:
    """Sends a GET request with retry options"""
    session = Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session.get(url)
