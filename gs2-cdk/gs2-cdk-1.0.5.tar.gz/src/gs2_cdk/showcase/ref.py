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

    def current_showcase_master(
            self,
    ) -> CurrentShowcaseMasterRef:
        return CurrentShowcaseMasterRef(
            namespace_name=self.namespace_name,
        )

    def display_item(
            self,
    ) -> DisplayItemRef:
        return DisplayItemRef(
            namespace_name=self.namespace_name,
        )

    def sales_item_master(
            self,
            sales_item_name: str,
    ) -> SalesItemMasterRef:
        return SalesItemMasterRef(
            namespace_name=self.namespace_name,
            sales_item_name=sales_item_name,
        )

    def sales_item_group_master(
            self,
            sales_item_group_name: str,
    ) -> SalesItemGroupMasterRef:
        return SalesItemGroupMasterRef(
            namespace_name=self.namespace_name,
            sales_item_group_name=sales_item_group_name,
        )

    def showcase_master(
            self,
            showcase_name: str,
    ) -> ShowcaseMasterRef:
        return ShowcaseMasterRef(
            namespace_name=self.namespace_name,
            showcase_name=showcase_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'showcase',
                self.namespace_name,
            ],
        ).str()


class SalesItemMasterRef:
    namespace_name: str
    sales_item_name: str

    def __init__(
            self,
            namespace_name: str,
            sales_item_name: str,
    ):
        self.namespace_name = namespace_name
        self.sales_item_name = sales_item_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'showcase',
                self.namespace_name,
                'salesItem',
                self.sales_item_name,
            ],
        ).str()


class SalesItemGroupMasterRef:
    namespace_name: str
    sales_item_group_name: str

    def __init__(
            self,
            namespace_name: str,
            sales_item_group_name: str,
    ):
        self.namespace_name = namespace_name
        self.sales_item_group_name = sales_item_group_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'showcase',
                self.namespace_name,
                'salesItemGroup',
                self.sales_item_group_name,
            ],
        ).str()


class ShowcaseMasterRef:
    namespace_name: str
    showcase_name: str

    def __init__(
            self,
            namespace_name: str,
            showcase_name: str,
    ):
        self.namespace_name = namespace_name
        self.showcase_name = showcase_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'showcase',
                self.namespace_name,
                'showcase',
                self.showcase_name,
            ],
        ).str()


class CurrentShowcaseMasterRef:
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
                'showcase',
                self.namespace_name,
            ],
        ).str()


class ShowcaseRef:
    namespace_name: str
    showcase_name: str

    def __init__(
            self,
            namespace_name: str,
            showcase_name: str,
    ):
        self.namespace_name = namespace_name
        self.showcase_name = showcase_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'showcase',
                self.namespace_name,
                'showcase',
                self.showcase_name,
            ],
        ).str()


class DisplayItemRef:
    namespace_name: str

    def __init__(
            self,
            namespace_name: str,
    ):
        self.namespace_name = namespace_name
