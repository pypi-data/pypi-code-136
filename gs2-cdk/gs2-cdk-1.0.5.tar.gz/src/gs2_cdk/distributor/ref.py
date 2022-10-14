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

    def current_distributor_master(
            self,
    ) -> CurrentDistributorMasterRef:
        return CurrentDistributorMasterRef(
            namespace_name=self.namespace_name,
        )

    def distributor_model(
            self,
            distributor_name: str,
    ) -> DistributorModelRef:
        return DistributorModelRef(
            namespace_name=self.namespace_name,
            distributor_name=distributor_name,
        )

    def distributor_model_master(
            self,
            distributor_name: str,
    ) -> DistributorModelMasterRef:
        return DistributorModelMasterRef(
            namespace_name=self.namespace_name,
            distributor_name=distributor_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'distributor',
                self.namespace_name,
            ],
        ).str()


class DistributorModelMasterRef:
    namespace_name: str
    distributor_name: str

    def __init__(
            self,
            namespace_name: str,
            distributor_name: str,
    ):
        self.namespace_name = namespace_name
        self.distributor_name = distributor_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'distributor',
                self.namespace_name,
                'model',
                self.distributor_name,
            ],
        ).str()


class DistributorModelRef:
    namespace_name: str
    distributor_name: str

    def __init__(
            self,
            namespace_name: str,
            distributor_name: str,
    ):
        self.namespace_name = namespace_name
        self.distributor_name = distributor_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'distributor',
                self.namespace_name,
                'model',
                self.distributor_name,
            ],
        ).str()


class CurrentDistributorMasterRef:
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
                'distributor',
                self.namespace_name,
            ],
        ).str()
