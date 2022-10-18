import os
import socket
from unittest.mock import patch

import pytest

from seeq import spy
from seeq.sdk import UserOutputV1
from seeq.spy._config import Setting
from seeq.spy._errors import SPyValueError
from seeq.spy.tests import test_common
from seeq.spy.tests.test_common import Sessions


def setup_module():
    test_common.initialize_sessions()


@pytest.mark.system
def test_default_session_bad_login():
    try:
        with pytest.raises(ValueError):
            spy.login('mark.derbecker@seeq.com', 'DataLab!', auth_token='Got any cheese?')

        assert spy.client is None
        assert spy.user is None

    finally:
        test_common.log_in_default_user()


# noinspection HttpUrlsUsage
@pytest.mark.system
def test_default_session_good_login():
    assert spy.client is not None
    assert spy.client.user_agent == f'Seeq-Python-SPy/{spy.__version__}/python'
    assert isinstance(spy.user, UserOutputV1)
    assert spy.user.username == 'agent_api_key'

    # force=False will mean that we don't try to login since we're already logged in
    spy.login(username='blah', password='wrong', force=False)

    assert spy.client is not None
    assert isinstance(spy.user, UserOutputV1)
    assert spy.user.username == 'agent_api_key'

    auth_token = spy.client.auth_token
    spy.session.client = None
    spy.client = None

    # Data Lab uses this pattern, and so we have to support it. We use gethostname() here just to make sure that the
    # default of http://localhost:34216 is not being used.
    url = f'http://{socket.gethostname().lower()}:34216'
    spy._config.set_seeq_url(url)

    spy.login(auth_token=auth_token)
    assert spy.client is not None

    # If we login again we want to make sure the session was not invalidated and auth_token is still valid
    spy.login(auth_token=auth_token)

    assert spy.client is not None
    assert isinstance(spy.user, UserOutputV1)
    assert spy.user.username == 'agent_api_key'
    assert spy.session.public_url == url

    # Make sure we can do a simple search
    df = spy.search({'Name': 'Area A_Temperature'}, workbook=spy.GLOBALS_ONLY)
    assert len(df) == 1


# noinspection HttpUrlsUsage
@pytest.mark.system
def test_login_with_private_url():
    public_url = 'http://localhost:34216'
    private_url = f'http://{socket.gethostname().lower()}:34216'
    with pytest.raises(SPyValueError):
        spy.login(username=test_common.SESSION_CREDENTIALS[Sessions.agent].username,
                  password=test_common.SESSION_CREDENTIALS[Sessions.agent].password,
                  private_url=private_url)

    spy.login(username=test_common.SESSION_CREDENTIALS[Sessions.agent].username,
              password=test_common.SESSION_CREDENTIALS[Sessions.agent].password,
              url=public_url,
              private_url=private_url)
    assert spy.client is not None
    assert isinstance(spy.user, UserOutputV1)
    assert spy.user.username == 'agent_api_key'
    assert spy.session.public_url == public_url
    assert spy.session.private_url == private_url


@pytest.mark.system
def test_login_to_different_server_than_data_lab():
    try:
        # Data Lab sets these environment variables and they are used if the user does
        # not supply URLs in the login call. This test makes sure that if the user DOES
        # supply a URL, that the environment variables are ignored.
        os.environ[Setting.SEEQ_URL.get_env_name()] = 'bad:@#$bad-public-url'
        os.environ[Setting.PRIVATE_URL.get_env_name()] = 'bad:@#$bad-private-url'

        spy.login(username=test_common.SESSION_CREDENTIALS[Sessions.agent].username,
                  password=test_common.SESSION_CREDENTIALS[Sessions.agent].password,
                  url=f'http://localhost:34216')
    finally:
        del os.environ[Setting.SEEQ_URL.get_env_name()]
        del os.environ[Setting.PRIVATE_URL.get_env_name()]


@pytest.mark.system
def test_good_login_user_switch():
    # login and get the token
    auth_token = spy.client.auth_token
    assert spy.user.username == 'agent_api_key'

    # create the state where kernel has no spy.user attached yet
    spy.client = None
    spy.user = None

    # do the initial auth_token login
    spy.login(auth_token=auth_token)
    # noinspection PyUnresolvedReferences
    assert spy.user.username == 'agent_api_key'

    # change the user inside the notebook
    spy.login(username=test_common.SESSION_CREDENTIALS[Sessions.nonadmin].username,
              password=test_common.SESSION_CREDENTIALS[Sessions.nonadmin].password)
    # noinspection PyUnresolvedReferences
    assert spy.user.username == test_common.SESSION_CREDENTIALS[Sessions.nonadmin].username

    # login again as when re-opening the notebook
    spy.login(auth_token=auth_token)
    # noinspection PyUnresolvedReferences
    assert spy.user.username == 'agent_api_key'


@pytest.mark.system
def test_credentials_file_with_username():
    try:
        with pytest.raises(ValueError):
            spy.login('mark.derbecker@seeq.com', 'DataLab!', credentials_file='credentials.key')
    finally:
        test_common.log_in_default_user()


@pytest.mark.system
def test_correct_origin_label_and_url_headers_in_data_lab():
    os.environ['SEEQ_SDL_CONTAINER_IS_DATALAB'] = 'true'
    os.environ['SEEQ_PROJECT_UUID'] = 'totally-real-id'

    with patch('seeq.spy._datalab.get_notebook_url') as url_mock:
        url_mock.return_value = "https://seeq-labs.com/data-lab/totally-real-id/notebooks/path/to/notebook in question"
        with patch('seeq.spy._datalab.get_data_lab_project_name') as name_mock:
            name_mock.return_value = "Project Name"

            spy.login(username=test_common.SESSION_CREDENTIALS[Sessions.agent].username,
                      password=test_common.SESSION_CREDENTIALS[Sessions.agent].password,
                      force=True)
            assert spy.client.default_headers['x-sq-origin-label'] == 'Project Name - path/to/notebook in question'
            assert spy.client.default_headers[
                       'x-sq-origin-url'] == '/data-lab/totally-real-id/notebooks/path/to/notebook%20in%20question'


@pytest.mark.system
def test_manually_setting_origin_label_and_url_headers():
    os.environ['SEEQ_SDL_CONTAINER_IS_DATALAB'] = 'false'
    spy.login(username=test_common.SESSION_CREDENTIALS[Sessions.agent].username,
              password=test_common.SESSION_CREDENTIALS[Sessions.agent].password,
              request_origin_url='/totally/a/real/url',
              request_origin_label='custom label',
              force=True)

    assert spy.client.default_headers['x-sq-origin-label'] == 'custom label'
    assert spy.client.default_headers['x-sq-origin-url'] == '/totally/a/real/url'
