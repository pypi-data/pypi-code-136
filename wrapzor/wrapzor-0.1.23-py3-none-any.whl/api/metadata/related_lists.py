from httpx import AsyncClient, Response

from wrapzor.core.tokens import inject_tokens, ZohoApi
from wrapzor.core.verify import verify_data
from wrapzor.models.metadata.related_lists import RelatedLists, RelatedListsRequest


@verify_data(input_model=RelatedListsRequest, output_model=RelatedLists)
@inject_tokens()
async def get_related_lists(client: AsyncClient, api: ZohoApi, params: dict) -> Response:
    url = f"{api.domain}/crm/{api.version}/settings/related_lists"
    response = await client.get(url, params=params)
    return response
