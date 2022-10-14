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

    def current_form_master(
            self,
    ) -> CurrentFormMasterRef:
        return CurrentFormMasterRef(
            namespace_name=self.namespace_name,
        )

    def form_model(
            self,
            form_model_name: str,
    ) -> FormModelRef:
        return FormModelRef(
            namespace_name=self.namespace_name,
            form_model_name=form_model_name,
        )

    def mold_model(
            self,
            mold_name: str,
    ) -> MoldModelRef:
        return MoldModelRef(
            namespace_name=self.namespace_name,
            mold_name=mold_name,
        )

    def form_model_master(
            self,
            form_model_name: str,
    ) -> FormModelMasterRef:
        return FormModelMasterRef(
            namespace_name=self.namespace_name,
            form_model_name=form_model_name,
        )

    def mold_model_master(
            self,
            mold_name: str,
    ) -> MoldModelMasterRef:
        return MoldModelMasterRef(
            namespace_name=self.namespace_name,
            mold_name=mold_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'formation',
                self.namespace_name,
            ],
        ).str()


class FormModelRef:
    namespace_name: str
    form_model_name: str

    def __init__(
            self,
            namespace_name: str,
            form_model_name: str,
    ):
        self.namespace_name = namespace_name
        self.form_model_name = form_model_name

    def acquire_actions_to_form_properties(
            self,
            mold_name: str,
            index: int,
            acquire_action: AcquireAction,
            config: List[AcquireActionConfig] = None,
            user_id: str = '#{userId}',
    ) -> AcquireActionsToFormProperties:
        return AcquireActionsToFormProperties(
            namespace_name=self.namespace_name,
            user_id=user_id,
            mold_name=mold_name,
            index=index,
            acquire_action=acquire_action,
            config=config,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'formation',
                self.namespace_name,
                'model',
                'form',
                self.form_model_name,
            ],
        ).str()


class FormModelMasterRef:
    namespace_name: str
    form_model_name: str

    def __init__(
            self,
            namespace_name: str,
            form_model_name: str,
    ):
        self.namespace_name = namespace_name
        self.form_model_name = form_model_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'formation',
                self.namespace_name,
                'model',
                'form',
                self.form_model_name,
            ],
        ).str()


class MoldModelRef:
    namespace_name: str
    mold_name: str

    def __init__(
            self,
            namespace_name: str,
            mold_name: str,
    ):
        self.namespace_name = namespace_name
        self.mold_name = mold_name

    def add_mold_capacity(
            self,
            capacity: int,
            user_id: str = '#{userId}',
    ) -> AddMoldCapacityByUserId:
        return AddMoldCapacityByUserId(
            namespace_name=self.namespace_name,
            user_id=user_id,
            mold_name=self.mold_name,
            capacity=capacity,
        )

    def set_mold_capacity(
            self,
            capacity: int,
            user_id: str = '#{userId}',
    ) -> SetMoldCapacityByUserId:
        return SetMoldCapacityByUserId(
            namespace_name=self.namespace_name,
            user_id=user_id,
            mold_name=self.mold_name,
            capacity=capacity,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'formation',
                self.namespace_name,
                'model',
                'mold',
                self.mold_name,
            ],
        ).str()


class MoldModelMasterRef:
    namespace_name: str
    mold_name: str

    def __init__(
            self,
            namespace_name: str,
            mold_name: str,
    ):
        self.namespace_name = namespace_name
        self.mold_name = mold_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'formation',
                self.namespace_name,
                'model',
                'mold',
                self.mold_name,
            ],
        ).str()


class CurrentFormMasterRef:
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
                'formation',
                self.namespace_name,
            ],
        ).str()


class FormRef:
    namespace_name: str
    mold_name: str
    index: str

    def __init__(
            self,
            namespace_name: str,
            mold_name: str,
            index: str,
    ):
        self.namespace_name = namespace_name
        self.mold_name = mold_name
        self.index = index

    def acquire_actions_to_form_properties(
            self,
            acquire_action: AcquireAction,
            config: List[AcquireActionConfig] = None,
            user_id: str = '#{userId}',
    ) -> AcquireActionsToFormProperties:
        return AcquireActionsToFormProperties(
            namespace_name=self.namespace_name,
            user_id=user_id,
            mold_name=self.mold_name,
            index=self.index,
            acquire_action=acquire_action,
            config=config,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'formation',
                self.namespace_name,
                'user',
                self.user_id,
                'mold',
                self.mold_name,
                'form',
                self.index,
            ],
        ).str()
