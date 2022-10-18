# -*- coding: ascii -*-
"""
ldap0.controls.pwdpolicy - classes for Password Policy controls
(see https://tools.ietf.org/html/draft-vchu-ldap-pwd-policy)
"""

from . import ResponseControl

__all__ = [
    'PasswordExpiringControl',
    'PasswordExpiredControl',
]


class PasswordExpiringControl(ResponseControl):
    """
    Indicates time in seconds when password will expire
    """
    controlType: str = '2.16.840.1.113730.3.4.5'

    def decode(self, encodedControlValue: bytes):
        self.gracePeriod = int(encodedControlValue)


class PasswordExpiredControl(ResponseControl):
    """
    Indicates that password is expired
    """
    controlType: str = '2.16.840.1.113730.3.4.4'

    def decode(self, encodedControlValue: bytes):
        self.passwordExpired = (encodedControlValue == b'0')
