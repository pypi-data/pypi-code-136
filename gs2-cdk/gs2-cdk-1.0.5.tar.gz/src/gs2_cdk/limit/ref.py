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

    def current_limit_master(
            self,
    ) -> CurrentLimitMasterRef:
        return CurrentLimitMasterRef(
            namespace_name=self.namespace_name,
        )

    def limit_model(
            self,
            limit_name: str,
    ) -> LimitModelRef:
        return LimitModelRef(
            namespace_name=self.namespace_name,
            limit_name=limit_name,
        )

    def limit_model_master(
            self,
            limit_name: str,
    ) -> LimitModelMasterRef:
        return LimitModelMasterRef(
            namespace_name=self.namespace_name,
            limit_name=limit_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'limit',
                self.namespace_name,
            ],
        ).str()


class LimitModelMasterRef:
    namespace_name: str
    limit_name: str

    def __init__(
            self,
            namespace_name: str,
            limit_name: str,
    ):
        self.namespace_name = namespace_name
        self.limit_name = limit_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'limit',
                self.namespace_name,
                'limit',
                self.limit_name,
            ],
        ).str()


class CurrentLimitMasterRef:
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
                'limit',
                self.namespace_name,
            ],
        ).str()


class LimitModelRef:
    namespace_name: str
    limit_name: str

    def __init__(
            self,
            namespace_name: str,
            limit_name: str,
    ):
        self.namespace_name = namespace_name
        self.limit_name = limit_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'limit',
                self.namespace_name,
                'limit',
                self.limit_name,
            ],
        ).str()
