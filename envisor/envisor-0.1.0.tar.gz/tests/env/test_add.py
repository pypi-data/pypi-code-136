import pytest

from envisor import Env


@pytest.mark.parametrize(
    ("sub_name", "expected_result"),
    (
        ("FOO", "FOO"),
        ("BAR", "BAR"),
        ("BAZ", "BAZ")
    )
)
def test_without_name(sub_name, expected_result) -> None:
    env = Env()
    foo_env = env + sub_name

    assert foo_env.name == expected_result


@pytest.mark.parametrize(
    ("naming_separator", "expected_result"),
    (
        ("_", "FOO_BAR"),
        ("", "FOOBAR")
    )
)
def test_with_name(naming_separator: str, expected_result: str) -> None:
    foo_env = Env("FOO", naming_separator=naming_separator)
    foo_bar_env = foo_env + "BAR"

    assert foo_bar_env.name == expected_result


def test_not_string() -> None:
    env = Env()

    with pytest.raises(TypeError):
        env + object()
