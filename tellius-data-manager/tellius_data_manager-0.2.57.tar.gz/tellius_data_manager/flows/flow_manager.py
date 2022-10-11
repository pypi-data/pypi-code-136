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
from typing import List

from tellius_data_manager.flows.flow import Flow
from tellius_data_manager.flows.flow_builder import FlowBuilder
from tellius_data_manager.tellius_object import TelliusObject


class FlowManager(TelliusObject):
    """

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__flow_builder: FlowBuilder = FlowBuilder()

        self.__flows: List[Flow] = list()

    def build(self, flow_config):
        for flow in flow_config["pipeline_drivers"]:
            self.__flows.append(self.__flow_builder.build(pipe_config=flow))

    def run(self, target: str):
        for flow in self.__flows:
            flow.run(target=target)
