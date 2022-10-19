import collections.abc
import json
import os
from enum import IntEnum
from functools import partial
from pathlib import Path
from typing import Any, Dict

import click

from . import utils

# Define option tools and classes

class Level(IntEnum):
    UNSET = 0
    DEFAULT = 1
    ENV = 2
    PRJ = 3
    TASK = 4
    CLI_OPTION = 5
    CLICK_OPTION = 6

class Option:
    def __init__(self, name: str, env_name: str = None, default = None, help: str = '', getter: collections.abc.Callable = None) -> None:
        _options[name] = self

        self.name = name
        self.default = default

        # preserve newlines in help text, but not leading or trailing whitespace
        self.help = '\n'.join([l.strip() for l in help.splitlines()])

        # env name defaults to all-caps with underscores
        if env_name is None:
            self.env_name = self.name.upper().replace('-', '_')
            if not self.env_name.startswith('ATOPILE'):
                self.env_name = 'ATOPILE_' + self.env_name
        else:
            self.env_name = env_name

        # set initial value and level
        env_value = os.getenv(self.env_name)
        if env_value is not None:
            self._value = env_value
            self.valve_level = Level.ENV
        elif default is not None:
            self._value = default
            self.valve_level = Level.DEFAULT
        else:
            self._value = None
            self.valve_level = Level.UNSET

        self.getter = getter

    def as_click_option(self, short_option=None):
        """
        Decorator to add this option as a click option
        """
        decals = [f'--{self.name}']
        if short_option:
            decals.append(short_option)

        def _wrapper(func):
            return click.option(*decals, help=self.help, default=None)(func)

        return _wrapper

    def as_click_arg(self, required=True):
        """
        Decorator to add this option as a click argument
        """
        def _wrapper(func):
            return click.argument(self.name, required=required, default=None)(func)
        return _wrapper

    @property
    def raw_value(self):
        return self._value

    @property
    def value(self):
        return self.get_value_with_args()

    def set_value(self, value, level):
        if level >= self.valve_level:
            self._value = value

    def get_value_with_args(self, **kwargs):
        if self.getter is not None:
            return self.getter(self.raw_value, **kwargs)
        return self.raw_value

_options: Dict[str, Option] = {}

def update_options(updates: Dict[str, Any], level: Level):
    for k, v in updates.items():
        if k in _options:
            _options[k].set_value(v, level)

def print_options():
    for option in _options.values():
        indent = 4
        print(f'{" " * indent}{option.name} (${option.env_name}):')
        print(utils.reindent_str(option.help, indent*2))
        print()

def get_relative(rel, base: Option):
    rel = Path(rel).expanduser()
    if rel.is_absolute():
        return rel
    return base.value / rel

def path_expand_user(val):
    return Path(val).expanduser()

# Define options

system_atopile_dir = Option(
    'system-atopile-dir',
    default='~/.atopile',
    help="""Location of the system atopile directory.""",
    getter=path_expand_user
)

# order of atopile-file and project-dir are a little weird, because project_dir
# is determined by the raw_value of atopile-file and the atopile-file is relative to 
# the project director. this works because one's raw and the others are computed values
# but it warrants explaining

atopile_file = Option(
    'atopile-file',
    default='.atopile.yaml',
    help="""Location of atopile file. 
        If relative, (eg. "build"), relative to project.
        If absolute, retain absoluteness.""",
)

def get_project_dir(start_dir: str) -> Path:
    start_dir = Path(start_dir).expanduser().absolute()

    for d in [start_dir] + list(start_dir.parents):
        config_file = d / atopile_file.raw_value
        if config_file.exists():
            return d

    raise FileNotFoundError(f'No file named {atopile_file.raw_value} found in {str(start_dir)} or any parent directories')

project_dir = Option(
    'project-dir',
    default='.',
    help="""Location of the project directory to target.""", 
    getter=get_project_dir
)

get_project_relative = partial(get_relative, base=project_dir)
atopile_file.getter = get_project_relative

project_atopile_dir = Option(
    'project-atopile-dir',
    default='.atopile',
    help="""Location of the project atopile directory.""",
    getter=get_project_relative
)

build_dir = Option(
    'build-dir',
    default='build',
    help="""Location of the build directory. 
        If relative, (eg. "build"), relative to project.
        If absolute, retain absoluteness.""",
    getter=get_project_relative
)

dist_dir = Option(
    'dist-dir',
    default='dist',
    help="""Location of the dist directory. 
        If relative, (eg. "dist"), relative to project.
        If absolute, retain absoluteness.""", 
    getter=get_project_relative
)

docker_options = Option(
    'docker-options',
    default='{}',
    help="""A JSON representation of docker configuration to be sent when spooling up new containers.
        See https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerList for options""",
    getter=json.loads
)

# These options are a little odd and warrant explaining. 
# Basically, docker-in-docker behaves unintatively. It's not a true VM and all actually runs on the 
# top-level docker instance on the host. Therefore any bind-mounting is relative to the host as well
# without these kinda shitty options, we're unable to bind-mount the correct locations into the stage 
# containers

def get_container_project_dir(val):
    if val == None:
        return project_dir.value
    else:
        return get_project_dir(val)

container_project_dir = Option(
    'container-project-dir',
    default=None,
    help="""Location of the project directory on a host machine 
        that will end up being bind-mounted into the stage 
        containers.""", 
    getter=get_container_project_dir
)

def get_container_build_dir(val):
    # default of None means just recycle the value of `build-dir`
    if val == None:
        val = build_dir.raw_value
    
    return get_relative(val, container_project_dir)

container_build_dir = Option(
    'container-build-dir',
    default=None,
    help="""Location of the build directory on a host machine 
        or relative to `container-project-dir` that will end 
        up being bind-mounted into the stage containers.""",
    getter=get_container_build_dir
)
