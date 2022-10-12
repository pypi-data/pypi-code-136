# Copyright (C) 2022 Cochise Ruhulessin
# 
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import pydantic
from ckms.types import ClaimSet
from cbra.ext.oauth2.types import RFC9068Token
from cbra.ext.oauth2.types import IPrincipal


class ServicePrincipal(IPrincipal, RFC9068Token): # type: ignore
    __module__: str = 'libwebid.lib'
    sub: str

    @pydantic.root_validator(pre=True)
    def preprocess(
        cls,
        values: dict[str, Any]
    ) -> dict[str, Any]:
        client_id = values.get('client_id')
        sub = values.get('sub')
        if sub != client_id:
            raise ValueError("The 'client_id' claim must match the 'sub' claim.")
        return values

    @classmethod
    def fromclaimset(cls, claims: ClaimSet) -> 'ServicePrincipal':
        return cls.parse_obj(claims.dict())

    def get_current_scope(self) -> set[str]:
        """Return the scope that is currrently granted to the principal."""
        return set(self.scope)

    def has_scope(self, scope: str | set[str]) -> bool:
        if isinstance(scope, str):
            scope = {scope}
        return bool(set(self.scope) >= scope)

    def is_authenticated(self) -> bool:
        return True

    def is_service(self) -> bool:
        return True

    def is_subject(self) -> bool:
        return False