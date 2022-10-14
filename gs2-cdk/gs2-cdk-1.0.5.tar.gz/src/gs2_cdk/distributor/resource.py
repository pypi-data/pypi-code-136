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


class DistributorModel:
    name: str
    metadata: str
    inbox_namespace_id: str
    white_list_target_ids: List[str]

    def __init__(
            self,
            name: str,
            metadata: str = None,
            inbox_namespace_id: str = None,
            white_list_target_ids: List[str] = None,
    ):
        self.name = name
        self.metadata = metadata
        self.inbox_namespace_id = inbox_namespace_id
        self.white_list_target_ids = white_list_target_ids

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.metadata:
            properties["Metadata"] = self.metadata
        if self.inbox_namespace_id:
            properties["InboxNamespaceId"] = self.inbox_namespace_id
        if self.white_list_target_ids:
            properties["WhiteListTargetIds"] = [
                element
                for element in self.white_list_target_ids
            ]
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return DistributorModelRef(
            namespace_name=namespace_name,
            distributor_name=self.name,
        )


class StampSheetResult:
    user_id: str
    transaction_id: str
    task_requests: List[ConsumeAction]
    sheet_request: AcquireAction
    task_results: List[str]
    sheet_result: str
    next_transaction_id: str
    created_at: int
    ttl_at: int

    def __init__(
            self,
            user_id: str,
            transaction_id: str,
            sheet_request: AcquireAction,
            created_at: int,
            ttl_at: int,
            task_requests: List[ConsumeAction] = None,
            task_results: List[str] = None,
            sheet_result: str = None,
            next_transaction_id: str = None,
    ):
        self.user_id = user_id
        self.transaction_id = transaction_id
        self.task_requests = task_requests
        self.sheet_request = sheet_request
        self.task_results = task_results
        self.sheet_result = sheet_result
        self.next_transaction_id = next_transaction_id
        self.created_at = created_at
        self.ttl_at = ttl_at

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.transaction_id:
            properties["TransactionId"] = self.transaction_id
        if self.task_requests:
            properties["TaskRequests"] = [
                element.properties()
                for element in self.task_requests
            ]
        if self.sheet_request:
            properties["SheetRequest"] = self.sheet_request.properties()
        if self.task_results:
            properties["TaskResults"] = [
                element
                for element in self.task_results
            ]
        if self.sheet_result:
            properties["SheetResult"] = self.sheet_result
        if self.next_transaction_id:
            properties["NextTransactionId"] = self.next_transaction_id
        if self.created_at:
            properties["CreatedAt"] = self.created_at
        if self.ttl_at:
            properties["TtlAt"] = self.ttl_at
        return properties

    def ref(
            self,
            namespace_name: str,
    ):
        return StampSheetResultRef(
            namespace_name=namespace_name,
            transaction_id=self.transactionId,
        )


class CurrentMasterData(CdkResource):

    version: str = '2019-03-01'
    namespace_name: str
    distributor_models: List[DistributorModel]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            distributor_models: List[DistributorModel],
            resource_name: str = None,
    ):
        self.namespace_name = namespace_name
        self.distributor_models = distributor_models

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Distributor::CurrentDistributorMaster"

    def properties(self) -> Dict[str, Any]:
        return {
            "NamespaceName": self.namespace_name,
            "Settings": {
                "version": self.version,
                "distributor_models": [
                    element.properties()
                    for element in self.distributor_models
                ],
            },
        }

    def alternate_keys(self) -> str:
        return self.namespace_name


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    assume_user_id: str
    auto_run_stamp_sheet_notification: NotificationSetting
    log_setting: LogSetting

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            assume_user_id: str = None,
            auto_run_stamp_sheet_notification: NotificationSetting = None,
            log_setting: LogSetting = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.assume_user_id = assume_user_id
        self.auto_run_stamp_sheet_notification = auto_run_stamp_sheet_notification
        self.log_setting = log_setting

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Distributor::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.assume_user_id:
            properties["AssumeUserId"] = self.assume_user_id
        if self.auto_run_stamp_sheet_notification:
            properties["AutoRunStampSheetNotification"] = self.auto_run_stamp_sheet_notification.properties()
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
            distributor_models: List[DistributorModel],
    ) -> Namespace:
        CurrentMasterData(
            stack=self.stack,
            namespace_name=self.name,
            distributor_models=distributor_models,
        ).add_depends_on(
            self,
        )
        return self


class DistributorModelMaster(CdkResource):

    stack: Stack
    namespace_name: str
    name: str
    description: str
    metadata: str
    inbox_namespace_id: str
    white_list_target_ids: List[str]

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            name: str,
            description: str = None,
            metadata: str = None,
            inbox_namespace_id: str = None,
            white_list_target_ids: List[str] = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name
        self.name = name
        self.description = description
        self.metadata = metadata
        self.inbox_namespace_id = inbox_namespace_id
        self.white_list_target_ids = white_list_target_ids

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Distributor::DistributorModelMaster"

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
        if self.inbox_namespace_id:
            properties["InboxNamespaceId"] = self.inbox_namespace_id
        if self.white_list_target_ids:
            properties["WhiteListTargetIds"] = [
                element
                for element in self.white_list_target_ids
            ]
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return DistributorModelMasterRef(
            namespace_name=namespace_name,
            distributor_name=self.name,
        )

    def get_attr_distributor_model_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.DistributorModelId"
        )
