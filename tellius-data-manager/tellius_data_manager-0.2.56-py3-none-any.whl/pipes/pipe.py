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

import traceback
import uuid
from typing import List, final, Final, Dict

from tellius_data_manager.pipes._pipe_state import _PipeState
from tellius_data_manager.pipes.pipe_stats.pipe_stats_factory import PipeStatsFactory
from tellius_data_manager.pipes.pipe_status import PipeStatus
from tellius_data_manager.tellius_object import TelliusObject


class Pipe(TelliusObject):
    """A Pipe is the basic unit of a transformation pipeline. This base class encapsulates all of the logic around the
    buildout and execution of a pipeline step. A pipe contains

    Args:
        job_id: Unique identifier for job. Changes each run.
        pipeline_id: Unique identifier for a pipeline. Same for all runs.
        pipe_id: Unique identifier for a pipe. Same for all runs.
        name: The name of the pipe step.
        parents: In a pipeline, or DAG, the parents are pipes that must execute before this pipe will execute.
        state: An object that contains metadata around the pipeline_drivers state and additional information.
    """

    _status: Final[PipeStatus] = PipeStatus.DEFINING

    def __init__(
        self,
        job_id: str,
        pipeline_id: str,
        pipe_id: str = None,
        name: str = None,
        parents: List[Pipe] = None,
        stats: Dict = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._name = name
        self._configure_defaults()
        # self._children: List[Pipe] = list()
        self._parents: List[Pipe] = parents or list()
        self._state: _PipeState = _PipeState()
        if stats:
            stats["name"] = f"{name} Stats"
            self._pipe_stats = PipeStatsFactory.generate(
                configuration=stats
            )

        self.pipe_id = pipe_id if pipe_id else uuid.uuid4().hex
        self.pipeline_id = pipeline_id
        self.job_id = job_id

    def _configure_defaults(self):
        """Makes sure that the application is properly configured when no suitable values are otherwise provided."""
        self._pipe_stats = PipeStatsFactory.generate(
            configuration={
                "name": f"{self._name} Stats",
                "type": "nullpipestats",
                "config": {},
            }
        )

    @property
    def stats(self):
        """Return the status for a Pipe

        Returns: Pipe's stats

        """
        return self._pipe_stats.stats

    @property
    def parents(self) -> List[Pipe]:
        """Pipes which appear in the pipeline as predecessors.

        Returns: Collection of Pipes

        """
        return self._parents

    @parents.setter
    def parents(self, value: List[Pipe]) -> None:
        """Set the value of the parents

        Args:
            value: collection of Pipe objects

        Raises:
            ValueError: value is not a list or any member of the list is not a Pipe.

        """
        if not isinstance(value, list) and any(
            [not isinstance(pipe, Pipe) for pipe in value]
        ):
            raise ValueError("value is not of type List[Pipe]")
        self._parents = value

    # @property
    # def children(self):
    #     return self._children
    #
    # @children.setter
    # def children(self, value):
    #     self._children = value

    @property
    def name(self) -> str:
        """

        Returns: name of the Pipe

        """
        return self._name

    @property
    def status(self) -> PipeStatus:
        """Get the Pipe's status.

        Returns: status of the pipe

        """
        return self._state.status

    @status.setter
    def status(self, value) -> None:
        """Set the Pipe's status.

        Args:
            value: new status of the pipe

        Returns:

        """
        self._state.status = value

    @property
    def info(self):
        return self._state.metadata

    def _can_pipe_run(self) -> bool:
        """Test whether a Pipe is ready to execute or not.

        Returns: True if Pipe's dependencies have been met. False otherwise.

        """
        if len(self._parents) == 0:
            return True

        if all([pipe.status == PipeStatus.SUCCESS for pipe in self._parents]):
            return True

        return False

    def _is_pipe_blocked(self) -> bool:
        if any(
            [
                pipe.status == PipeStatus.FAILURE or pipe.status == PipeStatus.BLOCKED
                for pipe in self._parents
            ]
        ):
            return True
        else:
            return False

    @final
    def run(self, parent: Pipe = None, parents: List[Pipe] = None, **kwargs) -> Pipe:
        """Execute a pipeline step. This is either used as a configured pipeline or as a standalone with an extensible
        API.

        Args:
            parent: [Optional] A single parent when the Pipe only has a single parent - will override parents
            parents: [Optional] A list of parents when the Pipe has many parents - will override parents.
            **kwargs:

        Returns: Instance of itself after it has fully executed through the pipeline.

        """
        try:
            self.status = PipeStatus.RUNNING
            self._logger.info("Starting run of stage '%s'", self.name)
            if parent and parents:
                raise ValueError(
                    "Unable to progress. "
                    "Both parent and parents were provided as inputs and only one is allowed."
                )
            elif parent:
                self.parents = [parent]
            elif parents:
                self.parents = parents

            if self._can_pipe_run():
                self._run(**kwargs)
                if "data" in self.info.keys():
                    self._pipe_stats.calculate(data=self.info["data"])
                self.status = PipeStatus.SUCCESS
                self._logger.info("Run of stage '%s' completed successfully.", self.name)
            elif self._is_pipe_blocked():
                self.status = PipeStatus.BLOCKED
                self._logger.info("Stage '%s' is currently blocked.", self.name)
        except:
            self.status = PipeStatus.FAILURE
            self._state.update_metadata(key="error", value=traceback.format_exc())
            self._logger.info("Stage '%s' ended in error.", self.name)
            self._handle_error()
        return self

    def _run(self, **kwargs) -> Pipe:
        raise self._return_base_object_error()
