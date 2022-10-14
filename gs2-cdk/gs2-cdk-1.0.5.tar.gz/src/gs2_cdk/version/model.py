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


class Version:
    major: int
    minor: int
    micro: int

    def __init__(
            self,
            major: int = None,
            minor: int = None,
            micro: int = None,
    ):
        self.major = major
        self.minor = minor
        self.micro = micro

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.major:
            properties["Major"] = self.major
        if self.minor:
            properties["Minor"] = self.minor
        if self.micro:
            properties["Micro"] = self.micro
        return properties


class Status:
    version_model: VersionModel
    current_version: Version

    def __init__(
            self,
            version_model: VersionModel = None,
            current_version: Version = None,
    ):
        self.version_model = version_model
        self.current_version = current_version

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.version_model:
            properties["VersionModel"] = self.version_model.properties()
        if self.current_version:
            properties["CurrentVersion"] = self.current_version.properties()
        return properties


class TargetVersion:
    version_name: str
    version: Version
    body: str
    signature: str

    def __init__(
            self,
            version_name: str = None,
            version: Version = None,
            body: str = None,
            signature: str = None,
    ):
        self.version_name = version_name
        self.version = version
        self.body = body
        self.signature = signature

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.version_name:
            properties["VersionName"] = self.version_name
        if self.version:
            properties["Version"] = self.version.properties()
        if self.body:
            properties["Body"] = self.body
        if self.signature:
            properties["Signature"] = self.signature
        return properties


class SignTargetVersion:
    region: str
    owner_id: str
    namespace_name: str
    version_name: str
    version: Version

    def __init__(
            self,
            region: str = None,
            owner_id: str = None,
            namespace_name: str = None,
            version_name: str = None,
            version: Version = None,
    ):
        self.region = region
        self.owner_id = owner_id
        self.namespace_name = namespace_name
        self.version_name = version_name
        self.version = version

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.region:
            properties["Region"] = self.region
        if self.owner_id:
            properties["OwnerId"] = self.owner_id
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.version_name:
            properties["VersionName"] = self.version_name
        if self.version:
            properties["Version"] = self.version.properties()
        return properties
