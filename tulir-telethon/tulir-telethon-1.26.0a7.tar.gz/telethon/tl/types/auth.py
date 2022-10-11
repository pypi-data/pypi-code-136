"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeUser
    from ...tl.types.help import TypeTermsOfService
    from ...tl.types.auth import TypeAuthorization, TypeCodeType, TypeSentCodeType



class Authorization(TLObject):
    CONSTRUCTOR_ID = 0x33fb7bb8
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, user: 'TypeUser', setup_password_required: Optional[bool]=None, otherwise_relogin_days: Optional[int]=None, tmp_sessions: Optional[int]=None):
        """
        Constructor for auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.user = user
        self.setup_password_required = setup_password_required
        self.otherwise_relogin_days = otherwise_relogin_days
        self.tmp_sessions = tmp_sessions

    def to_dict(self):
        return {
            '_': 'Authorization',
            'user': self.user.to_dict() if isinstance(self.user, TLObject) else self.user,
            'setup_password_required': self.setup_password_required,
            'otherwise_relogin_days': self.otherwise_relogin_days,
            'tmp_sessions': self.tmp_sessions
        }

    def _bytes(self):
        assert ((self.setup_password_required or self.setup_password_required is not None) and (self.otherwise_relogin_days or self.otherwise_relogin_days is not None)) or ((self.setup_password_required is None or self.setup_password_required is False) and (self.otherwise_relogin_days is None or self.otherwise_relogin_days is False)), 'setup_password_required, otherwise_relogin_days parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'\xb8{\xfb3',
            struct.pack('<I', (0 if self.setup_password_required is None or self.setup_password_required is False else 2) | (0 if self.otherwise_relogin_days is None or self.otherwise_relogin_days is False else 2) | (0 if self.tmp_sessions is None or self.tmp_sessions is False else 1)),
            b'' if self.otherwise_relogin_days is None or self.otherwise_relogin_days is False else (struct.pack('<i', self.otherwise_relogin_days)),
            b'' if self.tmp_sessions is None or self.tmp_sessions is False else (struct.pack('<i', self.tmp_sessions)),
            self.user._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _setup_password_required = bool(flags & 2)
        if flags & 2:
            _otherwise_relogin_days = reader.read_int()
        else:
            _otherwise_relogin_days = None
        if flags & 1:
            _tmp_sessions = reader.read_int()
        else:
            _tmp_sessions = None
        _user = reader.tgread_object()
        return cls(user=_user, setup_password_required=_setup_password_required, otherwise_relogin_days=_otherwise_relogin_days, tmp_sessions=_tmp_sessions)


class AuthorizationSignUpRequired(TLObject):
    CONSTRUCTOR_ID = 0x44747e9a
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, terms_of_service: Optional['TypeTermsOfService']=None):
        """
        Constructor for auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.terms_of_service = terms_of_service

    def to_dict(self):
        return {
            '_': 'AuthorizationSignUpRequired',
            'terms_of_service': self.terms_of_service.to_dict() if isinstance(self.terms_of_service, TLObject) else self.terms_of_service
        }

    def _bytes(self):
        return b''.join((
            b'\x9a~tD',
            struct.pack('<I', (0 if self.terms_of_service is None or self.terms_of_service is False else 1)),
            b'' if self.terms_of_service is None or self.terms_of_service is False else (self.terms_of_service._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 1:
            _terms_of_service = reader.tgread_object()
        else:
            _terms_of_service = None
        return cls(terms_of_service=_terms_of_service)


class CodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x741cd3e3
    SUBCLASS_OF_ID = 0xb3f3e401

    def to_dict(self):
        return {
            '_': 'CodeTypeCall'
        }

    def _bytes(self):
        return b''.join((
            b'\xe3\xd3\x1ct',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class CodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0x226ccefb
    SUBCLASS_OF_ID = 0xb3f3e401

    def to_dict(self):
        return {
            '_': 'CodeTypeFlashCall'
        }

    def _bytes(self):
        return b''.join((
            b'\xfb\xcel"',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class CodeTypeMissedCall(TLObject):
    CONSTRUCTOR_ID = 0xd61ad6ee
    SUBCLASS_OF_ID = 0xb3f3e401

    def to_dict(self):
        return {
            '_': 'CodeTypeMissedCall'
        }

    def _bytes(self):
        return b''.join((
            b'\xee\xd6\x1a\xd6',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class CodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0x72a3158c
    SUBCLASS_OF_ID = 0xb3f3e401

    def to_dict(self):
        return {
            '_': 'CodeTypeSms'
        }

    def _bytes(self):
        return b''.join((
            b'\x8c\x15\xa3r',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class ExportedAuthorization(TLObject):
    CONSTRUCTOR_ID = 0xb434e2b8
    SUBCLASS_OF_ID = 0x5fd1ec51

    # noinspection PyShadowingBuiltins
    def __init__(self, id: int, bytes: bytes):
        """
        Constructor for auth.ExportedAuthorization: Instance of ExportedAuthorization.
        """
        self.id = id
        self.bytes = bytes

    def to_dict(self):
        return {
            '_': 'ExportedAuthorization',
            'id': self.id,
            'bytes': self.bytes
        }

    def _bytes(self):
        return b''.join((
            b'\xb8\xe24\xb4',
            struct.pack('<q', self.id),
            self.serialize_bytes(self.bytes),
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.read_long()
        _bytes = reader.tgread_bytes()
        return cls(id=_id, bytes=_bytes)


class LoggedOut(TLObject):
    CONSTRUCTOR_ID = 0xc3a2835f
    SUBCLASS_OF_ID = 0xa804315

    def __init__(self, future_auth_token: Optional[bytes]=None):
        """
        Constructor for auth.LoggedOut: Instance of LoggedOut.
        """
        self.future_auth_token = future_auth_token

    def to_dict(self):
        return {
            '_': 'LoggedOut',
            'future_auth_token': self.future_auth_token
        }

    def _bytes(self):
        return b''.join((
            b'_\x83\xa2\xc3',
            struct.pack('<I', (0 if self.future_auth_token is None or self.future_auth_token is False else 1)),
            b'' if self.future_auth_token is None or self.future_auth_token is False else (self.serialize_bytes(self.future_auth_token)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 1:
            _future_auth_token = reader.tgread_bytes()
        else:
            _future_auth_token = None
        return cls(future_auth_token=_future_auth_token)


class LoginToken(TLObject):
    CONSTRUCTOR_ID = 0x629f1980
    SUBCLASS_OF_ID = 0x6b55f636

    def __init__(self, expires: Optional[datetime], token: bytes):
        """
        Constructor for auth.LoginToken: Instance of either LoginToken, LoginTokenMigrateTo, LoginTokenSuccess.
        """
        self.expires = expires
        self.token = token

    def to_dict(self):
        return {
            '_': 'LoginToken',
            'expires': self.expires,
            'token': self.token
        }

    def _bytes(self):
        return b''.join((
            b'\x80\x19\x9fb',
            self.serialize_datetime(self.expires),
            self.serialize_bytes(self.token),
        ))

    @classmethod
    def from_reader(cls, reader):
        _expires = reader.tgread_date()
        _token = reader.tgread_bytes()
        return cls(expires=_expires, token=_token)


class LoginTokenMigrateTo(TLObject):
    CONSTRUCTOR_ID = 0x68e9916
    SUBCLASS_OF_ID = 0x6b55f636

    def __init__(self, dc_id: int, token: bytes):
        """
        Constructor for auth.LoginToken: Instance of either LoginToken, LoginTokenMigrateTo, LoginTokenSuccess.
        """
        self.dc_id = dc_id
        self.token = token

    def to_dict(self):
        return {
            '_': 'LoginTokenMigrateTo',
            'dc_id': self.dc_id,
            'token': self.token
        }

    def _bytes(self):
        return b''.join((
            b'\x16\x99\x8e\x06',
            struct.pack('<i', self.dc_id),
            self.serialize_bytes(self.token),
        ))

    @classmethod
    def from_reader(cls, reader):
        _dc_id = reader.read_int()
        _token = reader.tgread_bytes()
        return cls(dc_id=_dc_id, token=_token)


class LoginTokenSuccess(TLObject):
    CONSTRUCTOR_ID = 0x390d5c5e
    SUBCLASS_OF_ID = 0x6b55f636

    def __init__(self, authorization: 'TypeAuthorization'):
        """
        Constructor for auth.LoginToken: Instance of either LoginToken, LoginTokenMigrateTo, LoginTokenSuccess.
        """
        self.authorization = authorization

    def to_dict(self):
        return {
            '_': 'LoginTokenSuccess',
            'authorization': self.authorization.to_dict() if isinstance(self.authorization, TLObject) else self.authorization
        }

    def _bytes(self):
        return b''.join((
            b'^\\\r9',
            self.authorization._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _authorization = reader.tgread_object()
        return cls(authorization=_authorization)


class PasswordRecovery(TLObject):
    CONSTRUCTOR_ID = 0x137948a5
    SUBCLASS_OF_ID = 0xfa72d43a

    def __init__(self, email_pattern: str):
        """
        Constructor for auth.PasswordRecovery: Instance of PasswordRecovery.
        """
        self.email_pattern = email_pattern

    def to_dict(self):
        return {
            '_': 'PasswordRecovery',
            'email_pattern': self.email_pattern
        }

    def _bytes(self):
        return b''.join((
            b'\xa5Hy\x13',
            self.serialize_bytes(self.email_pattern),
        ))

    @classmethod
    def from_reader(cls, reader):
        _email_pattern = reader.tgread_string()
        return cls(email_pattern=_email_pattern)


class SentCode(TLObject):
    CONSTRUCTOR_ID = 0x5e002502
    SUBCLASS_OF_ID = 0x6ce87081

    # noinspection PyShadowingBuiltins
    def __init__(self, type: 'TypeSentCodeType', phone_code_hash: str, next_type: Optional['TypeCodeType']=None, timeout: Optional[int]=None):
        """
        Constructor for auth.SentCode: Instance of SentCode.
        """
        self.type = type
        self.phone_code_hash = phone_code_hash
        self.next_type = next_type
        self.timeout = timeout

    def to_dict(self):
        return {
            '_': 'SentCode',
            'type': self.type.to_dict() if isinstance(self.type, TLObject) else self.type,
            'phone_code_hash': self.phone_code_hash,
            'next_type': self.next_type.to_dict() if isinstance(self.next_type, TLObject) else self.next_type,
            'timeout': self.timeout
        }

    def _bytes(self):
        return b''.join((
            b'\x02%\x00^',
            struct.pack('<I', (0 if self.next_type is None or self.next_type is False else 2) | (0 if self.timeout is None or self.timeout is False else 4)),
            self.type._bytes(),
            self.serialize_bytes(self.phone_code_hash),
            b'' if self.next_type is None or self.next_type is False else (self.next_type._bytes()),
            b'' if self.timeout is None or self.timeout is False else (struct.pack('<i', self.timeout)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _type = reader.tgread_object()
        _phone_code_hash = reader.tgread_string()
        if flags & 2:
            _next_type = reader.tgread_object()
        else:
            _next_type = None
        if flags & 4:
            _timeout = reader.read_int()
        else:
            _timeout = None
        return cls(type=_type, phone_code_hash=_phone_code_hash, next_type=_next_type, timeout=_timeout)


class SentCodeTypeApp(TLObject):
    CONSTRUCTOR_ID = 0x3dbb5986
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, length: int):
        """
        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall, SentCodeTypeMissedCall, SentCodeTypeEmailCode, SentCodeTypeSetUpEmailRequired.
        """
        self.length = length

    def to_dict(self):
        return {
            '_': 'SentCodeTypeApp',
            'length': self.length
        }

    def _bytes(self):
        return b''.join((
            b'\x86Y\xbb=',
            struct.pack('<i', self.length),
        ))

    @classmethod
    def from_reader(cls, reader):
        _length = reader.read_int()
        return cls(length=_length)


class SentCodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x5353e5a7
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, length: int):
        """
        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall, SentCodeTypeMissedCall, SentCodeTypeEmailCode, SentCodeTypeSetUpEmailRequired.
        """
        self.length = length

    def to_dict(self):
        return {
            '_': 'SentCodeTypeCall',
            'length': self.length
        }

    def _bytes(self):
        return b''.join((
            b'\xa7\xe5SS',
            struct.pack('<i', self.length),
        ))

    @classmethod
    def from_reader(cls, reader):
        _length = reader.read_int()
        return cls(length=_length)


class SentCodeTypeEmailCode(TLObject):
    CONSTRUCTOR_ID = 0x5a159841
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, email_pattern: str, length: int, apple_signin_allowed: Optional[bool]=None, google_signin_allowed: Optional[bool]=None, next_phone_login_date: Optional[datetime]=None):
        """
        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall, SentCodeTypeMissedCall, SentCodeTypeEmailCode, SentCodeTypeSetUpEmailRequired.
        """
        self.email_pattern = email_pattern
        self.length = length
        self.apple_signin_allowed = apple_signin_allowed
        self.google_signin_allowed = google_signin_allowed
        self.next_phone_login_date = next_phone_login_date

    def to_dict(self):
        return {
            '_': 'SentCodeTypeEmailCode',
            'email_pattern': self.email_pattern,
            'length': self.length,
            'apple_signin_allowed': self.apple_signin_allowed,
            'google_signin_allowed': self.google_signin_allowed,
            'next_phone_login_date': self.next_phone_login_date
        }

    def _bytes(self):
        return b''.join((
            b'A\x98\x15Z',
            struct.pack('<I', (0 if self.apple_signin_allowed is None or self.apple_signin_allowed is False else 1) | (0 if self.google_signin_allowed is None or self.google_signin_allowed is False else 2) | (0 if self.next_phone_login_date is None or self.next_phone_login_date is False else 4)),
            self.serialize_bytes(self.email_pattern),
            struct.pack('<i', self.length),
            b'' if self.next_phone_login_date is None or self.next_phone_login_date is False else (self.serialize_datetime(self.next_phone_login_date)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _apple_signin_allowed = bool(flags & 1)
        _google_signin_allowed = bool(flags & 2)
        _email_pattern = reader.tgread_string()
        _length = reader.read_int()
        if flags & 4:
            _next_phone_login_date = reader.tgread_date()
        else:
            _next_phone_login_date = None
        return cls(email_pattern=_email_pattern, length=_length, apple_signin_allowed=_apple_signin_allowed, google_signin_allowed=_google_signin_allowed, next_phone_login_date=_next_phone_login_date)


class SentCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0xab03c6d9
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, pattern: str):
        """
        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall, SentCodeTypeMissedCall, SentCodeTypeEmailCode, SentCodeTypeSetUpEmailRequired.
        """
        self.pattern = pattern

    def to_dict(self):
        return {
            '_': 'SentCodeTypeFlashCall',
            'pattern': self.pattern
        }

    def _bytes(self):
        return b''.join((
            b'\xd9\xc6\x03\xab',
            self.serialize_bytes(self.pattern),
        ))

    @classmethod
    def from_reader(cls, reader):
        _pattern = reader.tgread_string()
        return cls(pattern=_pattern)


class SentCodeTypeMissedCall(TLObject):
    CONSTRUCTOR_ID = 0x82006484
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, prefix: str, length: int):
        """
        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall, SentCodeTypeMissedCall, SentCodeTypeEmailCode, SentCodeTypeSetUpEmailRequired.
        """
        self.prefix = prefix
        self.length = length

    def to_dict(self):
        return {
            '_': 'SentCodeTypeMissedCall',
            'prefix': self.prefix,
            'length': self.length
        }

    def _bytes(self):
        return b''.join((
            b'\x84d\x00\x82',
            self.serialize_bytes(self.prefix),
            struct.pack('<i', self.length),
        ))

    @classmethod
    def from_reader(cls, reader):
        _prefix = reader.tgread_string()
        _length = reader.read_int()
        return cls(prefix=_prefix, length=_length)


class SentCodeTypeSetUpEmailRequired(TLObject):
    CONSTRUCTOR_ID = 0xa5491dea
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, apple_signin_allowed: Optional[bool]=None, google_signin_allowed: Optional[bool]=None):
        """
        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall, SentCodeTypeMissedCall, SentCodeTypeEmailCode, SentCodeTypeSetUpEmailRequired.
        """
        self.apple_signin_allowed = apple_signin_allowed
        self.google_signin_allowed = google_signin_allowed

    def to_dict(self):
        return {
            '_': 'SentCodeTypeSetUpEmailRequired',
            'apple_signin_allowed': self.apple_signin_allowed,
            'google_signin_allowed': self.google_signin_allowed
        }

    def _bytes(self):
        return b''.join((
            b'\xea\x1dI\xa5',
            struct.pack('<I', (0 if self.apple_signin_allowed is None or self.apple_signin_allowed is False else 1) | (0 if self.google_signin_allowed is None or self.google_signin_allowed is False else 2)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _apple_signin_allowed = bool(flags & 1)
        _google_signin_allowed = bool(flags & 2)
        return cls(apple_signin_allowed=_apple_signin_allowed, google_signin_allowed=_google_signin_allowed)


class SentCodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0xc000bba2
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, length: int):
        """
        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall, SentCodeTypeMissedCall, SentCodeTypeEmailCode, SentCodeTypeSetUpEmailRequired.
        """
        self.length = length

    def to_dict(self):
        return {
            '_': 'SentCodeTypeSms',
            'length': self.length
        }

    def _bytes(self):
        return b''.join((
            b'\xa2\xbb\x00\xc0',
            struct.pack('<i', self.length),
        ))

    @classmethod
    def from_reader(cls, reader):
        _length = reader.read_int()
        return cls(length=_length)

