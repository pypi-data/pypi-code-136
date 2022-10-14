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


class CategoryModel:

    class OrderDirection(Enum):
        ASC = "asc"
        DESC = "desc"

    class Scope(Enum):
        GLOBAL = "global"
        SCOPED = "scoped"
    name: str
    metadata: str
    minimum_value: int
    maximum_value: int
    order_direction: str
    scope: str
    unique_by_user_id: bool
    calculate_fixed_timing_hour: int
    calculate_fixed_timing_minute: int
    calculate_interval_minutes: int
    entry_period_event_id: str
    access_period_event_id: str
    generation: str

    def __init__(
            self,
            name: str,
            order_direction: OrderDirection,
            scope: Scope,
            unique_by_user_id: bool,
            metadata: str = None,
            minimum_value: int = None,
            maximum_value: int = None,
            calculate_fixed_timing_hour: int = None,
            calculate_fixed_timing_minute: int = None,
            calculate_interval_minutes: int = None,
            entry_period_event_id: str = None,
            access_period_event_id: str = None,
            generation: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.order_direction = order_direction
        self.scope = scope
        self.unique_by_user_id = unique_by_user_id
        self.calculate_fixed_timing_hour = calculate_fixed_timing_hour
        self.calculate_fixed_timing_minute = calculate_fixed_timing_minute
        self.calculate_interval_minutes = calculate_interval_minutes
        self.entry_period_event_id = entry_period_event_id
        self.access_period_event_id = access_period_event_id
        self.generation = generation

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.minimum_value:
            properties["MinimumValue"] = self.minimum_value
        if self.maximum_value:
            properties["MaximumValue"] = self.maximum_value
        if self.order_direction:
            properties["OrderDirection"] = self.order_direction
        if self.scope:
            properties["Scope"] = self.scope
        if self.unique_by_user_id:
            properties["UniqueByUserId"] = self.unique_by_user_id
        if self.calculate_fixed_timing_hour:
            properties["CalculateFixedTimingHour"] = self.calculate_fixed_timing_hour
        if self.calculate_fixed_timing_minute:
            properties["CalculateFixedTimingMinute"] = self.calculate_fixed_timing_minute
        if self.calculate_interval_minutes:
            properties["CalculateIntervalMinutes"] = self.calculate_interval_minutes
        if self.entry_period_event_id:
            properties["EntryPeriodEventId"] = self.entry_period_event_id
        if self.access_period_event_id:
            properties["AccessPeriodEventId"] = self.access_period_event_id
        if self.generation:
            properties["Generation"] = self.generation
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return CategoryModelRef(
            namespace_name=namespace_name,
            category_name=self.name,
        )

    @staticmethod
    def global(
        calculate_interval_minutes: int,
        name: str = None,
        metadata: str = None,
        minimum_value: int = None,
        maximum_value: int = None,
        order_direction: str = None,
        unique_by_user_id: bool = None,
        calculate_fixed_timing_hour: int = None,
        calculate_fixed_timing_minute: int = None,
        entry_period_event_id: str = None,
        access_period_event_id: str = None,
        generation: str = None,
    ) -> CategoryModel:
        return CategoryModel(
            scope=CategoryModel.Scope.GLOBAL,
            name=name,
            metadata=metadata,
            minimum_value=minimum_value,
            maximum_value=maximum_value,
            order_direction=order_direction,
            unique_by_user_id=unique_by_user_id,
            calculate_fixed_timing_hour=calculate_fixed_timing_hour,
            calculate_fixed_timing_minute=calculate_fixed_timing_minute,
            calculate_interval_minutes=calculate_interval_minutes,
            entry_period_event_id=entry_period_event_id,
            access_period_event_id=access_period_event_id,
            generation=generation,
        )

    @staticmethod
    def scoped(
        name: str = None,
        metadata: str = None,
        minimum_value: int = None,
        maximum_value: int = None,
        order_direction: str = None,
        unique_by_user_id: bool = None,
        calculate_fixed_timing_hour: int = None,
        calculate_fixed_timing_minute: int = None,
        entry_period_event_id: str = None,
        access_period_event_id: str = None,
        generation: str = None,
    ) -> CategoryModel:
        return CategoryModel(
            scope=CategoryModel.Scope.SCOPED,
            name=name,
            metadata=metadata,
            minimum_value=minimum_value,
            maximum_value=maximum_value,
            order_direction=order_direction,
            unique_by_user_id=unique_by_user_id,
            calculate_fixed_timing_hour=calculate_fixed_timing_hour,
            calculate_fixed_timing_minute=calculate_fixed_timing_minute,
            entry_period_event_id=entry_period_event_id,
            access_period_event_id=access_period_event_id,
            generation=generation,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-09-17'
    namespace_name: str
    category_models: List[CategoryModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            category_models: List[CategoryModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.category_models = category_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Ranking::CurrentRankingMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "category_models": [
                    element.properties()
                    for element in self.category_models
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
        return "GS2::Ranking::Namespace"

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
            category_models: List[CategoryModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            category_models=category_models,
        ).add_depends_on(
            self,
        )
        return self


class CategoryModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    minimum_value: int
    maximum_value: int
    order_direction: str
    scope: str
    unique_by_user_id: bool
    calculate_fixed_timing_hour: int
    calculate_fixed_timing_minute: int
    calculate_interval_minutes: int
    entry_period_event_id: str
    access_period_event_id: str
    generation: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            order_direction: str,
            scope: str,
            unique_by_user_id: bool,
            calculate_interval_minutes: int,
            description: str = None,
            metadata: str = None,
            minimum_value: int = None,
            maximum_value: int = None,
            calculate_fixed_timing_hour: int = None,
            calculate_fixed_timing_minute: int = None,
            entry_period_event_id: str = None,
            access_period_event_id: str = None,
            generation: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.order_direction = order_direction
        self.scope = scope
        self.unique_by_user_id = unique_by_user_id
        self.calculate_fixed_timing_hour = calculate_fixed_timing_hour
        self.calculate_fixed_timing_minute = calculate_fixed_timing_minute
        self.calculate_interval_minutes = calculate_interval_minutes
        self.entry_period_event_id = entry_period_event_id
        self.access_period_event_id = access_period_event_id
        self.generation = generation

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Ranking::CategoryModelMaster"

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
        if self.minimum_value:
            properties["MinimumValue"] = self.minimum_value
        if self.maximum_value:
            properties["MaximumValue"] = self.maximum_value
        if self.order_direction:
            properties["OrderDirection"] = self.order_direction
        if self.scope:
            properties["Scope"] = self.scope
        if self.unique_by_user_id:
            properties["UniqueByUserId"] = self.unique_by_user_id
        if self.calculate_fixed_timing_hour:
            properties["CalculateFixedTimingHour"] = self.calculate_fixed_timing_hour
        if self.calculate_fixed_timing_minute:
            properties["CalculateFixedTimingMinute"] = self.calculate_fixed_timing_minute
        if self.calculate_interval_minutes:
            properties["CalculateIntervalMinutes"] = self.calculate_interval_minutes
        if self.entry_period_event_id:
            properties["EntryPeriodEventId"] = self.entry_period_event_id
        if self.access_period_event_id:
            properties["AccessPeriodEventId"] = self.access_period_event_id
        if self.generation:
            properties["Generation"] = self.generation
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return CategoryModelMasterRef(
            namespace_name=namespace_name,
            category_name=self.name,
        )

    def get_attr_category_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.CategoryModelId"
        )
