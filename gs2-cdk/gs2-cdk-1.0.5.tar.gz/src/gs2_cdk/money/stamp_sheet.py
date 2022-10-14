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


class WithdrawByUserId(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            slot: int,
            count: int,
            paid_only: bool,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.slot = slot
        self.count = count
        self.paid_only = paid_only

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if slot:
            properties["slot"] = slot
        if count:
            properties["count"] = count
        if paid_only:
            properties["paidOnly"] = paid_only

        super().__init__(
            action="Gs2Money:WithdrawByUserId",
            request=properties,
        )


class DepositByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            slot: int,
            price: float,
            count: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.slot = slot
        self.price = price
        self.count = count

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if slot:
            properties["slot"] = slot
        if price:
            properties["price"] = price
        if count:
            properties["count"] = count

        super().__init__(
            action="Gs2Money:DepositByUserId",
            request=properties,
        )


class RecordReceipt(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            contents_id: str,
            receipt: str,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.contents_id = contents_id
        self.receipt = receipt

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if contents_id:
            properties["contentsId"] = contents_id
        if receipt:
            properties["receipt"] = receipt

        super().__init__(
            action="Gs2Money:RecordReceipt",
            request=properties,
        )
