import json
import logging

from blam_sdk.sdk_config import SdkConfig
from blam_sdk.services.base_service import BlamBaseService


class AssetService(BlamBaseService):
    def __init__(self, config: SdkConfig = None):
        super().__init__("asset", config)

    def create_asset(self, name, location, asset_type):
        asset = self._post(
            "", {"name": name, "location": location, "asset_type": asset_type}
        )
        logging.info(
            f"""
            Created asset
                ID: {asset['id']}
                Name: {asset['name']}
        """
        )
        return asset

    def add_location_to_asset(self, asset_id, location):
        return self._post(f"{asset_id}/locations", location)

    def update_asset_metadata(self, asset_id, metadata, set_by):
        asset = self._put(
            f"metadata/{asset_id}",
            json.dumps({"set_by": set_by, "metadata": metadata}),
        )
        logging.info(
            f"""
            Uodated Asset Metadata
                ID: {asset['id']}
                Metadata: {asset['metadata']}
        """
        )
        return asset

    def create_asset_with_metadata(
        self, name, location, asset_type, metadata, set_by
    ):
        asset = self.create_asset(name, location, asset_type)
        asset_with_metadata = self.update_asset_metadata(
            asset["id"], metadata, set_by
        )
        return asset_with_metadata

    def get_download_url(self, asset_id):
        return self._get(f"download/{asset_id}")["download_url"]

    def get_assets(self):
        return self._get()
