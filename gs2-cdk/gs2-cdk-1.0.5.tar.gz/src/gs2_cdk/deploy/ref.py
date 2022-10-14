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


class StackRef:
    stack_name: str

    def __init__(
            self,
            stack_name: str,
    ):
        self.stack_name = stack_name

    def event(
            self,
            event_name: str,
    ) -> EventRef:
        return EventRef(
            stack_name=self.stack_name,
            event_name=event_name,
        )

    def output(
            self,
            output_name: str,
    ) -> OutputRef:
        return OutputRef(
            stack_name=self.stack_name,
            output_name=output_name,
        )

    def resource(
            self,
            resource_name: str,
    ) -> ResourceRef:
        return ResourceRef(
            stack_name=self.stack_name,
            resource_name=resource_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stack',
                self.stack_name,
            ],
        ).str()


class ResourceRef:
    stack_name: str
    resource_name: str

    def __init__(
            self,
            stack_name: str,
            resource_name: str,
    ):
        self.stack_name = stack_name
        self.resource_name = resource_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stack',
                self.stack_name,
                'resource',
                self.resource_name,
            ],
        ).str()


class WorkingStackRef:
    stack_name: str

    def __init__(
            self,
            stack_name: str,
    ):
        self.stack_name = stack_name

    def working_resource(
            self,
            resource_name: str,
    ) -> WorkingResourceRef:
        return WorkingResourceRef(
            stack_name=self.stack_name,
            resource_name=resource_name,
        )

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'deploy',
                self.stack_name,
            ],
        ).str()


class WorkingResourceRef:
    stack_name: str
    resource_name: str

    def __init__(
            self,
            stack_name: str,
            resource_name: str,
    ):
        self.stack_name = stack_name
        self.resource_name = resource_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'deploy',
                self.stack_name,
                'workingResource',
                self.resource_name,
            ],
        ).str()


class EventRef:
    stack_name: str
    event_name: str

    def __init__(
            self,
            stack_name: str,
            event_name: str,
    ):
        self.stack_name = stack_name
        self.event_name = event_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stack',
                self.stack_name,
                'event',
                self.event_name,
            ],
        ).str()


class OutputRef:
    stack_name: str
    output_name: str

    def __init__(
            self,
            stack_name: str,
            output_name: str,
    ):
        self.stack_name = stack_name
        self.output_name = output_name

    def grn(self) -> str:
        return Join(
            ':',
            [
                'grn',
                'gs2',
                GetAttr.region().str(),
                GetAttr.owner_id().str(),
                'stack',
                self.stack_name,
                'output',
                self.output_name,
            ],
        ).str()
