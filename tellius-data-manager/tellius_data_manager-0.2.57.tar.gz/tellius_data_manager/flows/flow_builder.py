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
from tellius_data_manager.flows.flow import Flow

from tellius_data_manager.pipes.pipe_factory import PipeFactory


class FlowBuilder:
    @classmethod
    def build(cls, pipe_config: dict) -> Flow:

        flow = dict()
        flow["name"] = pipe_config["name"]
        flow["pipes"] = list()
        for pipe in pipe_config["pipes"]:
            flow["pipes"].append(PipeFactory.generate(configuration=pipe))

        # create pipe lookup
        pipe_lookup = {}
        for pipe in flow["pipes"]:
            pipe_lookup[pipe.name] = pipe

        # Link parents
        for pipe in flow["pipes"]:
            parent_string_list = pipe.parents
            pipe.parents = []
            for parent in parent_string_list:
                pipe.parents.append(pipe_lookup[parent])

        # Link children
        # TODO

        return Flow(flow_config=flow)
