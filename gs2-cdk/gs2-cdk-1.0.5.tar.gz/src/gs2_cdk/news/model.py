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


class News:
    section: str
    content: str
    title: str
    schedule_event_id: str
    timestamp: int
    front_matter: str

    def __init__(
            self,
            section: str = None,
            content: str = None,
            title: str = None,
            schedule_event_id: str = None,
            timestamp: int = None,
            front_matter: str = None,
    ):
        self.section = section
        self.content = content
        self.title = title
        self.schedule_event_id = schedule_event_id
        self.timestamp = timestamp
        self.front_matter = front_matter

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.section:
            properties["Section"] = self.section
        if self.content:
            properties["Content"] = self.content
        if self.title:
            properties["Title"] = self.title
        if self.schedule_event_id:
            properties["ScheduleEventId"] = self.schedule_event_id
        if self.timestamp:
            properties["Timestamp"] = self.timestamp
        if self.front_matter:
            properties["FrontMatter"] = self.front_matter
        return properties


class SetCookieRequestEntry:
    key: str
    value: str

    def __init__(
            self,
            key: str = None,
            value: str = None,
    ):
        self.key = key
        self.value = value

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.key:
            properties["Key"] = self.key
        if self.value:
            properties["Value"] = self.value
        return properties
