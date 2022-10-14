import os
from contextlib import contextmanager
from pathlib import Path
from tkinter import messagebox

from .util import get_full_path, remove_if_exists


class PlaygroundException(Exception):
    pass


class PGConfigNotFoundError(PlaygroundException):
    pass


class PGSettingsNotFoundError(PlaygroundException):
    pass


class PGJSONFormatError(PlaygroundException):
    pass


class PGInvalidConfError(PlaygroundException):
    pass


class PGInvalidSettingError(PlaygroundException):
    pass


class PGDoesNotExistError(PlaygroundException):
    pass


class PGNameNotEnteredError(PlaygroundException):
    pass


class PGTypeNotEnteredError(PlaygroundException):
    pass


@contextmanager
def status_manager(args, status=None):
    """Shows errors and cleans up the environment in case of exceptions."""
    current_dir = Path(".").resolve()
    try:
        yield
    except (Exception, KeyboardInterrupt) as err:
        result = get_result(err)
        set_status(result, status, error=True)
        cleanup(args)
    finally:
        os.chdir(current_dir)


def set_status(text, status=None, error=False):
    if status:
        status.set(text)
        if error:
            messagebox.showerror("Error", text)
    else:
        print(text)


def get_result(err):
    """Returns a result based on an exception."""
    results = {
        PGDoesNotExistError: "The playground '{0}' does not exist.",
        PGConfigNotFoundError: "The configuration could not be found.",
        PGSettingsNotFoundError: "Settings for playground '{0}' was not found.",
        PGInvalidConfError: "'{0}' was not found in the configuration.",
        PGInvalidSettingError: "Settings options missing: {0}",
        PGJSONFormatError: "JSON format error in '{0}': {1}",
        PGNameNotEnteredError: "The playground name has not been entered.",
        PGTypeNotEnteredError: "The playground type has not been set.",
    }
    result = results.get(type(err), str(err))
    return result.format(*err.args)


def cleanup(args):
    """Cleans up the environment in case of an error."""
    if args.command == "new":
        playground_dir = get_full_path(args.name)
        remove_if_exists(playground_dir)
