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


class RateModel:

    class TimingType(Enum):
        IMMEDIATE = "immediate"
        AWAIT = "await"
    name: str
    metadata: str
    consume_actions: List[ConsumeAction]
    timing_type: str
    lock_time: int
    enable_skip: bool
    skip_consume_actions: List[ConsumeAction]
    acquire_actions: List[AcquireAction]

    def __init__(
            self,
            name: str,
            timing_type: TimingType,
            metadata: str = None,
            consume_actions: List[ConsumeAction] = None,
            lock_time: int = None,
            enable_skip: bool = None,
            skip_consume_actions: List[ConsumeAction] = None,
            acquire_actions: List[AcquireAction] = None,
    ):
        self.name = name
        self.metadata = metadata
        self.consume_actions = consume_actions
        self.timing_type = timing_type
        self.lock_time = lock_time
        self.enable_skip = enable_skip
        self.skip_consume_actions = skip_consume_actions
        self.acquire_actions = acquire_actions

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.consume_actions:
            properties["ConsumeActions"] = [
                element.properties()
                for element in self.consume_actions
            ]
        if self.timing_type:
            properties["TimingType"] = self.timing_type
        if self.lock_time:
            properties["LockTime"] = self.lock_time
        if self.enable_skip:
            properties["EnableSkip"] = self.enable_skip
        if self.skip_consume_actions:
            properties["SkipConsumeActions"] = [
                element.properties()
                for element in self.skip_consume_actions
            ]
        if self.acquire_actions:
            properties["AcquireActions"] = [
                element.properties()
                for element in self.acquire_actions
            ]
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return RateModelRef(
            namespace_name=namespace_name,
            rate_name=self.name,
        )

    @staticmethod
    def immediate(
        name: str = None,
        metadata: str = None,
        consume_actions: List[ConsumeAction] = None,
        skip_consume_actions: List[ConsumeAction] = None,
        acquire_actions: List[AcquireAction] = None,
    ) -> RateModel:
        return RateModel(
            timing_type=RateModel.TimingType.IMMEDIATE,
            name=name,
            metadata=metadata,
            consume_actions=consume_actions,
            skip_consume_actions=skip_consume_actions,
            acquire_actions=acquire_actions,
        )

    @staticmethod
    def await(
        lock_time: int,
        enable_skip: bool,
        name: str = None,
        metadata: str = None,
        consume_actions: List[ConsumeAction] = None,
        skip_consume_actions: List[ConsumeAction] = None,
        acquire_actions: List[AcquireAction] = None,
    ) -> RateModel:
        return RateModel(
            timing_type=RateModel.TimingType.AWAIT,
            name=name,
            metadata=metadata,
            consume_actions=consume_actions,
            lock_time=lock_time,
            enable_skip=enable_skip,
            skip_consume_actions=skip_consume_actions,
            acquire_actions=acquire_actions,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-08-19'
    namespace_name: str
    rate_models: List[RateModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            rate_models: List[RateModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.rate_models = rate_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Exchange::CurrentRateMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "rate_models": [
                    element.properties()
                    for element in self.rate_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    enable_await_exchange: bool
    enable_direct_exchange: bool
    transaction_setting: TransactionSetting
    exchange_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            enable_await_exchange: bool,
            enable_direct_exchange: bool,
            transaction_setting: TransactionSetting,
            description: str = None,
            exchange_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.enable_await_exchange = enable_await_exchange
        self.enable_direct_exchange = enable_direct_exchange
        self.transaction_setting = transaction_setting
        self.exchange_script = exchange_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Exchange::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.enable_await_exchange:
            properties["EnableAwaitExchange"] = self.enable_await_exchange
        if self.enable_direct_exchange:
            properties["EnableDirectExchange"] = self.enable_direct_exchange
        if self.transaction_setting:
            properties["TransactionSetting"] = self.transaction_setting.properties()
        if self.exchange_script:
            properties["ExchangeScript"] = self.exchange_script.properties()
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
            rate_models: List[RateModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            rate_models=rate_models,
        ).add_depends_on(
            self,
        )
        return self


class RateModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    timing_type: str
    lock_time: int
    enable_skip: bool
    skip_consume_actions: List[ConsumeAction]
    acquire_actions: List[AcquireAction]
    consume_actions: List[ConsumeAction]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            timing_type: str,
            lock_time: int,
            enable_skip: bool,
            description: str = None,
            metadata: str = None,
            skip_consume_actions: List[ConsumeAction] = None,
            acquire_actions: List[AcquireAction] = None,
            consume_actions: List[ConsumeAction] = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.timing_type = timing_type
        self.lock_time = lock_time
        self.enable_skip = enable_skip
        self.skip_consume_actions = skip_consume_actions
        self.acquire_actions = acquire_actions
        self.consume_actions = consume_actions

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Exchange::RateModelMaster"

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
        if self.timing_type:
            properties["TimingType"] = self.timing_type
        if self.lock_time:
            properties["LockTime"] = self.lock_time
        if self.enable_skip:
            properties["EnableSkip"] = self.enable_skip
        if self.skip_consume_actions:
            properties["SkipConsumeActions"] = [
                element.properties()
                for element in self.skip_consume_actions
            ]
        if self.acquire_actions:
            properties["AcquireActions"] = [
                element.properties()
                for element in self.acquire_actions
            ]
        if self.consume_actions:
            properties["ConsumeActions"] = [
                element.properties()
                for element in self.consume_actions
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return RateModelMasterRef(
            namespace_name=namespace_name,
            rate_name=self.name,
        )

    def get_attr_rate_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.RateModelId"
        )
