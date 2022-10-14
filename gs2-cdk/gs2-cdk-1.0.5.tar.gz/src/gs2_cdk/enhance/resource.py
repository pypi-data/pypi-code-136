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
    name: str
    description: str
    metadata: str
    target_inventory_model_id: str
    acquire_experience_suffix: str
    material_inventory_model_id: str
    acquire_experience_hierarchy: List[str]
    experience_model_id: str
    bonus_rates: List[BonusRate]

    def __init__(
            self,
            name: str,
            target_inventory_model_id: str,
            acquire_experience_suffix: str,
            material_inventory_model_id: str,
            experience_model_id: str,
            description: str = None,
            metadata: str = None,
            acquire_experience_hierarchy: List[str] = None,
            bonus_rates: List[BonusRate] = None,
    ):
        self.name = name
        self.description = description
        self.metadata = metadata
        self.target_inventory_model_id = target_inventory_model_id
        self.acquire_experience_suffix = acquire_experience_suffix
        self.material_inventory_model_id = material_inventory_model_id
        self.acquire_experience_hierarchy = acquire_experience_hierarchy
        self.experience_model_id = experience_model_id
        self.bonus_rates = bonus_rates

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.target_inventory_model_id:
            properties["TargetInventoryModelId"] = self.target_inventory_model_id
        if self.acquire_experience_suffix:
            properties["AcquireExperienceSuffix"] = self.acquire_experience_suffix
        if self.material_inventory_model_id:
            properties["MaterialInventoryModelId"] = self.material_inventory_model_id
        if self.acquire_experience_hierarchy:
            properties["AcquireExperienceHierarchy"] = [
                element
                for element in self.acquire_experience_hierarchy
            ]
        if self.experience_model_id:
            properties["ExperienceModelId"] = self.experience_model_id
        if self.bonus_rates:
            properties["BonusRates"] = [
                element.properties()
                for element in self.bonus_rates
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


class CurrentMasterData(CdkResource):

    version: str = '2020-08-22'
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
        return "GS2::Enhance::CurrentRateMaster"

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
    enable_direct_enhance: bool
    transaction_setting: TransactionSetting
    enhance_script: ScriptSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            enable_direct_enhance: bool,
            transaction_setting: TransactionSetting,
            description: str = None,
            enhance_script: ScriptSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.enable_direct_enhance = enable_direct_enhance
        self.transaction_setting = transaction_setting
        self.enhance_script = enhance_script
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Enhance::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.enable_direct_enhance:
            properties["EnableDirectEnhance"] = self.enable_direct_enhance
        if self.transaction_setting:
            properties["TransactionSetting"] = self.transaction_setting.properties()
        if self.enhance_script:
            properties["EnhanceScript"] = self.enhance_script.properties()
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
    target_inventory_model_id: str
    acquire_experience_suffix: str
    material_inventory_model_id: str
    acquire_experience_hierarchy: List[str]
    experience_model_id: str
    bonus_rates: List[BonusRate]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            target_inventory_model_id: str,
            acquire_experience_suffix: str,
            material_inventory_model_id: str,
            experience_model_id: str,
            description: str = None,
            metadata: str = None,
            acquire_experience_hierarchy: List[str] = None,
            bonus_rates: List[BonusRate] = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.target_inventory_model_id = target_inventory_model_id
        self.acquire_experience_suffix = acquire_experience_suffix
        self.material_inventory_model_id = material_inventory_model_id
        self.acquire_experience_hierarchy = acquire_experience_hierarchy
        self.experience_model_id = experience_model_id
        self.bonus_rates = bonus_rates

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Enhance::RateModelMaster"

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
        if self.target_inventory_model_id:
            properties["TargetInventoryModelId"] = self.target_inventory_model_id
        if self.acquire_experience_suffix:
            properties["AcquireExperienceSuffix"] = self.acquire_experience_suffix
        if self.material_inventory_model_id:
            properties["MaterialInventoryModelId"] = self.material_inventory_model_id
        if self.acquire_experience_hierarchy:
            properties["AcquireExperienceHierarchy"] = [
                element
                for element in self.acquire_experience_hierarchy
            ]
        if self.experience_model_id:
            properties["ExperienceModelId"] = self.experience_model_id
        if self.bonus_rates:
            properties["BonusRates"] = [
                element.properties()
                for element in self.bonus_rates
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
