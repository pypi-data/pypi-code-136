# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime

import pydantic


class AuthorizedScope(pydantic.BaseModel):
    """Represents a scope that a Resource Owner has granted to a specific
    Client.
    """
    name: str = pydantic.Field(
        default=...
    )

    authorized: datetime.datetime = pydantic.Field(
        default_factory=datetime.datetime.utcnow
    )

    expires: datetime.datetime | None = pydantic.Field(
        default=None
    )

    def is_expired(self, now: datetime.datetime | None = None) -> bool:
        """Return a boolean indicating if the scope is expired."""
        now = now or datetime.datetime.utcnow()
        return self.expires is not None and (self.expires <= now)