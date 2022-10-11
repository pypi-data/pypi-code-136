#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Connect to S3 """


from boto3 import resource
from boto3.resources.factory import ServiceResource

from baseblock import BaseObject

from awsfile_helper.dmo import CredentialManager


class ConnectToS3(BaseObject):
    """ Connect to S3 """

    def __init__(self):
        """ Change Log

        Created:
            22-Jul-2022
            craigtrim@gmail.com
            *   https://bast-ai.atlassian.net/browse/COR-8
        """
        BaseObject.__init__(self, __name__)
        self._creds = CredentialManager()

    def process(self) -> ServiceResource:
        s3 = resource('s3',
                      aws_access_key_id=self._creds.access_key(),
                      aws_secret_access_key=self._creds.secret_key())

        return s3
