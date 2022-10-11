# Copyright 2022 Tellius, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import hashlib
import warnings

import pandas as pd
from azure.storage.blob import BlobServiceClient

from tellius_data_manager.errors.tdm_error import TDMError
from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_writers.csv_writer import (
    CSVWriter,
)

warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


class AzureBlobCSVWriter(CSVWriter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._container = kwargs.get("container")

    def execute(self, df: pd.DataFrame, filename: str, **kwargs):

        self._logger.info(f"Writing object {filename} to container {self._container}")

        output = df.to_csv(index=False, sep=",", encoding="utf-8", **kwargs)

        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(
            self._secrets.connection_string
        )

        # Create the container if it doesn't exist
        if self._container not in [
            container["name"] for container in blob_service_client.list_containers()
        ]:
            _ = blob_service_client.create_container(self._container)

        blob_client = blob_service_client.get_blob_client(
            container=self._container, blob=filename
        )

        blob_client.upload_blob(output, overwrite=True, blob_type="BlockBlob")

        blobs = blob_service_client.get_container_client(self._container).list_blobs()

        blobs = [blob for blob in blobs]
        if filename not in [blob["name"] for blob in blobs]:
            raise TDMError(
                "Blob {filename} not successfully written to Azure Blob Container {self._container}."
            )
        else:
            self._logger.info(
                f"Blob {filename} successfully written to Azure Blob Container {self._container}."
            )

        blob_md5 = [
            blob["content_settings"]["content_md5"]
            for blob in blobs
            if filename == blob["name"]
        ][0]
        if hashlib.md5(output.encode()).digest() != blob_md5:
            raise TDMError(
                f"While Blob {filename} was successfully written, the MD5 checksum does not match the "
                f"source MD5 checksum - and so it has been deleted."
            )
        else:
            self._logger.info(f"Blob {filename} has a valid MD5 checksum.")
