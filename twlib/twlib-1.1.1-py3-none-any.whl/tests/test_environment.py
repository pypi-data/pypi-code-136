from twlib.environment import Os, config


def test_os():
    assert config.os == 2
    assert config.os == Os.MAC
