# SPDX-License-Identifier: GPL-3.0-or-later

# Handling of gettext for Hydrilla.
#
# This file is part of Hydrilla
#
# Copyright (C) 2021, 2022 Wojtek Kosior
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
# I, Wojtek Kosior, thereby promise not to sue for violation of this
# file's license. Although I request that you do not make use of this
# code in a proprietary program, I am not going to enforce this in
# court.

import locale as lcl
import gettext
import typing as t

from pathlib import Path

here = Path(__file__).resolve().parent

localedir = here / 'locales'

supported_locales = [f.name for f in localedir.iterdir() if f.is_dir()]

default_locale = 'en_US'

def select_best_locale() -> str:
    """
    ....

    Otherwise, try to determine system's default language and use that.
    """
    # TODO: Stop referenceing flask here. Instead, allow other code to register
    #       custom locale resolvers and register flask-aware resolver during
    #       runtime from within the flask-related part(s) of the application.
    try:
        import flask
        use_flask = flask.has_request_context()
    except ModuleNotFoundError:
        use_flask = False

    if use_flask:
        best = flask.request.accept_languages.best_match(
            supported_locales,
            default=default_locale
        )
        assert best is not None
        return best

    # https://stackoverflow.com/questions/3425294/how-to-detect-the-os-default-language-in-python
    # I am not going to surrender to Microbugs' nonfree, crappy OS to test it,
    # so the lines inside try: block may actually fail.
    locale: t.Optional[str] = lcl.getdefaultlocale()[0]
    try:
        from ctypes.windll import kernel32 as windll # type: ignore
        locale = lcl.windows_locale[windll.GetUserDefaultUILanguage()]
    except:
        pass

    return locale if locale in supported_locales else default_locale

translations: t.Dict[str, gettext.NullTranslations] = {}

def translation(locale: t.Optional[str] = None) -> gettext.NullTranslations:
    """
    Configure translations for domain 'messages' and return the object that
    represents them. If the requested locale is not available, fall back to
    'en_US'.
    """
    if locale is None:
        locale = select_best_locale()

    if not (localedir / locale).is_dir():
        locale = 'en_US'

    if locale not in translations:
        translations[locale] = gettext.translation(
            'messages',
            localedir=localedir,
            languages=[locale]
        )

    return translations[locale]

def smart_gettext(msg: str, locale: t.Optional[str] = None) -> str:
    """...."""
    return translation(locale).gettext(msg)

_ = smart_gettext
