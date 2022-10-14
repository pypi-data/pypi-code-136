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


class VersionModel:

    class Scope(Enum):
        PASSIVE = "passive"
        ACTIVE = "active"
    name: str
    metadata: str
    warning_version: Version
    error_version: Version
    scope: str
    current_version: Version
    need_signature: bool
    signature_key_id: str

    def __init__(
            self,
            name: str,
            warning_version: Version,
            error_version: Version,
            scope: Scope,
            metadata: str = None,
            current_version: Version = None,
            need_signature: bool = None,
            signature_key_id: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.warning_version = warning_version
        self.error_version = error_version
        self.scope = scope
        self.current_version = current_version
        self.need_signature = need_signature
        self.signature_key_id = signature_key_id

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.warning_version:
            properties["WarningVersion"] = self.warning_version.properties()
        if self.error_version:
            properties["ErrorVersion"] = self.error_version.properties()
        if self.scope:
            properties["Scope"] = self.scope
        if self.current_version:
            properties["CurrentVersion"] = self.current_version.properties()
        if self.need_signature:
            properties["NeedSignature"] = self.need_signature
        if self.signature_key_id:
            properties["SignatureKeyId"] = self.signature_key_id
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return VersionModelRef(
            namespace_name=namespace_name,
            version_name=self.name,
        )

    @staticmethod
    def passive(
        need_signature: bool,
        name: str = None,
        metadata: str = None,
        warning_version: Version = None,
        error_version: Version = None,
        signature_key_id: str = None,
    ) -> VersionModel:
        return VersionModel(
            scope=VersionModel.Scope.PASSIVE,
            name=name,
            metadata=metadata,
            warning_version=warning_version,
            error_version=error_version,
            need_signature=need_signature,
            signature_key_id=signature_key_id,
        )

    @staticmethod
    def active(
        current_version: Version,
        name: str = None,
        metadata: str = None,
        warning_version: Version = None,
        error_version: Version = None,
        signature_key_id: str = None,
    ) -> VersionModel:
        return VersionModel(
            scope=VersionModel.Scope.ACTIVE,
            name=name,
            metadata=metadata,
            warning_version=warning_version,
            error_version=error_version,
            current_version=current_version,
            signature_key_id=signature_key_id,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-10-09'
    namespace_name: str
    version_models: List[VersionModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            version_models: List[VersionModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.version_models = version_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Version::CurrentVersionMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "version_models": [
                    element.properties()
                    for element in self.version_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    assume_user_id: str
    accept_version_script: ScriptSetting
    check_version_trigger_script_id: str
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            assume_user_id: str,
            description: str = None,
            accept_version_script: ScriptSetting = None,
            check_version_trigger_script_id: str = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.assume_user_id = assume_user_id
        self.accept_version_script = accept_version_script
        self.check_version_trigger_script_id = check_version_trigger_script_id
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Version::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.assume_user_id:
            properties["AssumeUserId"] = self.assume_user_id
        if self.accept_version_script:
            properties["AcceptVersionScript"] = self.accept_version_script.properties()
        if self.check_version_trigger_script_id:
            properties["CheckVersionTriggerScriptId"] = self.check_version_trigger_script_id
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
            version_models: List[VersionModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            version_models=version_models,
        ).add_depends_on(
            self,
        )
        return self


class VersionModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    warning_version: Version
    error_version: Version
    scope: str
    current_version: Version
    need_signature: bool
    signature_key_id: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            warning_version: Version,
            error_version: Version,
            scope: str,
            current_version: Version,
            need_signature: bool,
            signature_key_id: str,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.warning_version = warning_version
        self.error_version = error_version
        self.scope = scope
        self.current_version = current_version
        self.need_signature = need_signature
        self.signature_key_id = signature_key_id

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Version::VersionModelMaster"

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
        if self.warning_version:
            properties["WarningVersion"] = self.warning_version.properties()
        if self.error_version:
            properties["ErrorVersion"] = self.error_version.properties()
        if self.scope:
            properties["Scope"] = self.scope
        if self.current_version:
            properties["CurrentVersion"] = self.current_version.properties()
        if self.need_signature:
            properties["NeedSignature"] = self.need_signature
        if self.signature_key_id:
            properties["SignatureKeyId"] = self.signature_key_id
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return VersionModelMasterRef(
            namespace_name=namespace_name,
            version_name=self.name,
        )

    def get_attr_version_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.VersionModelId"
        )
