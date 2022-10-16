import enum
from datetime import date, datetime
from typing import List, Set

import pendulum

from chalk.features import feature, features
from chalk.features.feature import unwrap_feature
from chalk.serialization.codec import FeatureCodec


class CustomClass:
    def __init__(self, w: str):
        self.w = w

    def __eq__(self, other):
        return isinstance(other, CustomClass) and self.w == other.w


class Color(enum.Enum):
    blue = "blue"
    green = "green"
    orange = "orange"


@features
class Hello:
    a: str
    b: int
    c: datetime
    d: Color
    e: date
    y: Set[int]
    z: List[str]
    fancy: CustomClass = feature(encoder=lambda x: x.w, decoder=lambda x: CustomClass(x))


def _check_roundtrip(f, value):
    codec = FeatureCodec()
    f = unwrap_feature(f)
    encoded = codec.encode(f, value)
    decoded = codec.decode(f, encoded)
    assert decoded == value


def test_datetime():
    codec = FeatureCodec()
    serialized = "2022-04-08T22:26:03.303000+00:00"
    decoded = codec.decode(unwrap_feature(Hello.c), serialized)
    assert decoded == pendulum.parse(serialized)
    re_encoded = codec.encode(unwrap_feature(Hello.c), decoded)
    assert serialized == re_encoded


def test_custom_codecs():
    _check_roundtrip(Hello.fancy, CustomClass("hihi"))


def test_color():
    _check_roundtrip(Hello.d, Color.green)


def test_date():
    codec = FeatureCodec()
    assert "2022-04-08" == codec.encode(unwrap_feature(Hello.e), date.fromisoformat("2022-04-08"))
    _check_roundtrip(Hello.e, date.fromisoformat("2022-04-08"))


def test_list():
    _check_roundtrip(Hello.z, ["hello", "there"])
