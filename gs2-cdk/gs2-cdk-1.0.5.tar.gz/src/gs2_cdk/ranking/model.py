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

from enum import Enum
from ..core import *


class Ranking:
    rank: int
    index: int
    user_id: str
    score: int
    metadata: str
    created_at: int

    def __init__(
            self,
            rank: int = None,
            index: int = None,
            user_id: str = None,
            score: int = None,
            metadata: str = None,
            created_at: int = None,
    ):
        self.rank = rank
        self.index = index
        self.user_id = user_id
        self.score = score
        self.metadata = metadata
        self.created_at = created_at

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.rank:
            properties["Rank"] = self.rank
        if self.index:
            properties["Index"] = self.index
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.score:
            properties["Score"] = self.score
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.created_at:
            properties["CreatedAt"] = self.created_at
        return properties


class CalculatedAt:
    category_name: str
    calculated_at: int

    def __init__(
            self,
            category_name: str = None,
            calculated_at: int = None,
    ):
        self.category_name = category_name
        self.calculated_at = calculated_at

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.category_name:
            properties["CategoryName"] = self.category_name
        if self.calculated_at:
            properties["CalculatedAt"] = self.calculated_at
        return properties


class SubscribeUser:
    category_name: str
    user_id: str
    target_user_id: str

    def __init__(
            self,
            category_name: str = None,
            user_id: str = None,
            target_user_id: str = None,
    ):
        self.category_name = category_name
        self.user_id = user_id
        self.target_user_id = target_user_id

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.category_name:
            properties["CategoryName"] = self.category_name
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.target_user_id:
            properties["TargetUserId"] = self.target_user_id
        return properties
