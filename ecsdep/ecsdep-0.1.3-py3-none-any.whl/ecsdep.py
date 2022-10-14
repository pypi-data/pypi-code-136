#! /usr/bin/env python3

import click
import os
from .terraform import Terraform

# commands --------------------------------------------------
@click.group()
@click.option ('-f', '--file', default = None)
@click.option ('-s', '--silent', is_flag = True)
@click.pass_context
def cli (context, file, silent):
    if file is None:
        file = os.path.join (os.getcwd (), "docker-compose.yml")
        if not os.path.isfile (os.path.abspath (file)):
            file = os.path.join (os.getcwd (), "compose.ecs.yml")
    file = os.path.abspath (file)
    assert os.path.isfile (file), f"{file} not found"
    with open (file) as f:
        context.obj ["cli"] = Terraform (f.read (), path = file, silent = silent)


CLUSTER_SUBCOMMANDS = ("create", "destroy", "update", "show", "plan")
@cli.command ()
@click.argument ('subcommand')
@click.option ('-y', '--yes', is_flag = True)
@click.pass_context
def cluster (context, subcommand, yes):
    """
    SUBCOMMAND: create | destroy | update | show | plan
    """
    assert subcommand in CLUSTER_SUBCOMMANDS
    cli = context.obj ["cli"]
    out_tf = cli.generate_cluster_declares ()
    if subcommand == "show":
        print (out_tf)
        return
    if subcommand in ("create", "update", "plan"):
        return cli.create_cluster (subcommand == "plan")

    if not yes:
        cluter_name = cli.d ["x-ecs-cluster"]['name']
        ans = input (f"You are going to destroy cluster, type `{cluter_name}` if you are sure: ")
        if ans != cluter_name:
            print ('canceled')
            return
    cli.remove_cluster ()


SERVICE_SUBCOMMANDS = ("up", "down", "show", "plan")
@cli.command ()
@click.argument ('subcommand')
@click.argument ('stage', envvar = 'SERVICE_STAGE', default = "qa")
@click.argument ('tag', envvar = 'CI_COMMIT_SHA', default = "latest")
@click.option ('-y', '--yes', is_flag = True)
@click.option ('-t', '--latest', is_flag = True)
@click.pass_context
def service (context, subcommand, stage, tag, latest, yes):
    """
    SUBCOMMAND: up | down | show | plan
    """
    if latest:
        tag = "latest"
    assert subcommand in SERVICE_SUBCOMMANDS
    cli = context.obj ["cli"]
    out_tfs = cli.generate_service_declares (stage, tag [:8])
    if subcommand == "show":
        for k, v in out_tfs.items ():
            print (k)
            print ('───────────────────────────────────────────────────────')
            print (v)
        return

    if subcommand in ("up", "plan"):
        return cli.deploy_service (stage, subcommand == "plan")
    if not yes:
        service_name = cli.d ["x-ecs-service"]['name']
        ans = input (f"You are going to shutdown service, type `{service_name}` if you are sure: ")
        if ans != service_name:
            print ('canceled')
            return
    return cli.remove_service (stage)


def main ():
    cli (obj = {})

if __name__ == "__main__":
    main ()
