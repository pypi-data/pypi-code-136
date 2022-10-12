# SPDX-License-Identifier: CC0-1.0

# Copyright (C) 2022 Wojtek Kosior <koszko@koszko.org>
#
# Available under the terms of Creative Commons Zero v1.0 Universal.

import sys
from pathlib import Path

import pytest
import pkgutil
from tempfile import TemporaryDirectory
from typing import Iterable

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here / 'src'))

from hydrilla import translations as hydrilla_translations

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr('requests.sessions.Session.request')

@pytest.fixture
def mock_subprocess_run(monkeypatch, request):
    """
    Temporarily replace subprocess.run() with a function supplied through pytest
    marker 'subprocess_run'.

    The marker excepts 2 arguments:
    * the module inside which the subprocess attribute should be mocked and
    * a run() function to use.
    """
    where, mocked_run = request.node.get_closest_marker('subprocess_run').args

    class MockedSubprocess:
        """Minimal mocked version of the subprocess module."""
        run = mocked_run

    monkeypatch.setattr(where, 'subprocess', MockedSubprocess)

@pytest.fixture(autouse=True)
def no_gettext(monkeypatch, request):
    """
    Make gettext return all strings untranslated unless we request otherwise.
    """
    if request.node.get_closest_marker('enable_gettext'):
        return

    class MockedTraslations:
        """Replacement for gettext.GNUTranslations."""
        def __init__(self, dummy_locale):
            """Initialize this MockedTranslations."""
            pass
        def gettext(self, msg):
            """Return translated string unmodified."""
            return msg

    monkeypatch.setattr(hydrilla_translations, 'translation', MockedTraslations)

@pytest.fixture
def tmpdir() -> Iterable[Path]:
    """
    Provide test case with a temporary directory that will be automatically
    deleted after the test.
    """
    with TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)
