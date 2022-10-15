# manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Open source, MIT license: http://www.opensource.org/licenses/mit-license.php
"""
fragment assembler

"""
from manuscriptify.exceptions import InconvenientResults
from manuscriptify.exceptions import SortKeyError
from manuscriptify.google_api.clients import Clients

FIELDS = 'id, name, description, parents, mimeType'
FILE_MIME = 'application/vnd.google-apps.document'
FOLDER_MIME = 'application/vnd.google-apps.folder'


class FileTree(tuple):
    """all the relevant files, in their proper order"""

    def __new__(cls, source):
        drive = Clients()['drive']
        ancs, mime_type = cls._ancestors(drive, source)
        files = (cls._files(drive, ancs)
                 if mime_type == FOLDER_MIME
                 else ancs)
        return tuple(files)

    @classmethod
    def _ancestors(cls, drive, source):
        """get all relevant folders"""
        mime_type = FOLDER_MIME
        queries = [
            f"mimeType = '{mime_type}'",
            "'me' in owners",
            'trashed = false'
        ]
        kwargs = {
            'api_method': drive.files().list,
            'q': ' and '.join(queries),
            'pageSize': 100,
            'fields': f'nextPageToken, files({FIELDS})'
        }
        all_folders = cls.get_all_results(**kwargs)
        ancestors = [
            f['id'] for f in all_folders
            if f['name'] == source
        ]
        if len(ancestors) == 1:
            descendants = cls._descendants(ancestors, all_folders)
            ancestors.extend(descendants)
            return ancestors, mime_type
        elif len(ancestors) == 0:
            mime_type = FILE_MIME
            queries = [
                f"mimeType = '{mime_type}'",
                f"name = '{source}'",
                'trashed = false'
            ]
            kwargs['q'] = ' and '.join(queries)
            results = cls.get_all_results(**kwargs)
            if len(results) != 1:
                raise InconvenientResults(results)
            return results, mime_type
        else:
            raise InconvenientResults(ancestors)

    @staticmethod
    def _descendants(ancestors, all_folders):
        """get folders under the project root"""
        descendants = []
        while True:
            next_gen = [f['id'] for f in all_folders if
                        any(a in f['parents'] for
                            a in ancestors)]
            if not next_gen:
                break
            descendants.extend(next_gen)
            ancestors = next_gen
        return descendants

    @classmethod
    def _files(cls, drive, ancestors):
        """get all relevant files"""
        query = [f"'{folder_id}' in parents"
                 for folder_id in ancestors]
        queries = [
            f"({' or '.join(query)})",
            'trashed = false'
        ]
        kwargs = {
            'api_method': drive.files().list,
            'q': ' and '.join(queries),
            'pageSize': 100,
            'fields': f'nextPageToken, files({FIELDS})'
        }
        results = cls.get_all_results(**kwargs)
        prioritized = cls._prioritize(results)
        try:
            files = sorted(prioritized, key=cls._sort_key)
        except (ValueError, KeyError):
            raise SortKeyError(prioritized)
        return files

    @staticmethod
    def get_all_results(api_method, list_key='files', **kwargs):
        """chain all the result pages"""
        all_results = []
        page_token = None
        while True:
            if page_token:
                kwargs['pageToken'] = page_token
            results = api_method(**kwargs).execute()
            all_results.extend(results[list_key])
            if 'nextPageToken' not in all_results:
                break
            page_token = results['nextPageToken']
        return all_results

    @staticmethod
    def _prioritize(results):
        """add ancestor priorities"""
        for i, result in enumerate(results):
            while True:
                parents = [r for r in results if
                           r['id'] in result['parents']]
                if not parents:
                    break
                results[i]['description'] = '{}.{}'.format(parents[0]['description'],
                                                           results[i]['description'])
                result = parents[0]
        return results

    @staticmethod
    def _sort_key(x):
        """float the description field contents"""
        version_key = [
            int(u) for u in
            x['description'].split('.')
        ]
        return version_key
