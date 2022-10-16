#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

import pytest

from restapicall.utils import Utils


@pytest.fixture
def utils():
    return Utils


@pytest.fixture
def args():
    return {'format': 'json', 'limit': '100'}


class TestUtils:
    assert isinstance(Utils, object) is True


def test_build_uri(utils, args):
    assert utils.build_uri('http://oloc.com', ['foo', 'bar'], args) == 'http://oloc.com/foo/bar?format=json&limit=100'
