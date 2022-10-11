"""Pack to handle setting up content in the container.

This ensures that the OU Container Content application is integrated into the container and that all configured
files are distributed in the container as configured. This also sets the ``ou_container_content`` flag to ensure
that the OU Container Content application is run upon container startup.
"""
import os

from jinja2 import Environment

from ..utils import merge_settings, render_template


def process_settings(settings: dict) -> dict:
    """Process the content core settings.

    :param settings: The settings parsed from the configuration file
    :type settings: dict
    :return: The updated settings
    :rtype: dict
    """
    if 'content' in settings and settings['content']:
        settings = merge_settings(settings, {
            'flags': {
                'ou_container_content': True
            }
        })
    if 'flags' in settings and settings['flags']:
        if 'ou_container_content' in settings['flags'] and settings['flags']['ou_container_content']:
            settings = merge_settings(settings, {
                'packages': {
                    'pip': [
                        'ou-container-content>=1.1.1'
                    ]
                },
                'scripts': {
                    'build': [
                        {
                            'commands': [
                                'ou-container-content prepare'
                            ]
                        }
                    ]
                }
            })
    return settings


def generate_files(context: str, env: Environment, settings: dict) -> None:
    """Generate the build files for the content core.

    :param context: The context path within which the generation is running
    :type context: str
    :param env: The Jinja2 environment to use for loading and rendering templates
    :type env: :class:`~jinja2.environment.Environment`
    :param settings: The validated settings
    :type settings: dict
    """
    if 'flags' in settings and settings['flags']:
        if 'ou_container_content' in settings['flags'] and settings['flags']['ou_container_content']:
            render_template(context,
                            env,
                            'core/content/content_config.yaml',
                            os.path.join('ou-builder-build', 'content', 'content_config.yaml'),
                            settings)
