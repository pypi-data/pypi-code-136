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


import datetime
from unittest import mock

import lasso
from xml_utils import assert_xml_constraints

from mellon.models import Issuer
from mellon.models_utils import get_issuer
from mellon.utils import create_metadata, flatten_datetime, iso8601_to_datetime, make_session_dump
from mellon.views import check_next_url


def test_create_metadata(rf, private_settings, caplog):
    ns = {
        'sm': 'urn:oasis:names:tc:SAML:2.0:metadata',
        'ds': 'http://www.w3.org/2000/09/xmldsig#',
        'idpdisc': 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol',
    }
    private_settings.MELLON_PUBLIC_KEYS = ['xxx', '/yyy']
    private_settings.MELLON_NAME_ID_FORMATS = [lasso.SAML2_NAME_IDENTIFIER_FORMAT_UNSPECIFIED]
    private_settings.MELLON_DEFAULT_ASSERTION_CONSUMER_BINDING = 'artifact'
    request = rf.get('/')
    with mock.patch('mellon.utils.open', mock.mock_open(read_data='BEGIN\nyyy\nEND'), create=True):
        metadata = create_metadata(request)
    assert_xml_constraints(
        metadata.encode('utf-8'),
        (
            '/sm:EntityDescriptor[@entityID="http://testserver/metadata/"]',
            1,
            ('/*', 1),
            (
                '/sm:SPSSODescriptor',
                1,
                ('/*', 7),
                ('/sm:NameIDFormat', 1),
                ('/sm:SingleLogoutService', 2),
                (
                    '/sm:AssertionConsumerService[@isDefault=\'true\'][@Binding=\'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact\']',
                    1,
                ),
                (
                    '/sm:AssertionConsumerService[@isDefault=\'true\'][@Binding=\'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\']',
                    0,
                ),
                (
                    '/sm:AssertionConsumerService[@Binding=\'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\']',
                    1,
                ),
                (
                    '/sm:KeyDescriptor/ds:KeyInfo/ds:X509Data',
                    2,
                    ('/ds:X509Certificate', 2),
                    ('/ds:X509Certificate[text()=\'xxx\']', 1),
                    ('/ds:X509Certificate[text()=\'yyy\']', 1),
                ),
            ),
        ),
        namespaces=ns,
    )

    private_settings.MELLON_METADATA_PUBLISH_DISCOVERY_RESPONSE = True
    with mock.patch('mellon.utils.open', mock.mock_open(read_data='BEGIN\nyyy\nEND'), create=True):
        metadata = create_metadata(request)
    assert_xml_constraints(
        metadata.encode('utf-8'),
        (
            '/sm:EntityDescriptor[@entityID="http://testserver/metadata/"]',
            1,
            ('/*', 1),
            (
                '/sm:SPSSODescriptor',
                1,
                ('/*', 8),
                ('/sm:Extensions', 1, ('/idpdisc:DiscoveryResponse', 1)),
                ('/sm:NameIDFormat', 1),
                ('/sm:SingleLogoutService', 2),
                (
                    '/sm:AssertionConsumerService[@isDefault=\'true\'][@Binding=\'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact\']',
                    1,
                ),
                (
                    '/sm:AssertionConsumerService[@isDefault=\'true\'][@Binding=\'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\']',
                    0,
                ),
                (
                    '/sm:AssertionConsumerService[@Binding=\'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\']',
                    1,
                ),
                (
                    '/sm:KeyDescriptor/ds:KeyInfo/ds:X509Data',
                    2,
                    ('/ds:X509Certificate', 2),
                    ('/ds:X509Certificate[text()=\'xxx\']', 1),
                    ('/ds:X509Certificate[text()=\'yyy\']', 1),
                ),
            ),
        ),
        namespaces=ns,
    )

    private_settings.MELLON_ASSERTION_CONSUMER_BINDINGS = ['post']
    with mock.patch('mellon.utils.open', mock.mock_open(read_data='BEGIN\nyyy\nEND'), create=True):
        metadata = create_metadata(request)
    assert 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'
    assert_xml_constraints(
        metadata.encode('utf-8'),
        (
            '/sm:EntityDescriptor/sm:SPSSODescriptor',
            1,
            (
                '/sm:AssertionConsumerService[@Binding=\'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact\']',
                0,
            ),
            (
                '/sm:AssertionConsumerService[@Binding=\'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\']',
                1,
            ),
        ),
        namespaces=ns,
    )

    private_settings.MELLON_ASSERTION_CONSUMER_BINDINGS = ['artifact']
    with mock.patch('mellon.utils.open', mock.mock_open(read_data='BEGIN\nyyy\nEND'), create=True):
        metadata = create_metadata(request)
    assert 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'
    assert_xml_constraints(
        metadata.encode('utf-8'),
        (
            '/sm:EntityDescriptor/sm:SPSSODescriptor',
            1,
            (
                '/sm:AssertionConsumerService[@Binding=\'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact\']',
                1,
            ),
            (
                '/sm:AssertionConsumerService[@Binding=\'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\']',
                0,
            ),
        ),
        namespaces=ns,
    )


def test_iso8601_to_datetime(private_settings):
    import django.utils.timezone
    import pytz

    private_settings.TIME_ZONE = 'UTC'
    if hasattr(django.utils.timezone.get_default_timezone, 'cache_clear'):
        django.utils.timezone.get_default_timezone.cache_clear()
    django.utils.timezone._localtime = None
    private_settings.USE_TZ = False
    # UTC ISO8601 -> naive datetime UTC
    assert iso8601_to_datetime('2010-10-01T10:10:34Z') == datetime.datetime(2010, 10, 1, 10, 10, 34)
    # NAIVE ISO8601 -> naive datetime UTC
    assert iso8601_to_datetime('2010-10-01T10:10:34') == datetime.datetime(2010, 10, 1, 10, 10, 34)
    private_settings.USE_TZ = True
    # UTC+1h ISO8601 -> Aware datetime UTC
    assert iso8601_to_datetime('2010-10-01T10:10:34+01:00') == datetime.datetime(
        2010, 10, 1, 9, 10, 34, tzinfo=pytz.utc
    )
    # Naive ISO8601 -> Aware datetime UTC
    assert iso8601_to_datetime('2010-10-01T10:10:34') == datetime.datetime(
        2010, 10, 1, 10, 10, 34, tzinfo=pytz.utc
    )


def test_flatten_datetime():
    d = {
        'x': datetime.datetime(2010, 10, 10, 10, 10, 34),
        'y': 1,
        'z': 'u',
    }
    assert set(flatten_datetime(d).keys()) == {'x', 'y', 'z'}
    assert flatten_datetime(d)['x'] == '2010-10-10T10:10:34'
    assert flatten_datetime(d)['y'] == 1
    assert flatten_datetime(d)['z'] == 'u'


def test_check_next_url(rf):
    assert not check_next_url(rf.get('/'), '')
    assert not check_next_url(rf.get('/'), None)
    assert not check_next_url(rf.get('/'), '\x00')
    assert not check_next_url(rf.get('/'), '\u010e')
    assert not check_next_url(rf.get('/'), 'https://example.invalid/')
    # default hostname is testserver
    assert check_next_url(rf.get('/'), 'http://testserver/ok/')


def test_get_issuer_entity_id_migration(db, settings, metadata):
    entity_id1 = 'http://idp5/metadata'
    entity_id2 = 'http://idp6/metadata'
    settings.MELLON_IDENTITY_PROVIDERS = [
        {
            'METADATA': metadata,
        },
    ]
    issuer1 = get_issuer(entity_id1)
    assert issuer1.entity_id == entity_id1
    assert issuer1.slug is None

    settings.MELLON_IDENTITY_PROVIDERS = [
        {
            'METADATA': metadata,
            'SLUG': 'idp',
        },
    ]
    issuer2 = get_issuer(entity_id1)
    assert issuer2.id == issuer1.id
    assert issuer2.entity_id == entity_id1
    assert issuer2.slug == 'idp'

    settings.MELLON_IDENTITY_PROVIDERS = [
        {
            'METADATA': metadata.replace(entity_id1, entity_id2),
            'SLUG': 'idp',
        },
    ]
    issuer3 = get_issuer(entity_id2)
    assert issuer3.id == issuer1.id
    assert issuer3.entity_id == entity_id2
    assert issuer3.slug == 'idp'


def test_make_session_dump(db, django_user_model):
    from mellon.models import SessionIndex, UserSAMLIdentifier

    user = django_user_model.objects.create(username='user')
    issuer = Issuer.objects.create(entity_id='https://idp.example.com/metadata', slug='idp')
    saml_identifier = UserSAMLIdentifier.objects.create(
        user=user, name_id='1234', issuer=issuer, nid_format=lasso.SAML2_NAME_IDENTIFIER_FORMAT_PERSISTENT
    )

    for i in range(2):
        SessionIndex.objects.create(session_index=str(i), saml_identifier=saml_identifier, session_key='abcd')

    assert (
        make_session_dump(saml_identifier.sessionindex_set.all())
        == '''\
<ns0:Session xmlns:ns0="http://www.entrouvert.org/namespaces/lasso/0.0" xmlns:ns1="urn:oasis:names:tc:SAML:2.0:assertion" Version="2">
<ns0:NidAndSessionIndex AssertionID="" ProviderID="https://idp.example.com/metadata" SessionIndex="0">
<ns1:NameID Format="urn:oasis:names:tc:SAML:2.0:nameid-format:persistent">1234</ns1:NameID>
</ns0:NidAndSessionIndex>
<ns0:NidAndSessionIndex AssertionID="" ProviderID="https://idp.example.com/metadata" SessionIndex="1">
<ns1:NameID Format="urn:oasis:names:tc:SAML:2.0:nameid-format:persistent">1234</ns1:NameID>
</ns0:NidAndSessionIndex>
</ns0:Session>
'''
    )
