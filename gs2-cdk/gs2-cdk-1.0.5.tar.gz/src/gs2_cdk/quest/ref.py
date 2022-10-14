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
from .model import *
from .stamp_sheet import *

from typing import List


class NamespaceRef:
    namespace_name: str

    def __init__(
            self,
            namespace_name: str,
    ):
        self.namespace_name = namespace_name

    def current_quest_master(
            self,
    ) -> CurrentQuestMasterRef:
        return CurrentQuestMasterRef(
            namespace_name=self.namespace_name,
        )

    def quest_group_model(
            self,
            quest_group_name: str,
    ) -> QuestGroupModelRef:
        return QuestGroupModelRef(
            namespace_name=self.namespace_name,
            quest_group_name=quest_group_name,
        )

    def quest_group_model_master(
            self,
            quest_group_name: str,
    ) -> QuestGroupModelMasterRef:
        return QuestGroupModelMasterRef(
            namespace_name=self.namespace_name,
            quest_group_name=quest_group_name,
        )

    def create_progress(
            self,
            quest_model_id: str,
            force: bool,
            config: List[Config] = None,
            user_id: str = '#{userId}',
    ) -> CreateProgressByUserId:
        return CreateProgressByUserId(
            namespace_name=self.namespace_name,
            user_id=user_id,
            quest_model_id=quest_model_id,
            force=force,
            config=config,
        )

    def delete_progress(
            self,
            user_id: str = '#{userId}',
    ) -> DeleteProgressByUserId:
        return DeleteProgressByUserId(
            namespace_name=self.namespace_name,
            user_id=user_id,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'quest',
                self.namespace_name,
            ],
        ).str()


class QuestGroupModelMasterRef:
    namespace_name: str
    quest_group_name: str

    def __init__(
            self,
            namespace_name: str,
            quest_group_name: str,
    ):
        self.namespace_name = namespace_name
        self.quest_group_name = quest_group_name

    def quest_model_master(
            self,
            quest_name: str,
    ) -> QuestModelMasterRef:
        return QuestModelMasterRef(
            namespace_name=self.namespace_name,
            quest_group_name=self.quest_group_name,
            quest_name=quest_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'quest',
                self.namespace_name,
                'group',
                self.quest_group_name,
            ],
        ).str()


class QuestModelMasterRef:
    namespace_name: str
    quest_group_name: str
    quest_name: str

    def __init__(
            self,
            namespace_name: str,
            quest_group_name: str,
            quest_name: str,
    ):
        self.namespace_name = namespace_name
        self.quest_group_name = quest_group_name
        self.quest_name = quest_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'quest',
                self.namespace_name,
                'group',
                self.quest_group_name,
                'quest',
                self.quest_name,
            ],
        ).str()


class CurrentQuestMasterRef:
    namespace_name: str

    def __init__(
            self,
            namespace_name: str,
    ):
        self.namespace_name = namespace_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'quest',
                self.namespace_name,
            ],
        ).str()


class QuestGroupModelRef:
    namespace_name: str
    quest_group_name: str

    def __init__(
            self,
            namespace_name: str,
            quest_group_name: str,
    ):
        self.namespace_name = namespace_name
        self.quest_group_name = quest_group_name

    def quest_model(
            self,
            quest_name: str,
    ) -> QuestModelRef:
        return QuestModelRef(
            namespace_name=self.namespace_name,
            quest_group_name=self.quest_group_name,
            quest_name=quest_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'quest',
                self.namespace_name,
                'group',
                self.quest_group_name,
            ],
        ).str()


class QuestModelRef:
    namespace_name: str
    quest_group_name: str
    quest_name: str

    def __init__(
            self,
            namespace_name: str,
            quest_group_name: str,
            quest_name: str,
    ):
        self.namespace_name = namespace_name
        self.quest_group_name = quest_group_name
        self.quest_name = quest_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'quest',
                self.namespace_name,
                'group',
                self.quest_group_name,
                'quest',
                self.quest_name,
            ],
        ).str()
