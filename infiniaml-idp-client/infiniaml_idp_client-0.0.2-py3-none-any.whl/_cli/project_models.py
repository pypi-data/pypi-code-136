import json
from pathlib import Path
from typing import Any, Dict

import httpx
import typer

from infiniaml_idp_client import AccessKeyCredentials, IdpClient
from infiniaml_idp_client._cli.typed_dict_code_gen import generate
from infiniaml_idp_client._common.constants import IDP_URL

from .utils import get_docs

project_models_app = typer.Typer()


def _create_project_models(docs: Dict[str, Any], output: Path):
    result = generate(json.dumps(docs)).clean()
    with output.open("w") as module:
        module.write(result)


def _output_callback(path: Path):
    if path.suffix != ".py":
        raise typer.BadParameter("Output must be a valid python file")
    return path


@project_models_app.command("create")
def create_project_models(
    idp_url: str = typer.Option(
        IDP_URL,
        "--idp-url",
        "-u",
        help="The base url of the Intelligent Document Processing web application",
        envvar="IDP_URL",
    ),
    project_id: int = typer.Option(
        ...,
        "--project-id",
        "-p",
        envvar="PROJECT_ID",
    ),
    access_key_id: str = typer.Option(
        ...,
        help="ID of access key belonging to an IDP account",
        envvar="ACCESS_KEY_ID",
    ),
    access_key_secret: str = typer.Option(
        ...,
        help="Secret for access key belonging to an IDP account",
        envvar="ACCESS_KEY_SECRET",
    ),
    output: Path = typer.Option(
        ...,
        "--output",
        "-o",
        help="The filepath of the outputted python models",
        prompt="Enter output filepath",
        writable=True,
        callback=_output_callback,
    ),
):
    """
    ✨ Create models for specified project ✨

    The generated models (specifically JobInput and JobResult) should be used
    alongside the JobClient. It's handy and enables features such as autocomplete
    in your IDE.
    """
    try:
        creds = AccessKeyCredentials(access_key_id, access_key_secret, idp_url=idp_url)
        idp_client = IdpClient(creds, idp_url)
        docs = get_docs(idp_client, project_id)
        _create_project_models(docs, output)
    except httpx.HTTPStatusError as err:
        status_code = err.response.status_code
        typer.secho(f"Could not create models for project {project_id}, {status_code=} ", fg=typer.colors.RED)
        raise typer.Abort()

    typer.secho(f"🚀 Created project models at {output} 🚀", fg=typer.colors.GREEN)
