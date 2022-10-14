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
    change_password_if_take_over: bool
    different_user_id_for_login_and_data_retention: bool
    create_account_script: ScriptSetting
    authentication_script: ScriptSetting
    create_take_over_script: ScriptSetting
    do_take_over_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            change_password_if_take_over: bool,
            different_user_id_for_login_and_data_retention: bool,
            description: str = None,
            create_account_script: ScriptSetting = None,
            authentication_script: ScriptSetting = None,
            create_take_over_script: ScriptSetting = None,
            do_take_over_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.change_password_if_take_over = change_password_if_take_over
        self.different_user_id_for_login_and_data_retention = different_user_id_for_login_and_data_retention
        self.create_account_script = create_account_script
        self.authentication_script = authentication_script
        self.create_take_over_script = create_take_over_script
        self.do_take_over_script = do_take_over_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Account::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.change_password_if_take_over:
            properties["ChangePasswordIfTakeOver"] = self.change_password_if_take_over
        if self.different_user_id_for_login_and_data_retention:
            properties["DifferentUserIdForLoginAndDataRetention"] = self.different_user_id_for_login_and_data_retention
        if self.create_account_script:
            properties["CreateAccountScript"] = self.create_account_script.properties()
        if self.authentication_script:
            properties["AuthenticationScript"] = self.authentication_script.properties()
        if self.create_take_over_script:
            properties["CreateTakeOverScript"] = self.create_take_over_script.properties()
        if self.do_take_over_script:
            properties["DoTakeOverScript"] = self.do_take_over_script.properties()
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
