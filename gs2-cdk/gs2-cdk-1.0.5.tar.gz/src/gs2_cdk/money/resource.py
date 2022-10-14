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
    priority: str
    share_free: bool
    currency: str
    apple_key: str
    google_key: str
    enable_fake_receipt: bool
    create_wallet_script: ScriptSetting
    deposit_script: ScriptSetting
    withdraw_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            priority: str,
            share_free: bool,
            currency: str,
            enable_fake_receipt: bool,
            description: str = None,
            apple_key: str = None,
            google_key: str = None,
            create_wallet_script: ScriptSetting = None,
            deposit_script: ScriptSetting = None,
            withdraw_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.priority = priority
        self.share_free = share_free
        self.currency = currency
        self.apple_key = apple_key
        self.google_key = google_key
        self.enable_fake_receipt = enable_fake_receipt
        self.create_wallet_script = create_wallet_script
        self.deposit_script = deposit_script
        self.withdraw_script = withdraw_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Money::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.priority:
            properties["Priority"] = self.priority
        if self.share_free:
            properties["ShareFree"] = self.share_free
        if self.currency:
            properties["Currency"] = self.currency
        if self.apple_key:
            properties["AppleKey"] = self.apple_key
        if self.google_key:
            properties["GoogleKey"] = self.google_key
        if self.enable_fake_receipt:
            properties["EnableFakeReceipt"] = self.enable_fake_receipt
        if self.create_wallet_script:
            properties["CreateWalletScript"] = self.create_wallet_script.properties()
        if self.deposit_script:
            properties["DepositScript"] = self.deposit_script.properties()
        if self.withdraw_script:
            properties["WithdrawScript"] = self.withdraw_script.properties()
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
