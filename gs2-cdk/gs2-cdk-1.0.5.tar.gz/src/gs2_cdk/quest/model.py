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


class Contents:
    metadata: str
    complete_acquire_actions: List[AcquireAction]
    weight: int

    def __init__(
            self,
            metadata: str = None,
            complete_acquire_actions: List[AcquireAction] = None,
            weight: int = None,
    ):
        self.metadata = metadata
        self.complete_acquire_actions = complete_acquire_actions
        self.weight = weight

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.complete_acquire_actions:
            properties["CompleteAcquireActions"] = [
                element.properties()
                for element in self.complete_acquire_actions
            ]
        if self.weight:
            properties["Weight"] = self.weight
        return properties


class Reward:
    action: str
    request: str
    item_id: str
    value: int

    def __init__(
            self,
            action: str = None,
            request: str = None,
            item_id: str = None,
            value: int = None,
    ):
        self.action = action
        self.request = request
        self.item_id = item_id
        self.value = value

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.action:
            properties["Action"] = self.action
        if self.request:
            properties["Request"] = self.request
        if self.item_id:
            properties["ItemId"] = self.item_id
        if self.value:
            properties["Value"] = self.value
        return properties
