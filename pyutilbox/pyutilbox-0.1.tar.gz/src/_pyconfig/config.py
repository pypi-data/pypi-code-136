from os import environ

from .config_var import ConfigVar
from . import constants as Const


class Config:

	@staticmethod
	def is_loaded() -> bool:
		return environ.get(Const.PYENV_LOAD_STATUS_KEY) is not None

	@staticmethod
	def get(key: str = '', default=None) -> ConfigVar:
		return ConfigVar(key=key, value=environ.get(key, default=default))

	@staticmethod
	def environment() -> str:
		return Config.get(Const.ENVIRONMENT_VARIABLE_NAME, default=None)

	@staticmethod
	def debug():
		return Config.get(Const.DEBUG_VARIABLE_NAME).as_bool(default=Const.DEBUG_VARIABLE_VALUE)

IS_CONFIG_LOADED = Config.is_loaded()
