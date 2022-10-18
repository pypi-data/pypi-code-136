# -*- coding: ascii -*-
"""
ldap0.controls - support classes for LDAP controls

The ldap0.controls module provides LDAPControl classes.
Each class provides support for a certain control.
"""

import inspect
from importlib import import_module
from typing import Dict, Optional, Sequence, Tuple

import _libldap0


__all__ = [
    # Classes
    'LDAPControl',
    'RequestControl',
    'ResponseControl',
]


class RequestControl:
    """
    Base class for all request controls

    controlType
        OID as string of the LDAPv3 extended request control
    criticality
        sets the criticality of the control (boolean)
    encodedControlValue
        control value of the LDAPv3 extended request control
        (here it is the BER-encoded ASN.1 control value)
    """
    encoding: str = 'utf-8'
    controlType: Optional[str] = None

    def __init__(
            self,
            controlType: Optional[str] = None,
            criticality: bool = False,
            encodedControlValue: Optional[bytes] = None
        ):
        if controlType is not None:
            self.controlType = controlType
        self.criticality = criticality
        self.encodedControlValue = encodedControlValue

    def encode(self) -> bytes:
        """
        sets class attribute encodedControlValue to the BER-encoded ASN.1
        control value composed by class attributes set before
        """
        return self.encodedControlValue


class ResponseControl:
    """
    Base class for all response controls

    controlType
        OID as string of the LDAPv3 extended response control
    criticality
        sets the criticality of the received control (boolean)
    """
    encoding: str = 'utf-8'

    def __init__(
            self,
            controlType: Optional[str] = None,
            criticality: bool = False,
        ):
        if controlType is not None:
            self.controlType = controlType
        self.criticality = criticality

    def decode(self, encodedControlValue: bytes):
        """
        decodes the BER-encoded ASN.1 control value and sets the appropriate
        class attributes
        """
        self.controlValue = encodedControlValue


class LDAPControl(RequestControl, ResponseControl):
    """
    Base class for combined request/response controls
    """
    encoding: str = 'utf-8'
    controlType: Optional[str] = None

    def __init__(
            self,
            controlType: Optional[str] = None,
            criticality: bool = False,
            encodedControlValue: Optional[bytes] = None
        ):
        RequestControl.__init__(
            self,
            controlType=controlType,
            criticality=criticality,
            encodedControlValue=encodedControlValue,
        )


class ControlRegistry:
    """
    A simple registry for extended controls and their handler class
    """

    cmap: Dict[str, ResponseControl]

    def __init__(self, *module_names):
        self.cmap = None
        self._module_names = module_names

    def _reg(self, *module_names):
        for module_name in module_names:
            module = import_module(module_name)
            for _, cls in inspect.getmembers(module, inspect.isclass):
                if (
                        issubclass(cls, ResponseControl)
                        and hasattr(cls, 'controlType')
                        and cls.controlType is not None
                    ):
                    self.cmap[cls.controlType] = cls

    def get(self, control_type):
        if self.cmap is None:
            self.cmap = {}
            self._reg(*self._module_names)
        return self.cmap[control_type]

# response control OID to class registry
KNOWN_RESPONSE_CONTROLS = ControlRegistry(
    __name__+'.deref',
    __name__+'.libldap',
    __name__+'.openldap',
    __name__+'.pagedresults',
    __name__+'.ppolicy',
    __name__+'.psearch',
    __name__+'.pwdpolicy',
    __name__+'.readentry',
    __name__+'.sessiontrack',
    __name__+'.simple',
    __name__+'.sss',
    __name__+'.syncrepl',
    __name__+'.vlv',
)
