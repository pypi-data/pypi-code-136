"""The main OU Container Builder commandline application.

Run ``ou-container-builder --help`` for help with the command-line parameters.
"""
import click
import os

from yaml import safe_load

from .builder import run_build


@click.command()
@click.option('-c', '--context',
              default='.',
              help='Context within which the container will be built',
              show_default=True)
@click.option('-b/-nb', '--build/--no-build',
              default=True,
              help='Automatically build the container',
              show_default=True)
@click.option('--clean/--no-clean',
              default=True,
              help='Automatically clean up after building the container',
              show_default=True)
@click.option('--tag',
              multiple=True,
              help='Automatically tag the generated image')
def main(context: str, build: bool, clean: bool, tag: list):
    """Build your OU Container."""
    with open(os.path.join(context, 'ContainerConfig.yaml')) as config_f:
        settings = safe_load(config_f)
    result = run_build(settings, context, build, clean, tag)
    if result:
        click.echo(click.style('There are errors in your configuration settings:', fg='red'), err=True)
        click.echo(err=True)
        for error in result:
            click.echo(error, err=True)


if __name__ == '__main__':
    main()
