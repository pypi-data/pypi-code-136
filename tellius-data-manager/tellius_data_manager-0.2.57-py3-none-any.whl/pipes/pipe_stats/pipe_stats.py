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

from tellius_data_manager.tellius_object import TelliusObject


class PipeStats(TelliusObject):
    """
    Stats are information deemed interesting to be tracked for a data pipeline.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._stats = None

    @property
    def stats(self) -> Dict:
        """The computes stats for a pipe.

        Returns: Statistics computed from the pipe as a dictionary.

        """
        return self._stats

    def calculate(self, data: object) -> PipeStats:
        """Calculate teh statistics for the dataframe.

        Args:
            data: data object to be passed to have statistics computed on.

        Returns: Instance of PipeStats

        """
        self._return_base_object_error()
