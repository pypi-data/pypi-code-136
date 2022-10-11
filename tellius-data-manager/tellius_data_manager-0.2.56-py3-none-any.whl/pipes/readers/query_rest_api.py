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
import urllib3

from tellius_data_manager.pipes.readers.reader_pipe import ReaderPipe


class QueryRestAPI(ReaderPipe):
    urllib3.disable_warnings()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _run(self, connection_config: str = None, **kwargs) -> ReaderPipe:
        raise self._return_base_object_error()
