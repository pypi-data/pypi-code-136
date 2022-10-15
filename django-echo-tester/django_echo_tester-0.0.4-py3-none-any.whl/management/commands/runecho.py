import os
import random
import requests
from time import sleep

from django.core.management.base import BaseCommand
from django.test import override_settings
from django.conf import settings

from echo_tester.settings import simulator_settings
from echo_tester.parsers.response import ResponseParser
from echo_tester.store import StoreManager
from echo_tester import utils



def get_valid_middleware():
    """
        Clean middleware from ones which may cause errors while testing
    """

    testing_middleware = []
    for middleware_name in settings.MIDDLEWARE:
        is_safe_middleware = True

        for keyword in simulator_settings.SKIP_MIDDLEWARE_CONTAIN:
            if keyword in middleware_name:
                is_safe_middleware = False
                break

        if is_safe_middleware:
            testing_middleware.append(middleware_name)

    return list(testing_middleware)


class RequestSimulator:
    def __init__(self):
        # load the request items to simulate
        self.store_items = StoreManager().list_all_items()

        # TODO filter endpoint using user regex

    def __get_request_method_parameters(self, request):
        payload = request['payload']

        request['headers'].pop('Content-Length', '')

        # params of requests.get(**)
        params = {
            'url': request['url'],
            'params': payload['get'],
            'headers': request['headers'],
            'cookies': request['cookies'],
            'files': {
                name: open(path, 'rb')
                for name, path in payload['files'].items()
            },
            'data': payload['post'] or None,
            'json': payload['json'] or None,
        }
        # check if there is data to set
        return params

    def __simulate_request(self, request):
        params = self.__get_request_method_parameters(request)

        http_method = getattr(requests, request["method"].lower())
        response = http_method(**params, allow_redirects=False)

        return response

    def run(self):
        for item in self.store_items:
            stored_request = item.get('request')
            stored_response = item.get('response')
            response_checks = item.get('response_checks')

            response = self.__simulate_request(stored_request)
            parsed_response = ResponseParser(response).parse()

            is_equal = utils.is_equal_dicts(
                stored_response, parsed_response, response_checks
            )

            message = '[%(status_code)d] %(method)s %(path)s (%(store_id)s)' % {
                'status_code': response.status_code,
                'method': response.request.method,
                'path': response.url,
                'store_id': item.get('id'),
            }
            utils.print_(message, state=is_equal)
            utils.print_dicts_equality(stored_response, parsed_response, response_checks)


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # TODO ask for port from settings or just keep it random
        # NOTE it uses the url from the store as it made at first
        self.port = random.randint(10000, 60000)
        self.port = 8000

    def wait_until_server_running(self):
        # make sure server is up and running
        while True:
            try: # just try to ping to the server
                requests.get(f'http://127.0.0.1:{self.port}')
                break
            except Exception:
                sleep(1)

    def runserver(self):
        os.system(f'python manage.py runserver {self.port} > /dev/null &')

    def kill_server(self):
        # TODO check the OS then use the right command to kill port
        os.system(f'kill -9 $(lsof -t -i:{self.port})')

    @override_settings(MIDDLEWARE=get_valid_middleware())
    def simulate(self):
        s = RequestSimulator()
        s.run()

    def handle(self, *args, **options):
        self.kill_server()
        self.runserver()
        self.wait_until_server_running()
        self.simulate()
        self.kill_server()

        exit(0)
