from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.cmek_cluster_info import CMEKClusterInfo
from ...models.cockroach_cloud_enable_cmek_spec_cmek_cluster_specification import (
    CockroachCloudEnableCMEKSpecCMEKClusterSpecification,
)
from ...types import Response


def _get_kwargs(
    cluster_id: str,
    *,
    client: Client,
    json_body: CockroachCloudEnableCMEKSpecCMEKClusterSpecification,
) -> Dict[str, Any]:
    url = "{}/api/v1/clusters/{cluster_id}/cmek".format(client.base_url, cluster_id=cluster_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CMEKClusterInfo]]:
    if response.status_code == 200:
        response_200 = CMEKClusterInfo.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CMEKClusterInfo]]:
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
    json_body: CockroachCloudEnableCMEKSpecCMEKClusterSpecification,
) -> Response[Union[Any, CMEKClusterInfo]]:
    """Enable CMEK for a cluster.

    Args:
        cluster_id (str):
        json_body (CockroachCloudEnableCMEKSpecCMEKClusterSpecification):  Example:
            {'region_specs': [{'key_spec': {'auth_principal': 'arn:aws:iam::account:role/role-name-
            with-path', 'type': 'AWS_KMS', 'uri': 'arn:aws:kms:us-west-2:111122223333:key/id-of-kms-
            key'}, 'region': 'us-central1'}]}.

    Returns:
        Response[Union[Any, CMEKClusterInfo]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
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
    *,
    client: Client,
    json_body: CockroachCloudEnableCMEKSpecCMEKClusterSpecification,
) -> Optional[Union[Any, CMEKClusterInfo]]:
    """Enable CMEK for a cluster.

    Args:
        cluster_id (str):
        json_body (CockroachCloudEnableCMEKSpecCMEKClusterSpecification):  Example:
            {'region_specs': [{'key_spec': {'auth_principal': 'arn:aws:iam::account:role/role-name-
            with-path', 'type': 'AWS_KMS', 'uri': 'arn:aws:kms:us-west-2:111122223333:key/id-of-kms-
            key'}, 'region': 'us-central1'}]}.

    Returns:
        Response[Union[Any, CMEKClusterInfo]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cluster_id: str,
    *,
    client: Client,
    json_body: CockroachCloudEnableCMEKSpecCMEKClusterSpecification,
) -> Response[Union[Any, CMEKClusterInfo]]:
    """Enable CMEK for a cluster.

    Args:
        cluster_id (str):
        json_body (CockroachCloudEnableCMEKSpecCMEKClusterSpecification):  Example:
            {'region_specs': [{'key_spec': {'auth_principal': 'arn:aws:iam::account:role/role-name-
            with-path', 'type': 'AWS_KMS', 'uri': 'arn:aws:kms:us-west-2:111122223333:key/id-of-kms-
            key'}, 'region': 'us-central1'}]}.

    Returns:
        Response[Union[Any, CMEKClusterInfo]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: str,
    *,
    client: Client,
    json_body: CockroachCloudEnableCMEKSpecCMEKClusterSpecification,
) -> Optional[Union[Any, CMEKClusterInfo]]:
    """Enable CMEK for a cluster.

    Args:
        cluster_id (str):
        json_body (CockroachCloudEnableCMEKSpecCMEKClusterSpecification):  Example:
            {'region_specs': [{'key_spec': {'auth_principal': 'arn:aws:iam::account:role/role-name-
            with-path', 'type': 'AWS_KMS', 'uri': 'arn:aws:kms:us-west-2:111122223333:key/id-of-kms-
            key'}, 'region': 'us-central1'}]}.

    Returns:
        Response[Union[Any, CMEKClusterInfo]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
