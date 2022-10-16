import os
import ast
import sys
import click
import boto3
import time
import pyperclip
import pkg_resources
import ec2_manager
from pprint import pformat
from importlib.machinery import SourceFileLoader

try:
    VERSION = pkg_resources.get_distribution(ec2_manager.__name__).version
except:
    VERSION = 0


class OverrideCollector(ast.NodeVisitor):
    """
    Collects the override classes.
    """

    def __init__(self, file_path):
        super(OverrideCollector, self).__init__()
        module_name, extension = os.path.splitext(os.path.basename(file_path))
        self._module = SourceFileLoader(module_name, file_path).load_module()
        self._classes = []

        if os.path.exists(file_path):
            with open(file_path) as test_case_file:
                parsed_file = ast.parse(test_case_file.read())
                self.visit(parsed_file)

    def visit_ClassDef(self, node):
        """
        Override the method that visits nodes that are classes.
        """
        visited_class = getattr(self._module, node.name)

        if issubclass(visited_class, ec2_manager.EC2Manager):
            if visited_class not in self._classes:
                self._classes.append(visited_class)

    def __call__(self, *args, **kwargs):
        """
        Gets the classes.

        :returns: EC2Manager subclasses.
        """
        return self._classes


config = click.option(
    '--config',
    default=os.environ.get('EC2_MANAGER_CONFIG', 'config.yaml'),
    help='Path to config file.',
    required=True
)
repo = click.option(
    '--repo',
    default=os.environ.get('REPO'),
    help='The name of the repo i.e. "Hello-World"',
    required=False
)
github_username = click.option(
    '--github-username',
    default=os.environ.get('GITHUB_USERNAME'),
    help='Your github username i.e. "octocat"',
    required=False
)
github_token = click.option(
    '--github-token',
    default=os.environ.get('GITHUB_TOKEN'),
    help='A github personal access token that has permission to pull the repo',
    required=True
)
override_file = click.option(
    '--override-file',
    default=None,
    help='Path to the python file that overrides the base EC2Manager class.'
)


def get_class(kwargs):
    config_file = kwargs.get('config', 'config.yaml')
    file_path = kwargs.get('override_file') or 'override.py'

    if not os.path.exists(config_file):
        raise click.UsageError(f'The config file "{config_file}" was not found.')

    if kwargs.get('override_file') and not os.path.exists(file_path):
        raise click.UsageError(f'The override file {file_path} was not found on disk.')

    override_classes = OverrideCollector(file_path)()
    if len(override_classes) > 1:
        raise click.UsageError(
            f'There are more than one override classes found:\n {pformat([i.__name__ for i in override_classes])}.')

    if not override_classes:
        click.echo(
            f'No override class in file {file_path} was found. Defaulting to {ec2_manager.EC2Manager.__name__} class.'
        )
        return ec2_manager.EC2Manager

    return override_classes[0]


def get_first_env_file_data(kwargs):
    ec2_manager_instance = ec2_manager.EC2Manager(**kwargs)
    config = ec2_manager_instance.get_config()

    file_name = '.env'
    env_var = 'ENV_FILE'

    # try and get the first env file name from the config
    instances = list(config.get('instances', {}).values())
    if instances:
        env_file_data = instances[0].get('encoded_env_file', {})
        file_name = env_file_data.get('file_name', '.env')
        env_var = env_file_data.get('env_var', 'ENV_FILE')
    return file_name, env_var


def get_encoded_env_file(kwargs):
    file_name, env_var = get_first_env_file_data(kwargs)

    default_file_path = os.path.join(os.getcwd(), 'compose', file_name)
    env_file_path = click.prompt(
        'Please enter the local env file path',
        default=default_file_path if os.path.exists(default_file_path) else None
    )
    if not os.path.exists(env_file_path):
        click.echo(f'There was no env file found on disk at "{env_file_path}"!')
        return False

    # read the env file and encode it
    with open(env_file_path, 'r') as env_file:
        return ec2_manager.EC2Manager.encode_string(env_file.read())


@click.group(
    name='ec2-manager',
    help=f'EC2 Manager version {VERSION}. A CLI tool for quick and cost effective EC2 management.'
)
def cli():
    pass


@click.command()
def init():
    if click.confirm(f'Continue setting up project and overwrite files in this folder {os.getcwd()}'):
        # setup local project on disk
        ec2_manager_instance = ec2_manager.EC2Manager()
        ec2_manager_instance.init()


@click.command()
@repo
@github_username
@github_token
def set_secrets(**kwargs):
    token = kwargs.get('github_token')

    secrets = {}
    ec2_manager_instance = ec2_manager.EC2Manager(**kwargs)

    try:
        repo_name = ec2_manager_instance.repo
        username = ec2_manager_instance.github_user
        repo_instance = ec2_manager_instance.get_repo()
    except Exception as error:
        data = getattr(error, 'data', None)
        if data:
            message = data.get('message')
            if message:
                click.echo(f'Repo "{username}/{repo_name}" {message.lower()}')
                return
        raise error

    if click.confirm(f'Do you want to update your github token?'):
        secrets['GH_TOKEN'] = click.prompt(
            'Please enter your GH_TOKEN [****************************************]',
            default=token,
            show_default=False
        )

    if click.confirm(f'Do you want to update your AWS credentials?'):
        user_session = boto3.session.Session()
        user_credentials = user_session.get_credentials()

        time.sleep(0.1)
        print()
        secrets['AWS_REGION'] = click.prompt(
            'Please enter your AWS_REGION',
            default=user_session.region_name
        )
        secrets['AWS_ACCESS_KEY_ID'] = click.prompt(
            'Please enter your AWS_ACCESS_KEY [********************]',
            default=user_credentials.access_key,
            show_default=False
        )
        secrets['AWS_SECRET_ACCESS_KEY'] = click.prompt(
            'Please enter your AWS_SECRET_KEY [****************************************]',
            default=user_credentials.secret_key,
            show_default=False
        )

    if click.confirm(
            f'Do you want to update your encoded env file?'
    ):
        while True:
            key_name = click.prompt(
                'Please enter the env file secret name',
                default=get_first_env_file_data(kwargs)[-1]
            )
            encoded_env_file = get_encoded_env_file(kwargs)
            if not encoded_env_file:
                continue

            secrets[key_name] = encoded_env_file

            if click.confirm(f'Do you want to add another env file?'):
                continue
            else:
                break

    if secrets:
        if click.confirm(
                f'Do you want to set these secrets {list(secrets.keys())} on the repo f"{username}/{repo_name}"?'
        ):
            for key, value in secrets.items():
                click.echo(f'Setting {key} on {username}/{repo_name}...')
                repo_instance.create_secret(key, value)


@click.command()
def copy_env(**kwargs):
    encoded_env_file = get_encoded_env_file(kwargs)
    if encoded_env_file:
        pyperclip.copy(encoded_env_file)
        print(f'Copied encoded file content to clip board!')


@click.command()
@config
def destroy(**kwargs):
    ec2_manager_instance = get_class(kwargs)(**kwargs)
    ec2_manager_instance.destroy()


@click.command()
@repo
@github_username
@github_token
@override_file
def apply(**kwargs):
    ec2_manager_instance = get_class(kwargs)(**kwargs)
    ec2_manager_instance.apply()


def main():
    cli.add_command(init)
    cli.add_command(apply)
    cli.add_command(set_secrets)
    cli.add_command(copy_env)
    cli.add_command(destroy)
    cli()


if __name__ == '__main__':
    sys.exit(main())
