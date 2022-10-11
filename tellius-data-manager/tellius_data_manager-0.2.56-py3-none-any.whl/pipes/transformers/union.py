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


class Union(TransformerPipe):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _run(self, **kwargs) -> TransformerPipe:

        if len(self._parents) == 2:
            left_df: pd.DataFrame = self._parents[0].info["data"]
            right_df: pd.DataFrame = self._parents[1].info["data"]
        else:
            raise ValueError("Two parent Pipes are required.")

        if left_df is None:
            raise ValueError("'data' not found in first parent pipe")

        if right_df is None:
            raise ValueError("'data' not found in second parent pipe")

        if set(left_df.columns) - set(right_df.columns) != set():
            raise ValueError("The two datasets do not have the same columns.")

        df = pd.concat([left_df, right_df], ignore_index=True)

        self._state.update_metadata(key="data", value=df)

        return self
