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

import pandas as pd

from tellius_data_manager.pipes.transformers.transformer_pipe import TransformerPipe


class AddDateFromFilename(TransformerPipe):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _run(self, **kwargs) -> TransformerPipe:
        if len(self._parents) == 1:
            filename = self._parents[0].info["file"]
            data: pd.DataFrame = self._parents[0].info["data"]
        else:
            raise ValueError("No parent Pipe was provided.")

        if not filename:
            raise ValueError("'filename' not found in parent Pipe's metadata.")

        if data is None:
            raise ValueError("'data' not found in parent Pipe's metadata.")

        # Split out the date portion of the file
        date = str.split(
            os.path.splitext(filename)[0], "_"  # Get the name without the extension
        )

        data.insert(data.shape[1], "Date", str(date[1]))

        self._state.update_metadata(key="data", value=data)

        return self
