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
import io
import warnings

import pandas as pd
from azure.storage.blob import BlobServiceClient

from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_readers.csv_reader import (
    CSVReader,
)

warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


class AzureBlobParquetReader(CSVReader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._container = kwargs.get("container")

    def execute(self, filename: str = None, **kwargs) -> pd.DataFrame:
        # There is a well known bug in boto3 that will cause this to raise an invalid warning. Sessions work with a
        # collection pool and are handled behind the scenes.
        warnings.filterwarnings(
            action="ignore", message="unclosed", category=ResourceWarning
        )

        self._logger.info(f"Reading object {filename} from container {self._container}")

        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(
            self._secrets.connection_string
        )

        # Create the container if it doesn't exist
        if self._container not in [
            container["name"] for container in blob_service_client.list_containers()
        ]:
            container_client = blob_service_client.create_container(self._container)
        # else:
        #     container_client = blob_service_client.get_container(self._container)

        container_client = blob_service_client.get_container_client(
            container=self._container
        )

        if filename is None:
            df = pd.DataFrame()
            for blob in container_client.list_blobs():
                blob_client = container_client.get_blob_client(blob=blob)
                data = io.StringIO(blob_client.download_blob().readall().decode())
                df = pd.concat([df, pd.read_parquet(data)])

        return df
