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


class ExchangeByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            rate_name: str,
            count: int,
            config: List[Config] = None,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.rate_name = rate_name
        self.user_id = user_id
        self.count = count
        self.config = config

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if rate_name:
            properties["rateName"] = rate_name
        if user_id:
            properties["userId"] = user_id
        if count:
            properties["count"] = count
        if config:
            properties["config"] = config

        super().__init__(
            action="Gs2Exchange:ExchangeByUserId",
            request=properties,
        )


class DeleteAwaitByUserId(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            rate_name: str,
            await_name: str,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.rate_name = rate_name
        self.await_name = await_name

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if rate_name:
            properties["rateName"] = rate_name
        if await_name:
            properties["awaitName"] = await_name

        super().__init__(
            action="Gs2Exchange:DeleteAwaitByUserId",
            request=properties,
        )


class CreateAwaitByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            rate_name: str,
            count: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.rate_name = rate_name
        self.count = count

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if rate_name:
            properties["rateName"] = rate_name
        if count:
            properties["count"] = count

        super().__init__(
            action="Gs2Exchange:CreateAwaitByUserId",
            request=properties,
        )
