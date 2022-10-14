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


class AddExperienceByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            experience_name: str,
            property_id: str,
            experience_value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.experience_name = experience_name
        self.property_id = property_id
        self.experience_value = experience_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if experience_name:
            properties["experienceName"] = experience_name
        if property_id:
            properties["propertyId"] = property_id
        if experience_value:
            properties["experienceValue"] = experience_value

        super().__init__(
            action="Gs2Experience:AddExperienceByUserId",
            request=properties,
        )


class AddRankCapByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            experience_name: str,
            property_id: str,
            rank_cap_value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.experience_name = experience_name
        self.property_id = property_id
        self.rank_cap_value = rank_cap_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if experience_name:
            properties["experienceName"] = experience_name
        if property_id:
            properties["propertyId"] = property_id
        if rank_cap_value:
            properties["rankCapValue"] = rank_cap_value

        super().__init__(
            action="Gs2Experience:AddRankCapByUserId",
            request=properties,
        )


class SetRankCapByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            experience_name: str,
            property_id: str,
            rank_cap_value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.experience_name = experience_name
        self.property_id = property_id
        self.rank_cap_value = rank_cap_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if user_id:
            properties["userId"] = user_id
        if experience_name:
            properties["experienceName"] = experience_name
        if property_id:
            properties["propertyId"] = property_id
        if rank_cap_value:
            properties["rankCapValue"] = rank_cap_value

        super().__init__(
            action="Gs2Experience:SetRankCapByUserId",
            request=properties,
        )
