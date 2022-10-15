# manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Open source, MIT license: http://www.opensource.org/licenses/mit-license.php
"""
file generator

"""
from manuscriptify.parser import Parser
from manuscriptify.formatter import Formatter
from manuscriptify.filetree import FOLDER_MIME
from manuscriptify.google_api.clients import Clients

TEMPLATE = '1CRtUdlrV7PZ2OwTDIBZtOKhMHT-nRHCjkaD6Q4lUFkU'
docs, drive = Clients().values()


class Outfile:
    """the outfile generator"""

    def __init__(self, **kwargs):
        """compose a google doc out of the assembled content"""
        self.kwargs = kwargs
        filename = kwargs['source']
        doc_id = self._create_from_template(filename)
        kwargs_ = {
            'documentId': doc_id
        }
        doc = docs.documents().get(**kwargs_).execute()
        style = doc['documentStyle']
        kwargs['header_id'] = style['defaultHeaderId']
        requests = Parser(**kwargs)
        kwargs_['body'] = {
            'requests': requests
        }
        docs.documents().batchUpdate(**kwargs_).execute()
        kwargs = {
            'header_id': style['firstPageHeaderId'],
            'wc': requests.wc
        }
        kwargs_['body'] = {
            'requests': self._wc(**kwargs)
        }
        docs.documents().batchUpdate(**kwargs_).execute()
        o_id = self._get_outfolder()
        kwargs = {
            'fileId': doc_id,
            'addParents': o_id,
            'body': {'name': self.kwargs['title']}
        }
        drive.files().update(**kwargs).execute()

    @staticmethod
    def _create_from_template(filename):
        """copy the empty template document"""
        kwargs = {
            'fileId': TEMPLATE
        }
        file = drive.files().copy(**kwargs).execute()
        return file['id']

    @staticmethod
    def _wc(**kwargs):
        """add the word count header"""
        end_index = len(f'{kwargs["wc"]:,}') + 12
        header = [{
            'insertText': {
                'location': {
                    'segmentId': kwargs['header_id'],
                    'index': 0
                },
                'text': (f'Word count: {kwargs["wc"]:,}')
            }
        }]
        range_ = {
            'startIndex': 0,
            'endIndex': end_index,
            'segmentId': kwargs['header_id']
        }
        ts = Formatter.matter()
        header.append({
            'updateTextStyle': {
                'range': range_,
                'textStyle': ts,
                'fields': ','.join(ts.keys())
            }
        })
        st = Formatter.right()
        header.append({
            'updateParagraphStyle': {
                'range': range_,
                'paragraphStyle': st,
                'fields': ','.join(st.keys())
            }
        })
        return header

    @staticmethod
    def _get_outfolder():
        """get the folder we want to put stuff in"""
        queries = [
            f"mimeType = '{FOLDER_MIME}'",
            "name = 'manuscriptify'",
            'trashed = false'
        ]
        kwargs = {
            'q': ' and '.join(queries),
            'pageSize': 1,
            'fields': 'files(id)'
        }
        results = drive.files().list(**kwargs).execute()
        if results['files']:
            f = results['files'][0]
        else:
            kwargs = {
                'body': {
                    'name': 'manuscriptify',
                    'mimeType': FOLDER_MIME
                },
                'fields': 'id'
            }
            f = drive.files().create(**kwargs).execute()
        return f['id']
