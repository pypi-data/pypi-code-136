from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.database import Database
from ...types import Response


def _get_kwargs(
    cluster_id: str,
    name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/clusters/{cluster_id}/databases/{name}".format(client.base_url, cluster_id=cluster_id, name=name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Database]]:
    if response.status_code == 200:
        response_200 = Database.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, response.json())
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, response.json())
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, response.json())
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Database]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cluster_id: str,
    name: str,
    *,
    client: Client,
) -> Response[Union[Any, Database]]:
    """Delete a database.

    Args:
        cluster_id (str):
        name (str):

    Returns:
        Response[Union[Any, Database]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        name=name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cluster_id: str,
    name: str,
    *,
    client: Client,
) -> Optional[Union[Any, Database]]:
    """Delete a database.

    Args:
        cluster_id (str):
        name (str):

    Returns:
        Response[Union[Any, Database]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_id: str,
    name: str,
    *,
    client: Client,
) -> Response[Union[Any, Database]]:
    """Delete a database.

    Args:
        cluster_id (str):
        name (str):

    Returns:
        Response[Union[Any, Database]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        name=name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: str,
    name: str,
    *,
    client: Client,
) -> Optional[Union[Any, Database]]:
    """Delete a database.

    Args:
        cluster_id (str):
        name (str):

    Returns:
        Response[Union[Any, Database]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            name=name,
            client=client,
        )
    ).parsed
