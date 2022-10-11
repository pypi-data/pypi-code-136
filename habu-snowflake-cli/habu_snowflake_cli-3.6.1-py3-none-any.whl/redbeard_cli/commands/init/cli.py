import click

from redbeard_cli import snowflake_utils
from redbeard_cli.commands.init import (
    habu_setup as habu_setup_command
)


@click.command("version")
def version():
    habu_setup_command.pkg_version()


@click.command("generate-config")
def generate_config():
    habu_setup_command.generate_config()


@click.group()
def init():
    pass


@init.command(
    help="""Initialize Full Habu Snowflake framework.\n
    This will create all the objects required to run the Habu Agent in the specified Snowflake account.\n
    This includes:\n
      * Databases:\n
        * HABU_CLEAN_ROOM_COMMON\n
        * HABU_DATA_CONNECTIONS\n
    """
)
@click.option('-o', '--organization_id', required=True, help='Habu Organization ID')
@click.option('-c', '--config-file', default="./habu_snowflake_config.yaml",
              help='Snowflake account configuration file')
@click.option('-h', '--habu-account',
              help='Habu Snowflake account details used for orchestration in following format: <HABU_ORGANIZATION_NAME>.<HABU_ACCOUNT_NAME>')
def habu_framework(habu_account: str, config_file: str, organization_id: str):
    sf_connection, connection_params = snowflake_utils.new_connection_from_yaml_file(config_file)
    habu_setup_command.init_framework(sf_connection, organization_id, habu_account, connection_params['warehouse'])
