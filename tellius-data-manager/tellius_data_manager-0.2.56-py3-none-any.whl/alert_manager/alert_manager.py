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
import os
from pathlib import Path
from typing import Dict

from tellius_data_manager.config_reader.config_reader_factory import ConfigReaderFactory
from tellius_data_manager.utils import dict2obj


class AlertManager:
    """Abstraction to manage the process sending an alert.

    Args:
        name: name of the AlertManager
        secrets: Configuration for secret ConfigReader
    """

    _config_reader_factory = ConfigReaderFactory

    def __init__(self, name: str, secrets: Dict, **kwargs) -> None:
        self._name = name
        self._secret_reader = self._config_reader_factory.generate(
            configuration=secrets
        )
        self._secret_key = secrets["name"]

    @property
    def secrets(self):
        config = self._secret_reader.parse_configuration_file(
            configuration_file=os.path.join(Path.home(), ".tdm", "secrets.yml")
        )[self._secret_key]
        return dict2obj(config)

    def send_alert(self, message_content: str) -> None:
        """Send an alert with prescribed message content.

        Args:
            message_content: arbitrary string of message content.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} is a base class. It must implement the Pipe interface."
        )
