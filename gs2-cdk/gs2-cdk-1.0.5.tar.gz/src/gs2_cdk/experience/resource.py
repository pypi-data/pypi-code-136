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


class ExperienceModel:
    name: str
    metadata: str
    default_experience: int
    default_rank_cap: int
    max_rank_cap: int
    rank_threshold: Threshold

    def __init__(
            self,
            name: str,
            default_experience: int,
            default_rank_cap: int,
            max_rank_cap: int,
            rank_threshold: Threshold,
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.default_experience = default_experience
        self.default_rank_cap = default_rank_cap
        self.max_rank_cap = max_rank_cap
        self.rank_threshold = rank_threshold

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.default_experience:
            properties["DefaultExperience"] = self.default_experience
        if self.default_rank_cap:
            properties["DefaultRankCap"] = self.default_rank_cap
        if self.max_rank_cap:
            properties["MaxRankCap"] = self.max_rank_cap
        if self.rank_threshold:
            properties["RankThreshold"] = self.rank_threshold.properties()
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return ExperienceModelRef(
            namespace_name=namespace_name,
            experience_name=self.name,
        )


class Threshold:
    metadata: str
    values: List[int]

    def __init__(
            self,
            values: List[int],
            metadata: str = None,
    ):
        self.metadata = metadata
        self.values = values

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.values:
            properties["Values"] = [
                element
                for element in self.values
            ]
        return properties


class CurrentMasterData(CdkResource):

    version: str = '2019-01-11'
    namespace_name: str
    experience_models: List[ExperienceModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            experience_models: List[ExperienceModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.experience_models = experience_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Experience::CurrentExperienceMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "experience_models": [
                    element.properties()
                    for element in self.experience_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    experience_cap_script_id: str
    change_experience_script: ScriptSetting
    change_rank_script: ScriptSetting
    change_rank_cap_script: ScriptSetting
    overflow_experience_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            experience_cap_script_id: str = None,
            change_experience_script: ScriptSetting = None,
            change_rank_script: ScriptSetting = None,
            change_rank_cap_script: ScriptSetting = None,
            overflow_experience_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.experience_cap_script_id = experience_cap_script_id
        self.change_experience_script = change_experience_script
        self.change_rank_script = change_rank_script
        self.change_rank_cap_script = change_rank_cap_script
        self.overflow_experience_script = overflow_experience_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Experience::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.experience_cap_script_id:
            properties["ExperienceCapScriptId"] = self.experience_cap_script_id
        if self.change_experience_script:
            properties["ChangeExperienceScript"] = self.change_experience_script.properties()
        if self.change_rank_script:
            properties["ChangeRankScript"] = self.change_rank_script.properties()
        if self.change_rank_cap_script:
            properties["ChangeRankCapScript"] = self.change_rank_cap_script.properties()
        if self.overflow_experience_script:
            properties["OverflowExperienceScript"] = self.overflow_experience_script.properties()
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
            experience_models: List[ExperienceModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            experience_models=experience_models,
        ).add_depends_on(
            self,
        )
        return self


class ExperienceModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    default_experience: int
    default_rank_cap: int
    max_rank_cap: int
    rank_threshold_name: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            default_experience: int,
            default_rank_cap: int,
            max_rank_cap: int,
            rank_threshold_name: str,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.default_experience = default_experience
        self.default_rank_cap = default_rank_cap
        self.max_rank_cap = max_rank_cap
        self.rank_threshold_name = rank_threshold_name

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Experience::ExperienceModelMaster"

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
        if self.default_experience:
            properties["DefaultExperience"] = self.default_experience
        if self.default_rank_cap:
            properties["DefaultRankCap"] = self.default_rank_cap
        if self.max_rank_cap:
            properties["MaxRankCap"] = self.max_rank_cap
        if self.rank_threshold_name:
            properties["RankThresholdName"] = self.rank_threshold_name
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return ExperienceModelMasterRef(
            namespace_name=namespace_name,
            experience_name=self.name,
        )

    def get_attr_experience_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.ExperienceModelId"
        )


class ThresholdMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    values: List[int]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            values: List[int],
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.values = values

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Experience::ThresholdMaster"

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
        if self.values:
            properties["Values"] = [
                element
                for element in self.values
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return ThresholdMasterRef(
            namespace_name=namespace_name,
            threshold_name=self.name,
        )

    def get_attr_threshold_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.ThresholdId"
        )
