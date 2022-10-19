# django-mellon - SAML2 authentication for Django
# Copyright (C) 2014-2019 Entr'ouvert
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.utils.http import urlencode

from . import app_settings, utils

PASSIVE_TRIED_COOKIE = 'MELLON_PASSIVE_TRIED'


class PassiveAuthenticationMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # When unlogged remove the PASSIVE_TRIED cookie
        if (
            app_settings.OPENED_SESSION_COOKIE_NAME
            and PASSIVE_TRIED_COOKIE in request.COOKIES
            and (
                app_settings.OPENED_SESSION_COOKIE_NAME not in request.COOKIES
                or (hasattr(request, 'user') and request.user.is_authenticated)
            )
        ):
            response.delete_cookie(PASSIVE_TRIED_COOKIE)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # skip if explicitely asked in the query string
        if 'no-passive-auth' in request.GET:
            return
        # Skip AJAX requests
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return
        # Skip AJAX and media/script requests, unless mellon_no_passive is False on the view
        if getattr(view_func, 'mellon_no_passive', True) and 'text/html' not in request.headers.get(
            'Accept', ''
        ):
            return
        # Skip views asking to be skiped
        if getattr(view_func, 'mellon_no_passive', False):
            return
        # Skip mellon views
        if request.resolver_match.url_name and request.resolver_match.url_name.startswith('mellon_'):
            return
        if not any(utils.get_idps()):
            return
        if not app_settings.OPENED_SESSION_COOKIE_NAME:
            return
        if hasattr(request, 'user') and request.user.is_authenticated:
            old_opened_session_cookie = request.session.get('mellon_opened_session_cookie')
            if old_opened_session_cookie and old_opened_session_cookie != request.COOKIES.get(
                app_settings.OPENED_SESSION_COOKIE_NAME
            ):
                # close current session if the opened session cookie changed...
                auth.logout(request)
                # and continue with unlogged behaviour
            else:
                # otherwise, if current session is still active, do nothing
                return
        if app_settings.OPENED_SESSION_COOKIE_NAME not in request.COOKIES:
            return
        opened_session_cookie = request.COOKIES[app_settings.OPENED_SESSION_COOKIE_NAME]
        if request.COOKIES.get(PASSIVE_TRIED_COOKIE) == opened_session_cookie:
            return
        # all is good, try passive login
        params = {
            'next': request.build_absolute_uri(),
            'passive': '',
        }
        url = reverse('mellon_login') + '?%s' % urlencode(params)
        response = HttpResponseRedirect(url)
        # prevent loops
        response.set_cookie(PASSIVE_TRIED_COOKIE, value=opened_session_cookie, max_age=None)
        return response
