from tabulate import tabulate
import typer

from . import logger
from .common import is_valid_uuid
from .exceptions import TimonApiException
from .models import *

app = typer.Typer()


@app.command("list")
def list_deployment(ctx: typer.Context):
    try:
        deployments = ctx.obj.client.get_deployments(ctx.obj.project_id)
        print(tabulate([x.dict().values() for x in deployments], headers=Deployment.get_field_names(), tablefmt="psql"))
    except TimonApiException as e:
        logger.error(str(e))


@app.command("create")
def create_deployment(ctx: typer.Context, name: str, template: str):
    try:
        deployment = ctx.obj.client.create_deployment(name, template, ctx.obj.project_id)
        print(tabulate(deployment, headers=["Field", "Value"], tablefmt="psql"))
    except TimonApiException as e:
        logger.error(str(e))


@app.command("destroy")
def destroy_deployment(ctx: typer.Context, name: str):
    try:
        result = ctx.obj.client.destroy_deployment(name, ctx.obj.project_id)
        print(result)
    except TimonApiException as e:
        logger.error(str(e))


@app.command("reconcile")
def reconcile_deployment(ctx: typer.Context, name: str):
    try:
        result = ctx.obj.client.reconcile_deployment(name, ctx.obj.project_id)
        print(result)
    except TimonApiException as e:
        logger.error(str(e))


@app.command("show")
def show_deployment(ctx: typer.Context, name: str):
    try:
        deployment = ctx.obj.client.get_deployment(name, ctx.obj.project_id)
        print(tabulate(deployment, headers=["Field", "Value"], tablefmt="psql"))
    except TimonApiException as e:
        logger.error(str(e))


@app.command("edit")
def edit_deployment(name: str):
    logger.info("STUB: edit_deployment")


@app.command("update")
def update_deployment(name: str):
    logger.info("STUB: update_deployment")


@app.command("delete")
def delete_deployment(ctx: typer.Context, name: str):
    try:
        result = ctx.obj.client.delete_deployment(name, ctx.obj.project_id)
        print(result)
    except TimonApiException as e:
        logger.error(str(e))


@app.command("outputs")
def get_deployment_outputs(ctx: typer.Context, name: str, output: str = typer.Argument(default=None)):
    try:
        outputs = ctx.obj.client.get_deployment_outputs(name, output, ctx.obj.project_id)
        if output:
            print(outputs[output])
        else:
            print(outputs)
    except TimonApiException as e:
        logger.error(str(e))


@app.command("logs")
def get_deployment_logs(ctx: typer.Context, name: str, log_filter: str = typer.Argument(default="1 hour ago"), show: bool = typer.Option(default=False)):
    try:
        if is_valid_uuid(log_filter):
            log = ctx.obj.client.get_deployment_log(name, log_filter, ctx.obj.project_id)
            print(log.value)
        else:
            logs = ctx.obj.client.get_deployment_logs(name, ctx.obj.project_id, log_filter)
            if show:
                for log in logs:
                    log_with_value = ctx.obj.client.get_deployment_log(name, log.id, ctx.obj.project_id)
                    print()
                    print(log_with_value.value)
            else:
                print(tabulate([x.dict().values() for x in logs], headers=Log.get_field_names(), tablefmt="psql"))
    except TimonApiException as e:
        logger.error(str(e))
