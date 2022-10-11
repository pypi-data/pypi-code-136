import typing
import httpx
from loguru import logger
from httpx._types import QueryParamTypes


def http_get(
    base_url: str,
    segment: str = "",
    params: QueryParamTypes = None,
    access_token: str = None,
):
    """
    Fetch get request
    :param base_url: principal domain
    :param segment: request segment
    :param access_token: JWT access token
    :return: JSON response
    """
    headers = {
        "authorization": f"Bearer {access_token}",
    }
    with httpx.Client(
        base_url=base_url, headers=headers, verify=False, timeout=30
    ) as client:
        try:
            r = client.get(url=segment, params=params)
            r.raise_for_status()
        except httpx.HTTPStatusError as exc:
            logger.error(
                f"Error response {exc.response.status_code} while requesting {exc.request.url!r}"
            )
            return None
        except httpx.HTTPError as exc:
            logger.error(f"Error while requesting {exc.request.url!r}")
            return None
    return r.json()


def http_post(
    base_url: str, segment: str = "", data: typing.Optional[dict[str, str]] = None
):
    """
    Fetch post request
    :param base_url: principal domain
    :param segment: request segment
    :param data: request payload
    :return: JSON response
    """
    headers = {"content-type": "application/x-www-form-urlencoded"}
    with httpx.Client(
        base_url=base_url, headers=headers, verify=False, timeout=30
    ) as client:
        try:
            r = client.post(url=segment, data=data)
            r.raise_for_status()
        except httpx.HTTPStatusError as exc:
            logger.error(
                f"Error response {exc.response.status_code} while requesting {exc.request.url}"
            )
            return None
        except httpx.HTTPError as exc:
            logger.error(f"Error while requesting {exc.request.url}")
            return None
    return r.json()
