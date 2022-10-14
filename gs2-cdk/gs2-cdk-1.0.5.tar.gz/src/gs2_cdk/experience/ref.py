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

    def current_experience_master(
            self,
    ) -> CurrentExperienceMasterRef:
        return CurrentExperienceMasterRef(
            namespace_name=self.namespace_name,
        )

    def experience_model(
            self,
            experience_name: str,
    ) -> ExperienceModelRef:
        return ExperienceModelRef(
            namespace_name=self.namespace_name,
            experience_name=experience_name,
        )

    def threshold_master(
            self,
            threshold_name: str,
    ) -> ThresholdMasterRef:
        return ThresholdMasterRef(
            namespace_name=self.namespace_name,
            threshold_name=threshold_name,
        )

    def experience_model_master(
            self,
            experience_name: str,
    ) -> ExperienceModelMasterRef:
        return ExperienceModelMasterRef(
            namespace_name=self.namespace_name,
            experience_name=experience_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'experience',
                self.namespace_name,
            ],
        ).str()


class ExperienceModelMasterRef:
    namespace_name: str
    experience_name: str

    def __init__(
            self,
            namespace_name: str,
            experience_name: str,
    ):
        self.namespace_name = namespace_name
        self.experience_name = experience_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'experience',
                self.namespace_name,
                'model',
                self.experience_name,
            ],
        ).str()


class ExperienceModelRef:
    namespace_name: str
    experience_name: str

    def __init__(
            self,
            namespace_name: str,
            experience_name: str,
    ):
        self.namespace_name = namespace_name
        self.experience_name = experience_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'experience',
                self.namespace_name,
                'model',
                self.experience_name,
            ],
        ).str()


class ThresholdMasterRef:
    namespace_name: str
    threshold_name: str

    def __init__(
            self,
            namespace_name: str,
            threshold_name: str,
    ):
        self.namespace_name = namespace_name
        self.threshold_name = threshold_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'experience',
                self.namespace_name,
                'threshold',
                self.threshold_name,
            ],
        ).str()


class CurrentExperienceMasterRef:
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
                'experience',
                self.namespace_name,
            ],
        ).str()
