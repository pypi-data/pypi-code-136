from dataclasses import dataclass
from .helpers import mocked_env_variables, mocked_config_file, mocked_dotenv_file
from config import Config


@dataclass
class DummyConfig:
    field1: str
    field2: int


@dataclass
class DummyConfigWithDefault:
    field1: str
    field2: int = 0


def test_config_from_dotenv_file():
    env_vars = {
        "FIELD1": "value1",
        "FIELD2": "2"
    }

    with mocked_env_variables(env_vars):
        conf = Config().add_env_variables("").resolve(DummyConfig)

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_env_vars_with_section():
    env_vars = {
        "SEC__FIELD1": "value1",
        "SEC__FIELD2": "2"
    }

    with mocked_env_variables(env_vars):
        conf = Config().add_env_variables("").resolve(DummyConfig, "sec")

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_env_vars_with_nested_section():
    env_vars = {
        "SEC1__SEC2__FIELD1": "value1",
        "SEC1__SEC2__FIELD2": "2"
    }

    with mocked_env_variables(env_vars):
        conf = Config().add_env_variables("").resolve(DummyConfig, "sec1:sec2")

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_env_vars_with_multiple_sections():
    env_vars = {
        "SEC1__FIELD1": "value1",
        "SEC1__FIELD2": "2",
        "SEC2__FIELD1": "value3",
        "SEC2__FIELD2": "4"
    }

    with mocked_env_variables(env_vars):
        conf1 = Config().add_env_variables("").resolve(DummyConfig, "sec1")
        conf2 = Config().add_env_variables("").resolve(DummyConfig, "sec2")

    assert conf1.field1 == "value1"
    assert conf1.field2 == 2
    assert conf2.field1 == "value3"
    assert conf2.field2 == 4


def test_config_from_env_vars_with_prefix():
    env_vars = {
        "PRF_SEC__FIELD1": "value1",
        "PRF_SEC__FIELD2": "2"
    }

    with mocked_env_variables(env_vars):
        conf = Config().add_env_variables("PRF_").resolve(DummyConfig, "sec")

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_file():
    conf_file = {
        "FIELD1": "value1",
        "FIELD2": "2"
    }

    with mocked_config_file(conf_file) as path:
        conf = Config().add_file(path).resolve(DummyConfig)

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_file_with_section():
    conf_file = {
        "sec": {
            "FIELD1": "value1",
            "FIELD2": "2"
        }
    }

    with mocked_config_file(conf_file) as path:
        conf = Config().add_file(path).resolve(DummyConfig, "sec")

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_file_with_nested_section():
    conf_file = {
        "sec1": {
            "sec2": {
                "FIELD1": "value1",
                "FIELD2": "2"
            }
        }
    }

    with mocked_config_file(conf_file) as path:
        conf = Config().add_file(path).resolve(DummyConfig, "sec1:sec2")

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_file_with_multiple_section():
    conf_file = {
        "sec1": {
            "FIELD1": "value1",
            "FIELD2": "2"
        },
        "sec2": {
            "FIELD1": "value3",
            "FIELD2": 4
        },
    }

    with mocked_config_file(conf_file) as path:
        conf1 = Config().add_file(path).resolve(DummyConfig, "sec1")
        conf2 = Config().add_file(path).resolve(DummyConfig, "sec2")

    assert conf1.field1 == "value1"
    assert conf1.field2 == 2
    assert conf2.field1 == "value3"
    assert conf2.field2 == 4


def test_config_from_dict():
    conf_dict = {
        "FIELD1": "value1",
        "FIELD2": "2"
    }

    conf = Config().add_dict(conf_dict).resolve(DummyConfig)

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_dict_with_section():
    conf_dict = {
        "sec": {
            "FIELD1": "value1",
            "FIELD2": "2"
        }
    }

    conf = Config().add_dict(conf_dict).resolve(DummyConfig, "sec")

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_dict_with_section():
    conf_dict = {
        "sec1": {
            "sec2": {
                "FIELD1": "value1",
                "FIELD2": "2"
            }
        }
    }

    conf = Config().add_dict(conf_dict).resolve(DummyConfig, "sec1:sec2")

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_dict_with_multiple_sections():
    conf_dict = {
        "sec1": {
            "FIELD1": "value1",
            "FIELD2": "2"
        },
        "sec2": {
            "FIELD1": "value3",
            "FIELD2": 4
        },
    }

    conf1 = Config().add_dict(conf_dict).resolve(DummyConfig, "sec1")
    conf2 = Config().add_dict(conf_dict).resolve(DummyConfig, "sec2")

    assert conf1.field1 == "value1"
    assert conf1.field2 == 2
    assert conf2.field1 == "value3"
    assert conf2.field2 == 4


def test_config_field_without_value_is_none():
    conf_dict = {
        "FIELD1": "value1",
    }

    conf = Config().add_dict(conf_dict).resolve(DummyConfig)

    assert conf.field1 == "value1"
    assert conf.field2 == None


def test_config_retains_default_value_if_not_overriden():
    conf_dict = {
        "FIELD1": "value1",
    }

    conf = Config().add_dict(conf_dict).resolve(DummyConfigWithDefault)

    assert conf.field1 == "value1"
    assert conf.field2 == 0


def test_config_default_value_can_be_overriden():
    conf_dict = {
        "FIELD1": "value1",
        "FIELD2": "2",
    }

    conf = Config().add_dict(conf_dict).resolve(DummyConfigWithDefault)

    assert conf.field1 == "value1"
    assert conf.field2 == 2

def test_config_from_dotenv_file():
    env_vars = {
        "FIELD1": "value1",
        "FIELD2": "2"
    }

    with mocked_dotenv_file(env_vars) as dotenv_file:
        conf = Config().add_dotenv(dotenv_file).resolve(DummyConfig)

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_dotenv_file_with_section():
    env_vars = {
        "SEC__FIELD1": "value1",
        "SEC__FIELD2": "2"
    }

    with mocked_dotenv_file(env_vars) as dotenv_file:
        conf = Config().add_dotenv(dotenv_file).resolve(DummyConfig, "sec")

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_dotenv_file_with_nested_section():
    env_vars = {
        "SEC1__SEC2__FIELD1": "value1",
        "SEC1__SEC2__FIELD2": "2"
    }

    with mocked_dotenv_file(env_vars) as dotenv_file:
        conf = Config().add_dotenv(dotenv_file).resolve(DummyConfig, "sec1:sec2")

    assert conf.field1 == "value1"
    assert conf.field2 == 2


def test_config_from_dotenv_file_with_multiple_sections():
    env_vars = {
        "SEC1__FIELD1": "value1",
        "SEC1__FIELD2": "2",
        "SEC2__FIELD1": "value3",
        "SEC2__FIELD2": "4"
    }

    with mocked_dotenv_file(env_vars) as dotenv_file:
        conf1 = Config().add_dotenv(dotenv_file).resolve(DummyConfig, "sec1")
        conf2 = Config().add_dotenv(dotenv_file).resolve(DummyConfig, "sec2")

    assert conf1.field1 == "value1"
    assert conf1.field2 == 2
    assert conf2.field1 == "value3"
    assert conf2.field2 == 4
