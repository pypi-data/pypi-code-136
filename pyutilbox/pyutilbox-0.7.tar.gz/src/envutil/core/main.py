import os

from . import constants as Const
from .config_var import ConfigVar
from .core import load_config


class Config:
	load = load_config

	class Env:

		@staticmethod
		def name() -> str:
			return Config.get(Const.ENVIRONMENT_VARIABLE_NAME, default=None)

		@staticmethod
		def is_local():
			return Config.Env.name() == 'local'

	@staticmethod
	def is_loaded() -> bool:
		return os.environ.get(Const.PYENV_LOAD_STATUS_KEY) is not None

	@staticmethod
	def get(key: str = '', default=None) -> ConfigVar:
		return ConfigVar(key=key, value=os.environ.get(key, default=default))

	@staticmethod
	def debug():
		return Config.get(Const.DEBUG_VARIABLE_NAME).as_bool(default=Const.DEBUG_VARIABLE_VALUE)
