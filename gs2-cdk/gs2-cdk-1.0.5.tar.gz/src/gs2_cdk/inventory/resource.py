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


class InventoryModel:
    name: str
    metadata: str
    initial_capacity: int
    max_capacity: int
    protect_referenced_item: bool
    item_models: List[ItemModel]

    def __init__(
            self,
            name: str,
            initial_capacity: int,
            max_capacity: int,
            metadata: str = None,
            protect_referenced_item: bool = None,
            item_models: List[ItemModel] = None,
    ):
        self.name = name
        self.metadata = metadata
        self.initial_capacity = initial_capacity
        self.max_capacity = max_capacity
        self.protect_referenced_item = protect_referenced_item
        self.item_models = item_models

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.initial_capacity:
            properties["InitialCapacity"] = self.initial_capacity
        if self.max_capacity:
            properties["MaxCapacity"] = self.max_capacity
        if self.protect_referenced_item:
            properties["ProtectReferencedItem"] = self.protect_referenced_item
        if self.item_models:
            properties["ItemModels"] = [
                element.properties()
                for element in self.item_models
            ]
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return InventoryModelRef(
            namespace_name=namespace_name,
            inventory_name=self.name,
        )


class ItemModel:
    name: str
    metadata: str
    stacking_limit: int
    allow_multiple_stacks: bool
    sort_value: int

    def __init__(
            self,
            name: str,
            stacking_limit: int,
            allow_multiple_stacks: bool,
            sort_value: int,
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.stacking_limit = stacking_limit
        self.allow_multiple_stacks = allow_multiple_stacks
        self.sort_value = sort_value

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.stacking_limit:
            properties["StackingLimit"] = self.stacking_limit
        if self.allow_multiple_stacks:
            properties["AllowMultipleStacks"] = self.allow_multiple_stacks
        if self.sort_value:
            properties["SortValue"] = self.sort_value
        return properties

    def ref(
            self,
            namespace_name: str,
            inventory_name: str,
    ):
        return ItemModelRef(
            namespace_name=namespace_name,
            inventory_name=inventory_name,
            item_name=self.name,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-02-05'
    namespace_name: str
    inventory_models: List[InventoryModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            inventory_models: List[InventoryModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.inventory_models = inventory_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Inventory::CurrentItemModelMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "inventory_models": [
                    element.properties()
                    for element in self.inventory_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    acquire_script: ScriptSetting
    overflow_script: ScriptSetting
    consume_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            acquire_script: ScriptSetting = None,
            overflow_script: ScriptSetting = None,
            consume_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.acquire_script = acquire_script
        self.overflow_script = overflow_script
        self.consume_script = consume_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Inventory::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.acquire_script:
            properties["AcquireScript"] = self.acquire_script.properties()
        if self.overflow_script:
            properties["OverflowScript"] = self.overflow_script.properties()
        if self.consume_script:
            properties["ConsumeScript"] = self.consume_script.properties()
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
            inventory_models: List[InventoryModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            inventory_models=inventory_models,
        ).add_depends_on(
            self,
        )
        return self


class InventoryModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    initial_capacity: int
    max_capacity: int
    protect_referenced_item: bool

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            initial_capacity: int,
            max_capacity: int,
            protect_referenced_item: bool,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.initial_capacity = initial_capacity
        self.max_capacity = max_capacity
        self.protect_referenced_item = protect_referenced_item

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Inventory::InventoryModelMaster"

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
        if self.initial_capacity:
            properties["InitialCapacity"] = self.initial_capacity
        if self.max_capacity:
            properties["MaxCapacity"] = self.max_capacity
        if self.protect_referenced_item:
            properties["ProtectReferencedItem"] = self.protect_referenced_item
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return InventoryModelMasterRef(
            namespace_name=namespace_name,
            inventory_name=self.name,
        )

    def get_attr_inventory_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.InventoryModelId"
        )


class ItemModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    inventory_name: str
    name: str
    description: str
    metadata: str
    stacking_limit: int
    allow_multiple_stacks: bool
    sort_value: int

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            inventory_name: str,
            name: str,
            stacking_limit: int,
            allow_multiple_stacks: bool,
            sort_value: int,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.stacking_limit = stacking_limit
        self.allow_multiple_stacks = allow_multiple_stacks
        self.sort_value = sort_value

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Inventory::ItemModelMaster"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.inventory_name:
            properties["InventoryName"] = self.inventory_name
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.stacking_limit:
            properties["StackingLimit"] = self.stacking_limit
        if self.allow_multiple_stacks:
            properties["AllowMultipleStacks"] = self.allow_multiple_stacks
        if self.sort_value:
            properties["SortValue"] = self.sort_value
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
            inventory_name: str,
    ):
        return ItemModelMasterRef(
            namespace_name=namespace_name,
            inventory_name=inventory_name,
            item_name=self.name,
        )

    def get_attr_item_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.ItemModelId"
        )
