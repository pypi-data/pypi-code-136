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
from warnings import warn

from tellius_data_manager.state_manager.dataframe_state_manager import (
    DataframeStateManager,
)


class AzureBlobStateManager(DataframeStateManager):
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
        warn(
            f"{self.__class__.__name__} will be deprecated.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(
            state_object_name=state_object_name,
            name=name,
            version=version,
            job_id=job_id,
            pipeline_id=pipeline_id,
            reader=reader,
            writer=writer,
            **kwargs,
        )
