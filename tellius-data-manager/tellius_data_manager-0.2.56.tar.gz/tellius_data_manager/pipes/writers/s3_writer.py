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
from warnings import warn

from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_writers.dataframe_writer_factory import (
    DataframeWriterFactory,
)
from tellius_data_manager.pipes.writers.file_writer import FileWriter


class S3Writer(FileWriter):
    def __init__(self, **kwargs):
        warn(
            f"{self.__class__.__name__} will be deprecated.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(**kwargs)
        self._df_writer = DataframeWriterFactory.generate(
            configuration=kwargs["writer"]
        )
