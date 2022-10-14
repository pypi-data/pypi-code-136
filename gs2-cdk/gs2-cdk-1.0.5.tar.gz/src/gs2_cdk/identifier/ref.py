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
#
# deny overwrite

from __future__ import annotations
from .model import *
from .stamp_sheet import *

from typing import List


class UserRef:
    user_name: str

    def __init__(
            self,
            user_name: str,
    ):
        self.user_name = user_name

    def password(
            self,
    ) -> PasswordRef:
        return PasswordRef(
            user_name=self.user_name,
        )

    def attach_security_policy(
            self,
    ) -> AttachSecurityPolicyRef:
        return AttachSecurityPolicyRef(
            user_name=self.user_name,
        )


class SecurityPolicyRef:
    security_policy_name: str

    def __init__(
            self,
            security_policy_name: str,
    ):
        self.security_policy_name = security_policy_name


class PasswordRef:
    user_name: str

    def __init__(
            self,
            user_name: str,
    ):
        self.user_name = user_name


class AttachSecurityPolicyRef:
    user_name: str

    def __init__(
            self,
            user_name: str,
    ):
        self.user_name = user_name
