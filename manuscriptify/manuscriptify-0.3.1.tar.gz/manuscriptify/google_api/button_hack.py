# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging, webbrowser, shutil
import wsgiref.simple_server
from string import Template
from pathlib import Path
from distutils.dir_util import copy_tree

from google_auth_oauthlib.flow import InstalledAppFlow
from google_auth_oauthlib.flow import _WSGIRequestHandler
from google_auth_oauthlib.flow import _RedirectWSGIApp


class ButtonFlow(InstalledAppFlow):

    _SUCCESS_MESSAGE = (
        "The authentication flow has completed. You may close this window."
    )

    def run_local_server(
        self,
        host="localhost",
        port=8080,
        success_message=_SUCCESS_MESSAGE,
        open_browser=True,
        redirect_uri_trailing_slash=True,
        **kwargs
    ):
        """override the run_local_server method of InstalledAppFlow"""
        wsgi_app = _RedirectWSGIApp(success_message)
        wsgiref.simple_server.WSGIServer.allow_reuse_address = False
        local_server = wsgiref.simple_server.make_server(
            host, port, wsgi_app, handler_class=_WSGIRequestHandler
        )
        redirect_uri_format = (
            "http://{}:{}/" if redirect_uri_trailing_slash else "http://{}:{}"
        )
        self.redirect_uri = redirect_uri_format.format(host, local_server.server_port)
        auth_url, _ = self.authorization_url(**kwargs)

        # The following line was not written by Google
        button_page = self.make_button_page(auth_url)

        if open_browser:
            webbrowser.open(button_page, new=1, autoraise=True)
        local_server.handle_request()
        authorization_response = wsgi_app.last_request_uri.replace("http", "https")
        self.fetch_token(authorization_response=authorization_response)
        local_server.server_close()

        # The following line was not written by Google
        self.tidy_up()

        return self.credentials

    @staticmethod
    def make_button_page(auth_url):
        """make a page with a button that links to the auth url"""
        path = Path(__file__).resolve().parent
        src = path / 'launch_button'
        dest = Path().resolve() / 'launch_button'
        copy_tree(str(src), str(dest))
        params = {'AUTH_URL': auth_url}
        index = dest / 'index.html'
        with index.open() as f:
            template = Template(f.read())
            html = template.substitute(params)
        with index.open('w') as f:
            f.write(html)
        return f'file://{index}'

    @staticmethod
    def tidy_up():
        """remove local website files"""
        dest = Path().resolve() / 'launch_button'
        shutil.rmtree(dest)
