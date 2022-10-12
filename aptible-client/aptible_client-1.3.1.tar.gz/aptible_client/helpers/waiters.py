import json
import logging
import time
from typing import Any, Dict, Optional

from .constants import ORGANIZATION_ID, ENVIRONMENT_ID, ASSET_DELIMITER
from .exceptions import AssetFailedException, AssetTimeoutException, EnvironmentNotFoundException
from .misc import environments_matched_by_params_in_list
from ..api.assets_api import AssetsApi
from ..api.environments_api import EnvironmentsApi
from ..api_client import ApiClient
from ..configuration import Configuration
from ..model.asset_input import AssetInput


logger = logging.getLogger()


class Waiter:
    assets_api_instance: AssetsApi
    environments_api_instance: EnvironmentsApi
    environment_id: str
    organization_id: str
    force_new: bool

    def __init__(
            self,
            configuration: Configuration,
            environment_id: str = ENVIRONMENT_ID,
            organization_id: str = ORGANIZATION_ID,
            force_new: Optional[bool] = False,
    ):
        self.environment_id = environment_id
        self.organization_id = organization_id
        self.force_new = force_new
        self.logger = logger
        self.assets_api_instance = AssetsApi(ApiClient(configuration))
        self.environments_api_instance = EnvironmentsApi(ApiClient(configuration))
        self._validate_environment_access()

    def _validate_environment_access(self):
        try:
            environment = self.environments_api_instance.environment_get(
                self.environment_id,
                self.organization_id,
                _check_return_type=False
            )
            if not environment:
                raise EnvironmentNotFoundException(f"Unable to find environment id ({self.environment_id}) "
                                          f"or cannot access it on organization {self.organization_id}")
        except Exception:
            self.logger.exception("Unable to validate environment with error")
            raise

    def get_or_launch_asset_and_wait(
        self,
        asset: str,
        asset_parameters: Dict[str, Any]
    ):
        # get if found
        # launch and wait if not
        if not self.force_new:
            environment_assets = self.environments_api_instance.environment_get_assets(
                self.environment_id,
                self.organization_id,
                _check_return_type=False,
            )
            self.logger.debug("Querying environment assets if created previously to avoid re-creation")
            environment_asset = environments_matched_by_params_in_list(
                asset=asset,
                asset_parameters=asset_parameters,
                assets_list=environment_assets
            )
            if environment_asset:
                if environment_asset.status == "FAILED":
                    # relaunch asset if failed to try to kick-start it
                    self.logger.info(f"Found failed asset ({environment_asset.asset}) being searched and "
                                     f"relaunching: {environment_asset.id}")
                    return self.relaunch_failed_asset_and_wait(environment_asset.id, asset, asset_parameters)
                # it was previously deployed or is deploying, return it
                self.logger.info(f"Found asset ({environment_asset.asset}) being searched: {environment_asset.id}")
                return self.assets_api_instance.asset_get(
                    environment_asset.id,
                    self.environment_id,
                    self.organization_id
                )
        return self.always_launch_asset_and_wait(asset, asset_parameters)

    def wait_for_asset_to_be_status(
            self,
            asset_id: str,
            status: Optional[str] = "DEPLOYED"
    ) -> Dict[str, Any]:
        # Automatically break after 25 mins no matter what
        breakout_time = time.time() + (25 * 60)
        retries = 0
        max_retries = 3

        while time.time() < breakout_time and retries < max_retries:
            try:
                asset_data = self.assets_api_instance.asset_get(
                    asset_id,
                    self.environment_id,
                    self.organization_id,
                    _check_return_type=False
                )
                if str(asset_data['status']) == status:
                    self.logger.info(f"Asset is '{status}': ({asset_id})")
                    return asset_data
                if str(asset_data['status']) == "FAILED":
                    self.logger.exception(f"Asset deployed with failed!")
                    raise AssetFailedException(f"Unable to act on asset with ID ({asset_id}) in environment "
                                               f"({self.environment_id})")
            except Exception:
                self.logger.exception(f"Unable to act on asset on environment id ({self.environment_id}) "
                                      f"with exception")
                retries += 1
            time.sleep(10)
            if retries == max_retries:
                self.logger.exception(
                    f"Unable to create asset on environment id ({self.environment_id}) with exception"
                )
                raise AssetFailedException(f"Unable to create asset in environment ({self.environment_id} "
                                           f"after {max_retries} attempts")

            self.logger.info(f"Still waiting for asset to be status of '{status}': {asset_id}")

        raise AssetTimeoutException(f"Waited for asset ({asset_id}) to deploy and it took too long! (25 minutes)")

    def relaunch_failed_asset_and_wait(
            self,
            asset_id: str,
            asset: str,
            asset_parameters: Dict[str, Any],
    ):
        asset_input = AssetInput(
            asset=asset,
            asset_parameters=asset_parameters,
            asset_version=asset.split(ASSET_DELIMITER)[-1],
        )
        api_response = self.assets_api_instance.asset_update(
            asset_id,
            self.environment_id,
            self.organization_id,
            asset_input,
            _check_return_type=False
        )
        asset_id = api_response.id

        # Wait until asset is ready so we can use data from it
        self.logger.info(f"Relaunching/updating asset of type {asset}")
        asset_data = self.wait_for_asset_to_be_status(asset_id)
        return asset_data

    def always_launch_asset_and_wait(
            self,
            asset: str,
            asset_parameters: Dict[str, Any],
    ):
        # Launch Asset
        asset_input = AssetInput(
            asset=asset,
            asset_parameters=asset_parameters,
            asset_version=asset.split(ASSET_DELIMITER)[-1],
        )
        api_response = self.assets_api_instance.asset_create(
            self.environment_id,
            self.organization_id,
            asset_input,
            _check_return_type=False
        )
        asset_id = api_response.id

        # Wait until asset is ready so we can use data from it
        self.logger.info(f"Creating asset of type {asset}")
        asset_data = self.wait_for_asset_to_be_status(asset_id)
        return asset_data

    def always_destroy_asset_and_wait(
            self,
            asset_id: str,
    ):
        self.assets_api_instance.asset_delete(
            asset_id,
            self.environment_id,
            self.organization_id,
            _check_return_type=False
        )

        # Wait until asset is ready so we can use data from it
        self.logger.info(f"Destroying asset ({asset_id})")
        asset_data = self.wait_for_asset_to_be_status(asset_id, status="DESTROYED")
        return asset_data

    def find_destroy_asset_and_wait(self, asset, asset_parameters: Dict[str, Any]) -> None:
        environment_assets = self.environments_api_instance.environment_get_assets(
            self.environment_id,
            self.organization_id,
            _check_return_type=False,
        )
        self.logger.debug("Querying environment assets if created previously for destruction")
        environment_asset = environments_matched_by_params_in_list(
            asset=asset,
            asset_parameters=asset_parameters,
            assets_list=environment_assets
        )
        if environment_asset:
            # check if asset_parameters passed in are a subset of the existing set in the DB, if so we're good to go
            self.logger.info(f"Found asset ({environment_asset.asset}) being searched: {environment_asset.id}")
            self.always_destroy_asset_and_wait(environment_asset.id)
            return

        self.logger.warning(
            f"Unable to find non-destroyed asset ({asset}) with asset parameters {json.dumps(asset_parameters)}"
        )
