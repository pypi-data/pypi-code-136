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

from tellius_data_manager.tellius_object import TelliusObject
from tellius_data_manager.utils import dict2obj


class PersistenceOperator(TelliusObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def _secrets(self):
        secrets = self._secret_reader.parse_configuration_file(
            configuration_file=os.path.join(Path.home(), ".tdm", "secrets.yml")
        )[self._secret_key]

        return dict2obj(secrets)