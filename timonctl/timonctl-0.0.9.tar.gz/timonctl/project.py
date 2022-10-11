from tabulate import tabulate
import typer

from . import logger
from .exceptions import TimonApiException
from .models import *

app = typer.Typer()


@app.command("list")
def list_project(ctx: typer.Context):
    try:
        projects = ctx.obj.client.get_projects(ctx.obj.organisation_id)
        print(tabulate([x.dict().values() for x in projects], headers=Project.get_field_names(), tablefmt="psql"))
    except TimonApiException as e:
        logger.error(str(e))


@app.command("show")
def show_project(ctx: typer.Context, name: str):
    try:
        project = ctx.obj.client.get_project(name, ctx.obj.organisation_id)
        print(tabulate(project, headers=["Field", "Value"], tablefmt="psql"))
    except TimonApiException as e:
        logger.error(str(e))


@app.command("create")
def create_project(ctx: typer.Context, name: str):
    try:
        project = ctx.obj.client.create_project(name, ctx.obj.organisation_id)
        print(tabulate(project, headers=["Field", "Value"], tablefmt="psql"))
    except TimonApiException as e:
        logger.error(str(e))


@app.command("delete")
def delete_project(ctx: typer.Context, name: str):
    try:
        result = ctx.obj.client.delete_project(name, ctx.obj.organisation_id)
        print(result)
    except TimonApiException as e:
        logger.error(str(e))
