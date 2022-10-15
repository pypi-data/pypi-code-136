from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.cancel_suspended_job_get_payload import CancelSuspendedJobGetPayload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    workspace: str,
    id: str,
    resume_id: int,
    signature: str,
    payload: Union[Unset, CancelSuspendedJobGetPayload] = UNSET,
) -> Dict[str, Any]:
    url = "{}/w/{workspace}/jobs/cancel/{id}/{resume_id}/{signature}".format(
        client.base_url, workspace=workspace, id=id, resume_id=resume_id, signature=signature
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_payload: Union[Unset, Dict[str, Any]] = UNSET
    if not isinstance(payload, Unset):
        json_payload = payload.to_dict()

    params: Dict[str, Any] = {}
    if not isinstance(json_payload, Unset):
        params.update(json_payload)
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[None]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    workspace: str,
    id: str,
    resume_id: int,
    signature: str,
    payload: Union[Unset, CancelSuspendedJobGetPayload] = UNSET,
) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
        workspace=workspace,
        id=id,
        resume_id=resume_id,
        signature=signature,
        payload=payload,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    workspace: str,
    id: str,
    resume_id: int,
    signature: str,
    payload: Union[Unset, CancelSuspendedJobGetPayload] = UNSET,
) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
        workspace=workspace,
        id=id,
        resume_id=resume_id,
        signature=signature,
        payload=payload,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
