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


class SalesItem:
    name: str
    metadata: str
    consume_actions: List[ConsumeAction]
    acquire_actions: List[AcquireAction]

    def __init__(
            self,
            name: str,
            consume_actions: List[ConsumeAction],
            acquire_actions: List[AcquireAction],
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.consume_actions = consume_actions
        self.acquire_actions = acquire_actions

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.consume_actions:
            properties["ConsumeActions"] = [
                element.properties()
                for element in self.consume_actions
            ]
        if self.acquire_actions:
            properties["AcquireActions"] = [
                element.properties()
                for element in self.acquire_actions
            ]
        return properties


class SalesItemGroup:
    name: str
    metadata: str
    sales_items: List[SalesItem]

    def __init__(
            self,
            name: str,
            sales_items: List[SalesItem],
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.sales_items = sales_items

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.sales_items:
            properties["SalesItems"] = [
                element.properties()
                for element in self.sales_items
            ]
        return properties


class Showcase:
    name: str
    metadata: str
    sales_period_event_id: str
    display_items: List[DisplayItem]

    def __init__(
            self,
            name: str,
            display_items: List[DisplayItem],
            metadata: str = None,
            sales_period_event_id: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.sales_period_event_id = sales_period_event_id
        self.display_items = display_items

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.sales_period_event_id:
            properties["SalesPeriodEventId"] = self.sales_period_event_id
        if self.display_items:
            properties["DisplayItems"] = [
                element.properties()
                for element in self.display_items
            ]
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return ShowcaseRef(
            namespace_name=namespace_name,
            showcase_name=self.name,
        )


class DisplayItem:

    class Type(Enum):
        SALES_ITEM = "salesItem"
        SALES_ITEM_GROUP = "salesItemGroup"
    display_item_id: str
    type: str
    sales_item: SalesItem
    sales_item_group: SalesItemGroup
    sales_period_event_id: str

    def __init__(
            self,
            display_item_id: str,
            type: Type,
            sales_item: SalesItem = None,
            sales_item_group: SalesItemGroup = None,
            sales_period_event_id: str = None,
    ):
        self.display_item_id = display_item_id
        self.type = type
        self.sales_item = sales_item
        self.sales_item_group = sales_item_group
        self.sales_period_event_id = sales_period_event_id

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.display_item_id:
            properties["DisplayItemId"] = self.display_item_id
        if self.type:
            properties["Type"] = self.type
        if self.sales_item:
            properties["SalesItem"] = self.sales_item.properties()
        if self.sales_item_group:
            properties["SalesItemGroup"] = self.sales_item_group.properties()
        if self.sales_period_event_id:
            properties["SalesPeriodEventId"] = self.sales_period_event_id
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return DisplayItemRef(
            namespace_name=namespace_name,
        )

    @staticmethod
    def sales_item(
        sales_item: SalesItem,
        display_item_id: str = None,
        sales_period_event_id: str = None,
    ) -> DisplayItem:
        return DisplayItem(
            type=DisplayItem.Type.SALES_ITEM,
            display_item_id=display_item_id,
            sales_item=sales_item,
            sales_period_event_id=sales_period_event_id,
        )

    @staticmethod
    def sales_item_group(
        sales_item_group: SalesItemGroup,
        display_item_id: str = None,
        sales_period_event_id: str = None,
    ) -> DisplayItem:
        return DisplayItem(
            type=DisplayItem.Type.SALES_ITEM_GROUP,
            display_item_id=display_item_id,
            sales_item_group=sales_item_group,
            sales_period_event_id=sales_period_event_id,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-04-04'
    namespace_name: str
    showcases: List[Showcase]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            showcases: List[Showcase],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.showcases = showcases

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Showcase::CurrentShowcaseMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "showcases": [
                    element.properties()
                    for element in self.showcases
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
    buy_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            transaction_setting: TransactionSetting,
            description: str = None,
            buy_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.transaction_setting = transaction_setting
        self.buy_script = buy_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Showcase::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.transaction_setting:
            properties["TransactionSetting"] = self.transaction_setting.properties()
        if self.buy_script:
            properties["BuyScript"] = self.buy_script.properties()
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
            showcases: List[Showcase],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            showcases=showcases,
        ).add_depends_on(
            self,
        )
        return self


class SalesItemMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    consume_actions: List[ConsumeAction]
    acquire_actions: List[AcquireAction]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            consume_actions: List[ConsumeAction],
            acquire_actions: List[AcquireAction],
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.consume_actions = consume_actions
        self.acquire_actions = acquire_actions

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Showcase::SalesItemMaster"

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
        if self.consume_actions:
            properties["ConsumeActions"] = [
                element.properties()
                for element in self.consume_actions
            ]
        if self.acquire_actions:
            properties["AcquireActions"] = [
                element.properties()
                for element in self.acquire_actions
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return SalesItemMasterRef(
            namespace_name=namespace_name,
            sales_item_name=self.name,
        )

    def get_attr_sales_item_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.SalesItemId"
        )


class SalesItemGroupMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    sales_item_names: List[str]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            sales_item_names: List[str],
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.sales_item_names = sales_item_names

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Showcase::SalesItemGroupMaster"

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
        if self.sales_item_names:
            properties["SalesItemNames"] = [
                element
                for element in self.sales_item_names
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return SalesItemGroupMasterRef(
            namespace_name=namespace_name,
            sales_item_group_name=self.name,
        )

    def get_attr_sales_item_group_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.SalesItemGroupId"
        )


class ShowcaseMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    display_items: List[DisplayItemMaster]
    sales_period_event_id: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            display_items: List[DisplayItemMaster],
            description: str = None,
            metadata: str = None,
            sales_period_event_id: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.display_items = display_items
        self.sales_period_event_id = sales_period_event_id

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Showcase::ShowcaseMaster"

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
        if self.display_items:
            properties["DisplayItems"] = [
                element.properties()
                for element in self.display_items
            ]
        if self.sales_period_event_id:
            properties["SalesPeriodEventId"] = self.sales_period_event_id
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return ShowcaseMasterRef(
            namespace_name=namespace_name,
            showcase_name=self.name,
        )

    def get_attr_showcase_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.ShowcaseId"
        )
