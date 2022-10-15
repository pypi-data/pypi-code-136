# manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Open source, MIT license: http://www.opensource.org/licenses/mit-license.php
"""
main app logic

"""
from itertools import chain

from googleapiclient.errors import HttpError

from manuscriptify.filetree import FileTree
from manuscriptify.fragment import Fragment
from manuscriptify.chapter import Chapter
from manuscriptify.outfile import Outfile
from manuscriptify.decorators import run_with_shell_args
from manuscriptify.exceptions import InconvenientResults
from manuscriptify.exceptions import SortKeyError

FILE_MIME = 'application/vnd.google-apps.document'


@run_with_shell_args
def manuscriptify(**kwargs):
    source = kwargs['source']
    try:
        filetree = FileTree(source)
        fragments = []
        for f in filetree:
            try:
                if f['description'].isdigit():
                    chapter_name_frag = Chapter(f['name'])
                    fragments.append(chapter_name_frag)
            except KeyError:

                # single file use case
                pass

            if f['mimeType'] == FILE_MIME:
                fragment = Fragment(f['id'])
                fragments.append(fragment)
        kwargs['content'] = list(chain(*fragments))
        Outfile(**kwargs)
        print(source,
              'was manuscriptified')
    except AttributeError as e:
        app_errors = [InconvenientResults,
                      SortKeyError]
        if type(e) in app_errors:
            pass
        else:
            raise
    except HttpError as e:
        print(e)
        raise


manuscriptify('dummy_arg')
