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


class CountUpByUserId(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            limit_name: str,
            counter_name: str,
            count_up_value: int,
            max_value: int = None,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.limit_name = limit_name
        self.counter_name = counter_name
        self.user_id = user_id
        self.count_up_value = count_up_value
        self.max_value = max_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if limit_name:
            properties["limitName"] = limit_name
        if counter_name:
            properties["counterName"] = counter_name
        if user_id:
            properties["userId"] = user_id
        if count_up_value:
            properties["countUpValue"] = count_up_value
        if max_value:
            properties["maxValue"] = max_value

        super().__init__(
            action="Gs2Limit:CountUpByUserId",
            request=properties,
        )


class DeleteCounterByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            limit_name: str,
            counter_name: str,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.limit_name = limit_name
        self.user_id = user_id
        self.counter_name = counter_name

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if limit_name:
            properties["limitName"] = limit_name
        if user_id:
            properties["userId"] = user_id
        if counter_name:
            properties["counterName"] = counter_name

        super().__init__(
            action="Gs2Limit:DeleteCounterByUserId",
            request=properties,
        )
