"""Command line interface."""

import os
import sys

import typer
from pydantic.error_wrappers import ValidationError

from wefaas.export import ExportFormat

cli = typer.Typer()


@cli.command()
def serve(
    wefaas: str,
    port: int = typer.Option(8080, "--port", "-p"),
    host: str = typer.Option("0.0.0.0", "--host", "-h"),
) -> None:
    """Start a HTTP API server for the wefaas.

    This will launch a FastAPI server based on the OpenAPI standard and with an automatic interactive documentation.
    """
    # Add the current working directory to the sys path
    # This is required to resolve the wefaas path
    sys.path.append(os.getcwd())

    from wefaas.api.fastapi_app import launch_api  # type: ignore

    launch_api(wefaas, port, host)


@cli.command()
def call(wefaas: str, input_data: str) -> None:
    """Execute the wefaas from command line."""
    
    # Add the current working directory to the sys path
    # This is required to resolve the wefaas path
    sys.path.append(os.getcwd())
    try:
        from wefaas import Wefaas

        output = wefaas(wefaas)(input_data)
        if output:
            typer.echo(output.json(indent=4))
        else:
            typer.echo("Nothing returned!")
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)

@cli.command()
def deploy(wefaas: str) -> None:
    """Deploy an wefaas to a cloud platform.

    This provides additional features such as SSL, authentication, API tokens, unlimited scalability, load balancing, and monitoring.
    """
    typer.secho(
        "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
        fg=typer.colors.BRIGHT_YELLOW,
    )


@cli.command()
def export(
    wefaas: str, export_name: str, format: ExportFormat = ExportFormat.ZIP
) -> None:
    """Package and export an wefaas."""
    if format == ExportFormat.ZIP:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.DOCKER:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.WE:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )


if __name__ == "__main__":
    cli()