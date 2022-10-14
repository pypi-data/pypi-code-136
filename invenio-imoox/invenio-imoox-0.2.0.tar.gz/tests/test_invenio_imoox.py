# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Graz University of Technology.
#
# invenio-imoox is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from invenio_imoox import InvenioIMooX, __version__


def test_version():
    """Test version import."""
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioIMooX(app)
    assert "invenio-imoox" in app.extensions

    app = Flask("testapp")
    ext = InvenioIMooX()
    assert "invenio-imoox" not in app.extensions

    ext.init_app(app)
    assert "invenio-imoox" in app.extensions
