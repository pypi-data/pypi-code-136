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

import yaml

from tellius_data_manager.config_reader.config_reader import ConfigReader


class YamlConfigReader(ConfigReader):
    """Read YAML Configurations

    Args:
        config_file: Name of configuration file.
    """

    def __init__(self, config_file: str = None, **kwargs):
        super().__init__(**kwargs)
        self._configuration_file = config_file

    def parse_configuration_file(
        self, configuration_file: str = None, **kwargs
    ) -> Dict:
        """Read the configuration stored in a YAML file.

        Args:
            configuration_file: Filename where configuration yaml exists. Should be a fully qualified path - preferred.
            **kwargs: Various other arguments.

        Returns: Configuration file.

        Raises:
            ValueError: When the configuration file doesn't exist, is not a file (e.g. is a directory) or has an
            improper extension.

        """
        if configuration_file:
            self._configuration_file = configuration_file

        if not self._configuration_file:
            self._configuration_file = os.path.join(
                str(Path.home()), ".tdm", "config.yml"
            )

        if not os.path.exists(self._configuration_file):
            raise ValueError(
                f"configuration_file={self._configuration_file} does not exist."
            )

        if not os.path.isfile(self._configuration_file):
            raise ValueError(
                f"configuration_file={self._configuration_file} is not a file."
            )

        if os.path.splitext(self._configuration_file)[1][1:].lower() not in [
            "yaml",
            "yml",
        ]:
            raise ValueError(
                f"configuration_file={self._configuration_file} must end in one of yml, yaml, YML or YAML."
            )

        with open(self._configuration_file, "r") as stream:
            config: Dict = yaml.safe_load(stream)

        return config
