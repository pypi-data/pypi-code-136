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


import base64
import datetime
import logging
import re
import urllib.parse as urlparse
import xml.etree.ElementTree as ET
import zlib
from html import unescape
from unittest import mock

import lasso
import pytest
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.urls import reverse
from django.utils.encoding import force_str
from httmock import HTTMock, all_requests
from httmock import response as mock_response
from pytest import fixture

from mellon import models
from mellon.utils import create_metadata
from mellon.views import lasso_decode


@fixture
def idp_metadata():
    return open('tests/metadata.xml').read()


@fixture
def idp_private_key():
    return open('tests/idp-private-key.pem').read()


@fixture
def sp_private_key():
    return open('tests/sp-private-key.pem').read()


@fixture
def sp_public_key():
    return ''.join(open('tests/sp-public-key.pem').read().splitlines()[1:-1])


@fixture
def sp_settings(private_settings, idp_metadata, sp_private_key, sp_public_key):
    private_settings.MELLON_IDENTITY_PROVIDERS = [
        {
            'METADATA': idp_metadata,
        }
    ]
    private_settings.MELLON_PUBLIC_KEYS = [sp_public_key]
    private_settings.MELLON_PRIVATE_KEYS = [sp_private_key]
    private_settings.MELLON_NAME_ID_POLICY_FORMAT = lasso.SAML2_NAME_IDENTIFIER_FORMAT_PERSISTENT
    private_settings.LOGIN_REDIRECT_URL = '/'
    private_settings.MELLON_SIGNATURE_METHOD = 'RSA_SHA256'
    return private_settings


@fixture
def sp_metadata(sp_settings, rf):
    request = rf.get('/')
    return create_metadata(request)


class MockIdp:
    session_dump = None
    identity_dump = None

    def __init__(self, idp_metadata, private_key, sp_metadata, name_id=None):
        self.server = server = lasso.Server.newFromBuffers(idp_metadata, private_key)
        self.server.signatureMethod = lasso.SIGNATURE_METHOD_RSA_SHA256
        server.addProviderFromBuffer(lasso.PROVIDER_ROLE_SP, sp_metadata)

    def reset_session_dump(self):
        self.session_dump = None

    def process_authn_request_redirect(self, url, auth_result=True, consent=True, msg=None, name_id=None):
        login = self.login = lasso.Login(self.server)
        if self.identity_dump:
            login.setIdentityFromDump(self.identity_dump)
        if self.session_dump:
            login.setSessionFromDump(self.session_dump)
        login.processAuthnRequestMsg(url.split('?', 1)[1])
        # See
        # https://docs.python.org/2/library/zlib.html#zlib.decompress
        # for the -15 magic value.
        #
        # * -8 to -15: Uses the absolute value of wbits as the window size
        # logarithm. The input must be a raw stream with no header or trailer.
        #
        # it means Deflate instead of GZIP (same stream no header, no trailer)
        self.request = zlib.decompress(
            base64.b64decode(urlparse.parse_qs(urlparse.urlparse(url).query)['SAMLRequest'][0]), -15
        )
        assert 'rsa-sha256' in url
        try:
            login.validateRequestMsg(auth_result, consent)
        except lasso.LoginRequestDeniedError:
            pass
        else:
            login.buildAssertion(
                lasso.SAML_AUTHENTICATION_METHOD_PASSWORD,
                datetime.datetime.now().isoformat(),
                None,
                datetime.datetime.now().isoformat(),
                datetime.datetime.now().isoformat(),
            )
            for key in name_id or {}:
                setattr(login.assertion.subject.nameID, key, name_id[key])

            def add_attribute(name, *values, **kwargs):
                fmt = kwargs.get('fmt', lasso.SAML2_ATTRIBUTE_NAME_FORMAT_BASIC)
                statements = login.response.assertion[0].attributeStatement or [
                    lasso.Saml2AttributeStatement()
                ]
                statement = statements[0]
                login.response.assertion[0].attributeStatement = statements
                attributes = list(statement.attribute)
                for attribute in attributes:
                    if attribute.name == name and attribute.nameFormat == fmt:
                        break
                else:
                    attribute = lasso.Saml2Attribute()
                    attribute.name = name
                    attributes.append(attribute)
                    statement.attribute = attributes
                attribute_values = list(attribute.attributeValue)
                atv = lasso.Saml2AttributeValue()
                attribute_values.append(atv)
                attribute.attributeValue = attribute_values
                value_any = []
                for value in values:
                    if isinstance(value, lasso.Node):
                        value_any.append(value)
                    else:
                        mtn = lasso.MiscTextNode.newWithString(force_str(value))
                        mtn.textChild = True
                        value_any.append(mtn)
                atv.any = value_any

            add_attribute('email', 'john', '.doe@gmail.com')
            add_attribute('wtf', 'john', lasso.MiscTextNode.newWithXmlNode('<a>coucou</a>'))
            add_attribute('first_name', '<i>Fr\xe9d\xe9ric</i>')

        if not auth_result and msg:
            login.response.status.statusMessage = msg
        if login.protocolProfile == lasso.LOGIN_PROTOCOL_PROFILE_BRWS_ART:
            login.buildArtifactMsg(lasso.HTTP_METHOD_ARTIFACT_GET)
            self.artifact = login.artifact
            self.artifact_message = login.artifactMessage
        elif login.protocolProfile == lasso.LOGIN_PROTOCOL_PROFILE_BRWS_POST:
            login.buildAuthnResponseMsg()
        else:
            raise NotImplementedError
        if login.msgBody:
            assert b'rsa-sha256' in base64.b64decode(login.msgBody)
        if login.identity:
            self.identity_dump = login.identity.dump()
        else:
            self.identity_dump = None
        if login.session:
            self.session_dump = login.session.dump()
        else:
            self.session_dump = None
        return login.msgUrl, login.msgBody, login.msgRelayState

    def resolve_artifact(self, soap_message):
        login = lasso.Login(self.server)
        login.processRequestMsg(soap_message)
        assert 'rsa-sha256' in soap_message
        if hasattr(self, 'artifact') and self.artifact == login.artifact:
            # artifact is known, go on !
            login.artifactMessage = self.artifact_message
            # forget the artifact
            del self.artifact
            del self.artifact_message
        login.buildResponseMsg()
        assert 'rsa-sha256' in lasso_decode(login.msgBody)
        return '<?xml version="1.0"?>\n' + lasso_decode(login.msgBody)

    def init_slo(self, full=False, method=lasso.HTTP_METHOD_REDIRECT, relay_state=None):
        logout = lasso.Logout(self.server)
        logout.setIdentityFromDump(self.identity_dump)
        logout.setSessionFromDump(self.session_dump)
        logout.initRequest(None, method)
        logout.msgRelayState = relay_state
        if full:
            logout.request.sessionIndexes = ()
            logout.request.sessionIndex = None
        logout.buildRequestMsg()
        return logout.msgUrl, logout.msgBody, logout.msgRelayState

    def check_slo_return(self, url=None, body=None):
        logout = lasso.Logout(self.server)
        logout.setIdentityFromDump(self.identity_dump)
        logout.setSessionFromDump(self.session_dump)
        if body:
            logout.processResponseMsg(force_str(body))
        else:
            logout.processResponseMsg(url.split('?', 1)[-1])

    def process_logout_request_redirect(self, url):
        logout = lasso.Logout(self.server)
        logout.setIdentityFromDump(self.identity_dump)
        logout.setSessionFromDump(self.session_dump)
        logout.processRequestMsg(url.split('?', 1)[1])
        logout.validateRequest()
        logout.buildResponseMsg()
        return logout.msgUrl

    def mock_artifact_resolver(self):
        @all_requests
        def f(url, request):
            content = self.resolve_artifact(request.body)
            return mock_response(200, content=content, headers={'Content-Type': 'application/soap+xml'})

        return f


@fixture
def idp(sp_settings, idp_metadata, idp_private_key, sp_metadata):
    return MockIdp(idp_metadata, idp_private_key, sp_metadata)


def test_sso_slo(db, app, idp, caplog, sp_settings):
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state
    assert 'eo:next_url' not in str(idp.request)
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'created new user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'
    response = app.get(reverse('mellon_logout'), extra_environ={'HTTP_REFERER': '/some/path'})
    assert urlparse.urlparse(response['Location']).path == '/singleLogout'
    url = idp.process_logout_request_redirect(response.location)
    response = app.get(url)
    assert response.location == '/'

    # again, user is already logged out
    response = app.get(reverse('mellon_logout'), extra_environ={'HTTP_REFERER': '/some/path'})
    assert urlparse.urlparse(response['Location']).path == '/'


def test_sso_slo_next(db, app, idp, caplog, sp_settings):
    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    response = app.get(
        reverse('mellon_logout') + '?next=/some/path/', extra_environ={'HTTP_REFERER': '/other/path'}
    )
    assert urlparse.urlparse(response['Location']).path == '/singleLogout'
    url = idp.process_logout_request_redirect(response.location)
    response = app.get(url)
    assert response.location == '/some/path/'


def test_sso_slo_default_next_url(db, app, idp, caplog, sp_settings, rf, django_user_model):
    from mellon.views import logout

    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})

    request = rf.get('/logout/')
    request.session = app.session
    request.user = django_user_model.objects.get()
    response = logout(request, logout_next_url='/other/path/')
    assert list(request.session.values()) == ['/other/path/']

    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})

    request = rf.get('/logout/?next=/some/path/')
    request.session = app.session
    request.user = django_user_model.objects.get()
    response = logout(request, logout_next_url='/other/path/')
    assert list(request.session.values()) == ['/some/path/']


def test_sso_idp_slo(db, app, idp, caplog, sp_settings):
    assert Session.objects.count() == 0
    assert User.objects.count() == 0

    # first session
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state
    assert 'eo:next_url' not in str(idp.request)
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'created new user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'

    # start a new Lasso session
    idp.reset_session_dump()

    # second session
    app.cookiejar.clear()
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state
    assert 'eo:next_url' not in str(idp.request)
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'created new user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'

    assert Session.objects.count() == 2
    assert User.objects.count() == 1

    # idp logout
    url, body, relay_state = idp.init_slo()
    response = app.get(url)
    assert response.location.startswith('http://idp5/singleLogoutReturn?')
    assert Session.objects.count() == 1
    idp.check_slo_return(response.location)


def test_sso_idp_slo_soap(db, app, idp, caplog, sp_settings):
    assert Session.objects.count() == 0
    assert User.objects.count() == 0

    # first session
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state
    assert 'eo:next_url' not in str(idp.request)
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'created new user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'

    # start a new Lasso session
    idp.reset_session_dump()

    # second session
    caplog.clear()
    app.cookiejar.clear()
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state
    assert 'eo:next_url' not in str(idp.request)
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'looked up user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'

    assert Session.objects.count() == 2
    assert User.objects.count() == 1

    # idp logout
    app.cookiejar.clear()

    url, body, relay_state = idp.init_slo(method=lasso.HTTP_METHOD_SOAP)
    response = app.post(url, params=body, headers={'Content-Type': 'text/xml'})
    assert Session.objects.count() == 1
    idp.check_slo_return(body=response.content)


def test_sso_idp_slo_full(db, app, idp, caplog, sp_settings):
    assert Session.objects.count() == 0
    assert User.objects.count() == 0

    # first session
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state
    assert 'eo:next_url' not in str(idp.request)
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'created new user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'

    # second session
    caplog.clear()
    app.cookiejar.clear()
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state
    assert 'eo:next_url' not in str(idp.request)
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'looked up user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'

    assert Session.objects.count() == 2
    assert User.objects.count() == 1

    # idp logout
    url, body, relay_state = idp.init_slo(full=True)
    response = app.get(url)
    assert response.location.startswith('http://idp5/singleLogoutReturn?')
    assert Session.objects.count() == 0
    idp.check_slo_return(url=response.location)


def test_sso_idp_slo_full_soap(db, app, idp, caplog, sp_settings):
    assert Session.objects.count() == 0
    assert User.objects.count() == 0

    # first session
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state
    assert 'eo:next_url' not in str(idp.request)
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'created new user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'

    # second session
    caplog.clear()
    app.cookiejar.clear()
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state
    assert 'eo:next_url' not in str(idp.request)
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'looked up user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'

    assert Session.objects.count() == 2
    assert User.objects.count() == 1

    # idp logout
    app.cookiejar.clear()
    url, body, relay_state = idp.init_slo(method=lasso.HTTP_METHOD_SOAP, full=True)
    response = app.post(url, params=body, headers={'Content-Type': 'text/xml'})
    assert Session.objects.count() == 0
    idp.check_slo_return(body=response.content)


def test_sso(db, app, idp, caplog, sp_settings):
    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert not relay_state
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'created new user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == sp_settings.LOGIN_REDIRECT_URL
    assert app.session['mellon_session']['first_name'] == ['<i>Fr\xe9d\xe9ric</i>']
    assert app.session['mellon_session']['email'] == ['john.doe@gmail.com']
    assert app.session['mellon_session']['wtf'] == []
    assert not app.session['mellon_session']['force_authn']
    assert not app.session['mellon_session']['nonce']


def test_sso_request_denied(db, app, idp, caplog, sp_settings):
    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(
        response['Location'], auth_result=False, msg='User is not allowed to login'
    )
    assert not relay_state
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert (
        "status is not success codes: ['urn:oasis:names:tc:SAML:2.0:status:Responder',\
 'urn:oasis:names:tc:SAML:2.0:status:RequestDenied']"
        in caplog.text
    )


@pytest.mark.urls('urls_tests_template_base')
def test_template_base(db, app, idp, caplog, sp_settings):
    response = app.get(reverse('mellon_metadata'))
    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(
        response['Location'], auth_result=False, msg='User is not allowed to login'
    )
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'Theme is ok' in response.text

    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    response = app.get(reverse('mellon_logout'))
    assert urlparse.urlparse(response['Location']).path == '/singleLogout'


@pytest.mark.urls('urls_tests_template_hook')
def test_template_hook(db, app, idp, caplog, sp_settings):
    response = app.get(reverse('mellon_metadata'))
    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(
        response['Location'], auth_result=False, msg='User is not allowed to login'
    )
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'Theme is ok' in response.text
    assert 'HOOK' in response.text

    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    response = app.get(reverse('mellon_logout'))
    assert urlparse.urlparse(response['Location']).path == '/singleLogout'


def test_no_template_base(db, app, idp, caplog, sp_settings):
    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(
        response['Location'], auth_result=False, msg='User is not allowed to login'
    )
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'Theme is ok' not in response.text


def test_sso_request_denied_artifact(db, app, caplog, sp_settings, idp_metadata, idp_private_key, rf):
    sp_settings.MELLON_DEFAULT_ASSERTION_CONSUMER_BINDING = 'artifact'
    request = rf.get('/')
    sp_metadata = create_metadata(request)
    idp = MockIdp(idp_metadata, idp_private_key, sp_metadata)
    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(
        response['Location'], auth_result=False, msg='User is not allowed to login'
    )
    assert not relay_state
    assert body is None
    assert reverse('mellon_login') in url
    assert 'SAMLart' in url
    acs_artifact_url = url.split('testserver', 1)[1]
    with HTTMock(idp.mock_artifact_resolver()):
        response = app.get(acs_artifact_url, params={'RelayState': relay_state})
    assert (
        "status is not success codes: ['urn:oasis:names:tc:SAML:2.0:status:Responder',\
 'urn:oasis:names:tc:SAML:2.0:status:RequestDenied']"
        in caplog.text
    )
    assert 'User is not allowed to login' in response


def test_sso_artifact(db, app, caplog, sp_settings, idp_metadata, idp_private_key, rf):
    sp_settings.MELLON_DEFAULT_ASSERTION_CONSUMER_BINDING = 'artifact'
    request = rf.get('/')
    sp_metadata = create_metadata(request)
    idp = MockIdp(idp_metadata, idp_private_key, sp_metadata)
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state
    assert body is None
    assert reverse('mellon_login') in url
    assert 'SAMLart' in url
    acs_artifact_url = url.split('testserver', 1)[1]
    with HTTMock(idp.mock_artifact_resolver()):
        response = app.get(acs_artifact_url, params={'RelayState': relay_state})
    assert 'created new user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'
    # force delog, but keep session information for relaystate handling
    assert app.session
    del app.session['_auth_user_id']
    assert 'dead artifact' not in caplog.text

    caplog.clear()
    with HTTMock(idp.mock_artifact_resolver()):
        response = app.get(acs_artifact_url, params={'RelayState': relay_state})
    # verify retry login was asked
    assert 'dead artifact' in caplog.text
    assert urlparse.urlparse(response['Location']).path == reverse('mellon_login')
    response = response.follow()
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert relay_state

    # verify caplog has been cleaned
    caplog.clear()
    assert 'created new user' not in caplog.text
    assert body is None
    assert reverse('mellon_login') in url
    assert 'SAMLart' in url
    acs_artifact_url = url.split('testserver', 1)[1]

    caplog.clear()
    with HTTMock(idp.mock_artifact_resolver()):
        response = app.get(acs_artifact_url, params={'RelayState': relay_state})
    assert 'created new user' not in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert urlparse.urlparse(response['Location']).path == '/whatever/'


def test_sso_slo_pass_next_url(db, app, idp, caplog, sp_settings):
    sp_settings.MELLON_ADD_AUTHNREQUEST_NEXT_URL_EXTENSION = True
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert 'eo:next_url' in str(idp.request)
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'created new user' in caplog.text
    assert 'logged in using SAML' in caplog.text
    assert response['Location'].endswith('/whatever/')


def test_sso_artifact_no_loop(db, app, caplog, sp_settings, idp_metadata, idp_private_key, rf):
    sp_settings.MELLON_DEFAULT_ASSERTION_CONSUMER_BINDING = 'artifact'
    request = rf.get('/')
    sp_metadata = create_metadata(request)
    idp = MockIdp(idp_metadata, idp_private_key, sp_metadata)
    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert body is None
    assert reverse('mellon_login') in url
    assert 'SAMLart' in url
    acs_artifact_url = url.split('testserver', 1)[1]

    # forget the artifact
    idp.artifact = ''

    with HTTMock(idp.mock_artifact_resolver()):
        response = app.get(acs_artifact_url)
    assert 'MELLON_RETRY_LOGIN=1;' in response['Set-Cookie']

    # first error, we retry
    assert urlparse.urlparse(response['Location']).path == reverse('mellon_login')

    # check we are not logged
    assert not app.session

    # redo
    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert body is None
    assert reverse('mellon_login') in url
    assert 'SAMLart' in url
    acs_artifact_url = url.split('testserver', 1)[1]

    # forget the artifact
    idp.artifact = ''
    with HTTMock(idp.mock_artifact_resolver()):
        response = app.get(acs_artifact_url)

    # check cookie is deleted after failed retry
    # Py3-Dj111 variation
    assert re.match(r'.*MELLON_RETRY_LOGIN=("")?;', response['Set-Cookie'])
    assert 'Location' not in response

    # check we are still not logged
    assert not app.session

    # check return url is in page
    assert '"%s"' % sp_settings.LOGIN_REDIRECT_URL in response.text


def test_sso_slo_pass_login_hints_always_backoffice(db, app, idp, caplog, sp_settings):
    sp_settings.MELLON_LOGIN_HINTS = ['always_backoffice']
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    root = ET.fromstring(idp.request)
    login_hints = root.findall('.//{https://www.entrouvert.com/}login-hint')
    assert len(login_hints) == 1, 'missing login hint'
    assert login_hints[0].text == 'backoffice', 'login hint is not backoffice'


def test_sso_slo_pass_login_hints_backoffice(db, app, idp, caplog, sp_settings):
    sp_settings.MELLON_LOGIN_HINTS = ['backoffice']

    response = app.get(reverse('mellon_login'))
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    root = ET.fromstring(idp.request)
    login_hints = root.findall('.//{https://www.entrouvert.com/}login-hint')
    assert len(login_hints) == 0

    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    root = ET.fromstring(idp.request)
    login_hints = root.findall('.//{https://www.entrouvert.com/}login-hint')
    assert len(login_hints) == 0

    for next_url in ['/manage/', '/admin/', '/manager/']:
        response = app.get(reverse('mellon_login') + '?next=%s' % next_url)
        url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
        root = ET.fromstring(idp.request)
        login_hints = root.findall('.//{https://www.entrouvert.com/}login-hint')
        assert len(login_hints) == 1, 'missing login hint'
        assert login_hints[0].text == 'backoffice', 'login hint is not backoffice'


def test_passive_auth_middleware_ok(db, app, idp, caplog, settings):
    settings.MELLON_OPENED_SESSION_COOKIE_NAME = 'IDP_SESSION'
    assert 'MELLON_PASSIVE_TRIED' not in app.cookies
    # webtest-lint is against unicode
    app.set_cookie('IDP_SESSION', '1234')
    response = app.get('/', headers={'Accept': 'text/html'}, status=302)
    assert urlparse.urlparse(response.location).path == '/login/'
    assert urlparse.parse_qs(urlparse.urlparse(response.location).query, keep_blank_values=True) == {
        'next': ['http://testserver/'],
        'passive': [''],
    }
    assert app.cookies['MELLON_PASSIVE_TRIED'] == '1234'

    # simulate closing of session at IdP
    app.cookiejar.clear('testserver.local', '/', 'IDP_SESSION')
    assert 'IDP_SESSION' not in app.cookies

    # verify MELLON_PASSIVE_TRIED is removed
    assert 'MELLON_PASSIVE_TRIED' in app.cookies
    response = app.get('/', status=200)
    assert 'MELLON_PASSIVE_TRIED' not in app.cookies

    # check passive authentication is tried again
    app.set_cookie('IDP_SESSION', '1')
    response = app.get('/', headers={'Accept': 'text/html'}, status=302)
    assert urlparse.urlparse(response.location).path == '/login/'
    assert urlparse.parse_qs(urlparse.urlparse(response.location).query, keep_blank_values=True) == {
        'next': ['http://testserver/'],
        'passive': [''],
    }
    assert 'MELLON_PASSIVE_TRIED' in app.cookies

    # but not two times
    response = app.get('/', headers={'Accept': 'text/html'}, status=200)
    # if session change at IdP
    app.set_cookie('IDP_SESSION', 'abcd')
    # then we try again...
    response = app.get('/', headers={'Accept': 'text/html'}, status=302)

    # ok, let's change again and login
    app.set_cookie('IDP_SESSION', '5678')
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert app.session['mellon_opened_session_cookie'] == '5678'
    assert 'MELLON_PASSIVE_TRIED' not in app.cookies
    assert '_auth_user_id' in app.session
    # ok change the idp session id
    app.set_cookie('IDP_SESSION', '1234')
    # if we try a request, we are logged out and redirected to try a new passive login
    response = app.get('/', headers={'Accept': 'text/html'}, status=302)
    assert '_auth_user_id' not in app.session
    assert 'MELLON_PASSIVE_TRIED' in app.cookies


def test_passive_auth_middleware_no_passive_auth_parameter(db, app, idp, caplog, settings):
    settings.MELLON_OPENED_SESSION_COOKIE_NAME = 'IDP_SESSION'
    assert 'MELLON_PASSIVE_TRIED' not in app.cookies
    # webtest-lint is against unicode
    app.set_cookie('IDP_SESSION', '1')
    app.get('/?no-passive-auth', headers={'Accept': 'text/html'}, status=200)


def test_sso_user_change(db, app, idp, caplog, sp_settings):
    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])

    response = app.get(reverse('mellon_login') + '?next=/whatever/')
    other_identity = '<Identity xmlns="http://www.entrouvert.org/namespaces/lasso/0.0" Version="2"><lasso:Federation xmlns:lasso="http://www.entrouvert.org/namespaces/lasso/0.0" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" RemoteProviderID="http://testserver/metadata/" FederationDumpVersion="2"><lasso:LocalNameIdentifier><saml:NameID Format="urn:oasis:names:tc:SAML:2.0:nameid-format:persistent" NameQualifier="http://idp5/metadata" SPNameQualifier="http://testserver/metadata/">_otherE805F46B436F83669FB3F6CEE7</saml:NameID></lasso:LocalNameIdentifier></lasso:Federation></Identity>'
    idp.identity_dump = other_identity
    url, other_body, other_relay_state = idp.process_authn_request_redirect(response['Location'])

    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert 'created new user' in caplog.text
    caplog.clear()

    response = app.post(
        reverse('mellon_login'), params={'SAMLResponse': other_body, 'RelayState': other_relay_state}
    )
    assert 'created new user' in caplog.text


def test_debug_sso(db, app, idp, caplog, sp_settings, settings):
    response = app.get(reverse('mellon_debug_login') + '?next=/whatever/', status=403)

    settings.DEBUG = True
    response = app.get(reverse('mellon_debug_login') + '?next=/whatever/')
    assert urlparse.urlparse(response['Location']).path == '/login/'
    response = response.follow()
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert url.endswith(reverse('mellon_login'))
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    response_text = unescape(response.text)
    assert 'Attributes' in response.text
    assert "'email': ['john.doe@gmail.com']" in response_text
    assert '<saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"' in response_text
    assert '<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"' in response_text
    assert 'mellon: created new user _' in response_text
    # check also in logs
    assert "'email': ['john.doe@gmail.com']" in caplog.text
    assert '<saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"' in caplog.text
    assert '<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"' in caplog.text


def test_debug_sso_on_exception(db, app, idp, caplog, sp_settings, settings):
    settings.DEBUG = True
    response = app.get(reverse('mellon_debug_login') + '?next=/whatever/')
    response = response.follow()
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])

    def lasso_error(*args, **kwargs):
        raise lasso.Error

    with mock.patch('lasso.Login.acceptSso', side_effect=lasso_error):
        response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})

    response_text = unescape(response.text)
    assert '<saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"' in response_text


def test_nonce(db, app, idp, caplog, sp_settings):
    response = app.get(reverse('mellon_login') + '?nonce=1234')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert app.session['mellon_session']['nonce'] == '1234'


def test_force_authn(db, app, idp, caplog, sp_settings):
    response = app.get(reverse('mellon_login') + '?force-authn=1')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    assert idp.login.request.forceAuthn

    response = app.post(reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state})
    assert app.session['mellon_session']['force_authn']


def test_sso_slo_transient_name_identifier(db, app, idp, caplog, sp_settings):
    caplog.set_level(logging.WARNING)
    sp_settings.MELLON_TRANSIENT_FEDERATION_ATTRIBUTE = 'email'
    response = app.get('/login/')
    url, body, relay_state = idp.process_authn_request_redirect(
        response['Location'],
        name_id={
            'format': lasso.SAML2_NAME_IDENTIFIER_FORMAT_TRANSIENT,
            'content': '1234',
        },
    )
    response = app.post('/login/', params={'SAMLResponse': body, 'RelayState': relay_state})

    usi = models.UserSAMLIdentifier.objects.get()
    assert usi.name_id == 'john.doe@gmail.com'
    session_index = models.SessionIndex.objects.get(saml_identifier=usi)
    assert session_index.transient_name_id == '1234'

    response = app.get('/logout/')
    assert urlparse.urlparse(response['Location']).path == '/singleLogout'
    url = idp.process_logout_request_redirect(response.location)
    caplog.clear()
    response = app.get(url)
    assert len(caplog.records) == 0, 'logout failed'
    assert response.location == '/'


def test_sso_slo_token(db, app, rf, idp, caplog, django_user_model, freezer):
    from mellon.views import LogoutView

    caplog.set_level(logging.WARNING)
    response = app.get('/login/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    response = app.post('/login/', params={'SAMLResponse': body, 'RelayState': relay_state})

    assert models.SessionIndex.objects.count() == 1
    assert models.SessionIndex.objects.filter(logout_timestamp__isnull=True).count() == 1
    request = rf.get('/whatever/')
    request.session = app.session
    request.user = django_user_model.objects.get()
    token_logout_url = LogoutView.make_logout_token_url(request, next_url='/somepath/')
    assert models.SessionIndex.objects.count() == 1
    assert models.SessionIndex.objects.filter(logout_timestamp__isnull=False).count() == 1
    assert token_logout_url
    app.session.flush()
    assert '_auth_user_id' not in app.session
    response = app.get(token_logout_url)
    assert urlparse.urlparse(response['Location']).path == '/singleLogout'
    url = idp.process_logout_request_redirect(response.location)
    caplog.clear()
    freezer.move_to(datetime.timedelta(minutes=6))
    response = app.get(url)
    assert len(caplog.records) == 0, 'logout failed'
    assert response.location == '/somepath/'
    assert models.SessionIndex.objects.count() == 0


def test_sso_slo_update_of_new_fields(db, app, idp, caplog, sp_settings):
    response = app.get('/login/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    response = app.post(
        reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state}
    ).follow()
    # violent logout
    app.session.flush()

    # remove existing fields
    models.UserSAMLIdentifier.objects.all().update(
        nid_format=None, nid_name_qualifier=None, nid_sp_name_qualifier=None, nid_sp_provided_id=None
    )

    response = app.get('/login/')
    url, body, relay_state = idp.process_authn_request_redirect(response['Location'])
    response = app.post(
        reverse('mellon_login'), params={'SAMLResponse': body, 'RelayState': relay_state}
    ).follow()

    # check logout works
    response = app.get('/logout/')
    url = idp.process_logout_request_redirect(response.location)
    caplog.clear()
    response = app.get(url)
    assert len(caplog.records) == 0, 'logout failed'
