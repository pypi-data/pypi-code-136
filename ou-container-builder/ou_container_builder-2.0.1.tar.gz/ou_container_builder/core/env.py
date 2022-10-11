"""Pack to handle setting up environment variables in the container."""
from jinja2 import Environment


def process_settings(settings: dict) -> dict:
    """Process the env core settings.

    :param settings: The settings parsed from the configuration file
    :type settings: dict
    :return: The updated settings
    :rtype: dict
    """
    return settings


def generate_files(context: str, env: Environment, settings: dict) -> dict:
    """Generate the build files for the env core.

    :param context: The context path within which the generation is running
    :type context: str
    :param env: The Jinja2 environment to use for loading and rendering templates
    :type env: :class:`~jinja2.environment.Environment`
    :param settings: The validated settings
    :type settings: dict
    """
    pass
