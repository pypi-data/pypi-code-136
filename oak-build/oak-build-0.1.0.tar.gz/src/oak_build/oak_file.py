import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, List

from rusty_results import Result, Ok, Err, Option, Empty, Some

from oak_build.decorators import (
    TaskDeclarationsHolder,
    TaskDeclarations,
)
from oak_build.direcory_exec_context import DirectoryExecContext

DEFAULT_OAK_FILE = "oak_file.py"


@dataclass
class OakFile:
    tasks: Dict[str, Callable]
    dependencies: Dict[str, List[str]]
    aliases: Dict[str, str]
    context: Dict


class OakFileLoader:
    ALIAS_PATTERN = r"^[a-z][a-z0-9_-]*$"
    ALIAS_REGEXP = re.compile(ALIAS_PATTERN)

    @staticmethod
    def load_file(oak_file_path: Path) -> Result[OakFile, List[str]]:
        if not (oak_file_path.exists() and oak_file_path.is_file()):
            return Err([f"No such file {oak_file_path}"])

        code = compile(oak_file_path.read_text(), oak_file_path.name, "exec")
        context = {}
        with DirectoryExecContext(oak_file_path.parent), TaskDeclarationsHolder() as declarations:
            exec(code, context)
            return OakFileLoader._build_file_description(context, declarations)

    @staticmethod
    def _build_file_description(context: Dict, declarations: TaskDeclarations) -> Result[OakFile, List[str]]:
        errors = []

        tasks = declarations.tasks
        dependencies = declarations.dependencies

        aliases = {}
        for task_name, alias_list in declarations.aliases.items():
            for alias in alias_list:
                error = OakFileLoader._validate_alias(alias, task_name)
                if error.is_some:
                    errors.append(error.unwrap())
                else:
                    aliases[alias] = task_name

        if not errors:
            return Ok(OakFile(
                tasks,
                dependencies,
                aliases,
                context,
            ))
        else:
            return Err(errors)

    @staticmethod
    def _validate_alias(alias: str, task_name: str) -> Option[str]:
        if OakFileLoader.ALIAS_REGEXP.fullmatch(alias):
            return Empty()
        else:
            return Some(
                f"Alias \"{alias}\" for task {task_name} doesn't match alias pattern {OakFileLoader.ALIAS_PATTERN}"
            )
