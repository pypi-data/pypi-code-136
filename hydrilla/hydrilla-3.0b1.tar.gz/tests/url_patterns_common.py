# SPDX-License-Identifier: CC0-1.0

# Copyright (C) 2022 Wojtek Kosior <koszko@koszko.org>
#
# Available under the terms of Creative Commons Zero v1.0 Universal.

import pytest

from hydrilla import url_patterns

sample_url_str = 'http://example.com/aa/bb'

@pytest.fixture(scope='session')
def sample_url_parsed():
    """Generate a simple ParsedUrl object."""
    return url_patterns.ParsedUrl(
        orig_url           = sample_url_str,
        scheme             = 'http',
        domain_labels      = ('com', 'example'),
        path_segments      = ('aa', 'bb'),
        query              = '',
        has_trailing_slash = False,
        port               = 80
    )
