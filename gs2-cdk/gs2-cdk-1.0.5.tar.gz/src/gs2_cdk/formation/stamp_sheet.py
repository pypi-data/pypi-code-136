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


class AddMoldCapacityByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            mold_name: str,
            capacity: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.mold_name = mold_name
        self.capacity = capacity

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if mold_name:
            properties["moldName"] = mold_name
        if capacity:
            properties["capacity"] = capacity

        super().__init__(
            action="Gs2Formation:AddMoldCapacityByUserId",
            request=properties,
        )


class SetMoldCapacityByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            mold_name: str,
            capacity: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.mold_name = mold_name
        self.capacity = capacity

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if mold_name:
            properties["moldName"] = mold_name
        if capacity:
            properties["capacity"] = capacity

        super().__init__(
            action="Gs2Formation:SetMoldCapacityByUserId",
            request=properties,
        )


class AcquireActionsToFormProperties(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            mold_name: str,
            index: int,
            acquire_action: AcquireAction,
            config: List[AcquireActionConfig] = None,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.mold_name = mold_name
        self.index = index
        self.acquire_action = acquire_action
        self.config = config

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if mold_name:
            properties["moldName"] = mold_name
        if index:
            properties["index"] = index
        if acquire_action:
            properties["acquireAction"] = acquire_action
        if config:
            properties["config"] = config

        super().__init__(
            action="Gs2Formation:AcquireActionsToFormProperties",
            request=properties,
        )


class AcquireActionsToPropertyFormProperties(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            form_model_name: str,
            property_id: str,
            acquire_action: AcquireAction,
            config: List[AcquireActionConfig] = None,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.form_model_name = form_model_name
        self.property_id = property_id
        self.acquire_action = acquire_action
        self.config = config

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if form_model_name:
            properties["formModelName"] = form_model_name
        if property_id:
            properties["propertyId"] = property_id
        if acquire_action:
            properties["acquireAction"] = acquire_action
        if config:
            properties["config"] = config

        super().__init__(
            action="Gs2Formation:AcquireActionsToPropertyFormProperties",
            request=properties,
        )
