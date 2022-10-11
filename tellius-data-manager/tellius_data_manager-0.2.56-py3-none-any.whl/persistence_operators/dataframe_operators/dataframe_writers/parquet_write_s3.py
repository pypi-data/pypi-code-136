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
from io import StringIO

import boto3 as boto3
import pandas as pd

from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_writers.parquet_writer import (
    ParquetWriter,
)


class ParquetWriterS3(ParquetWriter):
    """Write Parquet file to S3.

    Args:
        bucket: Name of bucket in S3 that data will be written to.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._bucket = kwargs.get("bucket")

    def execute(self, df: pd.DataFrame, **kwargs):
        """
        Write data to a Parquet file in S3
        Args:
            df: Pandas dataframe with the data that is to be written to S3.
        Returns:

        """
        _secrets = self._secrets

        csv_buffer = StringIO()
        df.to_parquet(csv_buffer, index=False, sep=",", **kwargs)

        session = boto3.Session(
            aws_access_key_id=_secrets.access_key_id,
            aws_secret_access_key=_secrets.secret_access_key_id,
        )

        # Creating S3 Resource From the Session.
        s3_resource = session.resource("s3")
        s3_resource.Object(
            self._bucket, "Airwatch/AirWatch_Device_Application_PROD.csv"
        ).put(Body=csv_buffer.getvalue())
