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


class AccessLog:
    timestamp: int
    request_id: str
    service: str
    method: str
    user_id: str
    request: str
    result: str

    def __init__(
            self,
            timestamp: int = None,
            request_id: str = None,
            service: str = None,
            method: str = None,
            user_id: str = None,
            request: str = None,
            result: str = None,
    ):
        self.timestamp = timestamp
        self.request_id = request_id
        self.service = service
        self.method = method
        self.user_id = user_id
        self.request = request
        self.result = result

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.timestamp:
            properties["Timestamp"] = self.timestamp
        if self.request_id:
            properties["RequestId"] = self.request_id
        if self.service:
            properties["Service"] = self.service
        if self.method:
            properties["Method"] = self.method
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.request:
            properties["Request"] = self.request
        if self.result:
            properties["Result"] = self.result
        return properties


class AccessLogCount:
    service: str
    method: str
    user_id: str
    count: int

    def __init__(
            self,
            service: str = None,
            method: str = None,
            user_id: str = None,
            count: int = None,
    ):
        self.service = service
        self.method = method
        self.user_id = user_id
        self.count = count

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.service:
            properties["Service"] = self.service
        if self.method:
            properties["Method"] = self.method
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.count:
            properties["Count"] = self.count
        return properties


class IssueStampSheetLog:
    timestamp: int
    transaction_id: str
    service: str
    method: str
    user_id: str
    action: str
    args: str
    tasks: List[str]

    def __init__(
            self,
            timestamp: int = None,
            transaction_id: str = None,
            service: str = None,
            method: str = None,
            user_id: str = None,
            action: str = None,
            args: str = None,
            tasks: List[str] = None,
    ):
        self.timestamp = timestamp
        self.transaction_id = transaction_id
        self.service = service
        self.method = method
        self.user_id = user_id
        self.action = action
        self.args = args
        self.tasks = tasks

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.timestamp:
            properties["Timestamp"] = self.timestamp
        if self.transaction_id:
            properties["TransactionId"] = self.transaction_id
        if self.service:
            properties["Service"] = self.service
        if self.method:
            properties["Method"] = self.method
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.action:
            properties["Action"] = self.action
        if self.args:
            properties["Args"] = self.args
        if self.tasks:
            properties["Tasks"] = [
                element
                for element in self.tasks
            ]
        return properties


class IssueStampSheetLogCount:
    service: str
    method: str
    user_id: str
    action: str
    count: int

    def __init__(
            self,
            service: str = None,
            method: str = None,
            user_id: str = None,
            action: str = None,
            count: int = None,
    ):
        self.service = service
        self.method = method
        self.user_id = user_id
        self.action = action
        self.count = count

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.service:
            properties["Service"] = self.service
        if self.method:
            properties["Method"] = self.method
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.action:
            properties["Action"] = self.action
        if self.count:
            properties["Count"] = self.count
        return properties


class ExecuteStampSheetLog:
    timestamp: int
    transaction_id: str
    service: str
    method: str
    user_id: str
    action: str
    args: str

    def __init__(
            self,
            timestamp: int = None,
            transaction_id: str = None,
            service: str = None,
            method: str = None,
            user_id: str = None,
            action: str = None,
            args: str = None,
    ):
        self.timestamp = timestamp
        self.transaction_id = transaction_id
        self.service = service
        self.method = method
        self.user_id = user_id
        self.action = action
        self.args = args

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.timestamp:
            properties["Timestamp"] = self.timestamp
        if self.transaction_id:
            properties["TransactionId"] = self.transaction_id
        if self.service:
            properties["Service"] = self.service
        if self.method:
            properties["Method"] = self.method
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.action:
            properties["Action"] = self.action
        if self.args:
            properties["Args"] = self.args
        return properties


class ExecuteStampSheetLogCount:
    service: str
    method: str
    user_id: str
    action: str
    count: int

    def __init__(
            self,
            service: str = None,
            method: str = None,
            user_id: str = None,
            action: str = None,
            count: int = None,
    ):
        self.service = service
        self.method = method
        self.user_id = user_id
        self.action = action
        self.count = count

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.service:
            properties["Service"] = self.service
        if self.method:
            properties["Method"] = self.method
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.action:
            properties["Action"] = self.action
        if self.count:
            properties["Count"] = self.count
        return properties


class ExecuteStampTaskLog:
    timestamp: int
    task_id: str
    service: str
    method: str
    user_id: str
    action: str
    args: str

    def __init__(
            self,
            timestamp: int = None,
            task_id: str = None,
            service: str = None,
            method: str = None,
            user_id: str = None,
            action: str = None,
            args: str = None,
    ):
        self.timestamp = timestamp
        self.task_id = task_id
        self.service = service
        self.method = method
        self.user_id = user_id
        self.action = action
        self.args = args

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.timestamp:
            properties["Timestamp"] = self.timestamp
        if self.task_id:
            properties["TaskId"] = self.task_id
        if self.service:
            properties["Service"] = self.service
        if self.method:
            properties["Method"] = self.method
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.action:
            properties["Action"] = self.action
        if self.args:
            properties["Args"] = self.args
        return properties


class ExecuteStampTaskLogCount:
    service: str
    method: str
    user_id: str
    action: str
    count: int

    def __init__(
            self,
            service: str = None,
            method: str = None,
            user_id: str = None,
            action: str = None,
            count: int = None,
    ):
        self.service = service
        self.method = method
        self.user_id = user_id
        self.action = action
        self.count = count

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.service:
            properties["Service"] = self.service
        if self.method:
            properties["Method"] = self.method
        if self.user_id:
            properties["UserId"] = self.user_id
        if self.action:
            properties["Action"] = self.action
        if self.count:
            properties["Count"] = self.count
        return properties
