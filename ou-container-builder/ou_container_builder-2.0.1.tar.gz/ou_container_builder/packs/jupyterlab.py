"""Pack to install the Jupyterlab interface."""
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
        'packages': {
            'pip': ['jupyterlab>=3.4.3<4.0.0']
        },
        'server': {
            'default_path': '/lab'
        },
    })
    return settings


def generate_files(context: str, env: Environment, settings: dict, pack_settings: dict) -> None:
    """Generate the build files for the jupyterlab pack.

    This ensures that the the jupyterlab package is installed

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
