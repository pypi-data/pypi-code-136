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
from tellius_data_manager.factory import Factory


class ConfigRequiredFactory(Factory):
    """Factory abstraction designed to generate Pipe objects given the class name and the configuration (as a dict)."""

    @classmethod
    def _validate(cls, configuration: dict) -> bool:
        if "name" not in configuration.keys():
            raise AttributeError(
                'configuration does not have required value "name" as a parameter.'
            )

        if "config" not in configuration.keys():
            raise AttributeError(
                'configuration does not have required value "config" as a parameter.'
            )

        return True
