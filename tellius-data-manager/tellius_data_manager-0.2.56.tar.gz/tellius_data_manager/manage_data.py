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
from uuid import uuid4

from tellius_data_manager.flows.flow_manager import FlowManager
from tellius_data_manager.tellius_object import TelliusObject


class ManageData(TelliusObject):
    def __init__(self, config_reader) -> None:
        super().__init__()

        configuration = config_reader.parse_configuration_file()

        self._flow = FlowManager()
        self._flow.build(flow_config=configuration)
        self._run_id = uuid4()

    def run(self, target: str):
        self._logger.info("Starting run %s", self._run_id)
        self._flow.run(target=target)
