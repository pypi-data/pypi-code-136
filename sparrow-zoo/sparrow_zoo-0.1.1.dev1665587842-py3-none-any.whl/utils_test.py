from pathlib import Path

from .utils import get_slug


def test_get_slug_from_absolute_path():
    slug = get_slug(Path("/test/full/path/some_amazing_file.png"))
    assert slug == "some_amazing_file"


def test_get_slug_from_relative_path():
    slug = get_slug(Path("foobar.png"))
    assert slug == "foobar"


def test_get_slug_from_string_path():
    slug = get_slug("./anywhere/helloworld.json")
    assert slug == "helloworld"
