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


class AttributeRange:
    name: str
    min: int
    max: int

    def __init__(
            self,
            name: str = None,
            min: int = None,
            max: int = None,
    ):
        self.name = name
        self.min = min
        self.max = max

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.min:
            properties["Min"] = self.min
        if self.max:
            properties["Max"] = self.max
        return properties


class CapacityOfRole:
    role_name: str
    role_aliases: List[str]
    capacity: int
    participants: List[Player]

    def __init__(
            self,
            role_name: str = None,
            role_aliases: List[str] = None,
            capacity: int = None,
            participants: List[Player] = None,
    ):
        self.role_name = role_name
        self.role_aliases = role_aliases
        self.capacity = capacity
        self.participants = participants

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.role_name:
            properties["RoleName"] = self.role_name
        if self.role_aliases:
            properties["RoleAliases"] = [
                element
                for element in self.role_aliases
            ]
        if self.capacity:
            properties["Capacity"] = self.capacity
        if self.participants:
            properties["Participants"] = [
                element.properties()
                for element in self.participants
            ]
        return properties


class Attribute:
    name: str
    value: int

    def __init__(
            self,
            name: str = None,
            value: int = None,
    ):
        self.name = name
        self.value = value

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.name:
            properties["Name"] = self.name
        if self.value:
            properties["Value"] = self.value
        return properties


class Player:
    user_id: str
    attributes: List[Attribute]
    role_name: str
    deny_user_ids: List[str]

    def __init__(
            self,
            user_id: str = None,
            attributes: List[Attribute] = None,
            role_name: str = None,
            deny_user_ids: List[str] = None,
    ):
        self.user_id = user_id
        self.attributes = attributes
        self.role_name = role_name
        self.deny_user_ids = deny_user_ids

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.attributes:
            properties["Attributes"] = [
                element.properties()
                for element in self.attributes
            ]
        if self.role_name:
            properties["RoleName"] = self.role_name
        if self.deny_user_ids:
            properties["DenyUserIds"] = [
                element
                for element in self.deny_user_ids
            ]
        return properties


class GameResult:
    rank: int
    user_id: str

    def __init__(
            self,
            rank: int = None,
            user_id: str = None,
    ):
        self.rank = rank
        self.user_id = user_id

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.rank:
            properties["Rank"] = self.rank
        if self.user_id:
            properties["UserId"] = self.user_id
        return properties


class Ballot:
    user_id: str
    rating_name: str
    gathering_name: str
    number_of_player: int

    def __init__(
            self,
            user_id: str = None,
            rating_name: str = None,
            gathering_name: str = None,
            number_of_player: int = None,
    ):
        self.user_id = user_id
        self.rating_name = rating_name
        self.gathering_name = gathering_name
        self.number_of_player = number_of_player

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.rating_name:
            properties["RatingName"] = self.rating_name
        if self.gathering_name:
            properties["GatheringName"] = self.gathering_name
        if self.number_of_player:
            properties["NumberOfPlayer"] = self.number_of_player
        return properties


class SignedBallot:
    body: str
    signature: str

    def __init__(
            self,
            body: str = None,
            signature: str = None,
    ):
        self.body = body
        self.signature = signature

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.body:
            properties["Body"] = self.body
        if self.signature:
            properties["Signature"] = self.signature
        return properties


class WrittenBallot:
    ballot: Ballot
    game_results: List[GameResult]

    def __init__(
            self,
            ballot: Ballot = None,
            game_results: List[GameResult] = None,
    ):
        self.ballot = ballot
        self.game_results = game_results

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.ballot:
            properties["Ballot"] = self.ballot.properties()
        if self.game_results:
            properties["GameResults"] = [
                element.properties()
                for element in self.game_results
            ]
        return properties


class TimeSpan:
    days: int
    hours: int
    minutes: int

    def __init__(
            self,
            days: int = None,
            hours: int = None,
            minutes: int = None,
    ):
        self.days = days
        self.hours = hours
        self.minutes = minutes

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.days:
            properties["Days"] = self.days
        if self.hours:
            properties["Hours"] = self.hours
        if self.minutes:
            properties["Minutes"] = self.minutes
        return properties
