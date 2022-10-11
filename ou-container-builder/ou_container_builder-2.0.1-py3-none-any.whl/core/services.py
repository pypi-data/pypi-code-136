"""Pack to setup and run system services.

Automatically generates a sudoers file that ensures that the default user can start and stop all services.
"""
import os

from jinja2 import Environment

from ..utils import merge_settings, render_template


def process_settings(settings: dict) -> dict:
    """Process the services core settings.

    :param settings: The settings parsed from the configuration file
    :type settings: dict
    :return: The updated settings
    :rtype: dict
    """
    settings = merge_settings(settings, {
        'content': [
            {
                'source': 'ou-builder-build/services/services.sudoers',
                'target': '/etc/sudoers.d/99-services',
                'overwrite': 'always'
            }
        ],
        'flags': {
            'ou_container_content': True
        }
    })
    return settings


def generate_files(context: str, env: Environment, settings: dict) -> None:
    """Generate the build files for the services core.

    :param context: The context path within which the generation is running
    :type context: str
    :param env: The Jinja2 environment to use for loading and rendering templates
    :type env: :class:`~jinja2.environment.Environment`
    :param settings: The validated settings
    :type settings: dict
    """
    render_template(context,
                    env,
                    'core/services/sudoers',
                    os.path.join('ou-builder-build', 'services', 'services.sudoers'),
                    settings)
