import inspect
import re
from typing import List, Any, Optional, Callable


def append_if_not_none(iterable: List[Any], item: Optional[Any]) -> None:
    if item is not None:
        iterable.append(item)


# todo: unittest
def get_uncommented_lines(code: str) -> List[str]:
    uncommented_code = re.sub(re.compile("( *#.*\n)|\"\"\"(.|\n)*\"\"\""), "", code)
    lines = uncommented_code.split("\n")
    output_lines: List[str] = []

    for line in lines:
        if len(line.lstrip()):
            output_lines.append(line)

    output_lines.append("")

    return output_lines


def get_function_code_without_comments(function: Callable) -> str:  # type: ignore
    code = inspect.getsource(function)
    lines = get_uncommented_lines(code)

    chars_to_trim = len(lines[0]) - len(lines[0].lstrip())
    lines = [line[chars_to_trim:] for line in lines]
    # delete @staticmethod etc.
    while f'def {function.__name__}(' not in lines[0]:
        lines = lines[1:]
    return '\n'.join(lines)


def is_function_implemented(function: Callable) -> bool:  # type: ignore
    code = get_function_code_without_comments(function)
    lines = get_uncommented_lines(code)

    lines[0] = re.sub(re.compile("#.*"), "", lines[0]).rstrip(" ")
    if lines[0][-3:] == "...":
        return False
    if lines[1].lstrip() in ("pass", "..."):
        return False
    return True
