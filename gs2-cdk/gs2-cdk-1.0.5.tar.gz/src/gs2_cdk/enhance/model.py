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


class BonusRate:
    rate: float
    weight: int

    def __init__(
            self,
            rate: float = None,
            weight: int = None,
    ):
        self.rate = rate
        self.weight = weight

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.rate:
            properties["Rate"] = self.rate
        if self.weight:
            properties["Weight"] = self.weight
        return properties


class Material:
    material_item_set_id: str
    count: int

    def __init__(
            self,
            material_item_set_id: str = None,
            count: int = None,
    ):
        self.material_item_set_id = material_item_set_id
        self.count = count

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.material_item_set_id:
            properties["MaterialItemSetId"] = self.material_item_set_id
        if self.count:
            properties["Count"] = self.count
        return properties
