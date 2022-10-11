#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Manage AWS Credentials """


from baseblock import EnvIO
from baseblock import CryptoBase
from baseblock import BaseObject


class CredentialManager(BaseObject):
    """ Manage AWS Credentials """

    def __init__(self):
        """ Change Log

        Created:
            22-Jul-2022
            craigtrim@gmail.com
            *   https://bast-ai.atlassian.net/browse/COR-8
        """
        BaseObject.__init__(self, __name__)
        self._access_key = EnvIO.str_or_exception('AWS_ACCESS_KEY')
        self._secret_key = EnvIO.str_or_exception('AWS_SECRET_KEY')

    def access_key(self) -> str:
        return CryptoBase().decrypt_str(self._access_key)

    def secret_key(self) -> str:
        return CryptoBase().decrypt_str(self._secret_key)
