# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic
from ckms.jose import PayloadCodec
from unimatrix.exceptions import CanonicalException

from .invalidrefreshtoken import InvalidRefreshToken


class RefreshTokenIdentifier(pydantic.BaseModel):
    authorization_id: int
    client_id: int | str
    id: int

    @classmethod
    def parse_jwt(
        cls,
        client_id: int | str,
        token: str
    ) -> 'RefreshTokenIdentifier':
        try:
            _, jwt = PayloadCodec.introspect(
                token=token,
                accept={"rt+jwt"}
            )
            if jwt is None:
                raise InvalidRefreshToken
            jwt.verify()
            authorization_id = int(jwt.extra.get('authorization_id')) # type: ignore
            token_id = int(jwt.iss) # type: ignore
        except (CanonicalException, ValueError, TypeError):
            raise InvalidRefreshToken
        return cls(
            client_id=client_id,
            id=token_id,
            authorization_id=authorization_id
        )