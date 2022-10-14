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


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    allow_create_room: bool
    post_message_script: ScriptSetting
    create_room_script: ScriptSetting
    delete_room_script: ScriptSetting
    subscribe_room_script: ScriptSetting
    unsubscribe_room_script: ScriptSetting
    post_notification: NotificationSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            allow_create_room: bool,
            description: str = None,
            post_message_script: ScriptSetting = None,
            create_room_script: ScriptSetting = None,
            delete_room_script: ScriptSetting = None,
            subscribe_room_script: ScriptSetting = None,
            unsubscribe_room_script: ScriptSetting = None,
            post_notification: NotificationSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.allow_create_room = allow_create_room
        self.post_message_script = post_message_script
        self.create_room_script = create_room_script
        self.delete_room_script = delete_room_script
        self.subscribe_room_script = subscribe_room_script
        self.unsubscribe_room_script = unsubscribe_room_script
        self.post_notification = post_notification
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Chat::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.allow_create_room:
            properties["AllowCreateRoom"] = self.allow_create_room
        if self.post_message_script:
            properties["PostMessageScript"] = self.post_message_script.properties()
        if self.create_room_script:
            properties["CreateRoomScript"] = self.create_room_script.properties()
        if self.delete_room_script:
            properties["DeleteRoomScript"] = self.delete_room_script.properties()
        if self.subscribe_room_script:
            properties["SubscribeRoomScript"] = self.subscribe_room_script.properties()
        if self.unsubscribe_room_script:
            properties["UnsubscribeRoomScript"] = self.unsubscribe_room_script.properties()
        if self.post_notification:
            properties["PostNotification"] = self.post_notification.properties()
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
