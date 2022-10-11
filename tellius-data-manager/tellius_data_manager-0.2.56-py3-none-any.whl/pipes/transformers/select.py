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

from tellius_data_manager.pipes.transformers.transformer_pipe import TransformerPipe


class Select(TransformerPipe):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__columns = kwargs.get("columns")

    def _run(self, **kwargs) -> TransformerPipe:
        if len(self._parents) == 1:
            data: pd.DataFrame = self._parents[0].info["data"]
        else:
            raise ValueError("No parent Pipe was provided.")

        if data is None:
            raise ValueError("'data' not found in parent Pipe's metadata.")

        inadmissable_columns = set(self.__columns) - set(data.columns)
        self._logger.info(f"Inadmissable Columns: {list(inadmissable_columns)}")
        data = data[list(set(self.__columns) - inadmissable_columns)]

        self._state.update_metadata(key="data", value=data)

        return self
