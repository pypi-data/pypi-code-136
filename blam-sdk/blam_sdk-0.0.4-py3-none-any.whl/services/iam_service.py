from blam_sdk.sdk_config import SdkConfig
from blam_sdk.services.base_service import BlamBaseService


class IamService(BlamBaseService):
    def __init__(self, config: SdkConfig = None):
        super().__init__("iam", config)

    def create_org(self, name: str, description: str = None):
        return self._post("/org", {"name": name, "description": description})
