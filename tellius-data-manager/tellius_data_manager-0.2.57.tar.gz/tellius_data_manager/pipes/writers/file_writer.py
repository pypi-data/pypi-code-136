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
import uuid

import pandas as pd

from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_writers.dataframe_writer_factory import (
    DataframeWriterFactory,
)
from tellius_data_manager.pipes.writers.writer_pipe import WriterPipe


class FileWriter(WriterPipe):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._df_writer = DataframeWriterFactory.generate(
            configuration=kwargs["writer"]
        )

    def _run(self, filename: str = None, **kwargs) -> WriterPipe:
        if len(self.parents) != 1:
            raise ValueError(
                "Pipeline has no parents or numerous parents, but requires a single parent"
            )

        data: pd.DataFrame = self._parents[0].info["data"]

        if not filename:
            filename = f"output_`{uuid.uuid4().hex}.csv"

        self._state.update_metadata(key="file", value=filename)

        self._df_writer.execute(
            **{
                "df": data,
                "filename": filename,
                **kwargs
            }
        )

        return self
