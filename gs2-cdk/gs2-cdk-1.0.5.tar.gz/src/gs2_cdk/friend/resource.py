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
    follow_script: ScriptSetting
    unfollow_script: ScriptSetting
    send_request_script: ScriptSetting
    cancel_request_script: ScriptSetting
    accept_request_script: ScriptSetting
    reject_request_script: ScriptSetting
    delete_friend_script: ScriptSetting
    update_profile_script: ScriptSetting
    follow_notification: NotificationSetting
    receive_request_notification: NotificationSetting
    accept_request_notification: NotificationSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            follow_script: ScriptSetting = None,
            unfollow_script: ScriptSetting = None,
            send_request_script: ScriptSetting = None,
            cancel_request_script: ScriptSetting = None,
            accept_request_script: ScriptSetting = None,
            reject_request_script: ScriptSetting = None,
            delete_friend_script: ScriptSetting = None,
            update_profile_script: ScriptSetting = None,
            follow_notification: NotificationSetting = None,
            receive_request_notification: NotificationSetting = None,
            accept_request_notification: NotificationSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.follow_script = follow_script
        self.unfollow_script = unfollow_script
        self.send_request_script = send_request_script
        self.cancel_request_script = cancel_request_script
        self.accept_request_script = accept_request_script
        self.reject_request_script = reject_request_script
        self.delete_friend_script = delete_friend_script
        self.update_profile_script = update_profile_script
        self.follow_notification = follow_notification
        self.receive_request_notification = receive_request_notification
        self.accept_request_notification = accept_request_notification
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Friend::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.follow_script:
            properties["FollowScript"] = self.follow_script.properties()
        if self.unfollow_script:
            properties["UnfollowScript"] = self.unfollow_script.properties()
        if self.send_request_script:
            properties["SendRequestScript"] = self.send_request_script.properties()
        if self.cancel_request_script:
            properties["CancelRequestScript"] = self.cancel_request_script.properties()
        if self.accept_request_script:
            properties["AcceptRequestScript"] = self.accept_request_script.properties()
        if self.reject_request_script:
            properties["RejectRequestScript"] = self.reject_request_script.properties()
        if self.delete_friend_script:
            properties["DeleteFriendScript"] = self.delete_friend_script.properties()
        if self.update_profile_script:
            properties["UpdateProfileScript"] = self.update_profile_script.properties()
        if self.follow_notification:
            properties["FollowNotification"] = self.follow_notification.properties()
        if self.receive_request_notification:
            properties["ReceiveRequestNotification"] = self.receive_request_notification.properties()
        if self.accept_request_notification:
            properties["AcceptRequestNotification"] = self.accept_request_notification.properties()
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
