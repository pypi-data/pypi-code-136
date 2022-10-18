import bdb
import sys
import traceback
import types
from typing import TextIO

import rich
from docutils.utils import SystemMessage
from sphinx.application import Sphinx
from sphinx.errors import SphinxError
from sphinx.locale import __
from sphinx.util import format_exception_cut_frames, save_traceback
from sphinx.util.console import terminal_safe  # type: ignore


def exec_sphinx(app: Sphinx, args: types.SimpleNamespace):
    try:
        app.build(force_all=True)
    except (Exception, KeyboardInterrupt) as exc:
        handle_exception(app, args, exception=exc)
        return 2


def handle_exception(
    app: Sphinx,
    args: types.SimpleNamespace,
    exception: BaseException,
    stderr: TextIO = sys.stderr,
) -> None:  # NOQA
    if isinstance(exception, bdb.BdbQuit):
        return

    err = rich.console.Console(stderr=True)

    if args.pdb:
        err.print(__("[red]Exception occurred while building, starting debugger:[/]"))
        traceback.print_exc()
        pdb.post_mortem(sys.exc_info()[2])  # type: ignore
    else:
        print(file=stderr)
        if args.verbosity or args.traceback:
            traceback.print_exc(None, stderr)
            err.print()
        if isinstance(exception, KeyboardInterrupt):
            print(__("Interrupted!"))
        elif isinstance(exception, SystemMessage):
            err.print(__("[red]reST markup error:"))
            err.print(terminal_safe(exception.args[0]))
        elif isinstance(exception, SphinxError):
            err.print(f"[red]{exception.category}:[/]")
            err.print(str(exception))
        elif isinstance(exception, UnicodeError):
            err.print(__("[red]Encoding error:[/]"))
            print(terminal_safe(str(exception)))
            tbpath = save_traceback(app)
            err.print(
                __(
                    f"[red]The full traceback has been saved in {tbpath}, if you want to report the issue to the developers.[/]"
                )
            )
        elif isinstance(exception, RuntimeError) and "recursion depth" in str(
            exception
        ):
            err.print(__("[red]Recursion error:[/]"))
            err.print(terminal_safe(str(exception)))
            err.print()
            err.print(
                __(
                    "This can happen with very large or deeply nested source "
                    "files. You can carefully increase the default Python "
                    "recursion limit of 1000 in conf.py with e.g.:"
                )
            )
            err.print("    import sys; sys.setrecursionlimit(1500)")
        else:
            rich.print(__("[red]Exception occurred:[/]"))
            err.print(format_exception_cut_frames().rstrip())
            tbpath = save_traceback(app)
            err.print(
                __(
                    "[red]The full traceback has been saved in %s, if you "
                    "want to report the issue to the developers.[/]"
                )
                % tbpath
            )
            err.print(
                __(
                    "Please also report this if it was a user error, so "
                    "that a better error message can be provided next time."
                )
            )
            err.print(
                __(
                    "A bug report can be filed in the tracker at "
                    "<https://github.com/sphinx-doc/sphinx/issues>. Thanks!"
                )
            )
