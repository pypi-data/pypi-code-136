# SPDX-License-Identifier: CC0-1.0

# Copyright (C) 2022 Wojtek Kosior <koszko@koszko.org>
#
# Available under the terms of Creative Commons Zero v1.0 Universal.

import pytest
import re
import dataclasses as dc

from immutables import Map

from hydrilla import url_patterns
from hydrilla.exceptions import HaketiloException

from .url_patterns_common import *

@pytest.mark.parametrize('_in, out', [
    ({},                           sample_url_str),
    ({'path_segments': ()},        'http://example.com'),
    ({'has_trailing_slash': True}, 'http://example.com/aa/bb/'),
    ({'scheme': 'http_sth'},       'http_sth://example.com:80/aa/bb'),
    ({'port': 443},                'http://example.com:443/aa/bb'),

    ({'path_segments': (),
      'has_trailing_slash': True},
     'http://example.com/'),

    ({'scheme': 'https',
      'port': 443},
     'https://example.com/aa/bb'),

    ({'scheme': 'ftp',
      'port': 21},
     'ftp://example.com/aa/bb'),

    ({'scheme': 'file',
      'port': None,
      'domain_labels': ()},
     'file:///aa/bb')
])
def test_reconstruct_parsed_url(_in, out, sample_url_parsed):
    """Test the reconstruct_url() method of ParsedUrl class."""
    parsed_url = dc.replace(sample_url_parsed, **_in)
    assert parsed_url.reconstruct_url() == out

@pytest.mark.parametrize('_in, out', [
    ({'url': sample_url_str},                    {}),
    ({'url': 'http://example.com:80/aa/bb'},     {}),
    ({'url': 'http://example.com//aa///bb'},     {}),
    ({'url': 'http://example...com/aa/bb'},      {}),
    ({'url': 'http://example.com/aa/bb?c=d#ef'}, {}),
    ({'url': 'http://example.com'},              {'path_segments': ()}),
    ({'url': 'http://example.com/aa/bb/'},       {'has_trailing_slash': True}),
    ({'url': 'http://example.com:443/aa/bb'},    {'port': 443}),

    ({'url': 'http://example.com/'},
     {'path_segments': (),
      'has_trailing_slash': True}),

    ({'url': 'http://example.com/aa/bb',
      'is_pattern': True,
      'orig_url': 'http*://example.com/aa/bb/'},
     {}),

    ({'url': 'https://example.com/aa/bb'},
     {'scheme': 'https',
      'port': 443}),

    ({'url': 'ftp://example.com/aa/bb'},
     {'scheme': 'ftp',
      'port': 21}),

    ({'url': 'file:///aa/bb'},
     {'scheme': 'file',
      'port': None,
      'domain_labels': ()})
])
def test_parse_pattern_or_url(_in, out, sample_url_parsed):
    """Test normal use (no errors) of the _parse_pattern_or_url() function."""
    if 'orig_url' not in _in:
        _in = {**_in, 'orig_url': _in['url']}

    out = {**out, 'orig_url': _in['orig_url']}

    parsed_url = url_patterns._parse_pattern_or_url(**_in)
    assert parsed_url == dc.replace(sample_url_parsed, **out)

@pytest.mark.parametrize('_in, err', [
    ({'url': 'file://:78/unexpected/port'},  'err.url_{}.bad'),
    ({'url': 'file://unexpected.hostname/'}, 'err.url_{}.bad'),
    ({'url': 'http:///no/hostname'},         'err.url_{}.bad'),
    ({'url': 'invalid?://example.com'},      'err.url_{}.bad'),
    ({'url': 'invalid?://example.com',
      'orig_url': 'invalid?://example.com',
      'is_pattern': True},
     'err.url_pattern_{}.bad'),

    ({'url': 'unknown://example.com'}, 'err.url_{}.bad_scheme'),
    ({'url': 'unknown://example.com',
      'orig_url': 'unknown://example.com',
      'is_pattern': True},
     'err.url_pattern_{}.bad_scheme'),

    ({'url': 'http://example.com:80',
      'orig_url': 'http*://example.com:80',
      'is_pattern': True},
     'err.url_pattern_{}.special_scheme_port'),

    ({'url': 'http://example.com:65536'}, 'err.url_{}.bad_port'),
    ({'url': 'http://example.com:0'},     'err.url_{}.bad_port'),
    ({'url': 'http://example.com:65537',
      'orig_url': 'http://example.com:65537',
      'is_pattern': True},
     'err.url_pattern_{}.bad_port'),

    ({'url': 'http://example.com/?a=b',
      'orig_url': 'http://example.com/?a=b',
      'is_pattern': True},
     'err.url_pattern_{}.has_query'),

    ({'url': 'http://example.com/#abc',
      'orig_url': 'http://example.com/#abc',
      'is_pattern': True},
     'err.url_pattern_{}.has_frag')
])
def test_parse_pattern_or_url_err(_in, err, sample_url_parsed):
    """Test error conditions of the _parse_pattern_or_url() function."""
    if 'orig_url' not in _in:
        _in = {**_in, 'orig_url': _in['url']}

    err_url = _in['orig_url']
    err_regex = err.format(re.escape(err_url))

    with pytest.raises(HaketiloException, match=f'^{err_regex}$'):
        url_patterns._parse_pattern_or_url(**_in)

def test_parse_pattern_or_url_different_urls():
    """
    Verify the _parse_pattern_or_url() function allows passed URLs to be
    different only when parsing a pattern.
    """
    urls = [sample_url_str, sample_url_str.replace('http', 'http*')]

    url_patterns._parse_pattern_or_url(*urls, is_pattern=True)

    with pytest.raises(AssertionError):
        url_patterns._parse_pattern_or_url(*urls)

@pytest.mark.parametrize('_in, out', [
    ('http://example.com',  ('mocked_pr_http://example.com',)),
    ('ftp://example.com',   ('mocked_pr_ftp://example.com',)),
    ('http*://example.com', ('mocked_pr_http://example.com',
                             'mocked_pr_https://example.com'))
])
def test_parse_pattern(monkeypatch, _in, out):
    """...."""
    def mocked_parse_pattern_or_url(url, orig_url, is_pattern=False):
        """...."""
        assert is_pattern
        assert orig_url == _in

        return f'mocked_pr_{url}'

    monkeypatch.setattr(url_patterns, '_parse_pattern_or_url',
                        mocked_parse_pattern_or_url)

    assert tuple(url_patterns.parse_pattern(_in)) == out

def test_parse_url(monkeypatch):
    """...."""
    def mocked_parse_pattern_or_url(url, orig_url):
        """...."""
        return f'mocked_pr_{url}'

    monkeypatch.setattr(url_patterns, '_parse_pattern_or_url',
                        mocked_parse_pattern_or_url)

    assert url_patterns.parse_url('https://example.com') == \
        'mocked_pr_https://example.com'

def test_parsed_url_hash(sample_url_parsed):
    """...."""
    hash(sample_url_parsed)
