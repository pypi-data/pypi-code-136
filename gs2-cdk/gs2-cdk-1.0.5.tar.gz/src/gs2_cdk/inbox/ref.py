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

    def current_message_master(
            self,
    ) -> CurrentMessageMasterRef:
        return CurrentMessageMasterRef(
            namespace_name=self.namespace_name,
        )

    def global_message(
            self,
            global_message_name: str,
    ) -> GlobalMessageRef:
        return GlobalMessageRef(
            namespace_name=self.namespace_name,
            global_message_name=global_message_name,
        )

    def global_message_master(
            self,
            global_message_name: str,
    ) -> GlobalMessageMasterRef:
        return GlobalMessageMasterRef(
            namespace_name=self.namespace_name,
            global_message_name=global_message_name,
        )

    def send_message(
            self,
            metadata: str,
            read_acquire_actions: List[AcquireAction] = None,
            expires_at: int = None,
            expires_time_span: TimeSpan = None,
            user_id: str = '#{userId}',
    ) -> SendMessageByUserId:
        return SendMessageByUserId(
            namespace_name=self.namespace_name,
            user_id=user_id,
            metadata=metadata,
            read_acquire_actions=read_acquire_actions,
            expires_at=expires_at,
            expires_time_span=expires_time_span,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'inbox',
                self.namespace_name,
            ],
        ).str()


class CurrentMessageMasterRef:
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
                'inbox',
                self.namespace_name,
            ],
        ).str()


class GlobalMessageMasterRef:
    namespace_name: str
    global_message_name: str

    def __init__(
            self,
            namespace_name: str,
            global_message_name: str,
    ):
        self.namespace_name = namespace_name
        self.global_message_name = global_message_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'inbox',
                self.namespace_name,
                'master',
                'globalMessage',
                self.global_message_name,
            ],
        ).str()


class GlobalMessageRef:
    namespace_name: str
    global_message_name: str

    def __init__(
            self,
            namespace_name: str,
            global_message_name: str,
    ):
        self.namespace_name = namespace_name
        self.global_message_name = global_message_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'inbox',
                self.namespace_name,
                'globalMessage',
                self.global_message_name,
            ],
        ).str()
