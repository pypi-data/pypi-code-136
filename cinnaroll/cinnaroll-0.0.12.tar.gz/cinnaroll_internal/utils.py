import inspect
import re
from typing import List, Any, Optional, Callable


def append_if_not_none(iterable: List[Any], item: Optional[Any]) -> None:
    if item is not None:
        iterable.append(item)


def get_function_code(function: Callable) -> str:  # type: ignore
    code = inspect.getsource(function)
    lines = code.split("\n")
    chars_to_trim = len(lines[0]) - len(lines[0].lstrip())
    lines = [line[chars_to_trim:] for line in lines]
    # delete @staticmethod etc.
    while f'def {function.__name__}(' not in lines[0]:
        lines = lines[1:]
    return '\n'.join(lines)


def is_function_implemented(function: Callable) -> bool:  # type: ignore
    code = get_function_code(function)
    lines = code.split("\n")
    lines[0] = re.sub(re.compile("#.*"), "", lines[0]).rstrip(" ")
    if lines[0][-3:] == "...":
        return False
    if lines[1].lstrip() in ("pass", "..."):
        return False
    return True
