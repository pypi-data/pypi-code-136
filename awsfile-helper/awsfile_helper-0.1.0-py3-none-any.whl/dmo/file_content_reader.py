#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Reader for File Contents """


from baseblock import FileIO
from baseblock import BaseObject


class FileContentReader(BaseObject):
    """ Generic Reader for File Contents """

    def __init__(self):
        """ Change Log

        Created:
            6-Aug-2022
            craigtrim@gmail.com
            *   refactored out of 'find-s3-file' in pursuit of
                https://bast-ai.atlassian.net/browse/COR-72
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                file_path: str,
                file_ext: str) -> object:

        if file_ext in ['yaml', 'yml']:
            return FileIO.read_yaml(file_path)

        elif file_ext in ['txt', 'text', 'csv', 'tsv', 'owl']:
            return FileIO.read_lines(file_path)

        elif file_ext in ['json']:
            return FileIO.read_json(file_path)

        raise NotImplementedError(file_path)
