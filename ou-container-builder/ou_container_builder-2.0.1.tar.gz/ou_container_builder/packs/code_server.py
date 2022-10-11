"""Pack to install the Code Server interface."""
from jinja2 import Environment

from ..utils import merge_settings


def process_settings(settings: dict, pack_settings: dict) -> dict:
    """
    Process the user-provided settings.

    :param settings: The settings parsed from the configuration file
    :type settings: dict
    :param pack_settings: The pack-specific settings parsed from the configuration file
    :type settings: dict
    :return: The updated settings
    :rtype: dict
    """
    settings = merge_settings(settings, {
        'sources': {
            'apt': [
                {
                    'name': 'nodesource',
                    'key_url': 'https://deb.nodesource.com/gpgkey/nodesource.gpg.key',
                    'deb': {
                        'url': 'https://deb.nodesource.com/node_18.x',
                        'distribution': 'bullseye',
                        'component': 'main'
                    }
                }
            ],
        },
        'packages': {
            'apt': [
                'nodejs',
                'yarn'
            ],
        },
        'scripts': {
            'build': [
                {
                    'commands': [
                        'cd /opt',
                        'wget https://github.com/coder/code-server/releases/download/v4.6.1/code-server-4.6.1-linux-amd64.tar.gz',  # noqa: E501
                        'tar -zxvf code-server-4.6.1-linux-amd64.tar.gz',
                        'ln -s /opt/code-server-4.6.1-linux-amd64/bin/code-server /usr/local/bin',
                    ]
                }
            ]
        },
        'web_apps': [
            {
                'path': '/code-server/',
                'cmdline': [
                    'code-server',
                    '--auth',
                    'none',
                    '--disable-update-check',
                    '--bind-addr',
                    '0.0.0.0',
                    '--port',
                    '{port}'
                ],
                'timeout': 60,
                'default': True
            }
        ],
    })
    return settings


def generate_files(context: str, env: Environment, settings: dict, pack_settings: dict) -> None:
    """Generate the build files for the code-server pack.

    This ensures that the the code-server is installed

    :param context: The context path within which the generation is running
    :type context: str
    :param env: The Jinja2 environment to use for loading and rendering templates
    :type env: :class:`~jinja2.environment.Environment`
    :param settings: The validated settings
    :type settings: dict
    :param pack_settings: The validated pack-specific settings
    :type settings: dict
    """
    pass
