from ..base_plugin import BasePlugin
import os


class EnvPlugin(BasePlugin):

  def protocol(self) -> str:
    return 'env'

  def get_value(self, key: str):
    if key not in os.environ:
      raise Exception(f'Environment variable {key} is not defined')
    return os.environ[key]