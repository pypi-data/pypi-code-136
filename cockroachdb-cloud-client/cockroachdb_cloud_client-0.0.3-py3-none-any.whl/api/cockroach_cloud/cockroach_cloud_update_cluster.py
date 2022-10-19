from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.cluster import Cluster
from ...models.update_cluster_specification import UpdateClusterSpecification
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cluster_id: str,
    *,
    client: Client,
    json_body: UpdateClusterSpecification,
    field_mask: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/clusters/{cluster_id}".format(client.base_url, cluster_id=cluster_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["field_mask"] = field_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Cluster]]:
    if response.status_code == 200:
        response_200 = Cluster.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Cluster]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cluster_id: str,
    *,
    client: Client,
    json_body: UpdateClusterSpecification,
    field_mask: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, Cluster]]:
    """Scale or edit a cluster.

    Args:
        cluster_id (str):
        field_mask (Union[Unset, None, str]):
        json_body (UpdateClusterSpecification):  Example: {'dedicated': {'hardware':
            {'machine_type': 'n2-standard-8'}, 'region_nodes': {'us-central1': 5, 'us-west1': 3}}}.

    Returns:
        Response[Union[Any, Cluster]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
        field_mask=field_mask,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cluster_id: str,
    *,
    client: Client,
    json_body: UpdateClusterSpecification,
    field_mask: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, Cluster]]:
    """Scale or edit a cluster.

    Args:
        cluster_id (str):
        field_mask (Union[Unset, None, str]):
        json_body (UpdateClusterSpecification):  Example: {'dedicated': {'hardware':
            {'machine_type': 'n2-standard-8'}, 'region_nodes': {'us-central1': 5, 'us-west1': 3}}}.

    Returns:
        Response[Union[Any, Cluster]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
        field_mask=field_mask,
    ).parsed


async def asyncio_detailed(
    cluster_id: str,
    *,
    client: Client,
    json_body: UpdateClusterSpecification,
    field_mask: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, Cluster]]:
    """Scale or edit a cluster.

    Args:
        cluster_id (str):
        field_mask (Union[Unset, None, str]):
        json_body (UpdateClusterSpecification):  Example: {'dedicated': {'hardware':
            {'machine_type': 'n2-standard-8'}, 'region_nodes': {'us-central1': 5, 'us-west1': 3}}}.

    Returns:
        Response[Union[Any, Cluster]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
        field_mask=field_mask,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: str,
    *,
    client: Client,
    json_body: UpdateClusterSpecification,
    field_mask: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, Cluster]]:
    """Scale or edit a cluster.

    Args:
        cluster_id (str):
        field_mask (Union[Unset, None, str]):
        json_body (UpdateClusterSpecification):  Example: {'dedicated': {'hardware':
            {'machine_type': 'n2-standard-8'}, 'region_nodes': {'us-central1': 5, 'us-west1': 3}}}.

    Returns:
        Response[Union[Any, Cluster]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
            json_body=json_body,
            field_mask=field_mask,
        )
    ).parsed
