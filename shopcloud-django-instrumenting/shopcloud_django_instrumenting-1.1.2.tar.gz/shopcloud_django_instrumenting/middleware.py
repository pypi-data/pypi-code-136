import json
import logging


class LogRequestMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)
        return response

    def process_response(self, request, response):
        return response

    def process_request(self, request):
        data = json.dumps({
            'method': request.method,
            'path': request.path,
            'user': str(request.user).lower(),
            'agent': request.META.get('HTTP_USER_AGENT', 'no-agent'),
            'ip': request.headers.get("X-Appengine-User-Ip", 'no-ip'),
        })
        logging.info(f'djlog {data}')
