"""Pack to handle setting up the startup process in the container.

Generates the startup script and the sudoers file to ensure the user can chown their home-directory.
"""
import os.path

from jinja2 import Environment

from ..utils import merge_settings, render_template


def process_settings(settings: dict) -> dict:
    """Process the startup core settings.

    :param settings: The settings parsed from the configuration file
    :type settings: dict
    :return: The updated settings
    :rtype: dict
    """
    settings = merge_settings(settings, {
        'content': [
            {
                'source': 'ou-builder-build/startup/start.sh',
                'target': '/usr/bin/start.sh',
                'overwrite': 'always'
            },
            {
                'source': 'ou-builder-build/startup/home-dir.sudoers',
                'target': '/etc/sudoers.d/99-home-dir',
                'overwrite': 'always'
            }
        ],
        'scripts': {
            'build': [
                {
                    'commands': [
                        'chmod a+x /usr/bin/start.sh',
                        'chmod 0660 /etc/sudoers.d/99-home-dir'
                    ]
                }
            ]
        }
    })
    return settings


def generate_files(context: str, env: Environment, settings: dict) -> dict:
    """Generate the build files for the startup core.

    :param context: The context path within which the generation is running
    :type context: str
    :param env: The Jinja2 environment to use for loading and rendering templates
    :type env: :class:`~jinja2.environment.Environment`
    :param settings: The validated settings
    :type settings: dict
    """
    # Generate the start script
    render_template(context,
                    env,
                    'core/startup/start.sh',
                    os.path.join('ou-builder-build', 'startup', 'start.sh'),
                    settings)
    # Generate the home-dir chown sudoers
    render_template(context,
                    env,
                    'core/startup/home-dir.sudoers',
                    os.path.join('ou-builder-build', 'startup', 'home-dir.sudoers'),
                    settings)
