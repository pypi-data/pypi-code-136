from dataclasses import dataclass
from pathlib import Path
from typing import Optional, TextIO, Union

from atoti_core import keyword_only_dataclass

from ._config import Config, convert_path_to_absolute_string


@keyword_only_dataclass
@dataclass(frozen=True)
class LoggingConfig(Config):
    """The configuration describing how the session logs will be handled.

    Example:

        >>> logging_config = tt.LoggingConfig(destination="./atoti/server.log")

    """

    destination: Optional[Union[Path, str, TextIO]] = None
    """The place where the session logs will be written to.

    If ``None``, the logs will be written to ``logs/server.log`` in the session directory under ``$ATOTI_HOME`` (this environment variable itself defaults to ``$HOME/.atoti``).

    Note:
        Unless an instance of :class:`io.TextIOBase` is passed, the rolling policy is:

            * Maximum file size of 10MB.
            * Maximum history of 7 days.

        Once the maximum size is reached, logs are archived following the pattern ``f"{destination}.{date}.{i}.gz"`` where ``date`` is the creation date of the file in the ``yyyy-MM-dd`` format and ``i`` an integer incremented during the day.

    Example:

        To stream the session logs to the Python process' standard output:

        >>> import sys
        >>> logging_config = tt.LoggingConfig(destination=sys.stdout)
    """

    def __post_init__(self) -> None:
        if isinstance(self.destination, (Path, str)):
            convert_path_to_absolute_string(self, "destination")
