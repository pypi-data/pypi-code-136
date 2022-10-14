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


class ReceiveByUserId(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            mission_group_name: str,
            mission_task_name: str,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.mission_group_name = mission_group_name
        self.mission_task_name = mission_task_name
        self.user_id = user_id

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if mission_group_name:
            properties["missionGroupName"] = mission_group_name
        if mission_task_name:
            properties["missionTaskName"] = mission_task_name
        if user_id:
            properties["userId"] = user_id

        super().__init__(
            action="Gs2Mission:ReceiveByUserId",
            request=properties,
        )


class IncreaseCounterByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            counter_name: str,
            value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.counter_name = counter_name
        self.user_id = user_id
        self.value = value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if counter_name:
            properties["counterName"] = counter_name
        if user_id:
            properties["userId"] = user_id
        if value:
            properties["value"] = value

        super().__init__(
            action="Gs2Mission:IncreaseCounterByUserId",
            request=properties,
        )
