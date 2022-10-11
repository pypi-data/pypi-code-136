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

from typing import List, OrderedDict

from tellius_data_manager.flows.flow import Flow
from tellius_data_manager.pipes.pipe import Pipe


class CompositePipe(Pipe):
    """This is a CompositePipe designed to execute a conditional process."""

    def __init__(self, components: List[Pipe] = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self._components: OrderedDict[Pipe] = components or OrderedDict[Pipe]()

    def _run(self, **kwargs) -> Pipe:
        parents = self.parents
        for key, pipe in self._components:
            pipe.parents = parents
            parents = [pipe]

        flow = Flow(pipes=self._components, name=self.name, subflow=True)

        flow = flow.run()

        self.status = flow.status
        for key, value in flow.info:
            self._state.update_metadata(key, value)

        return self
