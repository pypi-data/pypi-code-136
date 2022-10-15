from typing import Any, Dict

import httpx

from ...client import Client
from ...models.resume_suspended_job_post_json_body import ResumeSuspendedJobPostJsonBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    workspace: str,
    id: str,
    resume_id: int,
    signature: str,
    json_body: ResumeSuspendedJobPostJsonBody,
) -> Dict[str, Any]:
    url = "{}/w/{workspace}/jobs/resume/{id}/{resume_id}/{signature}".format(
        client.base_url, workspace=workspace, id=id, resume_id=resume_id, signature=signature
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: ResumeSuspendedJobPostJsonBody,
) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
        workspace=workspace,
        id=id,
        resume_id=resume_id,
        signature=signature,
        json_body=json_body,
    )

    response = httpx.post(
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
    json_body: ResumeSuspendedJobPostJsonBody,
) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
        workspace=workspace,
        id=id,
        resume_id=resume_id,
        signature=signature,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
