
"""
TroveFM is an online store and headless CMS.

Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""


from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import HTTPException
from fastapi import status
from typing import Optional
from typing import Dict

from loguru import logger


class OAuth2PasswordBearerSecure(OAuth2):
    """A custom implementation of the OAuth2 scheme from FastAPI

    When called, this class will retrieve the JWT access_token from either:
        - A cookie, if a cookie is presented that contains an access_token
        - The 'Authorization' header of the request, if no cookie is found, but
          the header is present

    JWT access tokens are a convenient and popular way to maintain access after
    a person successfully authenticates with their username and password.
    Unfortunately, tokens are often set in the browser's Local Storage, from
    where they are retrieved and inserted into the 'Authorization' header by the
    http client used by the JavaScript framework that implements the GUI on the
    frontend.  This is a dangerous practice that leaves the access token suceptible
    to theft via a cross-site scripting (XSS) attack.

    In Trove, a check is made at login to see if the client supports cookies.  If
    a cookie can be set in the client, then we set a cookie that contains the access
    token, and set the cookie to 'httponly', meaning that it cannot be accessed via
    JavaScript.  The cookie will be automatically returned by the browser on
    subsequent requests, and the access token will be read from there.

    If the client does not support cookie storage, then we will return the access
    token in the JSON response to the login form submission.  It is expected that
    this type of client will have a way of securing the token and presenting it
    in the 'Authorization' header on subsequent requests.

    In the unlikely event that an API client presents BOTH a cookie containing an
    access token AND an 'Authorization' header with an access token, the token in
    the cookie will take precedence.
    """

    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(
            flows=flows,
            scheme_name=scheme_name,
            description=description,
            auto_error=auto_error
        )

    async def __call__(self, request: Request) -> Optional[str]:
        if authorization := request.cookies.get("access_token"):
            logger.info("Authorization token found in HTTP cookie.")
        elif authorization := request.headers.get("Authorization"):
            logger.info("Authorization token found in HTTP header.")
        else:
            authorization = None

        scheme, param = get_authorization_scheme_param(authorization)

        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param
