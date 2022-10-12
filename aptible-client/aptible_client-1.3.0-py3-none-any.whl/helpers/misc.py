import logging
import json
import os
from logging import Logger
from pathlib import Path
from typing import Any, Dict, List

from .constants import AUTH_API_URL, CLOUD_API_URL, ASSET_DELIMITER
from .exceptions import TokensNotFoundException
from ..api.environments_api import EnvironmentsApi
from ..configuration import Configuration
from ..model.environment_input import EnvironmentInput


logger: Logger = logging.getLogger(__name__)


def get_client_configuration() -> Configuration:
    """

    :return:
    """
    local_token = os.getenv("APTIBLE_TOKEN")
    if local_token is None:
        try:
            tokens_json_raw = open(str(Path.home() / ".aptible" / "tokens.json"), "r").read()
            tokens_json = json.loads(tokens_json_raw)
            if not tokens_json.get(AUTH_API_URL):
                raise Exception(f"AUTH_API_URL ({AUTH_API_URL}) key not found in json tokens")
            local_token = tokens_json.get(AUTH_API_URL)
        except Exception as e:
            error_message = "Unable to retrieve tokens from aptible client's default location"
            logger.exception(f"{error_message} Run 'aptible login' to create your token file")
            raise TokensNotFoundException(error_message) from e
    return Configuration(
        access_token=local_token,
        host=CLOUD_API_URL,
    )


def environments_matched_by_params_in_list(asset: str, asset_parameters: Dict[str, Any], assets_list: List[Any]) -> Any:
    for environment_asset in assets_list:
        # if using the same asset name prefix (non version), not destroyed, and same set of asset parameters
        if environment_asset.asset.split(ASSET_DELIMITER)[0:2] == asset.split(ASSET_DELIMITER)[0:2] and \
                environment_asset.status != "DESTROYED" and \
                'data' in environment_asset.current_asset_parameters and \
                asset_parameters.items() <= environment_asset.current_asset_parameters['data'].items():
            return environment_asset
    return None


def update_environment(
    environments_api_instance: EnvironmentsApi,
    environment_id: str,
    organization_id: str,
) -> None:
    environment = environments_api_instance.environment_get(environment_id, organization_id)
    environments_api_instance.environment_update(
        environment_id=environment_id,
        organization_id=organization_id,
        environment_input=EnvironmentInput(
            name=environment.name,
            description=environment.description,
            data={
                "upgrade_environment": True
            }
        )
    )
    logger.info("Sent request to upgrade environment")
