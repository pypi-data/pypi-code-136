# -*- coding: ascii -*-
"""
ldap0.res - basic classes for LDAP results
"""

from typing import Dict, List, Optional, Union, Sequence, Tuple

from pyasn1.error import PyAsn1Error

import _libldap0

from .dn import DNObj
from .base import decode_list
from .ldapurl import LDAPUrl
from .typehints import EntryBytes, EntryMixed, EntryStr
from .controls import ResponseControl, RequestControl, KNOWN_RESPONSE_CONTROLS
from .extop import ExtendedResponse

__all__ = [
    'LDAPResult',
    'SearchReference',
    'SearchResultEntry',
    'encode_request_ctrls',
    'decode_response_ctrls',
]


class IntermediateResponse:
    """
    Generic base class for a LDAPv3 intermediate response

    requestName
        OID as string of the LDAPv3 intermediate response
    encodedResponseValue
        BER-encoded ASN.1 value of the LDAPv3 intermediate response
    """
    encoding = 'utf-8'

    responseName = None

    def __init__(self, responseName=None, encodedResponseValue=None, ctrls=None):
        if responseName is not None:
            self.responseName = responseName
        self.responseValue = encodedResponseValue
        if encodedResponseValue is not None:
            self.decode(encodedResponseValue)
        self.ctrls = ctrls or []

    def __repr__(self):
        return '%s(responseName=%r, responseValue=%r)' % (
            self.__class__.__name__,
            self.responseName,
            self.responseValue,
        )

    @classmethod
    def check_resp_name(cls, name):
        """
        returns True if :name: is the correct expected responseName
        """
        return name == cls.responseName

    def decode(self, value: bytes):
        """
        decodes the BER-encoded ASN.1 extended operation response value and
        sets the appropriate class attributes
        """
        self.responseValue = value


class IntermediateResponseRegistry:
    """
    A simple registry for responses and their handler class
    """

    _handler_cls: Dict[str, Union[ExtendedResponse, IntermediateResponse]]

    def __init__(self):
        self._handler_cls = {}

    def register(
            self,
            handler: Union[ExtendedResponse, IntermediateResponse],
        ):
        """
        register an handler class for extended/intermediate response
        """
        self._handler_cls[handler.responseName] = handler

    def get(
            self,
            oid: str,
            default: Optional[Union[ExtendedResponse, IntermediateResponse]] = None,
        ) -> Optional[Union[ExtendedResponse, IntermediateResponse]]:
        """
        return handler class for extended/intermediate response by OID (responseName)
        """
        return self._handler_cls.get(oid, default)


# response OID to class registry
INTERMEDIATE_RESPONSE_REGISTRY = IntermediateResponseRegistry()


class SearchReference:
    """
    LDAP search continuation objects
    """
    __slots__ = (
        'ctrls',
        'encoding',
        '_ref_urls_b',
        '_ref_urls_o',
        '_ref_urls_s',
    )
    _ref_urls_s: Optional[List[str]]
    _ref_urls_o: Optional[List[LDAPUrl]]

    def __init__(self, entry: List[bytes], ctrls=None, encoding: str = 'utf-8'):
        self.encoding = encoding
        self._ref_urls_b = entry
        self._ref_urls_s = self._ref_urls_o = None
        self.ctrls = ctrls

    def __repr__(self) -> str:
        return '%s(%r, %r, encoding=%r)' % (
            self.__class__.__name__,
            self._ref_urls_b,
            self.ctrls,
            self.encoding,
        )

    @property
    def ref_url_strings(self) -> List[str]:
        if self._ref_urls_s is None:
            self._ref_urls_s = decode_list(self._ref_urls_b, encoding=self.encoding)
        return self._ref_urls_s

    @property
    def ref_ldap_urls(self) -> List[LDAPUrl]:
        if self._ref_urls_o is None:
            self._ref_urls_o = [LDAPUrl(url) for url in self.ref_url_strings]
        return self._ref_urls_o


class SearchResultEntry:
    """
    LDAP search result objects
    """
    __slots__ = (
        'ctrls',
        'dn_b',
        '_dn_o',
        '_dn_s',
        'encoding',
        '_entry_as',
        '_entry_b',
        '_entry_s',
    )
    dn_b: bytes
    _dn_s: Optional[str]
    _dn_o: Optional[DNObj]
    _entry_b: EntryBytes
    _entry_as: Optional[EntryMixed]
    _entry_s: Optional[EntryStr]

    def __init__(self, dn: bytes, entry: EntryBytes, ctrls=None, encoding: str = 'utf-8'):
        self.encoding = encoding
        self.dn_b = dn
        self._dn_s = self._dn_o = None
        self._entry_b = entry
        self._entry_as = self._entry_s = None
        self.ctrls = ctrls or []

    def __repr__(self) -> str:
        return '%s(%r, %r, %r, encoding=%r)' % (
            self.__class__.__name__,
            self.dn_b,
            self._entry_b,
            self.ctrls,
            self.encoding,
        )

    def __eq__(self, other):
        return (
            self.dn_s == other.dn_s
            and self.entry_as == other.entry_as
            and self.ctrls == other.ctrls
        )

    @property
    def dn_s(self):
        if self._dn_s is None:
            self._dn_s = self.dn_b.decode(self.encoding)
        return self._dn_s

    @property
    def dn_o(self):
        if self._dn_o is None:
            self._dn_o = DNObj.from_str(self.dn_s)
        return self._dn_o

    @property
    def entry_b(self) -> EntryBytes:
        return self._entry_b

    @property
    def entry_as(self) -> EntryMixed:
        if self._entry_as is None:
            self._entry_as: EntryMixed = {
                at.decode('ascii'): avs
                for at, avs in self._entry_b.items()
            }
        return self._entry_as

    @property
    def entry_s(self) -> EntryStr:
        if self._entry_s is None:
            self._entry_s: EntryStr = {
                at.decode('ascii'): [av.decode(self.encoding) for av in avs]
                for at, avs in self._entry_b.items()
            }
        return self._entry_s


class LDAPResult:
    """
    base class for LDAP result objects
    """
    __slots__ = (
        'rtype',
        'rdata',
        'msgid',
        'ctrls',
        'call_args',
    )
    rtype: int
    rdata: List[Union[SearchReference, SearchResultEntry, IntermediateResponse]]
    msgid: int
    ctrls: List[ResponseControl]

    def __init__(
            self,
            rtype: int,
            rdata,
            msgid: int,
            ctrls,
            encoding: str = 'utf-8',
            call_args = None,
        ):
        self.rtype = rtype
        self.rdata = []
        self.msgid = msgid
        self.ctrls = ctrls or []
        self.call_args = call_args
        for dn, entry, ctrls in rdata or []:
            if rtype == _libldap0.RES_SEARCH_REFERENCE:
                self.rdata.append(SearchReference(entry, ctrls, encoding=encoding))
            elif rtype == _libldap0.RES_SEARCH_ENTRY:
                self.rdata.append(SearchResultEntry(dn, entry, ctrls, encoding=encoding))
            elif rtype == _libldap0.RES_INTERMEDIATE:
                respoid = dn.decode(encoding)
                resp_class = INTERMEDIATE_RESPONSE_REGISTRY.get(respoid, IntermediateResponse)
                response = resp_class(respoid, encodedResponseValue=entry, ctrls=ctrls)
                self.rdata.append(response)
            else:
                raise NotImplementedError

    def __repr__(self) -> str:
        return '%s(%r, %r, %r, %r)' % (
            self.__class__.__name__,
            self.rtype,
            self.rdata,
            self.msgid,
            self.ctrls,
        )


def encode_request_ctrls(
        ctrls: Sequence[RequestControl]
    ) -> Tuple[str, bool, bytes]:
    """
    Return list of readily encoded 3-tuples which can be directly
    passed to C module _ldap

    ctrls
        sequence-type of RequestControl objects
    """
    if ctrls is None:
        return None
    return [
        (c.controlType.encode('ascii'), c.criticality, c.encode())
        for c in ctrls
    ]
    # end of encode_request_ctrls()


def decode_response_ctrls(
        ctrls: Sequence[ResponseControl],
        ctrl_reg: Optional[Dict[str, ResponseControl]] = None,
    ):
    """
    Returns list of readily decoded ResponseControl objects

    ctrls
        Sequence-type of 3-tuples returned by _libldap0.result() containing
        the encoded ASN.1 control values of response controls.
    ctrl_reg
        Dictionary mapping extended control's OID to ResponseControl class
        of response controls known by the application. If None
        ldap0.controls.KNOWN_RESPONSE_CONTROLS is used here.
    """
    if ctrl_reg is None:
        ctrl_reg = KNOWN_RESPONSE_CONTROLS
    result = []
    for ctrl_type, ctrl_criticality, ctrl_val in ctrls or []:
        ctrl_type = ctrl_type.decode('ascii')
        try:
            control_class = ctrl_reg.get(ctrl_type)
        except KeyError:
            if ctrl_criticality:
                raise _libldap0.UNAVAILABLE_CRITICAL_EXTENSION(
                    'Unknown critical response control, ctrl_type %r' % (ctrl_type)
                )
        else:
            control = control_class(criticality=ctrl_criticality)
            try:
                control.decode(ctrl_val)
            except PyAsn1Error as err:
                if ctrl_criticality:
                    raise err
            else:
                result.append(control)
    return result
    # end of decode_response_ctrls()
