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


class FormModel:
    name: str
    metadata: str
    slots: List[SlotModel]

    def __init__(
            self,
            name: str,
            slots: List[SlotModel],
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.slots = slots

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.slots:
            properties["Slots"] = [
                element.properties()
                for element in self.slots
            ]
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return FormModelRef(
            namespace_name=namespace_name,
            form_model_name=self.name,
        )


class MoldModel:
    name: str
    metadata: str
    initial_max_capacity: int
    max_capacity: int
    form_model: FormModel

    def __init__(
            self,
            name: str,
            initial_max_capacity: int,
            max_capacity: int,
            form_model: FormModel,
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.initial_max_capacity = initial_max_capacity
        self.max_capacity = max_capacity
        self.form_model = form_model

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.initial_max_capacity:
            properties["InitialMaxCapacity"] = self.initial_max_capacity
        if self.max_capacity:
            properties["MaxCapacity"] = self.max_capacity
        if self.form_model:
            properties["FormModel"] = self.form_model.properties()
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return MoldModelRef(
            namespace_name=namespace_name,
            mold_name=self.name,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-09-09'
    namespace_name: str
    mold_models: List[MoldModel]
    form_models: List[FormModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            mold_models: List[MoldModel],
            form_models: List[FormModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.mold_models = mold_models
        self.form_models = form_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Formation::CurrentFormMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "mold_models": [
                    element.properties()
                    for element in self.mold_models
                ],
                "form_models": [
                    element.properties()
                    for element in self.form_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    transaction_setting: TransactionSetting
    update_mold_script: ScriptSetting
    update_form_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            transaction_setting: TransactionSetting = None,
            update_mold_script: ScriptSetting = None,
            update_form_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.transaction_setting = transaction_setting
        self.update_mold_script = update_mold_script
        self.update_form_script = update_form_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Formation::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.transaction_setting:
            properties["TransactionSetting"] = self.transaction_setting.properties()
        if self.update_mold_script:
            properties["UpdateMoldScript"] = self.update_mold_script.properties()
        if self.update_form_script:
            properties["UpdateFormScript"] = self.update_form_script.properties()
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
            mold_models: List[MoldModel],
            form_models: List[FormModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            mold_models=mold_models,
            form_models=form_models,
        ).add_depends_on(
            self,
        )
        return self


class FormModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    slots: List[SlotModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            slots: List[SlotModel],
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.slots = slots

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Formation::FormModelMaster"

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
        if self.slots:
            properties["Slots"] = [
                element.properties()
                for element in self.slots
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return FormModelMasterRef(
            namespace_name=namespace_name,
            form_model_name=self.name,
        )

    def get_attr_form_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.FormModelId"
        )


class MoldModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    form_model_name: str
    initial_max_capacity: int
    max_capacity: int

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            form_model_name: str,
            initial_max_capacity: int,
            max_capacity: int,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.form_model_name = form_model_name
        self.initial_max_capacity = initial_max_capacity
        self.max_capacity = max_capacity

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Formation::MoldModelMaster"

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
        if self.form_model_name:
            properties["FormModelName"] = self.form_model_name
        if self.initial_max_capacity:
            properties["InitialMaxCapacity"] = self.initial_max_capacity
        if self.max_capacity:
            properties["MaxCapacity"] = self.max_capacity
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return MoldModelMasterRef(
            namespace_name=namespace_name,
            mold_name=self.name,
        )

    def get_attr_mold_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.MoldModelId"
        )
