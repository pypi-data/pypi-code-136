import argparse
import logging
import os.path
import subprocess

import rich
import typer

from myccli.compiler import Compiler
from myccli.config import MyceliumConfiguration, LOGGER_NAME, DEFAULT_DIST_DIR

app = typer.Typer()
cli_state = {
    'verbose': False
}


@app.command()
def compile(app_import_str: str):
    """
    Analyzes the current application and generates the corresponding Terraform.
    """
    project_path = os.path.abspath('.')

    config = MyceliumConfiguration.default(verbose=cli_state['verbose'])

    compiler = Compiler(project_path, app_import_str, config)
    compiler.compile()


@app.command()
def deploy():
    """
    Deploys the last generated terraform code.
    """
    if not os.path.exists(os.path.join(DEFAULT_DIST_DIR, '.terraform')):
        # rich.print('[bold yellow]WARNING: Terraform has not been initialized yet.')
        # do_init = typer.confirm('Do you want to initialize Terraform (terraform init)?')
        # if not do_init:
        #     raise typer.Abort()
        #
        subprocess.check_call('terraform init', shell=True, cwd=DEFAULT_DIST_DIR)
        print('\n')

    subprocess.check_call('terraform apply -auto-approve', shell=True, cwd=DEFAULT_DIST_DIR)


@app.command()
def destroy(
        force: bool = typer.Option(False, '-f', '--force')
):
    """
    Tears down all resources created by the last deployment.
    """
    cmd = 'terraform destroy'
    if force:
        cmd += ' -auto-approve'

    subprocess.check_call(cmd, shell=True, cwd=DEFAULT_DIST_DIR)


@app.callback()
def callback(
        verbose: bool = typer.Option(False, '-v', '--verbose')
):
    """
    Mycelium CLI
    """
    cli_state['verbose'] = verbose
    if verbose:
        logging.getLogger(LOGGER_NAME).setLevel(logging.DEBUG)


def run_cli():
    app()
