# SPDX-License-Identifier: CC0-1.0

# Copyright (C) 2022 Wojtek Kosior <koszko@koszko.org>
#
# Available under the terms of Creative Commons Zero v1.0 Universal.

import typing as t

import flask

from .. import state as st


class WebUIApp(flask.Flask):
    _haketilo_state: st.HaketiloState

def get_haketilo_state() -> st.HaketiloState:
    return t.cast(WebUIApp, flask.current_app)._haketilo_state
