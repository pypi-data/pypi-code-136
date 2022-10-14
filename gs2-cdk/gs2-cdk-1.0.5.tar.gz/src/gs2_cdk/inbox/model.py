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


class TimeSpan:
    days: int
    hours: int
    minutes: int

    def __init__(
            self,
            days: int = None,
            hours: int = None,
            minutes: int = None,
    ):
        self.days = days
        self.hours = hours
        self.minutes = minutes

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.days:
            properties["Days"] = self.days
        if self.hours:
            properties["Hours"] = self.hours
        if self.minutes:
            properties["Minutes"] = self.minutes
        return properties
