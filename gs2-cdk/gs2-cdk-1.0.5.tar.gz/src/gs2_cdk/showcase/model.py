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


class SalesItem:
    name: str
    metadata: str
    consume_actions: List[ConsumeAction]
    acquire_actions: List[AcquireAction]

    def __init__(
            self,
            name: str = None,
            metadata: str = None,
            consume_actions: List[ConsumeAction] = None,
            acquire_actions: List[AcquireAction] = None,
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
            name: str = None,
            metadata: str = None,
            sales_items: List[SalesItem] = None,
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


class DisplayItemMaster:

    class Type(Enum):
        SALES_ITEM = "salesItem"
        SALES_ITEM_GROUP = "salesItemGroup"
    display_item_id: str
    type: Type
    sales_item_name: str
    sales_item_group_name: str
    sales_period_event_id: str

    def __init__(
            self,
            display_item_id: str = None,
            type: Type = None,
            sales_item_name: str = None,
            sales_item_group_name: str = None,
            sales_period_event_id: str = None,
    ):
        self.display_item_id = display_item_id
        self.type = type
        self.sales_item_name = sales_item_name
        self.sales_item_group_name = sales_item_group_name
        self.sales_period_event_id = sales_period_event_id

    @staticmethod
    def sales_item(
        display_item_id: str,
        sales_item_name: str,
        sales_period_event_id: str = None,
    ) -> DisplayItemMaster:
        return DisplayItemMaster(
            type=DisplayItemMaster.Type.SALES_ITEM,
            display_item_id=display_item_id,
            sales_item_name=sales_item_name,
            sales_period_event_id=sales_period_event_id,
        )

    @staticmethod
    def sales_item_group(
        display_item_id: str,
        sales_item_group_name: str,
        sales_period_event_id: str = None,
    ) -> DisplayItemMaster:
        return DisplayItemMaster(
            type=DisplayItemMaster.Type.SALES_ITEM_GROUP,
            display_item_id=display_item_id,
            sales_item_group_name=sales_item_group_name,
            sales_period_event_id=sales_period_event_id,
        )

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.display_item_id:
            properties["DisplayItemId"] = self.display_item_id
        if self.type:
            properties["Type"] = self.type
        if self.sales_item_name:
            properties["SalesItemName"] = self.sales_item_name
        if self.sales_item_group_name:
            properties["SalesItemGroupName"] = self.sales_item_group_name
        if self.sales_period_event_id:
            properties["SalesPeriodEventId"] = self.sales_period_event_id
        return properties
