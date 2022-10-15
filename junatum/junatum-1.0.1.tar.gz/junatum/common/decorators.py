#!/usr/bin/env python3
import inspect
from functools import wraps
from typing import Iterable


def ensure_positive_number(*fields: Iterable):
    """양수를 강제할 때 사용하는 데코레이터

    :param fields: Iterable 검사하고 싶은 필드명
    """

    def decorator_wrapper(method):
        @wraps(method)
        def method_wrapper(*args, **kwargs):
            if not fields:
                raise TypeError

            sig = inspect.signature(method)
            values = sig.bind(*args, **kwargs)
            for field, value in values.arguments.items():
                if field not in fields:
                    continue
                if not isinstance(value, int):
                    raise ValueError(f'Argument must be integer type : {field}')
                if value < 1:
                    raise ValueError(f'Arguments out of range : {field} ({value})')

            return method(*args, **kwargs)

        return method_wrapper

    return decorator_wrapper
