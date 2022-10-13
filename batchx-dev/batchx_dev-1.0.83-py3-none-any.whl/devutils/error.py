import subprocess as sp
import traceback

from .debug import debug_print


# handle errors
def handle_unknown_exception(
    exception: Exception,
    identifier: str = "",
    reraise: bool = True,
):
    msg = """
    Caught Unexpected Exception in {id} command.
    Exception:
        {exception}
    Stacktrace:
        {stacktrace}
    """.format(
        id=identifier, exception=exception, stacktrace=traceback.format_exc()
    )
    debug_print(msg, verbose=True)
    if reraise:
        raise Exception(exception)
    else:
        return


def handle_value_error(
    exception: ValueError,
    exit_code: None | int = 0,
    identifier: str = "",
    reraise: bool = True,
):
    msg = """
    Caught ValueError in {id} command.
    Error:
        {error}
    Traceback:
        {stacktrace}
    """.format(
        id=identifier, error=exception, stacktrace=traceback.format_exc()
    )
    if reraise:
        raise ValueError(msg) from None
    else:
        return exit_code


def handle_called_process_error(
    exception: sp.CalledProcessError,
    identifier: str = "",
    reraise: bool = True,
):
    msg = """
    Caught CalledProcessError in {id} command.
    Error:
        {error}
    Traceback:
        {stacktrace}
    """.format(
        id=identifier, error=exception, stacktrace=traceback.format_exc()
    )
    debug_print(msg, verbose=True)
    if reraise:
        raise sp.CalledProcessError(exception)
    else:
        return
