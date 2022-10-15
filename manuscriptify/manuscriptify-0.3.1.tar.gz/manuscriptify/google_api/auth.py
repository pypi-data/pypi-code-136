# manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Open source, MIT license: http://www.opensource.org/licenses/mit-license.php
"""
google auth logic

"""
import sys, os.path, base64

from google.auth.transport.requests import Request
from google.auth.exceptions import TransportError
from google.oauth2.credentials import Credentials

from manuscriptify.google_api.button_hack import ButtonFlow as Flow
from manuscriptify.google_api.manuscriptify import manuscriptify_

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


class Auth(Credentials):
    """get credentials"""

    def __new__(cls):
        token = cls._get_token()
        return token

    @classmethod
    def _get_token(self):
        """get token using desktop app creds and google oauth flow"""
        token = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        try:
            if os.path.exists('token.json'):
                args = ['token.json', SCOPES]
                token = Credentials.from_authorized_user_file(*args)
            # If there are no (valid) credentials available, let the user log in.
            if not token or not token.valid:
                if token and token.expired and token.refresh_token:
                    token.refresh(Request())
                else:
                    sys.tracebacklimit = 0
                    args = [
                        eval(base64.b64decode(manuscriptify_)),
                        SCOPES
                    ]
                    flow = Flow.from_client_config(*args)
                    token = flow.run_local_server(port=0)
                    sys.tracebacklimit = 1000
                # Save the credentials for the next run
                with open('token.json', 'w') as f:
                    f.write(token.to_json())
        except TransportError:
            raise TransportError('no connection')
        return token
