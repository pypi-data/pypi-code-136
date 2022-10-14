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


class CounterScopeModel:

    class ResetType(Enum):
        NOT_RESET = "notReset"
        DAILY = "daily"
        WEEKLY = "weekly"
        MONTHLY = "monthly"

    class ResetDayOfWeek(Enum):
        SUNDAY = "sunday"
        MONDAY = "monday"
        TUESDAY = "tuesday"
        WEDNESDAY = "wednesday"
        THURSDAY = "thursday"
        FRIDAY = "friday"
        SATURDAY = "saturday"
    reset_type: ResetType
    reset_day_of_month: int
    reset_day_of_week: ResetDayOfWeek
    reset_hour: int

    def __init__(
            self,
            reset_type: ResetType = None,
            reset_day_of_month: int = None,
            reset_day_of_week: ResetDayOfWeek = None,
            reset_hour: int = None,
    ):
        self.reset_type = reset_type
        self.reset_day_of_month = reset_day_of_month
        self.reset_day_of_week = reset_day_of_week
        self.reset_hour = reset_hour

    @staticmethod
    def not_reset(
    ) -> CounterScopeModel:
        return CounterScopeModel(
            reset_type=CounterScopeModel.ResetType.NOT_RESET,
        )

    @staticmethod
    def daily(
        reset_hour: int,
    ) -> CounterScopeModel:
        return CounterScopeModel(
            reset_type=CounterScopeModel.ResetType.DAILY,
            reset_hour=reset_hour,
        )

    @staticmethod
    def weekly(
        reset_day_of_week: str,
        reset_hour: int,
    ) -> CounterScopeModel:
        return CounterScopeModel(
            reset_type=CounterScopeModel.ResetType.WEEKLY,
            reset_day_of_week=reset_day_of_week,
            reset_hour=reset_hour,
        )

    @staticmethod
    def monthly(
        reset_day_of_month: int,
        reset_hour: int,
    ) -> CounterScopeModel:
        return CounterScopeModel(
            reset_type=CounterScopeModel.ResetType.MONTHLY,
            reset_day_of_month=reset_day_of_month,
            reset_hour=reset_hour,
        )

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.reset_type:
            properties["ResetType"] = self.reset_type
        if self.reset_day_of_month:
            properties["ResetDayOfMonth"] = self.reset_day_of_month
        if self.reset_day_of_week:
            properties["ResetDayOfWeek"] = self.reset_day_of_week
        if self.reset_hour:
            properties["ResetHour"] = self.reset_hour
        return properties


class ScopedValue:

    class ResetType(Enum):
        NOT_RESET = "notReset"
        DAILY = "daily"
        WEEKLY = "weekly"
        MONTHLY = "monthly"
    reset_type: ResetType
    value: int
    next_reset_at: int
    updated_at: int

    def __init__(
            self,
            reset_type: ResetType = None,
            value: int = None,
            next_reset_at: int = None,
            updated_at: int = None,
    ):
        self.reset_type = reset_type
        self.value = value
        self.next_reset_at = next_reset_at
        self.updated_at = updated_at

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.reset_type:
            properties["ResetType"] = self.reset_type
        if self.value:
            properties["Value"] = self.value
        if self.next_reset_at:
            properties["NextResetAt"] = self.next_reset_at
        if self.updated_at:
            properties["UpdatedAt"] = self.updated_at
        return properties
