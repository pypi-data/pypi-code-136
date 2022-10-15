import inspect
from typing import Any, Union

from pydantic.fields import Undefined, UndefinedType


def parse(value: Any, /) -> Union[Any, UndefinedType]:
    if value is inspect.Parameter.empty:
        return Undefined
    else:
        return value
