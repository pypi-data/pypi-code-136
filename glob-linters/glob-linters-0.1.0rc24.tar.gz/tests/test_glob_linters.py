#!/usr/bin/env python

"""Tests for `glob_linters` package."""

import pytest  # pylint: disable=import-error

# from glob_linters import glob_linters


@pytest.fixture
def response() -> None:
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response) -> None:  # type: ignore
    # pylint: disable=redefined-outer-name
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
