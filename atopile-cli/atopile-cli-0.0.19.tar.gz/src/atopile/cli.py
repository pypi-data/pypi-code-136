import asyncio
import json
import logging
from pathlib import Path
from typing import List

import click

from . import build, options, utils, init_project, lib, resources
from .config_data import load_config_data, save_config_data

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def ensure_dir(dir: Path):
    if not dir.exists():
        dir.mkdir(parents=True)
        log.info(f'creating {str(dir)}')

@click.group()
@click.option('--options', '-o', 'options_list', multiple=True)
def cli(options_list: List[str]):
    if options_list:
        options_dict = {}
        for option in options_list:
            k, v = option.split('=', 1)
            v = v.strip('"\' \t\n')
            options_dict[k] = v
        options.update_options(options_dict, options.Level.CLI_OPTION)

@cli.command('options')
def cli_print_options():
    """Show information about configuration options available."""
    print(utils.reindent_str(
        """
        Configuration options.

        Settable via `-o/--options option=value` after `ato`, environment variables, etc...
        In order of increasing precedance:
        """,
        indent = 4
    ))
    for level in options.Level:
        print(f'     - {level.name}')
    print()
    options.print_options()

@cli.command('run')
@click.argument('task')
@options.project_dir.as_click_arg(required=False)
def cli_build(project_dir, task):
    """Build your project."""
    if project_dir:
        options.project_dir.set_value(project_dir, options.Level.CLICK_OPTION)

    try:
        build.build(task)
    except utils.AtopileError:
        exit(1)

@cli.command('init')
@click.argument('project_dir', 
                type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option("-m",
              "--merge",
              is_flag=True,
              show_default=True,
              default=False,
              help="Merge changes with the existing yaml file, preferring the existing file.")
def cli_init(project_dir, merge):
    """
    Add all the atopiley things to your project.
    """
    init_project.init_project(project_dir, merge)
    
@cli.group('kicad-lib')
def kicad_lib():
    pass

# install a resource to the project
@cli.command('install')
@click.argument('urls', nargs=-1, required=False)
@click.option('-n', '--name')
@click.option('-b', '--branch')
@options.project_dir.as_click_option()
def cli_install(urls, name, branch, project_dir):
    """
    Install a resource into your project if a resource 
    is specified, else, install all resources defined 
    in the config file to this system.

    eg. ato install

    eg. ato install gitlab.atopile.io/atopile/kibot.git

    If you want to specify a branch or name other than default, use the -b or -n flags.
    Note: These are only compatible with a single resource at a time.
    """
    if project_dir:
        options.project_dir.set_value(project_dir, options.Level.CLICK_OPTION)

    config_data = load_config_data()

    # make sure the urls are unqiue
    urls = list(set(urls))

    # figure out what to install based on the args
    if urls:
        if name or branch:
            if len(urls) > 1:
                log.error('You can only specify a name or branch for a single resource.')
                exit(1)
            else:
                resources_to_install = [resources.GitResource.from_url(urls[0], branch, name)]
        else:
            resources_to_install = [resources.GitResource.from_url(url) for url in urls]
        
    else:
        resources_to_install = resources.parse_resources(config_data['resources'])

    # do the installing
    async def do_install():
        installers = [r.install() for r in resources_to_install]
        await asyncio.gather(*installers)
    asyncio.run(do_install())

    # modify the config data if applicable
    if urls:
        config_data['resources'] += [r.to_dict() for r in resources_to_install]

    save_config_data(config_data)


# update a resource
@cli.command('update')
@click.argument('which_resources', nargs=-1, required=False)
@options.project_dir.as_click_option()
def cli_install(which_resources, project_dir):
    """
    Update a resource in your project if a resource
    """
    if project_dir:
        options.project_dir.set_value(project_dir, options.Level.CLICK_OPTION)

    config_data = load_config_data()
    current_resources = resources.parse_resources(config_data['resources'])
    current_resources_by_reference = {r.reference: r for r in current_resources}

    # make sure the urls are unqiue
    urls = list(set(urls))

    # figure out what to install based on the args
    if urls:
        resources_to_install = []
        for which_resource in which_resources:
            resources_to_install.append(interpret_ref(which_resource))
    else:
        resources_to_install = current_resources_by_reference.keys()
    resources_to_install = set(resources_to_install)

    # do the installing
    async def do_install():
        installers = [r.install() for r in resources_to_install]
        await asyncio.gather(*installers)
    asyncio.run(do_install())


def interpret_ref(ref: str, config_data: dict):
    """
    Figure out what "ref" is and return a path to it.
    """
    try:
        # is it soemthing explicit
        return utils.resolve_project_relative_ref(ref)
    except FileNotFoundError:
        pass

    # maybe it's a URL or reference?
    resources_by_ref = {r.reference: r for r in resources.parse_resources(config_data['resources'])}
    if lib in resources_by_ref:
        return utils.resolve_project_relative_ref(resources_by_ref[lib].path)
        
    # maybe it's a name of something?
    path_matches = list(options.project_atopile_dir.value.glob(f'**/{ref}'))
    if len(path_matches) == 1:
        return path_matches[0]
    else:
        log.warning(f'More than one path matched {ref} in {options.project_atopile_dir.value}')

    # yeah, I dunno what you're talking about
    log.error(f'Could not find {ref}.')
    raise FileNotFoundError

@kicad_lib.command('add')
@click.argument('lib_to_add')
@click.argument('kicad_project')
@options.project_dir.as_click_option()
def cli_add_kicad_lib(lib_to_add, kicad_project, project_dir):
    """Add a new library to the project's dependencies."""
    if project_dir:
        options.project_dir.set_value(project_dir, options.Level.CLICK_OPTION)
    project_dir = options.project_dir.value
    config_data = load_config_data()

    # figure out which kicad project the user's talking about
    kicad_project = utils.resolve_project_relative_ref(kicad_project)
    if not kicad_project.suffix == '.kicad_pro':
        log.error(f'{kicad_project} is not a .kicad_pro file.')
        exit(1)

    # figure out which library the user's talking about
    lib_to_add = interpret_ref(lib_to_add, config_data)

    # if the user referenced a directory, index it for them
    # otherwise, add the library to the project's dependencies
    if (project_dir / lib_to_add).is_dir():
        lib.index_kicad_libs(config_data, indexing_path=lib_to_add, kicad_project=kicad_project)
    else:
        lib_list = config_data.setdefault('libs', {}).setdefault(str(kicad_project), [])
        if str(lib_to_add) not in lib_list:
            lib_list.append(str(lib_to_add))

    lib.dump_kicad_lib_tables(config_data)

    save_config_data(config_data)

if __name__ == '__main__':
    cli()
