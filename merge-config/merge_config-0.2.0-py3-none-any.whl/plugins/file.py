from ..base_plugin import BasePlugin
import os


class FilePlugin(BasePlugin):

  def protocol(self) -> str:
    return 'file'

  def get_value(self, key: str):
    file = os.path.abspath(key)
    if not os.path.exists(file) or not os.path.isfile(file):
      raise Exception(f'File ${file} does not exist')
    with open(file, 'r') as contents:
      return contents.read()