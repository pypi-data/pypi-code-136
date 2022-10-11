"""The main OU Container Builder commandline application.

Run ``ou-container-builder --help`` for help with the command-line parameters.
"""
import os
import shutil
import subprocess

from jinja2 import Environment, PackageLoader

from . import packs, core
from .validator import validate_settings
from .utils import merge_settings


def clean_build(context: str) -> None:
    """Clean the build files.

    :param context: The context directory containing the build files.
    :type context: str
    """
    if os.path.exists(os.path.join(context, 'Dockerfile')):
        os.unlink(os.path.join(context, 'Dockerfile'))
    if os.path.exists(os.path.join(context, 'ou-builder-build')):
        shutil.rmtree(os.path.join(context, 'ou-builder-build'))


def process_settings(settings: dict) -> dict:
    """Process the settings.

    :param settings: The settings provided by the user on the command-line
    :type settings: dict
    :return: The validated settings
    :rtype: dict
    """
    settings = validate_settings(settings)
    # Setup the base settings
    settings = merge_settings({}, settings)
    # Handle optional packs
    if 'packs' in settings:
        for pack in settings['packs']:
            if pack['name'] == 'code_server':
                settings = packs.code_server.process_settings(settings, pack['options'])
            elif pack['name'] == 'jupyterlab':
                settings = packs.jupyterlab.process_settings(settings, pack['options'])
            elif pack['name'] == 'mariadb':
                settings = packs.mariadb.process_settings(settings, pack['options'])
            elif pack['name'] == 'nbclassic':
                settings = packs.nbclassic.process_settings(settings, pack['options'])
            elif pack['name'] == 'tutorial_server':
                settings = packs.tutorial_server.process_settings(settings, pack['options'])
    # Handle core packs
    settings = core.env.process_settings(settings)
    if 'services' in settings:
        settings = core.services.process_settings(settings)
    if 'scripts' in settings:
        settings = core.scripts.process_settings(settings)
    if 'web_apps' in settings:
        settings = core.web_apps.process_settings(settings)
    settings = core.hacks.process_settings(settings)
    settings = core.jupyter_server.process_settings(settings)
    settings = core.startup.process_settings(settings)
    settings = core.content.process_settings(settings)
    settings = core.packages.process_settings(settings)
    return validate_settings(settings)


def generate_files(settings: dict, context: str, env: Environment) -> None:
    """Generate the files required for the Docker build.

    :param settings: The validated settings
    :type settings: dict
    :param context: The context directory
    :type context: str
    :param en: The jinja2 environment
    :type env: :class:`~jinja2.environment.Environment`
    """
    if 'packs' in settings:
        for pack in settings['packs']:
            if pack['name'] == 'code_server':
                packs.code_server.generate_files(context, env, settings, pack['options'])
            elif pack['name'] == 'jupyterlab':
                packs.jupyterlab.generate_files(context, env, settings, pack['options'])
            elif pack['name'] == 'mariadb':
                packs.mariadb.generate_files(context, env, settings, pack['options'])
            elif pack['name'] == 'nbclassic':
                packs.nbclassic.generate_files(context, env, settings, pack['options'])
            elif pack['name'] == 'tutorial_server':
                packs.tutorial_server.generate_files(context, env, settings, pack['options'])
    core.env.generate_files(context, env, settings)
    if 'services' in settings:
        core.services.generate_files(context, env, settings)
    if 'scripts' in settings:
        core.scripts.generate_files(context, env, settings)
    if 'web_apps' in settings:
        core.web_apps.generate_files(context, env, settings)
    core.hacks.generate_files(context, env, settings)
    core.jupyter_server.generate_files(context, env, settings)
    core.startup.generate_files(context, env, settings)
    core.content.generate_files(context, env, settings)
    core.packages.generate_files(context, env, settings)

    # Generate the Dockerfile
    with open(os.path.join(context, 'Dockerfile'), 'w') as out_f:
        tmpl = env.get_template('Dockerfile.jinja2')
        out_f.write(tmpl.render(**settings))


def docker_build(context: str, tag: list) -> None:
    """Run the docker build.

    :param context: The build context directory
    :type context: str
    :param tag: The tags to apply to the Docker image
    :type tag: list
    """
    cmd = ['docker', 'build', context]
    if tag:
        for t in tag:
            cmd.append('--tag')
            cmd.append(t)
    subprocess.run(cmd)


def run_build(settings: dict, context: str, build: bool, clean: bool, tag: list) -> None:
    """Run the build process.

    This processes the ``settings``, generates the required files, and then runs the Docker build process.

    :param settings: The settings parsed from the configuration file
    :type settings: dict
    :param context: The directory within which to run the build
    :type context: str
    :param build: Whether to automatically invoke ``docker build``
    :type build: bool
    :param clean: Whether to automatically clean all generated files
    :type clean: bool
    :param tag: A list of tags to pass to docker
    :type tag: list[str]
    :return: A list with any errors that occured during processing
    :rtype: list
    """
    # Process and validate the settings
    settings = process_settings(settings)
    # Setup the build environment
    env = Environment(loader=PackageLoader('ou_container_builder', 'templates'), autoescape=False)
    clean_build(context)
    os.makedirs(os.path.join(context, 'ou-builder-build'))
    # Run the file generation
    generate_files(settings, context, env)

    if build:
        docker_build(context, tag)
        if clean:
            clean_build(context)
