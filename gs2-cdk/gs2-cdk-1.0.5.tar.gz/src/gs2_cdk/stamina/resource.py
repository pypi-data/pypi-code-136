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


class StaminaModel:
    name: str
    metadata: str
    recover_interval_minutes: int
    recover_value: int
    initial_capacity: int
    is_overflow: bool
    max_capacity: int
    max_stamina_table: MaxStaminaTable
    recover_interval_table: RecoverIntervalTable
    recover_value_table: RecoverValueTable

    def __init__(
            self,
            name: str,
            recover_interval_minutes: int,
            recover_value: int,
            initial_capacity: int,
            is_overflow: bool,
            metadata: str = None,
            max_capacity: int = None,
            max_stamina_table: MaxStaminaTable = None,
            recover_interval_table: RecoverIntervalTable = None,
            recover_value_table: RecoverValueTable = None,
    ):
        self.name = name
        self.metadata = metadata
        self.recover_interval_minutes = recover_interval_minutes
        self.recover_value = recover_value
        self.initial_capacity = initial_capacity
        self.is_overflow = is_overflow
        self.max_capacity = max_capacity
        self.max_stamina_table = max_stamina_table
        self.recover_interval_table = recover_interval_table
        self.recover_value_table = recover_value_table

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.recover_interval_minutes:
            properties["RecoverIntervalMinutes"] = self.recover_interval_minutes
        if self.recover_value:
            properties["RecoverValue"] = self.recover_value
        if self.initial_capacity:
            properties["InitialCapacity"] = self.initial_capacity
        if self.is_overflow:
            properties["IsOverflow"] = self.is_overflow
        if self.max_capacity:
            properties["MaxCapacity"] = self.max_capacity
        if self.max_stamina_table:
            properties["MaxStaminaTable"] = self.max_stamina_table.properties()
        if self.recover_interval_table:
            properties["RecoverIntervalTable"] = self.recover_interval_table.properties()
        if self.recover_value_table:
            properties["RecoverValueTable"] = self.recover_value_table.properties()
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return StaminaModelRef(
            namespace_name=namespace_name,
            stamina_name=self.name,
        )


class MaxStaminaTable:
    name: str
    metadata: str
    experience_model_id: str
    values: List[int]

    def __init__(
            self,
            name: str,
            experience_model_id: str,
            values: List[int],
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.experience_model_id = experience_model_id
        self.values = values

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.experience_model_id:
            properties["ExperienceModelId"] = self.experience_model_id
        if self.values:
            properties["Values"] = [
                element
                for element in self.values
            ]
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return MaxStaminaTableRef(
            namespace_name=namespace_name,
            max_stamina_table_name=self.name,
        )


class RecoverIntervalTable:
    name: str
    metadata: str
    experience_model_id: str
    values: List[int]

    def __init__(
            self,
            name: str,
            experience_model_id: str,
            values: List[int],
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.experience_model_id = experience_model_id
        self.values = values

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.experience_model_id:
            properties["ExperienceModelId"] = self.experience_model_id
        if self.values:
            properties["Values"] = [
                element
                for element in self.values
            ]
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return RecoverIntervalTableRef(
            namespace_name=namespace_name,
            recover_interval_table_name=self.name,
        )


class RecoverValueTable:
    name: str
    metadata: str
    experience_model_id: str
    values: List[int]

    def __init__(
            self,
            name: str,
            experience_model_id: str,
            values: List[int],
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.experience_model_id = experience_model_id
        self.values = values

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.experience_model_id:
            properties["ExperienceModelId"] = self.experience_model_id
        if self.values:
            properties["Values"] = [
                element
                for element in self.values
            ]
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return RecoverValueTableRef(
            namespace_name=namespace_name,
            recover_value_table_name=self.name,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-02-14'
    namespace_name: str
    stamina_models: List[StaminaModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            stamina_models: List[StaminaModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.stamina_models = stamina_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Stamina::CurrentStaminaMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "stamina_models": [
                    element.properties()
                    for element in self.stamina_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    overflow_trigger_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            overflow_trigger_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.overflow_trigger_script = overflow_trigger_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Stamina::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.overflow_trigger_script:
            properties["OverflowTriggerScript"] = self.overflow_trigger_script.properties()
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
            stamina_models: List[StaminaModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            stamina_models=stamina_models,
        ).add_depends_on(
            self,
        )
        return self


class StaminaModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    recover_interval_minutes: int
    recover_value: int
    initial_capacity: int
    is_overflow: bool
    max_capacity: int
    max_stamina_table_name: str
    recover_interval_table_name: str
    recover_value_table_name: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            recover_interval_minutes: int,
            recover_value: int,
            initial_capacity: int,
            is_overflow: bool,
            max_capacity: int,
            description: str = None,
            metadata: str = None,
            max_stamina_table_name: str = None,
            recover_interval_table_name: str = None,
            recover_value_table_name: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.recover_interval_minutes = recover_interval_minutes
        self.recover_value = recover_value
        self.initial_capacity = initial_capacity
        self.is_overflow = is_overflow
        self.max_capacity = max_capacity
        self.max_stamina_table_name = max_stamina_table_name
        self.recover_interval_table_name = recover_interval_table_name
        self.recover_value_table_name = recover_value_table_name

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Stamina::StaminaModelMaster"

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
        if self.recover_interval_minutes:
            properties["RecoverIntervalMinutes"] = self.recover_interval_minutes
        if self.recover_value:
            properties["RecoverValue"] = self.recover_value
        if self.initial_capacity:
            properties["InitialCapacity"] = self.initial_capacity
        if self.is_overflow:
            properties["IsOverflow"] = self.is_overflow
        if self.max_capacity:
            properties["MaxCapacity"] = self.max_capacity
        if self.max_stamina_table_name:
            properties["MaxStaminaTableName"] = self.max_stamina_table_name
        if self.recover_interval_table_name:
            properties["RecoverIntervalTableName"] = self.recover_interval_table_name
        if self.recover_value_table_name:
            properties["RecoverValueTableName"] = self.recover_value_table_name
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return StaminaModelMasterRef(
            namespace_name=namespace_name,
            stamina_name=self.name,
        )

    def get_attr_stamina_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.StaminaModelId"
        )


class MaxStaminaTableMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    experience_model_id: str
    values: List[int]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            experience_model_id: str,
            values: List[int],
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.experience_model_id = experience_model_id
        self.values = values

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Stamina::MaxStaminaTableMaster"

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
        if self.experience_model_id:
            properties["ExperienceModelId"] = self.experience_model_id
        if self.values:
            properties["Values"] = [
                element
                for element in self.values
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return MaxStaminaTableMasterRef(
            namespace_name=namespace_name,
            max_stamina_table_name=self.name,
        )

    def get_attr_max_stamina_table_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.MaxStaminaTableId"
        )


class RecoverIntervalTableMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    experience_model_id: str
    values: List[int]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            experience_model_id: str,
            values: List[int],
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.experience_model_id = experience_model_id
        self.values = values

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Stamina::RecoverIntervalTableMaster"

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
        if self.experience_model_id:
            properties["ExperienceModelId"] = self.experience_model_id
        if self.values:
            properties["Values"] = [
                element
                for element in self.values
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return RecoverIntervalTableMasterRef(
            namespace_name=namespace_name,
            recover_interval_table_name=self.name,
        )

    def get_attr_recover_interval_table_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.RecoverIntervalTableId"
        )


class RecoverValueTableMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    experience_model_id: str
    values: List[int]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            experience_model_id: str,
            values: List[int],
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.experience_model_id = experience_model_id
        self.values = values

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Stamina::RecoverValueTableMaster"

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
        if self.experience_model_id:
            properties["ExperienceModelId"] = self.experience_model_id
        if self.values:
            properties["Values"] = [
                element
                for element in self.values
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return RecoverValueTableMasterRef(
            namespace_name=namespace_name,
            recover_value_table_name=self.name,
        )

    def get_attr_recover_value_table_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.RecoverValueTableId"
        )
