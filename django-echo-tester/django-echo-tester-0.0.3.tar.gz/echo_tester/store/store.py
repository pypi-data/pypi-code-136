import uuid
from functools import partial
from datetime import datetime
from typing import Tuple

from echo_tester import utils
from echo_tester.settings import recorder_settings
from echo_tester.parsers.request import RequestParser, RequestIdentifier
from echo_tester.parsers.response import ResponseParser



class StoreManager:
    '''
    Manage & store the requests to simulate them later
    and check the response saved on it
    '''

    # TODO Try to apply singleton pattern

    def __init__(self, path=None):
        self.store = {}
        self.path = path or recorder_settings.STORE_PATH
        self.request_identifiers = recorder_settings.REQUEST_IDENTIFIERS
        self.response_checks = recorder_settings.RESPONSE_CHECKS

        self.__load()

    def __load(self):
        self.store = utils.read_file_smart(
            self.path, default_data=self.store
        )

    def __write(self):
        utils.write_file_safe(self.path, self.store)

    def save(self, request, response):
        """ Called from the middleware
        It almost uses all methods in the class """

        item_structure = self.build_store_item_structure(request, response)
        is_exist = self.__check_item_exist(item_structure)
        if not is_exist:
            self.__insert_item(item_structure)

        self.__manage_credentials(item_structure)

    def __manage_credentials(self, item_structure):
        endpoint, method, data = item_structure
        request = data['request']

        credentials = CredentialManager(request).get_credentials()
        if credentials is not None:
            self.__update_credentials(credentials)

    def build_store_item_structure(self, request, response) -> Tuple[str, str, dict]:
        parsed_request = RequestParser(request).parse()
        parsed_response = ResponseParser(response).parse()

        request_identifier = RequestIdentifier( parsed_request, self.request_identifiers )

        data = {
            'request': parsed_request,
            'response': parsed_response,

            'request_identifiers': self.request_identifiers,
            'response_checks': self.response_checks,

            'request_hash': request_identifier.get_hash(),
            'id': str(uuid.uuid4()),

            'created_at': str(datetime.now())
        }

        return parsed_request['path'], parsed_request['method'], data

    def __get_endpoint_items(self, endpoint, method):
        return self.store.get(endpoint, {}).get(method, [])

    def __get_endpoint_items_hashes(self, endpoint, method):
        items = self.__get_endpoint_items(endpoint, method)
        return map(lambda i: i['request_hash'], items)

    def __get_endpoint_items_by_hash(self, endpoint, method, hash):
        items = self.__get_endpoint_items(endpoint, method)
        return filter(
            lambda item: item['request_hash'] == hash, items
        )

    def __check_item_exist(self, item_structure):
        endpoint, method, incoming_item = item_structure

        # NOTE hash may be duplicated if response changed
        # Get Equal items if exist 
        equal_items = tuple(self.__get_endpoint_items_by_hash(
            endpoint, method, incoming_item['request_hash']
        ))
        responses = map(lambda item: item['response'], equal_items)

        is_duplicate_checker = partial(utils.is_equal_dicts, incoming_item['response'])
        is_duplicated = any(map(is_duplicate_checker, responses))

        return is_duplicated

    def __insert_item(self, item_structure):
        endpoint, method, incoming_item = item_structure

        items = self.store.get(endpoint, {}).get(method)
        if items is not None:
            items.append(incoming_item)
        else:
            self.store.update({
                endpoint: { method: [incoming_item] }
            })

        self.__write()

    def list_all_items(self):
        all_items = []
        for endpoint, methods in self.store.items():
            for method, items in methods.items():
                all_items.extend(items)

        return all_items

    def __generator_all_items(self):
        for endpoint, methods in self.store.items():
            for method, items in methods.items():
                for item in items:
                    yield item

    def __update_credentials(self, credentials):
        credentials_identifier_key = credentials['identifier_key']
        incoming_credentials_identifier = credentials['identifier']
        incoming_credentials = credentials['credentials']

        is_store_changed = False
        for item in self.__generator_all_items():
            stored_request = item.get('request')
            item_credentials_identifier = utils.get_dict_deep_key(stored_request, credentials_identifier_key)

            # Credentials updated only for the user with the same identifier
            if str(item_credentials_identifier) == str(incoming_credentials_identifier):
                updated_request = utils.bulk_update_dict_deeply(stored_request, incoming_credentials)
                stored_request.update(updated_request)

                is_store_changed = True

        if is_store_changed:
            self.__write()


class CredentialManager:
    """
    set credentials keys in the ConfigManager
    make sure that credential keys never uses for request_hash
    read the user.pk and the credentials list
    compare them with saved ones
      if new -> add them
      else -> 
          not changed -> skip
          changed -> update store (requests from this user) 
              with new credentials
    """
    def __init__(self, parsed_request: dict):
        # parsed request
        self.request = parsed_request
        self.pull_from_request = partial(utils.get_dict_deep_key, parsed_request)

        self.path = recorder_settings.CREDENTIALS_PATH
        self.credentials_keys = recorder_settings.CREDENTIALS_KEYS
        self.identifier_key = recorder_settings.CREDENTIALS_IDENTIFIER_KEY

        self.credentials = {}

        self.__load()

    def __load(self):
        self.credentials = utils.read_file_smart(
            self.path, default_data=self.credentials
        )

    def __write(self):
        utils.write_file_safe(self.path, self.credentials)

    def __extract_credentials(self):
        # in most cases its the pk
        identifier = self.pull_from_request(self.identifier_key)
        if not identifier: return

        current_user_credentials = {
            credential_key: self.pull_from_request(credential_key)
            for credential_key in self.credentials_keys
        }

        return {
            'identifier':str(identifier),
            'identifier_key': self.identifier_key,
            'credentials': current_user_credentials, 
        }

    def __check_credentials_changed(self, current_credentials):
        identifier = current_credentials['identifier']
        current_user_credentials = current_credentials['credentials']
        stored_user_credentials = self.credentials.get(identifier)

        is_new_user = stored_user_credentials is None
        is_changed = None

        if not is_new_user:
            is_equal = utils.is_equal_dicts(stored_user_credentials, current_user_credentials)
            is_changed = not is_equal

        return is_new_user or is_changed

    def __save(self, current_credentials):
        identifier = current_credentials['identifier']
        current_user_credentials = current_credentials['credentials']

        self.credentials[identifier] = current_user_credentials
        self.__write()

    def get_credentials(self):
        incoming_credentials = self.__extract_credentials()
        if incoming_credentials is None:
            return

        is_changed = self.__check_credentials_changed(incoming_credentials)
        if is_changed:
            self.__save(incoming_credentials)
        else:
            incoming_credentials = None

        return incoming_credentials
