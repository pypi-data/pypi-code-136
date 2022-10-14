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


class Namespace(CdkResource):

    stack: Stack
    name: str
    description: str
    type: str
    gcp_credential_json: str
    big_query_dataset_name: str
    log_expire_days: int
    aws_region: str
    aws_access_key_id: str
    aws_secret_access_key: str
    firehose_stream_name: str

    def __init__(
            self,
            stack: Stack,
            name: str,
            type: str,
            gcp_credential_json: str,
            big_query_dataset_name: str,
            log_expire_days: int,
            aws_region: str,
            aws_access_key_id: str,
            aws_secret_access_key: str,
            firehose_stream_name: str,
            description: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.type = type
        self.gcp_credential_json = gcp_credential_json
        self.big_query_dataset_name = big_query_dataset_name
        self.log_expire_days = log_expire_days
        self.aws_region = aws_region
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.firehose_stream_name = firehose_stream_name

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Log::Namespace"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.description:
            properties["Description"] = self.description
        if self.type:
            properties["Type"] = self.type
        if self.gcp_credential_json:
            properties["GcpCredentialJson"] = self.gcp_credential_json
        if self.big_query_dataset_name:
            properties["BigQueryDatasetName"] = self.big_query_dataset_name
        if self.log_expire_days:
            properties["LogExpireDays"] = self.log_expire_days
        if self.aws_region:
            properties["AwsRegion"] = self.aws_region
        if self.aws_access_key_id:
            properties["AwsAccessKeyId"] = self.aws_access_key_id
        if self.aws_secret_access_key:
            properties["AwsSecretAccessKey"] = self.aws_secret_access_key
        if self.firehose_stream_name:
            properties["FirehoseStreamName"] = self.firehose_stream_name
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


class Insight(CdkResource):

    stack: Stack
    namespace_name: str

    def __init__(
            self,
            stack: Stack,
            namespace_name: str,
            resource_name: str = None,
    ):
        self.stack = stack
        self.namespace_name = namespace_name

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Log::Insight"

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.namespace_name:
            properties["NamespaceName"] = self.namespace_name
        return properties

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
            namespace_name: str,
    ):
        return InsightRef(
            namespace_name=namespace_name,
            insight_name=self.name,
        )

    def get_attr_insight_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.InsightId"
        )
