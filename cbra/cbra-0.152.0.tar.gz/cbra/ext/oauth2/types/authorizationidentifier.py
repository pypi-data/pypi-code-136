# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import dataclasses


@dataclasses.dataclass
class AuthorizationIdentifier:
    """Identifies the :class:`~cbra.ext.oauth2.types.Authorization`
    given to a specific Client by the Resource Owner.
    """
    client_id: str
    sub: int | str