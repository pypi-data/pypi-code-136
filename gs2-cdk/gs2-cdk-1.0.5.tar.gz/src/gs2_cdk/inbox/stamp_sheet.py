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


class OpenMessageByUserId(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            message_name: str,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.message_name = message_name

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if message_name:
            properties["messageName"] = message_name

        super().__init__(
            action="Gs2Inbox:OpenMessageByUserId",
            request=properties,
        )


class SendMessageByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            metadata: str,
            read_acquire_actions: List[AcquireAction] = None,
            expires_at: int = None,
            expires_time_span: TimeSpan = None,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.metadata = metadata
        self.read_acquire_actions = read_acquire_actions
        self.expires_at = expires_at
        self.expires_time_span = expires_time_span

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if metadata:
            properties["metadata"] = metadata
        if read_acquire_actions:
            properties["readAcquireActions"] = read_acquire_actions
        if expires_at:
            properties["expiresAt"] = expires_at
        if expires_time_span:
            properties["expiresTimeSpan"] = expires_time_span

        super().__init__(
            action="Gs2Inbox:SendMessageByUserId",
            request=properties,
        )
