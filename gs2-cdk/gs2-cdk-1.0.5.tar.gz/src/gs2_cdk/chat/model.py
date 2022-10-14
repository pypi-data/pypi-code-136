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


class NotificationType:
    category: int
    enable_transfer_mobile_push_notification: bool

    def __init__(
            self,
            category: int = None,
            enable_transfer_mobile_push_notification: bool = None,
    ):
        self.category = category
        self.enable_transfer_mobile_push_notification = enable_transfer_mobile_push_notification

    def properties(self) -> Dict[str, Any]:
        properties = {}
        if self.category:
            properties["Category"] = self.category
        if self.enable_transfer_mobile_push_notification:
            properties["EnableTransferMobilePushNotification"] = self.enable_transfer_mobile_push_notification
        return properties
