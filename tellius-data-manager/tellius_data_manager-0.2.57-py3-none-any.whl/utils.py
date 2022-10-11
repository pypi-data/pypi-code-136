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
import json


class dynamic_object:
    def __init__(self, some_dictionary: dict):
        self.__dict__.update(some_dictionary)


def dict2obj(some_dictionary: dict) -> dynamic_object:
    return json.loads(json.dumps(some_dictionary), object_hook=dynamic_object)
