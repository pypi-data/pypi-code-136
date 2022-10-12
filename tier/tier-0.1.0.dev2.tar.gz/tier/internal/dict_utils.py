# std
from typing import Any, List, Optional as Opt, Union


def normalize_keys(opt_keys_or_path: Opt[Union[str, List[str]]] = None) -> List[str]:
    if opt_keys_or_path is None:
        return []
    elif isinstance(opt_keys_or_path, str):
        return opt_keys_or_path.split('.')
    elif isinstance(opt_keys_or_path, list):
        return opt_keys_or_path
    else:
        raise TypeError(f'str or list expected but got {type(opt_keys_or_path)}')


def safeget(
        d: dict,
        path: Union[str, List[str]],
        default: Opt[Any] = None,
) -> Any:
    path = normalize_keys(path)
    tmp = d
    for key in path:
        if isinstance(tmp, dict) and key in tmp:
            tmp = tmp[key]
        else:
            return default
    return tmp


def safeset(
        d: dict,
        path: Union[str, List[str]],
        value: Any,
) -> dict:
    if isinstance(path, str):
        path = path.split('.')
    tmp = d
    for key in path[:-1]:
        if key not in tmp:
            tmp[key] = {}
        tmp = tmp[key]
    tmp[path[-1]] = value
    return d
