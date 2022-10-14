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


class CounterModel:
    name: str
    metadata: str
    scopes: List[CounterScopeModel]
    challenge_period_event_id: str

    def __init__(
            self,
            name: str,
            scopes: List[CounterScopeModel],
            metadata: str = None,
            challenge_period_event_id: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.scopes = scopes
        self.challenge_period_event_id = challenge_period_event_id

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.scopes:
            properties["Scopes"] = [
                element.properties()
                for element in self.scopes
            ]
        if self.challenge_period_event_id:
            properties["ChallengePeriodEventId"] = self.challenge_period_event_id
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return CounterModelRef(
            namespace_name=namespace_name,
            counter_name=self.name,
        )


class MissionGroupModel:

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
    tasks: List[MissionTaskModel]
    reset_type: str
    reset_day_of_month: int
    reset_day_of_week: str
    reset_hour: int
    complete_notification_namespace_id: str

    def __init__(
            self,
            name: str,
            reset_type: ResetType,
            metadata: str = None,
            tasks: List[MissionTaskModel] = None,
            reset_day_of_month: int = None,
            reset_day_of_week: ResetDayOfWeek = None,
            reset_hour: int = None,
            complete_notification_namespace_id: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.tasks = tasks
        self.reset_type = reset_type
        self.reset_day_of_month = reset_day_of_month
        self.reset_day_of_week = reset_day_of_week
        self.reset_hour = reset_hour
        self.complete_notification_namespace_id = complete_notification_namespace_id

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.tasks:
            properties["Tasks"] = [
                element.properties()
                for element in self.tasks
            ]
        if self.reset_type:
            properties["ResetType"] = self.reset_type
        if self.reset_day_of_month:
            properties["ResetDayOfMonth"] = self.reset_day_of_month
        if self.reset_day_of_week:
            properties["ResetDayOfWeek"] = self.reset_day_of_week
        if self.reset_hour:
            properties["ResetHour"] = self.reset_hour
        if self.complete_notification_namespace_id:
            properties["CompleteNotificationNamespaceId"] = self.complete_notification_namespace_id
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return MissionGroupModelRef(
            namespace_name=namespace_name,
            mission_group_name=self.name,
        )

    @staticmethod
    def not_reset(
        name: str = None,
        metadata: str = None,
        tasks: List[MissionTaskModel] = None,
        complete_notification_namespace_id: str = None,
    ) -> MissionGroupModel:
        return MissionGroupModel(
            reset_type=MissionGroupModel.ResetType.NOT_RESET,
            name=name,
            metadata=metadata,
            tasks=tasks,
            complete_notification_namespace_id=complete_notification_namespace_id,
        )

    @staticmethod
    def daily(
        reset_hour: int,
        name: str = None,
        metadata: str = None,
        tasks: List[MissionTaskModel] = None,
        complete_notification_namespace_id: str = None,
    ) -> MissionGroupModel:
        return MissionGroupModel(
            reset_type=MissionGroupModel.ResetType.DAILY,
            name=name,
            metadata=metadata,
            tasks=tasks,
            reset_hour=reset_hour,
            complete_notification_namespace_id=complete_notification_namespace_id,
        )

    @staticmethod
    def weekly(
        reset_day_of_week: str,
        reset_hour: int,
        name: str = None,
        metadata: str = None,
        tasks: List[MissionTaskModel] = None,
        complete_notification_namespace_id: str = None,
    ) -> MissionGroupModel:
        return MissionGroupModel(
            reset_type=MissionGroupModel.ResetType.WEEKLY,
            name=name,
            metadata=metadata,
            tasks=tasks,
            reset_day_of_week=reset_day_of_week,
            reset_hour=reset_hour,
            complete_notification_namespace_id=complete_notification_namespace_id,
        )

    @staticmethod
    def monthly(
        reset_day_of_month: int,
        reset_hour: int,
        name: str = None,
        metadata: str = None,
        tasks: List[MissionTaskModel] = None,
        complete_notification_namespace_id: str = None,
    ) -> MissionGroupModel:
        return MissionGroupModel(
            reset_type=MissionGroupModel.ResetType.MONTHLY,
            name=name,
            metadata=metadata,
            tasks=tasks,
            reset_day_of_month=reset_day_of_month,
            reset_hour=reset_hour,
            complete_notification_namespace_id=complete_notification_namespace_id,
        )


class MissionTaskModel:
    name: str
    metadata: str
    counter_name: str
    target_value: int
    complete_acquire_actions: List[AcquireAction]
    challenge_period_event_id: str
    premise_mission_task_name: str

    def __init__(
            self,
            name: str,
            counter_name: str,
            target_value: int,
            metadata: str = None,
            complete_acquire_actions: List[AcquireAction] = None,
            challenge_period_event_id: str = None,
            premise_mission_task_name: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.counter_name = counter_name
        self.target_value = target_value
        self.complete_acquire_actions = complete_acquire_actions
        self.challenge_period_event_id = challenge_period_event_id
        self.premise_mission_task_name = premise_mission_task_name

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.counter_name:
            properties["CounterName"] = self.counter_name
        if self.target_value:
            properties["TargetValue"] = self.target_value
        if self.complete_acquire_actions:
            properties["CompleteAcquireActions"] = [
                element.properties()
                for element in self.complete_acquire_actions
            ]
        if self.challenge_period_event_id:
            properties["ChallengePeriodEventId"] = self.challenge_period_event_id
        if self.premise_mission_task_name:
            properties["PremiseMissionTaskName"] = self.premise_mission_task_name
        return properties

    def ref(
            self,
            namespace_name: str,
            mission_group_name: str,
    ):
        return MissionTaskModelRef(
            namespace_name=namespace_name,
            mission_group_name=mission_group_name,
            mission_task_name=self.name,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-05-28'
    namespace_name: str
    mission_group_models: List[MissionGroupModel]
    counter_models: List[CounterModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            mission_group_models: List[MissionGroupModel],
            counter_models: List[CounterModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.mission_group_models = mission_group_models
        self.counter_models = counter_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Mission::CurrentMissionMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "mission_group_models": [
                    element.properties()
                    for element in self.mission_group_models
                ],
                "counter_models": [
                    element.properties()
                    for element in self.counter_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class CounterModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    metadata: str
    description: str
    scopes: List[CounterScopeModel]
    challenge_period_event_id: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            scopes: List[CounterScopeModel],
            metadata: str = None,
            description: str = None,
            challenge_period_event_id: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.metadata = metadata
        self.description = description
        self.scopes = scopes
        self.challenge_period_event_id = challenge_period_event_id

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Mission::CounterModelMaster"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.description:
            properties["Description"] = self.description
        if self.scopes:
            properties["Scopes"] = [
                element.properties()
                for element in self.scopes
            ]
        if self.challenge_period_event_id:
            properties["ChallengePeriodEventId"] = self.challenge_period_event_id
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return CounterModelMasterRef(
            namespace_name=namespace_name,
            counter_name=self.name,
        )

    def get_attr_counter_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.CounterId"
        )


class MissionGroupModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    metadata: str
    description: str
    reset_type: str
    reset_day_of_month: int
    reset_day_of_week: str
    reset_hour: int
    complete_notification_namespace_id: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            reset_type: str,
            reset_day_of_month: int,
            reset_day_of_week: str,
            reset_hour: int,
            metadata: str = None,
            description: str = None,
            complete_notification_namespace_id: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.metadata = metadata
        self.description = description
        self.reset_type = reset_type
        self.reset_day_of_month = reset_day_of_month
        self.reset_day_of_week = reset_day_of_week
        self.reset_hour = reset_hour
        self.complete_notification_namespace_id = complete_notification_namespace_id

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Mission::MissionGroupModelMaster"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.description:
            properties["Description"] = self.description
        if self.reset_type:
            properties["ResetType"] = self.reset_type
        if self.reset_day_of_month:
            properties["ResetDayOfMonth"] = self.reset_day_of_month
        if self.reset_day_of_week:
            properties["ResetDayOfWeek"] = self.reset_day_of_week
        if self.reset_hour:
            properties["ResetHour"] = self.reset_hour
        if self.complete_notification_namespace_id:
            properties["CompleteNotificationNamespaceId"] = self.complete_notification_namespace_id
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return MissionGroupModelMasterRef(
            namespace_name=namespace_name,
            mission_group_name=self.name,
        )

    def get_attr_mission_group_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.MissionGroupId"
        )


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    transaction_setting: TransactionSetting
    mission_complete_script: ScriptSetting
    counter_increment_script: ScriptSetting
    receive_rewards_script: ScriptSetting
    complete_notification: NotificationSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            transaction_setting: TransactionSetting,
            description: str = None,
            mission_complete_script: ScriptSetting = None,
            counter_increment_script: ScriptSetting = None,
            receive_rewards_script: ScriptSetting = None,
            complete_notification: NotificationSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.transaction_setting = transaction_setting
        self.mission_complete_script = mission_complete_script
        self.counter_increment_script = counter_increment_script
        self.receive_rewards_script = receive_rewards_script
        self.complete_notification = complete_notification
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Mission::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.transaction_setting:
            properties["TransactionSetting"] = self.transaction_setting.properties()
        if self.mission_complete_script:
            properties["MissionCompleteScript"] = self.mission_complete_script.properties()
        if self.counter_increment_script:
            properties["CounterIncrementScript"] = self.counter_increment_script.properties()
        if self.receive_rewards_script:
            properties["ReceiveRewardsScript"] = self.receive_rewards_script.properties()
        if self.complete_notification:
            properties["CompleteNotification"] = self.complete_notification.properties()
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
            mission_group_models: List[MissionGroupModel],
            counter_models: List[CounterModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            mission_group_models=mission_group_models,
            counter_models=counter_models,
        ).add_depends_on(
            self,
        )
        return self


class MissionTaskModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    mission_group_name: str
    name: str
    metadata: str
    description: str
    counter_name: str
    target_value: int
    complete_acquire_actions: List[AcquireAction]
    challenge_period_event_id: str
    premise_mission_task_name: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            mission_group_name: str,
            name: str,
            counter_name: str,
            target_value: int,
            metadata: str = None,
            description: str = None,
            complete_acquire_actions: List[AcquireAction] = None,
            challenge_period_event_id: str = None,
            premise_mission_task_name: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.mission_group_name = mission_group_name
        self.name = name
        self.metadata = metadata
        self.description = description
        self.counter_name = counter_name
        self.target_value = target_value
        self.complete_acquire_actions = complete_acquire_actions
        self.challenge_period_event_id = challenge_period_event_id
        self.premise_mission_task_name = premise_mission_task_name

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Mission::MissionTaskModelMaster"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.mission_group_name:
            properties["MissionGroupName"] = self.mission_group_name
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.description:
            properties["Description"] = self.description
        if self.counter_name:
            properties["CounterName"] = self.counter_name
        if self.target_value:
            properties["TargetValue"] = self.target_value
        if self.complete_acquire_actions:
            properties["CompleteAcquireActions"] = [
                element.properties()
                for element in self.complete_acquire_actions
            ]
        if self.challenge_period_event_id:
            properties["ChallengePeriodEventId"] = self.challenge_period_event_id
        if self.premise_mission_task_name:
            properties["PremiseMissionTaskName"] = self.premise_mission_task_name
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
            mission_group_name: str,
    ):
        return MissionTaskModelMasterRef(
            namespace_name=namespace_name,
            mission_group_name=mission_group_name,
            mission_task_name=self.name,
        )

    def get_attr_mission_task_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.MissionTaskId"
        )
