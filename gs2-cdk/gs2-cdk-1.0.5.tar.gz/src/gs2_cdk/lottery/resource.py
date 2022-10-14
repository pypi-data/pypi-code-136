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


class LotteryModel:

    class Mode(Enum):
        NORMAL = "normal"
        BOX = "box"

    class Method(Enum):
        PRIZE_TABLE = "prize_table"
        SCRIPT = "script"
    name: str
    metadata: str
    mode: str
    method: str
    prize_table_name: str
    choice_prize_table_script_id: str

    def __init__(
            self,
            name: str,
            mode: Mode,
            method: Method,
            metadata: str = None,
            prize_table_name: str = None,
            choice_prize_table_script_id: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.mode = mode
        self.method = method
        self.prize_table_name = prize_table_name
        self.choice_prize_table_script_id = choice_prize_table_script_id

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.mode:
            properties["Mode"] = self.mode
        if self.method:
            properties["Method"] = self.method
        if self.prize_table_name:
            properties["PrizeTableName"] = self.prize_table_name
        if self.choice_prize_table_script_id:
            properties["ChoicePrizeTableScriptId"] = self.choice_prize_table_script_id
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return LotteryModelRef(
            namespace_name=namespace_name,
            lottery_name=self.name,
        )

    @staticmethod
    def prize_table(
        prize_table_name: str,
        name: str = None,
        metadata: str = None,
        mode: str = None,
    ) -> LotteryModel:
        return LotteryModel(
            method=LotteryModel.Method.PRIZE_TABLE,
            name=name,
            metadata=metadata,
            mode=mode,
            prize_table_name=prize_table_name,
        )

    @staticmethod
    def script(
        choice_prize_table_script_id: str,
        name: str = None,
        metadata: str = None,
        mode: str = None,
    ) -> LotteryModel:
        return LotteryModel(
            method=LotteryModel.Method.SCRIPT,
            name=name,
            metadata=metadata,
            mode=mode,
            choice_prize_table_script_id=choice_prize_table_script_id,
        )


class PrizeTable:
    name: str
    metadata: str
    prizes: List[Prize]

    def __init__(
            self,
            name: str,
            prizes: List[Prize],
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.prizes = prizes

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.prizes:
            properties["Prizes"] = [
                element.properties()
                for element in self.prizes
            ]
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return PrizeTableRef(
            namespace_name=namespace_name,
            prize_table_name=self.name,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-02-21'
    namespace_name: str
    lottery_models: List[LotteryModel]
    prize_tables: List[PrizeTable]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            lottery_models: List[LotteryModel],
            prize_tables: List[PrizeTable],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.lottery_models = lottery_models
        self.prize_tables = prize_tables

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Lottery::CurrentLotteryMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "lottery_models": [
                    element.properties()
                    for element in self.lottery_models
                ],
                "prize_tables": [
                    element.properties()
                    for element in self.prize_tables
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    transaction_setting: TransactionSetting
    lottery_trigger_script_id: str
    choice_prize_table_script_id: str
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            transaction_setting: TransactionSetting,
            description: str = None,
            lottery_trigger_script_id: str = None,
            choice_prize_table_script_id: str = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.transaction_setting = transaction_setting
        self.lottery_trigger_script_id = lottery_trigger_script_id
        self.choice_prize_table_script_id = choice_prize_table_script_id
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Lottery::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.transaction_setting:
            properties["TransactionSetting"] = self.transaction_setting.properties()
        if self.lottery_trigger_script_id:
            properties["LotteryTriggerScriptId"] = self.lottery_trigger_script_id
        if self.choice_prize_table_script_id:
            properties["ChoicePrizeTableScriptId"] = self.choice_prize_table_script_id
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
            lottery_models: List[LotteryModel],
            prize_tables: List[PrizeTable],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            lottery_models=lottery_models,
            prize_tables=prize_tables,
        ).add_depends_on(
            self,
        )
        return self


class LotteryModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    mode: str
    method: str
    prize_table_name: str
    choice_prize_table_script_id: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            mode: str,
            method: str,
            prize_table_name: str,
            choice_prize_table_script_id: str,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.mode = mode
        self.method = method
        self.prize_table_name = prize_table_name
        self.choice_prize_table_script_id = choice_prize_table_script_id

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Lottery::LotteryModelMaster"

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
        if self.mode:
            properties["Mode"] = self.mode
        if self.method:
            properties["Method"] = self.method
        if self.prize_table_name:
            properties["PrizeTableName"] = self.prize_table_name
        if self.choice_prize_table_script_id:
            properties["ChoicePrizeTableScriptId"] = self.choice_prize_table_script_id
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return LotteryModelMasterRef(
            namespace_name=namespace_name,
            lottery_name=self.name,
        )

    def get_attr_lottery_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.LotteryModelId"
        )


class PrizeTableMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    prizes: List[Prize]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            prizes: List[Prize],
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.prizes = prizes

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Lottery::PrizeTableMaster"

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
        if self.prizes:
            properties["Prizes"] = [
                element.properties()
                for element in self.prizes
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return PrizeTableMasterRef(
            namespace_name=namespace_name,
            prize_table_name=self.name,
        )

    def get_attr_prize_table_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.PrizeTableId"
        )
