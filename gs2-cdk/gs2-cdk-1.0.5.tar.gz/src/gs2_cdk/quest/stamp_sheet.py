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


class DeleteProgressByUserId(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id

        super().__init__(
            action="Gs2Quest:DeleteProgressByUserId",
            request=properties,
        )


class CreateProgressByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            quest_model_id: str,
            force: bool,
            config: List[Config] = None,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.quest_model_id = quest_model_id
        self.force = force
        self.config = config

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if quest_model_id:
            properties["questModelId"] = quest_model_id
        if force:
            properties["force"] = force
        if config:
            properties["config"] = config

        super().__init__(
            action="Gs2Quest:CreateProgressByUserId",
            request=properties,
        )
