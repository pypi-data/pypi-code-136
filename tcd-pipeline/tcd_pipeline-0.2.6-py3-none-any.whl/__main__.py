"""Main CLI application"""

import click

from tcd_pipeline.commands import generate_workflows


@click.group(help="TCD Pipeline tools")
@click.version_option(package_name="tcd_pipeline", message="version %(version)s")
def cli():
    """Main cli function"""


cli.add_command(generate_workflows.generate_workflows)

if __name__ == '__main__':
    cli()
