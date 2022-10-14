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
    server_type: str
    server_spec: str
    create_notification: NotificationSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            server_type: str,
            server_spec: str,
            description: str = None,
            create_notification: NotificationSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.server_type = server_type
        self.server_spec = server_spec
        self.create_notification = create_notification
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Realtime::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.server_type:
            properties["ServerType"] = self.server_type
        if self.server_spec:
            properties["ServerSpec"] = self.server_spec
        if self.create_notification:
            properties["CreateNotification"] = self.create_notification.properties()
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


class Room(CdkResource):

    stack: Stack
    owner_id: str
    namespace_name: str
    name: str
    ip_address: str
    port: int
    encryption_key: str

    def __init__(
            self,
            stack: Stack,
            owner_id: str,
            namespace_name: str,
            name: str,
            ip_address: str = None,
            port: int = None,
            encryption_key: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.owner_id = owner_id
        self.namespace_name = namespace_name
        self.name = name
        self.ip_address = ip_address
        self.port = port
        self.encryption_key = encryption_key

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Realtime::Room"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.owner_id:
            properties["OwnerId"] = self.owner_id
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.name:
            properties["Name"] = self.name
        if self.ip_address:
            properties["IpAddress"] = self.ip_address
        if self.port:
            properties["Port"] = self.port
        if self.encryption_key:
            properties["EncryptionKey"] = self.encryption_key
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return RoomRef(
            namespace_name=namespace_name,
            room_name=self.name,
        )

    def get_attr_room_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.RoomId"
        )
