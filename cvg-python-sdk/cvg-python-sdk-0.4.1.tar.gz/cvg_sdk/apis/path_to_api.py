import typing_extensions

from cvg_sdk.paths import PathValues
from cvg_sdk.apis.paths.health_reseller_token_project_project_token import HealthResellerTokenProjectProjectToken

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HEALTH_RESELLER_TOKEN_PROJECT_PROJECT_TOKEN: HealthResellerTokenProjectProjectToken,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HEALTH_RESELLER_TOKEN_PROJECT_PROJECT_TOKEN: HealthResellerTokenProjectProjectToken,
    }
)
