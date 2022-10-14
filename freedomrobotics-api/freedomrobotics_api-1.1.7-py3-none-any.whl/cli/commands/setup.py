import click

from freedomrobotics_api.cli.commands.base import add_options, common_options, error_message_catch

from freedomrobotics_api import FreedomClient
from freedomrobotics_api.credentials import (
    credentials_exist, Credentials, CREDENTIALS_PATH
)


@click.command()
@add_options(common_options)
@click.option('--force', default=False, is_flag=True)
def setup(**kwargs):
    user = kwargs.get('user')
    env = kwargs.get('env')
    force = kwargs.get('force')
    from freedomrobotics_api.api_handler import login

    if credentials_exist() and not force:
        click.confirm(
            click.style(
                f'There are already existent credentials on {CREDENTIALS_PATH}. '
                f'Are you sure you want to override them?',
                fg='yellow',
            ),
            abort=True
        )

    # Gather user information
    click.echo("OK, let's first login to the application in order to generate a token.")
    if not user:
        user = click.prompt("Insert user/email", type=str)

    password = click.prompt(f"Insert password for [{user}]", hide_input=True)

    with error_message_catch('Login'):
        url, token_id, secret = login(username=user, password=password, env=env)

    client = FreedomClient(token=token_id, secret=secret, url=url, env=env)

    # Create a token without expiration with same permissions
    with error_message_catch('New token creation'):
        token = client.get_token(token_id)
        description = f"Freedom CLI token created for user {user}"
        result = client.create_token(
            token.allowed_actions,
            token.accounts,
            token.devices,
            description,
            create_secret=True,
            raw=True,
            type="freedom_cli",
        )
        new_token_id = result['token']
        new_secret = result['secret']

    # Save the new credentials
    with error_message_catch('Credentials generation'):
        Credentials(token=new_token_id, secret=new_secret, url=url).save()
