import os

from django.conf import settings

from . import utils
from . import apps


APP_DIR = os.path.dirname(os.path.abspath(__file__))


class RecorderSettings:
    """Settings used while recording the requests"""
    ''' settings to change behavior while recording or simulating '''

    # ========= REQUEST (that comes to the server) ========= #
    REQUEST_IDENTIFIERS = [
        # Keys that identify the request to decide if the request is new or duplicated
        'method', 'basic_auth', 'rest_api'
    ]
    ALIAS_REQUEST_IDENTIFIERS = {
        # You can use those alias in `REQUEST_IDENTIFIERS` to make keys more readable
        'basic_auth': ['method', 'user.pk'],
        'rest_api': ['method', 'headers.Content-Type'],
    }

    SKIP_PATH = [
        # Don't record requests which paths starts with this
        # '/admin',
        '/favicon.ico',
        '/media/' if settings.MEDIA_URL == '/' else settings.MEDIA_URL,
        '/static/' if settings.STATIC_URL == '/' else settings.STATIC_URL,
    ]

    # ========= STORE (Where to save the request to simulate later) ========= #
    # TODO
    #   ask if user want to save each request into each app ?
    #   store dir inside the packages in other words use __dir__ magic var
    STORE_FILE_NAME = 'store/tester.store.json'
    STORE_FILES_DIR = f'{APP_DIR}/store/posted-files'

    @property
    def STORE_PATH(self):
        return utils.build_path(self.STORE_FILE_NAME)

    # ========= CREDENTIALS (Stored requests become useless if credentials changes, so we track them too) ========= #
    CREDENTIALS_WATCH = True
    CREDENTIALS_FILE_NAME = 'store/tester.credentials.json'
    CREDENTIALS_IDENTIFIER_KEY = 'user.pk'
    CREDENTIALS_KEYS = [
        # This is credentials keys
        'cookies.sessionid'
    ]

    @property
    def CREDENTIALS_PATH(self):
        return utils.build_path(self.CREDENTIALS_FILE_NAME)

    # ========= RESPONSE (Save responses to check if its changed/broken later) ========= #
    RESPONSE_CHECKS = [
        # When should we say response is changed ?!
        # What should we compare to decide if its broke or not
        'status_code', 'headers.Content-Type'
    ]

    # should we save html from response ?
    # it will use much  storage and performance will be bad
    DROP_HTML_FROM_RESPONSE = True
    DROP_MESSAGE = '[DATA DROPPED]'

    # ========= GENERAL ========= #
    RAISE_ERRORS = True # if errors happened while listening 
    IS_PRINT_REQUEST_ID = True # print id while listening to check it in the store faster


class SimulatorSettings:
    # Middleware can cause errors while simulating the old request
    # so set them here
    SKIP_MIDDLEWARE_CONTAIN = [
        # in simulating -- stop csrf and stop recording
        'csrf', apps.EchoTesterConfig.name
    ]


def load_settings():
    prefix = 'ECHO_TESTER_'
    settings_classes = [RecorderSettings, SimulatorSettings]

    for var in dir(settings):
        if var.startswith(prefix):
            var_name = var[len(prefix):]
            var_value = getattr(settings, var)
            for klass in settings_classes:
                # put var in the known place
                if var_name in dir(klass):
                    # TODO validate type before setting it
                    setattr(klass, var_name, var_value)


load_settings()

recorder_settings = RecorderSettings()
simulator_settings = SimulatorSettings()

# TODO
#   save data in db instead of json
#   create test that consist of array of an ordered requests to test something
#   modify just x, y, z in mod file that override the main file using simple id instead of hash
#   allow to use faker inside the post body
