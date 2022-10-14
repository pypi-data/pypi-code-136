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


class JobEntry:
    script_id: str
    args: str
    max_try_count: int

    def __init__(
            self,
            script_id: str = None,
            args: str = None,
            max_try_count: int = None,
    ):
        self.script_id = script_id
        self.args = args
        self.max_try_count = max_try_count

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.script_id:
            properties["ScriptId"] = self.script_id
        if self.args:
            properties["Args"] = self.args
        if self.max_try_count:
            properties["MaxTryCount"] = self.max_try_count
        return properties


class JobResultBody:
    try_number: int
    status_code: int
    result: str
    try_at: int

    def __init__(
            self,
            try_number: int = None,
            status_code: int = None,
            result: str = None,
            try_at: int = None,
    ):
        self.try_number = try_number
        self.status_code = status_code
        self.result = result
        self.try_at = try_at

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.try_number:
            properties["TryNumber"] = self.try_number
        if self.status_code:
            properties["StatusCode"] = self.status_code
        if self.result:
            properties["Result"] = self.result
        if self.try_at:
            properties["TryAt"] = self.try_at
        return properties
