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
from ..core import *
from .ref import *


class User(CdkResource):

    stack: Stack
    name: str
    description: str

    def __init__(
            self,
            stack: Stack,
            name: str,
            description: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Identifier::User"

    def properties(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
        }

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
    ):
        return UserRef(
            user_name=self.name,
        )

    def attach(
            self,
            security_policy: SecurityPolicy,
    ) -> User:
        AttachSecurityPolicy(
            stack=self.stack,
            user_name=self.name,
            security_policy_id=security_policy.get_attr_security_policy_id().str(),
        ).add_depends_on(
            self,
        ).add_depends_on(
            security_policy,
        )
        return self

    def identifier(self) -> Identifier:
        return Identifier(
            stack=self.stack,
            user_name=self.name,
        ).add_depends_on(
            self,
        )

    def get_attr_user_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.UserId"
        )


class Statement:

    effect: str
    actions: List[str]

    @staticmethod
    def allow(
            actions: List[str],
    ) -> Statement:
        statement = Statement()
        statement.effect = "Allow"
        statement.actions = actions
        return statement

    @staticmethod
    def allow_all() -> Statement:
        statement = Statement()
        statement.effect = "Allow"
        statement.actions = ['*']
        return statement

    @staticmethod
    def deny(
            actions: List[str],
    ) -> Statement:
        statement = Statement()
        statement.effect = "Deny"
        statement.actions = actions
        return statement

    @staticmethod
    def deny_all() -> Statement:
        statement = Statement()
        statement.effect = "Deny"
        statement.actions = ['*']
        return statement

    def action(self, action: str) -> Statement:
        self.actions.append(action)
        return self

    def properties(self) -> Dict[str, Any]:
        return {
            "Effect": self.effect,
            "Actions": [
                action
                for action in self.actions
            ],
            "Resources": ['*']
        }


class Policy:

    version: str = "2016-04-01"
    statements: List[Statement]

    def __init__(
            self,
            statements: List[Statement]
    ):
        self.statements = statements

    def properties(self) -> Dict[str, Any]:
        return {
            "Version": self.version,
            "Statements": [
                statement.properties()
                for statement in self.statements
            ],
        }


class SecurityPolicy(CdkResource):

    stack: Stack
    name: str
    description: str
    policy: Policy

    def __init__(
            self,
            stack: Stack,
            name: str,
            policy: Policy,
            description: str = None,
            resource_name: str = None,
    ):
        self.stack = stack
        self.name = name
        self.description = description
        self.policy = policy

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Identifier::SecurityPolicy"

    def properties(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "policy": self.policy.properties(),
        }

    def alternate_keys(self) -> str:
        return '' + self.name

    def ref(
            self,
    ):
        return SecurityPolicyRef(
            security_policy_name=self.name,
        )

    def get_attr_security_policy_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.SecurityPolicyId"
        )


class AttachSecurityPolicy(CdkResource):

    stack: Stack
    user_name: str
    security_policy_id: str

    def __init__(
            self,
            stack: Stack,
            user_name: str,
            security_policy_id: str,
            resource_name: str = None,
    ):
        self.stack = stack
        self.user_name = user_name
        self.security_policy_id = security_policy_id
        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def alternate_keys(self):
        return self.user_name

    def resource_type(self) -> str:
        return "GS2::Identifier::AttachSecurityPolicy"

    def properties(self) -> Dict[str, Any]:
        return {
            "userName": self.user_name,
            "securityPolicyId": self.security_policy_id,
        }


class Identifier(CdkResource):

    stack: Stack
    user_name: str

    def __init__(
            self,
            stack: Stack,
            user_name: str,
            resource_name: str = None,
    ):
        self.stack = stack
        self.user_name = user_name

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Identifier::Identifier"

    def properties(self) -> Dict[str, Any]:
        return {
            "userName": self.user_name,
        }

    def alternate_keys(self) -> str:
        return ''

    @staticmethod
    def AdministratorAccessGrn() -> str:
        return "grn:gs2::system:identifier:securityPolicy:AdministratorAccess"

    @staticmethod
    def ApplicationAccessGrn() -> str:
        return "grn:gs2::system:identifier:securityPolicy:ApplicationAccess"

    def get_attr_identifier_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.IdentifierId"
        )

    def get_attr_client_id(self) -> GetAttr:
        return GetAttr(
            self,
            "Item.ClientId"
        )

    def get_attr_client_secret(self) -> GetAttr:
        return GetAttr(
            self,
            "ClientSecret"
        )


class Password(CdkResource):

    stack: Stack
    user_name: str
    password: str

    def __init__(
            self,
            stack: Stack,
            user_name: str,
            password: str,
            resource_name: str = None,
    ):
        self.stack = stack
        self.user_name = user_name
        self.password = password

        if resource_name is None:
            resource_name = self.default_resource_name()

        super().__init__(resource_name)
        stack.add_resource(self)

    def resource_type(self) -> str:
        return "GS2::Identifier::Password"

    def properties(self) -> Dict[str, Any]:
        return {
            "userName": self.user_name,
            "password": self.password,
        }

    def alternate_keys(self) -> str:
        return ''+ self.user_name

    def ref(
            self,
    ):
        return PasswordRef(
            user_name=self.user_name,
        )
