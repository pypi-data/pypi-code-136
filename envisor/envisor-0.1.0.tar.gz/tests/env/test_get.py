import os
from typing import Any

import pytest

from envisor import Env


@pytest.mark.parametrize(
    ("value", "name", "type_", "nested_type", "expected_result"),
    (
        ("12345", "B27AA3AC0095AF22DE1FA909CF3C9D96F230FD", str, None, "12345"),
        ("12345", "A27AZ3DC0095BF22DE1FA106CF3C9D96F230SP", int, None, 12345),
        ("123.45", "Q27AZ3ZC0095BF22DE1FA108CD3C9D96F230SR", float, None, 123.45),
        ("1:2:3", "B37AZ3DC0095BF42DE1FA106CFDC9D96F230ZL", list, None, ["1", ":", "2", ":", "3"]),
        ("1:2:3", "T27AZ3DC0095BF22DE1FA106CF3C9D96F230ZA", list, str, ["1", "2", "3"]),
        ("1:2:3", "W21AZ3DC0095BF22DE1FA106CF3C9D96F230FE", list, int, [1, 2, 3]),
        ("1:2:3", "N37AZ3DC0095BF22DE1FA1068F3C9D96F230HE", set, str, {"1", "2", "3"}),
        ("1:2:3", "X53AZ3DC0095BF22DE1FA1068F3C9D96F230SW", set, int, {1, 2, 3}),
    )
)
def test(value: str, name: str, type_: Any, nested_type: Any, expected_result: Any) -> None:
    os.environ[name] = value
    env = Env()

    assert env.get(name, type_, nested_type) == expected_result


def test_no_value() -> None:
    env = Env()

    with pytest.raises(KeyError):
        env.get("J13AZ3DC0095BF22DEA1068XFD3C9D96A230ZE")


@pytest.mark.parametrize(
    ("name", "default", "expected_result"),
    (
        ("N37AZ3DC0095BF22DE1FA1068CFD3D96F230HE", None, None),
        ("B27AA3AC0095AF22DE1FA9069D3C9D96F230FD", "12345", "12345"),
        ("A27AZ3DC0095BF22DE1FA106FD3C9D96F230SP", 12345, 12345),
        ("D27AZ4DC0119BF22DE2ZA10CFD3C9D96F231GX", [1, 2, 3], [1, 2, 3])
    )
)
def test_default(name: str, default: Any, expected_result: Any) -> None:
    env = Env()

    assert env.get(name, default=default) == expected_result
