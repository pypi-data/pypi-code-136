from httpx import AsyncClient, Response

from wrapzor.core.tokens import inject_tokens, ZohoApi


@inject_tokens()
async def cancel_meeting(event_id: str, data: dict, client: AsyncClient, api: ZohoApi) -> Response:
    url = f"{api.domain}/crm/{api.version}/Events/{event_id}/actions/cancel"
    response = await client.post(url, data=data)
    return response