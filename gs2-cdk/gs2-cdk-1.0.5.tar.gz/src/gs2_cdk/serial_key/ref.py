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

    def current_campaign_master(
            self,
    ) -> CurrentCampaignMasterRef:
        return CurrentCampaignMasterRef(
            namespace_name=self.namespace_name,
        )

    def campaign_model(
            self,
            campaign_model_name: str,
    ) -> CampaignModelRef:
        return CampaignModelRef(
            namespace_name=self.namespace_name,
            campaign_model_name=campaign_model_name,
        )

    def serial_key(
            self,
            serial_key_code: str,
    ) -> SerialKeyRef:
        return SerialKeyRef(
            namespace_name=self.namespace_name,
            serial_key_code=serial_key_code,
        )

    def campaign_model_master(
            self,
            campaign_model_name: str,
    ) -> CampaignModelMasterRef:
        return CampaignModelMasterRef(
            namespace_name=self.namespace_name,
            campaign_model_name=campaign_model_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'serialKey',
                self.namespace_name,
            ],
        ).str()


class IssueJobRef:
    namespace_name: str
    campaign_model_name: str
    issue_job_name: str

    def __init__(
            self,
            namespace_name: str,
            campaign_model_name: str,
            issue_job_name: str,
    ):
        self.namespace_name = namespace_name
        self.campaign_model_name = campaign_model_name
        self.issue_job_name = issue_job_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'serialKey',
                self.namespace_name,
                'master',
                'campaign',
                self.campaign_model_name,
                'issue',
                'job',
                self.issue_job_name,
            ],
        ).str()


class SerialKeyRef:
    namespace_name: str
    serial_key_code: str

    def __init__(
            self,
            namespace_name: str,
            serial_key_code: str,
    ):
        self.namespace_name = namespace_name
        self.serial_key_code = serial_key_code

    def use(
            self,
            code: str,
            user_id: str = '#{userId}',
    ) -> UseByUserId:
        return UseByUserId(
            namespace_name=self.namespace_name,
            user_id=user_id,
            code=code,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'serialKey',
                self.namespace_name,
                'serialKey',
                self.serial_key_code,
            ],
        ).str()


class CampaignModelRef:
    namespace_name: str
    campaign_model_name: str

    def __init__(
            self,
            namespace_name: str,
            campaign_model_name: str,
    ):
        self.namespace_name = namespace_name
        self.campaign_model_name = campaign_model_name

    def issue_job(
            self,
            issue_job_name: str,
    ) -> IssueJobRef:
        return IssueJobRef(
            namespace_name=self.namespace_name,
            campaign_model_name=self.campaign_model_name,
            issue_job_name=issue_job_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'serialKey',
                self.namespace_name,
                'master',
                'campaign',
                self.campaign_model_name,
            ],
        ).str()


class CampaignModelMasterRef:
    namespace_name: str
    campaign_model_name: str

    def __init__(
            self,
            namespace_name: str,
            campaign_model_name: str,
    ):
        self.namespace_name = namespace_name
        self.campaign_model_name = campaign_model_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'serialKey',
                self.namespace_name,
                'master',
                'campaign',
                self.campaign_model_name,
            ],
        ).str()


class CurrentCampaignMasterRef:
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
                'serialKey',
                self.namespace_name,
            ],
        ).str()
