import typing_extensions

from cvg_sdk.apis.tags import TagValues
from cvg_sdk.apis.tags.health_api import HealthApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.HEALTH: HealthApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.HEALTH: HealthApi,
    }
)
