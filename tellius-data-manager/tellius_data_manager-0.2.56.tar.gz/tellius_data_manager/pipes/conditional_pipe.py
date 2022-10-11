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

from tellius_data_manager.pipes.composite_pipe import CompositePipe
from tellius_data_manager.pipes.pipe import Pipe


class ConditionalPipe(CompositePipe):
    """This is a CompositePipe designed to execute a conditional process."""

    def __init__(self, n, **kwargs) -> None:
        super().__init__(**kwargs)

    def _run(self, **kwargs) -> Pipe:
        raise self._return_base_object_error()
