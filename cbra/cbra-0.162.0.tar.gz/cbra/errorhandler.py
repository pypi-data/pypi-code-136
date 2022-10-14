# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import collections
import functools
import logging
from typing import NoReturn
from typing import TypeAlias
from typing import Union

import fastapi
import fastapi.exceptions
import pydantic

from .exceptions import NotFound
from .exceptions import MissingRequestBody
from .exceptions import UncaughtException
from .exceptions import UnprocessableEntity



ExceptionType: TypeAlias = Union[
    fastapi.exceptions.RequestValidationError,
    pydantic.ValidationError
]

class ErrorHandler:
    """Handlers :mod:`pydantic` and :mod:`fastapi` errors."""
    __module__: str = 'cbra.errorhandler'
    logger: logging.Logger = logging.getLogger('uvicorn')
    request: fastapi.Request

    def __init__(
        self,
        request: fastapi.Request
    ):
        self.request = request

    @functools.singledispatchmethod
    async def handle(self, exception: ExceptionType) -> NoReturn:
        raise NotImplementedError(type(exception))

    @handle.register
    async def handle_request_validation_error(
        self,
        exception: fastapi.exceptions.RequestValidationError
    ) -> NoReturn:
        """Handles a :class:`fastapi.exceptions.RequestValidationError`
        instance.
        """
        field_errors: dict[tuple[int | str, ...], set[str]] = collections.defaultdict(set)
        for error in exception.errors():
            loc, *fieldpath = error.get('loc')
            fieldpath = tuple(fieldpath)
            typ = error.get('type')
            if loc in ('path', 'query'):
                raise NotFound
            elif loc == 'body' and fieldpath:
                field_errors[fieldpath].add(typ)
            elif loc == 'body' and typ == 'value_error.missing':
                raise MissingRequestBody

        if field_errors:
            raise UnprocessableEntity(errors=field_errors)
        self.logger.exception("Caught fatal %s", type(exception).__name__)
        raise UncaughtException