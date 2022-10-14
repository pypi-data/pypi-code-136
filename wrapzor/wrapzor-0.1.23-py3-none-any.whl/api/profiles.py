from httpx import AsyncClient, Response

from wrapzor.core.tokens import inject_tokens, ZohoApi


@inject_tokens()
async def get_profiles(client: AsyncClient, api: ZohoApi) -> Response:
    url = f"{api.domain}/crm/{api.version}/settings/profiles"
    response = await client.get(url)
    return response
