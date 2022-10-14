import json
import typing
from typing import TypeVar, Callable, Awaitable, ParamSpec, Any, Type

from httpx import Response, codes
from pydantic import BaseModel

from wrapzor.errors import ArgsError, Message

B = TypeVar('B', bound=BaseModel)
U = TypeVar('U', bound=BaseModel | Response)
P = ParamSpec('P')


def verify_data(
        input_model: typing.Type[B] | None = None,
        output_model: typing.Type[U] = Response,
):
    def function_verify_data(
            f: Callable[P, Awaitable[Response]]
    ):
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> U:
            if input_model is not None:
                if "data" in kwargs:

                    data = kwargs["data"]
                    del kwargs["data"]
                    if not isinstance(data, dict):
                        raise TypeError("Argument data must be a dict")

                    kwargs["data"] = json.dumps(data)
                    _ = input_model(**data)
                    response = await f(*args, **kwargs)
                elif "params" in kwargs:
                    params = kwargs['params']
                    if not isinstance(params, dict):
                        raise TypeError('params must be a dict')
                    _ = input_model(**params)
                    response = await f(*args, **kwargs)
                else:
                    raise ArgsError(Message.input_data_missing)
            else:
                response = await f(*args, **kwargs)

            # if output_model is not None and response.status_code != codes.NO_CONTENT:
            if output_model is Response:
                return response # type: ignore

            response_data = response.json()
            if not isinstance(response_data, dict):
                raise TypeError("Response json -data- must be a dict")
            return output_model(**response_data) # type: ignore

        return wrapper

    return function_verify_data
