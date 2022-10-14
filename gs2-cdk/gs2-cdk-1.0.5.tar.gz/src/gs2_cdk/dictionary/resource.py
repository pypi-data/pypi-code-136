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
from .ref import *


class EntryModel:
    name: str
    metadata: str

    def __init__(
            self,
            name: str,
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return EntryModelRef(
            namespace_name=namespace_name,
            entry_name=self.name,
        )


class CurrentMasterData(CdkResource):

    version: str = '2020-04-30'
    namespace_name: str
    entry_models: List[EntryModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            entry_models: List[EntryModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.entry_models = entry_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Dictionary::CurrentEntryMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "entry_models": [
                    element.properties()
                    for element in self.entry_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    entry_script: ScriptSetting
    duplicate_entry_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            entry_script: ScriptSetting = None,
            duplicate_entry_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.entry_script = entry_script
        self.duplicate_entry_script = duplicate_entry_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Dictionary::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.entry_script:
            properties["EntryScript"] = self.entry_script.properties()
        if self.duplicate_entry_script:
            properties["DuplicateEntryScript"] = self.duplicate_entry_script.properties()
        if self.log_setting:
            properties["LogSetting"] = self.log_setting.properties()
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
    ):
        return NamespaceRef(
            namespace_name=self.name,
        )

    def get_attr_namespace_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.NamespaceId"
        )

    def master_data(
            self,
            entry_models: List[EntryModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            entry_models=entry_models,
        ).add_depends_on(
            self,
        )
        return self


class EntryModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Dictionary::EntryModelMaster"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.metadata:
            properties["Metadata"] = self.metadata
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return EntryModelMasterRef(
            namespace_name=namespace_name,
            entry_name=self.name,
        )

    def get_attr_entry_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.EntryModelId"
        )
