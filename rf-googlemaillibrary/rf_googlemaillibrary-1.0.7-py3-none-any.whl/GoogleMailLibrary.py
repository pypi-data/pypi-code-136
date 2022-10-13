from __future__ import print_function

# import base64 for decode
import base64
import os.path
import re

# import html2text to convert html to text
import html2text

# import google libraries
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# import robot libraries
from robotlibcore import HybridCore, keyword
from robot.api import logger


__version__ = '1.0.7'


class GoogleMailLibrary(HybridCore):
    """``GoogleMailLibrary`` is a Robot Framework Library for interfacing tests with Google Email using the             \
        ``Google mail API v1``.


        This document will try to explain how to use this library and how to integrate it to your robot test suites.


        = OAuth 2.0 Scope Information for the Google Mail API =
         Refer to the table for the available scopes that is implemented in this library.
        | =Scope=                                                | =Meaning=                                                    |
        | https://www.googleapis.com/auth/gmail.readonly         | Allows read-only access to the user's mail and their   \
                                                                   properties.                                                  |

        Other Scopes available can be visited on https://developers.google.com/gmail/api/auth/scopes.


        = Generating a Json token file =
        The library is set to only accept already generated token stored in a token.json file.

        Generating a Json token can easily be done by using the code snippet below. Just replace the variables to        \
            generate your token.

        Before running the code below, first enable Google Mail API on your account. Place the credentials.json file in  \
            the same directory as the snippet will be.

        Simply follow this quickstart guide from Google Sheets API v4                                                      \
            https://developers.google.com/gmail/api/quickstart/python.


        | from __future__ import print_function

        | import os.path

        | from google.auth.transport.requests import Request
        | from google.oauth2.credentials import Credentials
        | from google_auth_oauthlib.flow import InstalledAppFlow
        | from googleapiclient.discovery import build
        | from googleapiclient.errors import HttpError

        | # If modifying these scopes, delete the file token.json.
        | SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


        | def main():
        |
        |     creds = None
        |     # The file token.json stores the user's access and refresh tokens, and is
        |     # created automatically when the authorization flow completes for the first
        |     # time.
        |     if os.path.exists('token.json'):
        |         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        |     # If there are no (valid) credentials available, let the user log in.
        |     if not creds or not creds.valid:
        |         if creds and creds.expired and creds.refresh_token:
        |             creds.refresh(Request())
        |         else:
        |             flow = InstalledAppFlow.from_client_secrets_file(
        |                 'credentials.json', SCOPES)
        |             creds = flow.run_local_server(port=0)
        |         # Save the credentials for the next run
        |         with open('token.json', 'w') as token:
        |             token.write(creds.to_json())
        |
        |     try:
        |         # Call the Gmail API
        |         service = build('gmail', 'v1', credentials=creds)
        |         results = service.users().labels().list(userId='me').execute()
        |         labels = results.get('labels', [])
        |
        |         if not labels:
        |             print('No labels found.')
        |             return
        |         print('Labels:')
        |         for label in labels:
        |             print(label['name'])
        |
        |     except HttpError as error:
        |         To Do(developer) - Handle errors from gmail API.
        |         print(f'An error occurred: {error}')
        |
        |
        |    if __name__ == '__main__':
        |     main()

        Run The Snippet like any other code

        = Reading Emails From Gmail Inbox =
        The Gmail API lets you view and manage Gmail mailbox data like threads, messages, and labels.

        = Getting Specific Email =
        To get specific email, Gmail API requires {userId} and {id} and a method to choose.
        Gmail Api resources and methods can be found here: https://developers.google.com/gmail/api/reference/rest?apix=true

        === Sample HTTP request ===
        GET https://gmail.googleapis.com/gmail/v1/users/{userId}/{method}/{id}

        === Path Parameters ===
        | Parameters | Description |
        | `userId` | string - The user's email address. The special value me can be used to indicate the authenticated user.    |
        | `id` | string - The ID of the message to retrieve. This ID is usually retrieved using messages.list.      \
             The ID is also contained in the result when a message is inserted (messages.insert) or imported (messages.import). |

        === Query Parameters ===
        | Parameters | Description |
        | `format` | enum (Format) - The format to return the message in.   |
        | `metadataHeaders[]` | string -  When given and format is METADATA, only include headers specified.    |

        === Request Body ===
        The request body must be empty.

        === Response Body ===
        If successful, the response body contains an instance of Message.
        |   {
        |     "id": string,
        |     "threadId": string,
        |     "labelIds": [
        |         string
        |     ],
        |     "snippet": string,
        |     "historyId": string,
        |     "internalDate": string,
        |     "payload": {
        |         object (MessagePart)
        |     },
        |     "sizeEstimate": integer,
        |     "raw": string
        |    }

    """
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self,
                 scopes=['https://mail.google.com/'],
                 cred=""
                 ):

        """Google Mail API v1 requires that you set the scope to be used. Refer to the
           `OAuth 2.0 Scope Information for the Google Mail API`. Multiple Scopes could be defined.
           The Scopes should be the one used in generating the `token.json` file.
        """
        libraries = []
        HybridCore.__init__(self, libraries)
        self.SCOPE = scopes
        self.credentials = cred

    @keyword
    def initialize_email(self, tokenFile):

        """Initializes the connection to the specified Google Email. Takes 1 positional arguments\
            tokenFile.
           Sample Usage:
           | `Initialize Email`   | ${EXECDIR}/token.json   |
        """
        self.tokenFile = tokenFile
        self.userId = 'me'
        self.creds = self._validate_user_credential()
        self.service = build('gmail', 'v1', credentials=self.creds, cache_discovery=False)
        self.emailObject = self.service

    @keyword
    def parse_first_email(self):
        ''' GET https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}
            Gets the list of messages in inbox and return the first and most recent message in inbox
        '''
        try:
            raw = self.service.users().messages().get(userId=self.userId, id=self.get_first_id_in_inbox()).execute()

            return raw
        except HttpError as error:
            print(f'An error occurred: {error}')

    @keyword
    def parse_specific_email(self, email_id):
        ''' Please refer to https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get
            GET https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}
            Gets the specific email by providing id.

            Gmail api only allow sending snippet or raw messages.
            snippet will only show one or two lines of message.
            this will return raw data of first email
        '''

        try:
            raw = self.service.users().messages().get(userId=self.userId, id=email_id).execute()

            return raw
        except HttpError as error:
            print(f'An error occurred: {error}')

    @keyword
    def delete_message(self, email_id):

        ''' Please refer to https://developers.google.com/gmail/api/reference/rest/v1/users.messages/delete
            Delete https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}
            Delete the specific email by providing id.
        '''
        try:
            raw = self.service.users().messages().delete(userId=self.userId, id=email_id).execute()

            return raw
        except HttpError as error:
            print(f'An error occurred: {error}')

    @keyword
    def delete_all_messages(self):
        """ Gets the list of messages in inbox and Delete all messages
            Messages delete will be permanently deleted from inbox
        """

        raw_list = self._get_list_of_messages()
        while raw_list['resultSizeEstimate'] != 0:
            for d in raw_list['messages']:
                self.delete_message(d['id'])
            raw_list = self._get_list_of_messages()

    @keyword
    def get_first_id_in_inbox(self):
        """ Gets the list of messages in inbox and return the first and most recent message id in inbox

        """
        first_id = self._get_list_of_messages()
        first_id = first_id['messages'][0]['id']
        return first_id

    @keyword
    def return_sender_name(self, email_id):
        ''' Return the sender of the specific email
        '''

        try:
            raw = self.service.users().messages().get(userId=self.userId, id=email_id).execute()
            for d in raw['payload']['headers']:
                if d['name'] == 'From':
                    sender = d['value']

            return sender

        except HttpError as error:
            print(f'An error occurred: {error}')

    @keyword
    def return_email_timestamp(self, email_id):
        ''' Return the timestamp of the specific email
            Give Specific time when email was received
        '''

        try:
            raw = self.service.users().messages().get(userId=self.userId, id=email_id).execute()
            for d in raw['payload']['headers']:
                if d['name'] == 'X-Google-Original-Date':
                    date = d['value']

            return date

        except HttpError as error:
            print(f'An error occurred: {error}')

    @keyword
    def return_email_body_content(self, raw_message):
        """ Returns the actual Body Content of the email
            Gmail Api does only gives raw content (base64)
            Decodes base64 to a readable text.
        """
        mimeType = raw_message['payload']['mimeType']

        if mimeType == 'multipart/alternative':
            body_content = raw_message['payload']['parts'][0]['body']['data']
            decoded = self._decode_base64(body_content)
        else:
            body_content = raw_message['payload']['body']['data']
            print(body_content)
            decoded = self._convert_html_to_text(body_content)

        return decoded

    @keyword
    def inbox_should_not_be_empty(self):
        """ Checks if inbox is empty
            Pass test if true
        """

        self._wait_until(lambda: self._get_list_of_messages()['resultSizeEstimate'] >= 1,
                         "Inbox Contains No Messages.")

    @keyword
    def inbox_should_be_empty(self):
        """ Checks if inbox is not empty
            Pass test if true
        """
        print(self._get_list_of_messages())
        self._wait_until(lambda: self._get_list_of_messages()['resultSizeEstimate'] == 0,
                         "Inbox Contains Messages")

    def _convert_html_to_text(self, raw_message):
        """ Email Content can be simple text , rich text or HTML
            Using html2text library,Converts HTML Content into a readable text
        """
        decoded = self._decode_base64(raw_message)
        h = html2text.HTML2Text()
        email_content = h.handle(decoded)
        return email_content

    def _get_list_of_messages(self):
        """ Gets the list of all messages in inbox by using Gmail Api module and return ID
            Please refer to Google Api Documentation
            https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list
        """
        try:
            list = self.emailObject.users().messages().list(userId=self.userId).execute()
        except HttpError as error:
            print(f'An error occurred: {error}')
        return list

    def _decode_base64(self, base_64):
        """ Full raw data coming from gmail is decoded to base64.
            return decoded raw data from gmail to simple text, rich text or html
        """
        encoded = base64.urlsafe_b64decode(base_64.encode('utf-8'))
        decoded = encoded.decode()
        return decoded

    def _wait_until(self, condition, error):

        if condition():
            return
        else:
            raise ValueError(error)

    def _validate_user_credential(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        if os.path.exists(self.tokenFile):
            creds = Credentials.from_authorized_user_file(self.tokenFile, self.SCOPE)
            print("pass")
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials, self.SCOPE)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return creds
