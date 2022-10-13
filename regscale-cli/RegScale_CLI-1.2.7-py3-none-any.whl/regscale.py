#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""standard python imports"""
import os
import sys

import click
from rich.console import Console

import app.healthcheck as hc
import app.login as lg

############################################################
# Versioning
############################################################
from app._version import __version__
from app.ad import ad
from app.application import Application
from app.cisa import cisa
from app.jira import jira
from app.logz import create_logger
from app.migrations import migrations
from app.oscal import oscal
from app.servicenow import servicenow
from app.tenable import tenable
from app.wiz import wiz

############################################################
# CLI Command Definitions
############################################################


console = Console()

app = Application()

logger = create_logger()


@click.group()
def cli():
    """
    Welcome to the RegScale CLI client app!
    """


# About function
@cli.command()
def about():
    """Provides information about the CLI and its current version."""
    banner()
    console.print("[red]RegScale[/red] CLI Version: " + __version__)
    console.print("Author: J. Travis Howerton (thowerton@regscale.com)")
    console.print("Copyright: RegScale Incorporated")
    console.print("Website: https://www.regscale.com")
    console.print("Read the CLI Docs: https://regscale.com/documentation/cli-overview")
    java = app.get_java()
    matches = ["not found", "internal or external"]
    if not any(x in java for x in matches):
        console.print(f"Java: {java}")


def banner():
    """Banner"""
    txt = """

\t [#21a5bb]///////////////////////////\t
\t[#21a5bb]/////////////////////////*****\t
\t//////                  /*******\t
\t//////                      //////
\t//////              [#ef5d23]////[/#ef5d23]     //////
\t ////            [#ef5d23]////////[/#ef5d23]    /////
\t               [#ef5d23]////////[/#ef5d23]     //////[/#21a5bb]\t
\t [#f8b737]***[/#f8b737]         [#ef5d23]////////[/#ef5d23]    /(((///\t
\t[#f8b737]******[/#f8b737]      [#ef5d23]/((((/(([/#ef5d23]   ((((((((\t
\t[#f8b737]******[/#f8b737]    [#ef5d23](((((((([/#ef5d23]   ((((((((\t
\t[#f8b737]******[/#f8b737]  [#ef5d23]((((((([/#ef5d23]     (((((((\t
\t[#f8b737]******[/#f8b737] [#ef5d23](((#(([/#ef5d23]        (((([#23539e]####[/#23539e]\t
\t[#f8b737]******[/#f8b737] [#ef5d23]((##[/#ef5d23]            [#23539e]########[/#23539e]\t
\t[#f8b737]******[/#f8b737][#ef5d23]##[/#ef5d23]                [#23539e]######(([/#23539e]\t
\t[#f8b737]****[/#f8b737][#ef5d23]#[/#ef5d23]                   [#23539e]######[/#23539e]
\t[#f8b737]****[/#f8b737]                      [#23539e]#####[/#23539e]
    """
    console.print(txt)


# Log into RegScale to get a token
@cli.command()
@click.option(
    "--username",
    hide_input=False,
    help="RegScale User Name",
    prompt=True,
    required=True,
    default=lambda: os.environ.get("REGSCALE_USER", ""),
)
@click.option("--password", prompt=True, hide_input=True)
def login(username, password):
    """Logs the user into their RegScale instance"""
    if password:
        lg.login(username, password, app=app)
        sys.exit(0)


@cli.command()
def validate_token():
    """Check to see if token is valid"""
    if lg.is_valid(app=app):
        sys.exit(0)
    else:
        logger.warning("RegScale token is invalid, please login.")


# Check the health of the RegScale Application
@cli.command()
def healthcheck():
    """Monitoring tool to check the health of the RegScale instance"""
    hc.status()


# add OSCAL support
cli.add_command(oscal)

# add CISA support
cli.add_command(cisa)

# add data migration support
cli.add_command(migrations)

# add Wiz support
cli.add_command(wiz)

# add Azure Active Directory (AD) support
cli.add_command(ad)

# add ServiceNow support
cli.add_command(servicenow)

# add JIRA support
cli.add_command(jira)

# add Tenable support
cli.add_command(tenable)

# start function for the CLI
if __name__ == "__main__":
    cli()
