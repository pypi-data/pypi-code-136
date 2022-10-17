import logging, os

from . import constants as Const


class EnvUtils:

	@staticmethod
	def read_file(file: str = None):
		with open(file, 'r+') as _file:
			return _file.read()

	@staticmethod
	def write_to_file(file: str = None, data: str = ''):
		with open(file, 'w+') as _file:
			_file.write(data)

	@staticmethod
	def build_main_config_file(main_config_file: str = '', local_config_file: str = ''):
		try:
			import re
			EnvUtils.write_to_file(
				main_config_file,
				re.compile(Const.REGEX_CONFIG_VARIABLE_SELECT_PATTERN).sub(
					repl=Const.REGEX_CONFIG_VARIABLE_REPLACEMENT_PATTERN,
					string=EnvUtils.read_file(local_config_file)
				)
			)
		except Exception as e:
			logging.exception(e)

	@staticmethod
	def make_dir(directory: str, mode=0o777):
		try:
			if not os.path.isdir(directory):
				os.mkdir(directory, mode=mode)
		except Exception as e:
			logging.error(f"Exception occurred while creating directory[{directory}] :\n {e}")
