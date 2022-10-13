# Copyright (c) 2022 Shapelets.io
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from blacksheep.server.controllers import ApiController, delete, get, post, put
from guardpost.asynchronous.authentication import Identity
from requests import Session
from typing import List, Optional

from . import http_docs, IUsersService
from ..docs import docs
from ..model import PrincipalId, ResolvedPrincipalId, UserAttributes, UserId, UserProfile


class UsersHttpServer(ApiController):
    def __init__(self, svr: IUsersService) -> None:
        self._svr = svr
        super().__init__()

    @classmethod
    def route(cls) -> Optional[str]:
        return '/api/users'

    @get("/")
    async def user_list(self) -> List[UserProfile]:
        return self._svr.get_all()

    @delete("/")
    async def delete_all_users(self) -> bool:
        return self._svr.delete_all()

    @post("/checkNickName")  # description="Checks if the proposed username already exists"
    @docs(http_docs.nickname_doc)
    async def check_nickname(self, nickName: str) -> bool:
        return self._svr.nickname_exists(nickName)

    @get("/me")
    @docs(http_docs.me_doc)
    async def my_details(self, identity: Identity) -> UserProfile:
        if identity:
            return self._svr.get_user_details(identity.claims.get("userId"))
        return False

    @get("/{id}")
    async def get_user_details(self, id: int) -> Optional[UserProfile]:
        return self._svr.get_user_details(id)

    @put("/{id}")
    async def save_user_details(self, id: int, details: UserProfile) -> Optional[UserProfile]:
        self._svr.save_user_details(id, details)

    @delete("/{id}")
    async def delete_user(self, id: int):
        self._svr.delete(id)

    @get("/{id}/groups")
    async def get_user_groups(self, id: int):
        pass

    @get("/{id}/principals")
    async def get_user_principals(self, id: int) -> List[PrincipalId]:
        return self._svr.get_principals(id)


class UsersHttpProxy(IUsersService):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self) -> List[UserProfile]:
        users = self.session.get('/api/users/')
        return users

    def create(self, attributes: UserAttributes, principal: Optional[PrincipalId]) -> UserProfile:
        pass

    def delete_user(self, id: int):
        self.session.delete('/api/users/{id}', params=[("id", id)])

    def delete_all(self) -> bool:
        self.session.delete('/api/users/')
        return True

    def get_user_details(self, id: int) -> Optional[UserProfile]:
        return self.session.get('/api/users/{id}', params=[("id", id)])

    def save_user_details(self, id: int, details: UserProfile) -> Optional[UserProfile]:
        self.session.put('/api/users/{id}', params=[("id", id), ("details", details)])
        pass

    @docs(http_docs.nickname_doc)
    def nickname_exists(self, nickName: str) -> bool:
        return self.session.get('/api/users/checkNickName', params=[("nickName", nickName)])

    def get_principals(self, id: int) -> List[PrincipalId]:
        return self.session.get('/api/users/{id}/principals', params=[("id", id)])

    def dissociate_principal(self, principal: PrincipalId):
        pass

    def verify_principal(self, resolved_principal: ResolvedPrincipalId) -> bool:
        pass

    def resolve_principal(self, scope: str, pid: str) -> Optional[ResolvedPrincipalId]:
        pass

    def get_user_groups(self, id: int):
        response = self.session.get('/api/users/{id}/groups', params=[("id", id)])
        pass

    @docs(http_docs.me_doc)
    def my_details(self) -> UserProfile:
        response = self.session.get('/api/users/me')
        return UserProfile(uid=-1, nickName="pepe")
