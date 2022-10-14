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


class Probability:
    prize: DrawnPrize
    rate: float

    def __init__(
            self,
            prize: DrawnPrize = None,
            rate: float = None,
    ):
        self.prize = prize
        self.rate = rate

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.prize:
            properties["Prize"] = self.prize.properties()
        if self.rate:
            properties["Rate"] = self.rate
        return properties


class Prize:

    class Type(Enum):
        ACTION = "action"
        PRIZE_TABLE = "prize_table"
    prize_id: str
    type: Type
    acquire_actions: List[AcquireAction]
    drawn_limit: int
    limit_fail_over_prize_id: str
    prize_table_name: str
    weight: int

    def __init__(
            self,
            prize_id: str = None,
            type: Type = None,
            acquire_actions: List[AcquireAction] = None,
            drawn_limit: int = None,
            limit_fail_over_prize_id: str = None,
            prize_table_name: str = None,
            weight: int = None,
    ):
        self.prize_id = prize_id
        self.type = type
        self.acquire_actions = acquire_actions
        self.drawn_limit = drawn_limit
        self.limit_fail_over_prize_id = limit_fail_over_prize_id
        self.prize_table_name = prize_table_name
        self.weight = weight

    @staticmethod
    def action(
        prize_id: str,
        acquire_actions: List[AcquireAction],
        weight: int,
        drawn_limit: int = None,
        limit_fail_over_prize_id: str = None,
    ) -> Prize:
        return Prize(
            type=Prize.Type.ACTION,
            prize_id=prize_id,
            acquire_actions=acquire_actions,
            drawn_limit=drawn_limit,
            limit_fail_over_prize_id=limit_fail_over_prize_id,
            weight=weight,
        )

    @staticmethod
    def prize_table(
        prize_id: str,
        acquire_actions: List[AcquireAction],
        prize_table_name: str,
        weight: int,
        drawn_limit: int = None,
    ) -> Prize:
        return Prize(
            type=Prize.Type.PRIZE_TABLE,
            prize_id=prize_id,
            drawn_limit=drawn_limit,
            prize_table_name=prize_table_name,
            weight=weight,
        )

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.prize_id:
            properties["PrizeId"] = self.prize_id
        if self.type:
            properties["Type"] = self.type
        if self.acquire_actions:
            properties["AcquireActions"] = [
                element.properties()
                for element in self.acquire_actions
            ]
        if self.drawn_limit:
            properties["DrawnLimit"] = self.drawn_limit
        if self.limit_fail_over_prize_id:
            properties["LimitFailOverPrizeId"] = self.limit_fail_over_prize_id
        if self.prize_table_name:
            properties["PrizeTableName"] = self.prize_table_name
        if self.weight:
            properties["Weight"] = self.weight
        return properties


class DrawnPrize:
    prize_id: str
    acquire_actions: List[AcquireAction]

    def __init__(
            self,
            prize_id: str = None,
            acquire_actions: List[AcquireAction] = None,
    ):
        self.prize_id = prize_id
        self.acquire_actions = acquire_actions

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.prize_id:
            properties["PrizeId"] = self.prize_id
        if self.acquire_actions:
            properties["AcquireActions"] = [
                element.properties()
                for element in self.acquire_actions
            ]
        return properties


class BoxItem:
    acquire_actions: List[AcquireAction]
    remaining: int
    initial: int

    def __init__(
            self,
            acquire_actions: List[AcquireAction] = None,
            remaining: int = None,
            initial: int = None,
    ):
        self.acquire_actions = acquire_actions
        self.remaining = remaining
        self.initial = initial

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.acquire_actions:
            properties["AcquireActions"] = [
                element.properties()
                for element in self.acquire_actions
            ]
        if self.remaining:
            properties["Remaining"] = self.remaining
        if self.initial:
            properties["Initial"] = self.initial
        return properties


class BoxItems:
    box_id: str
    prize_table_name: str
    user_id: str
    items: List[BoxItem]

    def __init__(
            self,
            box_id: str = None,
            prize_table_name: str = None,
            user_id: str = None,
            items: List[BoxItem] = None,
    ):
        self.box_id = box_id
        self.prize_table_name = prize_table_name
        self.user_id = user_id
        self.items = items

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.box_id:
            properties["BoxId"] = self.box_id
        if self.prize_table_name:
            properties["PrizeTableName"] = self.prize_table_name
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.items:
            properties["Items"] = [
                element.properties()
                for element in self.items
            ]
        return properties
