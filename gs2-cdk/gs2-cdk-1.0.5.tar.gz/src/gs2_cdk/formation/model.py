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


class Slot:
    name: str
    property_id: str
    metadata: str

    def __init__(
            self,
            name: str = None,
            property_id: str = None,
            metadata: str = None,
    ):
        self.name = name
        self.property_id = property_id
        self.metadata = metadata

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.property_id:
            properties["PropertyId"] = self.property_id
        if self.metadata:
            properties["Metadata"] = self.metadata
        return properties


class SlotModel:
    name: str
    property_regex: str
    metadata: str

    def __init__(
            self,
            name: str = None,
            property_regex: str = None,
            metadata: str = None,
    ):
        self.name = name
        self.property_regex = property_regex
        self.metadata = metadata

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.property_regex:
            properties["PropertyRegex"] = self.property_regex
        if self.metadata:
            properties["Metadata"] = self.metadata
        return properties


class SlotWithSignature:

    class PropertyType(Enum):
        GS2_INVENTORY = "gs2_inventory"
        GS2_DICTIONARY = "gs2_dictionary"
    name: str
    property_type: PropertyType
    body: str
    signature: str
    metadata: str

    def __init__(
            self,
            name: str = None,
            property_type: PropertyType = None,
            body: str = None,
            signature: str = None,
            metadata: str = None,
    ):
        self.name = name
        self.property_type = property_type
        self.body = body
        self.signature = signature
        self.metadata = metadata

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.property_type:
            properties["PropertyType"] = self.property_type
        if self.body:
            properties["Body"] = self.body
        if self.signature:
            properties["Signature"] = self.signature
        if self.metadata:
            properties["Metadata"] = self.metadata
        return properties


class AcquireActionConfig:
    name: str
    config: List[Config]

    def __init__(
            self,
            name: str = None,
            config: List[Config] = None,
    ):
        self.name = name
        self.config = config

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.config:
            properties["Config"] = [
                element.properties()
                for element in self.config
            ]
        return properties
