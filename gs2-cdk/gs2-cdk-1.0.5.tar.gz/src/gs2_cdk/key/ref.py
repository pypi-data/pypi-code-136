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

    def key(
            self,
            key_name: str,
    ) -> KeyRef:
        return KeyRef(
            namespace_name=self.namespace_name,
            key_name=key_name,
        )

    def git_hub_api_key(
            self,
            api_key_name: str,
    ) -> GitHubApiKeyRef:
        return GitHubApiKeyRef(
            namespace_name=self.namespace_name,
            api_key_name=api_key_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'key',
                self.namespace_name,
            ],
        ).str()


class KeyRef:
    namespace_name: str
    key_name: str

    def __init__(
            self,
            namespace_name: str,
            key_name: str,
    ):
        self.namespace_name = namespace_name
        self.key_name = key_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'key',
                self.namespace_name,
                'key',
                self.key_name,
            ],
        ).str()


class GitHubApiKeyRef:
    namespace_name: str
    api_key_name: str

    def __init__(
            self,
            namespace_name: str,
            api_key_name: str,
    ):
        self.namespace_name = namespace_name
        self.api_key_name = api_key_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'key',
                self.namespace_name,
                'github',
                self.api_key_name,
            ],
        ).str()
