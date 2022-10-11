#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Read from an S3 Bucket """


import boto3
import botocore

from boto3.resources.factory import ServiceResource
from botocore import errorfactory

from baseblock import FileIO
from baseblock import BaseObject
from yaml import load


class S3BucketReader(BaseObject):
    """ Read from an S3 Bucket """

    def __init__(self,
                 s3: ServiceResource):
        """ Change Log

        Created:
            25-Jul-2022
            craigtrim@gmail.com
            *   in pursuit of
                https://bast-ai.atlassian.net/browse/COR-11
        """
        BaseObject.__init__(self, __name__)
        self._s3 = s3

    def process(self,
                bucket_name: str,
                file_name: str,
                load_files: bool) -> dict or None:
        """ Open and Read S3 Files

        Args:
            bucket_name (str): the name of the S3 bucket
            file_name (str): the file name (or prefix) to search for
            load_files (bool): load the contents of the input files
                if None, the keyed value will be None

        Returns:
            dict: a dictionary of file contents keyed by file name
        """

        # BUCKET_NAME = 'my-bucket' # replace with your bucket name
        # KEY = 'my_image_in_s3.jpg' # replace with your object key

        # s3 = boto3.resource('s3')
        file_path = FileIO.join(
            FileIO.local_directory_by_name('Graffl'), file_name)

        # try:
        #     s3.Bucket(bucket_name).download_file(file_name, file_path)
        # except botocore.exceptions.ClientError as e:
        #     if e.response['Error']['Code'] == "404":
        #         print("The object does not exist.")
        #     else:
        #         raise

        # if load_files:

        # # try:
        s3_bucket = self._s3.Bucket(bucket_name)

        files = [x for x in s3_bucket.objects.filter(Prefix=file_name)]

        d_files = {}
        for file in files:

            if not load_files:  # consumer just wants file paths, not contents
                d_files[file.key] = None
                continue

            if file.key.endswith('jpg') or file.key.endswith('png'):
                
                file.download_file(file_name, file_path)

                raise ValueError('bp1')

            data = file.get()['Body'].read().decode(encoding="utf-8",
                                                    errors="ignore")

            if file.key.endswith('.yaml') or file.key.endswith('.yml'):
                data = FileIO.parse_yaml(data)
            elif file.key.endswith('json'):
                data = FileIO.parse_json(data)

            d_files[file.key] = data

        return d_files

        # except Exception as e:
        #     self.logger.error(e)
        #     self.logger.error('\n'.join([
        #         "S3 Bucket Not Found",
        #         f"\tBucket Name: {bucket_name}",
        #         f"\tTarget File: {file_name}"]))
        #     return None
