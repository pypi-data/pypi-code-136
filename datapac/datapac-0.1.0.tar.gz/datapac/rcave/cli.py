import os

import click

from datapac.package import package
from datapac.rcave.services.pull import pull as pull_service
from datapac.rcave.services.push import push as push_service
from datapac.rcave.sources.postgres.source import load_artefacts as pg_load_artefacts
from datapac.rcave.sources.s3.source import load_artefacts as s3_load_artefacts
from datapac.rcave.utils.graph import Config
from datapac.rcave.utils.graph import Graph
from datapac.rcave.utils.graph import load
from datapac.utils.environment import Environment
from datapac.utils.environment import detect


def validate_config(ctx, param, value) -> Graph:
    return load(value)


def validate_env(ctx, param, value) -> Environment:
    return detect(value)


def validate_vars(ctx, param, value) -> dict:
    return {k: v for k, v in value}


def validate_path(ctx, param, value) -> str:
    return os.path.join(os.getcwd(), value)


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "config",
    "--config",
    "-c",
    required=True,
    help="Path to config file",
    callback=validate_config,
)
@click.option(
    "env",
    "--env",
    "-e",
    required=True,
    help="Name of env to pull from",
    callback=validate_env,
)
@click.option(
    "--vars",
    "-v",
    "variables",
    type=(str, str),
    multiple=True,
    callback=validate_vars,
)
@click.argument(
    "path",
    type=str,
    callback=validate_path,
)
def pull(config: Config, env: Environment, variables: dict, path: str):
    with package.create(path) as pkg:
        pull_service(env, config.graph, variables, pkg)


@cli.command()
@click.option(
    "env",
    "--env",
    "-e",
    required=True,
    help="Name of env to pull from",
    callback=validate_env,
)
@click.option(
    "--vars",
    "-v",
    "variables",
    type=(str, str),
    multiple=True,
    callback=validate_vars,
)
@click.argument(
    "path",
    type=str,
    callback=validate_path,
)
def push(env: Environment, variables: dict, path: str):
    with package.open(path, [pg_load_artefacts, s3_load_artefacts]) as pkg:
        push_service(env, pkg, variables)


if __name__ == "__main__":
    cli()
