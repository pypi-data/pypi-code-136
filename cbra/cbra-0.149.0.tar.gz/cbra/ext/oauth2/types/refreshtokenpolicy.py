# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import enum


class RefreshTokenPolicy(str, enum.Enum):
    """Describes the refresh policy for refresh tokens."""

    #: The token has a fixed expiration date, after which the resource
    #: owner must authorize the scope again.
    fixed = 'fixed'

    #: The token is valid for the number of seconds after it is issued,
    #: specified by the client.
    rolling = 'rolling'
