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
import json

from typing import List

from .model import *
from gs2_cdk import AcquireAction, ConsumeAction


class AddCapacityByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
            add_capacity_value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.user_id = user_id
        self.add_capacity_value = add_capacity_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if inventory_name:
            properties["inventoryName"] = inventory_name
        if user_id:
            properties["userId"] = user_id
        if add_capacity_value:
            properties["addCapacityValue"] = add_capacity_value

        super().__init__(
            action="Gs2Inventory:AddCapacityByUserId",
            request=properties,
        )


class SetCapacityByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
            new_capacity_value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.user_id = user_id
        self.new_capacity_value = new_capacity_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if inventory_name:
            properties["inventoryName"] = inventory_name
        if user_id:
            properties["userId"] = user_id
        if new_capacity_value:
            properties["newCapacityValue"] = new_capacity_value

        super().__init__(
            action="Gs2Inventory:SetCapacityByUserId",
            request=properties,
        )


class ConsumeItemSetByUserId(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
            item_name: str,
            consume_count: int,
            item_set_name: str = None,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.user_id = user_id
        self.item_name = item_name
        self.consume_count = consume_count
        self.item_set_name = item_set_name

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if inventory_name:
            properties["inventoryName"] = inventory_name
        if user_id:
            properties["userId"] = user_id
        if item_name:
            properties["itemName"] = item_name
        if consume_count:
            properties["consumeCount"] = consume_count
        if item_set_name:
            properties["itemSetName"] = item_set_name

        super().__init__(
            action="Gs2Inventory:ConsumeItemSetByUserId",
            request=properties,
        )


class AcquireItemSetByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
            item_name: str,
            acquire_count: int,
            expires_at: int,
            create_new_item_set: bool,
            item_set_name: str = None,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.item_name = item_name
        self.user_id = user_id
        self.acquire_count = acquire_count
        self.expires_at = expires_at
        self.create_new_item_set = create_new_item_set
        self.item_set_name = item_set_name

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if inventory_name:
            properties["inventoryName"] = inventory_name
        if item_name:
            properties["itemName"] = item_name
        if user_id:
            properties["userId"] = user_id
        if acquire_count:
            properties["acquireCount"] = acquire_count
        if expires_at:
            properties["expiresAt"] = expires_at
        if create_new_item_set:
            properties["createNewItemSet"] = create_new_item_set
        if item_set_name:
            properties["itemSetName"] = item_set_name

        super().__init__(
            action="Gs2Inventory:AcquireItemSetByUserId",
            request=properties,
        )


class VerifyReferenceOfByUserId(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
            item_name: str,
            item_set_name: str,
            reference_of: str,
            verify_type: str,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.user_id = user_id
        self.item_name = item_name
        self.item_set_name = item_set_name
        self.reference_of = reference_of
        self.verify_type = verify_type

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if inventory_name:
            properties["inventoryName"] = inventory_name
        if user_id:
            properties["userId"] = user_id
        if item_name:
            properties["itemName"] = item_name
        if item_set_name:
            properties["itemSetName"] = item_set_name
        if reference_of:
            properties["referenceOf"] = reference_of
        if verify_type:
            properties["verifyType"] = verify_type

        super().__init__(
            action="Gs2Inventory:VerifyReferenceOfByUserId",
            request=properties,
        )


class AddReferenceOfByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
            item_name: str,
            item_set_name: str,
            reference_of: str,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.user_id = user_id
        self.item_name = item_name
        self.item_set_name = item_set_name
        self.reference_of = reference_of

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if inventory_name:
            properties["inventoryName"] = inventory_name
        if user_id:
            properties["userId"] = user_id
        if item_name:
            properties["itemName"] = item_name
        if item_set_name:
            properties["itemSetName"] = item_set_name
        if reference_of:
            properties["referenceOf"] = reference_of

        super().__init__(
            action="Gs2Inventory:AddReferenceOfByUserId",
            request=properties,
        )


class DeleteReferenceOfByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
            item_name: str,
            item_set_name: str,
            reference_of: str,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.user_id = user_id
        self.item_name = item_name
        self.item_set_name = item_set_name
        self.reference_of = reference_of

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if inventory_name:
            properties["inventoryName"] = inventory_name
        if user_id:
            properties["userId"] = user_id
        if item_name:
            properties["itemName"] = item_name
        if item_set_name:
            properties["itemSetName"] = item_set_name
        if reference_of:
            properties["referenceOf"] = reference_of

        super().__init__(
            action="Gs2Inventory:DeleteReferenceOfByUserId",
            request=properties,
        )
