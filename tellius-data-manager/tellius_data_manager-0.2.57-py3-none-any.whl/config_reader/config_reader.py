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
from typing import Dict


class ConfigReader:
    """Base class abstracting the ability to read configurations"""

    def __init__(self, **kwargs):
        pass

    def parse_configuration_file(self, **kwargs) -> Dict:
        """Implements the ability to read a configuration file given specific inputs."""
        raise NotImplementedError(
            f"{self.__class__.__name__} is a base class. It must implement the Pipe interface."
        )
