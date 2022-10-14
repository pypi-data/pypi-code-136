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

    def current_ranking_master(
            self,
    ) -> CurrentRankingMasterRef:
        return CurrentRankingMasterRef(
            namespace_name=self.namespace_name,
        )

    def category_model(
            self,
            category_name: str,
    ) -> CategoryModelRef:
        return CategoryModelRef(
            namespace_name=self.namespace_name,
            category_name=category_name,
        )

    def category_model_master(
            self,
            category_name: str,
    ) -> CategoryModelMasterRef:
        return CategoryModelMasterRef(
            namespace_name=self.namespace_name,
            category_name=category_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'ranking',
                self.namespace_name,
            ],
        ).str()


class CategoryModelRef:
    namespace_name: str
    category_name: str

    def __init__(
            self,
            namespace_name: str,
            category_name: str,
    ):
        self.namespace_name = namespace_name
        self.category_name = category_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'ranking',
                self.namespace_name,
                'categoryModel',
                self.category_name,
            ],
        ).str()


class CategoryModelMasterRef:
    namespace_name: str
    category_name: str

    def __init__(
            self,
            namespace_name: str,
            category_name: str,
    ):
        self.namespace_name = namespace_name
        self.category_name = category_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'ranking',
                self.namespace_name,
                'categoryModelMaster',
                self.category_name,
            ],
        ).str()


class CurrentRankingMasterRef:
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
                'ranking',
                self.namespace_name,
            ],
        ).str()
