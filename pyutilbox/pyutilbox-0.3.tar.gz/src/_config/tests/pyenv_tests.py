import unittest
from pathlib import Path

from src._config import load_config, constants as Const, Config


class PyenvTest(unittest.TestCase):
	BASE_DIR = Path(__file__).parent.resolve().joinpath('sample_data').__str__()

	def setUp(self) -> None:
		load_config(env_path=self.BASE_DIR, file_type=Const.DOT_ENV_FILE)

	def test_load_env(self):
		self.assertTrue(Config.is_loaded())

	def test_get_config(self):
		self.assertEqual(Config.get(Const.PYENV_LOAD_STATUS_KEY).as_str(), '1')
		self.assertEqual(Config.get(Const.PYENV_LOAD_STATUS_KEY).as_int(), 1)
		self.assertEqual(Config.get(Const.PYENV_LOAD_STATUS_KEY).as_bool(), True)
		self.assertEqual(Config.get(Const.PYENV_LOAD_STATUS_KEY).as_float(), 1.0)
