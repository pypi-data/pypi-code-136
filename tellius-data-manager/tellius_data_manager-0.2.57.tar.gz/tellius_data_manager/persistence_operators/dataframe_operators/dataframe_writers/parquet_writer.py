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
import pandas as pd

from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_writers.dataframe_writer import (
    DataframeWriter,
)


class ParquetWriter(DataframeWriter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, df: pd.DataFrame, **kwargs):
        kwargs["path_or_buf"] = os.path.join(self._directory, kwargs.pop("filename"))
        df.to_parquet(index=False, **kwargs)
