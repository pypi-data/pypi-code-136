from blam_sdk.sdk_config import SdkConfig
from blam_sdk.services.base_service import BlamBaseService


class ConnectionsService(BlamBaseService):
    def __init__(self, config: SdkConfig = None):
        super().__init__("connections", config)

    def get_connections(self):
        return self._get()

    def create_connected_account(self, name, account_type):
        return self._post("", {"name": name, "account_type": account_type})
