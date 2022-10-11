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

import boto3 as boto3
import pandas as pd

from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_readers.csv_reader import (
    CSVReader,
)

warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


class S3ParquetReader(CSVReader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._bucket = kwargs.get("bucket")

    def execute(self, filename: str, **kwargs) -> pd.DataFrame:
        # There is a well known bug in boto3 that will cause this to raise an invalid warning. Sessions work with a
        # collection pool and are handled behind the scenes.
        warnings.filterwarnings(
            action="ignore", message="unclosed", category=ResourceWarning
        )

        self._logger.info(f"Reading object {filename} from bucket {self._bucket}")

        _secrets = self._secrets

        session = boto3.Session(
            aws_access_key_id=_secrets.access_key_id,
            aws_secret_access_key=_secrets.secret_access_key_id,
        )

        # Creating S3 Resource From the Session.
        s3_resource = session.resource("s3")
        data = (
            s3_resource.Object(self._bucket, filename)
            .get()["Body"]
            .read()
            .decode("utf-8")
        )
        df = pd.read_parquet(io.StringIO(data))

        return df
