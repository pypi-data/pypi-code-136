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


class CounterModelMasterRef:
    namespace_name: str
    counter_name: str

    def __init__(
            self,
            namespace_name: str,
            counter_name: str,
    ):
        self.namespace_name = namespace_name
        self.counter_name = counter_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'mission',
                self.namespace_name,
                'counter',
                self.counter_name,
            ],
        ).str()


class MissionGroupModelMasterRef:
    namespace_name: str
    mission_group_name: str

    def __init__(
            self,
            namespace_name: str,
            mission_group_name: str,
    ):
        self.namespace_name = namespace_name
        self.mission_group_name = mission_group_name

    def mission_task_model_master(
            self,
            mission_task_name: str,
    ) -> MissionTaskModelMasterRef:
        return MissionTaskModelMasterRef(
            namespace_name=self.namespace_name,
            mission_group_name=self.mission_group_name,
            mission_task_name=mission_task_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'mission',
                self.namespace_name,
                'group',
                self.mission_group_name,
            ],
        ).str()


class NamespaceRef:
    namespace_name: str

    def __init__(
            self,
            namespace_name: str,
    ):
        self.namespace_name = namespace_name

    def current_mission_master(
            self,
    ) -> CurrentMissionMasterRef:
        return CurrentMissionMasterRef(
            namespace_name=self.namespace_name,
        )

    def mission_group_model(
            self,
            mission_group_name: str,
    ) -> MissionGroupModelRef:
        return MissionGroupModelRef(
            namespace_name=self.namespace_name,
            mission_group_name=mission_group_name,
        )

    def counter_model(
            self,
            counter_name: str,
    ) -> CounterModelRef:
        return CounterModelRef(
            namespace_name=self.namespace_name,
            counter_name=counter_name,
        )

    def mission_group_model_master(
            self,
            mission_group_name: str,
    ) -> MissionGroupModelMasterRef:
        return MissionGroupModelMasterRef(
            namespace_name=self.namespace_name,
            mission_group_name=mission_group_name,
        )

    def counter_model_master(
            self,
            counter_name: str,
    ) -> CounterModelMasterRef:
        return CounterModelMasterRef(
            namespace_name=self.namespace_name,
            counter_name=counter_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'mission',
                self.namespace_name,
            ],
        ).str()


class CurrentMissionMasterRef:
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
                'mission',
                self.namespace_name,
            ],
        ).str()


class CounterModelRef:
    namespace_name: str
    counter_name: str

    def __init__(
            self,
            namespace_name: str,
            counter_name: str,
    ):
        self.namespace_name = namespace_name
        self.counter_name = counter_name

    def increase_counter(
            self,
            value: int,
            user_id: str = '#{userId}',
    ) -> IncreaseCounterByUserId:
        return IncreaseCounterByUserId(
            namespace_name=self.namespace_name,
            counter_name=self.counter_name,
            user_id=user_id,
            value=value,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'mission',
                self.namespace_name,
                'counter',
                self.counter_name,
            ],
        ).str()


class MissionGroupModelRef:
    namespace_name: str
    mission_group_name: str

    def __init__(
            self,
            namespace_name: str,
            mission_group_name: str,
    ):
        self.namespace_name = namespace_name
        self.mission_group_name = mission_group_name

    def mission_task_model(
            self,
            mission_task_name: str,
    ) -> MissionTaskModelRef:
        return MissionTaskModelRef(
            namespace_name=self.namespace_name,
            mission_group_name=self.mission_group_name,
            mission_task_name=mission_task_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'mission',
                self.namespace_name,
                'group',
                self.mission_group_name,
            ],
        ).str()


class MissionTaskModelRef:
    namespace_name: str
    mission_group_name: str
    mission_task_name: str

    def __init__(
            self,
            namespace_name: str,
            mission_group_name: str,
            mission_task_name: str,
    ):
        self.namespace_name = namespace_name
        self.mission_group_name = mission_group_name
        self.mission_task_name = mission_task_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'mission',
                self.namespace_name,
                'group',
                self.mission_group_name,
                'missionTaskModel',
                self.mission_task_name,
            ],
        ).str()


class MissionTaskModelMasterRef:
    namespace_name: str
    mission_group_name: str
    mission_task_name: str

    def __init__(
            self,
            namespace_name: str,
            mission_group_name: str,
            mission_task_name: str,
    ):
        self.namespace_name = namespace_name
        self.mission_group_name = mission_group_name
        self.mission_task_name = mission_task_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'mission',
                self.namespace_name,
                'group',
                self.mission_group_name,
                'missionTaskModelMaster',
                self.mission_task_name,
            ],
        ).str()
