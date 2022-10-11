import itertools
import os
import re
from typing import Any, Dict, List, Tuple, Optional

import pydantic.dataclasses

OKGREEN = "\033[92m"
OKRED = "\033[0;31m"
ENDC = "\033[0m"


@pydantic.dataclasses.dataclass
class Suggestion:
    """
    Suggestion for rewriting Ansible task
    """

    task_args: Dict[str, Any]
    file: str
    start_mark: int
    end_mark: int
    suggestion: Dict[str, Any]

    @classmethod
    def from_task(cls, task: Any, suggestion: Dict[str, Any]) -> "Suggestion":
        """
        :param task: Ansible task content
        :param suggestion: Suggestion as dict with action to do and data to use for update
        """
        task_args = task["task_args"]
        return cls(
            task_args=task_args,
            file=task["spotter_metadata"]["file"],
            start_mark=task["spotter_metadata"]["start_mark_index"],
            end_mark=task["spotter_metadata"]["end_mark_index"],
            suggestion=suggestion
        )


def _update_content(content: str, suggestion: Suggestion, colorize: bool) -> Optional[Tuple[str, int]]:
    """
    Update task content
    :param content: Old task content
    :param suggestion: Suggestion object for a specific task
    :param colorize: If True color things that will be changed
    :return: Tuple with updated content and content length difference, or none if matching failed.
    """
    suggestion_dict = suggestion.suggestion
    if suggestion_dict.get("action") != "FIX_FQCN":
        return content, 0

    part = content[suggestion.start_mark:suggestion.end_mark]
    before = suggestion_dict["data"]["before"]
    after = suggestion_dict["data"]["after"]
    regex = rf"([\t ]*)({before})(\s*:\s*)"

    replacement = f"{OKGREEN}{after}{ENDC}" if colorize else after
    match = re.search(regex, part, re.MULTILINE)
    if match is None:
        print("Applying suggestion failed: could not find string to replace.")
        return None

    s_index, e_index = match.span(2)
    end_content = content[:suggestion.start_mark + s_index] + replacement + content[suggestion.start_mark + e_index:]
    return end_content, len(replacement) - len(before)


def update_files(suggestions: List[Suggestion]) -> None:
    """
    Update files by following suggestions
    :param suggestions: List of suggestions as Suggestion objects
    """
    get_file_func = lambda x: x.file  # pylint: disable=unnecessary-lambda-assignment
    files = [(file, list(tasks)) for file, tasks in itertools.groupby(suggestions, get_file_func)]

    get_inode_func = lambda x: os.stat(x[0]).st_ino  # pylint: disable=unnecessary-lambda-assignment
    inodes = [next(group) for _, group in itertools.groupby(sorted(files, key=get_inode_func), get_inode_func)]

    for file, tasks in inodes:
        tasks_reversed = list(reversed(tasks))
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        end_content = content
        try:
            for task in tasks_reversed:
                update_result = _update_content(end_content, task, False)
                if update_result is None:
                    continue
                end_content, _ = update_result
        except Exception:  # pylint: disable=broad-except
            print(file)

        if end_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(end_content)
