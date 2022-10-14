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


class DirectEnhanceByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            rate_name: str,
            target_item_set_id: str,
            materials: List[Material] = None,
            config: List[Config] = None,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.rate_name = rate_name
        self.user_id = user_id
        self.target_item_set_id = target_item_set_id
        self.materials = materials
        self.config = config

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if rate_name:
            properties["rateName"] = rate_name
        if user_id:
            properties["userId"] = user_id
        if target_item_set_id:
            properties["targetItemSetId"] = target_item_set_id
        if materials:
            properties["materials"] = materials
        if config:
            properties["config"] = config

        super().__init__(
            action="Gs2Enhance:DirectEnhanceByUserId",
            request=properties,
        )


class DeleteProgressByUserId(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            rate_name: str,
            progress_name: str,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.rate_name = rate_name
        self.progress_name = progress_name

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if rate_name:
            properties["rateName"] = rate_name
        if progress_name:
            properties["progressName"] = progress_name

        super().__init__(
            action="Gs2Enhance:DeleteProgressByUserId",
            request=properties,
        )


class CreateProgressByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            rate_name: str,
            target_item_set_id: str,
            force: bool,
            materials: List[Material] = None,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.rate_name = rate_name
        self.target_item_set_id = target_item_set_id
        self.materials = materials
        self.force = force

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if rate_name:
            properties["rateName"] = rate_name
        if target_item_set_id:
            properties["targetItemSetId"] = target_item_set_id
        if materials:
            properties["materials"] = materials
        if force:
            properties["force"] = force

        super().__init__(
            action="Gs2Enhance:CreateProgressByUserId",
            request=properties,
        )
