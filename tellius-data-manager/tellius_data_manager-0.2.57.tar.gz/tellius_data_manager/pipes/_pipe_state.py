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
from __future__ import annotations

from typing import Dict

from tellius_data_manager.pipes.pipe_status import PipeStatus


class _PipeState:
    """The state of a Pipe."""

    def __init__(self) -> None:
        self.__status: PipeStatus = PipeStatus.UNDEFINED
        self.__metadata: Dict = dict()
        self.__runtime = None

    @property
    def status(self) -> PipeStatus:
        """Get the Pipe's state.

        Returns: Pipe's state

        """
        return self.__status

    @status.setter
    def status(self, value) -> None:
        """Set the Pipe's status.

        Args:
            value: New value for the pipes status

        """
        self.__status = value

    def update_metadata(self, key: str, value: object) -> None:
        """Update metadata about the pipeline."""
        self.__metadata[key] = value

    @property
    def metadata(self):
        """Get's teh Pipe's metadata.

        Returns: Pipe's metadata

        """
        return self.__metadata
