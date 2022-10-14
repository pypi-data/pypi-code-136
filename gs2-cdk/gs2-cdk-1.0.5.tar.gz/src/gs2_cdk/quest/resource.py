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


class QuestGroupModel:
    name: str
    metadata: str
    quests: List[QuestModel]
    challenge_period_event_id: str

    def __init__(
            self,
            name: str,
            metadata: str = None,
            quests: List[QuestModel] = None,
            challenge_period_event_id: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.quests = quests
        self.challenge_period_event_id = challenge_period_event_id

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.quests:
            properties["Quests"] = [
                element.properties()
                for element in self.quests
            ]
        if self.challenge_period_event_id:
            properties["ChallengePeriodEventId"] = self.challenge_period_event_id
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return QuestGroupModelRef(
            namespace_name=namespace_name,
            quest_group_name=self.name,
        )


class QuestModel:
    name: str
    metadata: str
    contents: List[Contents]
    challenge_period_event_id: str
    first_complete_acquire_actions: List[AcquireAction]
    consume_actions: List[ConsumeAction]
    failed_acquire_actions: List[AcquireAction]
    premise_quest_names: List[str]

    def __init__(
            self,
            name: str,
            contents: List[Contents],
            metadata: str = None,
            challenge_period_event_id: str = None,
            first_complete_acquire_actions: List[AcquireAction] = None,
            consume_actions: List[ConsumeAction] = None,
            failed_acquire_actions: List[AcquireAction] = None,
            premise_quest_names: List[str] = None,
    ):
        self.name = name
        self.metadata = metadata
        self.contents = contents
        self.challenge_period_event_id = challenge_period_event_id
        self.first_complete_acquire_actions = first_complete_acquire_actions
        self.consume_actions = consume_actions
        self.failed_acquire_actions = failed_acquire_actions
        self.premise_quest_names = premise_quest_names

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.contents:
            properties["Contents"] = [
                element.properties()
                for element in self.contents
            ]
        if self.challenge_period_event_id:
            properties["ChallengePeriodEventId"] = self.challenge_period_event_id
        if self.first_complete_acquire_actions:
            properties["FirstCompleteAcquireActions"] = [
                element.properties()
                for element in self.first_complete_acquire_actions
            ]
        if self.consume_actions:
            properties["ConsumeActions"] = [
                element.properties()
                for element in self.consume_actions
            ]
        if self.failed_acquire_actions:
            properties["FailedAcquireActions"] = [
                element.properties()
                for element in self.failed_acquire_actions
            ]
        if self.premise_quest_names:
            properties["PremiseQuestNames"] = [
                element
                for element in self.premise_quest_names
            ]
        return properties

    def ref(
            self,
            namespace_name: str,
            quest_group_name: str,
    ):
        return QuestModelRef(
            namespace_name=namespace_name,
            quest_group_name=quest_group_name,
            quest_name=self.name,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-05-14'
    namespace_name: str
    quest_group_models: List[QuestGroupModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            quest_group_models: List[QuestGroupModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.quest_group_models = quest_group_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Quest::CurrentQuestMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "quest_group_models": [
                    element.properties()
                    for element in self.quest_group_models
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
    start_quest_script: ScriptSetting
    complete_quest_script: ScriptSetting
    failed_quest_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            transaction_setting: TransactionSetting,
            description: str = None,
            start_quest_script: ScriptSetting = None,
            complete_quest_script: ScriptSetting = None,
            failed_quest_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.transaction_setting = transaction_setting
        self.start_quest_script = start_quest_script
        self.complete_quest_script = complete_quest_script
        self.failed_quest_script = failed_quest_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Quest::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.transaction_setting:
            properties["TransactionSetting"] = self.transaction_setting.properties()
        if self.start_quest_script:
            properties["StartQuestScript"] = self.start_quest_script.properties()
        if self.complete_quest_script:
            properties["CompleteQuestScript"] = self.complete_quest_script.properties()
        if self.failed_quest_script:
            properties["FailedQuestScript"] = self.failed_quest_script.properties()
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
            quest_group_models: List[QuestGroupModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            quest_group_models=quest_group_models,
        ).add_depends_on(
            self,
        )
        return self


class QuestGroupModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    challenge_period_event_id: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            description: str = None,
            metadata: str = None,
            challenge_period_event_id: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.challenge_period_event_id = challenge_period_event_id

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Quest::QuestGroupModelMaster"

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
        if self.challenge_period_event_id:
            properties["ChallengePeriodEventId"] = self.challenge_period_event_id
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return QuestGroupModelMasterRef(
            namespace_name=namespace_name,
            quest_group_name=self.name,
        )

    def get_attr_quest_group_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.QuestGroupModelId"
        )


class QuestModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    quest_group_name: str
    name: str
    description: str
    metadata: str
    contents: List[Contents]
    challenge_period_event_id: str
    first_complete_acquire_actions: List[AcquireAction]
    consume_actions: List[ConsumeAction]
    failed_acquire_actions: List[AcquireAction]
    premise_quest_names: List[str]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            quest_group_name: str,
            name: str,
            contents: List[Contents],
            description: str = None,
            metadata: str = None,
            challenge_period_event_id: str = None,
            first_complete_acquire_actions: List[AcquireAction] = None,
            consume_actions: List[ConsumeAction] = None,
            failed_acquire_actions: List[AcquireAction] = None,
            premise_quest_names: List[str] = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.quest_group_name = quest_group_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.contents = contents
        self.challenge_period_event_id = challenge_period_event_id
        self.first_complete_acquire_actions = first_complete_acquire_actions
        self.consume_actions = consume_actions
        self.failed_acquire_actions = failed_acquire_actions
        self.premise_quest_names = premise_quest_names

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Quest::QuestModelMaster"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        if self.quest_group_name:
            properties["QuestGroupName"] = self.quest_group_name
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.contents:
            properties["Contents"] = [
                element.properties()
                for element in self.contents
            ]
        if self.challenge_period_event_id:
            properties["ChallengePeriodEventId"] = self.challenge_period_event_id
        if self.first_complete_acquire_actions:
            properties["FirstCompleteAcquireActions"] = [
                element.properties()
                for element in self.first_complete_acquire_actions
            ]
        if self.consume_actions:
            properties["ConsumeActions"] = [
                element.properties()
                for element in self.consume_actions
            ]
        if self.failed_acquire_actions:
            properties["FailedAcquireActions"] = [
                element.properties()
                for element in self.failed_acquire_actions
            ]
        if self.premise_quest_names:
            properties["PremiseQuestNames"] = [
                element
                for element in self.premise_quest_names
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
            quest_group_name: str,
    ):
        return QuestModelMasterRef(
            namespace_name=namespace_name,
            quest_group_name=quest_group_name,
            quest_name=self.name,
        )

    def get_attr_quest_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.QuestModelId"
        )
