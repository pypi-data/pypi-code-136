from asyncio import sleep
from pathlib import Path

from httpx import AsyncClient, Response

from wrapzor.api.utils import get_job_state, get_job_id
from wrapzor.core.tokens import inject_tokens, ZohoApi
from wrapzor.errors import TimeOut
from wrapzor.logs import logs
from wrapzor.utils import now_str
from wrapzor.env import BULKS_DIR

COMPLETED = "COMPLETED"
HOUR = 60 * 60


@inject_tokens()
async def create_bulk(data: dict, client: AsyncClient, api: ZohoApi) -> Response:
    url = f"{api.domain}/crm/bulk/{api.version}/read"
    response = await client.post(url=url, data=data)
    return response


@inject_tokens()
async def get_bulk_status(id: str, client: AsyncClient, api: ZohoApi) -> Response:
    url = f"{api.domain}/crm/bulk/v3/read/{id}"
    response = await client.get(url=url)
    return response


async def wait_for_job_done(id: str, seconds: int = 5, max_wait=HOUR):
    slept = 0
    while True:
        response = await get_bulk_status(id)
        print(response.status_code)
        print(response.json())

        state = get_job_state(response)
        logs.debug(f"Fetching job progress: {state}")
        if slept >= max_wait:
            raise TimeOut(response)
        if state == COMPLETED:
            break
        await sleep(seconds)
        slept += seconds
    return response


@inject_tokens()
async def download_bulk_result(
        id: str,
        client: AsyncClient,
        api: ZohoApi,
) -> Response:
    url = f"{api.domain}/crm/bulk/{api.version}/read/{id}/result"
    response = await client.get(url=url)
    return response


def _get_path(path: str | Path) -> Path:
    return Path(path) if isinstance(path, str) else path


async def get_bulk(filename: str,
                   data: dict,
                   path: str | Path | None = None,
                   filename_only: bool = False) -> Path:
    _path = _get_path(BULKS_DIR if not path else path)

    res_creation = await create_bulk(data=data)
    job_id = get_job_id(res_creation)
    await wait_for_job_done(id=job_id)
    response = await download_bulk_result(id=job_id)
    final_path = _path / f"{filename}.zip" if filename_only else _path / f"{filename}___{id}_{now_str()}.zip"
    final_path.write_bytes(response.content)
    return final_path
