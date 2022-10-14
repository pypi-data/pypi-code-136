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


class GlobalMessage:
    name: str
    metadata: str
    read_acquire_actions: List[AcquireAction]
    expires_time_span: TimeSpan
    expires_at: int

    def __init__(
            self,
            name: str,
            metadata: str,
            read_acquire_actions: List[AcquireAction] = None,
            expires_time_span: TimeSpan = None,
            expires_at: int = None,
    ):
        self.name = name
        self.metadata = metadata
        self.read_acquire_actions = read_acquire_actions
        self.expires_time_span = expires_time_span
        self.expires_at = expires_at

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.read_acquire_actions:
            properties["ReadAcquireActions"] = [
                element.properties()
                for element in self.read_acquire_actions
            ]
        if self.expires_time_span:
            properties["ExpiresTimeSpan"] = self.expires_time_span.properties()
        if self.expires_at:
            properties["ExpiresAt"] = self.expires_at
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return GlobalMessageRef(
            namespace_name=namespace_name,
            global_message_name=self.name,
        )


class CurrentMasterData(CdkResource):

    version: str = '2020-03-12'
    namespace_name: str
    global_messages: List[GlobalMessage]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            global_messages: List[GlobalMessage],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.global_messages = global_messages

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Inbox::CurrentMessageMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "global_messages": [
                    element.properties()
                    for element in self.global_messages
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    is_automatic_deleting_enabled: bool
    transaction_setting: TransactionSetting
    receive_message_script: ScriptSetting
    read_message_script: ScriptSetting
    delete_message_script: ScriptSetting
    receive_notification: NotificationSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            is_automatic_deleting_enabled: bool = None,
            transaction_setting: TransactionSetting = None,
            receive_message_script: ScriptSetting = None,
            read_message_script: ScriptSetting = None,
            delete_message_script: ScriptSetting = None,
            receive_notification: NotificationSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.is_automatic_deleting_enabled = is_automatic_deleting_enabled
        self.transaction_setting = transaction_setting
        self.receive_message_script = receive_message_script
        self.read_message_script = read_message_script
        self.delete_message_script = delete_message_script
        self.receive_notification = receive_notification
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Inbox::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.is_automatic_deleting_enabled:
            properties["IsAutomaticDeletingEnabled"] = self.is_automatic_deleting_enabled
        if self.transaction_setting:
            properties["TransactionSetting"] = self.transaction_setting.properties()
        if self.receive_message_script:
            properties["ReceiveMessageScript"] = self.receive_message_script.properties()
        if self.read_message_script:
            properties["ReadMessageScript"] = self.read_message_script.properties()
        if self.delete_message_script:
            properties["DeleteMessageScript"] = self.delete_message_script.properties()
        if self.receive_notification:
            properties["ReceiveNotification"] = self.receive_notification.properties()
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
            global_messages: List[GlobalMessage],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            global_messages=global_messages,
        ).add_depends_on(
            self,
        )
        return self


class GlobalMessageMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    metadata: str
    read_acquire_actions: List[AcquireAction]
    expires_time_span: TimeSpan
    expires_at: int

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            metadata: str,
            read_acquire_actions: List[AcquireAction] = None,
            expires_time_span: TimeSpan = None,
            expires_at: int = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.metadata = metadata
        self.read_acquire_actions = read_acquire_actions
        self.expires_time_span = expires_time_span
        self.expires_at = expires_at

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Inbox::GlobalMessageMaster"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.read_acquire_actions:
            properties["ReadAcquireActions"] = [
                element.properties()
                for element in self.read_acquire_actions
            ]
        if self.expires_time_span:
            properties["ExpiresTimeSpan"] = self.expires_time_span.properties()
        if self.expires_at:
            properties["ExpiresAt"] = self.expires_at
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return GlobalMessageMasterRef(
            namespace_name=namespace_name,
            global_message_name=self.name,
        )

    def get_attr_global_message_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.GlobalMessageId"
        )
