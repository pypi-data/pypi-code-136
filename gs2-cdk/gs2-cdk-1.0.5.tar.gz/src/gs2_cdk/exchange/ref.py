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

    def rate_model_master(
            self,
            rate_name: str,
    ) -> RateModelMasterRef:
        return RateModelMasterRef(
            namespace_name=self.namespace_name,
            rate_name=rate_name,
        )

    def current_rate_master(
            self,
    ) -> CurrentRateMasterRef:
        return CurrentRateMasterRef(
            namespace_name=self.namespace_name,
        )

    def rate_model(
            self,
            rate_name: str,
    ) -> RateModelRef:
        return RateModelRef(
            namespace_name=self.namespace_name,
            rate_name=rate_name,
        )

    def create_await(
            self,
            rate_name: str,
            count: int,
            user_id: str = '#{userId}',
    ) -> CreateAwaitByUserId:
        return CreateAwaitByUserId(
            namespace_name=self.namespace_name,
            user_id=user_id,
            rate_name=rate_name,
            count=count,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'exchange',
                self.namespace_name,
            ],
        ).str()


class RateModelRef:
    namespace_name: str
    rate_name: str

    def __init__(
            self,
            namespace_name: str,
            rate_name: str,
    ):
        self.namespace_name = namespace_name
        self.rate_name = rate_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'exchange',
                self.namespace_name,
                'model',
                self.rate_name,
            ],
        ).str()


class RateModelMasterRef:
    namespace_name: str
    rate_name: str

    def __init__(
            self,
            namespace_name: str,
            rate_name: str,
    ):
        self.namespace_name = namespace_name
        self.rate_name = rate_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'exchange',
                self.namespace_name,
                'model',
                self.rate_name,
            ],
        ).str()


class CurrentRateMasterRef:
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
                'exchange',
                self.namespace_name,
            ],
        ).str()
