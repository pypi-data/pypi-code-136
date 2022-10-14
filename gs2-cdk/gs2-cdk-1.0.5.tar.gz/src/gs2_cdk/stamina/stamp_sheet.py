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
import json

from typing import List

from .model import *
from gs2_cdk import AcquireAction, ConsumeAction


class ConsumeStaminaByUserId(ConsumeAction):

    def __init__(
            self,
            namespace_name: str,
            stamina_name: str,
            consume_value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.stamina_name = stamina_name
        self.user_id = user_id
        self.consume_value = consume_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if stamina_name:
            properties["staminaName"] = stamina_name
        if user_id:
            properties["userId"] = user_id
        if consume_value:
            properties["consumeValue"] = consume_value

        super().__init__(
            action="Gs2Stamina:ConsumeStaminaByUserId",
            request=properties,
        )


class RecoverStaminaByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            stamina_name: str,
            recover_value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.stamina_name = stamina_name
        self.user_id = user_id
        self.recover_value = recover_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if stamina_name:
            properties["staminaName"] = stamina_name
        if user_id:
            properties["userId"] = user_id
        if recover_value:
            properties["recoverValue"] = recover_value

        super().__init__(
            action="Gs2Stamina:RecoverStaminaByUserId",
            request=properties,
        )


class RaiseMaxValueByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            stamina_name: str,
            raise_value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.stamina_name = stamina_name
        self.user_id = user_id
        self.raise_value = raise_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if stamina_name:
            properties["staminaName"] = stamina_name
        if user_id:
            properties["userId"] = user_id
        if raise_value:
            properties["raiseValue"] = raise_value

        super().__init__(
            action="Gs2Stamina:RaiseMaxValueByUserId",
            request=properties,
        )


class SetMaxValueByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            stamina_name: str,
            max_value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.stamina_name = stamina_name
        self.user_id = user_id
        self.max_value = max_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if stamina_name:
            properties["staminaName"] = stamina_name
        if user_id:
            properties["userId"] = user_id
        if max_value:
            properties["maxValue"] = max_value

        super().__init__(
            action="Gs2Stamina:SetMaxValueByUserId",
            request=properties,
        )


class SetRecoverIntervalByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            stamina_name: str,
            recover_interval_minutes: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.stamina_name = stamina_name
        self.user_id = user_id
        self.recover_interval_minutes = recover_interval_minutes

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if stamina_name:
            properties["staminaName"] = stamina_name
        if user_id:
            properties["userId"] = user_id
        if recover_interval_minutes:
            properties["recoverIntervalMinutes"] = recover_interval_minutes

        super().__init__(
            action="Gs2Stamina:SetRecoverIntervalByUserId",
            request=properties,
        )


class SetRecoverValueByUserId(AcquireAction):

    def __init__(
            self,
            namespace_name: str,
            stamina_name: str,
            recover_value: int,
            user_id: str = '#{userId}',
    ):
        self.namespace_name = namespace_name
        self.stamina_name = stamina_name
        self.user_id = user_id
        self.recover_value = recover_value

        properties = {}
        if namespace_name:
            properties["namespaceName"] = namespace_name
        if stamina_name:
            properties["staminaName"] = stamina_name
        if user_id:
            properties["userId"] = user_id
        if recover_value:
            properties["recoverValue"] = recover_value

        super().__init__(
            action="Gs2Stamina:SetRecoverValueByUserId",
            request=properties,
        )
