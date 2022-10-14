# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from __future__ import annotations

from enum import Enum
from ..core import *


class AccessToken:
    owner_id: str
    token: str
    user_id: str
    expire: int
    time_offset: int

    def __init__(
            self,
            owner_id: str = None,
            token: str = None,
            user_id: str = None,
            expire: int = None,
            time_offset: int = None,
    ):
        self.owner_id = owner_id
        self.token = token
        self.user_id = user_id
        self.expire = expire
        self.time_offset = time_offset

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.owner_id:
            properties["OwnerId"] = self.owner_id
        if self.token:
            properties["Token"] = self.token
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.expire:
            properties["Expire"] = self.expire
        if self.time_offset:
            properties["TimeOffset"] = self.time_offset
        return properties
