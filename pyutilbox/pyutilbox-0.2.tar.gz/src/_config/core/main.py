import logging
import os
from pathlib import Path

from . import constants as Const
from .config_var import ConfigVar
from .exceptions import PyenvException


def __get_environment_file(config_path: str, file_name: str, config_type: str):
	if not os.path.isdir(config_path):
		raise PyenvException.BaseDirDoesNotExists(config_path)

	config_file_list = list(Path(config_path).glob(f"*{config_type}"))
	local_config_file = Path(config_path).joinpath(f"{Const.LOCAL_CONFIG_FILE_PREFIX}{config_type}")
	main_config_file = Path(config_path).joinpath(f"{file_name}{config_type}")

	if local_config_file in config_file_list or main_config_file in config_file_list:
		if local_config_file in config_file_list:
			return local_config_file.__str__()
		else:
			return main_config_file.__str__()
	else:
		raise PyenvException.ConfigFileDoesNotExist(config_path)


def __load_configuration_file(config_file: str, config_type: str):
	if config_type == Const.DOT_ENV_FILE:
		from dotenv import load_dotenv
		return load_dotenv(config_file, verbose=True)


def load(env_path: str = '', file_name: str = '', file_type: str = Const.DOT_ENV_FILE):
	try:
		config_file = __get_environment_file(config_path=env_path, file_name=file_name, config_type=file_type)
		load_config = __load_configuration_file(config_file=config_file, config_type=file_type)
		if load_config:
			os.environ[Const.PYENV_LOAD_STATUS_KEY] = '1'
		else:
			raise PyenvException.ConfigurationLoadingFailed(config_file)
	except Exception as e:
		logging.error(e)
		exit()


def is_loaded() -> bool:
	return os.environ.get(Const.PYENV_LOAD_STATUS_KEY) is not None


def get(key: str = '', default=None) -> ConfigVar:
	return ConfigVar(key=key, value=os.environ.get(key, default=default))


def environment() -> str:
	return get(Const.ENVIRONMENT_VARIABLE_NAME, default=None)


def debug():
	return get(Const.DEBUG_VARIABLE_NAME).as_bool(default=Const.DEBUG_VARIABLE_VALUE)
