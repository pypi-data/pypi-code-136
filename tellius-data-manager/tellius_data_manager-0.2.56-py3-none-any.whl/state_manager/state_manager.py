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

import pandas as pd

from tellius_data_manager.tellius_object import TelliusObject


class StateManager(TelliusObject):
    """A StateManager is used to manage and track the state of a data pipeline through its various steps.

    Args:
        name: Name of the StateManager
        job_id: preferably unique identifier for the job
        pipeline_id: This identifies the pipeline regardless of when it was executed. It is static, whereas job_id is dynamic.
        version: Version number for the pipeline
        state_object_name: Name give to the state object as persisted.

    """

    def __init__(
        self,
        name: str,
        job_id: str,
        pipeline_id: str,
        version: float,
        state_object_name: str,
        **kwargs,
    ):
        super().__init__(name=name, **kwargs)
        self._state_object = state_object_name
        self._state_model = {
            "pipeline_id": pipeline_id,
            "job_id": job_id,
            "pipeline_name": state_object_name,
            "version": version,
            "name": name,
            "start_time": None,
            "stop_time": None,
            "flow_model": dict(),
            "status": None,
            "meta_state": dict(),
            "pull_stats": dict(),
            "push_stats": dict(),
        }
        self._state = pd.DataFrame()

    def read(self, **kwargs) -> StateManager:
        """To read into memory the state of a data pipeline."""
        raise self._return_base_object_error()

    def update(self, **kwargs) -> StateManager:
        """To update the state of a data pipeline."""
        raise self._return_base_object_error()
