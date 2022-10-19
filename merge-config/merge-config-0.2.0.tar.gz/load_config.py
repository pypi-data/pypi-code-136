import os
from dotenv import load_dotenv
from yaml import load as load_yaml, Loader
from typing import Dict, List, Any, TypeVar, Type
from deepmerge import always_merger
from flatten_dict import flatten, unflatten, reducers
import re
from .base_plugin import BasePlugin

load_dotenv()
T = TypeVar('T')


def load_default_file(config_dir: str) -> Dict[str, Any]:
  with open(f'{config_dir}/default.yml') as default_config_file:
    default_config = load_yaml(default_config_file, Loader=Loader)
    return default_config


def load_override_file(config_dir: str) -> Dict[str, Any]:
  override_file_path = f'{config_dir}/{os.environ.get("PYTHON_ENV")}.yml'
  if os.path.exists(override_file_path):
    with open(override_file_path) as override_file:
      return load_yaml(override_file, Loader=Loader)
  return {}


def replace_plugins(config: Dict[str, Any], plugins: List[BasePlugin]) -> Dict[str, Any]:
  replaced_config: Dict[str, Any] = {}
  value_regex = '\\$\\{(.*?):(.*?)\\}'
  for key, value in config.items():
    if value:
      matches = re.findall(value_regex, value)
      for match in matches:
        protocol = match[0]
        value_key = match[1]
        plugin: BasePlugin = next(filter(lambda plugin: plugin.protocol() == protocol, plugins), None)
        if not plugin:
          raise Exception(f'Failed to find a plugin with the protocol {protocol}')
        str_value: str = value
        value = str_value.replace('${' + protocol + ':' + value_key + '}', plugin.get_value(value_key))
      replaced_config[key] = value
  return replaced_config


def load_config(schema: Type[T], config_dir: str = f'{os.getcwd()}/config', plugins: List[BasePlugin] = []) -> T:
  env = os.environ.get('PYTHON_ENV')
  if not env:
    raise Exception('PYTHON_ENV environment variable is not defined')
  if not os.path.exists(f'{config_dir}/default.yml'):
    raise Exception(f'Failed to find the default configuration file ({config_dir}/default.yml)')
  default_config = load_default_file(config_dir)
  override_config = load_override_file(config_dir)
  merged = always_merger.merge(default_config, override_config)
  flattened = flatten(merged, reducer=reducers.make_reducer(delimiter='.'))
  replaced = replace_plugins(flattened, plugins)
  unflattened = unflatten(replaced, splitter='dot')
  config = schema(**unflattened)
  return config
