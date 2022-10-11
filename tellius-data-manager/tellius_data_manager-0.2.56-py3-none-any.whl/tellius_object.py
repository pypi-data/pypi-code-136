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
from __future__ import absolute_import

import logging
import traceback
from typing import List

from tellius_data_manager.alert_manager.alert_manager_factory import AlertManagerFactory
from tellius_data_manager.config_reader.config_reader import ConfigReader
from tellius_data_manager.config_reader.config_reader_factory import ConfigReaderFactory
from tellius_data_manager.alert_manager.alert_manager import AlertManager
from tellius_data_manager.logs.tellius_logger import TelliusLogger


class TelliusObject:
    """Base class for all objects within Tellius Data Manager (tellius_data_manager). It's purpose is to encapsulate logging and other
    common behavior found in writing coded to manage, support or execute data transformations in tellius_data_manager.
    """

    _config_reader_factory = ConfigReaderFactory

    def __init__(self, **kwargs):
        logging.setLoggerClass(TelliusLogger)
        self._logger = logging.getLogger(__name__)
        self._config_parser: ConfigReader = kwargs.get("config_reader")
        if not self._config_parser:
            self._config_parser = self.__create_default_config_reader()
        if "secrets" in kwargs.keys():
            self._secret_reader = self._config_reader_factory.generate(
                kwargs.get("secrets")
            )
            self._secret_key = kwargs.get("secrets")["name"]
        if not kwargs.get("alert_managers"):
            self.__alert_managers: List[AlertManager] = self.__generate_alert_managers()
        else:
            self.__alert_managers: List[AlertManager] = self.__generate_alert_managers(
                alert_manager_configs=kwargs.get("alert_managers")
            )

    def __generate_alert_managers(self, alert_manager_configs: List = None) -> List:
        alert_managers = list()
        if not alert_manager_configs:
            configuration = self._config_parser.parse_configuration_file()
        else:
            configuration = alert_manager_configs
        for alert_manager in configuration["alert_managers"]:
            alert_manager["config"]["name"] = alert_manager["name"]
            alert_managers.append(
                AlertManagerFactory.generate(configuration=alert_manager)
            )

        return alert_managers

    def __create_default_config_reader(self) -> ConfigReader:
        configuration = {
            "type": "yamlconfigreader",
            "config": {"name": "Default YAML Configuration Reader"},
            "name": "Default YAML Configuration Reader",
        }

        return self._config_reader_factory.generate(configuration=configuration)

    def _handle_error(self, exception: Exception = None) -> None:
        message = traceback.format_exc()
        self._logger.error(msg=message)
        self._raise_alert(exception)

    def _raise_alert(self, exception: Exception) -> None:
        for alert in self.__alert_managers:
            try:
                alert.send_alert((traceback.format_exc()))
            except:
                self._logger.warning(msg=f'There is an issue with the alerting mechanism: {traceback.format_exc()}')

    def _return_base_object_error(self):
        return NotImplementedError(
            f"{self.__class__.__name__} is a base class. It must implement the Pipe interface."
        )

    @property
    def _secrets(self):
        raise self._return_base_object_error()
