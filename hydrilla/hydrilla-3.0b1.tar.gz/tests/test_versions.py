# SPDX-License-Identifier: CC0-1.0

# Copyright (C) 2022 Wojtek Kosior <koszko@koszko.org>
#
# Available under the terms of Creative Commons Zero v1.0 Universal.

import pytest

from hydrilla import versions

sample_version_tuples  = [(4, 5, 3), (1, 0, 5), (3,)]
sample_version_strings = ['4.5.3',   '1.0.5',   '3']

sample_versions = [*zip(sample_version_tuples, sample_version_strings)]

@pytest.mark.parametrize('version_tuple', sample_version_tuples)
def test_normalize(version_tuple):
    """Verify that normalize() produces proper results."""
    assert versions.normalize([*version_tuple])    == version_tuple
    assert versions.normalize([*version_tuple, 0]) == version_tuple

@pytest.mark.parametrize('version_tuple, string', sample_versions)
def test_parse(version_tuple, string):
    """Verify that parse() produces proper results."""
    assert versions.parse(string)
    assert versions.parse(string + '.0') == tuple([*version_tuple, 0])

def test_parse_version_bad_string():
    """Verify that parse() raises when passed an invalid string."""
    with pytest.raises(ValueError):
        versions.parse('i am not a valid version')

@pytest.mark.parametrize('version_tuple, string', sample_versions)
def test_version_string(version_tuple, string):
    """Verify that version_string() produces proper results."""
    for _version_tuple, _string in [
            (version_tuple,              string),
            (tuple([*version_tuple, 0]), f'{string}.0')
    ]:
        assert versions.version_string(_version_tuple)    == _string
        assert versions.version_string(_version_tuple, 5) == f'{_string}-5'
