import logging

from pathlib import Path
from typing import List, Tuple, Optional
from argparse import ArgumentParser, REMAINDER

from oak_build.app_logging import DEFAULT_LEVEL, LEVELS, init_logging
from oak_build.oak_file import DEFAULT_OAK_FILE, OakFileLoader, OakFile
from oak_build.task_runner import TaskRunner


class App:
    def __init__(self, args: List[str]):
        parser = App._init_arg_parser()
        parsed_args = parser.parse_args(args)

        init_logging(parsed_args.log_level)

        self.oak_file: Path = parsed_args.file
        self.tasks: List[str] = parsed_args.tasks

    def run(self) -> int:
        code, oak_file = self._load_oak_file()
        if code:
            return code
        errors = TaskRunner().run_tasks(oak_file, self.tasks)
        if errors:
            for error in errors:
                logging.error(error)
            return 1
        return 0

    def _load_oak_file(self) -> Tuple[int, Optional[OakFile]]:
        file_description = OakFileLoader.load_file(self.oak_file)
        if file_description.is_ok:
            return 0, file_description.unwrap()
        else:
            errors = file_description.unwrap_err()
            logging.error(f"Found {len(errors)} errors:")
            for error in errors:
                logging.error(error)
            return 1, None

    @staticmethod
    def _init_arg_parser() -> ArgumentParser:
        parser = ArgumentParser(prog="oak")
        parser.add_argument("-l", "--log-level", default=DEFAULT_LEVEL, choices=LEVELS)
        parser.add_argument("-f", "--file", default=DEFAULT_OAK_FILE, type=Path)
        parser.add_argument("tasks", nargs=REMAINDER)
        return parser



