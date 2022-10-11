#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find Cloud files on S3 within the 'bast-core-data' bucket """


import os

from baseblock import BaseObject


class FindOwlFile(BaseObject):
    """ Find Ontology files on S3 within the 'bast-core-data' bucket """

    def __init__(self,
                 file_name: str,
                 file_version: str = None):
        """ Change Log

        Created:
            6-Aug-2022
            craigtrim@gmail.com
            *   refactored out of 'ontology-by-version' in pursuit of
                https://bast-ai.atlassian.net/browse/COR-74

        Args:
            file_name (str): the qualified name of the file to retrieve
            file_version (str, optional): the file version. Defaults to '*'.
                the default '*' will always retrieve the latest version
        """
        BaseObject.__init__(self, __name__)

        if not file_name.startswith('ontologies/'):
            file_name = f"ontologies/{file_name}"

        self._file_name = file_name
        self._file_version = file_version

    def process(self) -> dict:

        from awsfile_helper import FindS3File

        d_owl_file = FindS3File(
            file_name=self._file_name,
            file_ext='owl',
            file_version=self._file_version).process()

        d_txt_file = FindS3File(
            file_name=self._file_name,
            file_ext='txt',
            file_version=d_owl_file['version']).process()

        return {
            'owl': d_owl_file,
            'txt': d_txt_file,
            'path': os.path.dirname(d_owl_file['path'])
        }
