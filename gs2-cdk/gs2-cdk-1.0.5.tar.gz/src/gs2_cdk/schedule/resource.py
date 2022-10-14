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


class Event:

    class ScheduleType(Enum):
        ABSOLUTE = "absolute"
        RELATIVE = "relative"

    class RepeatType(Enum):
        ALWAYS = "always"
        DAILY = "daily"
        WEEKLY = "weekly"
        MONTHLY = "monthly"

    class RepeatBeginDayOfWeek(Enum):
        SUNDAY = "sunday"
        MONDAY = "monday"
        TUESDAY = "tuesday"
        WEDNESDAY = "wednesday"
        THURSDAY = "thursday"
        FRIDAY = "friday"
        SATURDAY = "saturday"

    class RepeatEndDayOfWeek(Enum):
        SUNDAY = "sunday"
        MONDAY = "monday"
        TUESDAY = "tuesday"
        WEDNESDAY = "wednesday"
        THURSDAY = "thursday"
        FRIDAY = "friday"
        SATURDAY = "saturday"
    name: str
    metadata: str
    schedule_type: str
    repeat_type: str
    absolute_begin: int
    absolute_end: int
    repeat_begin_day_of_month: int
    repeat_end_day_of_month: int
    repeat_begin_day_of_week: str
    repeat_end_day_of_week: str
    repeat_begin_hour: int
    repeat_end_hour: int
    relative_trigger_name: str
    relative_duration: int

    def __init__(
            self,
            name: str,
            schedule_type: ScheduleType,
            metadata: str = None,
            repeat_type: RepeatType = None,
            absolute_begin: int = None,
            absolute_end: int = None,
            repeat_begin_day_of_month: int = None,
            repeat_end_day_of_month: int = None,
            repeat_begin_day_of_week: RepeatBeginDayOfWeek = None,
            repeat_end_day_of_week: RepeatEndDayOfWeek = None,
            repeat_begin_hour: int = None,
            repeat_end_hour: int = None,
            relative_trigger_name: str = None,
            relative_duration: int = None,
    ):
        self.name = name
        self.metadata = metadata
        self.schedule_type = schedule_type
        self.repeat_type = repeat_type
        self.absolute_begin = absolute_begin
        self.absolute_end = absolute_end
        self.repeat_begin_day_of_month = repeat_begin_day_of_month
        self.repeat_end_day_of_month = repeat_end_day_of_month
        self.repeat_begin_day_of_week = repeat_begin_day_of_week
        self.repeat_end_day_of_week = repeat_end_day_of_week
        self.repeat_begin_hour = repeat_begin_hour
        self.repeat_end_hour = repeat_end_hour
        self.relative_trigger_name = relative_trigger_name
        self.relative_duration = relative_duration

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.schedule_type:
            properties["ScheduleType"] = self.schedule_type
        if self.repeat_type:
            properties["RepeatType"] = self.repeat_type
        if self.absolute_begin:
            properties["AbsoluteBegin"] = self.absolute_begin
        if self.absolute_end:
            properties["AbsoluteEnd"] = self.absolute_end
        if self.repeat_begin_day_of_month:
            properties["RepeatBeginDayOfMonth"] = self.repeat_begin_day_of_month
        if self.repeat_end_day_of_month:
            properties["RepeatEndDayOfMonth"] = self.repeat_end_day_of_month
        if self.repeat_begin_day_of_week:
            properties["RepeatBeginDayOfWeek"] = self.repeat_begin_day_of_week
        if self.repeat_end_day_of_week:
            properties["RepeatEndDayOfWeek"] = self.repeat_end_day_of_week
        if self.repeat_begin_hour:
            properties["RepeatBeginHour"] = self.repeat_begin_hour
        if self.repeat_end_hour:
            properties["RepeatEndHour"] = self.repeat_end_hour
        if self.relative_trigger_name:
            properties["RelativeTriggerName"] = self.relative_trigger_name
        if self.relative_duration:
            properties["RelativeDuration"] = self.relative_duration
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return EventRef(
            namespace_name=namespace_name,
            event_name=self.name,
        )

    @staticmethod
    def absolute(
        repeat_type: str,
        absolute_begin: int,
        absolute_end: int,
        name: str = None,
        metadata: str = None,
        repeat_begin_day_of_month: int = None,
        repeat_end_day_of_month: int = None,
        repeat_begin_day_of_week: str = None,
        repeat_end_day_of_week: str = None,
        repeat_begin_hour: int = None,
        repeat_end_hour: int = None,
    ) -> Event:
        return Event(
            schedule_type=Event.ScheduleType.ABSOLUTE,
            name=name,
            metadata=metadata,
            repeat_type=repeat_type,
            absolute_begin=absolute_begin,
            absolute_end=absolute_end,
            repeat_begin_day_of_month=repeat_begin_day_of_month,
            repeat_end_day_of_month=repeat_end_day_of_month,
            repeat_begin_day_of_week=repeat_begin_day_of_week,
            repeat_end_day_of_week=repeat_end_day_of_week,
            repeat_begin_hour=repeat_begin_hour,
            repeat_end_hour=repeat_end_hour,
        )

    @staticmethod
    def relative(
        relative_trigger_name: str,
        relative_duration: int,
        name: str = None,
        metadata: str = None,
        repeat_begin_day_of_month: int = None,
        repeat_end_day_of_month: int = None,
        repeat_begin_day_of_week: str = None,
        repeat_end_day_of_week: str = None,
        repeat_begin_hour: int = None,
        repeat_end_hour: int = None,
    ) -> Event:
        return Event(
            schedule_type=Event.ScheduleType.RELATIVE,
            name=name,
            metadata=metadata,
            repeat_begin_day_of_month=repeat_begin_day_of_month,
            repeat_end_day_of_month=repeat_end_day_of_month,
            repeat_begin_day_of_week=repeat_begin_day_of_week,
            repeat_end_day_of_week=repeat_end_day_of_week,
            repeat_begin_hour=repeat_begin_hour,
            repeat_end_hour=repeat_end_hour,
            relative_trigger_name=relative_trigger_name,
            relative_duration=relative_duration,
        )

    @staticmethod
    def always(
        name: str = None,
        metadata: str = None,
        schedule_type: str = None,
        absolute_begin: int = None,
        absolute_end: int = None,
        relative_trigger_name: str = None,
        relative_duration: int = None,
    ) -> Event:
        return Event(
            repeat_type=Event.RepeatType.ALWAYS,
            name=name,
            metadata=metadata,
            schedule_type=schedule_type,
            absolute_begin=absolute_begin,
            absolute_end=absolute_end,
            relative_trigger_name=relative_trigger_name,
            relative_duration=relative_duration,
        )

    @staticmethod
    def daily(
        repeat_begin_hour: int,
        repeat_end_hour: int,
        name: str = None,
        metadata: str = None,
        schedule_type: str = None,
        absolute_begin: int = None,
        absolute_end: int = None,
        relative_trigger_name: str = None,
        relative_duration: int = None,
    ) -> Event:
        return Event(
            repeat_type=Event.RepeatType.DAILY,
            name=name,
            metadata=metadata,
            schedule_type=schedule_type,
            absolute_begin=absolute_begin,
            absolute_end=absolute_end,
            repeat_begin_hour=repeat_begin_hour,
            repeat_end_hour=repeat_end_hour,
            relative_trigger_name=relative_trigger_name,
            relative_duration=relative_duration,
        )

    @staticmethod
    def weekly(
        repeat_begin_day_of_week: str,
        repeat_end_day_of_week: str,
        repeat_begin_hour: int,
        repeat_end_hour: int,
        name: str = None,
        metadata: str = None,
        schedule_type: str = None,
        absolute_begin: int = None,
        absolute_end: int = None,
        relative_trigger_name: str = None,
        relative_duration: int = None,
    ) -> Event:
        return Event(
            repeat_type=Event.RepeatType.WEEKLY,
            name=name,
            metadata=metadata,
            schedule_type=schedule_type,
            absolute_begin=absolute_begin,
            absolute_end=absolute_end,
            repeat_begin_day_of_week=repeat_begin_day_of_week,
            repeat_end_day_of_week=repeat_end_day_of_week,
            repeat_begin_hour=repeat_begin_hour,
            repeat_end_hour=repeat_end_hour,
            relative_trigger_name=relative_trigger_name,
            relative_duration=relative_duration,
        )

    @staticmethod
    def monthly(
        repeat_begin_day_of_month: int,
        repeat_end_day_of_month: int,
        repeat_begin_hour: int,
        repeat_end_hour: int,
        name: str = None,
        metadata: str = None,
        schedule_type: str = None,
        absolute_begin: int = None,
        absolute_end: int = None,
        relative_trigger_name: str = None,
        relative_duration: int = None,
    ) -> Event:
        return Event(
            repeat_type=Event.RepeatType.MONTHLY,
            name=name,
            metadata=metadata,
            schedule_type=schedule_type,
            absolute_begin=absolute_begin,
            absolute_end=absolute_end,
            repeat_begin_day_of_month=repeat_begin_day_of_month,
            repeat_end_day_of_month=repeat_end_day_of_month,
            repeat_begin_hour=repeat_begin_hour,
            repeat_end_hour=repeat_end_hour,
            relative_trigger_name=relative_trigger_name,
            relative_duration=relative_duration,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-03-31'
    namespace_name: str
    events: List[Event]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            events: List[Event],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.events = events

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Schedule::CurrentEventMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "events": [
                    element.properties()
                    for element in self.events
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
        return "GS2::Schedule::Namespace"

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
            events: List[Event],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            events=events,
        ).add_depends_on(
            self,
        )
        return self


class EventMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    schedule_type: str
    absolute_begin: int
    absolute_end: int
    repeat_type: str
    repeat_begin_day_of_month: int
    repeat_end_day_of_month: int
    repeat_begin_day_of_week: str
    repeat_end_day_of_week: str
    repeat_begin_hour: int
    repeat_end_hour: int
    relative_trigger_name: str
    relative_duration: int

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            schedule_type: str,
            absolute_begin: int,
            absolute_end: int,
            repeat_type: str,
            repeat_begin_day_of_month: int,
            repeat_end_day_of_month: int,
            repeat_begin_day_of_week: str,
            repeat_end_day_of_week: str,
            repeat_begin_hour: int,
            repeat_end_hour: int,
            relative_trigger_name: str,
            relative_duration: int,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.schedule_type = schedule_type
        self.absolute_begin = absolute_begin
        self.absolute_end = absolute_end
        self.repeat_type = repeat_type
        self.repeat_begin_day_of_month = repeat_begin_day_of_month
        self.repeat_end_day_of_month = repeat_end_day_of_month
        self.repeat_begin_day_of_week = repeat_begin_day_of_week
        self.repeat_end_day_of_week = repeat_end_day_of_week
        self.repeat_begin_hour = repeat_begin_hour
        self.repeat_end_hour = repeat_end_hour
        self.relative_trigger_name = relative_trigger_name
        self.relative_duration = relative_duration

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Schedule::EventMaster"

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
        if self.schedule_type:
            properties["ScheduleType"] = self.schedule_type
        if self.absolute_begin:
            properties["AbsoluteBegin"] = self.absolute_begin
        if self.absolute_end:
            properties["AbsoluteEnd"] = self.absolute_end
        if self.repeat_type:
            properties["RepeatType"] = self.repeat_type
        if self.repeat_begin_day_of_month:
            properties["RepeatBeginDayOfMonth"] = self.repeat_begin_day_of_month
        if self.repeat_end_day_of_month:
            properties["RepeatEndDayOfMonth"] = self.repeat_end_day_of_month
        if self.repeat_begin_day_of_week:
            properties["RepeatBeginDayOfWeek"] = self.repeat_begin_day_of_week
        if self.repeat_end_day_of_week:
            properties["RepeatEndDayOfWeek"] = self.repeat_end_day_of_week
        if self.repeat_begin_hour:
            properties["RepeatBeginHour"] = self.repeat_begin_hour
        if self.repeat_end_hour:
            properties["RepeatEndHour"] = self.repeat_end_hour
        if self.relative_trigger_name:
            properties["RelativeTriggerName"] = self.relative_trigger_name
        if self.relative_duration:
            properties["RelativeDuration"] = self.relative_duration
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return EventMasterRef(
            namespace_name=namespace_name,
            event_name=self.name,
        )

    def get_attr_event_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.EventId"
        )
