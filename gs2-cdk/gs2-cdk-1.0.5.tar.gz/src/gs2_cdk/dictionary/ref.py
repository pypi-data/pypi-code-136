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

    def current_entry_master(
            self,
    ) -> CurrentEntryMasterRef:
        return CurrentEntryMasterRef(
            namespace_name=self.namespace_name,
        )

    def entry_model(
            self,
            entry_name: str,
    ) -> EntryModelRef:
        return EntryModelRef(
            namespace_name=self.namespace_name,
            entry_name=entry_name,
        )

    def entry_model_master(
            self,
            entry_name: str,
    ) -> EntryModelMasterRef:
        return EntryModelMasterRef(
            namespace_name=self.namespace_name,
            entry_name=entry_name,
        )

    def add_entries(
            self,
            entry_model_names: List[str] = None,
            user_id: str = '#{userId}',
    ) -> AddEntriesByUserId:
        return AddEntriesByUserId(
            namespace_name=self.namespace_name,
            user_id=user_id,
            entry_model_names=entry_model_names,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'dictionary',
                self.namespace_name,
            ],
        ).str()


class EntryModelRef:
    namespace_name: str
    entry_name: str

    def __init__(
            self,
            namespace_name: str,
            entry_name: str,
    ):
        self.namespace_name = namespace_name
        self.entry_name = entry_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'dictionary',
                self.namespace_name,
                'model',
                self.entry_name,
            ],
        ).str()


class EntryModelMasterRef:
    namespace_name: str
    entry_name: str

    def __init__(
            self,
            namespace_name: str,
            entry_name: str,
    ):
        self.namespace_name = namespace_name
        self.entry_name = entry_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'dictionary',
                self.namespace_name,
                'model',
                self.entry_name,
            ],
        ).str()


class CurrentEntryMasterRef:
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
                'dictionary',
                self.namespace_name,
            ],
        ).str()
