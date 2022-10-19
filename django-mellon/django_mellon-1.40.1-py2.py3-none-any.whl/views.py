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


import logging
import uuid
import xml.etree.ElementTree as ET
from contextlib import contextmanager, nullcontext
from importlib import import_module
from io import StringIO
from xml.sax.saxutils import escape

import django.http
import lasso
import requests
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.core import signing
from django.db import transaction
from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.http import urlencode
from django.utils.timezone import now
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.views.generic.base import RedirectView
from requests.exceptions import RequestException

from . import app_settings, models, models_utils, utils

RETRY_LOGIN_COOKIE = 'MELLON_RETRY_LOGIN'

lasso.setFlag('thin-sessions')


def lasso_decode(x):
    return x


EO_NS = 'https://www.entrouvert.com/'
LOGIN_HINT = '{%s}login-hint' % EO_NS

User = get_user_model()


class HttpResponseBadRequest(django.http.HttpResponseBadRequest):
    def __init__(self, *args, **kwargs):
        kwargs['content_type'] = kwargs.get('content_type', 'text/plain')
        super().__init__(*args, **kwargs)
        self['X-Content-Type-Options'] = 'nosniff'


class LogMixin:
    """Initialize a module logger in new objects"""

    def __init__(self, *args, **kwargs):
        self.log = logging.getLogger(__name__)
        super().__init__(*args, **kwargs)


def check_next_url(request, next_url):
    log = logging.getLogger(__name__)
    if not next_url:
        return
    if not utils.is_nonnull(next_url):
        log.warning('next parameter ignored, as it contains null characters')
        return
    try:
        next_url.encode('ascii')
    except UnicodeError:
        log.warning('next parameter ignored, as is\'s not an ASCII string')
        return
    if not utils.same_origin(request.build_absolute_uri(), next_url):
        log.warning('next parameter ignored as it is not of the same origin')
        return
    return next_url


class ProfileMixin:
    profile = None

    def set_next_url(self, next_url):
        if not check_next_url(self.request, next_url):
            return
        self.set_state('next_url', next_url)

    def set_state(self, name, value):
        assert self.profile
        relay_state = self.get_relay_state(create=True)
        self.request.session['mellon_%s_%s' % (name, relay_state)] = value

    def get_state(self, name, default=None):
        if self.profile:
            relay_state = self.get_relay_state()
            key = 'mellon_%s_%s' % (name, relay_state)
            return self.request.session.get(key, default)
        return default

    def get_relay_state(self, create=False):
        if self.profile and self.profile.msgRelayState:
            try:
                return uuid.UUID(self.profile.msgRelayState)
            except ValueError:
                pass
        if create:
            assert self.profile
            self.profile.msgRelayState = str(uuid.uuid4())
            return self.profile.msgRelayState

    def get_next_url(self, default=None):
        return self.get_state('next_url', default=default)

    def show_message_status_is_not_success(self, profile, prefix):
        status_codes, idp_message = utils.get_status_codes_and_message(profile)
        args = ['%s: status is not success codes: %r', prefix, status_codes]
        if idp_message:
            args[0] += ' message: %s'
            args.append(idp_message)
        self.log.warning(*args)

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except utils.CreateServerError:
            return self.failure(
                request,
                reason=_(
                    'Unable to initialize a SAML server object, the private key '
                    'is maybe invalid or unreadable, please check its access '
                    'rights and content.'
                ),
            )

    def failure(self, request, reason='', status_codes=()):
        '''show error message to user after a login failure'''
        login = self.profile
        idp = utils.get_idp(login and login.remoteProviderId)
        if not idp and login:
            self.log.warning('entity id %r is unknown', login.remoteProviderId)
            return HttpResponseBadRequest('entity id %r is unknown' % login.remoteProviderId)
        error_url = utils.get_setting(idp, 'ERROR_URL')
        error_redirect_after_timeout = utils.get_setting(idp, 'ERROR_REDIRECT_AFTER_TIMEOUT')
        if error_url:
            error_url = resolve_url(error_url)
        next_url = error_url or self.get_next_url(default=resolve_url(settings.LOGIN_REDIRECT_URL))
        return self.render(
            request,
            'mellon/authentication_failed.html',
            {
                'debug': settings.DEBUG,
                'reason': reason,
                'status_codes': status_codes,
                'issuer': login and login.remoteProviderId,
                'next_url': next_url,
                'relaystate': login and login.msgRelayState,
                'error_redirect_after_timeout': error_redirect_after_timeout,
            },
        )


class LoginView(ProfileMixin, LogMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.debug_login = request.session.get('mellon_debug_login')
        with self.capture_logs() if self.debug_login else nullcontext():
            return super().dispatch(request, *args, **kwargs)

    @property
    def template_base(self):
        return self.kwargs.get('template_base', 'base.html')

    def render(self, request, template_names, context):
        context['template_base'] = self.template_base
        if 'context_hook' in self.kwargs:
            self.kwargs['context_hook'](context)
        return render(request, template_names, context)

    def get_idp(self, request):
        entity_id = request.POST.get('entityID') or request.GET.get('entityID')
        if not entity_id:
            for idp in utils.get_idps():
                return idp
            else:
                return {}
        else:
            return utils.get_idp(entity_id)

    def post(self, request, *args, **kwargs):
        '''Assertion consumer'''
        if 'SAMLart' in request.POST:
            if 'artifact' not in app_settings.ASSERTION_CONSUMER_BINDINGS:
                raise Http404('artifact binding is not supported')
            return self.continue_sso_artifact(request, lasso.HTTP_METHOD_ARTIFACT_POST)
        if 'SAMLResponse' not in request.POST:
            if 'post' not in app_settings.ASSERTION_CONSUMER_BINDINGS:
                raise Http404('post binding is not supported')
            return self.get(request, *args, **kwargs)
        if not utils.is_nonnull(request.POST['SAMLResponse']):
            return HttpResponseBadRequest('SAMLResponse contains a null character')
        self.log.info('Got SAML Response', extra={'saml_response': request.POST['SAMLResponse']})
        self.profile = login = utils.create_login(request)
        idp_message = None
        status_codes = []
        # prevent null characters in SAMLResponse
        try:
            login.processAuthnResponseMsg(request.POST['SAMLResponse'])
            login.acceptSso()
        except lasso.ProfileCannotVerifySignatureError:
            self.log.warning(
                'SAML authentication failed: signature validation failed for %r', login.remoteProviderId
            )
        except lasso.ParamError:
            self.log.exception('lasso param error')
        except (
            lasso.LoginStatusNotSuccessError,
            lasso.ProfileStatusNotSuccessError,
            lasso.ProfileRequestDeniedError,
        ):
            self.show_message_status_is_not_success(login, 'SAML authentication failed')
        except lasso.Error as e:
            if self.debug_login:
                return self.render_debug_template(request, login)
            return HttpResponseBadRequest('error processing the authentication response: %r' % e)
        else:
            if 'RelayState' in request.POST and utils.is_nonnull(request.POST['RelayState']):
                login.msgRelayState = request.POST['RelayState']
            return self.sso_success(request, login)
        return self.failure(request, reason=idp_message, status_codes=status_codes)

    def get_attribute_value(self, attribute, attribute_value):
        # check attribute_value contains only text
        for node in attribute_value.any:
            if not isinstance(node, lasso.MiscTextNode) or not node.textChild:
                self.log.warning('unsupported attribute %s', attribute.exportToXml())
                return None
        return ''.join(lasso_decode(node.content) for node in attribute_value.any)

    def sso_success(self, request, login):
        attributes = {}
        attribute_statements = login.assertion.attributeStatement
        for ats in attribute_statements:
            for at in ats.attribute:
                values = attributes.setdefault(at.name, [])
                for attribute_value in at.attributeValue:
                    content = self.get_attribute_value(at, attribute_value)
                    if content is not None:
                        values.append(content)
        entity_id = attributes['issuer'] = login.remoteProviderId
        in_response_to = login.response.inResponseTo
        if in_response_to:
            attributes['nonce'] = request.session.get('mellon-nonce-%s' % in_response_to)
            attributes['force_authn'] = request.session.get('mellon-force-authn-%s' % in_response_to, False)

        if login.nameIdentifier:
            name_id = login.nameIdentifier
            name_id_format = force_str(name_id.format or lasso.SAML2_NAME_IDENTIFIER_FORMAT_UNSPECIFIED)
            attributes.update(
                {
                    'name_id_content': lasso_decode(name_id.content),
                    'name_id_format': name_id_format,
                }
            )
            if name_id.nameQualifier:
                attributes['name_id_name_qualifier'] = force_str(name_id.nameQualifier)
            if name_id.spNameQualifier:
                attributes['name_id_sp_name_qualifier'] = force_str(name_id.spNameQualifier)
            if name_id.spProvidedId:
                attributes['name_id_provided_id'] = force_str(name_id.spProvidedId)
        authn_statement = login.assertion.authnStatement[0]
        if authn_statement.authnInstant:
            attributes['authn_instant'] = utils.iso8601_to_datetime(authn_statement.authnInstant)
        if authn_statement.sessionNotOnOrAfter:
            attributes['session_not_on_or_after'] = utils.iso8601_to_datetime(
                authn_statement.sessionNotOnOrAfter
            )
        if authn_statement.sessionIndex:
            attributes['session_index'] = authn_statement.sessionIndex
        attributes['authn_context_class_ref'] = ()
        if authn_statement.authnContext:
            authn_context = authn_statement.authnContext
            if authn_context.authnContextClassRef:
                attributes['authn_context_class_ref'] = authn_context.authnContextClassRef
        self.log.debug('trying to authenticate with attributes %r', attributes)
        response = self.authenticate(request, login, attributes)
        response.delete_cookie(RETRY_LOGIN_COOKIE)
        if self.debug_login:
            return self.render_debug_template(request, login, attributes)
        return response

    def authenticate(self, request, login, attributes):
        user = auth.authenticate(
            request=request, issuer=models_utils.get_issuer(attributes['issuer']), saml_attributes=attributes
        )
        next_url = self.get_next_url(default=resolve_url(settings.LOGIN_REDIRECT_URL))
        if user is not None:
            if user.is_active:
                self.login(user, attributes)
            else:
                self.log.warning(
                    'user %s (NameID is %r) is inactive, login refused', user, attributes['name_id_content']
                )
                return self.render(
                    request, 'mellon/inactive_user.html', {'user': user, 'saml_attributes': attributes}
                )
        else:
            self.log.warning('no user found for NameID %r', attributes['name_id_content'])
            return self.render(request, 'mellon/user_not_found.html', {'saml_attributes': attributes})
        return HttpResponseRedirect(next_url)

    def render_debug_template(self, request, login, attributes=None):
        request.session['mellon_debug_login'] = False
        context = {
            'logs': self.stream.getvalue(),
            'attributes': attributes,
            'login': login,
            'response_dump': login.response and login.response.debug(4),
            'assertion_dump': login.assertion and login.assertion.debug(4),
        }
        self.log.info('mellon: debug login attributes %s', attributes)
        self.log.info('mellon: debug login assertion_dump %s', context['assertion_dump'])
        self.log.info('mellon: debug login response_dump %s', context['response_dump'])
        return self.render(request, 'mellon/debug_login.html', context)

    def login(self, user, attributes):
        if self.debug_login:
            self.log.info('mellon: would login user %s (username %s)', user.get_full_name(), user)
            return

        utils.login(self.request, user)
        if (
            app_settings.OPENED_SESSION_COOKIE_NAME
            and app_settings.OPENED_SESSION_COOKIE_NAME in self.request.COOKIES
        ):
            self.request.session['mellon_opened_session_cookie'] = self.request.COOKIES[
                app_settings.OPENED_SESSION_COOKIE_NAME
            ]
        session_index = attributes['session_index']
        if session_index:
            if not self.request.session.session_key:
                self.request.session.create()
            models.SessionIndex.objects.get_or_create(
                saml_identifier=user.saml_identifier,
                session_key=self.request.session.session_key,
                session_index=session_index,
                # keep transient nameid to be able to produce logout requests
                transient_name_id=attributes['name_id_content']
                if attributes['name_id_format'] == lasso.SAML2_NAME_IDENTIFIER_FORMAT_TRANSIENT
                else None,
            )
        self.log.info('user %s (NameID is %r) logged in using SAML', user, attributes['name_id_content'])
        self.request.session['mellon_session'] = utils.flatten_datetime(attributes)
        if 'session_not_on_or_after' in attributes and not settings.SESSION_EXPIRE_AT_BROWSER_CLOSE:
            self.request.session.set_expiry(utils.get_seconds_expiry(attributes['session_not_on_or_after']))

    def retry_login(self):
        """Retry login if it failed for a temporary error.

        Use a cookie to prevent looping forever.
        """
        if RETRY_LOGIN_COOKIE in self.request.COOKIES:
            response = self.failure(
                self.request, reason=_('There were too many redirections with the identity provider.')
            )
            response.delete_cookie(RETRY_LOGIN_COOKIE)
            return response
        url = reverse('mellon_login')
        next_url = self.get_next_url()
        if next_url:
            url = '%s?%s' % (url, urlencode({REDIRECT_FIELD_NAME: next_url}))
        response = HttpResponseRedirect(url)
        response.set_cookie(RETRY_LOGIN_COOKIE, value='1', max_age=None)
        return response

    def continue_sso_artifact(self, request, method):
        idp_message = None
        status_codes = []

        if method == lasso.HTTP_METHOD_ARTIFACT_GET:
            message = request.META['QUERY_STRING']
            artifact = request.GET['SAMLart']
            relay_state = request.GET.get('RelayState')
        else:  # method == lasso.HTTP_METHOD_ARTIFACT_POST:
            message = request.POST['SAMLart']
            artifact = request.POST['SAMLart']
            relay_state = request.POST.get('RelayState')

        self.profile = login = utils.create_login(request)
        if relay_state and utils.is_nonnull(relay_state):
            login.msgRelayState = relay_state
        try:
            login.initRequest(message, method)
        except lasso.ProfileInvalidArtifactError:
            self.log.warning('artifact is malformed %r', artifact)
            return HttpResponseBadRequest('artifact is malformed %r' % artifact)
        except lasso.ServerProviderNotFoundError:
            self.log.warning('no entity id found for artifact %s', artifact)
            return HttpResponseBadRequest('no entity id found for this artifact %r' % artifact)
        idp = utils.get_idp(login.remoteProviderId)
        if not idp:
            return HttpResponseBadRequest('entity id %r is unknown' % login.remoteProviderId)
        verify_ssl_certificate = utils.get_setting(idp, 'VERIFY_SSL_CERTIFICATE')
        login.buildRequestMsg()
        try:
            result = requests.post(
                login.msgUrl,
                data=login.msgBody,
                headers={'content-type': 'text/xml'},
                timeout=app_settings.ARTIFACT_RESOLVE_TIMEOUT,
                verify=verify_ssl_certificate,
            )
        except RequestException as e:
            self.log.warning('unable to reach %r: %s', login.msgUrl, e)
            return self.failure(
                request,
                reason=_('IdP is temporarily down, please try again ' 'later.'),
                status_codes=status_codes,
            )
        if result.status_code != 200:
            self.log.warning(
                'SAML authentication failed: IdP returned %s when given artifact: %r',
                result.status_code,
                result.content,
            )
            return self.failure(request, reason=idp_message, status_codes=status_codes)

        self.log.info('Got SAML Artifact Response', extra={'saml_response': result.content})
        result.encoding = utils.get_xml_encoding(result.content)
        try:
            login.processResponseMsg(result.text)
            login.acceptSso()
        except lasso.ProfileMissingResponseError:
            # artifact is invalid, idp returned no response
            self.log.warning('ArtifactResolveResponse is empty: dead artifact %r', artifact)
            return self.retry_login()
        except lasso.ProfileInvalidMsgError:
            self.log.warning('ArtifactResolveResponse is malformed %r', result.content[:200])
            if settings.DEBUG:
                return HttpResponseBadRequest('ArtififactResolveResponse is malformed\n%r' % result.content)
            else:
                return HttpResponseBadRequest('ArtififactResolveResponse is malformed')
        except lasso.ProfileCannotVerifySignatureError:
            self.log.warning(
                'SAML authentication failed: signature validation failed for %r', login.remoteProviderId
            )
        except lasso.ParamError:
            self.log.exception('lasso param error')
        except (
            lasso.LoginStatusNotSuccessError,
            lasso.ProfileStatusNotSuccessError,
            lasso.ProfileRequestDeniedError,
        ):
            status = login.response.status
            a = status
            while a.statusCode:
                status_codes.append(a.statusCode.value)
                a = a.statusCode
            args = ['SAML authentication failed: status is not success codes: %r', status_codes]
            if status.statusMessage:
                idp_message = lasso_decode(status.statusMessage)
                args[0] += ' message: %r'
                args.append(status.statusMessage)
            self.log.warning(*args)
        except lasso.Error as e:
            self.log.exception('unexpected lasso error')
            return HttpResponseBadRequest('error processing the authentication response: %r' % e)
        else:
            return self.sso_success(request, login)
        return self.failure(request, reason=idp_message, status_codes=status_codes)

    def request_discovery_service(self, request, is_passive=False):
        return_url = request.build_absolute_uri()
        return_url += '&' if '?' in return_url else '?'
        return_url += 'nodisco=1'
        url = app_settings.DISCOVERY_SERVICE_URL
        params = {
            # prevent redirect loops with the discovery service
            'entityID': request.build_absolute_uri(reverse('mellon_metadata')),
            'return': return_url,
        }
        if is_passive:
            params['isPassive'] = 'true'
        url += '?' + urlencode(params)
        return HttpResponseRedirect(url)

    def get(self, request, *args, **kwargs):
        '''Initialize login request'''
        if 'SAMLart' in request.GET:
            if 'artifact' not in app_settings.ASSERTION_CONSUMER_BINDINGS:
                raise Http404('artifact binding is not supported')
            return self.continue_sso_artifact(request, lasso.HTTP_METHOD_ARTIFACT_GET)

        # redirect to discovery service if needed
        if (
            'entityID' not in request.GET
            and 'nodisco' not in request.GET
            and app_settings.DISCOVERY_SERVICE_URL
        ):
            return self.request_discovery_service(request, is_passive=request.GET.get('passive') == '1')

        next_url = check_next_url(self.request, request.GET.get(REDIRECT_FIELD_NAME))
        idp = self.get_idp(request)
        if not idp:
            return HttpResponseBadRequest('no idp found')
        self.profile = login = utils.create_login(request)
        self.log.debug('authenticating to %r', idp['ENTITY_ID'])
        try:
            login.initAuthnRequest(idp['ENTITY_ID'], lasso.HTTP_METHOD_REDIRECT)
            authn_request = login.request
            # configure NameID policy
            policy = authn_request.nameIdPolicy
            policy.allowCreate = utils.get_setting(idp, 'NAME_ID_POLICY_ALLOW_CREATE')
            policy.format = utils.get_setting(idp, 'NAME_ID_POLICY_FORMAT')
            force_authn = utils.get_setting(idp, 'FORCE_AUTHN') or 'force-authn' in request.GET
            # link the nonce and forceAuthn state to the request-id
            if 'nonce' in request.GET:
                request.session['mellon-nonce-%s' % authn_request.id] = request.GET['nonce']
            if force_authn:
                request.session['mellon-force-authn-%s' % authn_request.id] = True
                authn_request.forceAuthn = True
            if request.GET.get('passive') == '1':
                authn_request.isPassive = True
            # configure requested AuthnClassRef
            authn_classref = utils.get_setting(idp, 'AUTHN_CLASSREF')
            if authn_classref:
                authn_classref = tuple(str(x) for x in authn_classref)
                req_authncontext = lasso.Samlp2RequestedAuthnContext()
                authn_request.requestedAuthnContext = req_authncontext
                req_authncontext.authnContextClassRef = authn_classref

            if utils.get_setting(idp, 'ADD_AUTHNREQUEST_NEXT_URL_EXTENSION'):
                authn_request.extensions = lasso.Samlp2Extensions()
                eo_next_url = escape(request.build_absolute_uri(next_url or '/'))
                # lasso>2.5.1 introduced a better API
                if hasattr(authn_request.extensions, 'any'):
                    authn_request.extensions.any = (
                        str(
                            '<eo:next_url xmlns:eo="https://www.entrouvert.com/">%s</eo:next_url>'
                            % eo_next_url
                        ),
                    )
                else:
                    authn_request.extensions.setOriginalXmlnode(
                        str(
                            '''<samlp:Extensions
                                 xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
                                 xmlns:eo="https://www.entrouvert.com/">
                               <eo:next_url>%s</eo:next_url>
                            </samlp:Extensions>'''
                            % eo_next_url
                        )
                    )
            self.set_next_url(next_url)
            self.add_login_hints(idp, authn_request, request=request, next_url=next_url or '/')
            login.buildAuthnRequestMsg()
        except lasso.Error as e:
            return HttpResponseBadRequest('error initializing the authentication request: %r' % e)
        self.log.debug('sending authn request %r', authn_request.dump())
        self.log.debug('to url %r', login.msgUrl)
        return HttpResponseRedirect(login.msgUrl)

    def add_extension_node(self, authn_request, node):
        '''Factorize adding an XML node to the samlp:Extensions node'''
        if not authn_request.extensions:
            authn_request.extensions = lasso.Samlp2Extensions()
        assert hasattr(authn_request.extensions, 'any'), 'extension nodes need lasso > 2.5.1'
        serialized = ET.tostring(node, 'utf-8')
        # tostring return bytes in PY3, but lasso needs str
        serialized = serialized.decode('utf-8')
        extension_content = authn_request.extensions.any or ()
        extension_content += (serialized,)
        authn_request.extensions.any = extension_content

    def is_in_backoffice(self, request, next_url):
        path = utils.get_local_path(request, next_url)
        return path and path.startswith(('/admin/', '/manage/', '/manager/'))

    def add_login_hints(self, idp, authn_request, request, next_url=None):
        login_hints = utils.get_setting(idp, 'LOGIN_HINTS', [])
        hints = []
        for login_hint in login_hints:
            if login_hint == 'backoffice':
                if next_url and self.is_in_backoffice(request, next_url):
                    hints.append('backoffice')
            if login_hint == 'always_backoffice':
                hints.append('backoffice')

        for hint in hints:
            node = ET.Element(LOGIN_HINT)
            node.text = hint
            self.add_extension_node(authn_request, node)

    @contextmanager
    def capture_logs(self):
        self.stream = StringIO()
        handler = logging.StreamHandler(self.stream)
        handler.setLevel(logging.DEBUG)
        self.log.root.addHandler(handler)
        try:
            yield
        finally:
            self.log.root.removeHandler(handler)


# we need fine control of transactions to prevent double user creations
login = transaction.non_atomic_requests(csrf_exempt(LoginView.as_view()))


class LogoutView(ProfileMixin, LogMixin, View):
    def get(self, request, *args, logout_next_url='/', **kwargs):
        if 'token' in request.GET:
            return self.sp_logout_token(request, token=request.GET['token'], logout_next_url=logout_next_url)
        elif 'SAMLRequest' in request.GET:
            return self.idp_logout(request, request.META['QUERY_STRING'], 'redirect')
        elif 'SAMLResponse' in request.GET:
            return self.sp_logout_response(request, logout_next_url=logout_next_url)
        else:
            return self.sp_logout_request(request, logout_next_url=logout_next_url)

    def post(self, request, *args, **kwargs):
        return self.idp_logout(request, force_str(request.body), 'soap')

    def logout(self, request, saml_user, session_indexes, indexes, mode):
        session_keys = set(indexes.values_list('session_key', flat=True))
        indexes.delete()

        synchronous_logout = request.user == saml_user
        asynchronous_logout = (
            mode == 'soap'
            # the current session is not the only killed
            or len(session_keys) != 1
            or (
                # there is not current session
                not request.user.is_authenticated
                # or the current session is not part of the list
                or request.session.session_key not in session_keys
            )
        )

        if asynchronous_logout:
            current_session_key = request.session.session_key if request.user.is_authenticated else None

            session_engine = import_module(settings.SESSION_ENGINE)
            store = session_engine.SessionStore()

            count = 0
            for session_key in session_keys:
                if session_key != current_session_key:
                    try:
                        store.delete(session_key)
                        count += 1
                    except Exception:
                        self.log.warning('could not delete session_key %s', session_key, exc_info=True)
            if not session_indexes:
                self.log.info('asynchronous logout of all sessions of user %s', saml_user)
            elif count:
                self.log.info('asynchronous logout of %d sessions of user %s', len(session_keys), saml_user)

        if synchronous_logout:
            user = request.user
            auth.logout(request)
            self.log.info('synchronous logout of %s', user)

    def idp_logout(self, request, msg, mode):
        '''Handle logout request emitted by the IdP'''
        self.profile = logout = utils.create_logout(request)
        try:
            logout.processRequestMsg(msg)
        except lasso.Error as e:
            return HttpResponseBadRequest('error processing logout request: %r' % e)

        entity_id = force_str(logout.remoteProviderId)
        session_indexes = {force_str(sessionIndex) for sessionIndex in logout.request.sessionIndexes}

        saml_identifier = (
            models.UserSAMLIdentifier.objects.filter(
                name_id=force_str(logout.nameIdentifier.content),
                issuer=models_utils.get_issuer(entity_id),
            )
            .select_related('user', 'issuer')
            .first()
        )

        if saml_identifier:
            name_id_user = saml_identifier.user
            indexes = models.SessionIndex.objects.select_related('saml_identifier').filter(
                saml_identifier=saml_identifier
            )
            if session_indexes:
                indexes = indexes.filter(session_index__in=session_indexes)

            # lasso has too much state :/
            logout.setSessionFromDump(utils.make_session_dump(indexes))

            try:
                logout.validateRequest()
            except lasso.Error as e:
                self.log.warning('error validating logout request: %r' % e)
            else:
                if session_indexes:
                    self.log.info('logout requested for sessionIndexes %s', session_indexes)
                else:
                    self.log.info('full logout requested, no sessionIndexes')
                self.logout(
                    request,
                    saml_user=name_id_user,
                    session_indexes=session_indexes,
                    indexes=indexes,
                    mode=mode,
                )

        try:
            logout.buildResponseMsg()
        except lasso.Error as e:
            return HttpResponseBadRequest('error processing logout request: %r' % e)
        if logout.msgBody:
            return HttpResponse(force_str(logout.msgBody), content_type='text/xml')
        else:
            return HttpResponseRedirect(logout.msgUrl)

    def next_url_cookie_name(self, relaystate):
        return f'MellonNextURL-{relaystate}'

    def sp_logout_request(self, request, logout_next_url=None):
        '''Launch a logout request to the identity provider'''
        referer = request.headers.get('Referer')
        field_next_url = request.GET.get(REDIRECT_FIELD_NAME)
        next_url = None
        if field_next_url and utils.same_origin(request.build_absolute_uri(), field_next_url):
            next_url = field_next_url
        next_url = next_url or logout_next_url
        if not referer or utils.same_origin(request.build_absolute_uri(), referer):
            if hasattr(request, 'user') and request.user.is_authenticated:
                logout = None
                try:
                    issuer = request.session.get('mellon_session', {}).get('issuer')
                    if issuer:
                        self.profile = logout = utils.create_logout(request)
                        self.get_relay_state(create=True)
                        try:
                            session_indexes = models.SessionIndex.objects.filter(
                                saml_identifier__user=request.user,
                                saml_identifier__issuer__entity_id=issuer,
                                session_key=request.session.session_key,
                            )
                            if not session_indexes:
                                self.log.error('unable to find lasso session dump')
                            else:
                                session_dump = utils.make_session_dump(session_indexes)
                                logout.setSessionFromDump(session_dump)
                            session_indexes.update(logout_timestamp=now())
                            logout.initRequest(issuer, lasso.HTTP_METHOD_REDIRECT)
                            logout.buildRequestMsg()
                        except lasso.Error as e:
                            self.log.error('unable to initiate a logout request %r', e)
                        else:
                            self.log.debug('sending LogoutRequest %r', logout.request.dump())
                            self.log.debug('to URL %r', logout.msgUrl)
                            return HttpResponseRedirect(logout.msgUrl)
                finally:
                    auth.logout(request)
                    # set next_url after local logout, as the session is wiped by auth.logout
                    if logout:
                        self.set_next_url(next_url)
                    self.log.info('user logged out, SLO request sent to IdP')
            else:
                # anonymous user: if next_url is None redirect to referer
                return HttpResponseRedirect(next_url)
        else:
            self.log.warning('logout refused referer %r is not of the same origin', referer)
        return HttpResponseRedirect(next_url)

    def sp_logout_response(self, request, logout_next_url='/'):
        '''Launch a logout request to the identity provider'''
        self.profile = logout = utils.create_logout(request)
        logout.msgRelayState = request.GET.get('RelayState')
        cookie_name = self.next_url_cookie_name(logout.msgRelayState)
        cookie_next_url = request.COOKIES.get(cookie_name)
        next_url = self.get_next_url() or cookie_next_url or logout_next_url
        # the user shouldn't be logged anymore at this point but it may happen
        # that a concurrent SSO happened in the meantime, so we do another
        # logout to make sure.
        try:
            logout.processResponseMsg(request.META['QUERY_STRING'])
        except lasso.ProfileStatusNotSuccessError:
            self.show_message_status_is_not_success(logout, 'SAML logout failed')
        except lasso.LogoutPartialLogoutError:
            self.log.warning('partial logout')
        except lasso.Error as e:
            self.log.warning('unable to process a logout response: %s', e)
        response = HttpResponseRedirect(next_url)
        if cookie_name in request.COOKIES:
            response.delete_cookie(cookie_name)
        models.SessionIndex.cleanup(chunk_size=100)
        return response

    TOKEN_SALT = 'mellon-logout-token'

    def sp_logout_token(self, request, token, logout_next_url):
        token_content = signing.loads(token, salt=self.TOKEN_SALT)
        next_url = token_content['next_url'] or logout_next_url
        session_index_pk = token_content['session_index_pk']
        session_index = models.SessionIndex.objects.filter(pk=session_index_pk).first()
        session_indexes = models.SessionIndex.objects.filter(
            saml_identifier=session_index.saml_identifier, session_key=session_index.session_key
        )
        if session_indexes:
            session_dump = utils.make_session_dump(session_indexes)
            logout = utils.create_logout(request)
            logout.msgRelayState = str(uuid.uuid4())
            try:
                logout.setSessionFromDump(session_dump)
                logout.initRequest(
                    session_indexes[0].saml_identifier.issuer.entity_id, lasso.HTTP_METHOD_REDIRECT
                )
                logout.buildRequestMsg()
            except lasso.Error as e:
                self.log.error('unable to initiate a logout request %r', e)
                return HttpResponseRedirect(next_url)
            except Exception:
                self.log.exception('unable to initiate a logout request')
                return HttpResponseRedirect(next_url)
            else:
                self.log.debug('sending LogoutRequest %r to URL %r', logout.request.dump(), logout.msgUrl)
                response = HttpResponseRedirect(logout.msgUrl)
                response.set_cookie(
                    self.next_url_cookie_name(logout.msgRelayState),
                    value=next_url,
                    max_age=600,
                    samesite='Lax',
                )
                return response
        return HttpResponseRedirect(next_url)

    @classmethod
    def make_logout_token_url(cls, request, next_url=None):
        issuer = request.session.get('mellon_session', {}).get('issuer')
        if not issuer:
            return None
        session_indexes = models.SessionIndex.objects.filter(
            saml_identifier__user=request.user, saml_identifier__issuer__entity_id=issuer
        ).order_by('-id')
        if not session_indexes:
            return None

        token_content = {
            'next_url': next_url,
            'session_index_pk': session_indexes[0].pk,
        }
        token = signing.dumps(token_content, salt=cls.TOKEN_SALT)
        session_indexes.update(logout_timestamp=now())
        return reverse('mellon_logout') + '?' + urlencode({'token': token})


logout = csrf_exempt(LogoutView.as_view())


def metadata(request, **kwargs):
    metadata = utils.create_metadata(request)
    return HttpResponse(metadata, content_type='text/xml')


class DebugLoginView(RedirectView):
    pattern_name = 'mellon_login'
    query_string = True

    def dispatch(self, request, *args, **kwargs):
        if not settings.DEBUG:
            return HttpResponseForbidden()
        request.session['mellon_debug_login'] = True
        return super().dispatch(request, *args, **kwargs)


debug_login = csrf_exempt(DebugLoginView.as_view())
