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


class RatingModel:
    name: str
    metadata: str
    volatility: int

    def __init__(
            self,
            name: str,
            volatility: int,
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.volatility = volatility

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.volatility:
            properties["Volatility"] = self.volatility
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return RatingModelRef(
            namespace_name=namespace_name,
            rating_name=self.name,
        )


class CurrentMasterData(CdkResource):

    version: str = '2020-06-24'
    namespace_name: str
    rating_models: List[RatingModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            rating_models: List[RatingModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.rating_models = rating_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Matchmaking::CurrentRatingModelMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "rating_models": [
                    element.properties()
                    for element in self.rating_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    enable_rating: bool
    create_gathering_trigger_type: str
    create_gathering_trigger_realtime_namespace_id: str
    create_gathering_trigger_script_id: str
    complete_matchmaking_trigger_type: str
    complete_matchmaking_trigger_realtime_namespace_id: str
    complete_matchmaking_trigger_script_id: str
    change_rating_script: ScriptSetting
    join_notification: NotificationSetting
    leave_notification: NotificationSetting
    complete_notification: NotificationSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            enable_rating: bool,
            create_gathering_trigger_type: str,
            create_gathering_trigger_realtime_namespace_id: str,
            create_gathering_trigger_script_id: str,
            complete_matchmaking_trigger_type: str,
            complete_matchmaking_trigger_realtime_namespace_id: str,
            complete_matchmaking_trigger_script_id: str,
            description: str = None,
            change_rating_script: ScriptSetting = None,
            join_notification: NotificationSetting = None,
            leave_notification: NotificationSetting = None,
            complete_notification: NotificationSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.enable_rating = enable_rating
        self.create_gathering_trigger_type = create_gathering_trigger_type
        self.create_gathering_trigger_realtime_namespace_id = create_gathering_trigger_realtime_namespace_id
        self.create_gathering_trigger_script_id = create_gathering_trigger_script_id
        self.complete_matchmaking_trigger_type = complete_matchmaking_trigger_type
        self.complete_matchmaking_trigger_realtime_namespace_id = complete_matchmaking_trigger_realtime_namespace_id
        self.complete_matchmaking_trigger_script_id = complete_matchmaking_trigger_script_id
        self.change_rating_script = change_rating_script
        self.join_notification = join_notification
        self.leave_notification = leave_notification
        self.complete_notification = complete_notification
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Matchmaking::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.enable_rating:
            properties["EnableRating"] = self.enable_rating
        if self.create_gathering_trigger_type:
            properties["CreateGatheringTriggerType"] = self.create_gathering_trigger_type
        if self.create_gathering_trigger_realtime_namespace_id:
            properties["CreateGatheringTriggerRealtimeNamespaceId"] = self.create_gathering_trigger_realtime_namespace_id
        if self.create_gathering_trigger_script_id:
            properties["CreateGatheringTriggerScriptId"] = self.create_gathering_trigger_script_id
        if self.complete_matchmaking_trigger_type:
            properties["CompleteMatchmakingTriggerType"] = self.complete_matchmaking_trigger_type
        if self.complete_matchmaking_trigger_realtime_namespace_id:
            properties["CompleteMatchmakingTriggerRealtimeNamespaceId"] = self.complete_matchmaking_trigger_realtime_namespace_id
        if self.complete_matchmaking_trigger_script_id:
            properties["CompleteMatchmakingTriggerScriptId"] = self.complete_matchmaking_trigger_script_id
        if self.change_rating_script:
            properties["ChangeRatingScript"] = self.change_rating_script.properties()
        if self.join_notification:
            properties["JoinNotification"] = self.join_notification.properties()
        if self.leave_notification:
            properties["LeaveNotification"] = self.leave_notification.properties()
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
            rating_models: List[RatingModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            rating_models=rating_models,
        ).add_depends_on(
            self,
        )
        return self


class Gathering(CdkResource):

    stack: Stack
    namespace_name: str
    user_id: str
    player: Player
    attribute_ranges: List[AttributeRange]
    capacity_of_roles: List[CapacityOfRole]
    allow_user_ids: List[str]
    expires_at: int
    expires_at_time_span: TimeSpan

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            user_id: str,
            player: Player,
            capacity_of_roles: List[CapacityOfRole],
            attribute_ranges: List[AttributeRange] = None,
            allow_user_ids: List[str] = None,
            expires_at: int = None,
            expires_at_time_span: TimeSpan = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.user_id = user_id
        self.player = player
        self.attribute_ranges = attribute_ranges
        self.capacity_of_roles = capacity_of_roles
        self.allow_user_ids = allow_user_ids
        self.expires_at = expires_at
        self.expires_at_time_span = expires_at_time_span

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Matchmaking::Gathering"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.player:
            properties["Player"] = self.player.properties()
        if self.attribute_ranges:
            properties["AttributeRanges"] = [
                element.properties()
                for element in self.attribute_ranges
            ]
        if self.capacity_of_roles:
            properties["CapacityOfRoles"] = [
                element.properties()
                for element in self.capacity_of_roles
            ]
        if self.allow_user_ids:
            properties["AllowUserIds"] = [
                element
                for element in self.allow_user_ids
            ]
        if self.expires_at:
            properties["ExpiresAt"] = self.expires_at
        if self.expires_at_time_span:
            properties["ExpiresAtTimeSpan"] = self.expires_at_time_span.properties()
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
            user_id: str,
    ):
        return GatheringRef(
            namespace_name=namespace_name,
            user_id=user_id,
            gathering_name=self.name,
        )

    def get_attr_gathering_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.GatheringId"
        )


class RatingModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    volatility: int

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            volatility: int,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.volatility = volatility

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Matchmaking::RatingModelMaster"

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
        if self.volatility:
            properties["Volatility"] = self.volatility
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return RatingModelMasterRef(
            namespace_name=namespace_name,
            rating_name=self.name,
        )

    def get_attr_rating_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.RatingModelId"
        )
