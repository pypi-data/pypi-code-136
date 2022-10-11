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
import os

import pandas as pd

from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_readers.dataframe_reader import (
    DataframeReader,
)


class ParquetReader(DataframeReader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._directory = kwargs["folder"]

    def execute(self, **kwargs) -> pd.DataFrame:
        kwargs["path"] = os.path.join(self._directory, kwargs["file"])
        df = pd.read_parquet(**kwargs)
        return df
