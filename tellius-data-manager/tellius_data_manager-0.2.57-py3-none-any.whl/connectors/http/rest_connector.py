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
import requests

from tellius_data_manager.config_reader.config_reader import ConfigReader
from tellius_data_manager.connectors.connector import Connector


class RestConnector(Connector):
    def __init__(self, configuration_name: str, **kwargs):
        super().__init__(**kwargs)
        self._config_reader = ConfigReader()
        self._configuration = configuration_name

    @property
    def connect(self):
        configuration = self._config_reader.parse_configuration_file(
            configuration_file=self._configuration
        )
        _access_token_url = configuration[""]
        _access_token = requests.post(_access_token_url, verify=False)
        return "Bearer " + _access_token.json()["access_token"]
