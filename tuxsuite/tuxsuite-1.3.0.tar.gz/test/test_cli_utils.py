# -*- coding: utf-8 -*-

import pytest
from tuxsuite.cli.utils import file_or_url


def test_file_or_url():
    url = "http://www.example.com/"
    result = file_or_url(url)
    assert result == url

    with pytest.raises(SystemExit):
        file_or_url("/temp/unknown")
