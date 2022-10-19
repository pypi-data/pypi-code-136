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
import importlib
import logging
from functools import wraps
from urllib.parse import urlparse
from xml.parsers import expat

import isodate
import lasso
from django.conf import settings
from django.contrib import auth
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.timezone import get_default_timezone, is_aware, make_aware, make_naive, now

from . import app_settings

logger = logging.getLogger(__name__)


class CreateServerError(Exception):
    pass


def create_metadata(request):
    entity_id = reverse('mellon_metadata')
    login_url = reverse(app_settings.LOGIN_URL)
    logout_url = reverse(app_settings.LOGOUT_URL)
    public_keys = []
    for public_key in app_settings.PUBLIC_KEYS:
        if public_key.startswith('/'):
            # clean PEM file
            content = open(public_key).read()
            public_key = ''.join(content.splitlines()[1:-1])
        public_keys.append(public_key)
    name_id_formats = app_settings.NAME_ID_FORMATS
    ctx = {
        'request': request,
        'entity_id': request.build_absolute_uri(entity_id),
        'login_url': request.build_absolute_uri(login_url),
        'logout_url': request.build_absolute_uri(logout_url),
        'public_keys': public_keys,
        'name_id_formats': name_id_formats,
        'assertion_consumer_bindings': app_settings.ASSERTION_CONSUMER_BINDINGS,
        'default_assertion_consumer_binding': app_settings.DEFAULT_ASSERTION_CONSUMER_BINDING,
        'organization': app_settings.ORGANIZATION,
        'contact_persons': app_settings.CONTACT_PERSONS,
    }
    if app_settings.METADATA_PUBLISH_DISCOVERY_RESPONSE:
        ctx['discovery_endpoint_url'] = request.build_absolute_uri(reverse('mellon_login'))
    return render_to_string('mellon/metadata.xml', ctx)


def create_server(request):
    root = request.build_absolute_uri('/')
    cache = getattr(settings, '_MELLON_SERVER_CACHE', {})
    if root not in cache:
        metadata = create_metadata(request)
        if app_settings.PRIVATE_KEY:
            private_key = app_settings.PRIVATE_KEY
            private_key_password = app_settings.PRIVATE_KEY_PASSWORD
        elif app_settings.PRIVATE_KEYS:
            private_key = app_settings.PRIVATE_KEYS[0]
            private_key_password = None
            if isinstance(private_key, (tuple, list)):
                private_key_password = private_key[1]
                private_key = private_key[0]
        else:  # no signature
            private_key = None
            private_key_password = None
        server = lasso.Server.newFromBuffers(
            metadata, private_key_content=private_key, private_key_password=private_key_password
        )
        if not server:
            raise CreateServerError
        if app_settings.SIGNATURE_METHOD:
            symbol_name = 'SIGNATURE_METHOD_' + app_settings.SIGNATURE_METHOD.replace('-', '_').upper()
            if hasattr(lasso, symbol_name):
                server.signatureMethod = getattr(lasso, symbol_name)
            else:
                logger.warning('mellon: unable to set signature method %s', app_settings.SIGNATURE_METHOD)

        server.setEncryptionPrivateKeyWithPassword(private_key, private_key_password)
        private_keys = app_settings.PRIVATE_KEYS
        # skip first key if it is already loaded
        if not app_settings.PRIVATE_KEY:
            private_keys = app_settings.PRIVATE_KEYS[1:]
        for key in private_keys:
            password = None
            if isinstance(key, (tuple, list)):
                password = key[1]
                key = key[0]
            server.setEncryptionPrivateKeyWithPassword(key, password)
        for idp in get_idps():
            if idp and idp.get('METADATA'):
                try:
                    server.addProviderFromBuffer(lasso.PROVIDER_ROLE_IDP, idp['METADATA'])
                except lasso.Error as e:
                    logger.error('bad metadata in idp %s, %s', idp['ENTITY_ID'], e)
        cache[root] = server
        settings._MELLON_SERVER_CACHE = cache
    return cache.get(root)


def create_login(request):
    server = create_server(request)
    login = lasso.Login(server)
    if not app_settings.PRIVATE_KEY and not app_settings.PRIVATE_KEYS:
        login.setSignatureHint(lasso.PROFILE_SIGNATURE_HINT_FORBID)
    return login


def get_idp(entity_id):
    for adapter in get_adapters():
        if hasattr(adapter, 'get_idp'):
            idp = adapter.get_idp(entity_id)
            if idp:
                return idp
    return {}


def get_idps():
    for adapter in get_adapters():
        if hasattr(adapter, 'get_idps'):
            yield from adapter.get_idps()


def flatten_datetime(d):
    d = d.copy()
    for key, value in d.items():
        if isinstance(value, datetime.datetime):
            d[key] = value.isoformat()
    return d


def iso8601_to_datetime(date_string, default=None):
    """Convert a string formatted as an ISO8601 date into a datetime
    value.

    This function ignores the sub-second resolution"""
    try:
        dt = isodate.parse_datetime(date_string)
    except Exception:
        return default
    if is_aware(dt):
        if not settings.USE_TZ:
            dt = make_naive(dt, get_default_timezone())
    else:
        if settings.USE_TZ:
            dt = make_aware(dt, get_default_timezone())
    return dt


def get_seconds_expiry(datetime_expiry):
    return (datetime_expiry - now()).total_seconds()


def to_list(func):
    @wraps(func)
    def f(*args, **kwargs):
        return list(func(*args, **kwargs))

    return f


def import_object(path):
    module, name = path.rsplit('.', 1)
    module = importlib.import_module(module)
    return getattr(module, name)


@to_list
def get_adapters(idp={}, **kwargs):
    idp = idp or {}
    adapters = tuple(idp.get('ADAPTER', ())) + tuple(app_settings.ADAPTER)
    for adapter in adapters:
        klass = import_object(adapter)
        yield klass(**kwargs)


def get_values(saml_attributes, name):
    values = saml_attributes.get(name)
    if values is None:
        return ()
    if not isinstance(values, (list, tuple)):
        return (values,)
    return values


def get_setting(idp, name, default=None):
    """Get a parameter from an IdP specific configuration or from the main
    settings.
    """
    return idp.get(name) or getattr(app_settings, name, default)


def make_session_dump(session_indexes):
    return render_to_string('mellon/session_dump.xml', {'session_indexes': session_indexes})


def create_logout(request):
    server = create_server(request)
    logout = lasso.Logout(server)
    if not app_settings.PRIVATE_KEY and not app_settings.PRIVATE_KEYS:
        logout.setSignatureHint(lasso.PROFILE_SIGNATURE_HINT_FORBID)
    return logout


def is_nonnull(s):
    return '\x00' not in s


PROTOCOLS_TO_PORT = {
    'http': '80',
    'https': '443',
}


def netloc_to_host_port(netloc):
    if not netloc:
        return None, None
    splitted = netloc.split(':', 1)
    if len(splitted) > 1:
        return splitted[0], splitted[1]
    return splitted[0], None


def same_domain(domain1, domain2):
    if domain1 == domain2:
        return True

    if not domain1 or not domain2:
        return False

    if domain2.startswith('.'):
        # p1 is a sub-domain or the base domain
        if domain1.endswith(domain2) or domain1 == domain2[1:]:
            return True
    return False


def same_origin(url1, url2):
    """Checks if both URL use the same domain. It understands domain patterns on url2, i.e. .example.com
    matches www.example.com.

    If not scheme is given in url2, scheme compare is skipped.
    If not scheme and not port are given, port compare is skipped.
    The last two rules allow authorizing complete domains easily.
    """
    p1, p2 = urlparse(url1), urlparse(url2)
    p1_host, p1_port = netloc_to_host_port(p1.netloc)
    p2_host, p2_port = netloc_to_host_port(p2.netloc)

    # url2 is relative, always same domain
    if url2.startswith('/') and not url2.startswith('//'):
        return True

    if p2.scheme and p1.scheme != p2.scheme:
        return False

    if not same_domain(p1_host, p2_host):
        return False

    try:
        if (p2_port or (p1_port and p2.scheme)) and (
            (p1_port or PROTOCOLS_TO_PORT[p1.scheme]) != (p2_port or PROTOCOLS_TO_PORT[p2.scheme])
        ):
            return False
    except (ValueError, KeyError):
        return False

    return True


def get_status_codes_and_message(profile):
    assert profile, 'missing lasso.Profile'
    assert profile.response, 'missing response in profile'
    assert profile.response.status, 'missing status in response'

    from .views import lasso_decode

    status_codes = []

    status = profile.response.status
    a = status
    while a.statusCode:
        status_codes.append(lasso_decode(a.statusCode.value))
        a = a.statusCode
    message = None
    if status.statusMessage:
        message = lasso_decode(status.statusMessage)
    return status_codes, message


def login(request, user):
    for adapter in get_adapters():
        if hasattr(adapter, 'auth_login'):
            adapter.auth_login(request, user)
            break
    else:
        auth.login(request, user)


def get_xml_encoding(content):
    xml_encoding = 'utf-8'

    def xmlDeclHandler(version, encoding, standalone):
        global xml_encoding

        if encoding:
            xml_encoding = encoding

    parser = expat.ParserCreate()
    parser.XmlDeclHandler = xmlDeclHandler
    try:
        parser.Parse(content, True)
    except expat.ExpatError as e:
        raise ValueError('invalid XML %s' % e)
    return xml_encoding


def get_local_path(request, url):
    if not url:
        return
    parsed = urlparse(url)
    path = parsed.path
    if request.META.get('SCRIPT_NAME'):
        path = path[len(request.META['SCRIPT_NAME']) :]
    return path
