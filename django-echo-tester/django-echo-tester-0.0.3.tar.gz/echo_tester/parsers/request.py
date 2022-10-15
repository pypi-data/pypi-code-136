import json

from django.core.files.storage import default_storage

from echo_tester import utils
from echo_tester.settings import recorder_settings



class RequestParser:
    def __init__(self, request):
        self.request = request

    def __get_user(self):
        return {
            'user': {
                'is_authenticated': self.request.user.is_authenticated,
                'is_staff': self.request.user.is_staff,
                'username': self.request.user.username,
                'id': self.request.user.id,
                'pk': self.request.user.pk,
            }
        }

    def __get_payload_files(self):
        # save image in folder and set string path instead
        files = self.request.FILES.dict()
        new_files = {}
        for field_name, file in files.items():
            file_path = utils.join_path(recorder_settings.STORE_FILES_DIR, file.name)
            file_path = default_storage.path(file_path)
            file_path = default_storage.save(file_path, file)

            new_files[field_name] = file_path

        return new_files

    def __get_payload_json(self):
        # TODO see if this is work
        # test this with rest_framework and see if body exist etc...
        body = self.request.body
        if isinstance(body, bytes):
            try:
                body = body.decode('utf8')
            except UnicodeDecodeError:
                # it maybe a file
                pass

        if self.request.headers['content-type'] == 'application/json':
            body = json.loads(body) if isinstance(body, str) else None
        else:
            body = None

        return body

    def __get_payload(self):
        return {
            'payload': {
                'files': self.__get_payload_files(),
                # url params
                'get': self.request.GET.dict(),
                # form params
                'post': self.request.POST.dict(),
                # json and more
                'json': self.__get_payload_json(),
            }
        }

    def __get_url_info(self):
        return {
            'path': self.request.path,
            # TODO temporary until i solve the other problems
            'url': self.request.build_absolute_uri().split('?')[0],
            'scheme': self.request.scheme,
        }

    def __get_header_info(self):
        headers = eval(f'{self.request.headers}')
        headers.pop('Cookie', '')
        headers.pop('Content-Length', '')

        return {
            'cookies': self.request.COOKIES,
            'method': self.request.method,
            'headers': headers,
        }

    def parse(self):
        return {
            **self.__get_url_info(),
            **self.__get_header_info(),
            **self.__get_payload(),
            **self.__get_user()
        }


class RequestIdentifier:
    """ This class convert a dict -> hash string using a list of keys """
    def __init__(self, parsed_request: dict, identifiers: list=None):
        self.parsed_request = parsed_request
        self.identifiers_keys = self.__get_identifiers_keys(
            identifiers or recorder_settings.REQUEST_IDENTIFIERS
        )
        self.hash_value_pipes = [
            lambda val: '' if val is None else val,
            str,
            lambda val: val.split(';')[0] if val.startswith('multipart/form-data;') else val,
        ]

    def __get_identifiers_keys(self, identifiers: list) -> list:
        """Check passed identifiers and Convert alias keys if exist"""

        if not identifiers:
            raise Exception(
                'Please set `REQUEST_IDENTIFIERS` so we can track the requests duplication'
            )

        identifiers_keys = set()

        # if key is alias -> translate it
        for identifier in identifiers:
            alias_to = recorder_settings.ALIAS_REQUEST_IDENTIFIERS.get(identifier)

            if alias_to is None: 
                identifiers_keys.add(identifier)
            else:
                identifiers_keys.update(alias_to)

        return identifiers_keys

    def get_hash(self):
        return utils.identify_dict(
            self.parsed_request, self.identifiers_keys, self.hash_value_pipes
        )
