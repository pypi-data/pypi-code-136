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

from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_readers.csv_reader import (
    CSVReader,
)
from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_readers.dataframe_reader_factory import (
    DataframeReaderFactory,
)
from tellius_data_manager.pipes.readers.reader_pipe import ReaderPipe


class ReadLocalFile(ReaderPipe):
    """Pipe for reading a local file into a pandas DataFrame."""

    def __init__(self, **kwargs):
        """

        Args:
            **kwargs: See `tellius_data_manager.pipes.readers.read.Read` and `tellius_data_manager.pipes.pipe.Pipe` for additional arguments

        __Overrides__:

        def run(full_pathname: str, filename: str, folder: str) -> Pipe:

        Reading from a file requires either a filename or a full_pathname. You can optionally override the folder that
        file where the source file is located.
        Args:
            full_pathname: Fully qualified filename with path.
            filename: Name of file without path.
            folder: [Optional] If you wish to override the filepath that was used to construct the Pipe.
            **kwargs: Optional arguments

        Returns: Pipe after it has executed
        """
        super().__init__(**kwargs)
        self._reader = DataframeReaderFactory.generate(configuration=kwargs["reader"])

    def _run(
        self,
        filename: str,
        **kwargs,
    ) -> ReaderPipe:
        self._state.update_metadata(key="file", value=filename)

        self._state.update_metadata(
            key="data",
            value=self._reader.execute(
                **{
                    "file": filename,
                }
            ),
        )

        return self
