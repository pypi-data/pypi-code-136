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
import os.path
from typing import Dict, List

import pandas
import pandas as pd

from tellius_data_manager.pipes.transformers.transformer_pipe import TransformerPipe
from flatten_json import flatten


class FlattenJSONToTable(TransformerPipe):
    """Flatten data stored either in JSON (python dict) or a list of JSON entries (list of python dict's)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _run(self, **kwargs) -> TransformerPipe:
        if len(self._parents) == 1:
            data: Dict = self._parents[0].info["data"]
        else:
            raise ValueError("No parent Pipe was provided.")

        if data is None:
            raise ValueError("'data' not found in parent Pipe's metadata.")

        if isinstance(data, List) and all(
            [isinstance(data_dict, Dict) for data_dict in data]
        ):

            data: pd.DataFrame = pd.DataFrame(
                [flatten(data_dict) for data_dict in data]
            )
        elif isinstance(data, Dict):
            data: pd.DataFrame = pd.DataFrame(flatten(data))
        else:
            raise ValueError("data must either be a dict or a list of dicts.")

        self._state.update_metadata(key="data", value=data)

        return self
