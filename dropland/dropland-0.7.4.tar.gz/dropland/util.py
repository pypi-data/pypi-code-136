import hashlib
import os
import re
from asyncio import get_running_loop, iscoroutinefunction, run as run_main
from functools import partial
from importlib import import_module
from typing import Any, Callable, Dict, Iterable, List

import ujson


def import_path(dotted_path: str):
    if ':' in dotted_path:
        module_path, attr_path = dotted_path.rsplit(':', maxsplit=1)
    else:
        module_path, attr_path = dotted_path.rsplit('.', maxsplit=1)

    module = import_module(module_path)

    if ':' in dotted_path:
        result = module
        for attr_name in attr_path.rsplit('.'):
            result = getattr(result, attr_name)
        return result

    return getattr(module, attr_path)


def lazy_import(dotted_path: str, callable: bool = False, as_partial: bool = False):
    if callable:
        def inner(*args, **kwargs):
            if as_partial:
                return partial(import_path(dotted_path), *args, **kwargs)
            return import_path(dotted_path)(*args, **kwargs)
    else:
        def inner():
            return import_path(dotted_path)
    return inner


def iscoroutinefunction_partial(f):
    while isinstance(f, partial):
        f = f.func
    return iscoroutinefunction(f)


def invoke_sync(func, *args, **kwargs):
    try:
        loop = get_running_loop()
    except RuntimeError:
        loop = None

    if iscoroutinefunction_partial(func):
        if loop:
            return loop.create_task(func(*args, **kwargs))
        else:
            return run_main(func(*args, **kwargs))
    else:
        return func(*args, **kwargs)


async def invoke_async(func, *args, **kwargs):
    if iscoroutinefunction_partial(func):
        return await func(*args, **kwargs)
    else:
        loop = get_running_loop()
        func = partial(func, *args, **kwargs)
        return await loop.run_in_executor(None, func)


def snake2kebab(string: str) -> str:
    return re.sub('_', '-', string)


def kebab2snake(string: str) -> str:
    return re.sub('-', '_', string)


def snake2camel(string: str, upper: bool = False) -> str:
    result = []

    for i, word in enumerate(string.split('_')):
        if upper or i > 0:
            word = word.capitalize()
        result.append(word)

    return ''.join(result)


def default_value(type_: type):
    def getter(value: Any, default: Any):
        return type_(value) if value is not None else default
    return getter


def expandvars_dict(settings_dict):
    """Expands all environment variables in a settings dictionary."""
    return dict((key, os.path.expandvars(value)) for key, value in settings_dict.items())


def prepare_enum_keys(enum_class):
    return [snake2kebab(str(e.value).lower()) for e in enum_class]


def dict_values_to_str(data: dict):
    result = dict()

    for k, v in data.items():
        if isinstance(v, str):
            pass
        elif isinstance(v, dict):
            v = dict_values_to_str(v)
        elif isinstance(v, list):
            v = [str(i) for i in v]
        else:
            v = str(v)

        result[str(k)] = v

    return result


def build_dict_from_dotted_keys(
        iterable: Iterable, key_getter: Callable[[Any], Any],
        value_getter: Callable[[Any], Any])\
        -> Dict[str, Any]:
    result = {}

    for obj in iterable:
        keys = key_getter(obj).split('.')
        cur_dict = result

        for key in keys[:-1]:
            if key not in cur_dict:
                cur_dict[key] = {}

            if not isinstance(cur_dict[key], dict):
                cur_dict[key] = {'.': cur_dict[key]}
            cur_dict = cur_dict[key]

        cur_dict[keys[-1]] = value_getter(obj)

    return result


def build_dotted_keys_from_dict(dict_: Dict[str, Any], root_key: str = None) -> Dict[str, Any]:
    def traverse(key_stack: List[str], values: Dict[str, Any]) -> Dict[str, Any]:
        res = {}

        for k, v in values.items():
            if isinstance(v, dict):
                res.update(traverse(key_stack + [k], v))
            elif isinstance(v, list):
                for i in v:
                    i = traverse(key_stack + [k], i)
                    if isinstance(i, dict):
                        res |= i
            else:
                res['.'.join(key_stack + [k])] = v

        return res

    return traverse([root_key] if root_key else [], dict_)


def obj_dict_to_str_dict(data: dict, value_getter: Callable[[Any], Any]):
    def traverse(values: Dict[str, Any]) -> Dict[str, Any]:
        res = {}

        for k, v in values.items():
            if isinstance(v, dict):
                res[k] = traverse(v)
            elif v is None:
                pass
            else:
                res[k] = value_getter(v)

        return res

    return traverse(data)


def calculate_digest(data: Any, size: int = 0) -> str:
    if isinstance(data, dict):
        dumped = ujson.dumps(dict_values_to_str(data))
    else:
        dumped = str(data)

    dumped = dumped.encode('utf-8')
    size = size if 0 < size <= hashlib.blake2b.MAX_DIGEST_SIZE else 4 + int(len(dumped) / 32)
    digest_size = min(hashlib.blake2b.MAX_DIGEST_SIZE, size)
    hash_sum = hashlib.blake2b(dumped, digest_size=digest_size)
    return hash_sum.hexdigest()
