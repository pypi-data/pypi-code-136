import tempfile

import pytest
from yaml_config import open_config

from .dataset import open_config as open_config_data


@pytest.fixture
def create_config():
    temp = tempfile.NamedTemporaryFile(mode='w+', suffix='.yml')
    temp.write(open_config_data.CONFIG)
    temp.seek(0)

    yield (temp.name, )

    temp.close()


def test_file_dosenot_exist():
    """Тест проверяет случай когда файл конфига отсутствует."""
    with pytest.raises(FileNotFoundError):
        open_config('lol', 'kek')


def test_config(create_config):
    """Тест проверяет случай когда конфиг существует."""
    path = create_config[0]
    conf = open_config('random', path)
    assert conf == open_config_data.RESULT, 'Данные из конфига не совпадают с датасетом'
