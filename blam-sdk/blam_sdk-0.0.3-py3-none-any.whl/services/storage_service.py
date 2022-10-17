from blam_sdk.sdk_config import SdkConfig
from blam_sdk.services.base_service import BlamBaseService


class StorageService(BlamBaseService):
    def __init__(self, config: SdkConfig = None):
        super().__init__("storage", config)

    def create_account(
        self,
        bucket_name: str,
        description: str = None,
        use: str = None,
        account_type: str = "s3",
    ):
        return self._post(
            "/",
            {
                "bucket_name": bucket_name,
                "description": description,
                "use": use,
                "account_type": account_type,
            },
        )

    def get_upload_url(self, key, bucket=None, use=None):
        url_path = f"upload?key={key}"
        if use is not None:
            return self._get(f"{url_path}&use={use}")
        else:
            return self._get(f"{url_path}&bucket={bucket}")
