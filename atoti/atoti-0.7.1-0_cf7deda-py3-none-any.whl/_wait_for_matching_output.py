from __future__ import annotations

import re
import shlex
from datetime import datetime, timedelta
from io import StringIO
from subprocess import Popen  # nosec
from typing import Tuple


def wait_for_matching_output(
    pattern: str,
    *,
    process: Popen[str],
    timeout: timedelta = timedelta(seconds=100),
) -> Tuple[re.Match[str], str]:
    if not process.stdout:
        raise RuntimeError("Expected process to have an stdout.")

    with StringIO() as output:

        def get_error_message(*, reason: str) -> str:
            command = shlex.join(process.args)  # type: ignore
            return "\n".join(
                [
                    reason,
                    "COMMAND:",
                    command,
                    "PATTERN:",
                    pattern,
                    "OUTPUT:",
                    "".join(output.getvalue()),
                ]
            )

        start = datetime.now()

        while process.poll() is None:
            if (datetime.now() - start) > timeout:
                raise RuntimeError(
                    get_error_message(
                        reason=f"{timeout.total_seconds()} seconds elapsed but the process output did not match the expected pattern."
                    )
                )

            line = process.stdout.readline()
            output.write(line)

            match = re.search(pattern, line)
            if match:
                return match, output.getvalue()

        raise RuntimeError(
            get_error_message(
                reason="Process exited before its output matched the expected pattern."
            )
        )
