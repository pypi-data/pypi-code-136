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

    def current_lottery_master(
            self,
    ) -> CurrentLotteryMasterRef:
        return CurrentLotteryMasterRef(
            namespace_name=self.namespace_name,
        )

    def prize_table(
            self,
            prize_table_name: str,
    ) -> PrizeTableRef:
        return PrizeTableRef(
            namespace_name=self.namespace_name,
            prize_table_name=prize_table_name,
        )

    def lottery_model(
            self,
            lottery_name: str,
    ) -> LotteryModelRef:
        return LotteryModelRef(
            namespace_name=self.namespace_name,
            lottery_name=lottery_name,
        )

    def prize_table_master(
            self,
            prize_table_name: str,
    ) -> PrizeTableMasterRef:
        return PrizeTableMasterRef(
            namespace_name=self.namespace_name,
            prize_table_name=prize_table_name,
        )

    def lottery_model_master(
            self,
            lottery_name: str,
    ) -> LotteryModelMasterRef:
        return LotteryModelMasterRef(
            namespace_name=self.namespace_name,
            lottery_name=lottery_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'lottery',
                self.namespace_name,
            ],
        ).str()


class LotteryModelMasterRef:
    namespace_name: str
    lottery_name: str

    def __init__(
            self,
            namespace_name: str,
            lottery_name: str,
    ):
        self.namespace_name = namespace_name
        self.lottery_name = lottery_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'lottery',
                self.namespace_name,
                'lotteryModel',
                self.lottery_name,
            ],
        ).str()


class PrizeTableMasterRef:
    namespace_name: str
    prize_table_name: str

    def __init__(
            self,
            namespace_name: str,
            prize_table_name: str,
    ):
        self.namespace_name = namespace_name
        self.prize_table_name = prize_table_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'lottery',
                self.namespace_name,
                'table',
                self.prize_table_name,
            ],
        ).str()


class LotteryModelRef:
    namespace_name: str
    lottery_name: str

    def __init__(
            self,
            namespace_name: str,
            lottery_name: str,
    ):
        self.namespace_name = namespace_name
        self.lottery_name = lottery_name

    def draw(
            self,
            count: int,
            config: List[Config] = None,
            user_id: str = '#{userId}',
    ) -> DrawByUserId:
        return DrawByUserId(
            namespace_name=self.namespace_name,
            lottery_name=self.lottery_name,
            user_id=user_id,
            count=count,
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
                'lottery',
                self.namespace_name,
                'lotteryModel',
                self.lottery_name,
            ],
        ).str()


class PrizeTableRef:
    namespace_name: str
    prize_table_name: str

    def __init__(
            self,
            namespace_name: str,
            prize_table_name: str,
    ):
        self.namespace_name = namespace_name
        self.prize_table_name = prize_table_name

    def prize_limit(
            self,
            prize_id: str,
    ) -> PrizeLimitRef:
        return PrizeLimitRef(
            namespace_name=self.namespace_name,
            prize_table_name=self.prize_table_name,
            prize_id=prize_id,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'lottery',
                self.namespace_name,
                'table',
                self.prize_table_name,
            ],
        ).str()


class CurrentLotteryMasterRef:
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
                'lottery',
                self.namespace_name,
            ],
        ).str()


class PrizeLimitRef:
    namespace_name: str
    prize_table_name: str
    prize_id: str

    def __init__(
            self,
            namespace_name: str,
            prize_table_name: str,
            prize_id: str,
    ):
        self.namespace_name = namespace_name
        self.prize_table_name = prize_table_name
        self.prize_id = prize_id

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'lottery',
                self.namespace_name,
                'table',
                self.prize_table_name,
                'prize',
                self.prize_id,
            ],
        ).str()
