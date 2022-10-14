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
from .ref import *


class LimitModel:

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
    name: str
    metadata: str
    reset_type: str
    reset_day_of_month: int
    reset_day_of_week: str
    reset_hour: int

    def __init__(
            self,
            name: str,
            reset_type: ResetType,
            metadata: str = None,
            reset_day_of_month: int = None,
            reset_day_of_week: ResetDayOfWeek = None,
            reset_hour: int = None,
    ):
        self.name = name
        self.metadata = metadata
        self.reset_type = reset_type
        self.reset_day_of_month = reset_day_of_month
        self.reset_day_of_week = reset_day_of_week
        self.reset_hour = reset_hour

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.reset_type:
            properties["ResetType"] = self.reset_type
        if self.reset_day_of_month:
            properties["ResetDayOfMonth"] = self.reset_day_of_month
        if self.reset_day_of_week:
            properties["ResetDayOfWeek"] = self.reset_day_of_week
        if self.reset_hour:
            properties["ResetHour"] = self.reset_hour
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return LimitModelRef(
            namespace_name=namespace_name,
            limit_name=self.name,
        )

    @staticmethod
    def not_reset(
        name: str = None,
        metadata: str = None,
    ) -> LimitModel:
        return LimitModel(
            reset_type=LimitModel.ResetType.NOT_RESET,
            name=name,
            metadata=metadata,
        )

    @staticmethod
    def daily(
        reset_hour: int,
        name: str = None,
        metadata: str = None,
    ) -> LimitModel:
        return LimitModel(
            reset_type=LimitModel.ResetType.DAILY,
            name=name,
            metadata=metadata,
            reset_hour=reset_hour,
        )

    @staticmethod
    def weekly(
        reset_day_of_week: str,
        reset_hour: int,
        name: str = None,
        metadata: str = None,
    ) -> LimitModel:
        return LimitModel(
            reset_type=LimitModel.ResetType.WEEKLY,
            name=name,
            metadata=metadata,
            reset_day_of_week=reset_day_of_week,
            reset_hour=reset_hour,
        )

    @staticmethod
    def monthly(
        reset_day_of_month: int,
        reset_hour: int,
        name: str = None,
        metadata: str = None,
    ) -> LimitModel:
        return LimitModel(
            reset_type=LimitModel.ResetType.MONTHLY,
            name=name,
            metadata=metadata,
            reset_day_of_month=reset_day_of_month,
            reset_hour=reset_hour,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-04-05'
    namespace_name: str
    limit_models: List[LimitModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            limit_models: List[LimitModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.limit_models = limit_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Limit::CurrentLimitMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "limit_models": [
                    element.properties()
                    for element in self.limit_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Limit::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.log_setting:
            properties["LogSetting"] = self.log_setting.properties()
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
    ):
        return NamespaceRef(
            namespace_name=self.name,
        )

    def get_attr_namespace_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.NamespaceId"
        )

    def master_data(
            self,
            limit_models: List[LimitModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            limit_models=limit_models,
        ).add_depends_on(
            self,
        )
        return self


class LimitModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    reset_type: str
    reset_day_of_month: int
    reset_day_of_week: str
    reset_hour: int

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            reset_type: str,
            reset_day_of_month: int,
            reset_day_of_week: str,
            reset_hour: int,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.reset_type = reset_type
        self.reset_day_of_month = reset_day_of_month
        self.reset_day_of_week = reset_day_of_week
        self.reset_hour = reset_hour

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Limit::LimitModelMaster"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.reset_type:
            properties["ResetType"] = self.reset_type
        if self.reset_day_of_month:
            properties["ResetDayOfMonth"] = self.reset_day_of_month
        if self.reset_day_of_week:
            properties["ResetDayOfWeek"] = self.reset_day_of_week
        if self.reset_hour:
            properties["ResetHour"] = self.reset_hour
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return LimitModelMasterRef(
            namespace_name=namespace_name,
            limit_name=self.name,
        )

    def get_attr_limit_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.LimitModelId"
        )
