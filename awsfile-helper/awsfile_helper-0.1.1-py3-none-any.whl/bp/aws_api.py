#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" API for AWS Content Management """


import os

from baseblock import EnvIO
from baseblock import BaseObject

from awsfile_helper.svc import ConnectToS3
from awsfile_helper.svc import ReadFromS3
from awsfile_helper.svc import FindLatestVersionNumber
from awsfile_helper.svc import DownloadFromS3
from awsfile_helper.svc import FindFileByVersion


class AwsAPI(BaseObject):
    """ API for AWS Content Management """

    def __init__(self):
        """ Change Log

        Created:
            22-Jul-2022
            craigtrim@gmail.com
            *   https://bast-ai.atlassian.net/browse/COR-8
        Updated:
            5-Aug-2022
            craigtrim@gmail.com
            *   adhere to latest standard on file version
                https://bast-ai.atlassian.net/browse/COR-59
        """
        BaseObject.__init__(self, __name__)
        self._s3 = ConnectToS3().process()
        self._download_files = DownloadFromS3(self._s3).process
        self._read_files = ReadFromS3(self._s3).process
        self._find_latest_version_number = FindLatestVersionNumber(
            self._read_files).process
        self._find_file_by_version = FindFileByVersion(
            self._download_files).process

    def read_files(self,
                   bucket_name: str,
                   file_name: str,
                   load_files: bool = True) -> dict:
        """ Open and Read S3 Files

        Args:
            bucket_name (str): the name of the S3 bucket
            file_name (str): the file name (or prefix) to search for
            load_files (bool): load the contents of the input files
                if None, the keyed value will be None

        Returns:
            dict: a dictionary of file contents keyed by file name
        """
        return self._read_files(
            file_name=file_name,
            bucket_name=bucket_name,
            load_files=load_files)

    def download_files(self,
                       bucket_name: str,
                       file_name: str) -> dict:
        """ Persist S3 Files to Local Directory

        Args:
            bucket_name (str): the name of the S3 bucket
            file_name (str): the file name (or prefix) to search for

        Returns:
            dict: a dictionary of file paths keyed by file name
        """
        return self._download_files(
            file_name=file_name,
            bucket_name=bucket_name)

    def latest_version_number(self,
                              bucket_name: str,
                              file_name: str) -> str or None:
        """ Get the Latest Version of a File

        Args:
            bucket_name (str): the name of the bucket
                e.g., bast-core-data
            file_name (str): the qualified name of the file
                e.g., 'training/myeliza/doctor'

        Returns:
            str or None: the latest version
                e.g., '0.1.2'
        """
        return self._find_latest_version_number(
            bucket_name=bucket_name,
            file_name=file_name)

    def file_by_version(self,
                        bucket_name: str,
                        file_name: str,
                        file_ext: str,
                        version: str = None) -> str:
        """ Download a versioned Bast S3 file to a local directory

        Args:
            bucket_name (str): the name of the bucket
                e.g., bast-core-data
            file_name (str): the qualified name of the file
                e.g., 'training/myeliza/doctor'
            file_ext (str): the file extension
                e.g., 'txt'
            version (str, optional): the version of the file to access
                e.g., '0.1.0'
                if the version is not provided as a parameter, the value will be retrieved from the environment
                    - the file_name will be used as the key
                if the version is not provided in the environment, the value will default to '*'
                    - the use of '*' signifies the service should retrieve the latest version

        Returns:
            str: the local path of the downloaded S3 file
        """

        if not version or not len(version):
            version = EnvIO.str_or_default(file_name, '*')

        if version == '*':
            version = self.latest_version_number(
                bucket_name=bucket_name,
                file_name=file_name)

        return self._find_file_by_version(
            bucket_name=bucket_name,
            file_name=file_name,
            file_ext=file_ext,
            version=version)

    # def ontology_by_version(self,
    #                         bucket_name: str,
    #                         model_name: str,
    #                         version: str) -> dict:
    #     """ Access a Versioned Ontology File

    #     Args:
    #         bucket_name (str): the name of the bucket
    #             e.g., bast-core-data
    #         file_name (str): the non-qualified name of the ontology model
    #             e.g., 'ontologica'
    #         version (str): the version of the file to access
    #             e.g., '0.1.0'

    #     Returns:
    #         str: the absolute path containing both files
    #     """

    #     file_name = f"owl/{model_name}"

    #     owl_path = self.file_by_version(
    #         bucket_name=bucket_name,
    #         file_name=file_name,
    #         file_ext='owl',
    #         version=version)

    #     self.file_by_version(
    #         bucket_name=bucket_name,
    #         file_name=file_name,
    #         file_ext='txt',
    #         version=version)

    #     basename = os.path.basename(owl_path)
    #     base_path = owl_path.split(basename)[0].strip()

    #     return base_path
