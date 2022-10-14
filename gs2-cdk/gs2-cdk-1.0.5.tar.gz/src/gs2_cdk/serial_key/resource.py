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


class CampaignModel:
    name: str
    metadata: str
    enable_campaign_code: bool

    def __init__(
            self,
            name: str,
            enable_campaign_code: bool,
            metadata: str = None,
    ):
        self.name = name
        self.metadata = metadata
        self.enable_campaign_code = enable_campaign_code

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.enable_campaign_code:
            properties["EnableCampaignCode"] = self.enable_campaign_code
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return CampaignModelRef(
            namespace_name=namespace_name,
            campaign_model_name=self.name,
        )


class CurrentMasterData(CdkResource):

    version: str = '2022-09-13'
    namespace_name: str
    campaign_models: List[CampaignModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            campaign_models: List[CampaignModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.campaign_models = campaign_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::SerialKey::CurrentCampaignMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "campaign_models": [
                    element.properties()
                    for element in self.campaign_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::SerialKey::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
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
            campaign_models: List[CampaignModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            campaign_models=campaign_models,
        ).add_depends_on(
            self,
        )
        return self


class CampaignModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    enable_campaign_code: bool

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            enable_campaign_code: bool,
            description: str = None,
            metadata: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.enable_campaign_code = enable_campaign_code

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::SerialKey::CampaignModelMaster"

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
        if self.enable_campaign_code:
            properties["EnableCampaignCode"] = self.enable_campaign_code
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return CampaignModelMasterRef(
            namespace_name=namespace_name,
            campaign_model_name=self.name,
        )

    def get_attr_campaign_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.CampaignId"
        )
