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
from tellius_data_manager.config_optional_factory import ConfigOptionalFactory
from tellius_data_manager.config_reader.config_reader import ConfigReader


class ConfigReaderFactory(ConfigOptionalFactory):
    """
    Factory abstraction designed to generate ConfigReader objects given the class
    name and the configuration (as a dict).
    """

    _cls_type = ConfigReader
