import json
import requests
import django

from echo_tester.settings import recorder_settings


class ResponseParser:
    def __init__(self, response):
        self.response = response

    def __get_data(self):
        content_type, *charset = self.response.headers \
            .get('Content-Type') \
            .replace(' ', '') \
            .split(';', 1)

        charset = charset[0] if charset else 'utf8'

        # charset = 'utf8'
        data = self.response.content

        if content_type == 'application/json':
            data = data.decode(charset)
            data = json.loads(data)
        elif recorder_settings.DROP_HTML_FROM_RESPONSE:
            data = recorder_settings.DROP_MESSAGE
        elif content_type == 'text/html':
            data = data.decode(charset)
        else:
            try:
                data = data.decode(charset)
            except Exception:
                data = None

        return {
            'data': data,

            'content_length': self.response.headers.get('Content-Length'),
            'content_encoding': self.response.headers.get('Content-Encoding'),
            'content_type': self.response.headers.get('Content-Type'),
        }

    def __get_cookies_dict(self, response):
        cookies_dict = {}
        if isinstance(response, requests.models.Response):
            cookies_dict = response.cookies.get_dict()
        elif isinstance(response, django.http.response.HttpResponse):
            cookies_dict =  {k: v.value for k, v in response.cookies.items()}

        return cookies_dict

    def __get_headers(self):
        headers = eval(str(self.response.headers))
        headers.pop('Set-Cookie', '')

        return {
            'status_code': self.response.status_code,
            # in case its requests.response && its not working in django response
            'cookies': self.__get_cookies_dict(self.response),
            'headers': headers,
        }

    def parse(self):
        return {
            **self.__get_headers(),
            **self.__get_data()
        }


