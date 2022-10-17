import requests

from blam_sdk import SdkConfig
from blam_sdk.services import AssetService, StorageService


class AssetStorageHelper:
    def __init__(self, config: SdkConfig = None):
        self.asset_service = AssetService(config)
        self.storage_service = StorageService(config)

    def download_file(self, asset_id, download_dir):
        download_url = self.asset_service.get_download_url(asset_id)
        file_ext = download_url.split("?")[0].split(".")[-1]
        req = requests.get(download_url, stream=True)
        dl_path = f"{download_dir}/{asset_id}.{file_ext}"
        with open(dl_path, "wb") as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return dl_path

    def upload_file(self, file_path, bucket=None, use=None):
        if bucket is None and use is None:
            raise ValueError("Must provide either bucket or use")
        key = file_path.split("/")[-1]
        upload_url = self.storage_service.get_upload_url(key, bucket, use)
        req = requests.put(
            upload_url["upload_url"], data=open(file_path, "rb")
        )
        if req.status_code != 200:
            raise Exception(f"Error uploading file: {req.text}")
        return f"s3://{upload_url['bucket']}/{key}"
