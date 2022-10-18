from tabulate import tabulate
import typer

from . import logger
from .exceptions import TimonApiException, TimonException
from .models import *


app = typer.Typer()


@app.command("import")
def import_flow(ctx: typer.Context, path: str, name: str):
    try:
        flow = ctx.obj.client.import_flow(path, name, ctx.obj.project_id)
        print(tabulate(flow, headers=["Field", "Value"], tablefmt="psql"))
    except TimonApiException as e:
        logger.error(str(e))
    except TimonException as e:
        print(str(e))


@app.command("list")
def list_flows(ctx: typer.Context):
    try:
        flows = ctx.obj.client.get_flows(ctx.obj.project_id)
        print(
            tabulate(
                [x.dict().values() for x in flows],
                headers=Flow.get_field_names(),
                tablefmt="psql",
            )
        )
    except TimonApiException as e:
        logger.error(str(e))


@app.command("show")
def show_flow(ctx: typer.Context, name: str):
    try:
        flow = ctx.obj.client.get_flow(name, ctx.obj.project_id)
        print(tabulate(flow, headers=["Field", "Value"], tablefmt="psql"))
    except TimonApiException as e:
        logger.error(str(e))


@app.command("edit")
def edit_flow(ctx: typer.Context, name: str):
    logger.info("STUB: edit_flow")


@app.command("update")
def update_flow(ctx: typer.Context, name: str):
    logger.info("STUB: update_flow")


@app.command("delete")
def delete_flow(ctx: typer.Context, name: str):
    try:
        result = ctx.obj.client.delete_flow(name, ctx.obj.project_id)
        print(result)
    except TimonApiException as e:
        logger.error(str(e))
