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
from typing import Dict, Callable

from tellius_data_manager.pipes.logics.logics_pipe import LogicsPipe


class IfStep(LogicsPipe):
    """LogicsPipe designed to execute a logical 'if' condition."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _run(self, if_test_function: Callable, inputs: Dict = None) -> LogicsPipe:
        """Execute the conditional step in a pipe.

        Args:
            if_test_function: function that must return a boolean
            inputs: inputs that the if_test_function will take as inputs

        Returns: Instance of LogicsPipe

        """
        if inputs:
            if_truth = if_test_function(**inputs)
        else:
            if_truth = if_test_function()
        self._state.update_metadata(key="if_truth", value=if_truth)

        return self
