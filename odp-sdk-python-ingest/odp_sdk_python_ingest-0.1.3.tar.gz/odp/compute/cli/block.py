"""
CLI tool for deploying prefect blocks
"""
import asyncio
from ast import literal_eval
import click
import logging
from typing import cast, Dict, Type

from prefect.blocks.core import Block
from prefect.settings import temporary_settings
from prefect.utilities.importtools import import_object

from .params import TypeParamType
from odp.auth.prefect.prefect_b2c_client import PrefectB2cClient


def split_on_first(string: str, on: str):
    elements = string.split(on)
    return elements[0], on.join(elements[1:])


@click.command()
@click.option(
    "-d",
    "--dry-run",
    is_flag=True,
    help="Build docker image, but don't deploy to prefect server",
)
@click.option("--api-server", type=str, required=False, help="Prefect API url")
@click.option(
    "--verbose", is_flag=True, help="Enable verbose output. Is overloaded by --debug"
)
@click.option("--debug", is_flag=True, help="Enable debug-output. Overloads --verbose")
@click.option("--block", type=TypeParamType(), help="Import path for block type")
@click.option("-n", "--name", help="Block name as a slug")
@click.option(
    "-p",
    "--param",
    multiple=True,
    callback=lambda ctx, param, value: dict(
        map(lambda x: split_on_first(x, "="), value)
    ),
    help="Parameter to be forwarded to flow. Basic types will be evaluated",
)
@click.option(
    "--overwrite",
    is_flag=True,
    help="Overwrite existing blocks with the same name/slug",
)
def block(
    name: str,
    block: Type,
    overwrite: bool,
    param: Dict[str, str],
    api_server: str,
    dry_run: bool,
    verbose: bool,
    debug: bool,
):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    elif verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    if not issubclass(block, Block):
        raise ValueError(
            "The provided block class '{}' is not a subclass of {}.{}".format(
                block.__name__, Block.__module__, Block.__name__
            )
        )

    block_parameters = block.__fields__

    for p, value in param.items():

        if not p in block_parameters:
            raise ValueError(
                f"The parameter '{p}' is not an input argument of '{block.__name__}'"
            )

        try:
            param[p] = literal_eval(value)
        except (ValueError, SyntaxError):
            param[p] = value

    block_obj = cast(Block, block(**param))

    if not dry_run:
        client = PrefectB2cClient(api_server=api_server)

        with temporary_settings(client.get_prefect_config(api_server)):
            uuid: str = block_obj.save(name, overwrite=overwrite)  # type: ignore

            click.echo(f"New block ID: {uuid}")
