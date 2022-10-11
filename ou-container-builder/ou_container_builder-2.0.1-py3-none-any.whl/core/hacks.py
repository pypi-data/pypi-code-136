"""Pack to handle built-in hacks."""
from jinja2 import Environment


def process_settings(settings: dict) -> dict:
    """Process the hacks core settings.

    :param settings: The settings parsed from the configuration file
    :type settings: dict
    :return: The updated settings
    :rtype: dict
    """
    if 'packages' in settings and 'apt' in settings['packages']:
        if 'openjdk-11-jdk' in settings['packages']['apt']:
            if 'hacks' in settings:
                if 'missing-man1' not in settings['hacks']:
                    settings['hacks'].append('missing-man1')
            else:
                settings['hacks'] = ['missing-man1']
    return settings


def generate_files(context: str, env: Environment, settings: dict) -> dict:
    """Generate the build files for the hacks core.

    :param context: The context path within which the generation is running
    :type context: str
    :param env: The Jinja2 environment to use for loading and rendering templates
    :type env: :class:`~jinja2.environment.Environment`
    :param settings: The validated settings
    :type settings: dict
    """
    pass
