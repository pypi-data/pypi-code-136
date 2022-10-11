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

import datetime
from typing import Dict

import pandas as pd

from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_readers.dataframe_reader_factory import (
    DataframeReaderFactory,
)
from tellius_data_manager.persistence_operators.dataframe_operators.dataframe_writers.dataframe_writer_factory import (
    DataframeWriterFactory,
)
from tellius_data_manager.pipes.pipe_status import PipeStatus
from tellius_data_manager.state_manager.state_manager import StateManager


class DataframeStateManager(StateManager):
    """
    StatManager where the state is stored as files within Azure Blob Storage

    writer: Writer for writing to Azure Blob
    reader: Reader for reading from Azure Blob
    """

    def __init__(
        self,
        state_object_name: str,
        writer: Dict,
        reader: Dict,
        pipeline_id: str,
        job_id: str,
        name: str,
        version: float,
        **kwargs,
    ):
        super().__init__(
            state_object_name=state_object_name,
            name=name,
            version=version,
            job_id=job_id,
            pipeline_id=pipeline_id,
            **kwargs,
        )
        self._writer = DataframeWriterFactory.generate(configuration=writer)
        self._reader = DataframeReaderFactory.generate(configuration=reader)

    @property
    def state(self):
        return self._state

    def read(self, asset_filter: str = None, **kwargs) -> StateManager:
        df = self._reader.execute(filename_filter=asset_filter)
        if df.shape[0] > 0:
            df.sort_values(by=["start_time"], ascending=False, inplace=True)
        self._state = df
        return self

    def update(
        self,
        start_time: float,
        stop_time: float,
        flow_model: Dict,
        status: PipeStatus,
        meta_state: Dict,
        pull_stats: Dict,
        push_stats: Dict,
        job_id: str = None,
        **kwargs,
    ) -> StateManager:
        self._state_model.update(
            {
                "start_time": start_time,
                "stop_time": stop_time,
                "flow_model": flow_model,
                "status": status,
                "meta_state": meta_state,
                "pull_stats": pull_stats,
                "push_stats": push_stats,
            }
        )

        if job_id:
            self._state_model.update({"job_id": job_id})

        df = pd.DataFrame.from_records([self._state_model])
        self._writer.execute(
            df=df,
            filename=f"{self._state_object} {int(datetime.datetime.now().timestamp())}",
        )

        return self
