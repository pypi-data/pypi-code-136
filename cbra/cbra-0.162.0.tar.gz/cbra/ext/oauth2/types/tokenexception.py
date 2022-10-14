# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi


class TokenException(Exception):
    __module__: str = 'cbra.ext.oauth2.types'
    code: str
    description: str | None = None

    def __init__(self, code: str, description: str | None = None):
        self.code = code
        self.description = description

    def as_response(self) -> fastapi.responses.JSONResponse:
        return fastapi.responses.JSONResponse(
            status_code=400,
            content={
                'error': self.code,
                'error_description': self.description or (
                    "The server refuses to disclose any further information regarding "
                    "the error condition."
                )
            }
        )