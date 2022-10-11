#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Writer for File Contents """


from baseblock import FileIO
from baseblock import BaseObject


class FileContentWriter(BaseObject):
    """ Generic Writer for File Contents """

    def __init__(self):
        """ Change Log

        Created:
            6-Aug-2022
            craigtrim@gmail.com
            *   refactored out of 'persist-from-s3' in pursuit of
                https://bast-ai.atlassian.net/browse/COR-72
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                file_data: object,
                file_path: str,
                file_ext: str) -> None:

        if file_ext in ['txt', 'owl', 'csv', 'tsv']:
            FileIO.write_string(
                input_text=file_data, file_path=file_path)

        elif file_ext in ['json', 'yaml', 'yml']:
            FileIO.write_json(data=file_data, file_path=file_path)

        elif file_ext in ['jpg', 'png']:
            print (file_data)
            with open(file_path, 'wb') as f:
                f.write(file_data)

        else:
            raise NotImplementedError(file_ext)
