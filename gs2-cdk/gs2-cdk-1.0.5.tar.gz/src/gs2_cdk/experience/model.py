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


class Threshold:
    metadata: str
    values: List[int]

    def __init__(
            self,
            metadata: str = None,
            values: List[int] = None,
    ):
        self.metadata = metadata
        self.values = values

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.values:
            properties["Values"] = [
                element
                for element in self.values
            ]
        return properties
