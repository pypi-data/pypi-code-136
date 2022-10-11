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
from tellius_data_manager.connectors.object_stores.object_store import ObjectStore


class S3(ObjectStore):
    """A Connector is an object designed to be used to connect to a data source. It is NOT the tool that extracts/reads
    insert/write data to or from the data source, but only the connection object as an abstraction. It is used in
    combination of a factory and strategy pattern as part of a data pipeline construct."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def connect(self, **kwargs):
        """Obtains and returns/yields a connection object."""
        raise self._return_base_object_error()
