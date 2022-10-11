"""Pack to install the MariaDB database."""
import os

from jinja2 import Environment

from ..utils import merge_settings, render_template


def process_settings(settings: dict, pack_settings: dict) -> dict:
    """Process the user-provided settings.

    :param settings: The settings parsed from the configuration file
    :type settings: dict
    :param pack_settings: The pack-specific settings parsed from the configuration file
    :type settings: dict
    :return: The updated settings
    :rtype: dict
    """
    settings = merge_settings(settings, {
        'packages': {
            'apt': ['mariadb-server', 'sudo']
        },
        'scripts': {
            'build': [
                {
                    'commands': [
                        'mkdir -p /run/mysqld',
                        f'sed -e "s#datadir.*=.*#datadir = $HOME/mariadb#" -e "s#user.*=.*#user = {settings["image"]["user"]}#" -i /etc/mysql/mariadb.conf.d/50-server.cnf',  # noqa: E501
                        f'chown -R {settings["image"]["user"]}: /var/log/mysql /run/mysqld',
                        'chmod a+x /usr/bin/mariadb-setup.sh',
                        f'printf "{settings["image"]["user"]} ALL=NOPASSWD: /usr/bin/mariadb-setup.sh\\n" > /etc/sudoers.d/99-mariadb'  # noqa: E501
                    ]
                },
            ],
            'startup': [
                {
                    'commands': [
                        'sudo /usr/bin/mariadb-setup.sh'
                    ]
                }
            ]
        },
        'services': [
            'mariadb'
        ],
        'content': [
            {
                'source': '/var/lib/mysql',
                'target': 'mariadb',
                'overwrite': 'never'
            },
            {
                'source': 'ou-builder-build/mariadb/mariadb-setup.sh',
                'target': '/usr/bin/mariadb-setup.sh',
                'overwrite': 'always'
            }
        ]
    })
    return settings


def generate_files(context: str, env: Environment, settings: dict, pack_settings: dict) -> None:
    """Generate the build files for the mariadb pack.

    This ensures that the the mariadb service is activated and that the configured database is set up in the user's
    home-directory.

    :param context: The context path within which the generation is running
    :type context: str
    :param env: The Jinja2 environment to use for loading and rendering templates
    :type env: :class:`~jinja2.environment.Environment`
    :param settings: The validated settings
    :type settings: dict
    :param pack_settings: The validated pack-specific settings
    :type settings: dict
    """
    render_template(context,
                    env,
                    'packs/mariadb/setup.sh',
                    os.path.join('ou-builder-build', 'mariadb', 'mariadb-setup.sh'),
                    pack_settings)
