#!/usr/bin/env python

"""Tests for `razator_utils` package."""
from pathlib import Path

import pytest

from razator_utils import batchify, camel_to_snake, log, flatten_dict


def test_camel_to_snake():
    """Test the camel_to_snake function which converts camelCase to snake_case"""
    assert camel_to_snake('thisIsTest') == 'this_is_test'
    assert camel_to_snake('anotherATest') == 'another_a_test'


def test_batchify():
    iterable = ['a', 'b', 'c', 'd', 'e']
    assert [x for x in batchify(iterable, 2)] == [['a', 'b'], ['c', 'd'], ['e']]


def test_stout_log():
    logger = log.get_stout_logger('pytest.py', 'INFO')
    assert logger.level == 20
    log_file = Path('test.log')
    file_logger = log.get_file_logger('pytest_file_log.py', log_file, 'WARNING')
    file_logger.warning('This is a warning')
    assert log_file.exists()
    log_file.unlink()


@pytest.mark.parametrize('test_data,expected', [
    ({}, {}),
    ({'not_nested': 'dictionary'}, {'not_nested': 'dictionary'}),
    ({'single': {'nested': 'dict'}}, {'single_nested': 'dict'}),
    (
        {'single': {'nested': 'dict'}, 'multiple': {'key1': 'val1', 'key2': 'val2'}},
        {'single_nested': 'dict', 'multiple_key1': 'val1', 'multiple_key2': 'val2'}
     ),
    (
        {'single': {'nested': 'dict'}, 'multiple': {'dict1': {'key1': 'val1'}, 'key2': 'val2'}},
        {'single_nested': 'dict', 'multiple_dict1_key1': 'val1', 'multiple_key2': 'val2'}
    ),
    (
        {'triple': {'nested': {'dictionary': 'val'}}},
        {'triple_nested_dictionary': 'val'}
    ),
    (({'single': {'nested': 'dict'}}, '', '.'), {'single.nested': 'dict'}),
    (({'single': {'nested': 'dict'}}, 'flat', '.'), {'flat.single.nested': 'dict'}),
])
def test_flatten_dict(test_data, expected):
    if isinstance(test_data, tuple):
        pass
    else:
        assert flatten_dict(test_data) == expected
