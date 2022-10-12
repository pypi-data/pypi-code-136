from __future__ import annotations

import os
import platform
from functools import cached_property
from io import TextIOBase
from pathlib import Path
from subprocess import PIPE, STDOUT, Popen  # nosec
from threading import Thread
from typing import IO, List, Optional, Union

from atoti_core import get_active_plugins, local_to_absolute_path

from ._check_java_version import check_java_version
from ._get_java_executable_path import get_java_executable_path
from ._path_utils import get_atoti_home
from ._wait_for_matching_output import wait_for_matching_output
from .config._session_config import SessionConfig, get_logging_destination_io

JAR_PATH = Path(__file__).parent / "data" / "atoti.jar"

DEFAULT_HADOOP_PATH = Path(__file__).parent / "bin" / "hadoop-3.2.1"

# Keep in sync with Java's ApplicationStarter.ENABLE_AUTH_OPTION.
_ENABLE_AUTH_OPTION = "--enable-auth"

# Keep in sync with Java's ServerUtils.serverStarted().
_PY4J_SERVER_STARTED_PATTERN = (
    r"Py4J server started on port (?P<port>\d+)(?: with auth token (?P<token>.+))?$"
)


def _get_logs_directory(session_directory: Path) -> Path:
    return session_directory / "logs"


def _create_session_directory(*, session_id: str) -> Path:
    session_directory = get_atoti_home() / session_id
    _get_logs_directory(session_directory).mkdir(parents=True)
    return session_directory


def _copy_stream(
    input_stream: IO[str], output_stream: Optional[Union[IO[str], TextIOBase]] = None
) -> None:
    try:
        for line in input_stream:
            if output_stream:
                output_stream.write(line)
            else:
                # When no output stream is passed, the input stream is still iterated upon to avoid blocking it but nothing is done with its lines.
                ...
    except ValueError:
        # The input stream has been closed, nothing left to do.
        ...


class ServerSubprocess:
    def __init__(self, *, config: SessionConfig, session_id: str):
        self._config = config

        self._session_directory = _create_session_directory(session_id=session_id)

        self._process = Popen(  # pylint: disable=consider-using-with
            self.command,
            stderr=STDOUT,
            stdout=PIPE,
            text=True,
        )

        match, startup_output = wait_for_matching_output(
            _PY4J_SERVER_STARTED_PATTERN,
            process=self._process,
        )

        self.py4j_java_port = int(match.group("port"))
        self.auth_token: Optional[str] = match.group("token")

        logging_destination_io = get_logging_destination_io(self._config)

        if logging_destination_io:
            logging_destination_io.write(startup_output)
        else:
            startup_log_path = (
                _get_logs_directory(self._session_directory) / "startup.log"
            )
            startup_log_path.write_text(startup_output, encoding="utf8")

        self._output_copier = Thread(
            target=_copy_stream,
            args=(self._process.stdout, logging_destination_io),
            daemon=True,
        )
        self._output_copier.start()

    @cached_property
    def command(self) -> List[str]:
        java_executable_path = get_java_executable_path()

        java_version = check_java_version(
            (17,), java_executable_path=java_executable_path
        )
        add_opens_options = (
            [
                # Arrow reflexive access : https://github.com/activeviam/activepivot/pull/4297/files#diff-d9ef6fa90dda49aa1ec2907eba7be19c916c5f553c9846b365d30a307740aea2
                "--add-opens=java.base/java.nio=ALL-UNNAMED",
                # Py4J reflexive access : java.lang.reflect.InaccessibleObjectException: Unable to make public java.lang.Object[] java.util.HashMap$KeySet.toArray() accessible: module java.base does not "opens java.util" to unnamed module @647fd8ce
                "--add-opens=java.base/java.util=ALL-UNNAMED",
                "--add-opens=java.base/java.lang=ALL-UNNAMED",
            ]
            if java_version[0] == 17
            else []
        )

        command: List[str] = [str(get_java_executable_path())]

        command += add_opens_options
        command += [
            "-jar",
            f"-Dserver.port={self._config.port}",
            f"-Dserver.session_directory={self._session_directory}",
        ]

        if not get_logging_destination_io(self._config):
            command.append("-Dserver.logging.disable_console_logging=true")

        # The user is allowed to pass any options to Java, even dangerous ones.
        command.extend(self._config.java_options)

        if platform.system() == "Windows":
            command.append(
                f"-Dhadoop.home.dir={local_to_absolute_path(DEFAULT_HADOOP_PATH)}"
            )
            hadoop_path = local_to_absolute_path(DEFAULT_HADOOP_PATH / "bin")
            if hadoop_path not in os.environ["PATH"]:
                os.environ["PATH"] = f"{os.environ['PATH']};{hadoop_path}"

        jar_paths = [
            *(self._config.extra_jars),
            *[
                local_to_absolute_path(plugin.jar_path)
                for plugin in get_active_plugins().values()
                if plugin.jar_path
            ],
        ]
        if len(jar_paths) > 0:
            command.append(
                f"-Dloader.path={','.join([local_to_absolute_path(path) for path in jar_paths])}"
            )

        command.append(local_to_absolute_path(JAR_PATH))

        # The created subprocesses always have authentication enabled.
        # This way it's easy to detect an existing detached process: if an unauthenticated connection can be made on Py4J's default port it means it's a detached process.
        command.append(_ENABLE_AUTH_OPTION)

        return command

    @cached_property
    def logs_path(self) -> Path:
        if get_logging_destination_io(self._config):
            raise RuntimeError(
                "Logs have been configured to be written to a specified IO."
            )

        if self._config.logging and self._config.logging.destination:
            if not isinstance(self._config.logging.destination, (str, Path)):
                raise TypeError("Unexpected type of logging destination.")

            return Path(self._config.logging.destination)

        return _get_logs_directory(self._session_directory) / "server.log"

    @cached_property
    def pid(self) -> int:
        return self._process.pid

    def wait(self) -> None:
        """Wait for the process to terminate.

        This will prevent the Python process from exiting.
        If the Py4J gateway is closed the atoti server will stop itself anyway.
        """
        self._process.wait()
        self._output_copier.join()
