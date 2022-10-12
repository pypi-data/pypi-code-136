"""Linters"""
# pylint: disable=subprocess-run-check

import logging
import subprocess

logger = logging.getLogger(__name__)


class Linter:
    """Linter parent class"""

    def __init__(self, executable: str) -> None:
        self.executable = executable
        self.options: list[str] = []
        self.cmd_result: subprocess.CompletedProcess
        self.stdout: list[str]
        self.stderr: list[str]
        self.use_config_file: bool = False

    def lint(self, filename: str) -> int:
        """General linting method

        Parameters
        ----------
        filename : str
            File path to be linted

        Returns
        -------
        int
            Return code of the linter program
        """
        logger.info("Linting with [%s] on file %s", self.executable, filename)
        cmd = [self.executable] + self.options + [filename]
        logger.debug("Linting command: %s", " ".join(cmd))
        self.cmd_result = subprocess.run(cmd, capture_output=True)
        self.stdout = self.cmd_result.stdout.decode().strip().split("\n")
        self.stderr = self.cmd_result.stderr.decode().strip().split("\n")

        self.process_output()
        return self.cmd_result.returncode

    def process_output(self) -> None:
        """Process output, since some linters print errors to stdout"""
        logger.debug("Linter stdout:")
        for out in self.stdout:
            logger.debug("\t%s", out)

        if self.cmd_result.returncode != 0:
            logger.error("Found errors:")
            for err in self.stderr:
                logger.error("\t%s", err)
        else:
            logger.info("Check passed.")


# Linters for c/c++
class ClangFormat(Linter):
    """`clang-format` linter"""

    def __init__(self, executable: str) -> None:
        super().__init__(executable)
        self.options = ["--dry-run", "--Werror"]


class Cpplint(Linter):
    """`cpplint` linter"""


# Linters for Python
class Pylint(Linter):
    """`pylint` linter"""

    def __init__(self, executable: str) -> None:
        super().__init__(executable)
        self.options = ["--output-format=parseable"]

    def process_output(self) -> None:
        if self.cmd_result.returncode != 0:
            logger.error("Found errors:")
            for err in self.stdout:
                logger.error("\t%s", err)
        else:
            logger.info("Check passed.")


class Flake8(Linter):
    """`flake8` linter"""

    def process_output(self) -> None:
        if self.cmd_result.returncode != 0:
            logger.error("Found errors:")
            for err in self.stdout:
                logger.error("\t%s", err)
        else:
            logger.info("Check passed.")


class Black(Linter):
    """`black` linter"""

    def __init__(self, executable: str) -> None:
        super().__init__(executable)
        self.options = ["--check", "--diff"]

    def process_output(self) -> None:
        if self.cmd_result.returncode != 0:
            logger.error("Found errors:")
            for err in self.stdout:
                logger.error("\t%s", err)
        else:
            logger.info("Check passed.")


class Isort(Linter):
    """`isort` linter"""

    def __init__(self, executable: str) -> None:
        super().__init__(executable)
        self.options = ["--check-only", "--diff"]

    def process_output(self) -> None:
        if self.cmd_result.returncode != 0:
            logger.error("Found errors:")
            for err in self.stdout:
                logger.error("\t%s", err)
        else:
            logger.info("Check passed.")


class Mypy(Linter):
    """`mypy` linter"""

    def __init__(self, executable: str) -> None:
        super().__init__(executable)
        self.options = ["--pretty", "--show-error-context", "--show-error-codes"]

    def process_output(self) -> None:
        if self.cmd_result.returncode != 0:
            logger.error("Found errors:")
            for err in self.stdout:
                logger.error("\t%s", err)
        else:
            logger.info("Check passed.")
