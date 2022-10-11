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
from enum import Enum


class PipeStatus(Enum):
    """The state of a pipe, within a pipeline.
    SUCCESS when a pipe has been executed and the result was successful execution.
    FAILURE when a pipe has been executed and the execution ended in a terminal fault.
    QUEUED when the pipe is waiting to execute.
    RUNNING when the pipe is currently being executed.
    DEFINING when the pipe is being defined.
    UNDEFINED when the pipe has not yet been initialized.
    BLOCKED when any one parent of a pipe has failed."""

    SUCCESS = 1
    FAILURE = 2
    QUEUED = 3
    RUNNING = 4
    DEFINING = 5
    UNDEFINED = 6
    BLOCKED = 7
