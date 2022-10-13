import logging
from typing import Optional, Any, Union

from qottoauth.api import QottoAuthApi
from qottoauth.models import (
    Application,
    Permission,
    Organization,
    Account,
    Member,
    Namespace,
    User,
    Role,
    Authorization,
    Matching,
    Cookie,
    Identity,
)

__all__ = [
    'QottoAuthService',
]

logger = logging.getLogger(__name__)


class QottoAuthService:

    def __init__(
            self,
            api: QottoAuthApi,
    ):
        self.api = api

    def is_authorized(
            self,
            permission: Permission,
            user: User = None, member: Member = None,
            organization: Union[Organization, Namespace] = None,
    ) -> bool:
        authorized_data = self.api.query(
            name='isAuthorized',
            variables=[
                ('permissionId', 'ID!', permission.permission_id),
                ('userId', 'ID', user.user_id if user else None),
                ('memberId', 'ID', member.member_id if member else None),
                ('organizationId', 'ID',
                 organization.organization_id if organization and isinstance(organization, Organization) else None),
                ('organizationNamespace', 'String',
                 str(organization) if organization and isinstance(organization, Namespace) else None),
            ],
            body='',
        )
        return authorized_data  # type: ignore

    def get_accounts(self) -> list[Account]:
        accounts_data = self.api.query(
            name='accounts',
            body='''
                id
                user {
                    id
                    name
                    isSuperuser
                }
                application {
                    id
                    name
                    description
                }
                enabled
                data
            ''',
        )
        return [
            Account(
                account_id=account_data['id'],
                user=User(
                    user_id=account_data['user']['id'],
                    name=account_data['user']['name'],
                    is_superuser=account_data['user']['isSuperuser'],
                ),
                application=Application(
                    application_id=account_data['application']['id'],
                    name=account_data['application']['name'],
                    description=account_data['application']['description'],
                ),
                enabled=account_data['enabled'],
                data=account_data['data'],
            )
            for account_data in accounts_data
        ]

    def get_account(self, account_id: str) -> Optional[Account]:
        account_data = self.api.query(
            name='account',
            variables=[
                ('id', 'ID!', account_id),
            ],
            body='''
                id
                user {
                    id
                    name
                    isSuperuser
                }
                application {
                    id
                    name
                    description
                }
                enabled
                data
            ''',
        )
        if not account_data:
            return None
        return Account(
            account_id=account_data['id'],
            user=User(
                user_id=account_data['user']['id'],
                name=account_data['user']['name'],
                is_superuser=account_data['user']['isSuperuser'],
            ),
            application=Application(
                application_id=account_data['application']['id'],
                name=account_data['application']['name'],
                description=account_data['application']['description'],
            ),
            enabled=account_data['enabled'],
            data=account_data['data'],
        )

    def get_organizations(self) -> list[Organization]:
        organizations_data = self.api.query(
            name='organizations',
            body='''
                id
                name
                namespace
            ''',
        )
        return [
            Organization(
                organization_id=organization_data['id'],
                name=organization_data['name'],
                namespace=Namespace(organization_data['namespace']),
            ) for organization_data in organizations_data
        ]

    def get_organization(self, organization_id: str) -> Optional[Organization]:
        organization_data = self.api.query(
            name='organization',
            variables=[
                ('id', 'ID!', organization_id),
            ],
            body='''
                id
                name
                namespace
            ''',
        )
        if not organization_data:
            return None
        return Organization(
            organization_id=organization_data['id'],
            name=organization_data['name'],
            namespace=Namespace(organization_data['namespace']),
        )

    def get_organization_members(self, organization: Organization) -> list[Member]:
        return [
            member for member in self.get_members()
            if member.organization == organization
        ]

    def get_organization_roles(self, organization: Organization) -> list[Role]:
        return [
            role for role in self.get_roles()
            if role.organization == organization
        ]

    def get_organization_authorizations(self, organization: Organization) -> list[Authorization]:
        return [
            authorization for authorization in self.get_authorizations()
            if authorization.organization == organization
        ]

    def get_applications(self) -> list[Application]:
        applications_data = self.api.query(
            name='applications',
            body='''
                id
                name
                description
            ''',
        )
        return [
            Application(
                application_id=application_data['id'],
                name=application_data['name'],
                description=application_data['description'],
            ) for application_data in applications_data
        ]

    def get_application(self, application_id: str) -> Optional[Application]:
        application_data = self.api.query(
            name='application',
            variables=[
                ('id', 'ID!', application_id),
            ],
            body='''
                id
                name
                description
            ''',
        )
        if not application_data:
            return None
        return Application(
            application_id=application_data['id'],
            name=application_data['name'],
            description=application_data['description'],
        )

    def get_application_permissions(self, application: Application) -> list[Permission]:
        return [
            permission for permission in self.get_permissions()
            if permission.application == application
        ]

    def get_application_accounts(self, application: Application) -> list[Account]:
        return [
            account for account in self.get_accounts()
            if account.application == application
        ]

    def get_permissions(self) -> list[Permission]:
        permissions_data = self.api.query(
            name='permissions',
            body='''
                id
                name
                description
                application {
                    id
                    name
                    description
                }
            ''',
        )
        return [
            Permission(
                permission_id=permission_data['id'],
                name=permission_data['name'],
                description=permission_data['description'],
                application=Application(
                    application_id=permission_data['application']['id'],
                    name=permission_data['application']['name'],
                    description=permission_data['application']['description'],
                ),
            ) for permission_data in permissions_data
        ]

    def get_permission(self, permission_id: str) -> Optional[Permission]:
        permission_data = self.api.query(
            name='permission',
            variables=[
                ('id', 'ID!', permission_id),
            ],
            body='''
                id
                name
                description
                application {
                    id
                    name
                    description
                }
            ''',
        )
        if not permission_data:
            return None
        return Permission(
            permission_id=permission_data['id'],
            name=permission_data['name'],
            description=permission_data['description'],
            application=Application(
                application_id=permission_data['application']['id'],
                name=permission_data['application']['name'],
                description=permission_data['application']['description'],
            ),
        )

    def get_identities(self) -> list[Identity]:
        identities_data = self.api.query(
            name='identities',
            body='''
                id
                name
                providerId
                email
                blocked
                user {
                    id
                    name
                    isSuperuser
                }
            ''',
        )
        return [
            Identity(
                identity_id=identity_data['id'],
                name=identity_data['name'],
                provider_id=identity_data['providerId'],
                email=identity_data['email'],
                blocked=identity_data['blocked'],
                user=User(
                    user_id=identity_data['user']['id'],
                    name=identity_data['user']['name'],
                    is_superuser=identity_data['user']['isSuperuser'],
                ) if identity_data.get('user') else None,
            ) for identity_data in identities_data
        ]

    def get_identity(self, identity_id: str) -> Optional[Identity]:
        identity_data = self.api.query(
            name='identity',
            variables=[
                ('id', 'ID!', identity_id),
            ],
            body='''
                id
                name
                providerId
                email
                blocked
                user {
                    id
                    name
                    isSuperuser
                }
            ''',
        )
        if not identity_data:
            return None
        return Identity(
            identity_id=identity_data['id'],
            name=identity_data['name'],
            provider_id=identity_data['providerId'],
            email=identity_data['email'],
            blocked=identity_data['blocked'],
            user=User(
                user_id=identity_data['user']['id'],
                name=identity_data['user']['name'],
                is_superuser=identity_data['user']['isSuperuser'],
            ) if identity_data.get('user') else None,
        )

    def get_identity_from_provider(
            self,
            provider_id: str,
            id_token: str,
    ) -> Identity:
        identity_data = self.api.query(
            name='identityFromProvider',
            variables=[
                ('providerId', 'String!', provider_id),
                ('idToken', 'String!', id_token),
            ],
            body='''
                id
                name
                providerId
                email
                blocked
                user {
                    id
                    name
                    isSuperuser
                }
            ''',
        )
        return Identity(
            identity_id=identity_data['id'],
            name=identity_data['name'],
            provider_id=identity_data['providerId'],
            email=identity_data['email'],
            blocked=identity_data['blocked'],
            user=User(
                user_id=identity_data['user']['id'],
                name=identity_data['user']['name'],
                is_superuser=identity_data['user']['isSuperuser'],
            ) if identity_data.get('user') else None,
        )

    def get_users(self) -> list[User]:
        users_data = self.api.query(
            name='users',
            body='''
                id
                name
                isSuperuser
            ''',
        )
        return [
            User(
                user_id=user_data['id'],
                name=user_data['name'],
                is_superuser=user_data['isSuperuser'],
            ) for user_data in users_data
        ]

    def get_user(self, user_id: str) -> Optional[User]:
        user_data = self.api.query(
            name='user',
            variables=[
                ('id', 'ID!', user_id),
            ],
            body='''
                id
                name
                isSuperuser
            ''',
        )
        if not user_data:
            return None
        return User(
            user_id=user_data['id'],
            name=user_data['name'],
            is_superuser=user_data['isSuperuser'],
        )

    def get_user_from_cookies(
            self,
            token: Optional[str],
            secret: Optional[str],
    ) -> Optional[User]:
        if not token or not secret:
            return None
        user_data: dict = self.api.query(
            name='userFromCookies',
            variables=[
                ('tokenCookie', 'String!', token),
                ('secretCookie', 'String!', secret),
            ],
            body="""
                id
                name
                isSuperuser
            """,
        )
        if not user_data:
            return None
        return User(
            user_id=user_data['id'],
            name=user_data['name'],
            is_superuser=user_data['isSuperuser'],
        )

    def get_user_members(self, user: User) -> list[Member]:
        return [
            member for member in self.get_members()
            if member.user == user
        ]

    def get_user_identities(self, user: User) -> list[Identity]:
        user_data = self.api.query(
            name='user',
            variables=[
                ('id', 'ID!', user.user_id),
            ],
            body='''
                identities {
                    id
                    name
                    providerId
                    email
                    blocked
                }
            ''',
        )
        return [
            Identity(
                identity_id=identity_data['id'],
                name=identity_data['name'],
                provider_id=identity_data['providerId'],
                email=identity_data['email'],
                blocked=identity_data['blocked'],
                user=user,
            ) for identity_data in user_data['identities']
        ]

    def get_user_accounts(self, user: User) -> list[Account]:
        accounts_data = self.api.query(
            name='user',
            variables=[
                ('id', 'ID!', user.user_id),
            ],
            body='''
            accounts {
                id
                user {
                    id
                    name
                    isSuperuser
                }
                application {
                    id
                    name
                    description
                }
                enabled
                data
            }
            ''',
        )['accounts']
        return [
            Account(
                account_id=account_data['id'],
                user=User(
                    user_id=account_data['user']['id'],
                    name=account_data['user']['name'],
                    is_superuser=account_data['user']['isSuperuser'],
                ),
                application=Application(
                    application_id=account_data['application']['id'],
                    name=account_data['application']['name'],
                    description=account_data['application']['description'],
                ),
                enabled=account_data['enabled'],
                data=account_data['data'],
            )
            for account_data in accounts_data
        ]

    def get_user_account(self, user: User, application: Application) -> Optional[Account]:
        for account in self.get_user_accounts(user):
            if account.application == application:
                return account
        return None

    def get_members(self) -> list[Member]:
        members_data = self.api.query(
            name='members',
            body='''
                id
                user {
                    id
                    name
                    isSuperuser
                }
                organization {
                    id
                    name
                    namespace
                }
            ''',
        )
        return [
            Member(
                member_id=member_data['id'],
                user=User(
                    user_id=member_data['user']['id'],
                    name=member_data['user']['name'],
                    is_superuser=member_data['user']['isSuperuser'],
                ),
                organization=Organization(
                    organization_id=member_data['organization']['id'],
                    name=member_data['organization']['name'],
                    namespace=Namespace(member_data['organization']['namespace']),
                ),
            ) for member_data in members_data
        ]

    def get_member(self, member_id: str) -> Optional[Member]:
        member_data = self.api.query(
            name='member',
            variables=[
                ('id', 'ID!', member_id),
            ],
            body='''
                id
                user {
                    id
                    name
                    isSuperuser
                }
                organization {
                    id
                    name
                    namespace
                }
            ''',
        )
        if not member_data:
            return None
        return Member(
            member_id=member_data['id'],
            user=User(
                user_id=member_data['user']['id'],
                name=member_data['user']['name'],
                is_superuser=member_data['user']['isSuperuser'],
            ),
            organization=Organization(
                organization_id=member_data['organization']['id'],
                name=member_data['organization']['name'],
                namespace=Namespace(member_data['organization']['namespace']),
            ),
        )

    def get_member_from_cookies(
            self,
            token: Optional[str],
            secret: Optional[str],
    ) -> Optional[Member]:
        if not token or not secret:
            return None
        member_data: dict = self.api.query(
            name='memberFromCookies',
            variables=[
                ('tokenCookie', 'String!', token),
                ('secretCookie', 'String!', secret),
            ],
            body="""
                id
                organization {
                    id
                    name
                    namespace
                }
                user {
                    id
                    name
                    isSuperuser
                }
            """,
        )
        if not member_data:
            return None
        user_data = member_data['user']
        organization_data = member_data['organization']
        return Member(
            member_id=member_data['id'],
            organization=Organization(
                organization_id=organization_data['id'],
                name=organization_data['name'],
                namespace=Namespace(organization_data['namespace']),
            ),
            user=User(
                user_id=user_data['id'],
                name=user_data['name'],
                is_superuser=user_data['isSuperuser'],
            ),
        )

    def get_member_roles(self, member: Member) -> list[Role]:
        member_data = self.api.query(
            name='member',
            variables=[
                ('id', 'ID!', member.member_id),
            ],
            body='''
                roles {
                    id
                    name
                    description
                    organization {
                        id
                        name
                        namespace
                    }
                    inheritance
                }
            ''',
        )
        if not member_data:
            return []
        return [
            Role(
                role_id=role_data['id'],
                name=role_data['name'],
                description=role_data['description'],
                organization=Organization(
                    organization_id=role_data['organization']['id'],
                    name=role_data['organization']['name'],
                    namespace=Namespace(role_data['organization']['namespace']),
                ),
                inheritance=role_data['inheritance'],
            ) for role_data in member_data['roles']
        ]

    def get_member_authorizations(self, member: Member) -> list[Authorization]:
        member_data = self.api.query(
            name='member',
            variables=[
                ('id', 'ID!', member.member_id),
            ],
            body='''
                authorizations {
                    id
                    name
                    description
                    organization {
                        id
                        name
                        namespace
                    }
                    inheritance
                    matching
                }
            ''',
        )
        if not member_data:
            return []
        return [
            Authorization(
                authorization_id=authorization_data['id'],
                name=authorization_data['name'],
                description=authorization_data['description'],
                organization=Organization(
                    organization_id=authorization_data['organization']['id'],
                    name=authorization_data['organization']['name'],
                    namespace=Namespace(authorization_data['organization']['namespace']),
                ),
                inheritance=authorization_data['inheritance'],
                matching=Matching(authorization_data['matching']),
            ) for authorization_data in member_data['authorizations']
        ]

    def get_authorizations(self) -> list[Authorization]:
        authorizations_data = self.api.query(
            name='authorizations',
            body='''
                id
                name
                description
                organization {
                    id
                    name
                    namespace
                }
                inheritance
                matching
            ''',
        )
        return [
            Authorization(
                authorization_id=authorization_data['id'],
                name=authorization_data['name'],
                description=authorization_data['description'],
                organization=Organization(
                    organization_id=authorization_data['organization']['id'],
                    name=authorization_data['organization']['name'],
                    namespace=Namespace(authorization_data['organization']['namespace']),
                ),
                inheritance=authorization_data['inheritance'],
                matching=Matching(authorization_data['matching']),
            ) for authorization_data in authorizations_data
        ]

    def get_authorization(self, authorization_id: str) -> Optional[Authorization]:
        authorization_data = self.api.query(
            name='authorization',
            variables=[
                ('id', 'ID!', authorization_id),
            ],
            body='''
                id
                name
                description
                organization {
                    id
                    name
                    namespace
                }
                inheritance
                matching
            ''',
        )
        if not authorization_data:
            return None
        return Authorization(
            authorization_id=authorization_data['id'],
            name=authorization_data['name'],
            description=authorization_data['description'],
            organization=Organization(
                organization_id=authorization_data['organization']['id'],
                name=authorization_data['organization']['name'],
                namespace=Namespace(authorization_data['organization']['namespace']),
            ),
            inheritance=authorization_data['inheritance'],
            matching=Matching(authorization_data['matching']),
        )

    def get_authorization_permissions(self, authorization: Authorization) -> list[Permission]:
        authorization_data = self.api.query(
            name='authorization',
            variables=[
                ('id', 'ID!', authorization.authorization_id),
            ],
            body='''
                permissions {
                    id
                    name
                    description
                    application {
                        id
                        name
                        description
                    }
                }
            ''',
        )
        if not authorization_data:
            return []
        return [
            Permission(
                permission_id=permission_data['id'],
                name=permission_data['name'],
                description=permission_data['description'],
                application=Application(
                    application_id=permission_data['application']['id'],
                    name=permission_data['application']['name'],
                    description=permission_data['application']['description'],
                ),
            ) for permission_data in authorization_data['permissions']
        ]

    def get_roles(self) -> list[Role]:
        roles_data = self.api.query(
            name='roles',
            body='''
                id
                name
                description
                organization {
                    id
                    name
                    namespace
                }
                inheritance
            ''',
        )
        return [
            Role(
                role_id=role_data['id'],
                name=role_data['name'],
                description=role_data['description'],
                organization=Organization(
                    organization_id=role_data['organization']['id'],
                    name=role_data['organization']['name'],
                    namespace=Namespace(role_data['organization']['namespace']),
                ),
                inheritance=role_data['inheritance'],
            ) for role_data in roles_data
        ]

    def get_role(self, role_id: str) -> Optional[Role]:
        role_data = self.api.query(
            name='role',
            variables=[
                ('id', 'ID!', role_id),
            ],
            body='''
                id
                name
                description
                organization {
                    id
                    name
                    namespace
                }
                inheritance
            ''',
        )
        if not role_data:
            return None
        return Role(
            role_id=role_data['id'],
            name=role_data['name'],
            description=role_data['description'],
            organization=Organization(
                organization_id=role_data['organization']['id'],
                name=role_data['organization']['name'],
                namespace=Namespace(role_data['organization']['namespace']),
            ),
            inheritance=role_data['inheritance'],
        )

    def get_role_authorizations(self, role: Role) -> list[Authorization]:
        role_data = self.api.query(
            name='role',
            variables=[
                ('id', 'ID!', role.role_id),
            ],
            body='''
                authorizations {
                    id
                    name
                    description
                    organization {
                        id
                        name
                        namespace
                    }
                    inheritance
                    matching
                }
            ''',
        )
        if not role_data:
            return []
        return [
            Authorization(
                authorization_id=authorization_data['id'],
                name=authorization_data['name'],
                description=authorization_data['description'],
                organization=Organization(
                    organization_id=authorization_data['organization']['id'],
                    name=authorization_data['organization']['name'],
                    namespace=Namespace(authorization_data['organization']['namespace']),
                ),
                inheritance=authorization_data['inheritance'],
                matching=Matching(authorization_data['matching']),
            ) for authorization_data in role_data['authorizations']
        ]

    def get_cookies(
            self,
            user: User = None,
            organization: Organization = None,
    ) -> dict[str, Cookie]:
        cookies_data: list[dict[str, Any]] = self.api.query(
            name='cookies',
            variables=[
                ('userId', 'ID', user.user_id if user else None),
                ('organizationId', 'ID', organization.organization_id if organization else None),
            ],
            body="""
                name
                value
                domain
                maxAge
                secure
                httpOnly
            """,
        )
        return {
            cookie_data['name']: Cookie(
                name=cookie_data['name'],
                value=cookie_data['value'],
                domain=cookie_data['domain'],
                max_age=cookie_data['maxAge'],
                secure=cookie_data['secure'],
                http_only=cookie_data['httpOnly'],
            )
            for cookie_data in cookies_data
        }

    def create_application(
            self,
            application_name: str,
            application_description: str,
    ) -> Application:
        application_data = self.api.mutation(
            name='createApplication',
            input_value={
                'name': application_name,
                'description': application_description,
            },
            body='''
            application {
                id
                name
                description
            }
            ''',
        )['application']
        return Application(
            application_id=application_data['id'],
            name=application_data['name'],
            description=application_data['description'],
        )

    def register_application(
            self,
            application_name: str,
            application_description: str,
    ) -> Application:
        application_data = self.api.mutation(
            name='registerApplication',
            input_value={
                'name': application_name,
                'description': application_description,
            },
            body='''
                application {
                    id
                    name
                    description
                }
                created
                updated
            '''
        )['application']

        return Application(
            application_id=application_data['id'],
            name=application_data['name'],
            description=application_data['description'],
        )

    def delete_application(self, application: Application) -> bool:
        application_data = self.api.mutation(
            name='deleteApplication',
            input_value={
                'applicationId': application.application_id,
            },
            body='''
                deleted
            '''
        )
        return application_data['deleted']  # type: ignore

    def create_permission(
            self,
            application: Application,
            permission_name: str,
            permission_description: str,
    ) -> Permission:
        permission_data = self.api.mutation(
            name='createPermission',
            input_value={
                'applicationId': application.application_id,
                'name': permission_name,
                'description': permission_description,
            },
            body='''
            permission {
                id
                name
                description
                application {
                    id
                    name
                    description
                }
            }
            ''',
        )['permission']
        return Permission(
            permission_id=permission_data['id'],
            name=permission_data['name'],
            description=permission_data['description'],
            application=Application(
                application_id=permission_data['application']['id'],
                name=permission_data['application']['name'],
                description=permission_data['application']['description'],
            ),
        )

    def register_permission(
            self,
            application: Application,
            permission_name: str,
            permission_description: str,
    ) -> Permission:
        permission_data = self.api.mutation(
            name='registerPermission',
            input_value={
                'applicationId': application.application_id,
                'name': permission_name,
                'description': permission_description,
            },
            body='''
                permission {
                    id
                    name
                    description
                }
                created
                updated
            '''
        )['permission']

        return Permission(
            application=application,
            permission_id=permission_data['id'],
            name=permission_data['name'],
            description=permission_data['description'],
        )

    def delete_permission(self, permission: Permission) -> bool:
        permission_data = self.api.mutation(
            name='deletePermission',
            input_value={
                'permissionId': permission.permission_id,
            },
            body='''
                deleted
            '''
        )

        return permission_data['deleted']  # type: ignore

    def create_account(self, application: Application, user: User) -> Account:
        account_data = self.api.mutation(
            name='createAccount',
            input_value={
                'applicationId': application.application_id,
                'userId': user.user_id,
            },
            body='''
            account {
                id
                user {
                    id
                    name
                    isSuperuser
                }
                application {
                    id
                    name
                    description
                }
                enabled
                data
            }
            ''',
        )['account']

        return Account(
            account_id=account_data['id'],
            user=User(
                user_id=account_data['user']['id'],
                name=account_data['user']['name'],
                is_superuser=account_data['user']['isSuperuser'],
            ),
            application=Application(
                application_id=account_data['application']['id'],
                name=account_data['application']['name'],
                description=account_data['application']['description'],
            ),
            enabled=account_data['enabled'],
            data=account_data['data'],
        )

    def update_account(self, account: Account, set_enabled: bool = None) -> Account:
        account_data = self.api.mutation(
            name='updateAccount',
            input_value={
                'accountId': account.account_id,
                'setEnabled': set_enabled,
            },
            body='''
            account {
                id
                user {
                    id
                    name
                    isSuperuser
                }
                application {
                    id
                    name
                    description
                }
                enabled
                data
            }
            ''',
        )['account']

        return Account(
            account_id=account_data['id'],
            user=User(
                user_id=account_data['user']['id'],
                name=account_data['user']['name'],
                is_superuser=account_data['user']['isSuperuser'],
            ),
            application=Application(
                application_id=account_data['application']['id'],
                name=account_data['application']['name'],
                description=account_data['application']['description'],
            ),
            enabled=account_data['enabled'],
            data=account_data['data'],
        )

    def delete_account(self, account: Account) -> bool:
        account_data = self.api.mutation(
            name='deleteAccount',
            input_value={
                'accountId': account.account_id,
            },
            body='''
                deleted
            '''
        )
        return account_data['deleted']  # type: ignore

    def create_organization(
            self,
            name: str,
            namespace: Namespace,
    ) -> Organization:
        organization_data = self.api.mutation(
            name='createOrganization',
            input_value={
                'name': name,
                'namespace': str(namespace),
            },
            body='''
            organization {
                id
                name
                namespace
            }
            ''',
        )['organization']

        return Organization(
            organization_id=organization_data['id'],
            name=organization_data['name'],
            namespace=Namespace(organization_data['namespace']),
        )

    def delete_organization(self, organization: Organization) -> bool:
        organization_data = self.api.mutation(
            name='deleteOrganization',
            input_value={
                'organizationId': organization.organization_id,
            },
            body='''
                deleted
            '''
        )
        return organization_data['deleted']  # type: ignore

    def create_user(
            self,
            name: str,
    ) -> User:
        user_data = self.api.mutation(
            name='createUser',
            input_value={
                'name': name,
            },
            body='''
            user {
                id
                name
                isSuperuser
            }
            ''',
        )['user']

        return User(
            user_id=user_data['id'],
            name=user_data['name'],
            is_superuser=user_data['isSuperuser'],
        )

    def create_user_from_identity(
            self,
            identity: Identity,
    ) -> User:
        user_data = self.api.mutation(
            name='createUserFromIdentity',
            input_value={
                'identityId': identity.identity_id,
            },
            body='''
            user {
                id
                name
                isSuperuser
            }
            ''',
        )['user']

        return User(
            user_id=user_data['id'],
            name=user_data['name'],
            is_superuser=user_data['isSuperuser'],
        )

    def delete_user(self, user: User) -> bool:
        user_data = self.api.mutation(
            name='deleteUser',
            input_value={
                'userId': user.user_id,
            },
            body='''
                deleted
            '''
        )

        return user_data['deleted']  # type: ignore

    def update_user(
            self,
            user: User,
            add_identity: Identity = None,
            remove_identity: Identity = None,
    ) -> User:
        user_data = self.api.mutation(
            name='updateUser',
            input_value={
                'userId': user.user_id,
                'addIdentityId': add_identity.identity_id if add_identity else None,
                'removeIdentityId': remove_identity.identity_id if remove_identity else None,
            },
            body='''
            user {
                id
                name
                isSuperuser
            }
            ''',
        )['user']

        return User(
            user_id=user_data['id'],
            name=user_data['name'],
            is_superuser=user_data['isSuperuser'],
        )

    def delete_identity(self, identity: Identity) -> bool:
        identity_data = self.api.mutation(
            name='deleteIdentity',
            input_value={
                'identityId': identity.identity_id,
            },
            body='''
                deleted
            '''
        )
        return identity_data['deleted']  # type: ignore

    def create_member(
            self,
            user: User,
            organization: Organization,
    ) -> Member:
        member_data = self.api.mutation(
            name='createMember',
            input_value={
                'userId': user.user_id,
                'organizationId': organization.organization_id,
            },
            body='''
            member {
                id
            }
            ''',
        )['member']

        return Member(
            member_id=member_data['id'],
            user=user,
            organization=organization,
        )

    def update_member(
            self,
            member: Member,
            add_authorization: Authorization = None,
            remove_authorization: Authorization = None,
            add_role: Role = None,
            remove_role: Role = None,
    ) -> Member:
        self.api.mutation(
            name='updateMember',
            input_value={
                'memberId': member.member_id,
                'addAuthorizationId': add_authorization.authorization_id if add_authorization else None,
                'removeAuthorizationId': remove_authorization.authorization_id if remove_authorization else None,
                'addRoleId': add_role.role_id if add_role else None,
                'removeRoleId': remove_role.role_id if remove_role else None,
            },
            body='''
            member {
                id
            }
            ''',
        )

        return member

    def delete_member(self, member: Member) -> bool:
        member_data = self.api.mutation(
            name='deleteMember',
            input_value={
                'memberId': member.member_id,
            },
            body='''
                deleted
            '''
        )
        return member_data['deleted']  # type: ignore

    def create_role(
            self,
            organization: Organization,
            name: str,
            description: str,
            inheritance: bool,
    ) -> Role:
        role_data = self.api.mutation(
            name='createRole',
            input_value={
                'organizationId': organization.organization_id,
                'name': name,
                'description': description,
                'inheritance': inheritance,
            },
            body='''
            role {
                id
                name
                description
                inheritance
            }
            ''',
        )['role']

        return Role(
            role_id=role_data['id'],
            name=role_data['name'],
            description=role_data['description'],
            inheritance=role_data['inheritance'],
            organization=organization,
        )

    def update_role(
            self,
            role: Role,
            add_authorization: Authorization = None,
            remove_authorization: Authorization = None,
    ) -> Role:
        role_data = self.api.mutation(
            name='updateRole',
            input_value={
                'roleId': role.role_id,
                'addAuthorizationId': add_authorization.authorization_id if add_authorization else None,
                'removeAuthorizationId': remove_authorization.authorization_id if remove_authorization else None,
            },
            body='''
            role {
                id
                name
                description
                inheritance
            }
            ''',
        )['role']

        return Role(
            role_id=role_data['id'],
            name=role_data['name'],
            description=role_data['description'],
            inheritance=role_data['inheritance'],
            organization=role.organization,
        )

    def delete_role(self, role: Role) -> bool:
        role_data = self.api.mutation(
            name='deleteRole',
            input_value={
                'roleId': role.role_id,
            },
            body='''
                deleted
            '''
        )
        return role_data['deleted']  # type: ignore

    def create_authorization(
            self,
            organization: Organization,
            name: str,
            description: str,
            inheritance: bool,
            matching: Matching,
    ) -> Authorization:
        authorization_data = self.api.mutation(
            name='createAuthorization',
            input_value={
                'organizationId': organization.organization_id,
                'name': name,
                'description': description,
                'inheritance': inheritance,
                'matching': matching.value,
            },
            body='''
            authorization {
                id
                name
                description
                inheritance
                matching
            }
            ''',
        )['authorization']

        return Authorization(
            authorization_id=authorization_data['id'],
            name=authorization_data['name'],
            description=authorization_data['description'],
            inheritance=authorization_data['inheritance'],
            matching=Matching(authorization_data['matching']),
            organization=organization,
        )

    def update_authorization(
            self,
            authorization: Authorization,
            add_permission: Permission = None,
            remove_permission: Permission = None,
    ) -> Authorization:
        self.api.mutation(
            name='updateAuthorization',
            input_value={
                'authorizationId': authorization.authorization_id,
                'addPermissionId': add_permission.permission_id if add_permission else None,
                'removePermissionId': remove_permission.permission_id if remove_permission else None,
            },
            body='''
            authorization {
                id
            }
            ''',
        )

        return authorization

    def delete_authorization(self, authorization: Authorization) -> bool:
        authorization_data = self.api.mutation(
            name='deleteAuthorization',
            input_value={
                'authorizationId': authorization.authorization_id,
            },
            body='''
                deleted
            '''
        )
        return authorization_data['deleted']  # type: ignore
