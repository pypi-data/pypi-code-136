#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find JPG files on S3 within the 'iceberg-data-core' """


import os

from baseblock import BaseObject
from awsfile_helper import AwsAPI


class FindJpgFile(BaseObject):
    """ Find JPG files on S3 within the 'iceberg-data-core' """

    __api = None

    def __init__(self,
                 book_name: str,
                 chapter: int,
                 page: int):
        """ Change Log

        Created:
            11-Oct-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/awsfile-helper/issues/1

        Args:
            book_name (str): the name of the book
            chapter (int): the chapter
            page (int): the page
        """
        BaseObject.__init__(self, __name__)
        self._page = page
        self._chapter = chapter
        self._book_name = book_name

    def _api(self):
        if not self.__api:
            self.__api = AwsAPI().download_files
        return self.__api

    @staticmethod
    def _fmtint(x: int) -> str:
        if x < 10:
            return f"0{str(x)}"
        return str(x)

    @staticmethod
    def _file_name(chapter: str,
                   page: str) -> str:
        return f"CH{chapter}-PG{page}.jpg"

    def process(self) -> dict:

        # lazy-load method...
        download_files = self._api()

        chapter = self._fmtint(self._chapter)
        page = self._fmtint(self._page)
        file_name = self._file_name(chapter=chapter,
                                    page=page)

        qualified_file_name = f"book/{self._book_name}/{file_name}"
        bucket_name = "iceberg-data-core"

        file_path = download_files(
            bucket_name=bucket_name,
            file_name=qualified_file_name)

        return {
            'path': file_path,
            'chapter': self._chapter,
            'page': self._page,
            'name': file_name
        }
