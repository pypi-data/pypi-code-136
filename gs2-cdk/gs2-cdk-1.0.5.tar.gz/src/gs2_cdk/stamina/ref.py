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

    def current_stamina_master(
            self,
    ) -> CurrentStaminaMasterRef:
        return CurrentStaminaMasterRef(
            namespace_name=self.namespace_name,
        )

    def max_stamina_table(
            self,
            max_stamina_table_name: str,
    ) -> MaxStaminaTableRef:
        return MaxStaminaTableRef(
            namespace_name=self.namespace_name,
            max_stamina_table_name=max_stamina_table_name,
        )

    def recover_interval_table(
            self,
            recover_interval_table_name: str,
    ) -> RecoverIntervalTableRef:
        return RecoverIntervalTableRef(
            namespace_name=self.namespace_name,
            recover_interval_table_name=recover_interval_table_name,
        )

    def recover_value_table(
            self,
            recover_value_table_name: str,
    ) -> RecoverValueTableRef:
        return RecoverValueTableRef(
            namespace_name=self.namespace_name,
            recover_value_table_name=recover_value_table_name,
        )

    def stamina_model(
            self,
            stamina_name: str,
    ) -> StaminaModelRef:
        return StaminaModelRef(
            namespace_name=self.namespace_name,
            stamina_name=stamina_name,
        )

    def recover_interval_table_master(
            self,
            recover_interval_table_name: str,
    ) -> RecoverIntervalTableMasterRef:
        return RecoverIntervalTableMasterRef(
            namespace_name=self.namespace_name,
            recover_interval_table_name=recover_interval_table_name,
        )

    def max_stamina_table_master(
            self,
            max_stamina_table_name: str,
    ) -> MaxStaminaTableMasterRef:
        return MaxStaminaTableMasterRef(
            namespace_name=self.namespace_name,
            max_stamina_table_name=max_stamina_table_name,
        )

    def recover_value_table_master(
            self,
            recover_value_table_name: str,
    ) -> RecoverValueTableMasterRef:
        return RecoverValueTableMasterRef(
            namespace_name=self.namespace_name,
            recover_value_table_name=recover_value_table_name,
        )

    def stamina_model_master(
            self,
            stamina_name: str,
    ) -> StaminaModelMasterRef:
        return StaminaModelMasterRef(
            namespace_name=self.namespace_name,
            stamina_name=stamina_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stamina',
                self.namespace_name,
            ],
        ).str()


class StaminaModelMasterRef:
    namespace_name: str
    stamina_name: str

    def __init__(
            self,
            namespace_name: str,
            stamina_name: str,
    ):
        self.namespace_name = namespace_name
        self.stamina_name = stamina_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stamina',
                self.namespace_name,
                'model',
                self.stamina_name,
            ],
        ).str()


class MaxStaminaTableMasterRef:
    namespace_name: str
    max_stamina_table_name: str

    def __init__(
            self,
            namespace_name: str,
            max_stamina_table_name: str,
    ):
        self.namespace_name = namespace_name
        self.max_stamina_table_name = max_stamina_table_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stamina',
                self.namespace_name,
                'maxStaminaTable',
                self.max_stamina_table_name,
            ],
        ).str()


class RecoverIntervalTableMasterRef:
    namespace_name: str
    recover_interval_table_name: str

    def __init__(
            self,
            namespace_name: str,
            recover_interval_table_name: str,
    ):
        self.namespace_name = namespace_name
        self.recover_interval_table_name = recover_interval_table_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stamina',
                self.namespace_name,
                'recoverIntervalTable',
                self.recover_interval_table_name,
            ],
        ).str()


class RecoverValueTableMasterRef:
    namespace_name: str
    recover_value_table_name: str

    def __init__(
            self,
            namespace_name: str,
            recover_value_table_name: str,
    ):
        self.namespace_name = namespace_name
        self.recover_value_table_name = recover_value_table_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stamina',
                self.namespace_name,
                'recoverValueTable',
                self.recover_value_table_name,
            ],
        ).str()


class CurrentStaminaMasterRef:
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
                'stamina',
                self.namespace_name,
            ],
        ).str()


class StaminaModelRef:
    namespace_name: str
    stamina_name: str

    def __init__(
            self,
            namespace_name: str,
            stamina_name: str,
    ):
        self.namespace_name = namespace_name
        self.stamina_name = stamina_name

    def recover_stamina(
            self,
            recover_value: int,
            user_id: str = '#{userId}',
    ) -> RecoverStaminaByUserId:
        return RecoverStaminaByUserId(
            namespace_name=self.namespace_name,
            stamina_name=self.stamina_name,
            user_id=user_id,
            recover_value=recover_value,
        )

    def raise_max_value(
            self,
            raise_value: int,
            user_id: str = '#{userId}',
    ) -> RaiseMaxValueByUserId:
        return RaiseMaxValueByUserId(
            namespace_name=self.namespace_name,
            stamina_name=self.stamina_name,
            user_id=user_id,
            raise_value=raise_value,
        )

    def set_max_value(
            self,
            max_value: int,
            user_id: str = '#{userId}',
    ) -> SetMaxValueByUserId:
        return SetMaxValueByUserId(
            namespace_name=self.namespace_name,
            stamina_name=self.stamina_name,
            user_id=user_id,
            max_value=max_value,
        )

    def set_recover_interval(
            self,
            recover_interval_minutes: int,
            user_id: str = '#{userId}',
    ) -> SetRecoverIntervalByUserId:
        return SetRecoverIntervalByUserId(
            namespace_name=self.namespace_name,
            stamina_name=self.stamina_name,
            user_id=user_id,
            recover_interval_minutes=recover_interval_minutes,
        )

    def set_recover_value(
            self,
            recover_value: int,
            user_id: str = '#{userId}',
    ) -> SetRecoverValueByUserId:
        return SetRecoverValueByUserId(
            namespace_name=self.namespace_name,
            stamina_name=self.stamina_name,
            user_id=user_id,
            recover_value=recover_value,
        )

    def consume_stamina(
            self,
            consume_value: int,
            user_id: str = '#{userId}',
    ) -> ConsumeStaminaByUserId:
        return ConsumeStaminaByUserId(
            namespace_name=self.namespace_name,
            stamina_name=self.stamina_name,
            user_id=user_id,
            consume_value=consume_value,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stamina',
                self.namespace_name,
                'model',
                self.stamina_name,
            ],
        ).str()


class MaxStaminaTableRef:
    namespace_name: str
    max_stamina_table_name: str

    def __init__(
            self,
            namespace_name: str,
            max_stamina_table_name: str,
    ):
        self.namespace_name = namespace_name
        self.max_stamina_table_name = max_stamina_table_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stamina',
                self.namespace_name,
                'maxStaminaTable',
                self.max_stamina_table_name,
            ],
        ).str()


class RecoverIntervalTableRef:
    namespace_name: str
    recover_interval_table_name: str

    def __init__(
            self,
            namespace_name: str,
            recover_interval_table_name: str,
    ):
        self.namespace_name = namespace_name
        self.recover_interval_table_name = recover_interval_table_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stamina',
                self.namespace_name,
                'recoverIntervalTable',
                self.recover_interval_table_name,
            ],
        ).str()


class RecoverValueTableRef:
    namespace_name: str
    recover_value_table_name: str

    def __init__(
            self,
            namespace_name: str,
            recover_value_table_name: str,
    ):
        self.namespace_name = namespace_name
        self.recover_value_table_name = recover_value_table_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stamina',
                self.namespace_name,
                'recoverValueTable',
                self.recover_value_table_name,
            ],
        ).str()
