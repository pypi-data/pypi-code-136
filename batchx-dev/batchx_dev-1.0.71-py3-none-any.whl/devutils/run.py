import json
import os
import subprocess as sp
import traceback
from pathlib import Path
import sys

from batchx import bx

from .CTE import DEFAULT_MEMORY_MB, DEFAULT_VCPUS
from .debug import debug_print
from .error import (
    handle_called_process_error,
    handle_unknown_exception,
    handle_value_error,
)
from .io import save_json

from functools import partial


def check_for_custom_exception(
    stderr: str,
    custom_exceptions: list | None = None,
):
    if custom_exceptions is None:
        custom_exceptions = []

    for custom_exception in custom_exceptions:
        if custom_exception.is_applicable(stderr):
            debug_print(
                "{id} Stderr".format(id=custom_exception.IDENTIFIER), stderr, long=False
            )
            sys.exit(custom_exception.BX_ERROR_CODE)
        else:
            pass
    return


def run_command(
    command: str,
    identifier: str = "",
    output_fp: Path | str | None = None,
    verbose: bool = True,
    cwd=None,
    shell: bool = True,
    acceptable_exit_codes: tuple[int, ...] = (0,),
    reraise: bool = True,
    custom_exceptions: list | None = None,
):

    debug_print("{} command".format(identifier), command, verbose=verbose, long=False)
    run_subprocess = partial(
        sp.run,
        command,
        cwd=cwd,
        shell=shell,
        stderr=sp.PIPE,
        encoding="utf-8",
    )

    try:
        if output_fp is None:
            completed_subprocess = run_subprocess()
        else:
            with open(output_fp, "w") as f:
                completed_subprocess = run_subprocess(stdout=f)
    except Exception as e:
        handle_unknown_exception(exception=e, identifier=identifier, reraise=reraise)

    # see if the output is good or we need to trigger an error of some kind.
    exit_code = completed_subprocess.returncode
    stderr = completed_subprocess.stderr

    check_for_custom_exception(stderr, custom_exceptions=custom_exceptions)
    check_for_acceptable_exit_code(
        stderr=stderr, exit_code=exit_code, acceptable_exit_codes=acceptable_exit_codes
    )
    return


def run_bx_job(
    tool,
    inputs,
    output_fp=None,
    environment=None,
    vcpus=DEFAULT_VCPUS,
    memory_mb=DEFAULT_MEMORY_MB,
    timeout_s=15 * 60,
    verbose=True,
    reraise: bool = True,
    acceptable_exit_codes: tuple[int, ...] = (0, 7),
):
    # Initialize
    identifier = "{t} bx job submit".format(t=tool)

    if environment is None:
        environment = os.environ["BATCHX_ENV"]

    # Start service & create request
    bx.connect()
    job_service = bx.JobService()

    request = job_service.SubmitRequest(
        environment=environment,
        image=tool,
        vcpus=vcpus,
        memory=memory_mb,
        timeout=timeout_s,
        input_json=json.dumps(inputs),
    )
    debug_print("{} Request".format(identifier), request, verbose=verbose)

    # Submit job and get result
    try:
        response = job_service.Run(request)
        debug_print("{} Response".format(identifier), response, verbose=verbose)

        # check potential error message
        error_message = getattr(response, "error_message", None)
        if error_message not in {None, ""}:
            debug_print(
                "{} Error message".format(identifier),
                error_message,
                verbose=verbose,
                long=False,
            )

        # check exit code
        exit_code = getattr(response, "exit_code", None)
        debug_print(
            "{} Exit code".format(identifier),
            exit_code,
            verbose=verbose,
            long=False,
        )
        exit_code = check_for_acceptable_exit_code(
            exit_code=exit_code, acceptable_exit_codes=acceptable_exit_codes
        )

        # if the above went well, write the result to file
        output_json = json.loads(getattr(response, "output_json", "{}"))
        if output_fp is not None:
            save_json(output_json, output_fp)
            return exit_code
        else:
            return output_json

    except ValueError as e:
        handle_value_error(
            exception=e, exit_code=exit_code, identifier=identifier, reraise=reraise
        )
    except Exception as e:
        handle_unknown_exception(exception=e, identifier=tool, reraise=reraise)


def check_for_acceptable_exit_code(
    stderr: str | None = None,
    exit_code: int | None = None,
    acceptable_exit_codes: tuple[int, ...] = (0,),
):
    if exit_code not in acceptable_exit_codes:
        error_message = """
        Exit code {c} not in acceptable exit codes {ac}.
        StdErr:
            {stderr}
        """.format(
            stderr=stderr,
            c=exit_code,
            ac=acceptable_exit_codes,
        )
        raise ValueError(error_message) from None
    else:
        return exit_code
