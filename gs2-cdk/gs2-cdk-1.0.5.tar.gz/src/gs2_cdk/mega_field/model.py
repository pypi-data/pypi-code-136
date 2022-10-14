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


class Position:
    x: float
    y: float
    z: float

    def __init__(
            self,
            x: float = None,
            y: float = None,
            z: float = None,
    ):
        self.x = x
        self.y = y
        self.z = z

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.x:
            properties["X"] = self.x
        if self.y:
            properties["Y"] = self.y
        if self.z:
            properties["Z"] = self.z
        return properties


class MyPosition:
    position: Position
    vector: Vector
    r: float

    def __init__(
            self,
            position: Position = None,
            vector: Vector = None,
            r: float = None,
    ):
        self.position = position
        self.vector = vector
        self.r = r

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.position:
            properties["Position"] = self.position.properties()
        if self.vector:
            properties["Vector"] = self.vector.properties()
        if self.r:
            properties["R"] = self.r
        return properties


class Scope:
    layer_name: str
    r: float
    limit: int

    def __init__(
            self,
            layer_name: str = None,
            r: float = None,
            limit: int = None,
    ):
        self.layer_name = layer_name
        self.r = r
        self.limit = limit

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.layer_name:
            properties["LayerName"] = self.layer_name
        if self.r:
            properties["R"] = self.r
        if self.limit:
            properties["Limit"] = self.limit
        return properties


class Vector:
    x: float
    y: float
    z: float

    def __init__(
            self,
            x: float = None,
            y: float = None,
            z: float = None,
    ):
        self.x = x
        self.y = y
        self.z = z

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.x:
            properties["X"] = self.x
        if self.y:
            properties["Y"] = self.y
        if self.z:
            properties["Z"] = self.z
        return properties
