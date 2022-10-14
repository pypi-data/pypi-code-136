"""Console script for baseten."""
import configparser
import functools
import logging
import sys

import click
from truss.cli import cli_group as truss_commands

from baseten import version as b10_version
from baseten.client_commands import baseten_cli, models_cli, pretrained_cli
from baseten.common.settings import (read_config, set_config_value,
                                     set_server_url)
from baseten.common.util import setup_logger

logger = logging.getLogger(__name__)


def ensure_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        config = read_config()
        try:
            config.get('api', 'api_key')
        except configparser.NoOptionError:
            click.echo('You must first run the `baseten login` cli command.')
            sys.exit()
        result = func(*args, **kwargs)
        return result
    return wrapper


@click.group(name="baseten", invoke_without_command=True)
@click.pass_context
@click.option(
    "-v",
    "--version",
    is_flag=True,
    show_default=False,
    default=False,
    help="Show baseten package version.",
)
def cli_group(ctx, version):
    setup_logger('baseten', logging.INFO)
    if not ctx.invoked_subcommand:
        if version:
            click.echo(b10_version())
        else:
            click.echo(ctx.get_help())


@cli_group.command()
@click.option('--server_url', prompt='BaseTen server URL')
def configure(server_url):
    if set_server_url(server_url):
        click.echo('Saved server URL.')
    else:
        click.echo('That is not a valid URL.')


@cli_group.command()
@click.option('--api_key', prompt='BaseTen API key', hide_input=True)
def login(api_key):
    set_config_value('api', 'api_key', api_key)
    click.echo('Saved API key.')


truss_commands.add_command(baseten_cli.deploy_from_directory)
cli_group.add_command(truss_commands)
cli_group.add_command(pretrained_cli.pretrained)
cli_group.add_command(models_cli.models)

if __name__ == '__main__':
    cli_group()
