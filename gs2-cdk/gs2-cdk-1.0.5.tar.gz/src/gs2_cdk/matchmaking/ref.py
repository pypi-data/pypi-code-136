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

    def current_rating_model_master(
            self,
    ) -> CurrentRatingModelMasterRef:
        return CurrentRatingModelMasterRef(
            namespace_name=self.namespace_name,
        )

    def rating_model(
            self,
            rating_name: str,
    ) -> RatingModelRef:
        return RatingModelRef(
            namespace_name=self.namespace_name,
            rating_name=rating_name,
        )

    def vote(
            self,
            rating_name: str,
            gathering_name: str,
    ) -> VoteRef:
        return VoteRef(
            namespace_name=self.namespace_name,
            rating_name=rating_name,
            gathering_name=gathering_name,
        )

    def rating_model_master(
            self,
            rating_name: str,
    ) -> RatingModelMasterRef:
        return RatingModelMasterRef(
            namespace_name=self.namespace_name,
            rating_name=rating_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'matchmaking',
                self.namespace_name,
            ],
        ).str()


class GatheringRef:
    namespace_name: str
    gathering_name: str

    def __init__(
            self,
            namespace_name: str,
            gathering_name: str,
    ):
        self.namespace_name = namespace_name
        self.gathering_name = gathering_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'matchmaking',
                self.namespace_name,
                'gathering',
                self.gathering_name,
            ],
        ).str()


class RatingModelMasterRef:
    namespace_name: str
    rating_name: str

    def __init__(
            self,
            namespace_name: str,
            rating_name: str,
    ):
        self.namespace_name = namespace_name
        self.rating_name = rating_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'matchmaking',
                self.namespace_name,
                'model',
                self.rating_name,
            ],
        ).str()


class RatingModelRef:
    namespace_name: str
    rating_name: str

    def __init__(
            self,
            namespace_name: str,
            rating_name: str,
    ):
        self.namespace_name = namespace_name
        self.rating_name = rating_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'matchmaking',
                self.namespace_name,
                'model',
                self.rating_name,
            ],
        ).str()


class CurrentRatingModelMasterRef:
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
                'matchmaking',
                self.namespace_name,
            ],
        ).str()


class VoteRef:
    namespace_name: str
    rating_name: str
    gathering_name: str

    def __init__(
            self,
            namespace_name: str,
            rating_name: str,
            gathering_name: str,
    ):
        self.namespace_name = namespace_name
        self.rating_name = rating_name
        self.gathering_name = gathering_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'matchmaking',
                self.namespace_name,
                'vote',
                self.rating_name,
                self.gathering_name,
            ],
        ).str()
