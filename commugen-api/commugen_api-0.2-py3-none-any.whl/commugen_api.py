import base64

import requests

from commugen_api.response_objects import CommugenModel, CommugenDomains, CommugenTables, CommugenSingleRecord, \
    CommugenOptions

MAX_COUNT = 100


class CommugenException(Exception):

    def __init__(self, code=None, id=None, description=None, **kwargs):
        self.code = code
        self.id = id
        self.description = description
        self.kwargs = ', '.join(f'{k}: {v}' for k, v in kwargs.items())

    def __str__(self):
        return 'http status: {0}, id: {1} - {2}, {3}'.format(
            self.code, self.id, self.description, self.kwargs)


class CommugenAPI:

    def __init__(self, user, password, host, port, **kwargs):
        self.prefix = f'https://{host}:{port}/v0'
        self.headers = self._authentication_header(user, password)
        self._session = requests.api
        self.verify = kwargs.pop('verify', True)

    def _authentication_header(self, user, password):
        message = f'{user}:{password}'
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return {'Authorization': f'Basic {base64_message}'}

    def _send_request(self, method, url, params=None, json=None):

        try:
            response = self._session.request(method=method,
                                             url=url,
                                             headers=self.headers,
                                             params=params,
                                             json=json,
                                             verify=self.verify
                                             )
            response.raise_for_status()
            results = response.json()
        except requests.exceptions.HTTPError as http_error:
            response = http_error.response
            json_response = response.json()
            error = json_response.get("error", {})
            raise CommugenException(
                **error
            )
        return results

    def get_model(self, domain, model, published=True, f='', **kwargs):

        if published:
            f = ' '.join([f, '_publicState.eq.0'])

        if f:
            f = f.split()
            kwargs = list(kwargs.items()) + [('f', filter) for filter in f]

        url = '/'.join([self.prefix, domain, model])
        response = self._send_request(method='GET', url=url, params=kwargs)
        return CommugenModel(response)

    def get_entry(self, domain, model, id):
        url = '/'.join([self.prefix, domain, model, str(id)])
        response = self._send_request(method='GET', url=url)
        return CommugenSingleRecord(response)

    def add_entry(self, domain, model, payload):
        url = '/'.join([self.prefix, domain, model])
        response = self._send_request(method='POST', url=url, json=payload)
        return CommugenSingleRecord(response)

    def update_entry(self, domain, model, id, payload):
        url = '/'.join([self.prefix, domain, model, str(id)])
        response = self._send_request(method='PUT', url=url, json=payload)
        return CommugenSingleRecord(response)

    def get_full_table(self, domain, model, **kwargs):

        table = self.get_model(domain=domain, model=model, count=MAX_COUNT, **kwargs)
        offset = MAX_COUNT
        while table.records.hasMore:
            extention = self.get_model(domain=domain, model=model, count=MAX_COUNT, offset=offset, **kwargs)
            table.records.list.extend(extention.records.list)
            table.records.hasMore = extention.records.hasMore
            offset += MAX_COUNT
        return table

    def get_domains(self):
        response = self._send_request('GET', self.prefix)
        return CommugenDomains(response)

    def get_models(self, domain):
        url = '/'.join([self.prefix, domain])
        response = self._send_request('GET', url)
        return CommugenTables(response)

    def get_options(self, domain, model, id=''):
        url = '/'.join([self.prefix, domain, model, str(id)])
        response = self._send_request('OPTIONS', url)
        return CommugenOptions(response)