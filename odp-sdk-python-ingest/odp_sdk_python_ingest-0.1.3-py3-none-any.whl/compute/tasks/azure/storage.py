from typing import Optional, Union, Dict

from azure.storage.blob import BlobServiceClient, ContainerClient
from prefect import Task
from prefect.utilities.tasks import defaults_from_attrs


class AzBlobPut(Task):
    def __init__(
        self,
        container: Optional[str] = None,
        blob: Optional[str] = None,
        overwrite: bool = False,
        **kwargs
    ):
        self.container = container
        self.blob = blob
        self.overwrite = overwrite

        super().__init__(**kwargs)

    @defaults_from_attrs(
        "container",
        "blob",
        "overwrite",
    )
    def run(
        self,
        data: Union[str, bytes],
        connection_string: str,
        metadata: Optional[Dict[str, str]] = None,
        container: str = None,
        blob: str = None,
        overwrite: bool = None,
    ) -> str:
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )
        container_client: ContainerClient = blob_service_client.get_container_client(
            container
        )

        blob_client = container_client.upload_blob(
            name=blob, data=data, metadata=metadata, overwrite=overwrite
        )

        return blob_client.url
