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

from tellius_data_manager.pipes.pipe_stats.pipe_stats import PipeStats


class DataFrameStats(PipeStats):
    """
    Stats for a pandas DataFrame.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._stats = {
            "row_count": None,
            "column_count": None,
            "column_names": list(),
            "column_stats": dict(),
        }

    def calculate(self, data: pd.DataFrame) -> PipeStats:
        """Calculate stats for the pandas DataFrame.

        Args:
            data: data to compute stats of.

        Returns: instance of PipeStats.

        """
        self._stats["row_count"], self._stats["column_count"] = data.shape
        self._stats["column_names"] = list(data.columns)

        # Get stats for each of the columns
        for column in data.columns:
            self._stats["column_stats"][column] = {}

        for item in data.isna().sum().items():
            self._stats["column_stats"][item[0]]["missing_count"] = item[1]

        for item in data.isnull().sum().items():
            self._stats["column_stats"][item[0]]["null_count"] = item[1]

        for item in data.dtypes.items():
            self._stats["column_stats"][item[0]]["type"] = item[1]

        return self
