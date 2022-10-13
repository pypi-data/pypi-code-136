from typing import Any, Tuple, Optional
from uuid import uuid4

from qottoauth.api.base import QottoAuthApi, QottoAuthApiError
from qottoauth.models import (
    Role,
    Organization,
    Identity,
    Account,
    Matching,
    Namespace,
    Application,
    Permission,
    Authorization,
    Member,
    User,
)

__all__ = [
    'QottoAuthTestApi',
]


class IdGenerator:
    def __init__(self) -> None:
        self._id = 0

    def __call__(self) -> str:
        self._id += 1
        return str(self._id)


gen_id = IdGenerator()


class QottoAuthTestApi(QottoAuthApi):

    def __init__(self):
        self._applications: dict[str, Application] = {}
        self._accounts: dict[str, Account] = {}
        self._permissions: dict[str, Permission] = {}
        self._authorizations: dict[str, Authorization] = {}
        self._authorization_permissions: dict[str, set[Permission]] = {}
        self._roles: dict[str, Role] = {}
        self._role_authorizations: dict[str, set[Authorization]] = {}
        self._members: dict[str, Member] = {}
        self._member_cookies: dict[str, tuple[str, str]] = {}
        self._member_roles: dict[str, set[Role]] = {}
        self._member_authorizations: dict[str, set[Authorization]] = {}
        self._organizations: dict[str, Organization] = {}
        self._users: dict[str, User] = {}
        self._user_cookies: dict[str, tuple[str, str]] = {}
        self._identities: dict[str, Identity] = {}

    def query(
            self,
            name: str,
            body: str,
            variables: list[Tuple[str, str, Any]] = None,
    ):
        kwargs = {}
        if variables:
            for var_name, var_type, var_value in variables:
                kwargs[var_name] = var_value
        if hasattr(self, name):
            try:
                return getattr(self, name)(**kwargs)
            except Exception as e:
                raise QottoAuthApiError from e
        raise QottoAuthApiError(f"Unknown query {name}")

    def mutation(
            self,
            name: str,
            body: str,
            input_name: str = 'input',
            input_type: str = None,
            input_value: dict[str, Any] = None,
    ):
        if hasattr(self, name):
            try:
                return getattr(self, name)(**input_value)
            except Exception as e:
                raise QottoAuthApiError from e
        raise QottoAuthApiError(f"Unknown mutation {name}")

    def application(self, id):
        return dict(
            id=self._applications[id].application_id,
            name=self._applications[id].name,
            description=self._applications[id].description,
        ) if id in self._applications else None

    def applications(self):
        return [self.application(id) for id in self._applications]

    def registerApplication(self, name, description):
        for application in self._applications.values():
            if application.name == name:
                return dict(application=self.application(application.application_id))
        application = Application(gen_id(), name, description)
        self._applications[application.application_id] = application
        return dict(application=self.application(application.application_id))

    def account(self, id):
        return dict(
            id=self._accounts[id].account_id,
            application=self.application(self._accounts[id].application.application_id),
            user=self.user(self._accounts[id].user.user_id),
            enabled=self._accounts[id].enabled,
            data=self._accounts[id].data,
        ) if id in self._accounts else None

    def accounts(self):
        return [self.account(id) for id in self._accounts]

    def createAccount(self, userId, applicationId):
        for account in self._accounts.values():
            if account.application.application_id == applicationId and account.user.user_id == userId:
                raise ValueError(f"Account already exists for user {userId} and application {applicationId}")
        account = Account(gen_id(), self._applications[applicationId], self._users[userId], True, {})
        self._accounts[account.account_id] = account
        return dict(account=self.account(account.account_id))

    def updateAccount(self, accountId, setEnabled):
        self._accounts[accountId].enabled = setEnabled
        return self.account(accountId)

    def deleteAccount(self, accountId):
        if accountId in self._accounts:
            del self._accounts[accountId]
            return dict(deleted=True)
        else:
            return dict(deleted=False)

    def permission(self, id):
        return dict(
            id=self._permissions[id].permission_id,
            application=self.application(self._permissions[id].application.application_id),
            name=self._permissions[id].name,
            description=self._permissions[id].description,
        ) if id in self._permissions else None

    def permissions(self):
        return [self.permission(id) for id in self._permissions]

    def registerPermission(self, applicationId, name, description):
        for permission in self._permissions.values():
            if permission.application.application_id == applicationId and permission.name == name:
                return dict(permission=self.permission(permission.permission_id))
        permission = Permission(self._applications[applicationId], gen_id(), name, description)
        self._permissions[permission.permission_id] = permission
        return dict(permission=self.permission(permission.permission_id))

    def user(self, id):
        return dict(
            id=self._users[id].user_id,
            name=self._users[id].name,
            isSuperuser=self._users[id].is_superuser,
            accounts=[
                dict(
                    id=user_account.account_id,
                    application=self.application(user_account.application.application_id),
                    user=dict(
                        id=self._users[id].user_id,
                        name=self._users[id].name,
                        isSuperuser=self._users[id].is_superuser,
                    ),
                    enabled=user_account.enabled,
                    data=user_account.data,

                ) for user_account in [
                    account for account in self._accounts.values() if account.user.user_id == id
                ]
            ],
        ) if id in self._users else None

    def userFromCookies(self, tokenCookie, secretCookie):
        for user_id, (user_token, user_secret) in self._user_cookies.items():
            if user_token == tokenCookie and user_secret == secretCookie:
                return self.user(user_id)
        return None

    def users(self):
        return [self.user(id) for id in self._users]

    def createUser(self, name):
        user = User(gen_id(), name, False)
        self._users[user.user_id] = user
        self._user_cookies[user.user_id] = (str(uuid4()), str(uuid4()))
        return dict(user=self.user(user.user_id))

    def createUserFromIdentity(self, identityId):
        if identityId not in self._identities:
            raise ValueError(f"Unknown identity {identityId}")
        user = User(gen_id(), self._identities[identityId].name, False)
        self._users[user.user_id] = user
        return dict(user=self.user(user.user_id))

    def deleteUser(self, userId):
        if userId in self._users:
            del self._users[userId]
            accounts_to_delete = [account for account in self._accounts.values() if account.user.user_id == userId]
            members_to_delete = [member for member in self._members.values() if member.user.user_id == userId]
            for account in accounts_to_delete:
                self.deleteAccount(account.account_id)
            for member in members_to_delete:
                self.deleteMember(member.member_id)
            return dict(deleted=True)
        else:
            return dict(deleted=False)

    def identity(self, identityId):
        return dict(
            id=self._identities[identityId].identity_id,
            user=self.user(self._identities[identityId].user.user_id) if self._identities[identityId].user else None,
            providerId=self._identities[identityId].provider_id,
            name=self._identities[identityId].name,
            email=self._identities[identityId].email,
            blocked=self._identities[identityId].blocked,
        ) if identityId in self._identities else None

    def identities(self):
        return [self.identity(id) for id in self._identities]

    def createIdentity(self, providerId, name, email):
        identity = Identity(gen_id(), name, providerId, email, None, False)
        self._identities[identity.identity_id] = identity
        return dict(identity=self.identity(identity.identity_id))

    def deleteIdentity(self, identityId):
        if identityId in self._identities:
            del self._identities[identityId]
            return dict(deleted=True)
        else:
            return dict(deleted=False)

    def authorization(self, authorizationId):
        return dict(
            id=self._authorizations[authorizationId].authorization_id,
            name=self._authorizations[authorizationId].name,
            description=self._authorizations[authorizationId].description,
            organization=self.organization(self._authorizations[authorizationId].organization.organization_id),
            inheritance=self._authorizations[authorizationId].inheritance,
            matching=str(self._authorizations[authorizationId].matching),
            permissions=[self.permission(permission.permission_id) for permission in
                         self._authorization_permissions[authorizationId]],
        ) if authorizationId in self._authorizations else None

    def authorizations(self):
        return [self.authorization(id) for id in self._authorizations]

    def createAuthorization(self, organizationId, name, description, inheritance, matching):
        authorization = Authorization(
            gen_id(), name, description, self._organizations[organizationId], inheritance, Matching(matching)
        )
        self._authorizations[authorization.authorization_id] = authorization
        self._authorization_permissions[authorization.authorization_id] = set()
        return dict(authorization=self.authorization(authorization.authorization_id))

    def updateAuthorization(self, authorizationId, addPermissionId=None, removePermissionId=None):
        if addPermissionId:
            self._authorization_permissions[authorizationId].add(self._permissions[addPermissionId])
        if removePermissionId:
            self._authorization_permissions[authorizationId].remove(self._permissions[removePermissionId])
        return dict(authorization=self.authorization(authorizationId))

    def deleteAuthorization(self, authorizationId):
        if authorizationId in self._authorizations:
            del self._authorizations[authorizationId]
            del self._authorization_permissions[authorizationId]
            return dict(deleted=True)
        else:
            return dict(deleted=False)

    def role(self, roleId):
        return dict(
            id=self._roles[roleId].role_id,
            name=self._roles[roleId].name,
            description=self._roles[roleId].description,
            organization=self.organization(self._roles[roleId].organization.organization_id),
            inheritance=self._roles[roleId].inheritance,
            authorizations=[self.authorization(authorization.authorization_id) for authorization in
                            self._role_authorizations[roleId]],
        ) if roleId in self._roles else None

    def roles(self):
        return [self.role(id) for id in self._roles]

    def createRole(self, organizationId, name, description, inheritance):
        role = Role(gen_id(), name, description, self._organizations[organizationId], inheritance)
        self._roles[role.role_id] = role
        self._role_authorizations[role.role_id] = set()
        return dict(role=self.role(role.role_id))

    def updateRole(self, roleId, addAuthorizationId=None, removeAuthorizationId=None):
        if addAuthorizationId:
            self._role_authorizations[roleId].add(self._authorizations[addAuthorizationId])
        if removeAuthorizationId:
            self._role_authorizations[roleId].remove(self._authorizations[removeAuthorizationId])
        return dict(role=self.role(roleId))

    def deleteRole(self, roleId):
        if roleId in self._roles:
            del self._roles[roleId]
            del self._role_authorizations[roleId]
            return dict(deleted=True)
        else:
            return dict(deleted=False)

    def organization(self, organizationId):
        return dict(
            id=self._organizations[organizationId].organization_id,
            name=self._organizations[organizationId].name,
            namespace=str(self._organizations[organizationId].namespace),
        ) if organizationId in self._organizations else None

    def organizations(self):
        return [self.organization(id) for id in self._organizations]

    def createOrganization(self, name, namespace):
        for organization in self._organizations.values():
            if organization.namespace == Namespace(namespace):
                raise Exception("Organization with this namespace already exists")
        organization = Organization(gen_id(), name, Namespace(namespace))
        self._organizations[organization.organization_id] = organization
        return dict(organization=self.organization(organization.organization_id))

    def deleteOrganization(self, organizationId):
        if organizationId in self._organizations:
            del self._organizations[organizationId]
            members_to_delete = [member for member in self._members.values() if
                                 member.organization.organization_id == organizationId]
            for member in members_to_delete:
                self.deleteMember(member.member_id)
            authorizations_to_delete = [authorization for authorization in self._authorizations.values() if
                                        authorization.organization.organization_id == organizationId]
            for authorization in authorizations_to_delete:
                self.deleteAuthorization(authorization.authorization_id)
            roles_to_delete = [role for role in self._roles.values() if
                               role.organization.organization_id == organizationId]
            for role in roles_to_delete:
                self.deleteRole(role.role_id)

            return dict(deleted=True)
        else:
            return dict(deleted=False)

    def member(self, memberId):
        return dict(
            id=self._members[memberId].member_id,
            user=self.user(self._members[memberId].user.user_id),
            organization=self.organization(self._members[memberId].organization.organization_id),
            roles=[self.role(role.role_id) for role in self._member_roles[memberId]],
            authorizations=[self.authorization(authorization.authorization_id) for authorization in
                            self._member_authorizations[memberId]],
        ) if memberId in self._members else None

    def memberFromCookies(self, tokenCookie, secretCookie):
        for member_id, (member_token, member_secret) in self._member_cookies.items():
            if tokenCookie == member_token and secretCookie == member_secret:
                return self.member(member_id)
        return None

    def members(self):
        return [self.member(id) for id in self._members]

    def createMember(self, userId, organizationId):
        for member in self._members.values():
            if member.user.user_id == userId and member.organization.organization_id == organizationId:
                raise Exception("Member already exists")
        member = Member(gen_id(), self._users[userId], self._organizations[organizationId])
        self._members[member.member_id] = member
        self._member_roles[member.member_id] = set()
        self._member_authorizations[member.member_id] = set()
        self._member_cookies[member.member_id] = (str(uuid4()), str(uuid4()))
        return dict(member=self.member(member.member_id))

    def updateMember(
            self, memberId,
            addRoleId=None, removeRoleId=None,
            addAuthorizationId=None, removeAuthorizationId=None
    ):
        if addRoleId:
            self._member_roles[memberId].add(self._roles[addRoleId])
        if removeRoleId:
            self._member_roles[memberId].remove(self._roles[removeRoleId])
        if addAuthorizationId:
            self._member_authorizations[memberId].add(self._authorizations[addAuthorizationId])
        if removeAuthorizationId:
            self._member_authorizations[memberId].remove(self._authorizations[removeAuthorizationId])
        return dict(member=self.member(memberId))

    def deleteMember(self, memberId):
        if memberId in self._members:
            del self._members[memberId]
            del self._member_roles[memberId]
            del self._member_authorizations[memberId]
            del self._member_cookies[memberId]
            return dict(deleted=True)
        else:
            return dict(deleted=False)

    def cookies(self, userId=None, organizationId=None):
        token, secret = None, None
        if organizationId is None:
            token, secret = self._user_cookies[userId]
        else:
            for member_id, (member_token, member_secret) in self._member_cookies.items():
                if (
                        self._members[member_id].user.user_id == userId
                        and self._members[member_id].organization.organization_id == organizationId
                ):
                    token, secret = member_token, member_secret
        if not token or not secret:
            raise ValueError(f"No cookies found for user #{userId} in organization #{organizationId}.")
        return [
            dict(name='token', value=token, domain='domain', maxAge=3600, secure=True, httpOnly=False),
            dict(name='secret', value=secret, domain='domain', maxAge=3600, secure=True, httpOnly=True),
        ]

    def isAuthorized(
            self,
            userId: str = None, memberId: str = None,
            permissionId: str = None,
            organizationId: str = None,
            organizationNamespace: str = None,
    ) -> bool:
        user: Optional[User] = None
        if userId:
            user = self._users[userId]
        member: Optional[Member] = None
        if memberId:
            member = self._members[memberId]
        if not permissionId:
            raise ValueError("No permissionId provided.")
        permission: Permission = self._permissions[permissionId]
        namespace: Optional[Namespace] = None
        if organizationId:
            namespace = self._organizations[organizationId].namespace
        if organizationNamespace:
            namespace = Namespace(organizationNamespace)
        if not member:
            return user.is_superuser if user else False
        all_authorizations = set()
        for role in self._member_roles[member.member_id]:
            for authorization in self._role_authorizations[role.role_id]:
                all_authorizations.add(authorization)
        for authorization in self._member_authorizations[member.member_id]:
            all_authorizations.add(authorization)
        for authorization in all_authorizations:
            if permission in self._authorization_permissions[authorization.authorization_id]:
                if not namespace:
                    return True
                if not authorization.organization.namespace >= namespace:
                    continue
                if not authorization.inheritance and authorization.organization.namespace != namespace:
                    continue
                if namespace.matches(member.organization.namespace, authorization.matching):
                    return True
        return False
