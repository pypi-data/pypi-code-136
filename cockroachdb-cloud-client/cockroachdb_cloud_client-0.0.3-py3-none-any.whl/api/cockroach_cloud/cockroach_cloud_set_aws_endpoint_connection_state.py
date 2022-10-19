from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.aws_endpoint_connection import AwsEndpointConnection
from ...models.cockroach_cloud_set_aws_endpoint_connection_state_json_body import (
    CockroachCloudSetAwsEndpointConnectionStateJsonBody,
)
from ...types import Response


def _get_kwargs(
    cluster_id: str,
    endpoint_id: str,
    *,
    client: Client,
    json_body: CockroachCloudSetAwsEndpointConnectionStateJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/clusters/{cluster_id}/networking/aws-endpoint-connections/{endpoint_id}".format(
        client.base_url, cluster_id=cluster_id, endpoint_id=endpoint_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, AwsEndpointConnection]]:
    if response.status_code == 200:
        response_200 = AwsEndpointConnection.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, AwsEndpointConnection]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cluster_id: str,
    endpoint_id: str,
    *,
    client: Client,
    json_body: CockroachCloudSetAwsEndpointConnectionStateJsonBody,
) -> Response[Union[Any, AwsEndpointConnection]]:
    """Sets the AWS Endpoint Connection state based on what is passed in the body: accepted or rejected.
    The \"status\" in the returned proto does not reflect the latest post-update status, but rather
    the status before the state is transitioned.

    Args:
        cluster_id (str):
        endpoint_id (str):
        json_body (CockroachCloudSetAwsEndpointConnectionStateJsonBody):

    Returns:
        Response[Union[Any, AwsEndpointConnection]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        endpoint_id=endpoint_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cluster_id: str,
    endpoint_id: str,
    *,
    client: Client,
    json_body: CockroachCloudSetAwsEndpointConnectionStateJsonBody,
) -> Optional[Union[Any, AwsEndpointConnection]]:
    """Sets the AWS Endpoint Connection state based on what is passed in the body: accepted or rejected.
    The \"status\" in the returned proto does not reflect the latest post-update status, but rather
    the status before the state is transitioned.

    Args:
        cluster_id (str):
        endpoint_id (str):
        json_body (CockroachCloudSetAwsEndpointConnectionStateJsonBody):

    Returns:
        Response[Union[Any, AwsEndpointConnection]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        endpoint_id=endpoint_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cluster_id: str,
    endpoint_id: str,
    *,
    client: Client,
    json_body: CockroachCloudSetAwsEndpointConnectionStateJsonBody,
) -> Response[Union[Any, AwsEndpointConnection]]:
    """Sets the AWS Endpoint Connection state based on what is passed in the body: accepted or rejected.
    The \"status\" in the returned proto does not reflect the latest post-update status, but rather
    the status before the state is transitioned.

    Args:
        cluster_id (str):
        endpoint_id (str):
        json_body (CockroachCloudSetAwsEndpointConnectionStateJsonBody):

    Returns:
        Response[Union[Any, AwsEndpointConnection]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        endpoint_id=endpoint_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: str,
    endpoint_id: str,
    *,
    client: Client,
    json_body: CockroachCloudSetAwsEndpointConnectionStateJsonBody,
) -> Optional[Union[Any, AwsEndpointConnection]]:
    """Sets the AWS Endpoint Connection state based on what is passed in the body: accepted or rejected.
    The \"status\" in the returned proto does not reflect the latest post-update status, but rather
    the status before the state is transitioned.

    Args:
        cluster_id (str):
        endpoint_id (str):
        json_body (CockroachCloudSetAwsEndpointConnectionStateJsonBody):

    Returns:
        Response[Union[Any, AwsEndpointConnection]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            endpoint_id=endpoint_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
