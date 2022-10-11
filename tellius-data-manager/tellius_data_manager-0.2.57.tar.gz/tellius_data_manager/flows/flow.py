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

from tellius_data_manager.pipes._pipe_state import _PipeState
from tellius_data_manager.pipes.pipe_status import PipeStatus
from tellius_data_manager.tellius_object import TelliusObject


class Flow(TelliusObject):
    """
    A flow is a collection of Pipes that are executed as a unit. A Flow can be composed
    additionally of additional subflows.
    """
    def __init__(self, flow_config: dict, subflow: bool = True, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__name = flow_config["name"]
        self.__pipes = flow_config["pipes"]
        self.__sub = "sub" if subflow else ""
        self._state: _PipeState = _PipeState()

    @property
    def status(self) -> PipeStatus:
        """Retrieve the status of a flow

        Returns: Flow status

        """
        return self._state.status

    @status.setter
    def status(self, value: PipeStatus) -> None:
        """Set the status of a flow

        Args:
            value: value of status to be set

        """
        self._state.status = value

    @property
    def info(self) -> Dict:
        """Metadata about the flow

        Returns: The flows metadata

        """
        return self._state.metadata

    def run(self, target: str) -> Flow:
        """Execute the flow.

        TODO: Need to change target concept...
        Args:
            target: The target of th estart of the pipeline.

        Returns: Instance of the flow

        """

        self._logger.info("Starting %sflow %s", self.__sub, self.__name)

        # Queue up all pipe status
        for pipe in self.__pipes:
            pipe.status = PipeStatus.QUEUED

        # Execute round of parents / roots
        processed_count = 0
        for pipe in self.__pipes:
            if len(pipe.parents) == 0:
                pipe.run(source=target)

        # Handle failed status

        # Execute recursively the remaining processing steps.
        remaining_pipes_to_process = sum(
            [1 for pipe in self.__pipes if pipe.status is PipeStatus.QUEUED]
        )
        failed_pipes = sum(
            [1 for pipe in self.__pipes if pipe.status is PipeStatus.FAILURE]
        )

        failed_pipes_exist = failed_pipes > 0
        queue_pipes_exist = remaining_pipes_to_process > 0
        current_metadata = {}
        while queue_pipes_exist and not failed_pipes_exist:
            for pipe in self.__pipes:
                parents_executed = sum(
                    [
                        1
                        for parent in pipe.parents
                        if parent.status is PipeStatus.SUCCESS
                    ]
                ) == len(pipe.parents)
                parent_failed = sum(
                    [
                        1
                        for parent in pipe.parents
                        if parent.status is PipeStatus.FAILURE
                    ]
                )
                if parent_failed > 0:
                    pipe.status = PipeStatus.FAILURE
                elif pipe.status is PipeStatus.QUEUED and parents_executed:
                    pipe.run()
                    current_metadata = pipe.info

            remaining_pipes_to_process = sum(
                [1 for pipe in self.__pipes if pipe.status is PipeStatus.QUEUED]
            )
            failed_pipes = sum(
                [1 for pipe in self.__pipes if pipe.status is PipeStatus.FAILURE]
            )

            failed_pipes_exist = failed_pipes > 0
            queue_pipes_exist = remaining_pipes_to_process > 0

        self.status = PipeStatus.SUCCESS if failed_pipes == 0 else PipeStatus.FAILURE
        for key, value in current_metadata.items():
            self._state.update_metadata(key, value)

        return self
