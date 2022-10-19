import datetime
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.cockroach_cloud_list_cluster_nodes_pagination_sort_order import (
    CockroachCloudListClusterNodesPaginationSortOrder,
)
from ...models.list_cluster_nodes_response import ListClusterNodesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cluster_id: str,
    *,
    client: Client,
    region_name: Union[Unset, None, str] = UNSET,
    pagination_page: Union[Unset, None, str] = UNSET,
    pagination_limit: Union[Unset, None, int] = UNSET,
    pagination_as_of_time: Union[Unset, None, datetime.datetime] = UNSET,
    pagination_sort_order: Union[Unset, None, CockroachCloudListClusterNodesPaginationSortOrder] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/clusters/{cluster_id}/nodes".format(client.base_url, cluster_id=cluster_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["region_name"] = region_name

    params["pagination.page"] = pagination_page

    params["pagination.limit"] = pagination_limit

    json_pagination_as_of_time: Union[Unset, None, str] = UNSET
    if not isinstance(pagination_as_of_time, Unset):
        json_pagination_as_of_time = pagination_as_of_time.isoformat() if pagination_as_of_time else None

    params["pagination.as_of_time"] = json_pagination_as_of_time

    json_pagination_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(pagination_sort_order, Unset):
        json_pagination_sort_order = pagination_sort_order.value if pagination_sort_order else None

    params["pagination.sort_order"] = json_pagination_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ListClusterNodesResponse]]:
    if response.status_code == 200:
        response_200 = ListClusterNodesResponse.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ListClusterNodesResponse]]:
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
    region_name: Union[Unset, None, str] = UNSET,
    pagination_page: Union[Unset, None, str] = UNSET,
    pagination_limit: Union[Unset, None, int] = UNSET,
    pagination_as_of_time: Union[Unset, None, datetime.datetime] = UNSET,
    pagination_sort_order: Union[Unset, None, CockroachCloudListClusterNodesPaginationSortOrder] = UNSET,
) -> Response[Union[Any, ListClusterNodesResponse]]:
    """List nodes for a cluster.

     Sort order: Region name, node name

    Args:
        cluster_id (str):
        region_name (Union[Unset, None, str]):
        pagination_page (Union[Unset, None, str]):
        pagination_limit (Union[Unset, None, int]):
        pagination_as_of_time (Union[Unset, None, datetime.datetime]):
        pagination_sort_order (Union[Unset, None,
            CockroachCloudListClusterNodesPaginationSortOrder]):

    Returns:
        Response[Union[Any, ListClusterNodesResponse]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        region_name=region_name,
        pagination_page=pagination_page,
        pagination_limit=pagination_limit,
        pagination_as_of_time=pagination_as_of_time,
        pagination_sort_order=pagination_sort_order,
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
    region_name: Union[Unset, None, str] = UNSET,
    pagination_page: Union[Unset, None, str] = UNSET,
    pagination_limit: Union[Unset, None, int] = UNSET,
    pagination_as_of_time: Union[Unset, None, datetime.datetime] = UNSET,
    pagination_sort_order: Union[Unset, None, CockroachCloudListClusterNodesPaginationSortOrder] = UNSET,
) -> Optional[Union[Any, ListClusterNodesResponse]]:
    """List nodes for a cluster.

     Sort order: Region name, node name

    Args:
        cluster_id (str):
        region_name (Union[Unset, None, str]):
        pagination_page (Union[Unset, None, str]):
        pagination_limit (Union[Unset, None, int]):
        pagination_as_of_time (Union[Unset, None, datetime.datetime]):
        pagination_sort_order (Union[Unset, None,
            CockroachCloudListClusterNodesPaginationSortOrder]):

    Returns:
        Response[Union[Any, ListClusterNodesResponse]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
        region_name=region_name,
        pagination_page=pagination_page,
        pagination_limit=pagination_limit,
        pagination_as_of_time=pagination_as_of_time,
        pagination_sort_order=pagination_sort_order,
    ).parsed


async def asyncio_detailed(
    cluster_id: str,
    *,
    client: Client,
    region_name: Union[Unset, None, str] = UNSET,
    pagination_page: Union[Unset, None, str] = UNSET,
    pagination_limit: Union[Unset, None, int] = UNSET,
    pagination_as_of_time: Union[Unset, None, datetime.datetime] = UNSET,
    pagination_sort_order: Union[Unset, None, CockroachCloudListClusterNodesPaginationSortOrder] = UNSET,
) -> Response[Union[Any, ListClusterNodesResponse]]:
    """List nodes for a cluster.

     Sort order: Region name, node name

    Args:
        cluster_id (str):
        region_name (Union[Unset, None, str]):
        pagination_page (Union[Unset, None, str]):
        pagination_limit (Union[Unset, None, int]):
        pagination_as_of_time (Union[Unset, None, datetime.datetime]):
        pagination_sort_order (Union[Unset, None,
            CockroachCloudListClusterNodesPaginationSortOrder]):

    Returns:
        Response[Union[Any, ListClusterNodesResponse]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        region_name=region_name,
        pagination_page=pagination_page,
        pagination_limit=pagination_limit,
        pagination_as_of_time=pagination_as_of_time,
        pagination_sort_order=pagination_sort_order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: str,
    *,
    client: Client,
    region_name: Union[Unset, None, str] = UNSET,
    pagination_page: Union[Unset, None, str] = UNSET,
    pagination_limit: Union[Unset, None, int] = UNSET,
    pagination_as_of_time: Union[Unset, None, datetime.datetime] = UNSET,
    pagination_sort_order: Union[Unset, None, CockroachCloudListClusterNodesPaginationSortOrder] = UNSET,
) -> Optional[Union[Any, ListClusterNodesResponse]]:
    """List nodes for a cluster.

     Sort order: Region name, node name

    Args:
        cluster_id (str):
        region_name (Union[Unset, None, str]):
        pagination_page (Union[Unset, None, str]):
        pagination_limit (Union[Unset, None, int]):
        pagination_as_of_time (Union[Unset, None, datetime.datetime]):
        pagination_sort_order (Union[Unset, None,
            CockroachCloudListClusterNodesPaginationSortOrder]):

    Returns:
        Response[Union[Any, ListClusterNodesResponse]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
            region_name=region_name,
            pagination_page=pagination_page,
            pagination_limit=pagination_limit,
            pagination_as_of_time=pagination_as_of_time,
            pagination_sort_order=pagination_sort_order,
        )
    ).parsed
