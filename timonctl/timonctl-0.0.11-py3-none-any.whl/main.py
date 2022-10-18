from getpass import getpass
import sys
from types import SimpleNamespace

from tabulate import tabulate
import typer

from . import logger, settings
from .client import get_client, get_http_client
from .blueprint import app as app_blueprint
from .common import get_token_from_file, remove_token_file
from .deployment import app as app_deployment
from .environment import app as app_environment
from .exceptions import (
    TimonApiException,
    TimonLoginRequiredException,
    TimonTokenExpiredException,
)
from .flow import app as app_flow
from .project import app as app_project
from .schemas import validate_content
from .template import app as app_template


app = typer.Typer()
app.add_typer(app_blueprint, name="blueprint")
app.add_typer(app_deployment, name="deployment")
app.add_typer(app_environment, name="environment")
app.add_typer(app_flow, name="flow")
app.add_typer(app_project, name="project")
app.add_typer(app_template, name="template")


@app.command()
def login(
    ctx: typer.Context,
    force: bool = typer.Option(False, "--force"),
    prompt: bool = typer.Option(False, "--prompt"),
    show: bool = typer.Option(False, "--show"),
):
    token = None

    if not force:
        token = get_token_from_file(ctx.obj.profile.name)

    if not token:
        password = None
        if force:
            ctx.obj.profile.auth.password = getpass()
        else:
            password = ctx.obj.profile.auth.get("password")
        if not password:
            ctx.obj.profile.auth.password = getpass()

        client = get_http_client(ctx.obj.profile)
        logger.debug(f"Requesting token for {ctx.obj.profile.name}")
        token = client.login()
        print("Logged in successfully.")
    else:
        print("Already logged in.")

    if show:
        print(tabulate(token, headers=["Field", "Value"], tablefmt="psql"))


@app.command()
def logout(ctx: typer.Context):
    try:
        remove_token_file(ctx.obj.profile.name)
        print("Logged out successfully.")
    except FileNotFoundError:
        print("Already logged out.")


@app.command()
def validate(schema: str, path: str):
    logger.debug(f"Validating {schema} {path}")
    try:
        with open(path) as fp:
            validate_content(fp.read(), schema)
        print(f"{schema.title()} {path} is valid.")
    except Exception as e:
        print(f"{schema.title()} {path} is not valid:\n{e}")
        sys.exit(1)


@app.callback()
def entrypoint(
    ctx: typer.Context, profile: str = typer.Option("default", envvar="TIMON_PROFILE")
):

    if ctx.invoked_subcommand == "validate":
        return

    try:
        with open("timon.yaml") as fp:
            validate_content(fp.read(), "config")
    except Exception as e:
        print(str(e))
        sys.exit(1)

    ns_profile = settings.profiles.get(profile)
    ns_profile.name = profile

    if ctx.invoked_subcommand not in ["login", "logout", "validate"]:
        try:
            client = get_client(ns_profile)
        except TimonTokenExpiredException:
            print(f"New log in required. Token for {profile} expired")
            remove_token_file(profile)
            sys.exit(1)
        except TimonLoginRequiredException:
            print(f"Log in required. No valid token for {profile} found.")
            sys.exit(1)
        except TimonApiException as e:
            logger.error(str(e))
            sys.exit(1)

        ctx.obj = SimpleNamespace(
            client=client,
            organisation_id=client.organisation_id,
            profile=ns_profile,
            project_id=client.project_id,
        )
    else:
        ctx.obj = SimpleNamespace(profile=ns_profile)


# NOTE: this intermediate step is required to be able to add common
#       arguments with entrypoint()
#
#       https://jacobian.org/til/common-arguments-with-typer/
def main():
    app()


if __name__ == "__main__":
    main()
