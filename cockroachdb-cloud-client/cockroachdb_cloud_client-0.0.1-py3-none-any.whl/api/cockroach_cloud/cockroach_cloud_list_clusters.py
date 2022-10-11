import datetime
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.cockroach_cloud_list_clusters_pagination_sort_order import CockroachCloudListClustersPaginationSortOrder
from ...models.list_clusters_response import ListClustersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    show_inactive: Union[Unset, None, bool] = True,
    pagination_page: Union[Unset, None, str] = UNSET,
    pagination_limit: Union[Unset, None, int] = UNSET,
    pagination_as_of_time: Union[Unset, None, datetime.datetime] = UNSET,
    pagination_sort_order: Union[Unset, None, CockroachCloudListClustersPaginationSortOrder] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/clusters".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["show_inactive"] = show_inactive

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ListClustersResponse]]:
    if response.status_code == 200:
        response_200 = ListClustersResponse.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ListClustersResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    show_inactive: Union[Unset, None, bool] = True,
    pagination_page: Union[Unset, None, str] = UNSET,
    pagination_limit: Union[Unset, None, int] = UNSET,
    pagination_as_of_time: Union[Unset, None, datetime.datetime] = UNSET,
    pagination_sort_order: Union[Unset, None, CockroachCloudListClustersPaginationSortOrder] = UNSET,
) -> Response[Union[Any, ListClustersResponse]]:
    """List clusters owned by an organization.

     Sort order: Cluster name

    Args:
        show_inactive (Union[Unset, None, bool]):  Default: True.
        pagination_page (Union[Unset, None, str]):
        pagination_limit (Union[Unset, None, int]):
        pagination_as_of_time (Union[Unset, None, datetime.datetime]):
        pagination_sort_order (Union[Unset, None, CockroachCloudListClustersPaginationSortOrder]):

    Returns:
        Response[Union[Any, ListClustersResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        show_inactive=show_inactive,
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
    *,
    client: Client,
    show_inactive: Union[Unset, None, bool] = True,
    pagination_page: Union[Unset, None, str] = UNSET,
    pagination_limit: Union[Unset, None, int] = UNSET,
    pagination_as_of_time: Union[Unset, None, datetime.datetime] = UNSET,
    pagination_sort_order: Union[Unset, None, CockroachCloudListClustersPaginationSortOrder] = UNSET,
) -> Optional[Union[Any, ListClustersResponse]]:
    """List clusters owned by an organization.

     Sort order: Cluster name

    Args:
        show_inactive (Union[Unset, None, bool]):  Default: True.
        pagination_page (Union[Unset, None, str]):
        pagination_limit (Union[Unset, None, int]):
        pagination_as_of_time (Union[Unset, None, datetime.datetime]):
        pagination_sort_order (Union[Unset, None, CockroachCloudListClustersPaginationSortOrder]):

    Returns:
        Response[Union[Any, ListClustersResponse]]
    """

    return sync_detailed(
        client=client,
        show_inactive=show_inactive,
        pagination_page=pagination_page,
        pagination_limit=pagination_limit,
        pagination_as_of_time=pagination_as_of_time,
        pagination_sort_order=pagination_sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    show_inactive: Union[Unset, None, bool] = True,
    pagination_page: Union[Unset, None, str] = UNSET,
    pagination_limit: Union[Unset, None, int] = UNSET,
    pagination_as_of_time: Union[Unset, None, datetime.datetime] = UNSET,
    pagination_sort_order: Union[Unset, None, CockroachCloudListClustersPaginationSortOrder] = UNSET,
) -> Response[Union[Any, ListClustersResponse]]:
    """List clusters owned by an organization.

     Sort order: Cluster name

    Args:
        show_inactive (Union[Unset, None, bool]):  Default: True.
        pagination_page (Union[Unset, None, str]):
        pagination_limit (Union[Unset, None, int]):
        pagination_as_of_time (Union[Unset, None, datetime.datetime]):
        pagination_sort_order (Union[Unset, None, CockroachCloudListClustersPaginationSortOrder]):

    Returns:
        Response[Union[Any, ListClustersResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        show_inactive=show_inactive,
        pagination_page=pagination_page,
        pagination_limit=pagination_limit,
        pagination_as_of_time=pagination_as_of_time,
        pagination_sort_order=pagination_sort_order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    show_inactive: Union[Unset, None, bool] = True,
    pagination_page: Union[Unset, None, str] = UNSET,
    pagination_limit: Union[Unset, None, int] = UNSET,
    pagination_as_of_time: Union[Unset, None, datetime.datetime] = UNSET,
    pagination_sort_order: Union[Unset, None, CockroachCloudListClustersPaginationSortOrder] = UNSET,
) -> Optional[Union[Any, ListClustersResponse]]:
    """List clusters owned by an organization.

     Sort order: Cluster name

    Args:
        show_inactive (Union[Unset, None, bool]):  Default: True.
        pagination_page (Union[Unset, None, str]):
        pagination_limit (Union[Unset, None, int]):
        pagination_as_of_time (Union[Unset, None, datetime.datetime]):
        pagination_sort_order (Union[Unset, None, CockroachCloudListClustersPaginationSortOrder]):

    Returns:
        Response[Union[Any, ListClustersResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            show_inactive=show_inactive,
            pagination_page=pagination_page,
            pagination_limit=pagination_limit,
            pagination_as_of_time=pagination_as_of_time,
            pagination_sort_order=pagination_sort_order,
        )
    ).parsed
