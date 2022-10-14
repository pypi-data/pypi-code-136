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

    def current_field_master(
            self,
    ) -> CurrentFieldMasterRef:
        return CurrentFieldMasterRef(
            namespace_name=self.namespace_name,
        )

    def area_model(
            self,
            area_model_name: str,
    ) -> AreaModelRef:
        return AreaModelRef(
            namespace_name=self.namespace_name,
            area_model_name=area_model_name,
        )

    def node(
            self,
            node_name: str,
    ) -> NodeRef:
        return NodeRef(
            namespace_name=self.namespace_name,
            node_name=node_name,
        )

    def layer(
            self,
            area_model_name: str,
            layer_model_name: str,
    ) -> LayerRef:
        return LayerRef(
            namespace_name=self.namespace_name,
            area_model_name=area_model_name,
            layer_model_name=layer_model_name,
        )

    def area_model_master(
            self,
            area_model_name: str,
    ) -> AreaModelMasterRef:
        return AreaModelMasterRef(
            namespace_name=self.namespace_name,
            area_model_name=area_model_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'megaField',
                self.namespace_name,
            ],
        ).str()


class AreaModelRef:
    namespace_name: str
    area_model_name: str

    def __init__(
            self,
            namespace_name: str,
            area_model_name: str,
    ):
        self.namespace_name = namespace_name
        self.area_model_name = area_model_name

    def layer_model(
            self,
            layer_model_name: str,
    ) -> LayerModelRef:
        return LayerModelRef(
            namespace_name=self.namespace_name,
            area_model_name=self.area_model_name,
            layer_model_name=layer_model_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'megaField',
                self.namespace_name,
                'model',
                'area',
                self.area_model_name,
            ],
        ).str()


class AreaModelMasterRef:
    namespace_name: str
    area_model_name: str

    def __init__(
            self,
            namespace_name: str,
            area_model_name: str,
    ):
        self.namespace_name = namespace_name
        self.area_model_name = area_model_name

    def layer_model_master(
            self,
            layer_model_name: str,
    ) -> LayerModelMasterRef:
        return LayerModelMasterRef(
            namespace_name=self.namespace_name,
            area_model_name=self.area_model_name,
            layer_model_name=layer_model_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'megaField',
                self.namespace_name,
                'master',
                'area',
                self.area_model_name,
            ],
        ).str()


class LayerModelRef:
    namespace_name: str
    area_model_name: str
    layer_model_name: str

    def __init__(
            self,
            namespace_name: str,
            area_model_name: str,
            layer_model_name: str,
    ):
        self.namespace_name = namespace_name
        self.area_model_name = area_model_name
        self.layer_model_name = layer_model_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'megaField',
                self.namespace_name,
                'model',
                'area',
                self.area_model_name,
                'layer',
                self.layer_model_name,
            ],
        ).str()


class LayerModelMasterRef:
    namespace_name: str
    area_model_name: str
    layer_model_name: str

    def __init__(
            self,
            namespace_name: str,
            area_model_name: str,
            layer_model_name: str,
    ):
        self.namespace_name = namespace_name
        self.area_model_name = area_model_name
        self.layer_model_name = layer_model_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'megaField',
                self.namespace_name,
                'model',
                'area',
                self.area_model_name,
                'layer',
                self.layer_model_name,
            ],
        ).str()


class CurrentFieldMasterRef:
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
                'megaField',
                self.namespace_name,
            ],
        ).str()


class NodeRef:
    namespace_name: str
    node_name: str

    def __init__(
            self,
            namespace_name: str,
            node_name: str,
    ):
        self.namespace_name = namespace_name
        self.node_name = node_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'megaField',
                self.namespace_name,
                'node',
                self.node_name,
            ],
        ).str()


class LayerRef:
    namespace_name: str
    area_model_name: str
    layer_model_name: str

    def __init__(
            self,
            namespace_name: str,
            area_model_name: str,
            layer_model_name: str,
    ):
        self.namespace_name = namespace_name
        self.area_model_name = area_model_name
        self.layer_model_name = layer_model_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'megaField',
                self.namespace_name,
                'layer',
                self.area_model_name,
                self.layer_model_name,
            ],
        ).str()
