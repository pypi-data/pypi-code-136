#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Avoid and S3 call and Read File direct from Cache """


import os

from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject


class ReadFromCache(BaseObject):
    """ Avoid and S3 call and Read File direct from Cache """

    def __init__(self):
        """ Change Log

        Created:
            6-Aug-2022
            craigtrim@gmail.com
            *   https://bast-ai.atlassian.net/browse/COR-72
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def _construct_local_path(file_path: str) -> str:
        if file_path:
            FileIO.exists_or_create(file_path)
            return file_path
        return FileIO.local_directory_by_name('BastAI')

    @staticmethod
    # TODO: replace with baseblock function in 0.1.5
    def normpath(path: str) -> str:
        """ Normalize Path to use forward slashes

        This differs from
            os.path.normpath
        in that the Python std lib call will normalize on a platform-specific basis

        This means a path like this
            alpha/bravo/charlie
        will become
            alpha\\bravo\\charlie
        on a Windows platform; which is silly, because forward slashes work just fine on Windows

        Args:
            path (str): the incoming path

        Returns:
            str: the outgoing path
        """
        if '\\' in path:
            path = path.replace('\\', '/')
            os.path.normpath
        return path

    def process(self,
                file_name: str,
                file_ext: str,
                file_version: str) -> dict or None:
        sw = Stopwatch()

        file_name = self.normpath(file_name)

        file_path = file_name
        file_name = f"{file_name.split('/')[-1]}-{file_version}.{file_ext}"

        cached_copy = os.path.normpath(os.path.join(
            FileIO.local_directory_by_name('BastAI'),
            file_path, file_version, file_name))

        if FileIO.exists(cached_copy):

            if self.isEnabledForDebug:
                self.logger.debug('\n'.join([
                    "Cached Read Completed",
                    f"\tFile Name: {file_name}",
                    f"\tTotal Time: {str(sw)}",
                    "\tTotal Files: 1"]))

            return cached_copy
