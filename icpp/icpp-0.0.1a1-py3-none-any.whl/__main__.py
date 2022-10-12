"""__main__.py
The double underscores indicate that this file has a special meaning in Python.
When running a package (!) as a script with -m, 'python -m icpp', Python
executes the contents of the __main__.py file.

In other words, __main__.py acts as the entry point of our program and takes care of
the main flow, calling other parts as needed

reference: https://realpython.com/pypi-publish-python-package/
"""
from typing import Optional
from enum import Enum
import typer
import icpp

# Instantiate the Typer app globally with app = typer.Typer().
# That way, we can decorate any function we want to call from the command line,
# using the @app.command() decorator.
app = typer.Typer()


class Verbose(str, Enum):
    """Verbosity options."""

    SILENT = "silent"
    VERBOSE = "verbose"


state = {"verbose": Verbose.VERBOSE}


def version_callback(value: bool) -> None:
    """Prints package version.

    When the user issues the command `icpp --version`, this callback is called.

    Arguments:
        value: when True, the package version is printed.

    Returns:

    Raises:
        typer.Exit(): program is terminated before anything else is executed
    """
    if value:
        typer.echo(f"icpp version: {icpp.__version__}")
        raise typer.Exit()


@app.callback()
# pylint: disable=unused-argument
def main_callback(
    # https://typer.tiangolo.com/tutorial/options/version/
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        help="Prints version of package",
        callback=version_callback,
        is_eager=True,
    ),
    verbose: Verbose = typer.Option(
        Verbose.VERBOSE,
        "--verbose",
        case_sensitive=False,
    ),
) -> None:
    """An API for C++ applications on the Internet Computer."""
    state["verbose"] = Verbose.VERBOSE


@app.command()
def health() -> None:
    """Health check.

    Provides a simple health check that prints: `icpp status: ok`

    Arguments:

    Returns:

    Raises:
    """
    typer.echo("icpp status: ok")


def main() -> None:
    """Entry point of program"""
    app(prog_name="icpp")


if __name__ == "__main__":
    main()
