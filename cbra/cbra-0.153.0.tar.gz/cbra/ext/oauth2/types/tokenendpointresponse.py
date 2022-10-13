# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from .error import Error
from .iresponse import IResponse
from .tokenresponse import TokenResponse


class TokenEndpointResponse(pydantic.BaseModel, IResponse):
    __root__: TokenResponse | Error

    @property
    def access_token(self) -> str:
        if not isinstance(self.__root__, TokenResponse):
            raise TypeError
        return self.__root__.access_token

    @property
    def error(self) -> str:
        if not isinstance(self.__root__, Error):
            raise TypeError
        return self.__root__.error

    @property
    def error_description(self) -> str | None:
        if not isinstance(self.__root__, Error):
            raise TypeError
        return self.__root__.error_description

    @property
    def refresh_token(self) -> str | None:
        if not isinstance(self.__root__, TokenResponse):
            raise TypeError
        return self.__root__.refresh_token

    def is_error(self) -> bool:
        return self.__root__.is_error()