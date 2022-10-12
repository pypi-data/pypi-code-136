#!/usr/bin/env python

import sys

import click

from cli.commands import appinfo
from cli.commands import auth
from cli.commands import download
from cli.commands import purchase
from cli.commands import search
from cli.commands import version
from cli.logger import logger
from networking.http_client import HTTPClient


@click.group()
@click.option('--debug/--no-debug')
@click.option('-p', '--proxy', help="http proxy")
def cli(debug, proxy):
    """A cli tool for interacting with Apple's ipa files."""

    if debug:
        level = "DEBUG"
    else:
        level = "INFO"
    logger.remove()
    format = "<level>{level: <7}</level> | <level>{message}</level>"
    logger.add(sys.stderr, format=format, level=level)

    if proxy:
        HTTPClient.proxy = proxy


def main():
    cli.add_command(version.version)
    cli.add_command(auth.auth)
    cli.add_command(search.search)
    cli.add_command(purchase.purchase)
    cli.add_command(appinfo.appinfo)
    cli.add_command(download.download)
    cli()


if __name__ == '__main__':
    main()
