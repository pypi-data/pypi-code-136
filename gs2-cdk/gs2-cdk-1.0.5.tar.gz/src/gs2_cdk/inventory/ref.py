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
from .model import *
from .stamp_sheet import *

from typing import List


class NamespaceRef:
    namespace_name: str

    def __init__(
            self,
            namespace_name: str,
    ):
        self.namespace_name = namespace_name

    def current_item_model_master(
            self,
    ) -> CurrentItemModelMasterRef:
        return CurrentItemModelMasterRef(
            namespace_name=self.namespace_name,
        )

    def inventory_model(
            self,
            inventory_name: str,
    ) -> InventoryModelRef:
        return InventoryModelRef(
            namespace_name=self.namespace_name,
            inventory_name=inventory_name,
        )

    def inventory_model_master(
            self,
            inventory_name: str,
    ) -> InventoryModelMasterRef:
        return InventoryModelMasterRef(
            namespace_name=self.namespace_name,
            inventory_name=inventory_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'inventory',
                self.namespace_name,
            ],
        ).str()


class InventoryModelMasterRef:
    namespace_name: str
    inventory_name: str

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name

    def item_model_master(
            self,
            item_name: str,
    ) -> ItemModelMasterRef:
        return ItemModelMasterRef(
            namespace_name=self.namespace_name,
            inventory_name=self.inventory_name,
            item_name=item_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'inventory',
                self.namespace_name,
                'model',
                self.inventory_name,
            ],
        ).str()


class InventoryModelRef:
    namespace_name: str
    inventory_name: str

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name

    def item_model(
            self,
            item_name: str,
    ) -> ItemModelRef:
        return ItemModelRef(
            namespace_name=self.namespace_name,
            inventory_name=self.inventory_name,
            item_name=item_name,
        )

    def add_capacity(
            self,
            add_capacity_value: int,
            user_id: str = '#{userId}',
    ) -> AddCapacityByUserId:
        return AddCapacityByUserId(
            namespace_name=self.namespace_name,
            inventory_name=self.inventory_name,
            user_id=user_id,
            add_capacity_value=add_capacity_value,
        )

    def set_capacity(
            self,
            new_capacity_value: int,
            user_id: str = '#{userId}',
    ) -> SetCapacityByUserId:
        return SetCapacityByUserId(
            namespace_name=self.namespace_name,
            inventory_name=self.inventory_name,
            user_id=user_id,
            new_capacity_value=new_capacity_value,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'inventory',
                self.namespace_name,
                'model',
                self.inventory_name,
            ],
        ).str()


class ItemModelMasterRef:
    namespace_name: str
    inventory_name: str
    item_name: str

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
            item_name: str,
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.item_name = item_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'inventory',
                self.namespace_name,
                'model',
                self.inventory_name,
                'item',
                self.item_name,
            ],
        ).str()


class ItemModelRef:
    namespace_name: str
    inventory_name: str
    item_name: str

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
            item_name: str,
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.item_name = item_name

    def acquire_item_set(
            self,
            acquire_count: int,
            expires_at: int,
            create_new_item_set: bool,
            item_set_name: str = None,
            user_id: str = '#{userId}',
    ) -> AcquireItemSetByUserId:
        return AcquireItemSetByUserId(
            namespace_name=self.namespace_name,
            inventory_name=self.inventory_name,
            item_name=self.item_name,
            user_id=user_id,
            acquire_count=acquire_count,
            expires_at=expires_at,
            create_new_item_set=create_new_item_set,
            item_set_name=item_set_name,
        )

    def add_reference_of(
            self,
            item_set_name: str,
            reference_of: str,
            user_id: str = '#{userId}',
    ) -> AddReferenceOfByUserId:
        return AddReferenceOfByUserId(
            namespace_name=self.namespace_name,
            inventory_name=self.inventory_name,
            user_id=user_id,
            item_name=self.item_name,
            item_set_name=item_set_name,
            reference_of=reference_of,
        )

    def consume_item_set(
            self,
            consume_count: int,
            item_set_name: str = None,
            user_id: str = '#{userId}',
    ) -> ConsumeItemSetByUserId:
        return ConsumeItemSetByUserId(
            namespace_name=self.namespace_name,
            inventory_name=self.inventory_name,
            user_id=user_id,
            item_name=self.item_name,
            consume_count=consume_count,
            item_set_name=item_set_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'inventory',
                self.namespace_name,
                'model',
                self.inventory_name,
                'item',
                self.item_name,
            ],
        ).str()


class CurrentItemModelMasterRef:
    namespace_name: str

    def __init__(
            self,
            namespace_name: str,
    ):
        self.namespace_name = namespace_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'inventory',
                self.namespace_name,
            ],
        ).str()


class ReferenceOfRef:
    namespace_name: str
    inventory_name: str
    item_name: str
    item_set_name: str
    reference_of: str

    def __init__(
            self,
            namespace_name: str,
            inventory_name: str,
            item_name: str,
            item_set_name: str,
            reference_of: str,
    ):
        self.namespace_name = namespace_name
        self.inventory_name = inventory_name
        self.item_name = item_name
        self.item_set_name = item_set_name
        self.reference_of = reference_of

    def delete_reference_of(
            self,
            user_id: str = '#{userId}',
    ) -> DeleteReferenceOfByUserId:
        return DeleteReferenceOfByUserId(
            namespace_name=self.namespace_name,
            inventory_name=self.inventory_name,
            user_id=user_id,
            item_name=self.item_name,
            item_set_name=self.item_set_name,
            reference_of=self.reference_of,
        )

    def verify_reference_of(
            self,
            verify_type: str,
            user_id: str = '#{userId}',
    ) -> VerifyReferenceOfByUserId:
        return VerifyReferenceOfByUserId(
            namespace_name=self.namespace_name,
            inventory_name=self.inventory_name,
            user_id=user_id,
            item_name=self.item_name,
            item_set_name=self.item_set_name,
            reference_of=self.reference_of,
            verify_type=verify_type,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'inventory',
                self.namespace_name,
                'user',
                self.user_id,
                'inventory',
                self.inventory_name,
                'item',
                self.item_name,
                'itemSet',
                self.item_set_name,
                'referenceOf',
            ],
        ).str()
